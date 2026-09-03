---
layout: default
title: Empagliflozin
parent: 僅模型預測 (L5)
nav_order: 129
evidence_level: L5
indication_count: 3
---

# Empagliflozin
{: .fs-9 }

證據等級: **L5** | 預測適應症: **3** 個
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

# Empagliflozin：原始適應症資料缺失 → 預測新適應症為 Focal Stiff Limb Syndrome

## 一句話摘要

Empagliflozin（SGLT2 抑制劑）在本 Evidence Pack 中原始適應症與作用機轉均標示為資料缺口，無法確認其既有臨床用途。TxGNN 模型預測其對 **Focal Stiff Limb Syndrome**（與 Classic Stiff Person Syndrome 同分並列）具有潛在效果，但**目前無任何臨床試驗、無任何文獻佐證**，且模型附帶的機轉分析本身已指出兩者間**無已知生物學關聯**。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原始適應症 | 資料缺失（Evidence Pack 未提供，對應 DG001） |
| 預測新適應症 | Focal Stiff Limb Syndrome（Rank 1，與 Classic Stiff Person Syndrome 同分） |
| TxGNN 預測分數 | 99.06% |
| 證據等級 | L5（純模型預測，無試驗、無文獻） |
| 台灣上市狀態 | 未上市 |
| 許可證數量 | 0 |
| 建議決策 | Hold |

## 為什麼這個預測合理？

目前沒有完整的作用機轉（MOA）資料——Evidence Pack 中 `original_moa` 欄位本身即標示為資料缺口（DG002）。根據 TxGNN 附帶的機轉關聯敘述，可得知 empagliflozin 屬 SGLT2 抑制劑，藥理作用為抑制腎臟近曲小管的鈉-葡萄糖共同運輸蛋白 2（SGLT2），減少腎臟對葡萄糖的再吸收。

由於 `original_indications` 與 `taiwan_regulatory.licenses` 均為空值，無法比對此藥物已核准用途與三個預測適應症（focal stiff limb syndrome、classic stiff person syndrome、opsismodysplasia）之間的關聯性。

更關鍵的是，TxGNN 自身附帶的機轉分析已明確指出：這三個預測適應症在生物學機轉上與 SGLT2 抑制劑的腎臟/代謝作用路徑**無已知關聯**——stiff limb/person syndrome 屬自體免疫神經傳導疾病（核心病理為抗 GAD65 抗體導致 GABA 能抑制性傳導缺損），opsismodysplasia 則為 INPPL1 基因突變引起的骨骼發育不良疾病。三者皆缺乏臨床前或臨床證據支持此連結，屬純演算法高分預測，不具生物學合理性佐證。

## 臨床試驗證據

目前無相關臨床試驗登記。

## 文獻證據

目前無相關文獻資料。

## 台灣市場資訊

Empagliflozin 目前**未在台灣上市**，查驗登記許可證數量為 0，無許可證明細資料可列示。

## 安全性考量

請參考藥品仿單以取得完整安全性資訊（Evidence Pack 中之 key_warnings、contraindications 與藥物交互作用資料目前均為資料缺口，DDI 查詢結果為 not_found）。

## 結論與後續步驟

**決策：Hold**

**理由：**
三項預測適應症證據等級均為 L5（純模型預測），無任何臨床試驗或文獻佐證，且 TxGNN 自身機轉分析已指出與原始藥理路徑無已知關聯；同時藥物層級仍有 Blocking 級資料缺口（TFDA 仿單警語/禁忌），尚未具備進入下一階段安全性初評（S1）的最低條件。

**若要繼續推進，需要補齊：**
- TFDA 仿單警語與禁忌資料（DG001，Blocking，為進入 S1 安全性初評之前提）
- 完整作用機轉（MOA）資料（DG002）
- 針對三項預測適應症，檢索是否存在臨床前動物實驗或個案報告可支持機轉合理性
- 若持續無法建立生物學合理性，建議暫緩此候選藥物-適應症配對的後續資源投入
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

