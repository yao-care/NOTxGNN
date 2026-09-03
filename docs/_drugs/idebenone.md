---
layout: default
title: Idebenone
parent: 僅模型預測 (L5)
nav_order: 174
evidence_level: L5
indication_count: 10
---

# Idebenone
{: .fs-9 }

證據等級: **L5** | 預測適應症: **10** 個
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

# Idebenone：目前無核准適應症 → 預測新適應症 Hepatic Porphyria（肝性紫質症）

## 一句話總結

Idebenone（艾迪苯醌）目前在市場上尚無核准適應症，也未在 Norway 上市，公開資料顯示其為合成 CoQ10 類似物，主要作用於粒線體電子傳遞鏈支持與抗氧化。TxGNN 模型預測其可能對**肝性紫質症（Hepatic Porphyria）**有效，但目前**0 篇臨床試驗**與**0 篇文獻**支持此方向，證據等級為最低的 **L5**（純模型預測）。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原始適應症 | 尚無核准適應症紀錄（藥品未上市） |
| 預測新適應症 | Hepatic porphyria（肝性紫質症） |
| TxGNN 預測分數 | 99.92% |
| 證據等級 | L5 |
| Norway 市場狀態 | 未上市 |
| 授權張數 | 0 |
| 建議決策 | Hold |

---

## 為什麼這個預測合理？

由於 DrugBank 的 `original_moa` 欄位標記為資料缺口，本節改以模型推理文字中提供的機轉描述為依據：Idebenone 為合成 CoQ10（輔酶 Q10）類似物，主要作用是抗氧化及支持粒線體電子傳遞鏈——其獨特之處在於可繞過 Complex I，直接將電子傳遞至 Complex III，因此在粒線體功能受損的疾病中具有理論基礎。

然而，肝性紫質症的病理機轉主要為血基質（heme）合成路徑中特定酵素缺陷，導致紫質前驅物在肝臟或紅血球中堆積，這與粒線體氧化磷酸化功能之間並無已知的直接關聯。換言之，TxGNN 給出的高分（99.92%）較可能反映知識圖譜中的間接關聯（例如兩者皆與「肝臟」節點相連），而非具體的藥理機轉證據。

此外，本次 Evidence Pack 中共列出 10 項 TxGNN 預測適應症，除本報告聚焦的肝性紫質症外，其餘 9 項（如 idiopathic copper-associated cirrhosis、primitive portal vein thrombosis、immune-mediated necrotizing myopathy 等）證據等級同樣為 L5，僅有 2 項（immune-mediated necrotizing myopathy、antisynthetase syndrome）因與 idebenone 已知的粒線體肌肉疾病應用經驗（如 Duchenne 肌肉失養症）機轉相似度較高，被標記為 S1「Research Question」，其餘均為 S0「Hold」。

---

## 臨床試驗證據

目前無相關臨床試驗登記。

---

## 文獻證據

目前無相關文獻資料。

---

## Norway 市場資訊

Idebenone 目前**未在 Norway 上市**，無任何有效授權（total_licenses = 0），故無可列示之核准產品資訊。

---

## 安全性考量

請參閱藥品仿單以取得完整安全性資訊。

> 補充說明：本次 Evidence Pack 標記 TFDA 仿單警語／禁忌（DG001）為 **Blocking** 等級資料缺口，這意味著在缺乏該資料前，本候選藥物**無法進入 S1 安全性初評階段**，此為決策為 Hold 的關鍵原因之一。

---

## 結論與後續建議

**決策：Hold**

**理由：**
- 排名第一之預測適應症（肝性紫質症）證據等級為 L5，無任何臨床試驗或文獻支持，機轉關聯性亦被自評為薄弱（純屬圖譜關聯推測）。
- 安全性資料缺口（TFDA 仿單警語/禁忌）為 Blocking 等級，依現行規則無法進入 S1 安全性初評。

**若要推進，需要補充：**
- TFDA 仿單警語與禁忌資料（DG001，Blocking）
- DrugBank 完整作用機轉（MOA）資料，以強化機轉關聯性分析（DG002，High）
- 針對機轉合理性較高的候選適應症（immune-mediated necrotizing myopathy、antisynthetase syndrome）優先蒐集臨床前或病例文獻，作為後續研究假說驗證起點
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

