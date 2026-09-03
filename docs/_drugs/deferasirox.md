---
layout: default
title: Deferasirox
parent: 僅模型預測 (L5)
nav_order: 100
evidence_level: L5
indication_count: 5
---

# Deferasirox
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

# Deferasirox：從鐵過載治療 到 HIV 感染症預測

## 一句話摘要

Deferasirox 是一款口服三價鐵螯合劑，本 Evidence Pack 未提供其正式核准適應症資料，但依既有藥理學知識，臨床上用於治療輸血相關鐵過載。TxGNN 模型將其預測適應症中排名第一的訊號指向 **HIV 感染症**，目前僅有 **2 篇文獻**（機轉性體外研究與藥品新聞回顧）支持，**無任何已註冊臨床試驗**，證據強度偏弱。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原始適應症 | 資料缺失（`original_indications` 未提供、Norway 未上市無授權資料可查） |
| 預測新適應症 | HIV infectious disease |
| TxGNN 預測分數 | 99.40% |
| 證據等級 | L4（機轉/臨床前研究層級） |
| Norway 市場狀態 | ✗ 未上市 |
| 授權數量 | 0 |
| 建議決策 | Hold |

---

## 為何此預測具合理性？

目前尚無詳細作用機轉（MOA）正式資料（`original_moa` 標示為 Data Gap）。根據 Evidence Pack 中的關聯性分析，Deferasirox 為口服三價鐵螯合劑，其主要藥理作用是降低胞內游離鐵濃度，臨床上多用於鐵過載相關病症；此機轉在鐵代謝與病毒交互作用領域可能具有延伸適用性。

支持 HIV 適應症預測的機轉假說來自一篇體外研究：endolysosome 中的鐵離子濃度會影響 HIV-1 Tat 蛋白的寡聚化程度，進而調控 LTR 轉錄活化（PMID 34550543）。此假說認為鐵螯合可能間接抑制病毒轉錄活化，但這是**間接的鐵代謝-病毒交互作用假說**，並非藥物直接抗病毒機轉，也尚未有任何臨床試驗驗證此一路徑在人體中的有效性。

另需說明，本 Evidence Pack 同時列出另外 4 個 TxGNN 預測訊號（chronic HCV、罕見神經發育疾病、obsolete 家族性混合型高血脂症、dermatofibrosarcoma protuberans），其證據等級多為 L5（純模型預測、無文獻或臨床證據支持），建議狀態均為 Hold，故本報告聚焦於證據相對較完整的 HIV 適應症訊號（rank 1）。

---

## 臨床試驗證據

目前無相關已註冊臨床試驗

---

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 關鍵發現 |
|------|-----|------|------|---------|
| [34550543](https://pubmed.ncbi.nlm.nih.gov/34550543/) | 2021 | Preclinical mechanistic study | Journal of Neurovirology | Endolysosome 內鐵離子濃度會限制 HIV-1 Tat 蛋白寡聚化與 β-catenin 表現，進而抑制 Tat 介導之 HIV-1 LTR transactivation（體外機轉研究） |
| [16529348](https://pubmed.ncbi.nlm.nih.gov/16529348/) | 2006 | Review/Drug news | Journal of the American Pharmacists Association | 屬於新藥上市回顧報導（涵蓋 ramelteon、tipranavir、nepafenac、deferasirox），未提供 deferasirox 與 HIV 相關之具體療效資料 |

---

## Norway 市場資訊

目前 Deferasirox 於 Norway 市場狀態為「未上市」，無授權（licenses）資料可供列示。

---

## 安全性考量

請參閱藥品仿單以獲取安全性資訊（本 Evidence Pack 中之警語、禁忌、藥物交互作用資料均標示為 Data Gap，且 DG001 已列為 Blocking 等級缺口，尚待自 TFDA 官網取得正式仿單資料）。

---

## 結論與後續建議

**決策：Hold**

**理由：**
現有支持 HIV 適應症的證據僅為單篇體外機轉研究（L4），缺乏任何臨床試驗或人體驗證資料；同時安全性仿單資料（警語、禁忌）為 Blocking 等級缺口（DG001），在此資料補齊前無法進行 S1 安全性初評，尚不足以支持進入後續開發階段。

**若欲推進，需補充：**
- TFDA 仿單警語與禁忌資料（DG001，Blocking，需下載並解析官方仿單 PDF）
- 完整作用機轉（MOA）資料（DG002，High，可透過 DrugBank API 查詢補齊）
- 針對「鐵螯合-HIV Tat 轉錄調控」假說之體內驗證研究，或至少建立此適應症之臨床前/早期臨床試驗規劃
- 藥物交互作用（DDI）正式查詢結果，目前為 not_found 狀態
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

