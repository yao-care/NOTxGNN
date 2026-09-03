---
layout: default
title: Pitolisant
parent: 中證據等級 (L3-L4)
nav_order: 281
evidence_level: L4
indication_count: 3
---

# Pitolisant
{: .fs-9 }

證據等級: **L4** | 預測適應症: **3** 個
{: .fs-6 .fw-300 }

---

## 目錄
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## 藥師評估報告

</div>

# Pitolisant：從嗜睡症（Narcolepsy）到失眠（Insomnia）？

## 一句話總結

Pitolisant 是一種組織胺 H3 受體反向促效劑，國際上核准用於成人及兒童猝睡症（narcolepsy）與 OSA 患者的殘餘日間嗜睡，藥理作用為**促進清醒**。TxGNN 模型預測其可能對**失眠（Insomnia）**有效，但此推論與藥物機轉方向相反，現有 **1 篇試驗（已撤回、招募人數 0）**與 **8 篇文獻（皆未針對失眠）**均無法支持此關聯，判斷為知識圖譜產生的低可信度預測。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原始適應症 | 台灣/本地無正式核准資料（尚未上市）；依國際文獻，歐美已核准用於成人及 ≥6 歲兒童猝睡症（合併或不合併猝倒症），及 OSA 患者接受 CPAP 治療後之殘餘日間嗜睡 |
| 預測新適應症 | 失眠（Insomnia） |
| TxGNN 預測分數 | 99.71% |
| 證據等級 | L4 |
| 本地上市狀況 | 未上市 |
| 核准許可證數量 | 0 |
| 建議決策 | **Hold** |

---

## 為什麼需要謹慎看待此預測？

目前尚無 Pitolisant 的正式作用機轉（MOA）資料庫紀錄（DrugBank 欄位為資料缺口），但根據證據包中多篇文獻描述：**Pitolisant 是選擇性組織胺 H3 受體反向促效劑（inverse agonist）**，其作用是抑制突觸前 H3 自體受體，進而增加腦內組織胺（及間接的多巴胺、正腎上腺素）釋放，藥理效果為**促進清醒（wake-promoting）**。此機轉已被證實可有效治療猝睡症的白日過度嗜睡，以及 OSA 患者對 CPAP 治療反應不佳的殘餘嗜睡。

問題在於：**失眠（insomnia）需要的是促進睡眠，而非促進清醒**，兩者治療方向在藥理學上直接矛盾。文獻中 PMID 34521328 甚至明確對比指出，pitolisant 用於嗜睡症治療，而 H1 拮抗劑 doxepin 才是用於失眠——兩者機轉相反。

唯一與失眠標籤相關的臨床試驗（NCT02800083）實際上是針對**酒精使用障礙（Alcohol Use Disorder）**設計，並非失眠試驗，且該試驗狀態為 WITHDRAWN、招募人數為 0，不具參考價值。綜合判斷，此預測極可能是 TxGNN 知識圖譜嵌入產生的偽關聯（可能與 narcolepsy/嗜睡症本體分類混淆有關），不建議作為機轉合理性佐證。

---

## 臨床試驗證據

| 試驗編號 | 期別 | 狀態 | 收案人數 | 重點發現 |
|---------|------|------|------|---------|
| [NCT02800083](https://clinicaltrials.gov/study/NCT02800083) | Phase 2 | Withdrawn | 0 | 實際設計為評估 pitolisant 用於**酒精使用障礙**治療之隨機雙盲試驗，非失眠試驗；已撤回、無受試者資料，不能作為失眠證據（relevance grade C） |

---

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 重點發現 |
|------|-----|------|------|---------|
| [36931805](https://pubmed.ncbi.nlm.nih.gov/36931805/) | 2023 | RCT（兒童猝睡症） | Lancet Neurol | Pitolisant 用於 ≥6 歲兒童猝睡症（合併/不合併猝倒症）之安全性與療效，非失眠適應症 |
| [33121980](https://pubmed.ncbi.nlm.nih.gov/33121980/) | 2021 | RCT（OSA 殘餘嗜睡） | Chest | Pitolisant 改善 CPAP 治療下 OSA 患者殘餘日間嗜睡 |
| [36169322](https://pubmed.ncbi.nlm.nih.gov/36169322/) | 2022 | 真實世界世代研究 | Rev Neurol | 難治性第一型猝睡症患者使用 pitolisant 之療效與安全性 |
| [31917607](https://pubmed.ncbi.nlm.nih.gov/31917607/) | 2020 | RCT（OSA 白日嗜睡） | Am J Respir Crit Care Med | Pitolisant 用於拒絕 CPAP 治療之中重度 OSA 患者白日嗜睡 |
| [34521328](https://pubmed.ncbi.nlm.nih.gov/34521328/) | 2022 | Review | Curr Neuropharmacol | 組織胺系統與神經精神疾病：明確區分 pitolisant（促清醒，治嗜睡）與 doxepin（H1 拮抗劑，治失眠）之相反機轉 |
| [30214155](https://pubmed.ncbi.nlm.nih.gov/30214155/) | 2018 | Review | Drug Des Devel Ther | Pitolisant 用於猝睡症之藥物發展綜述 |
| [22356925](https://pubmed.ncbi.nlm.nih.gov/22356925/) | 2012 | Review/藥理學 | Clin Neuropharmacol | H3 自受體阻斷增加腦內組織胺、促進清醒，用於青少年難治性嗜睡 |
| [34225942](https://pubmed.ncbi.nlm.nih.gov/34225942/) | 2021 | Review | Handbook Clin Neurol | 組織胺受體（H1-H4）機轉綜述，未涉及失眠治療 |

**注意：以上 8 篇文獻皆圍繞猝睡症或 OSA 嗜睡治療，無一篇直接研究 pitolisant 於失眠之應用。**

---

## 台灣上市資訊

目前 Pitolisant 尚未於本地市場上市，無核准許可證資料。

---

## 安全性考量

請參考藥品仿單以取得完整安全性資訊。

> ⚠ 資料缺口提醒：TFDA 仿單警語/禁忌資料為 **Blocking** 等級缺口（DG001），在補齊前無法進行 S1 安全性初評。

---

## 結論與後續行動

**決策：Hold**

**理由：**
- 失眠適應症的藥理機轉與 pitolisant 的清醒促進作用方向相反，屬機轉矛盾；唯一相關試驗實際針對酒精使用障礙、已撤回且零收案，8 篇文獻均與失眠無直接關聯。判斷此為 TxGNN 知識圖譜的低可信度／偽關聯預測，證據等級 L4 但方向性存疑。
- 藥物尚未於本地上市（0 張許可證），且 TFDA 仿單警語/禁忌資料為 Blocking 缺口，即使未來考慮其他適應症方向，也無法略過此步驟進入安全性評估。

**若要繼續推進，需要：**
- 補齊 TFDA 仿單警語與禁忌資料（DG001，Blocking，來源：TFDA 官網仿單 PDF）
- 補齊 DrugBank 完整作用機轉（MOA）資料（DG002，High，來源：DrugBank API）
- 若欲探索失眠以外的其他新適應症方向，建議優先評估與原始核准適應症（猝睡症、OSA 嗜睡）機轉一致的候選，而非目前排名較低但機轉方向矛盾的失眠假說

**補充：其他預測適應症僅供參考，暫不建議投入資源**
- ADHD（rank 2，L5，Research Question）：機轉上 H3 拮抗劑可能改善認知/專注力，但 7 篇文獻皆為藥物類別層級的綜述，pitolisant 本身無 ADHD 臨床試驗資料
- Faciodigitogenital syndrome（rank 3，L5，Hold）：無任何機轉、文獻或試驗支持，判斷為知識圖譜噪音，不建議投入任何資源
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

