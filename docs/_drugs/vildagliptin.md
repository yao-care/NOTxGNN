---
layout: default
title: Vildagliptin
parent: 僅模型預測 (L5)
nav_order: 385
evidence_level: L5
indication_count: 10
---

# Vildagliptin
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

# Vildagliptin: From Type 2 Diabetes Mellitus to Classic Stiff Person Syndrome

## One-Sentence Summary

Vildagliptin is a DPP-4 (dipeptidyl peptidase-IV) inhibitor originally developed for glycemic control in type 2 diabetes mellitus.
The TxGNN model predicts it may be effective for **Classic Stiff Person Syndrome**,
but this prediction is currently supported by **0 clinical trials** and **0 publications** — it is a model-only signal.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Type 2 Diabetes Mellitus (drug class/literature-derived; no Norway license record exists for this drug) |
| Predicted New Indication | Classic Stiff Person Syndrome |
| TxGNN Prediction Score | 99.88% |
| Evidence Level | L5 |
| Norway Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available (DG002, High severity). Based on literature retrieved for this evidence pack, vildagliptin is a selective DPP-4 inhibitor that blocks degradation of the incretin hormones GLP-1 and GIP, thereby enhancing glucose-dependent insulin secretion and suppressing inappropriate glucagon release — its efficacy in type 2 diabetes is well documented.

For the top-ranked prediction, **classic stiff person syndrome**, there is **no known mechanistic link** to the DPP-4/incretin pathway. Stiff person syndrome is an anti-GAD65 autoimmune neurological disorder affecting GABAergic inhibitory transmission, a biological system unrelated to incretin signaling. The evidence pack itself notes this explicitly: the prediction rests solely on the TxGNN embedding score, with no supporting trials or publications identified.

By contrast, other candidates further down the model's ranked list have stronger biological plausibility — notably **type 1 diabetes mellitus** (rank 10), where DPP-4 inhibition could theoretically prolong endogenous GLP-1 activity to support residual β-cell function, and this is backed by an actual randomized controlled trial (see Conclusion). This top prediction should therefore be read as a low-confidence, mechanism-agnostic model output rather than a biologically grounded hypothesis.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Norway Market Information

Vildagliptin currently holds **no marketing authorization** in Norway (market status: Not Marketed; 0 licenses on record). No product-level dosage form or approved-indication data is available for this market.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked predicted indication (classic stiff person syndrome) has no mechanistic rationale, no clinical trial evidence, and no supporting literature — it is a pure L5 model prediction. Combined with the lack of Norway market authorization and missing safety/MOA data, there is no basis to advance this candidate.

**To proceed, the following is needed:**
- Official product label / regulatory safety data (warnings, contraindications) — currently blocking (DG001)
- Verified mechanism of action data from DrugBank or equivalent source (DG002)
- Independent mechanistic or preclinical rationale connecting DPP-4 inhibition to GAD65-mediated autoimmune neurological disease before any further evaluation
- **Alternative candidate worth tracking instead:** type 1 diabetes mellitus (rank 10) already has an L2/S2 "Research Question" status, including a completed double-blind RCT (rapamycin + vildagliptin, PMID 33124663) targeting β-cell function recovery — this is a substantially stronger repurposing signal than the top-ranked prediction and may warrant separate evaluation
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

