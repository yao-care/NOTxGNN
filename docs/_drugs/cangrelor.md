---
layout: default
title: Cangrelor
parent: 僅模型預測 (L5)
nav_order: 21
evidence_level: L5
indication_count: 0
---

# Cangrelor
{: .fs-9 }

證據等級: **L5** | 預測適應症: **0** 個
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

# Cangrelor: No Repurposing Predictions Available

## One-Sentence Summary

Cangrelor is an intravenous, direct-acting P2Y12 platelet receptor antagonist used in acute cardiovascular settings such as percutaneous coronary intervention (PCI).
The current evidence pack contains **no TxGNN repurposing predictions** for this drug, and critical data gaps in mechanism of action and safety information prevent a complete evaluation.
This report serves as a preliminary record pending further data collection.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Antiplatelet therapy during percutaneous coronary intervention (PCI) |
| Predicted New Indication | No prediction available |
| TxGNN Prediction Score | N/A |
| Evidence Level | L5 — model prediction only; no supporting predictions generated |
| Norway Market Status | Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why Assessment Is Limited

Cangrelor (brand names: Kengreal / Kengrexal) is a short-acting, reversible P2Y12 ADP receptor antagonist administered intravenously. Unlike oral antiplatelet agents such as clopidogrel or ticagrelor, cangrelor has an extremely short plasma half-life (~3–5 minutes), making it uniquely suited for procedural settings where rapid platelet inhibition onset and offset are required.

Detailed mechanism of action data from DrugBank was not retrieved in the current evidence pack (Data Gap DG002). Without this information, it is not possible to reason about mechanistic similarity to potential new indications.

More critically, the TxGNN model did not generate any repurposing predictions for cangrelor in this pipeline run. The `predicted_indications` array is empty, meaning the core analytical output of the repurposing workflow is absent. This may reflect insufficient graph connectivity in the underlying knowledge graph, or the drug may simply not have been scored against any new disease nodes in this run.

---

## Norway Market Information

Cangrelor is **not currently approved or marketed in Norway**. No product authorizations are on record in the regulatory database.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The evidence pack contains no TxGNN-generated repurposing predictions, and two blocking/high-severity data gaps (DG001: safety warnings; DG002: mechanism of action) prevent any meaningful clinical or mechanistic evaluation.

**To proceed, the following is needed:**
- Re-run TxGNN scoring pipeline to generate `predicted_indications` for cangrelor
- Retrieve mechanism of action (MOA) from DrugBank API (Data Gap DG002)
- Parse package insert PDF to extract key warnings and contraindications (Data Gap DG001 — currently marked as Blocking severity)
- Review EMA/Norwegian regulatory status for cangrelor (Kengrexal), as the drug is EU-approved and may qualify for a Norway market authorization review
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

