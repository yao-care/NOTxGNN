---
layout: default
title: Diflunisal
parent: 僅模型預測 (L5)
nav_order: 109
evidence_level: L5
indication_count: 10
---

# Diflunisal
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

# Diflunisal:從 NSAID 消炎鎮痛藥物到僵直性脊椎炎（Ankylosing Spondylitis）

> **選案說明**：Evidence Pack 中 TxGNN 分數最高的第 1–4、6–9 名（如 acromesomelic dysplasia、brachyolmia 等）皆為極罕見遺傳性骨骼/結構性疾病，且各筆 `repurposing_rationale` 已明確指出機轉不成立、無任何臨床證據，屬於知識圖譜雜訊（L5/S0/Hold）。本報告以唯一具備實質文獻證據的第 5 名候選——**僵直性脊椎炎**——為主體評估對象（第 10 名 inflammatory spondylopathy 屬同一疾病譜系，證據重疊，一併說明）。

## 一句話摘要

Diflunisal 的原始核准適應症在本次 Evidence Pack 中缺乏台灣仿單資料（無上市許可紀錄）。
TxGNN 模型預測其可能對**僵直性脊椎炎**有效，但文獻回顧顯示此關聯**並非新穎再利用**，而是 NSAID 藥物類別的既有臨床應用範疇；目前有 **0 件臨床試驗**、**7 篇相關文獻**（其中僅 3 篇為 diflunisal 本品的直接研究，1 篇為 RCT）支持此方向。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原始適應症 | 資料缺口（`taiwan_regulatory.licenses` 為空，無核准適應症紀錄可查） |
| 預測新適應症 | Ankylosing Spondylitis（僵直性脊椎炎） |
| TxGNN 預測分數 | 99.98%（rank 373） |
| 證據等級 | L2（1 件已完成之 Phase 2/3 等級 RCT，1986 年） |
| 台灣上市狀態 | 未上市 |
| 許可證數量 | 0 |
| 建議決策 | **Hold** |

## 為什麼這個預測合理？

目前尚無 DrugBank 詳細作用機轉資料（`original_moa` 為資料缺口）。根據現有文獻與同組候選項的 `repurposing_rationale` 描述，Diflunisal 屬於非類固醇消炎藥（NSAID）家族的水楊酸衍生物，推定機轉與同類 NSAID 一致：抑制環氧化酶（COX-1/COX-2），降低前列腺素合成，達到消炎、鎮痛效果。

僵直性脊椎炎是一種發炎性脊椎關節病，NSAID 為其**標準治療藥物類別**之一。也就是說，TxGNN 找到的這個關聯，本質上是重新確認 NSAID 藥理學上早已成立的既有臨床應用，**而非發掘全新的再利用機會**——這點在 Evidence Pack 的 `repurposing_rationale` 中也已明確標註（「屬藥物既有臨床應用範疇（非新穎再利用）」）。

值得注意的是，支持文獻中僅 3 篇（PMID 3524970、4062389、3546687）是 diflunisal 本品在 AS 病人上的直接研究（均出自 1985–1986 年同一研究團隊，樣本數約 33–38 人），其餘 4 篇文獻（diclofenac、naproxen、pirprofen review）談的是**其他 NSAID 藥物**在 AS 的療效，屬於藥物類別層級的佐證，並非 diflunisal 專屬證據，解讀時應予以區分。

## 臨床試驗證據

目前無相關臨床試驗登記（`clinical_trials` 為空陣列）。

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 關鍵發現 |
|------|-----|------|------|---------|
| [3524970](https://pubmed.ncbi.nlm.nih.gov/3524970/) | 1986 | RCT | Clinical Rheumatology | 38 名男性 AS 患者，12 週雙盲隨機試驗比較 diflunisal（500mg bid）與 phenylbutazone（200mg bid），兩者皆能改善 AS 症狀嚴重度，diflunisal 初期鎮痛起效較快、較明顯，延續 36 週開放期效果維持 |
| [4062389](https://pubmed.ncbi.nlm.nih.gov/4062389/) | 1985 | Cohort | Annals of the Rheumatic Diseases | 同批 38 名 AS 患者（diflunisal 或 phenylbutazone 治療）48 週追蹤，血清 IgA 濃度與胸廓擴張度、腰椎前彎指數相關，X 光變化較嚴重者 IgA 較高 |
| [3546687](https://pubmed.ncbi.nlm.nih.gov/3546687/) | 1986 | Cohort | The Journal of Rheumatology | 33 名 AS 患者雙盲隨機接受 diflunisal 或 phenylbutazone 治療 12 週（延伸至 48 週），評估肺功能（VC）與疾病活動度、NSAID 治療的關係 |
| [2670397](https://pubmed.ncbi.nlm.nih.gov/2670397/) | 1989 | Review | Clinical Pharmacy | Diclofenac（非 diflunisal）藥理學回顧，屬同類 NSAID 於風濕疾病的類別層級佐證 |
| [6772422](https://pubmed.ncbi.nlm.nih.gov/6772422/) | 1980 | Review | Drugs | Diclofenac 於風濕疾病（含 AS）之藥理與治療應用回顧，非 diflunisal 專屬證據 |
| [387372](https://pubmed.ncbi.nlm.nih.gov/387372/) | 1979 | Review | Drugs | Naproxen 於風濕疾病治療回顧，非 diflunisal 專屬證據 |
| [3539573](https://pubmed.ncbi.nlm.nih.gov/3539573/) | 1986 | Review | Drugs | Pirprofen 藥效學/藥動學回顧，提及可作為 AS 等風濕疾病治療替代選項，非 diflunisal 專屬證據 |

## 台灣上市資訊

Diflunisal 目前**未於台灣上市**（`market_status: 未上市`），無任何許可證紀錄（`total_licenses: 0`），因此無法提供品名、劑型或核准適應症內容。

## 安全性考量

Evidence Pack 中的關鍵警語、禁忌症皆標示為資料缺口，藥物交互作用查詢無結果（`query_status: not_found`）。

請參考仿單說明書取得安全性資訊。

> ⚠️ 特別注意：Meta 資料中 `DG001`（TFDA 仿單警語/禁忌）被標記為 **Blocking** 等級缺口，明確指出「無法進入 S1 安全性初評」，此為本案無法直接推進的主要原因。

## 結論與後續建議

**決策：Hold**

**理由：**
- 雖然僵直性脊椎炎有 1 件 1986 年的小規模（n=38）RCT 支持 diflunisal 療效（L2 證據等級），但此關聯本質上是 NSAID 類別已知用途的重申，而非真正的新穎再利用發現，附加價值有限。
- 更關鍵的是，TFDA 仿單警語/禁忌資料為 **Blocking** 等級缺口，依規則無法進入 S1 安全性初評，在缺口補齊前不應推進任何決策。
- 藥物於台灣未上市（0 張許可證），亦無 DDI 查詢結果，整體安全性資訊嚴重不足。

**要推進，需要補齊：**
- TFDA 仿單 PDF 下載與解析（DG001，Blocking，來源：TFDA 官網）
- DrugBank 作用機轉（MOA）資料查詢（DG002，High，來源：DrugBank API）
- 若後續評估僵直性脊椎炎方向，需確認其是否已被涵蓋於 diflunisal 其他國家既有適應症內，以釐清此案是否真正構成「老藥新用」而非既有用途延伸
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

