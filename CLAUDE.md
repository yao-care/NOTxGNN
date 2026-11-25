# NOTxGNN 維護說明

各站共通的維護流程見母 repo（yao-care/txgnn）的 CLAUDE.md；本檔只記本站自己的機制。

---

## 藥物頁查核機制（2026-11-12 起）

用戶 2026-11-12 決定：30 站各有自己的查核機制，核心流程比照 TwTxGNN（Tw 的 CLAUDE.md「藥物頁人工查核紀錄」「藥物頁許可證表與張數」兩節）；
UsTxGNN 是第一個試做站（做法見 UsTxGNN/CLAUDE.md 同名一節）。本站的規則與程式都在本 repo，頁面文字用挪威文（bokmål），依據是EMA 的集中許可資料（不含挪威國家許可 DMP）。
本站的在地字樣、頁首規則細節、歷史刪改的提交清單集中在 `src/notxgnn/regulatory/site.py`。

| 環節 | 本站檔案 | 說明 |
|------|----------|------|
| 查核紀錄 | `docs/_data/drug_reviews.json` | 單一真實來源，欄位同 Tw（correct／annotate／rereview／rereview_result／header_level／description_level、history、status） |
| 套用 | `scripts/apply_drug_reviews.py` | 套到 `docs/_drugs/*.md`：查核框 `<!-- review:begin id -->`、每頁在免責聲明前的查核紀錄表；可重複執行；`--check` 只檢查、`--touch` 連 last_modified_at 一起改 |
| 頁首等級 | `src/notxgnn/regulatory/page_format.py` | 頁首＝快速總覽「Evidensnivå／Bevisnivå」格的**第一個**等級（主預測）。2026-11-12 實測 435 頁有總覽等級，433 頁符合；另 2 頁頁首 N/A（沒有保留預測）由「N/A 頁不重算」涵蓋，所以照實寫成程式、不改現有等級；Tw 是整格取最高，本站不同 |
| 撤回預測 | `src/notxgnn/regulatory/withdrawn.py` | verdict=withdraw 的預測不進證據監測（`scripts/extract_drug_list.py`）、搜尋索引與 FHIR（母目錄 `.claude/rebuild_search_index.py`、`.claude/sync_fhir_levels.py` 會讀本站這支） |
| 許可證 | `snapshots/no_licenses.json.gz`、`scripts/build_license_snapshot.py`、`src/notxgnn/regulatory/licenses.py` | 快照存本藥許可證號與事實層；gate 依快照驗市場段落表格的許可證號屬於本藥、狀態列與張數列＝事實層寫法、表格列狀態不跟事實相反（本站沒有程式產生的許可證表，不驗表格列內容） |
| 刪改轉紀錄 | `scripts/reviews_from_edits.py` | 依 git 前後版本（或改寫前後目錄）把正文刪改轉成 correct 紀錄 |
| 待查清單 | `docs/_data/drug_reviews_uncertain.json`、`scripts/check_original_indications.py` | 原適應症交叉驗證與待重審項目；證據包沒有許可證適應症文字時照實回報可比對 0 頁 |
| gate | `scripts/check_seo_docs.py` 最後 4 項 | 紀錄都已套用、許可證＝快照、頁首＝快速總覽等級、撤回預測沒有對外發布 |

原則（同 Tw）：基本事實照主管機關資料更正；模型預測原文不刪不改寫，只加註；證據等級與決策只經重審（rereview → rereview_result）變更。

改頁之後要跑：

```bash
python3 scripts/apply_drug_reviews.py          # 重套查核紀錄（sync_notes_to_docs.py、每週排程結尾都會自動跑）
python3 scripts/build_license_snapshot.py --ws <工作目錄>   # 證據包或事實層變了才要（每週排程會自動跑）
python3 scripts/check_seo_docs.py              # 必須 exit 0
```

2026-10-31～11-06 依新事實直接刪掉的矛盾子句，2026-11-12 已用 `scripts/reviews_from_edits.py --git` 轉成 200 筆紀錄（143 頁；其中 3 筆因報告在 11 月經 AI 重產、原句已不在頁面，標 resolved_by_regeneration）。
`scripts/sync_notes_to_docs.py` 依 notes 重寫整頁後會重套紀錄，notes 裡的舊錯句會被紀錄再更正一次。

2026-11-12 正文許可狀態對事實層掃描：6 頁（cetrorelix、ranibizumab、roxadustat、tasimelteon、tobramycin、verteporfin）在 11 月 AI 重產時照證據包（local_regulatory 全標 Cancelled only）寫成「opphørt／trukket tilbake／avsluttet」，EMA 資料（bundle）是 Authorised、事實層有效；以 11 筆 `no-lic-20261112-*` 紀錄更正（含 tasimelteon 表格列「status: opphørt」→「godkjent」）。

2026-11-12 許可證表格列狀態對事實層（母目錄 check_drug_page.py --row-status）：4 列 EMA 現行許可（Cerezyme、Yervoy、Vectibix、Erivedge）標成註銷、2 列（Natpar、Optruma）寫 godkjent 但 EMA 為 Withdrawn，以 6 筆 `no-row-20261112-*` correct 紀錄更正（依證據包原始狀態逐列確認）。

## 作用機轉段的資料來源與查核機制（2026-11-19）

用戶 2026-11-19 決定把 NZTxGNN 同日的作法推到各站（seo-ops 轉交：搜「<藥名> mechanism of action」落在藥物頁排名 30–99，因為頁面寫「作用機轉資料不可得」）。
2026-11-19 量測：本站公開藥物頁（排除 noindex、轉址頁）有 387 頁在正文章節寫這種句子（證據包 drugbank.source＝vocab_only、沒有作用機轉文字，AI 照實寫「沒有資料」；本站最常見的寫法：「Detaljerte data om virkningsmekanisme er foreløpig ikke tilgjengelige.」）。
作用機轉是藥物本身的基本藥理事實、不是模型預測，所以照查核機制補：每段都節錄官方仿單或資料庫原文、附可點的出處與取用日期，不自己寫。

- 來源（理由同 NZTxGNN/CLAUDE.md 同名一節）：美國 FDA 核准仿單（openFDA drug label，連結到 NLM DailyMed 同一份 SPL setid；FDA 仿單是美國政府公開資料），美國沒有仿單時用 ChEMBL drug mechanism 表（CC BY-SA 3.0）；證據包的 DrugBank 欄位只有 vocab，DrugBank 文字授權也不允許轉載，不用。
  2026-11-19 這次用 openFDA 的 drug label 全量下載檔（download.open.fda.gov，同一批資料，只留 human prescription 仿單；`--fda-bulk <目錄>`），不吃 API 每日 1,000 次配額；之後少量重跑可直接用 API（不給 `--fda-bulk`）。快取目錄各站共用。
- `scripts/build_mechanism_reviews.py --cache <目錄> [--fda-bulk <目錄>]`：掃公開頁正文章節（排除結論／下一步的待辦、安全性、摘要、總覽表、查核紀錄、免責聲明等）裡同時有「作用機轉」「資料」「沒有」字樣的短句（本站語言的字樣在檔內 L 的 KW／DATA／NEG／EXCL）→ 依 front matter monitor_inn（INN 另對 USAN，表在 US_NAME）查 openFDA，選仿單規則同 NZ：只用單一成分、主成分名（去鹽類；酯類要相同）跟本頁相同的處方藥仿單；排序全身給藥→節錄夠長→有 12.1→有品牌名→版本新；美國只有複方仿單的只節錄 12.1 裡講本藥成分的句子並寫明是複方；節錄照原文 2～4 句、不改寫。
  紀錄寫進 `docs/_data/drug_reviews.json`（action＝mechanism，id `no-moa-<日期>-<藥>-1`，sources 附 url、accessed、excerpt、label_version、section、set_id 或 chembl_id）；仿單與 ChEMBL 都沒有的，列進 `docs/_data/drug_reviews_uncertain.json`（source＝mechanism of action，附原因）。已有紀錄或已列待查的頁不重抓。`--list` 只列仍寫「不可得」的頁。
- 替換句格式：本站語言（norsk）的出處句＋節錄的忠實翻譯（標明「非官方翻譯」）＋英文原文（照引、為準）＋DailyMed 連結、仿單版本、取用日期（用戶 2026-11-19 決定「當地語言摘要＋英文原文」）。只換「不可得」那一句（英文站句首子句後接 so／but 的後半句是 AI 推論，保留），不加框；查核紀錄表列原句與出處。模型預測與其他正文不動。
- 翻譯：節錄的翻譯是 AI 輔助的忠實翻譯（不增不減，藥名、基因與受體符號、數字、「[…]」照原文），2026-11-19 批次產生，存在紀錄 sources 的 translation（translation_lang、translation_note 註明非官方、英文原文為準）；頁面上同時列英文原文。`--translations <檔>` 讀翻譯、`--need <檔>` 列出還沒翻的節錄（這些頁那次不寫紀錄，gate 會擋，翻好再跑）。
- 2026-11-19 結果：368 頁寫入紀錄（美國仿單 329、ChEMBL 39），19 頁列待查（美國沒有單一成分處方藥仿單、仿單段落不是作用機轉，且 ChEMBL 沒有已核准分子的機轉紀錄；多是胺基酸、維生素、礦物質、賦形劑、生物製劑或只在別國上市的藥）。
- `scripts/apply_drug_reviews.py` 支援 mechanism；gate 第 21 項（`scripts/check_seo_docs.py`，函式在 build_mechanism_reviews.gate_errors）：公開頁仍寫「不可得」、既沒有 mechanism 紀錄也沒列待查的，擋下；有紀錄沒套上的由查核紀錄那一項擋。
- 注意：節錄的是美國仿單，劑型與適應症可能跟本站市場的產品不同（例如取到外用仿單）；文字上已寫明是美國 FDA 核准仿單。`sync_notes_to_docs.py` 整頁重寫後會重套紀錄（claim 是頁面原句）；報告重產、原句改寫後要再跑 build_mechanism_reviews.py。
- 2026-11-20 補做：程式更新：同頁不只一句「不可得」時每句各一筆紀錄（-1、-2…）；同頁別筆紀錄的更正文字、錨點與已套上的節錄不再當成「不可得」句；gate 改成公開頁仍寫「不可得」、又沒列待查就擋（不再只看該頁有沒有紀錄）；同頁第二句起補 1 筆紀錄（id 結尾 -2）；ChEMBL 譯文（詞組清單）後補句號 39 筆；同 id 重發，前版 replacement 存 history。
- 2026-11-20 試跑母目錄「交付前驗證」規則時補做：偵測改成原條件不動、另加新增寫法（L2，比中的再用 NOT 排除以缺資料為前提的模型推論），字樣用獨立、更寬的偵測全量掃出的候選句逐句標註校準（A 沒有漏、B 沒有誤中）；偵測漏抓的「不可得」句補 20 筆紀錄、1 頁列待查；節錄後面接著 AI 說明「上面描述依據」的句子（會讀成美國仿單的出處）2 筆改成那句在節錄前（原文不改，只換順序）；同頁重複引用同一段節錄的 1 筆改成指向上方節錄的一句（附同一個來源連結）；以上同 id 重發，前版存 history。程式另加 reorder_src_tail、同頁已引用同一段節錄時改指向上方（產生器 txgnn/.claude/moa_rollout_20261119/fix_20261120/）。

## 說明頁與證據等級頁的在地資料（2026-11-19）

用戶 2026-11-19 決定的第一批改版（母目錄 `.claude/gen_local_pages_20261119.py` 產生，不逐站手改）：說明頁（about／guide／sources／downloads／methodology，自有結構站只有證據等級頁與隱私頁）加本站資料區塊（`<!-- local-facts -->`）、證據等級頁的事實段與藥名表（`<!-- tier-facts -->`、`<!-- tier-table -->`）、隱私頁的適用法律／權利／著作權與資料來源段（`<!-- privacy-law -->`）；en／es／de 樣板站的共用長段落縮成一段（`<!-- local-condensed -->`）。
資料檔 `docs/_data/local_facts.json`、`docs/_data/evidence_tier_facts.json` 由 `scripts/local_facts.py`（＝母目錄 `.claude/local_facts_lib.py`）依藥物頁、許可證快照、查核紀錄、FHIR 算；`apply_drug_reviews.py`、許可證快照程式結尾會自動 `--write`，`check_seo_docs.py` 跑 `--check` 擋過期。跨站欄位（cross：本站獨有預測、30 站中位數）與頁面區塊只由母目錄產生器更新；藥物頁改等級、noindex 或預測後要在母目錄重跑。

## 藥物頁 description 句尾在地化（2026-11-19）

用戶 2026-11-19 決定（「藥物頁簡述在地化」，SEO 工具判定 30 站藥物頁近似重複，原因之一是 description 句尾都是同一句「原適應症：本地資料未記載」）：公開藥物頁（排除 noindex、轉址頁）front matter description 句尾的「Opprinnelig indikasjon: Ikke registrert i de lokale dataene」換成本站許可證快照事實層（`snapshots/*_licenses.json.gz`，經 `src/*/regulatory/licenses.py` 的 snapshot()）的品項數句子，資料名稱照本站口徑：EMA 集中許可（不含 DMP 國家許可）。藥名、預測新適應症、等級字樣不動（母目錄 sync_description_levels.py 照舊對得到）；已有原適應症原文的頁不動。
例：acetylsalicylic_acid「Opprinnelig indikasjon: Ikke registrert i de lokale dataene」→「Sentrale EU-godkjenninger (EMA): 3 (gyldige: 3)」；2026-11-19 改了 12 頁。
由母目錄 `.claude/drug_meta_description.py --apply --site NOTxGNN` 產生（站上複本 `tools/txgnn/.claude/drug_meta_description.py --apply --root .`），改動記在 `docs/_data/description_local_log.json`（pages＝目前句尾與原字樣、entries＝每次改動前後整行，可還原）。快照數字變了重跑會換新數字；`apply_drug_reviews.py`、`build_license_snapshot.py` 結尾會自動 --apply，`check_seo_docs.py` 跑 --check 擋「還是未記載句尾」或「數字跟快照不符」。只改 front matter，lastmod_fix 不算正文改動、last_modified_at 不動。
同日修：`apply_drug_reviews.py`、`build_license_snapshot.py` 結尾重算 local_facts 的 atexit 掛鉤在結束時取不到 `__file__`（NameError，之前其實沒跑成），改成先算好路徑。

## 許可證表與正文張數由程式產生（2026-11-24）

用戶 2026-11-24 決定（各站同日，本站做表＋B）：每週許可證排程只改得到概覽表的狀態列／張數列，AI 寫在市場段落的自由格式許可證表（適應症格是 AI 翻成挪威文的 EMA 治療領域）與正文張數句會跟著 EMA 資料過期、讓 checker 擋整頁；改成程式產生、每週自動同步。
- A. 程式許可證表：`scripts/sync_license_tables.py`（範本 DETxGNN／FITxGNN，同為 EMA 資料）依證據包 tfda.records（EMA 集中許可，人用）產生
  「| Godkjenningsnummer | Preparatnavn (EMA) | Virkestoff(er) (EMA, engelsk) | Terapeutisk område (EMA, engelsk) | Status |」：品名、成分、治療領域照 EMA 英文原文、不翻譯（表頭註明語言）；
  狀態照 EMA Medicine status（Authorised→Gyldig、Withdrawn→Trukket tilbake、Lapsed→Bortfalt、Expired→Utløpt、Revoked→Tilbakekalt、Suspended→Suspendert、Refused→Avslått）；
  有效在前、最多 20 列（partial 頁加「Tabellen viser N av M …」）、表後來源句；沒有人用集中許可時一句 NONE_LINE。前後 `<!-- licenses:begin -->`／`<!-- licenses:end -->`。
  取代市場段落（site.MARKET_SECTIONS；這次另加 Norsk markedsinformasjon、Markedsinformasjon i Norge、Markedsinformasjon for Norge/EØS 三種寫法，以前 gate 沒驗）的第一張許可證表；段落沒有表時放在段落結尾。
  `--migrate`（第一次換表時用）拿掉緊鄰舊表、只講舊表列了幾筆的說明句或子句（CAPTION：「De fem første er vist nedenfor.」「Tabellen viser fem av dem.」「Utvalg på 5:」「Et utvalg:」等），查核紀錄更正文字所在的句子不動。
  快照 `snapshots/no_licenses.json.gz` 另存 rows／total；gate 第 18 項（`src/notxgnn/regulatory/licenses.py`）擋程式區塊≠快照重算、市場段落沒有程式表。
  每週排程由 `scripts/license_adapter.py` 的 `sync_tables`（--bundles）重排，PAGE_NOTE 讓 3b 自我檢查接受區塊標記與說明句。
- B. 正文張數改寫：`scripts/rewrite_license_counts.py`＋`src/notxgnn/regulatory/count_prose.py`（移植 Kr／My，句型照 DE 改成挪威文：「N av M godkjenninger er gyldige」「N gyldige tillatelser (av M)」「Det finnes N gyldig tillatelse av M」「Totalt er det N tillatelser」）；
  有保留、講證據包或查詢、相對數、劑型或單方／複方、獸用、國家許可、廠商、表格顯示筆數的句子不動，partial 頁與事實總數 0 的頁整頁不動；0／1 張跨越（單複數）、文字數詞、「alle／begge … gyldig／kansellert」而事實不符的不改、列待查。不寫查核框；gate 第 22 項擋「再跑一次會變」。
- 誰會跑：`scripts/apply_drug_reviews.py`（非 --check）結尾依快照跑 A、B；`scripts/build_license_snapshot.py` 寫完快照再跑一次（`--no-rewrite` 不跑；不給 `--ws` 時用 tools/txgnn）；sync_notes_to_docs.py 整頁重寫後經 apply 也會跑。
- 2026-11-24 套用（資料 data-20261112-163044）：程式表 443 頁（公開頁 444 頁中有市場段落的 443 頁全部換掉；irbesartan 沒有市場段落不加；noindex 頁沒有市場段落）；拿掉舊表說明句 11 處；
  正文張數程式改寫 0 句（現行正文張數 210 句全部跟事實層一致）；判斷不了的 19 句列進待查清單（zero-result 18、word 1，全是下面的「kansellert」句）。
  查核紀錄：被取代表上錨著的 7 筆（6 筆 `no-row-20261112-*`、`no-lic-20261112-tasimelteon-1`）標 superseded（superseded_by programmatic-license-table-2026-11-24）；
  說明框寫死張數（site.FIGURES「Antall godkjenninger i dataene: N, hvorav gyldige: V」）的 209 筆同 id 重發成不寫數字、指向概覽表與程式表（FIGURES 樣板同步改，免得新紀錄又寫死）；
  其中 4 筆（amlodipine、trastuzumab、tadalafil、indacaterol）的更正文字裡有舊表筆數說明句，同一次重發一併刪除；新紀錄 3 筆：rilpivirine（「另一張 kansellert、沒列在表上」，EMA 為 Authorised）、
  vildagliptin（「De to siste er …」講舊表沒列的兩張）、formoterol（「Listen er et utvalg …, og flere av dem gjelder kombinasjonsprodukter」→ 證據包 10 張全是複方）。last_modified_at：正文有變的 443 頁改 2026-11-24。
- 另寫的寬偵測（同句有許可字樣、數字不在事實層 {total, valid, cancelled}，或「alle／begge … gyldig」而有效≠總數，或寫 kansellert 等註銷字而事實沒有註銷）全量掃公開頁：改前 115 句、改後 114 句，剩下全是
  「kansellert」類：正文 136 句（86 頁）與表格裡另一列 AI 寫的張數列 15 格（例 alectinib「Antall autorisasjoner | 1 (kansellert)」、duloxetine「5 (alle kansellert)」；標準的「Antall godkjenninger」列是對的）把 EMA Authorised 的許可寫成 kansellert（11 月 AI 重產時照證據包「Cancelled only」寫的），
  checker 的 no `_CANC_NO` 不含 kansellert、count_row 只驗標準的「Antall godkjenninger」列，所以沒擋。數量超過交付門檻，未在這次處理，待用戶決定（母目錄 `.claude/license_labels/NOTxGNN.json` 也把「Kansellert」記成 valid）。

## 正文「kansellert」的舊錯句更正（2026-11-24 第二輪）

用戶 2026-11-24 決定（第二輪：第一輪列進待查的舊錯句逐句寫查核紀錄更正）：11 月 AI 重產時證據包 local_regulatory 把全部許可標成 Cancelled only（狀態對應壞掉），
正文照著寫「kansellert」（「den eneste norske godkjenningen er kansellert」「begge tillatelser er kansellert」等），概覽表另多一列 AI 寫的張數列（「| Antall tillatelser | 5 (alle kansellert) |」）。
同一 Release（data-20261112-163044）的證據包 tfda.records（EMA 集中許可）與快照事實層都是 Authorised／有效。
- 全量掃公開頁（排除 noindex、轉址頁、查核框、程式區塊）：「kansell」155 處（88 頁）；其中 reteplase「den eneste godkjenningen er kansellert」成立（EMA Withdrawn），不改；
  buprenorphine（4 張中 1 張 Withdrawn）、ustekinumab（13 張中 1 張 Withdrawn）的「alle … kansellert」不成立。
- 154 筆 `no-lic-20261124b-<藥>-N`：只拿掉「kansellert」的子句或前提，其他文字不動；整句只講註銷的句子、概覽表重複的 AI 張數列（15 格，留程式維護的「Antall godkjenninger」列）、
  只建立在註銷前提上的待辦條目（「Avklaring av hvorfor godkjenningen er kansellert」等）刪除；待辦條目的「, siden … er kansellert」前提拿掉、建議保留。
  aztreonam 的「enkeltstoff」說法也不成立（Emblaveo＝avibactam＋aztreonam），整段 Merk 刪除。更正說明不寫張數，指向概覽表與程式許可證表。
  另 2 筆（phenylalanine「tidligere var godkjent」、mometasone「var godkjent」）照 EMA Authorised 改成「er godkjent」。
- 待查清單裡第一輪 B 判斷不了的 19 句全部由上面的紀錄更正，標 resolved（record_ids）。
- 驗證：checker 全量前後 0；母目錄 checker 的 no `_CANC_NO`／`cw`／row 狀態字加上 kansellert 的暫時副本：改前 M3 126 句（82 頁）、改後 0（建議母目錄照這樣加）。gate exit 0。

## 整頁沒有市場段落的公開頁補程式表（2026-11-24 第三輪）

用戶 2026-11-24 第三輪決定（比照 JpTxGNN 第二輪的 `add_section`）：公開頁（非 noindex、非轉址）整頁沒有市場段落（site.MARKET_SECTIONS 任一寫法）、但證據包有人用 EMA 集中許可紀錄的，補「## Markedsinformasjon for Norge」段落與程式表。
- `scripts/sync_license_tables.py` 的 `add_section`：放在「## Sikkerhetsvurderinger」（或 Sikkerhetsmomenter）之前（沒有就「## Konklusjon og neste steg」、再沒有就「## Ansvarsfraskrivelse」）；表照 program_block；noindex 頁、沒有人用集中許可的頁不補。
  apply_drug_reviews.py、build_license_snapshot.py 結尾與每週排程 sync_tables 都會跑；`PAGE_NOTE` 放行補的段落標題行。
- gate 第 18 項（`src/notxgnn/regulatory/licenses.py` 第 5 條）：公開頁快照有程式表列、卻整頁沒有市場段落就擋。
- 2026-11-24 全量量測 1 頁、補 1 頁：irbesartan（10 張 EMA 集中許可，全部 Gyldig）；正文沒有寫死張數或劑型的市場說法，沒有新紀錄。checker 全量前後都是 0；gate exit 0。

## EMA 新集中許可依原規則補收（2026-11-25 第五輪）

用戶 2026-11-25 決定（第五輪第 2 條「新許可補收接進每週排程」；DE、FI、NO 三站同一份 EMA medicines report，同一支邏輯逐站放）：證據包的許可是 collectors/nofda.py 依 data/processed/drug_mapping.csv（2026-03 EMA 清單、scripts/process_fda_data.py 只留 Human＋Authorised，逐成分對 DrugBank）收的，
之後 EMA 新核准（或 2026-03 時還只有 CHMP 意見、之後才核准）的集中許可不在 drug_mapping，每週排程只更新既有號碼的狀態，永遠收不進來。
- `scripts/add_current_ema_products.py [--download | --xlsx 檔] [--dry-run] [--report]`（DE、FI 同一支）：候選＝現行清單裡不在 drug_mapping 的產品號碼、Human、Authorised（照本站基準清單的收錄範圍）、有 Active substance；
  用同一支 map_fda_drugs_to_drugbank 對 DrugBank ID，證據包 tfda.drugbank_ids 有交集、號碼不在證據包的補一筆（欄位照收集器 _format，另記 source、added）；20 筆上限，超過只記 records_not_stored、算進 total_matches。只加不刪、可重複執行。
  --download 把現行清單存成 data/raw/ema_medicines_report_current.xlsx（Release 帶著）。`.github/workflows/license-refresh.yml` 在 license_refresh 前以 --download 跑，有補收就照常發新 Release。
- 2026-11-25 第一次跑（清單 2026-11-25，2,765 筆）：現行候選 54 筆、對到 DrugBank 26 筆；17 個證據包補 23 筆（records 22、只算張數 1（denosumab）），全部 Authorised；第二次跑 0 筆。
  mapper 不認 hemifumarate 鹽類的 ruxolitinib 學名藥（原規則一樣對不到）不補。證據包 local_regulatory 重算 10 個；概覽狀態列／張數列 10 頁、程式表 11 頁由程式同步，正文張數 B 改寫 1 句（pegfilgrastim）；data overlay 推 `claude/data-overlay-NOTxGNN-emanew`。
- 正文跟新事實矛盾、B 判斷不了的 4 句（文字數詞）以 `no-lic-20261125-*` 更正（insulin_glargine「Alle fem tillatelser … (5 av 5)」「Alle fem norske tillatelser」、insulin_lispro「Alle fire godkjenningene」「med fire gyldige godkjenninger」），
  `no-lic-20261112-ranibizumab-1`（更正文字「Alle syv godkjenningene er gyldige」）同 id 重發成不寫數字（前版存 history）。
- 驗證：改到的 11 頁（都是公開頁）逐頁掃許可張數／全稱／唯一字樣；checker 前後都是 0、row-status 0；gate exit 0。
