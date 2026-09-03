---
layout: default
title: Lonafarnib
parent: 僅模型預測 (L5)
nav_order: 213
evidence_level: L5
indication_count: 1
---

# Lonafarnib
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

# Lonafarnib: From Progeria/HDV Infection to Leprosy

## One-Sentence Summary

> Lonafarnib is a farnesyltransferase inhibitor with established clinical use in Hutchinson-Gilford Progeria Syndrome and hepatitis D virus (HDV) infection.
> The TxGNN model predicts it may be effective for **Leprosy**,
> but currently **no clinical trials** and **no publications** support this direction — the prediction rests on the model score alone.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in current dataset (known clinical uses per literature: Hutchinson-Gilford Progeria Syndrome, HDV infection) |
| Predicted New Indication | Leprosy |
| TxGNN Prediction Score | 99.14% |
| Evidence Level | L5 |
| Norway Market Status | Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in this Evidence Pack (`original_moa: [Data Gap]`). Based on external knowledge, lonafarnib is a farnesyltransferase inhibitor whose established clinical applications are Hutchinson-Gilford Progeria Syndrome (blocking farnesylation of defective lamin A/progerin) and chronic HDV infection (blocking prenylation of the large HDV antigen to prevent viral assembly).

No known or plausible mechanistic link connects farnesyltransferase inhibition to the pathophysiology of leprosy, which is driven by *Mycobacterium leprae* infection, mycobacterial cell wall biosynthesis, and host immune/granulomatous response. No literature was found describing an effect of prenylation inhibition on mycobacterial viability or anti-mycobacterial host immunity. The prediction should therefore be treated as a model-generated hypothesis without independent mechanistic or empirical support.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Norway Market Information

Lonafarnib currently holds no market authorization in Norway (0 licenses on record; market status: not marketed).

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is supported only by a TxGNN model score (L5) with no corroborating clinical trials, literature, or plausible mechanistic rationale linking farnesyltransferase inhibition to leprosy pathophysiology. The drug is also not currently marketed in Norway, and core safety data (warnings, contraindications, DDI) are unavailable.

**To proceed, the following is needed:**
- Confirmed mechanism of action (MOA) data from DrugBank or primary literature
- TFDA/regulatory label data (warnings, contraindications) to clear the S1 safety gate
- Preclinical or mechanistic studies evaluating farnesyltransferase inhibition in *M. leprae* infection or host anti-mycobacterial immunity
- At minimum, case-level or observational evidence before advancing beyond S0
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

