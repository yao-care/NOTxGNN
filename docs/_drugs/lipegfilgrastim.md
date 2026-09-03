---
layout: default
title: Lipegfilgrastim
parent: 僅模型預測 (L5)
nav_order: 211
evidence_level: L5
indication_count: 5
---

# Lipegfilgrastim
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

# Lipegfilgrastim: From Chemotherapy-Induced Neutropenia to Primary Release Disorder of Platelets

## One-Sentence Summary

Lipegfilgrastim is a pegylated recombinant human G-CSF analog known clinically for treating chemotherapy-induced neutropenia.
The TxGNN model predicts it may be effective for **Primary Release Disorder of Platelets**,
but this prediction is currently supported by **0 clinical trials** and **0 publications** — it is a model-only hypothesis with no empirical evidence.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Chemotherapy-induced neutropenia (based on known drug class information; not confirmed in the source evidence pack) |
| Predicted New Indication | Primary Release Disorder of Platelets |
| TxGNN Prediction Score | 99.93% |
| Evidence Level | L5 |
| Norway Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available (flagged as a High-severity data gap). Based on known information, Lipegfilgrastim is a pegylated recombinant human G-CSF analog that stimulates proliferation and differentiation of granulocyte (neutrophil) precursor cells in bone marrow, and its efficacy in chemotherapy-induced neutropenia is well established.

However, the predicted new indication — primary release disorder of platelets — involves a pathology of defective platelet granule content release, a mechanism with no known overlap with neutrophil-stimulating G-CSF activity. The evidence pack's own mechanistic assessment explicitly states there is no verifiable biological pathway connecting the two, and this ranking (score 0.9993, graph rank 1044) reflects TxGNN knowledge-graph association scoring alone, not a validated pharmacological hypothesis.

The remaining four predicted indications in this evidence pack (severe nonproliferative diabetic retinopathy, pseudo-von Willebrand disease, Glanzmann thrombasthenia, diabetic retinopathy) show similarly weak or speculative mechanistic links — ranging from an unproven endothelial-progenitor-cell mobilization hypothesis to structurally/genetically defined platelet disorders with no cytokine-modulated pathway. None currently rise above L5 (model prediction only).

## Clinical Trial Evidence

Currently no related clinical trials registered

## Literature Evidence

Currently no related literature available

## Norway Market Information

Lipegfilgrastim is not currently marketed in Norway (0 authorizations on record). No product license data is available.

## Safety Considerations

Please refer to the package insert for safety information.

*Note: A Blocking-severity data gap (DG001) exists for TFDA warning/contraindication data, which prevents this candidate from entering the S1 safety pre-assessment stage.*

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
All five predicted indications remain at evidence stage S0 (model prediction only) with no supporting clinical trials or literature, and a Blocking-severity safety data gap prevents progression to formal safety pre-assessment. The mechanistic rationale for the top prediction is explicitly assessed as lacking biological plausibility.

**To proceed, the following is needed:**
- TFDA/regulatory warning and contraindication data (Blocking gap, DG001) — required before any S1 safety review
- Confirmed original mechanism of action (MOA) data via DrugBank API (High-priority gap, DG002)
- Independent literature or preclinical evidence establishing a biological pathway between G-CSF activity and platelet release/function disorders
- Registration of dedicated clinical trials, or identification of existing off-label case data, for any of the five candidate indications
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

