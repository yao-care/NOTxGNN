---
layout: default
title: Spironolactone
parent: 僅模型預測 (L5)
nav_order: 332
evidence_level: L5
indication_count: 2
---

# Spironolactone
{: .fs-9 }

證據等級: **L5** | 預測適應症: **2** 個
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

# Spironolactone: From an Undocumented Original Indication to Hypotrichosis Simplex of the Scalp

## One-Sentence Summary

> The original approved indication for spironolactone is not documented in this evidence pack (data gap, pending DrugBank/label lookup).
> The TxGNN model predicts a possible link to **Hypotrichosis Simplex of the Scalp**,
> but this prediction is currently supported by **0 clinical trials** and **0 publications** — model score alone.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not documented in evidence pack (data gap — pending DrugBank query) |
| Predicted New Indication | Hypotrichosis Simplex of the Scalp |
| TxGNN Prediction Score | 99.26% |
| Evidence Level | L5 (model prediction only, no clinical trials or literature) |
| Norway Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available for spironolactone in this evidence pack (`original_moa` = data gap). Based on the rationale text supplied alongside the prediction, spironolactone is known to act as a **mineralocorticoid receptor antagonist with anti-androgen activity**, and it does have real-world off-label use in androgenetic alopecia — so a general link between spironolactone and hair-related conditions is not implausible on its face.

However, the evidence pack's own mechanistic assessment for this specific prediction is skeptical: **hypotrichosis simplex of the scalp** is an autosomal dominant, structural/developmental hair follicle disorder that is **not androgen-dependent**. There is no established biological link between spironolactone's known MOA and this disease's pathophysiology — the connection is assessed as a TxGNN extrapolation based on phenotypic similarity (hair-related outcomes) rather than genuine mechanistic overlap.

A second, lower-ranked prediction (**congenital hypotrichosis milia**, score 99.04%) shows the same pattern: a rare ectodermal/follicular developmental disorder with no known relationship to mineralocorticoid or anti-androgen pathways. Both predictions in this evidence pack are flagged as lacking mechanistic support beyond the model's statistical association.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Norway Market Information

Spironolactone is currently **not marketed** in Norway under this evidence pack (0 authorizations, no license records available).

---

## Safety Considerations

Please refer to the package insert for safety information.

*(Note: key warnings, contraindications, and DDI data are flagged as blocking/high-severity data gaps — see Conclusion below.)*

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Both candidate indications are supported only by TxGNN model scores (L5, no clinical or literature evidence), and the evidence pack's own mechanistic rationale explicitly notes a lack of biological plausibility for the top prediction. In addition, a **Blocking** data gap (missing TFDA/label warnings and contraindications) prevents the drug from even entering the S1 safety pre-assessment stage.

**To proceed, the following is needed:**
- TFDA/product label warnings and contraindications (DG001 — Blocking, required for S1 safety screening)
- Mechanism of action data via DrugBank API (DG002 — High severity)
- Documentation of spironolactone's original approved indication(s)
- Independent clinical or preclinical evidence linking spironolactone to hypotrichosis simplex of the scalp, beyond model-derived similarity
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

