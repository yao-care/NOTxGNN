---
layout: default
title: Entacapone
parent: 僅模型預測 (L5)
nav_order: 132
evidence_level: L5
indication_count: 10
---

# Entacapone
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

# Entacapone: From Parkinson's Disease to PLA2G6-Associated Neurodegeneration

## One-Sentence Summary

Entacapone is a COMT inhibitor used as an adjunct to levodopa/carbidopa therapy in Parkinson's disease, extending dopamine precursor availability.
The TxGNN model predicts it may be effective for **PLA2G6-Associated Neurodegeneration**,
but currently **no clinical trials** and **no publications** support this specific prediction.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Parkinson's disease (adjunct to levodopa therapy) — inferred from repurposing rationale text; no formal indication text or MOA data provided in this evidence pack |
| Predicted New Indication | PLA2G6-Associated Neurodegeneration |
| TxGNN Prediction Score | 99.76% |
| Evidence Level | L5 |
| Norway Market Status | ✗ Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available (Data Gap DG002). Based on information present elsewhere in this evidence pack, entacapone is known as a COMT inhibitor co-administered with levodopa in Parkinson's disease, prolonging levodopa's central availability. Its efficacy in Parkinson's disease is well established.

For the top-ranked prediction, PLA2G6-Associated Neurodegeneration, the evidence pack provides **no mechanistic rationale text, no clinical trials, and no literature**. This is unusual compared to lower-ranked predictions in the same batch (e.g., rank 4 "juvenile parkinsonism of Hunt" and rank 7 "Lewy body dementia"), which do include reasoned mechanistic links to dopaminergic pathways. Without any supporting rationale or evidence, this top-ranked prediction should be treated as an unvalidated model output rather than a scientifically substantiated hypothesis — despite carrying the highest TxGNN score in this batch.

Notably, two other candidates in this same prediction set — **Lewy body dementia** (rank 7) and **progressive supranuclear palsy-corticobasal syndrome** (rank 10) — have documented literature and/or clinical trial signals tied to dopaminergic mechanisms shared with Parkinson's disease. These may warrant prioritization over PLA2G6-Associated Neurodegeneration for further evaluation.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Norway Market Information

Entacapone is not currently marketed in Norway (0 authorizations on record); no license data is available in this evidence pack.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked prediction (PLA2G6-Associated Neurodegeneration) has no supporting clinical trials, literature, or mechanistic rationale — it is a pure model output (L5) and should not proceed without further validation.

**To proceed, the following is needed:**
- TFDA/regulatory label data (warnings, contraindications) — currently a Blocking data gap (DG001)
- Confirmed mechanism of action from DrugBank — currently a High-severity data gap (DG002)
- Preclinical or mechanistic studies linking entacapone's COMT-inhibitory activity to PLA2G6-associated neurodegeneration pathology
- Consider evaluating the better-evidenced alternatives in this batch (Lewy body dementia, PSP-corticobasal syndrome) as higher-priority repurposing candidates for entacapone
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

