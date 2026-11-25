"""依原收集規則補收 EMA 現行清單有、證據包沒收的集中許可（2026-11-25 第五輪，用戶決定；全程不用 AI）。

問題：證據包的許可是 collectors/nofda.py 收的：藥名 → DrugBank ID → data/processed/drug_mapping.csv（2026-03 EMA medicines report
逐成分對 DrugBank，scripts/run_kg_prediction.py 的 map_fda_drugs_to_drugbank）→ 許可號。drug_mapping 是 2026-03 那份清單做的，
之後 EMA 新核准的集中許可（例 pegfilgrastim 的 EMEA/H/C/006085、006937）不在 drug_mapping，每週排程（license_adapter）只更新既有號碼的狀態，
永遠收不進來，張數落後。

做法（規則跟原收集器相同，不放寬）：
- 讀 EMA medicines report（--download 下載現行版並存到 data/raw/ema_medicines_report_current.xlsx，讓 Release 帶著；或 --xlsx 給檔案）。
- 候選＝不在 drug_mapping.csv 的產品號碼、Medicine status 不在 config/fields.yaml 的 withdrawn_statuses、有 Active substance
  （＝loader.filter_active_drugs 的條件）；本站 2026-03 基準清單（data/raw/<cc>_fda_drugs.json）只收 Authorised 的（FI、NO 的
  process_fda_data.py 只留 Human＋Authorised），候選也只收 Authorised；獸用（EMEA/V/）只在基準清單本來就收獸用時才收（DE）。
- 候選用同一支 map_fda_drugs_to_drugbank（同一份 drugbank_vocab、同樣的 config 欄位）對 DrugBank ID；證據包 tfda.drugbank_ids 有交集、
  號碼不在證據包（records、veterinary_records、excluded_records、records_not_stored）的就補一筆，欄位照收集器 _format，
  另記 source（清單日期與規則）、added（補收日）。
- 人用（EMEA/H/）進 records（原收集器最多存 20 筆；超過的只記在 records_not_stored 並算進 total_matches）；獸用進 veterinary_records
  （不算進人用張數，同 license_adapter.preprocess 的 EXCLUDE_VET）。
- 只加不刪、可重複執行（已收的號碼不重收）。狀態照清單原文（之後由每週排程照常更新）。
- 證據包讀不到就停（不當成沒有紀錄）；清單少於 1,500 筆或找不到表頭就停。

用法（repo 根目錄）：python3 scripts/add_current_ema_products.py [--download | --xlsx 檔] [--dry-run] [--report out.tsv]
每週排程（.github/workflows/license-refresh.yml）在 license_refresh 前以 --download 跑；有補收就照常發新 Release。
"""
import datetime
import importlib
import io
import json
import re
import sys
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))
URL = "https://www.ema.europa.eu/en/documents/report/medicines-output-medicines-report_en.xlsx"
SAVE = ROOT / "data" / "raw" / "ema_medicines_report_current.xlsx"
BUNDLES = ROOT / "data" / "bundles"
MAPPING = ROOT / "data" / "processed" / "drug_mapping.csv"
CAP = 20  # 原收集器 _format 存的筆數上限
MIN_ROWS = 1500


def pkg():
    return next(p.name for p in (ROOT / "src").iterdir() if p.is_dir() and p.name.endswith("txgnn"))


def download():
    import requests
    for attempt in range(4):
        try:
            r = requests.get(URL, timeout=180, headers={"User-Agent": "Mozilla/5.0 (compatible; TxGNN/1.0; research)"})
            r.raise_for_status()
            SAVE.parent.mkdir(parents=True, exist_ok=True)
            SAVE.write_bytes(r.content)
            return SAVE
        except Exception:
            if attempt == 3:
                raise
            time.sleep(15 * (attempt + 1))


def read_report(path):
    import openpyxl
    ws = openpyxl.load_workbook(io.BytesIO(Path(path).read_bytes()), read_only=True).active
    head, out = None, []
    for row in ws.iter_rows(values_only=True):
        if head is None:
            if row and "EMA product number" in row and "Medicine status" in row:
                head = [str(h or "").strip() for h in row]
            continue
        rec = {h: ("" if v is None else str(v).strip()) for h, v in zip(head, row) if h}
        if rec.get("EMA product number"):
            out.append(rec)
    if head is None:
        raise SystemExit("找不到表頭（EMA product number／Medicine status），疑似格式改變，不補收")
    if len(out) < MIN_ROWS:
        raise SystemExit(f"清單只有 {len(out)} 筆，疑似格式改變，不補收")
    return out


def main(argv):
    import csv
    import pandas as pd
    dry = "--dry-run" in argv
    rep = argv[argv.index("--report") + 1] if "--report" in argv else None
    if "--download" in argv:
        path = download()
    elif "--xlsx" in argv:
        path = Path(argv[argv.index("--xlsx") + 1])
    else:
        raise SystemExit("要給 --download 或 --xlsx <檔>")
    P = pkg()
    loader = importlib.import_module(f"{P}.data.loader")
    mapper = importlib.import_module(f"{P}.mapping.drugbank_mapper")
    cfg = loader.load_config()
    fm = cfg["field_mapping"]
    withdrawn = set(cfg.get("withdrawn_statuses") or [])
    today = datetime.date.today().isoformat()
    xdate = datetime.date.fromtimestamp(Path(path).stat().st_mtime).isoformat()
    rows = read_report(path)

    with open(MAPPING, encoding="utf-8-sig", newline="") as f:
        mapped = {str(r.get("license_id") or "").strip() for r in csv.DictReader(f)}
    base_raw = sorted(p for p in (ROOT / "data" / "raw").glob("*_fda_drugs.json") if not p.name.startswith("._"))
    base = json.loads(base_raw[0].read_text(encoding="utf-8")) if base_raw else []
    take_vet = any(str(r.get("EMA product number") or "").startswith("EMEA/V/") for r in base)
    # 基準清單的收錄範圍：FI／NO 的 process_fda_data.py 只留 Human＋Authorised，DE 收全部狀態（再由 withdrawn_statuses 濾）
    only_auth = bool(base) and {str(r.get("Medicine status") or "") for r in base} <= {"Authorised"}

    lid, ing, st = fm["license_id"], fm["ingredients"], fm["status"]
    cand = [r for r in rows if r[lid] not in mapped and r.get(st) not in withdrawn and r.get(ing)
            and (not only_auth or r.get(st) == "Authorised")
            and (r[lid].startswith("EMEA/H/") or (take_vet and r[lid].startswith("EMEA/V/")))]
    by_lic = {r[lid]: r for r in cand}
    mres = mapper.map_fda_drugs_to_drugbank(pd.DataFrame(cand), field_mapping={
        "license_id": lid, "brand_name": fm.get("brand_name_local", ""), "ingredients": ing}) if cand else pd.DataFrame()
    db_to_new = {}
    for _, m in mres.iterrows():
        if m.get("mapping_success") and m.get("drugbank_id"):
            db_to_new.setdefault(str(m["drugbank_id"]).upper(), set()).add(str(m["license_id"]))

    def g(r, k):
        c = fm.get(k) or ""
        return str(r.get(c, "") or "").strip() if c else ""

    src = f"EMA medicines report ({xdate}; not in the 2026-03 drug_mapping, matched to DrugBank with the same rule as the original collector)"
    out, nb, nrec, nvet = [], 0, 0, 0
    for f in sorted(BUNDLES.glob("*/drug_bundle.json")):
        try:
            b = json.loads(f.read_text(encoding="utf-8"))
        except Exception as e:
            raise SystemExit(f"讀不到證據包 {f}：{e}")  # 讀不到資料就停，不當成沒有紀錄
        tf = b.get("tfda")
        if not isinstance(tf, dict):
            continue
        ids = {str(x).upper() for x in (tf.get("drugbank_ids") or [])}
        new = sorted({l for db in ids for l in db_to_new.get(db, ())})
        if not new:
            continue
        have = {str(r.get("license_id") or "") for k in ("records", "veterinary_records", "excluded_records") for r in (tf.get(k) or [])}
        have |= {str(x) for x in tf.get("records_not_stored") or []}
        recs, vet = list(tf.get("records") or []), list(tf.get("veterinary_records") or [])
        not_stored = list(tf.get("records_not_stored") or [])
        total = tf.get("total_matches") if isinstance(tf.get("total_matches"), int) else len(recs)
        added = []
        for l in new:
            if l in have:
                continue
            r = by_lic[l]
            rec = {"license_id": g(r, "license_id"), "brand_name_zh": g(r, "brand_name_local"), "brand_name_en": g(r, "brand_name_en"),
                   "ingredients": g(r, "ingredients"), "indication": g(r, "indication"), "dosage_form": g(r, "dosage_form"),
                   "manufacturer": g(r, "manufacturer"), "license_holder": g(r, "manufacturer"), "approval_date": g(r, "approval_date"),
                   "expiry_date": "", "status": g(r, "status"), "source": src, "added": today}
            if l.startswith("EMEA/V/"):
                vet.append(dict(rec, note="veterinary; excluded from human licence counts"))
                where = "veterinary"
                nvet += 1
            else:
                total += 1
                if len(recs) < CAP:
                    recs.append(rec)
                    where = "records"
                else:
                    not_stored.append(l)
                    where = "not_stored"
            have.add(l)
            added.append(l)
            out.append(f"{f.parent.name}\t{l}\t{rec['brand_name_zh']}\t{where}\t{rec['status']}\t{rec['ingredients']}")
        if not added:
            continue
        nb += 1
        nrec += len(added)
        tf.update(records=recs, total_matches=total, found=bool(recs) or bool(tf.get("found")))
        if vet:
            tf["veterinary_records"] = vet
        if not_stored:
            tf["records_not_stored"] = not_stored
        if not dry:
            f.write_text(json.dumps(b, ensure_ascii=False, indent=2), encoding="utf-8")
    if rep:
        Path(rep).write_text("page\tlicense_id\tproduct\twhere\tstatus\tingredients\n" + "\n".join(out) + "\n", encoding="utf-8")
    print(f"清單 {len(rows)} 筆，不在 drug_mapping 的現行候選 {len(cand)} 筆、對到 DrugBank {sum(len(v) for v in db_to_new.values())} 筆（獸用{'收' if take_vet else '不收'}；{'只收 Authorised' if only_auth else '狀態照 withdrawn_statuses 濾'}）")
    print(f"{'（試跑）' if dry else ''}依原規則補收：{nb} 個證據包、{nrec} 筆（獸用 {nvet} 筆）")


if __name__ == "__main__":
    main(sys.argv[1:])
