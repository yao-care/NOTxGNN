---
layout: default
title: Eculizumab
parent: 僅模型預測 (L5)
nav_order: 119
evidence_level: L5
indication_count: 10
---

# Eculizumab
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

# Eculizumab: From Original Indication Not Provided to Cyclic Hematopoiesis

## One-Sentence Summary

> The evidence pack for eculizumab does not include original indication or mechanism-of-action (MOA) data (flagged as a **blocking data gap**).
> The TxGNN model predicts eculizumab may be effective for **cyclic hematopoiesis**, but this prediction is supported by **0 clinical trials** and **0 publications**, and the accompanying mechanistic rationale explicitly states there is **no known biological link** between eculizumab's complement-inhibiting mechanism and this disease.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not provided in evidence pack (data gap) |
| Predicted New Indication | Cyclic Hematopoiesis |
| TxGNN Prediction Score | 99.97% |
| Evidence Level | L5 |
| Norway Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data for eculizumab is not available in this evidence pack (marked as a High-severity data gap). Based on the drug's known target class, eculizumab is an anti-C5 monoclonal antibody that blocks terminal complement activation (MAC/C5a formation).

The repurposing rationale provided alongside this prediction, however, is explicitly **negative**: cyclic hematopoiesis is caused by *ELANE* gene mutations affecting neutrophil elastase and granulocyte production regulation — a pathway unrelated to complement activation. The rationale states there is "no known intersection" between eculizumab's mechanism and this disease's pathophysiology, and characterizes the prediction as arising purely from TxGNN network-similarity patterns rather than any mechanistic hypothesis.

This is an important caveat: a high TxGNN score alone does not indicate biological plausibility. In this case, the model score (rank 597, score 0.9997) is not corroborated by mechanism, clinical trials, or literature, which is consistent with its classification as **L5 – model prediction only**.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

*Note: Among the other 9 lower-ranked candidate indications in this evidence pack, two (rank 4 – congenital neutropenia-myelofibrosis-nephromegaly syndrome; rank 10 – primary release disorder of platelets) returned literature hits, but these were reviewed and judged to be search noise — the retrieved papers discuss eculizumab's already-established use in PNH, aHUS, and myasthenic syndromes, not the predicted indications themselves. None constitute direct or indirect evidence for the top-ranked prediction (cyclic hematopoiesis).*

---

## Norway Market Information

Eculizumab is not currently marketed and holds no active authorizations on file (0 licenses recorded).

---

## Safety Considerations

Please refer to the package insert for safety information.

*Note: TFDA/label warnings, contraindications, and DDI data could not be retrieved and are flagged in the source evidence pack as a **Blocking** data gap — this specifically prevents the candidate from proceeding to the S1 preliminary safety evaluation stage.*

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked predicted indication (cyclic hematopoiesis) has no supporting clinical trials or literature, and the provided mechanistic rationale explicitly states there is no biological link between eculizumab's complement-inhibition mechanism and this disease — the TxGNN score reflects network similarity only. Combined with a blocking gap in TFDA safety/label data, this candidate cannot currently advance past S0.

**To proceed, the following is needed:**
- TFDA package insert (warnings, contraindications) — blocking gap, required to enter S1 safety evaluation
- Mechanism of action (MOA) data via DrugBank API — required for mechanistic plausibility assessment
- Original indication/regulatory history for eculizumab, currently absent from this evidence pack
- Independent mechanistic or preclinical evidence specifically linking complement (C5) inhibition to cyclic hematopoiesis, if this candidate is to be reconsidered
- Re-screening of the remaining 9 lower-ranked candidates in this pack, all of which also carry L5/Hold status with no direct supporting evidence
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

