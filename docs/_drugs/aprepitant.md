---
layout: default
title: Aprepitant
parent: 僅模型預測 (L5)
nav_order: 33
evidence_level: L5
indication_count: 10
---

# Aprepitant
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

# Aprepitant: From Chemotherapy-Induced Nausea and Vomiting to Nephrogenic Syndrome of Inappropriate Antidiuresis

## One-Sentence Summary

> Aprepitant is a neurokinin-1 (NK1)/substance P receptor antagonist, publicly known for use in preventing chemotherapy-induced and postoperative nausea and vomiting.
> The TxGNN model predicts it may be effective for **Nephrogenic Syndrome of Inappropriate Antidiuresis**,
> but currently **no clinical trials** and **no literature** support this specific direction — the model's own rationale states there is no known mechanistic link between NK1 antagonism and AVP receptor signaling.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not captured in evidence pack (aprepitant is a known NK1/substance P receptor antagonist, commonly indicated for CINV/PONV) |
| Predicted New Indication | Nephrogenic Syndrome of Inappropriate Antidiuresis |
| TxGNN Prediction Score | 99.97% |
| Evidence Level | L5 |
| Taiwan Market Status | 未上市 (Not marketed) |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the structured evidence pack. Based on the model's own rationale, aprepitant is known to be an NK1 (neurokinin-1/substance P receptor) antagonist. Its established pharmacology relates to substance P–mediated emetic pathways, not to arginine vasopressin (AVP) receptor signaling, which underlies nephrogenic syndrome of inappropriate antidiuresis.

The repurposing rationale explicitly states that this indication has no known intersection with the AVP signaling pathway, and that the high TxGNN score is purely data-driven rather than mechanism-supported. There is no plausible pharmacological bridge between the original NK1-antagonist activity and the pathophysiology of this predicted indication based on currently available information.

Given the absence of any mechanistic hypothesis grounded in existing pharmacology, this prediction should be treated as an exploratory signal only, not as a mechanistically motivated repurposing candidate.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Norway Market Information

No Taiwan marketing authorizations were found for this product (market status: 未上市 / not marketed, 0 licenses on record).

## Safety Considerations

Please refer to the package insert for safety information.

*(Note: TFDA label warnings/contraindications data is flagged as a **Blocking** data gap (DG001) — this evaluation cannot proceed to a full S1 safety assessment until this is resolved.)*

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction sits at evidence level L5 — a model score with no supporting clinical trials or literature, and the model's own rationale confirms no known mechanistic link to the original drug's pharmacology. Combined with a blocking gap in TFDA safety labeling data, there is currently no basis to advance this candidate beyond hypothesis generation.

**To proceed, the following is needed:**
- TFDA label warnings/contraindications (DG001, Blocking) — required before any S1 safety evaluation
- Confirmed mechanism of action data from DrugBank (DG002)
- Preclinical or mechanistic studies establishing a biological link between NK1 antagonism and AVP-mediated antidiuresis
- Any clinical case reports, observational data, or trials specifically evaluating aprepitant in SIADH/nephrogenic antidiuresis-related conditions
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

