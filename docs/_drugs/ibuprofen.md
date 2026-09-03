---
layout: default
title: Ibuprofen
parent: 僅模型預測 (L5)
nav_order: 171
evidence_level: L5
indication_count: 7
---

# Ibuprofen
{: .fs-9 }

證據等級: **L5** | 預測適應症: **7** 個
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

# Ibuprofen: From NSAID Therapy to Acromesomelic Dysplasia, Hunter-Thompson Type

## One-Sentence Summary

> Ibuprofen is a widely used nonsteroidal anti-inflammatory drug (NSAID), though no Taiwan-specific approved indication text is available in this evidence pack.
> The TxGNN model's top prediction is **Acromesomelic Dysplasia, Hunter-Thompson Type**, a rare congenital skeletal disorder,
> but this candidate currently has **0 clinical trials** and **0 publications** supporting it, and the model's own rationale flags it as a likely embedding-clustering false positive.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available — no `original_indications` or Taiwan license data in this evidence pack |
| Predicted New Indication | Acromesomelic Dysplasia, Hunter-Thompson Type |
| TxGNN Prediction Score | 99.74% |
| Evidence Level | L5 |
| Taiwan Market Status | Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available (flagged as a High-severity data gap, DG002). Ibuprofen is generally known as a propionic-acid-class NSAID that inhibits COX-1/COX-2 and prostaglandin synthesis, but no drug-specific MOA record was returned for this candidate.

Importantly, this prediction should **not** be treated as mechanistically well-supported. The model's own rationale for the top-ranked disease states that Acromesomelic Dysplasia, Hunter-Thompson Type is caused by *GDF5* gene mutations — a congenital structural skeletal disorder with **no known pathogenic overlap** with the COX/prostaglandin-inhibition pathway that underlies ibuprofen's pharmacology. The evidence pack explicitly notes this high score is suspected to be a **graph-embedding clustering false positive** rather than a biologically grounded signal.

This pattern repeats across all seven ranked candidates in this pack: brachyolmia-amelogenesis imperfecta syndrome, myosclerosis, brachyolmia, brachydactyly-syndactyly syndrome, pseudoachondroplasia, and colobomatous microphthalmia-rhizomelic dysplasia syndrome are all rare congenital or developmental skeletal/connective-tissue disorders. Only pseudoachondroplasia's rationale notes a plausible (but purely symptomatic, non-disease-modifying) link — NSAID use for joint pain — while every other candidate is explicitly described as lacking a known inflammatory or mechanistic pathway connection to ibuprofen. None of the seven candidates has any supporting clinical trial or literature evidence.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Taiwan Market Information

Ibuprofen currently has **no marketing authorization in Taiwan** (0 licenses on record; market status: Not marketed). No product name, dosage form, or approved indication text is available for this evidence pack.

---

## Safety Considerations

Please refer to the package insert for safety information.

*(Note: TFDA label warnings/contraindications are recorded as a Blocking data gap (DG001) — this is required before any S1 safety pre-assessment can proceed.)*

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
All seven TxGNN-predicted indications for ibuprofen are rare congenital skeletal/connective-tissue disorders with L5 evidence (score-only, no clinical trials or literature), and the top-ranked candidate's own mechanistic rationale flags it as a likely embedding-clustering false positive with no known pathogenic overlap with NSAID pharmacology. Combined with a Blocking gap on TFDA label data and a High-severity gap on MOA, this candidate cannot advance past S0.

**To proceed, the following is needed:**
- TFDA label warnings/contraindications (DG001, Blocking) — required before any safety pre-assessment
- DrugBank MOA data (DG002, High) to properly assess mechanistic plausibility
- Independent biological/genetic rationale review to confirm or rule out the suspected embedding-clustering artifact before treating this prediction as a viable candidate
- If pursuing further, re-run TxGNN ranking against non-rare-disease indication sets to check whether this candidate list reflects a systematic clustering issue specific to ibuprofen's embedding
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

