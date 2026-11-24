#!/usr/bin/env python3
"""市場段落的許可證表由程式產生（2026-11-24，用戶決定「程式產生許可證表」；範本 DETxGNN／FITxGNN 同名檔（同為 EMA 資料）、
UkTxGNN／SgTxGNN 同名檔、ZaTxGNN sync_license_pages.py）。

為什麼：市場段落的許可證表原本是 AI 寫的自由格式表（多數表頭「Godkjenningsnummer／Tillatelsesnummer／Autorisasjonsnummer／Lisensnummer |
Produktnavn | Doseringsform／Legemiddelform | Godkjent indikasjon」，適應症格是 AI 翻成挪威文的 EMA 治療領域；known_use_pages 的表
「Tillatelse | Produkt | Legemiddelform | Status」）。EMA 資料每週變，AI 表不會跟著改，跟事實矛盾時 checker 擋整頁
（2026-11-12 以 no-row 紀錄人工更正過 6 列）。改成程式依證據包（data/bundles 的 tfda.records＝EMA 集中許可，人用；獸用 EMEA/V/C
已由 license_adapter.preprocess 移到 veterinary_records，不列）產生，每週排程（license_adapter.sync_tables）自動同步。

表的內容（全程不用 AI；用戶 2026-11-24 決定欄位照主管機關原文、不翻譯，表頭註明語言）：
  | Godkjenningsnummer | Preparatnavn (EMA) | Virkestoff(er) (EMA, engelsk) | Terapeutisk område (EMA, engelsk) | Status |
  狀態欄照 EMA Medicine status 轉成本站寫法（Authorised→Gyldig、Withdrawn→Trukket tilbake…，STATUS_NO；本站頁面原本就用 Gyldig）；
  排序：有效在前，同狀態依 EMA 號碼；最多 MAX_ROWS 列（證據包只收前 20 筆的 partial 頁多一句 SHOW）。
  表後一行來源句（SOURCE）；本藥沒有人用集中許可時整個區塊只有 NONE_LINE 一行。
  區塊前後各一行 <!-- licenses:begin --> <!-- licenses:end -->（查核紀錄、刪句工具與 gate 用來分辨程式寫的字）。
放在哪：本頁市場段落（## 標題＝site.MARKET_SECTIONS）裡有許可證表的那一段，取代第一張許可證表（表頭第一格含 nummer／Tillatelse／
  Godkjenning）；都沒有表時放在第一個市場段落結尾（段落結尾的 --- 分隔線之前）。沒有市場段落的頁不加。
  表以外的文字不動（正文張數由 scripts/rewrite_license_counts.py 依快照改寫）。
  --migrate（2026-11-24 第一次換表時用）：市場段落裡只講舊表列了幾筆的說明句或子句（CAPTION，例「De fem første er vist nedenfor.」
  「Tabellen viser fem av dem.」「Utvalg på 5:」）一併拿掉；查核紀錄更正文字所在的句子不動（那些由紀錄同 id 重發處理）。
資料來源：預設讀快照 snapshots/no_licenses.json.gz 的 rows／total（scripts/build_license_snapshot.py 依證據包算好，用 rows_of）；
  --bundles 改讀 data/bundles（每週排程在建新快照前用）。gate（scripts/check_seo_docs.py 的許可證項）檢查程式區塊＝快照重算的結果。
誰會跑：scripts/apply_drug_reviews.py（非 --check）結尾、scripts/build_license_snapshot.py 結尾、每週排程
  license_adapter.sync_tables（--bundles）。sync_notes_to_docs.py 整頁重寫後會跑 apply_drug_reviews.py，所以也會重新產生。
用法（repo 根目錄）：python3 scripts/sync_license_tables.py [--bundles] [--check] [--migrate] [頁 ...]
"""
import gzip
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))
from notxgnn.regulatory import site as C  # noqa: E402

SNAP = ROOT / "snapshots" / f"{C.CODE}_licenses.json.gz"
BEGIN = "<!-- licenses:begin -->"
END = "<!-- licenses:end -->"
HEAD = ["| Godkjenningsnummer | Preparatnavn (EMA) | Virkestoff(er) (EMA, engelsk) | Terapeutisk område (EMA, engelsk) | Status |",
        "|------|------|------|------|------|"]
SOURCE = ("Kilde: EMA – Medicines output (sentralt godkjente legemidler til mennesker); preparatnavn, virkestoffer og terapeutisk område "
          "er gjengitt i engelsk original. Nasjonale markedsføringstillatelser (DMP) og veterinærpreparater er ikke med i disse dataene.")
SHOW = "Tabellen viser {n} av {m} sentrale EU-godkjenninger i disse dataene (gyldige først)."
NONE_LINE = ("I de brukte EMA-dataene er det ikke registrert noen sentral EU-godkjenning av et legemiddel til mennesker med dette virkestoffet; "
             "nasjonale markedsføringstillatelser (DMP) er ikke med i disse dataene.")
MAX_ROWS = 20
STATUS_NO = {"authorised": "Gyldig", "withdrawn": "Trukket tilbake", "lapsed": "Bortfalt", "expired": "Utløpt",
             "revoked": "Tilbakekalt", "suspended": "Suspendert", "refused": "Avslått", "not authorised": "Ikke godkjent"}
# 每週排程 3b 的自我檢查（license_refresh）：改到的行除了表格列只能是這些（license_adapter.PAGE_NOTE 用同一份）
PAGE_NOTE = (r"^(" + "|".join(re.escape(x) for x in (BEGIN, END, SOURCE, NONE_LINE))
             + r"|Tabellen viser \d+ av \d+ sentrale EU-godkjenninger i disse dataene \(gyldige først\)\.)$")
# --migrate：只講舊表列了幾筆的說明句（整句或冒號／分號前後的子句）
NUMW = r"(?:\d+|to|tre|fire|fem|seks|sju|syv|åtte|ni|ti)"
CAPTION = re.compile(
    r"(?:De " + NUMW + r" første(?: i dataene)?(?: er vist (?:nedenfor|under))?"
    r"|Tabellen viser " + NUMW + r" av dem"
    r"|Tabellen viser de " + NUMW + r" første av i alt " + NUMW + r" registrerte godkjenninger"
    r"|Listen viser (?:de " + NUMW + r" første|inntil " + NUMW + r" av i alt " + NUMW + r" lisenser)"
    r"|Utvalg på " + NUMW + r"|Et utvalg|Eksempler \(opptil " + NUMW + r"\))[.:]?", re.I)


def cell(x, n=90):
    t = re.sub(r"\s+", " ", str(x or "").replace("|", "/").replace(";", "; ")).strip()
    t = re.sub(r"\s+;", ";", t)
    return (t if len(t) <= n else t[:n - 1].rstrip() + "…") or "–"


def status_no(s):
    s = str(s or "").strip()
    return STATUS_NO.get(s.lower(), s or "–")


def rows_of(tf, fc=None):
    """證據包 tfda（人用集中許可）→ (表格列, 總數)。總數＝total_matches 與收錄筆數取大者（partial 頁 total_matches 較大）。"""
    seen, valid, other = set(), [], []
    for r in tf.get("records") or []:
        k = str(r.get("license_id") or "").strip()
        if not k or k in seen or k.startswith("EMEA/V/"):
            continue
        seen.add(k)
        st = str(r.get("status") or "").strip()
        row = (k, f"| {k} | {cell(r.get('brand_name_zh') or r.get('brand_name_en'), 60)} | {cell(r.get('ingredients'), 90)} | "
                  f"{cell(r.get('indication'), 110)} | {status_no(st)} |")
        (valid if st.lower() == "authorised" else other).append(row)
    rows = [x[1] for x in sorted(valid)] + [x[1] for x in sorted(other)]
    return rows, max(len(rows), int(tf.get("total_matches") or 0))


def program_block(rows, total):
    if not rows:
        return [NONE_LINE]
    out = HEAD + rows[:MAX_ROWS] + [""]
    if total > min(len(rows), MAX_ROWS):
        out.append(SHOW.format(n=min(len(rows), MAX_ROWS), m=total))
        out.append("")
    return out + [SOURCE]


def wrap(block):
    return [BEGIN, ""] + block + ["", END]


def _is_license_table_head(lines, k):
    if not (lines[k].startswith("|") and (k == 0 or not lines[k - 1].startswith("|"))
            and k + 1 < len(lines) and re.match(r"\|\s*:?-", lines[k + 1])):
        return False
    first = (lines[k].strip().strip("|").split("|") or [""])[0]
    return bool(re.search(r"nummer|tillatelse|godkjenning|lisens|autorisasjon", first, re.I))


def _sections(lines):
    out = []
    for i, ln in enumerate(lines):
        if ln.startswith("## ") and ln[3:].strip() in C.MARKET_SECTIONS:
            j = next((k for k in range(i + 1, len(lines)) if lines[k].startswith("## ")), len(lines))
            out.append((i, j))
    return out


def _splice(lines, x, y, blk):
    """lines[x:y] 換成 blk，前後各留恰好一行空行（只動接縫處的空行）"""
    head, tail = lines[:x], lines[y:]
    while head and not head[-1].strip():
        head.pop()
    while tail and not tail[0].strip():
        tail.pop(0)
    return head + [""] + blk + ([""] + tail if tail else [""])


def process(text, rows, total):
    """回傳新內容（沒有市場段落時原樣）。可重複執行。"""
    lines = text.replace("\r\n", "\n").split("\n")
    blk = wrap(program_block(rows, total))
    if BEGIN in lines and END in lines:
        return "\n".join(_splice(lines, lines.index(BEGIN), lines.index(END) + 1, blk))
    secs = _sections(lines)
    for a, b in secs:
        tb = [k for k in range(a + 1, b) if _is_license_table_head(lines, k)]
        if tb:
            y = tb[0]
            while y + 1 < b and lines[y + 1].startswith("|"):
                y += 1
            return "\n".join(_splice(lines, tb[0], y + 1, blk))
    if not secs:
        return text
    a, b = secs[0]
    e = b
    while e > a + 1 and (not lines[e - 1].strip() or lines[e - 1].strip() == "---"):
        e -= 1
    return "\n".join(_splice(lines, e, e, blk))


def drop_captions(text, protect=()):
    """--migrate：市場段落裡只講舊表列了幾筆的說明句或子句拿掉（查核框、程式區塊、表格、查核紀錄的更正文字不動）。
    回傳 (新內容, 拿掉的片段)。子句：句子以「;」「:」分成幾段，只拿掉整段都是 CAPTION 的那段。"""
    lines = text.split("\n")
    out, dropped, in_box = [], [], False
    inside = {k for a, b in _sections(lines) for k in range(a + 1, b)}
    for k, ln in enumerate(lines):
        if ln.startswith("<!-- review:begin") or ln == BEGIN:
            in_box = True
        if ln.startswith("<!-- review:end") or ln == END:
            in_box = False
            out.append(ln)
            continue
        if in_box or k not in inside or ln.startswith(("|", "#", ">")) or not ln.strip():
            out.append(ln)
            continue
        sents = re.split(r"(?<=[.!?:])\s+", ln)
        keep = []
        for s in sents:
            if any(p and (s.strip() in p or p in s) for p in protect):  # 查核紀錄的更正文字所在的句子不動
                keep.append(s)
                continue
            parts = re.split(r"(;\s*)", s)
            segs = parts[0::2]
            if len(segs) > 1 and CAPTION.fullmatch(segs[0].strip()):
                # 「De fem første er vist under; doseringsform er ikke oppgitt i dataene.」→ 拿掉前半，後半首字大寫
                dropped.append(segs[0].strip())
                rest = "".join(parts[2:]).strip()
                keep.append(rest[:1].upper() + rest[1:])
                continue
            # 「Markedsført: 16 av 16 tillatelser er gyldige. Eksempler (opptil 5):」由句子分割處理
            if CAPTION.fullmatch(s.strip()):
                dropped.append(s.strip())
                continue
            keep.append(s)
        if keep:
            out.append(" ".join(keep))
        elif out and not out[-1].strip():
            out.pop()  # 整行拿掉時，連帶拿掉一行空行
    return "\n".join(out), dropped


def _snapshot():
    return json.loads(gzip.open(SNAP).read().decode("utf-8")).get("drugs", {}) if SNAP.exists() else {}


def _bundle(stem):
    for key in (stem, stem.replace("-", "_"), stem.replace("_", "-")):
        f = ROOT / "data/bundles" / key / "drug_bundle.json"
        if f.exists():
            return json.loads(f.read_text(encoding="utf-8"))
    return None


def is_redirect(text):
    h = text[:3000]
    return 'http-equiv="refresh"' in h or bool(re.search(r"^layout:\s*id_redirect", h, re.M))


def _protect():
    f = ROOT / "docs/_data/drug_reviews.json"
    out = {}
    if f.exists():
        for r in json.loads(f.read_text(encoding="utf-8")).get("records", []):
            out.setdefault(r["file"], []).extend(x.strip() for x in (r.get("replacement"), r.get("anchor")) if x and x.strip())
    return out


def run(from_bundles=False, check=False, only=None, migrate=False, log=None):
    """回傳改到的頁（檔名）。快照或證據包沒有的頁不動。"""
    snap = {} if from_bundles else _snapshot()
    prot = _protect() if migrate else {}
    changed = []
    for p in sorted((ROOT / "docs/_drugs").glob("*.md")):
        if only and p.name not in only and p.stem not in only:
            continue
        raw = p.read_bytes().decode("utf-8")
        if is_redirect(raw):
            continue
        if from_bundles:
            b = _bundle(p.stem)
            if b is None:
                continue
            rows, total = rows_of(b.get("tfda") or {})
        else:
            e = snap.get(p.stem)
            if not e or "rows" not in e:
                continue
            rows, total = e["rows"], e["total"]
        crlf = "\r\n" in raw[:500]
        t0 = raw.replace("\r\n", "\n")
        new = process(t0, rows, total)
        if migrate and new != t0:
            new, dropped = drop_captions(new, prot.get(p.name, ()))
            if log is not None:
                log += [(p.stem, s) for s in dropped]
        if new != t0:
            changed.append(p.name)
            if not check:
                p.write_bytes((new.replace("\n", "\r\n") if crlf else new).encode("utf-8"))
    return changed


def block_problems(sec_lines, entry):
    """gate 用：段落裡的程式區塊＝快照重算的結果（licenses.page_problems 呼叫）"""
    has_b, has_e = BEGIN in sec_lines, END in sec_lines
    if has_b != has_e:
        return ["程式許可證區塊標記不成對"]
    if not has_b or "rows" not in entry:
        return []
    i, j = sec_lines.index(BEGIN), sec_lines.index(END)
    got = [x for x in sec_lines[i + 1:j] if x.strip()]
    want = [x for x in program_block(entry["rows"], entry["total"]) if x.strip()]
    if got != want:
        k = next((k for k, (x, y) in enumerate(zip(got, want)) if x != y), min(len(got), len(want)))
        return [f"程式許可證區塊第 {k + 1} 行跟快照重算的結果不同（程式表被手改或資料已更新：跑 python3 scripts/sync_license_tables.py）"]
    return []


if __name__ == "__main__":
    a = sys.argv[1:]
    only = {x for x in a if not x.startswith("--")} or None
    log = []
    ch = run(from_bundles="--bundles" in a, check="--check" in a, only=only, migrate="--migrate" in a, log=log)
    for stem, s in log:
        print(f"拿掉說明句\t{stem}\t{s}")
    print(f"程式許可證表：{'待改' if '--check' in a else '改'} {len(ch)} 頁")
    if "--check" in a:
        sys.exit(1 if ch else 0)
