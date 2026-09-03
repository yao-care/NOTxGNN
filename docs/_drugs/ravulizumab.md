---
layout: default
title: Ravulizumab
parent: 僅模型預測 (L5)
nav_order: 298
evidence_level: L5
indication_count: 10
---

# Ravulizumab
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

# Ravulizumab: From Complement-Mediated Disease to Congenital Neutropenia (G6PC3 Deficiency)

## One-Sentence Summary

> Ravulizumab is a long-acting terminal complement (C5) inhibitor; its original approved indication is not available in the current dataset.
> The TxGNN model predicts it may be effective for **Autosomal Recessive Severe Congenital Neutropenia due to G6PC3 Deficiency**,
> but this prediction is currently supported by **0 clinical trials** and **0 publications** — evidence rests entirely on the model's embedding similarity, and the evidence pack itself flags the mechanistic rationale as likely spurious.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available in current dataset (no approved indication text in Norway regulatory records) |
| Predicted New Indication | Autosomal Recessive Severe Congenital Neutropenia due to G6PC3 Deficiency |
| TxGNN Prediction Score | 99.96% |
| Evidence Level | L5 |
| Norway Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the structured MOA field. However, the evidence pack's own repurposing rationale describes ravulizumab as a long-acting C5 complement inhibitor (a derivative of eculizumab), meaning its established pharmacology blocks the terminal complement cascade (C5 cleavage → C5a/C5b-9 formation).

The predicted indication — congenital neutropenia due to G6PC3 deficiency — is driven by endoplasmic reticulum stress and apoptosis in neutrophil precursors, a mechanism rooted in glycogen/glucose metabolism rather than complement activation. According to the evidence pack's own mechanistic assessment, **there is no known direct biological link between the C5 complement pathway and G6PC3-deficient neutropenia**. The high TxGNN score most likely reflects embedding-space similarity across a cluster of neutrophil-related diseases in the knowledge graph, rather than a genuine, validated mechanistic connection.

This caveat is consistent across the other top-ranked predictions in this evidence pack (cyclic hematopoiesis, CXCR2-deficient neutropenia, X-linked SCN) — all are neutrophil/hematopoietic disorders with distinct, non-complement-driven etiologies, reinforcing that the model may be clustering on phenotypic similarity (neutropenia) rather than shared drug-target biology.

---

## Clinical Trial Evidence

Currently no related clinical trials registered

---

## Literature Evidence

Currently no related literature available

---

## Norway Market Information

Ravulizumab is not currently marketed in Norway, and no authorization records are available in the dataset.

---

## Safety Considerations

Please refer to the package insert for safety information.

*Note: TFDA label warnings/contraindications (DG001) are flagged as a **Blocking** data gap in the evidence pack — this drug cannot proceed to a safety pre-assessment (S1) until this data is obtained.*

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
This prediction is supported only by an L5 model score (rank 731/~, no clinical trials, no literature), and the evidence pack's own mechanistic analysis explicitly questions the biological plausibility of the C5-pathway/G6PC3-neutropenia link, attributing the high score to disease-embedding similarity rather than genuine target relevance. Combined with a Blocking data gap on TFDA safety labeling, this candidate does not meet the threshold to advance past S0.

**To proceed, the following is needed:**
- Structured MOA data from DrugBank/label sources (currently a High-severity data gap, DG001/DG002)
- TFDA/regulatory label (warnings, contraindications) to enable S1 safety pre-assessment (Blocking gap)
- Independent literature or preclinical evidence directly linking complement C5 activity to G6PC3-deficient neutrophil pathology
- Confirmation of the drug's actual original approved indication(s), currently missing from regulatory records
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

