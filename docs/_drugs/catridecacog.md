---
layout: default
title: Catridecacog
parent: 僅模型預測 (L5)
nav_order: 78
evidence_level: L5
indication_count: 3
---

# Catridecacog
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

# Catridecacog：從凝血因子 XIII 替代治療到原發性血小板釋放障礙

## 一句話總結

Catridecacog 是重組人類凝血因子 XIII A 次單元，作用機轉為促進纖維蛋白交聯、穩定已形成的血栓。目前原始適應症資料尚未取得，僅能由藥物機轉推論其傳統用途與凝血因子 XIII 相關出血疾病有關。TxGNN 模型預測其可能與 **Primary release disorder of platelets（原發性血小板釋放障礙）** 有關，預測分數達 **99.29%**，但**目前無任何臨床試驗或文獻證據**支持此連結。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原始適應症 | 資料缺口（`original_indications` 未提供；由機轉推論與凝血因子 XIII 缺乏/出血傾向相關） |
| 預測新適應症 | Primary release disorder of platelets |
| TxGNN 預測分數 | 99.29%（rank 7143） |
| 證據等級 | L5（僅模型預測，無臨床試驗或文獻支持） |
| 挪威市場狀態 | 未上市 |
| 許可證數量 | 0 |
| 建議決策 | Hold |

## 為什麼這個預測合理？

目前作用機轉資料本身即為資料缺口，但根據 Evidence Pack 中的機轉關聯分析可推知：Catridecacog 為重組凝血因子 XIII A 次單元，作用於凝血級聯的**終端步驟**——促進纖維蛋白交聯以穩定已形成的血栓。這是一個「結構穩定」型機轉，而非參與血小板活化、聚集或顆粒釋放的路徑。

Primary release disorder of platelets（原發性血小板釋放障礙）的病理機轉是血小板活化後**顆粒分泌功能異常**，屬於血小板功能層次的問題，與凝血因子 XIII 所處的纖維蛋白交聯層次並無已知直接生理路徑重疊。兩者僅在「出血傾向疾病」這個表型分類上相似，TxGNN 給出的高分較可能反映的是**知識圖譜中出血相關疾病節點的表型鄰近性**，而非真實的機轉因果關係。在原始 MOA 與適應症資料完整補齊之前，這個關聯仍屬推測層級，無法排除也無法證實。

> 補充：同一批次（`TW-DB09310-multi`）另有兩個相關預測，供決策參考：

| 排序 | 預測適應症 | TxGNN 分數 | 機轉合理性摘要 |
|---|---|---|---|
| 2 | Pseudo-von Willebrand disease | 99.29% | 病理為血小板 GPIbα 受體功能異常，與 Factor XIII 機轉無直接關聯，屬表型相似驅動的預測 |
| 3 | Glanzmann thrombasthenia | 99.15% | GPIIb/IIIa 整合素缺陷，理論上 Factor XIII 或可作為血栓結構穩定的輔助手段，但無任何實證支持 |

## 臨床試驗證據

目前無相關臨床試驗登記。

## 文獻證據

目前無相關文獻可供參考。

## 挪威市場資訊

此藥品目前於挪威**未取得任何上市許可**（`market_status: 未上市`，`total_licenses: 0`），無授權登記資料可供列表。

## 安全性考量

請參考藥品仿單所載安全性資訊。

> 提醒：根據資料缺口清單，「TFDA 仿單警語/禁忌」屬 **Blocking** 等級缺口（DG001），在取得完整仿單資料之前，本候選藥物**無法進入 S1 安全性初評階段**。

## 結論與下一步

**決策：Hold**

**理由：**
- 兩個候選預測皆停留在 **L5**（僅模型預測），無任何臨床試驗或文獻佐證機轉關聯性；
- 安全性資料存在 Blocking 等級缺口（DG001：TFDA 仿單警語/禁忌未知），依規範無法進入下一階段安全性評估。

**若要繼續推進，需要補齊：**
- TFDA／原廠仿單完整警語與禁忌資料（DG001，Blocking，來源：TFDA 官網，方法：下載仿單 PDF 並解析）
- DrugBank 作用機轉（MOA）完整資料（DG002，High，來源：DrugBank API）
- 原始適應症（`original_indications`）確認，以利與預測適應症進行機轉關聯比對
- 持續監測是否出現新的臨床試驗登記或文獻，作為證據等級升級依據
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

