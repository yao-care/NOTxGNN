---
layout: default
title: Glimepiride
parent: 僅模型預測 (L5)
nav_order: 163
evidence_level: L5
indication_count: 9
---

# Glimepiride
{: .fs-9 }

證據等級: **L5** | 預測適應症: **9** 個
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

# Glimepiride：從第二型糖尿病到 Focal Stiff Limb Syndrome（機轉關聯性存疑）

## 一句話總結

Glimepiride 是磺醯脲類（sulfonylurea）口服降血糖藥物，作用於胰臟 β 細胞 KATP 通道促進胰島素分泌。
TxGNN 模型預測其可能對 **Focal Stiff Limb Syndrome** 有效，
但目前**無臨床試驗、無文獻支持**，且模型自身生成的機轉推論已明確指出此為知識圖譜的潛在偽陽性連結。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原始適應症 | 第二型糖尿病（依藥理學常識推斷；本 Evidence Pack 未提供正式核准適應症文字，`original_indications` 為空） |
| 預測新適應症 | Focal Stiff Limb Syndrome |
| TxGNN 預測分數 | 99.75%（rank 3254 / 全庫排序） |
| 證據等級 | L5（僅模型預測，無實際研究） |
| 當地市場狀態 | ✗ 未上市 |
| 核准證號數量 | 0 |
| 建議決策 | **Hold** |

---

## 為什麼這個預測合理性存疑？

Glimepiride 的作用機轉為阻斷胰臟 β 細胞 KATP 通道（SUR1/Kir6.2 次單元），促使細胞去極化、鈣離子流入，進而刺激胰島素分泌，屬於典型的磺醯脲類降血糖藥物機轉。此機轉高度侷限於胰島 β 細胞與血糖調控路徑。

Focal Stiff Limb Syndrome 屬於 Stiff Person Syndrome 光譜疾病，核心病理為抗 GAD65 抗體導致中樞神經系統 GABA 合成障礙，造成肌肉僵直與痙攣，本質上是自體免疫神經系統疾病，與磺醯脲類藥物的胰島素分泌機轉並無已知交集。

依 Evidence Pack 提供之 `repurposing_rationale`，此高分預測**極可能是知識圖譜偽陽性**：GAD65 蛋白同時表現於中樞神經系統 GABA 能神經元與胰臟 β 細胞，TxGNN 很可能是透過「GAD65／糖尿病」這個共病捷徑產生錯誤的高分關聯，而非反映真實的藥理學合理性。目前無法建立支持此預測的生物學假說，亦無任何機轉層級（MOA）正式資料可供驗證——`original_moa` 為 Data Gap，屬於本案高優先級待補資訊。

> 補充：本組九個候選適應症中，第 9 名「Pancreatic agenesis」的機轉假說相對較合理（磺醯脲類已知可用於 KATP 通道基因 KCNJ11/ABCC8 突變之新生兒糖尿病），但因胰臟發育不全患者可能缺乏足量功能性 β 細胞，合理性仍存在重大不確定性，且僅有的文獻（PMID 12720536）與此適應症無直接相關。此候選值得留意但仍不足以支持進入下一階段。

---

## 臨床試驗證據

目前無相關臨床試驗登記。

---

## 文獻證據

目前無相關文獻可查。

---

## 當地市場資訊

本藥品目前**未於當地市場核准上市**，無有效核准證號資料（`total_licenses` = 0）。

---

## 安全性考量

請參閱藥品仿單以獲得安全性資訊。

> 注意：`data_gaps` 中標記「TFDA 仿單警語/禁忌」為 **Blocking** 等級缺口，直接影響安全性初評（S1）之進行，需優先補齊。

---

## 結論與後續步驟

**決策：Hold**

**理由：**
- 證據等級為 L5，僅有模型預測分數，無任何臨床試驗或文獻支持。
- 模型自身生成的機轉推論已明確指出此為知識圖譜偽陽性（透過 GAD65 節點產生的間接連結），缺乏生物學合理性。
- 藥物尚未於當地市場核准上市，且作用機轉（MOA）與安全性仿單資料均為待補缺口，無法進行安全性初評。

**若要繼續推進，需要補齊：**
- Glimepiride 正式 MOA 資料（DrugBank API 查詢）
- TFDA／當地主管機關仿單警語與禁忌症資料（解決 Blocking 缺口 DG001）
- 針對 Stiff Person Syndrome 光譜疾病與磺醯脲類藥物之間，尋求任何體外／動物實驗或病例報告等初步機轉證據
- 若優先順序調整，建議另行評估第 9 名候選「Pancreatic agenesis」，因其具備相對明確的 KATP 通道機轉基礎，值得獨立檢視是否有 KCNJ11/ABCC8 相關案例報告可支持
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

