"""EMA 集中許可（DE、FI、NO、EU 四站共用；2026-10-30）。各站 license_adapters/<站>.py 是本檔的複本，推廣時一起複製。

來源：EMA medicines report（https://www.ema.europa.eu/en/documents/report/medicines-output-medicines-report_en.xlsx，免金鑰）。
表頭列含「EMA product number」「Medicine status」（前面有說明列，自動找表頭）。人用與獸用都取：
DE 的證據包混有獸用集中許可（EMEA/V/C，原本的資料問題，另案處理），狀態一樣要追。
證據包紀錄 license_id＝EMA product number（EMEA/H/C/xxxxxx）、status＝Medicine status 原文
（Authorised／Withdrawn／Lapsed／Expired／Revoked／Suspended／Refused…）；reviewer 依文字判定。新檔沒有的編號保留原狀態。
"""
import io
import time

import openpyxl
import requests

RAW_FILE = "raw/ema_medicine_status.json"
# 獸用集中許可（EMEA/V/C）移出人用藥的許可證計算（pm 2026-10-30；狀態列寫法 pm 選 b，見 check_drug_page.NO_CENTRAL）。
EXCLUDE_VET = True
URL = "https://www.ema.europa.eu/en/documents/report/medicines-output-medicines-report_en.xlsx"


def fetch():
    for attempt in range(4):
        try:
            r = requests.get(URL, timeout=180, headers={"User-Agent": "Mozilla/5.0 (compatible; TxGNN/1.0; research)"})
            r.raise_for_status()
            break
        except Exception:
            if attempt == 3:
                raise
            time.sleep(15 * (attempt + 1))
    ws = openpyxl.load_workbook(io.BytesIO(r.content), read_only=True).active
    head, out = None, []
    for row in ws.iter_rows(values_only=True):
        if head is None:
            if row and "EMA product number" in row and "Medicine status" in row:
                head = list(row)
            continue
        rec = dict(zip(head, row))
        k = str(rec.get("EMA product number") or "").strip()
        if k:
            out.append({"ema": k, "status": str(rec.get("Medicine status") or "").strip()})
    if head is None:
        raise RuntimeError("找不到表頭（EMA product number／Medicine status）")
    return out


def validate(new, old):
    p = []
    if len(new) < 1500:
        p.append(f"只解析出 {len(new)} 筆，疑似格式改變")
    if sum(1 for r in new if not r["status"]) > 0.01 * max(1, len(new)):
        p.append("超過 1% 缺 Medicine status")
    if old and len(new) < 0.9 * len(old):
        p.append(f"筆數 {len(new)} 比上次 {len(old)} 少超過 10%")
    return p


def status_index(new):
    return {r["ema"]: r["status"] for r in new if r["status"]}


def record_id(rec):
    return str(rec.get("license_id") or "").strip()


def update(rec, new):
    if rec.get("status") == new:
        return False
    rec["status"] = new
    return True


def preprocess(bundle):
    """把獸用集中許可移到 tfda.veterinary_records（保留原紀錄、不刪），total_matches 同步扣除；有移動回 True"""
    if not EXCLUDE_VET:
        return False
    tf = bundle.get("tfda") or {}
    recs = tf.get("records") or []
    vet = [r for r in recs if str(r.get("license_id") or "").startswith("EMEA/V/")]
    if not vet:
        return False
    tf["records"] = [r for r in recs if r not in vet]
    tf["veterinary_records"] = (tf.get("veterinary_records") or []) + [dict(r, note="veterinary; excluded from human licence counts") for r in vet]
    if isinstance(tf.get("total_matches"), int):
        tf["total_matches"] = max(0, tf["total_matches"] - len(vet))
    return True


# 2026-11-24（用戶決定「程式產生許可證表」）：每週排程（license_refresh_20261029.py 的 sync_tables 掛鉤）在概覽表同步之後，
# 依證據包把市場段落的程式許可證表重排（scripts/sync_license_tables.py --bundles；只寫有變的頁）。
# PAGE_NOTE：排程 3b 自我檢查允許的非表格列（程式區塊標記、來源句、Tabellen viser 句、沒有集中許可的說明句；2026-11-24 第三輪起含補的市場段落標題）。
def _slt(site_dir):
    import importlib.util
    from pathlib import Path
    s = importlib.util.spec_from_file_location("sync_license_tables", Path(site_dir) / "scripts" / "sync_license_tables.py")
    m = importlib.util.module_from_spec(s)
    s.loader.exec_module(m)
    return m


def sync_tables(site_dir, bundles):
    """回傳 [(頁, 欄位, 前值, 後值)]；所有有證據包的頁都比對（只寫內容有變的），不只 bundles 列出的藥"""
    import difflib
    from pathlib import Path
    m = _slt(site_dir)
    drugs = Path(site_dir) / "docs" / "_drugs"
    before = {p.name: p.read_text(encoding="utf-8") for p in drugs.glob("*.md")}
    out = []
    for name in m.run(from_bundles=True):
        new = (drugs / name).read_text(encoding="utf-8")
        for l in difflib.unified_diff(before[name].split("\n"), new.split("\n"), lineterm="", n=0):
            if l[:1] in "+-" and not l.startswith(("+++", "---")) and l[1:].startswith("|"):
                out.append((name[:-3], "Lisenstabell (programgenerert)", l[1:] if l[0] == "-" else "", l[1:] if l[0] == "+" else ""))
    return out


try:
    import importlib.util as _ilu
    from pathlib import Path as _P
    _s = _ilu.spec_from_file_location("_slt_note", _P(__file__).resolve().parent / "sync_license_tables.py")
    _m = _ilu.module_from_spec(_s)
    _s.loader.exec_module(_m)
    PAGE_NOTE = _m.PAGE_NOTE
except Exception:  # 站上的 license_adapter 被母目錄當模組載入時，路徑一定在 scripts/ 下；這裡只防萬一
    PAGE_NOTE = r"^<!-- licenses:(begin|end) -->$"
