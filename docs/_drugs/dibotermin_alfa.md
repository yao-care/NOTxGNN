---
layout: default
title: Dibotermin Alfa
parent: 僅模型預測 (L5)
nav_order: 108
evidence_level: L5
indication_count: 9
---

# Dibotermin Alfa
{: .fs-9 }

證據等級: **L5** | 預測適應症: **9** 個
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

# Dibotermin Alfa: From Bone Regeneration to Esotropia

## One-Sentence Summary

> Dibotermin alfa is a recombinant human BMP-2 used to promote bone induction and regeneration (e.g., spinal fusion, tibial fracture repair).
> The TxGNN model predicts it may be effective for **Esotropia**,
> but this prediction is currently supported by **0 clinical trials** and **0 publications**, and no plausible mechanistic pathway has been identified.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available from Norway regulatory data (drug not marketed); per evidence context, historically used for bone induction/regeneration (spinal fusion, tibial fracture repair) |
| Predicted New Indication | Esotropia |
| TxGNN Prediction Score | 99.97% |
| Evidence Level | L5 (model prediction only, no clinical or literature support) |
| Norway Market Status | Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available (`original_moa: [Data Gap]`). Based on the limited information available in the evidence pack, dibotermin alfa is a recombinant human bone morphogenetic protein-2 (BMP-2), and its known clinical use relates to bone induction and regeneration — for example, spinal fusion and tibial fracture repair.

Esotropia is a form of strabismus caused by extraocular muscle/neuromuscular imbalance, a condition mechanistically unrelated to osteoinduction. The evidence pack's own rationale explicitly states there is **no known mechanistic relationship** between BMP-2 signaling and esotropia, and no experimental or clinical evidence supports this link.

Given the absence of both mechanistic rationale and empirical evidence, this prediction should be treated as a pure model artifact rather than a biologically grounded repurposing hypothesis. The same caveat applies to several other TxGNN-ranked indications for this drug (e.g., breast cancer subtypes), where the underlying BMP-2 tumor biology literature — where it exists at all — points toward tumor-promoting rather than therapeutic effects.

---

## Clinical Trial Evidence

Currently no related clinical trials registered

---

## Literature Evidence

Currently no related literature available

*Note: A lower-ranked candidate (breast tumor luminal A/B, rank 5) returned 19 "matching" PMIDs, but all were confirmed to be database keyword mismatches (B-cell immunology, hepatitis B vaccines, HLA-B serotyping) unrelated to either the drug or the disease, and are excluded as noise.*

---

## Norway Market Information

Dibotermin alfa currently holds no market authorization in Norway (0 licenses on record); no product or approved indication text is available.

---

## Safety Considerations

Please refer to the package insert for safety information.

*(Note: TFDA/Norway label warnings and contraindications are flagged as a **Blocking** data gap — required before any safety-stage (S1) evaluation can proceed.)*

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN score is high, but there is zero clinical trial or literature support, no coherent mechanistic link between BMP-2 osteoinduction and esotropia (a neuromuscular condition), and the drug is not currently marketed in Norway. This combination places the candidate at the lowest evidence tier (L5) with no basis to advance.

**To proceed, the following is needed:**
- TFDA/Norway package insert warnings and contraindications (currently Blocking data gap, DG001)
- Confirmed mechanism of action data from DrugBank or primary literature (DG002)
- Any preclinical or case-level evidence specifically linking BMP-2 signaling to extraocular muscle/neuromuscular function
- Re-screening of the other TxGNN-ranked candidates (e.g., breast cancer subtypes) for genuine literature support, since automated matches were found to include false positives
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

