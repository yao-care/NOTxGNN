---
layout: default
title: Chenodeoxycholic Acid
parent: 僅模型預測 (L5)
nav_order: 86
evidence_level: L5
indication_count: 5
---

# Chenodeoxycholic Acid
{: .fs-9 }

證據等級: **L5** | 預測適應症: **5** 個
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

# Chenodeoxycholic Acid：原始適應症資料缺失 → 預測新適應症「同型合子家族性高膽固醇血症」(HoFH)

## 一句話摘要

> 鵝去氧膽酸（Chenodeoxycholic Acid, DB06777）目前**原始適應症與作用機轉資料均缺失**（Data Gap DG002），且尚未於台灣上市（許可證 0 張）。
> TxGNN 模型預測其可能對**同型合子家族性高膽固醇血症（HoFH）**有效，
> 但目前僅有 **0 項臨床試驗**與 **1 篇文獻**支持，且該文獻實際主題為腦腱黃瘤病（CTX）而非 HoFH，證據力極弱。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原始適應症 | 資料缺失（`original_indications` 為空，`original_moa` 亦未提供，見 DG002） |
| 預測新適應症 | 同型合子家族性高膽固醇血症（Homozygous Familial Hypercholesterolemia, HoFH） |
| TxGNN 預測分數 | 99.57%（原始 rank 5013） |
| 證據等級 | L5（僅模型預測，無臨床試驗，唯一文獻主題不符） |
| 台灣上市狀態 | 未上市 |
| 許可證張數 | 0 |
| 建議決策 | Hold |

---

## 為什麼這個預測看似合理？

目前尚無詳細作用機轉（MOA）資料可供查證（Data Gap DG002）。根據已知的一般藥理知識，鵝去氧膽酸為天然膽酸之一，可活化 FXR（法尼醇 X 受體）並回饋抑制 CYP7A1，進而降低膽固醇轉化為膽酸的速率——理論上與脂質代謝路徑有間接關聯。

Rank 1 預測適應症 HoFH 的病因是 LDL 受體基因功能喪失，導致血中 LDL 膽固醇無法被有效清除。CDCA 經 FXR/CYP7A1 路徑調控的是膽固醇「下游代謝」，並無已知機轉可代償 LDL 受體本身的功能缺陷，機轉關聯性薄弱。

更關鍵的是，附帶的唯一支持文獻（PMID 25424010）實際探討主題為**腦腱黃瘤病（CTX）**，與 HoFH 是病因完全不同的兩種疾病，僅因臨床上皆可能出現黃瘤（xanthoma）表現而被疾病本體標籤誤配，並非真實佐證。其餘四項候選適應症（rank 2–5）機轉關聯性更薄弱：rank 2、3 為 COL4A1 相關血管/眼部先天異常，與膽酸代謝無已知交集，rank 2 附帶的 19 篇文獻多為各類先天眼部畸形個案回顧，與 CDCA 藥理完全無關，屬關鍵字誤配所致雜訊；rank 4、5 的疾病本體標籤本身標示為「obsolete」（已棄用術語），顯示本體資料品質問題。整體而言，本次預測群組不具臨床可解釋性。

---

## 臨床試驗證據

目前無相關註冊臨床試驗。

---

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 重點摘要 |
|------|-----|------|------|---------|
| [25424010](https://pubmed.ncbi.nlm.nih.gov/25424010/) | 2014 | Review (Tier 3) | Orphanet Journal of Rare Diseases | 本文為腦腱黃瘤病（CTX）之致病機轉、臨床表現、診斷與治療的完整回顧，**主題並非 HoFH**；研判為疾病標籤誤配所致的文獻雜訊，不構成 HoFH 適應症之直接佐證。 |

---

## 台灣市場資訊

目前查無台灣上市許可資料，本藥物尚未於台灣獲證上市。

---

## 安全性考量

目前尚無台灣仿單警語、禁忌症及藥物交互作用資料（Data Gap DG001，嚴重度：**Blocking**，此缺口將阻擋 S1 安全性初評）。待取得 TFDA 官方仿單並解析後方可補充完整安全性評估。

---

## 結論與後續步驟

**決策：Hold**

**理由：**
- 所有 5 項預測適應症之證據等級均為 L5——僅有模型預測分數，無臨床試驗支持，且唯一附帶文獻主題不符（或完全無關），機轉關聯性薄弱甚至為疾病標籤誤配所致的雜訊；
- 藥物原始適應症與作用機轉資料缺失（DG002, High），且台灣仿單警語/禁忌症資料缺失（DG001, Blocking），無法進行 S1 安全性初評。

**若要推進，需要補充：**
- 取得 DrugBank 或原廠仿單之正式作用機轉（MOA）與原始核准適應症資料
- 取得 TFDA 官方仿單 PDF 並解析警語、禁忌症與藥物交互作用，以解除 DG001 Blocking 缺口
- 針對 rank 1 候選（HoFH）補充主題真正相符的臨床試驗或文獻證據——目前唯一文獻（CTX）與 HoFH 不符
- 檢視疾病本體（ontology）資料品質，排除 rank 3–5 候選中「obsolete」已棄用術語及與藥理機轉無關的疾病標籤誤配問題
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

