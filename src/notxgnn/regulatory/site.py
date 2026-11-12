"""本站查核機制的在地設定（NOTxGNN，挪威文〔bokmål〕；2026-11-12 建）。

程式（page_format、licenses、withdrawn、scripts/apply_drug_reviews.py、build_license_snapshot.py、reviews_from_edits.py、
check_original_indications.py）的核心流程比照 TwTxGNN／UsTxGNN，本站的字樣、規則細節、提交清單集中在這裡。
本站的許可證資料是 EMA 集中許可（不含挪威國家許可 DMP），事實層只涵蓋這部分（checker X_SCOPE、NO_CENTRAL）。
"""
import re

SITE = "NOTxGNN"
CODE = "no"

# ---- 頁首等級（page_format）----
OVERVIEW_LEVEL_LABELS = ["Evidensnivå", "Bevisnivå"]
HEADER_LABEL = "Evidensnivå"
# 2026-11-12 實測：435 頁有總覽等級，433 頁頁首＝總覽格第一個等級（主預測）；另 2 頁（abiraterone_acetate、canagliflozin）
# 頁首 N/A、總覽格寫「L5 (ingen prediksjon …)」，是沒有保留預測的頁，由 HEADER_KEEP_NA 涵蓋 → first，不改等級
HEADER_RULE = "first"
HEADER_KEEP_NA = True
HEADER_EXCEPTIONS: dict = {}
WITHDRAWN_RE = re.compile(r"^\s*(\*\*)?(Trukket tilbake|Tilbaketrukket)\b", re.I)
DESC_LEVEL_WORD = r"evidensnivå|bevisnivå"
DESC_LEVEL_DEFAULT = "evidensnivå"
NA_DESC = "kun kjente bruksområder"

# ---- 許可證（licenses）----
MARKET_SECTIONS = ["Markedsinformasjon for Norge", "Informasjon om det norske markedet", "Informasjon om markedet i Norge"]

# ---- 查核框與查核紀錄表（apply_drug_reviews）----
DISCLAIMER_RE = re.compile(r"^## Ansvarsfraskrivelse\b", re.M)
LOG_HEAD = "## Kontrollogg"
LOG_COLS = "| Kontrolldato | Punkt | Tiltak | Kilde |"
LABEL = {"correct": "Kontrollrettelse", "annotate": "Kontrollmerknad", "rereview": "Venter på ny vurdering",
         "rereview_result": "Resultat av ny vurdering"}
ACTION = {"correct": "Rettet", "annotate": "Merknad lagt til", "rereview": "Merket for ny vurdering",
          "section": "Avsnitt med kilder lagt til", "rereview_result": "Ny vurdering fullført",
          "header_level": "Evidensnivået i toppteksten ble beregnet på nytt fra hurtigoversikten",
          "description_level": "Sidebeskrivelsens evidensnivå følger toppteksten"}
VERDICT = {"maintain": "Uendret", "downgrade": "Nedgradert", "upgrade": "Oppgradert", "withdraw": "Trukket tilbake"}
BOX_HEAD = "> **{label} ({date})**: "
ORIG_STATED = "Opprinnelig sto det: «{claim}»"
SPACE, FULL_STOP, SENT_END = " ", ".", ".!?)»"
PAREN = " ({})"
JOIN, LIST_SEP, ITEM_SEP = " / ", "; ", ", "
SOURCE_WORD = "Kilde: "
DECISION = "Anbefalt beslutning: "
TABLE_UPDATED = "{labels} på siden er oppdatert etter den nye vurderingen; de opprinnelige verdiene står i kontrolloggen nedenfor."
LEVEL_SAME = "evidensnivå {o} uendret"
LEVEL_CHANGE = "evidensnivå {o} → {n}"
ACT_REREVIEWED = "Merket for ny vurdering → vurdert på nytt (se resultatet av den nye vurderingen)"
ACT_HEADER = "Evidensnivået i toppteksten ble beregnet på nytt fra hurtigoversikten ({o} → {n})"
ACT_HEADER_WD = "Hovedprediksjonen ble trukket tilbake ved ny vurdering; evidensnivået i toppteksten ble beregnet på nytt ({o} → {n})"
ACT_NA_LIST = ", vises nå under «{title}»"
ACT_RESULT = "Ny vurdering: {verdict}, {change}"
ACT_TABLE = "; {label}: «{a}» → «{b}»"
ACT_DESC = "Sidebeskrivelsen: «evidensnivå {o}» ble endret til «{n}» (følger toppteksten; øvrig tekst uendret, originalen er lagret i posten)"
ACT_REVISED = " (revidert {d}; tidligere versjon er lagret i posten)"
ST_SUPERSEDED = "Erstattet av den programgenererte lisenstabellen (tidligere: {act})"
ST_REGEN = "Finnes ikke lenger etter at rapporten ble generert på nytt ({d}: {note}; tidligere: {act})"
ST_PROGRAM = "Finnes ikke lenger etter en programretting ({d}: {note}; tidligere: {act})"
ST_WITHDRAWN = "Kontrollen er trukket tilbake ({d}: {note}; tidligere: {act})"
INTRO = ("Nedenfor er kontrolloggen for denne siden: opplysninger kontrollert mot EMAs data om sentrale EU-godkjenninger. "
         "Rettelser gjelder bare grunnleggende faktaopplysninger; modellens prediksjoner, evidensnivåer og konklusjoner er ikke skrevet om.")
INTRO_HEADER = ("Nedenfor er kontrolloggen for denne siden; evidensnivået i toppteksten følger hurtigoversikten. "
                "Modellens prediksjoner, oversiktstabellen og konklusjonene er ikke skrevet om.")
INTRO_RERE = ("Nedenfor er kontrolloggen for denne siden: opplysninger kontrollert mot EMAs data om sentrale EU-godkjenninger. Rettelser gjelder "
              "bare grunnleggende faktaopplysninger, og modellens prediksjonstekst er ikke skrevet om; evidensnivåer og beslutninger er bare endret "
              "gjennom et resultat av ny vurdering (nedgradering, oppgradering eller tilbaketrekking), med de opprinnelige verdiene nedenfor.")

# ---- 刪改轉紀錄（reviews_from_edits）----
# 2026-10-31～11-06 的許可證刪改（git log docs/_drugs）：d362206d 刪「只剩註銷許可」、d19127bc 撤銷頁的狀態列與正文照資料範圍寫、
# 8c12de1a 第二批掃描刪矛盾子句。排程狀態格、排除表、AI 重產、description、空行修正不算。
COMMITS = ["d362206d", "d19127bc", "8c12de1a"]
REGEN_COMMITS = ["07ad2131", "ec9ed499", "57f14680", "d47a8e15", "f9b0ee59", "9b842e88", "40cfec53"]
SOURCES = [{"title": "EMA – Medicines output: medicines report", "url": "https://www.ema.europa.eu/en/documents/report/medicines-output-medicines-report_en.xlsx"},
           {"title": "European Medicines Agency", "url": "https://www.ema.europa.eu/"}]
SENT = re.compile(r'(?<=[.!?])\s+(?=[A-ZÆØÅ0-9(*"«\[])|\n')
CLASS_EXTRA: dict = {}
NOTES = {
    "tw": "Fjernet: gjenværende maltekst om Taiwans legemiddelmyndighet (TFDA), som ikke gjelder denne norske siden.",
    "cancel": "Fjernet: opplysningen om at godkjenningene er avregistrert eller at ingen gyldig godkjenning finnes, stemte ikke med EMAs data om sentrale EU-godkjenninger ({date}).",
    "count": "Fjernet: antallet eller statusen for godkjenningene stemte ikke med EMAs data om sentrale EU-godkjenninger ({date}).",
    "generic": "Fjernet: opplysningen stemte ikke med EMAs godkjenningsdata ({date}).",
}
FIGURES = " Antall godkjenninger i dataene: {total}, hvorav gyldige: {valid}; oppdaterte tall står i hurtigoversikten og i markedsinformasjonen."
SUMMARY = "Fjernet: «{text}»"
STRIP_CHARS = " ,;.\n-"
REGEN_NOTE = "rapporten ble generert på nytt i november 2026 og inneholder ikke lenger opplysningen"

# ---- 原適應症交叉驗證（check_original_indications）----
ORIGINAL_LABELS = ["Opprinnelig indikasjon"]
ORIGINAL_NONE_RE = re.compile(r"^\s*(ikke registrert|ikke oppgitt|ingen|mangler|n/a)", re.I)
PHRASE_SPLIT = re.compile(r"[;,/()]+|\bog\b|\beller\b", re.I)
PHRASE_MIN = 4
