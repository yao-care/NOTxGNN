"""正文許可證張數的程式改寫（2026-11-24 建，用戶決定「正文張數自動改寫」；做法移植 KrTxGNN／MyTxGNN 同名檔，
句型照 DETxGNN 同名檔（同為 EMA 集中許可）改成本站挪威文〔bokmål〕）。

正文裡「N av M godkjenninger er gyldige」「N gyldige tillatelser (av M)」「Det finnes N gyldig tillatelse av M」
「Alle N godkjenninger er gyldige」「Totalt er det N tillatelser」這類 EMA 集中許可張數敘述，由程式依許可證快照
（snapshots/no_licenses.json.gz 的 facts）改寫，每週資料更新後跟著改，不逐筆寫查核紀錄（同 Kr／My／Tw：程式改寫的張數敘述是程式產生的正文）。

只改「句型明確、數字確定是本藥 EMA 集中許可張數」的地方，其餘一律不動：
  - 句子要有許可字樣（tillatelse／godkjenning／lisens／autorisasjon），且沒有試驗、文獻、病人、劑量、年份等字樣（NOT_LICENSE）。
  - 跳過：查核框（<!-- review -->）、程式許可證區塊（<!-- licenses -->）、表格列、標題、front matter；
    查核紀錄 replacement／anchor 所在的句子（改了紀錄會對不上）。
  - 整句不動（skipped）：有保留（minst、ufullstendig、utvalg…）、講證據包或查詢（evidenspakke、søk、returnerte…）、
    相對數（ytterligere、øvrige、andre、resterende）、劑型或單方／複方子集、獸用、其他國家或國家許可（FDA、DMP、nasjonal…）、廠商；
    講表格顯示筆數（tabell、listen, vist, første…，reason＝display）；事實層 partial 或總數 0 的頁整頁不動。
角色：「X av Y」的 X 看後面的狀態字（gyldig→有效；avregistrert／trukket tilbake／kansellert…→註銷），Y＝總數；
「N gyldig(e) …」有效；「N kansellerte／avregistrerte …」註銷；「N (registrerte) godkjenninger」總數（後面接「er avregistrert」算註銷）；
其餘數字不動。數字可寫成阿拉伯數字或 to～tolv、begge；「én／en／ett」只在緊接（gyldig）許可名詞時算 1。
同一行只要有一句含許可證數字而被略過，整行都不動（免得前後句數字對不上）。
數字已等於該角色的任一合理讀法（沒有限定詞的總數＝總數或有效數）就不動；不等於時兩種讀法相同才改，不同列為 ambiguous。
不改、列出（要改請寫查核紀錄）：原數字 0（zero-premise）、新數字 0（zero-result）、1 跟非 1 之間的改動（名詞與形容詞單複數
要跟著改，grammar）、文字數詞（word，用戶 2026-11-24：文字數詞不改）、句子說「alle／begge … gyldig」或「ingen … avregistrert」
而有效≠總數（premise）、說「den eneste／denne godkjenningen」而改動跨過 1（premise）。
"""
from __future__ import annotations

import re

SENT_SPLIT = re.compile(r"(?<=[.!?])\s+(?=[A-ZÆØÅ*\[(>-])")
WORDS = {"to": 2, "tre": 3, "fire": 4, "fem": 5, "seks": 6, "sju": 7, "syv": 7, "åtte": 8, "ni": 9, "ti": 10,
         "elleve": 11, "tolv": 12, "begge": 2}
ONE = r"(?:én|en|ett|ei|éi)"
NOUN = r"(?:markedsførings)?(?:tillatels(?:e|en|er|ene)|godkjenning(?:en|er|ene)?|lisens(?:en|er|ene)?|autorisasjon(?:en|er|ene)?)"
LICENSE = re.compile(r"tillatels|godkjenning|lisens|autorisasjon", re.I)
CANC = r"(?:avregistrert\w*|trukket tilbake|tilbaketrukk\w*|tilbakekal\w*|utløpt\w*|annuller\w*|opphevet\w*|opphørt\w*|kansellert\w*|bortfalt\w*|ugyldig\w*)"
VALID = r"(?:gyldig\w*|aktiv\w*)"
ADJ = r"(?:(?:registrerte?|norske?|europeiske?|sentrale?|norske/europeiske|eneste|EU-|EMA-|kjente)\s*)*"
NUM = re.compile(r"(?<![\w.,/-])(\d{1,4}|" + "|".join(sorted(WORDS, key=len, reverse=True)) + r"|" + ONE +
                 r"(?=\s+(?:(?:eneste\s+)?(?:gyldige?\s+|kansellerte?\s+|avregistrerte?\s+)?" + ADJ + NOUN + r")))(?![\w%-])", re.I)
NOT_LICENSE = re.compile(r"studie|forsøk|pasient|deltaker|PMID|NCT|publikasjon|artikkel|tilfelle|\bmg\b|\bml\b|%|\bår\b|måned|uke|dose|"
                         r"\bscore|indikasjon|fase\b|fase-|\b(?:19|20)\d\d\b", re.I)
HEDGED = re.compile(r"\bminst\b|minimum|ufullstendig|delvis|utvalg|muligens|trolig|antakelig|"
                    r"evidenspakke|Evidence Pack|\bsøk\w*|spørring|returnerte|datasett|"
                    r"ytterligere|\bandre\b|øvrige|resterende|\bblant\b|\bherav\b|"
                    r"veterinær|EMEA/V|enkeltstoff|kombinasjon|"
                    r"tablett|kapsel|injeksjon|infusjon|oppløsning|pulver|sprøyte|\bpenn\b|dråper|krem|salve|inhal|plaster|implantat|"
                    r"\bFDA\b|\bUSA\b|\bDMP\b|nasjonal|produsent|innehaver", re.I)
DISPLAY = re.compile(r"tabell|\blisten\b|\blisten viser\b|\bførste\b|\bvist\b|nedenfor|ovenfor|følgende|oppført|oppstilt|\bunder:", re.I)
BLOCK = re.compile(r"<!-- (review|licenses):begin.*?<!-- \1:end[^>]*-->", re.S)


def _val(tok):
    t = tok.lower()
    if t.isdigit():
        return int(t)
    if t in WORDS:
        return WORDS[t]
    return 1


def _role(s, a, b):
    left, right = s[max(0, a - 45):a], s[b:b + 80]
    # 「X av Y」的 Y（前面是數字或「gyldig(e) tillatelse(r)」）＝總數；其他「av N」不動
    if re.search(r"\bav\s+(?:totalt\s+|i alt\s+)?$", left, re.I):
        pre = re.sub(r"\bav\s+(?:totalt\s+|i alt\s+)?$", "", left, flags=re.I)
        if re.search(r"(\d+|" + "|".join(WORDS) + r"|" + ONE + r")\s*$", pre, re.I) or \
                re.search(r"(gyldige?|kansellerte?|avregistrerte?)\s+(?:" + ADJ + NOUN + r"\s*)?\(?$", pre, re.I):
            return "total"
        return None
    # 「X av Y …」的 X：看後面的狀態字
    m = re.match(r"\s+av\s+(?:totalt\s+|i alt\s+)?\S+\s+" + ADJ + r"(?:" + NOUN + r")?\s*(?:\([^)]*\)\s*)?"
                 r"(?:(?:er|var|blir|i dag|nå|fortsatt|fremdeles|registrert som|i dataene)\s+){0,3}(" + VALID + "|" + CANC + ")", right, re.I)
    if m:
        return "cancelled" if re.match(CANC, m.group(1), re.I) else "valid"
    if re.match(r"\s+av\s+", right):
        if re.search(r"gyldig\w*\s*\(?$", left, re.I) or re.search(r"gyldige?\s+" + ADJ + NOUN + r"\s*\(?$", left, re.I):
            return "valid"  # 「Begge tillatelsene er gyldige (2 av 2)」
        return None
    if re.match(r"\s+(?:eneste\s+)?gyldige?\s+" + ADJ + NOUN, right, re.I):
        return "valid"
    if re.match(r"\s+(?:eneste\s+)?" + CANC + r"\s+" + ADJ + NOUN, right, re.I):
        return "cancelled"
    m = re.match(r"\s+" + ADJ + NOUN + r"\b([^.;,:]{0,40})", right, re.I)
    if m:
        tail = m.group(1)
        if re.search(r"\b(er|var|ble|har status)\s+(?:\w+\s+)?" + CANC, tail, re.I):
            return "cancelled"
        if re.search(r"\b(er|var)\s+(?:\w+\s+)?gyldig", tail, re.I) and not re.search(r"\b(alle|samtlige|begge)\s*$", left, re.I):
            return "valid"
        return "total"
    return None


def _readings(role, f, explicit):
    t, v, c = f.get("total"), f.get("valid"), f.get("cancelled")
    if role == "cancelled":
        return {c}, c
    if role == "valid":
        return {v}, v
    if explicit:
        return {t}, t
    return {t, v}, (t if t == v else None)


def _premise_ok(sent, f):
    lo = sent.lower()
    if re.search(r"\b(alle|samtlige|begge|den eneste|det eneste|eneste)\b[^.;]{0,60}" + VALID, lo) and f.get("valid") != f.get("total"):
        return False
    if re.search(r"\b(alle|samtlige|begge)\b[^.;]{0,60}" + CANC, lo) and f.get("cancelled") != f.get("total"):
        return False
    if re.search(r"\b(ingen|ikke)\b[^.;]{0,30}" + CANC, lo) and f.get("cancelled"):
        return False
    return True


def rewrite_sentence(sent, f):
    """回傳 (新句子, 跳過理由或 None)。"""
    if not LICENSE.search(sent) or not NUM.search(sent):
        return sent, None
    found = [(m, _role(sent, m.start(), m.end())) for m in NUM.finditer(sent)]
    found = [(m, r) for m, r in found if r]
    if not found:
        return sent, None
    if NOT_LICENSE.search(sent):
        return sent, None
    if HEDGED.search(sent):
        return sent, "hedged/subset"
    explicit = any(r in ("valid", "cancelled") for _, r in found) or bool(re.search(r"\b(totalt|i alt|til sammen)\b", sent, re.I))
    if DISPLAY.search(sent):  # 講表格顯示筆數：不改；數字跟事實對不上時列出（reason＝display）
        bad = any(_val(m.group(1)) not in _readings(r, f, explicit)[0] for m, r in found)
        return sent, ("display" if bad else "display-ok")
    subs = []
    for m, role in found:
        old = _val(m.group(1))
        ok, v = _readings(role, f, explicit)
        if old in ok:
            continue
        if v is None:
            return sent, "ambiguous"
        if old == 0:
            return sent, "zero-premise"
        if v == 0:
            return sent, "zero-result"
        if not m.group(1).isdigit():
            return sent, "word"
        if (old == 1) != (v == 1):
            return sent, "grammar"
        subs.append((m, v))
    if not subs:
        return sent, None
    if not _premise_ok(sent, f):
        return sent, "premise"
    out, pos = [], 0
    for m, v in subs:
        out.append(sent[pos:m.start(1)])
        out.append(str(v))
        pos = m.end(1)
    out.append(sent[pos:])
    return "".join(out), None


def _line(ln, f, protect, skipped):
    if ln.startswith(("|", "#", "{:")) or not ln.strip():
        return ln
    parts = SENT_SPLIT.split(ln)
    seps = SENT_SPLIT.findall(ln)
    new, held = [], False
    for s in parts:
        if any(p and (p in s or s in p) for p in protect):
            new.append(s)
            continue
        ns, why = rewrite_sentence(s, f)
        if why:
            skipped.append((why, s.strip()))
            held = True
        new.append(ns)
    if held:  # 同一行有句子判斷不了：整行不動
        return ln
    out = new[0]
    for sep, s in zip(seps, new[1:]):
        out += sep + s
    return out


def rewrite(text, facts, protect=()):
    """text：整頁 markdown。facts：快照的 facts。回傳 (新內容, skipped)。front matter、查核框、程式區塊、表格不動。"""
    skipped = []
    if not facts or facts.get("partial") or not facts.get("total"):
        return text, skipped
    protect = [p.strip() for p in protect if p and len(p.strip()) >= 6]
    fm_end = 0
    if text.startswith("---"):
        j = text.find("\n---", 3)
        fm_end = j + 4 if j > 0 else 0
    body = text[fm_end:]
    keep = []

    def hold(m):
        keep.append(m.group(0))
        return f"\x00{len(keep) - 1}\x00"
    body = BLOCK.sub(hold, body)
    lines = [ln if "\x00" in ln else _line(ln, facts, protect, skipped) for ln in body.split("\n")]
    body = re.sub(r"\x00(\d+)\x00", lambda m: keep[int(m.group(1))], "\n".join(lines))
    return text[:fm_end] + body, skipped
