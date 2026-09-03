---
layout: default
title: Selinexor
parent: 僅模型預測 (L5)
nav_order: 321
evidence_level: L5
indication_count: 1
---

# Selinexor
{: .fs-9 }

證據等級: **L5** | 預測適應症: **1** 個
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

# Selinexor：資料缺口下的預測適應症 — Drug-Induced Osteoporosis

## 一句話摘要

> Selinexor（DrugBank ID: DB11942）目前**原始適應症與作用機轉（MOA）皆為資料缺口**，且未於台灣（Norway 註冊資料庫）取得任何藥證。
> TxGNN 模型預測其可能對 **Drug-Induced Osteoporosis（藥物誘發性骨質疏鬆症）** 有效，
> 但目前**沒有任何臨床試驗、沒有任何文獻**支持此關聯，純屬知識圖譜連結預測。

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | 無資料（`original_indications` 為空陣列，`original_moa` 標記為 [Data Gap]） |
| Predicted New Indication | Drug-induced osteoporosis |
| TxGNN Prediction Score | 99.22% |
| Evidence Level | L5（僅模型預測，無實際研究） |
| Norway (Taiwan) Market Status | 未上市 |
| Number of Authorizations | 0 |
| Recommended Decision | **Hold** |

---

## Why is This Prediction Reasonable?

目前並無法取得 Selinexor 的詳細作用機轉資料（`original_moa` = [Data Gap]），亦無原始適應症紀錄可供比對。由於缺乏原始適應症與 MOA 資訊，無法建立「原始適應症 → 新適應症」之間的藥理學連結敘事。

根據 evidence pack 中的 `repurposing_rationale.mechanistic_link` 記載：TxGNN 分數 0.992 屬於**純知識圖譜連結預測**，資料集本身並未提供支持此關聯的生物機轉描述。即便外部公開資訊可能已知 Selinexor 的藥理分類，本報告依規定僅採計 Evidence Pack 內已驗證、已引用的資料，不得逕自代入未經本資料集驗證之外部知識，因此此機轉關聯**不予採計**。

換言之，此預測目前僅具有統計連結強度上的參考價值，尚無機轉層面或臨床證據層面的支持。

---

## Clinical Trial Evidence

目前無相關臨床試驗註冊。

---

## Literature Evidence

目前無相關文獻資料。

---

## Norway (Taiwan) Market Information

Selinexor 目前於本地（Norway/Taiwan 註冊系統）**未上市**，無任何藥證紀錄（`total_licenses` = 0），故無藥證資訊可供列表。

---

## Safety Considerations

請參考藥品仿單以獲取安全性資訊。

（`key_warnings`、`contraindications` 均標記為資料缺口，`ddi.query_status` = not_found，無藥物交互作用紀錄可供列示。）

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale：**
- 本候選案目前無任何臨床試驗或文獻證據支持（Evidence Level = L5），僅為 TxGNN 模型純知識圖譜預測分數。
- `data_gaps` 中 DG001（TFDA 仿單警語/禁忌）標記為 **Blocking** 等級，依規定無法進入 S1 安全性初評；DG002（MOA）為 High 等級缺口，影響機轉關聯性分析。
- 藥物於本地未上市，無實際處方或安全性使用經驗可供參考。

**To proceed, the following is needed：**
- 補齊 TFDA（或對應主管機關）仿單之警語與禁忌資訊，解除 DG001 阻斷性缺口
- 透過 DrugBank API 或其他來源補齊作用機轉（MOA）資料，解除 DG002
- 補充原始適應症紀錄，建立與 Drug-induced osteoporosis 之機轉/臨床合理性論述
- 檢索是否有任何臨床試驗（含 ICTRP）或同儕審查文獻可支持此適應症關聯
- 確認藥物交互作用（DDI）資料，以利後續安全性初評（S1）
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

