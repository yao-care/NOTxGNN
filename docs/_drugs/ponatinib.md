---
layout: default
title: Ponatinib
parent: 僅模型預測 (L5)
nav_order: 284
evidence_level: L5
indication_count: 2
---

# Ponatinib
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

# Ponatinib: From Unspecified Original Indication to Gingival Fibromatosis

## One-Sentence Summary

> Ponatinib's original approved indication and mechanism of action are not available in the current data set (both flagged as data gaps).
> The TxGNN model predicts it may be effective for **Gingival Fibromatosis**,
> but this prediction is currently supported by **0 clinical trials** and **0 publications** — evidence level L5 (model prediction only).

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available (no license or indication data on file) |
| Predicted New Indication | Fibromatosis, gingival |
| TxGNN Prediction Score | 99.04% |
| Evidence Level | L5 |
| Norway Market Status | Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data for ponatinib is not on file (flagged as a High-severity data gap). However, the evidence pack's own repurposing rationale identifies ponatinib as a multi-kinase inhibitor targeting BCR-ABL, FGFR, PDGFR, VEGFR, KIT, and SRC — consistent with its known class as a tyrosine kinase inhibitor.

Gingival fibromatosis is mechanistically linked to SOS1/PDGFR signaling and fibroblast overproliferation. Since ponatinib inhibits PDGFR, there is a theoretical basis for suppressing fibroblast proliferation. However, this link is derived purely from the TxGNN score — there is no supporting mechanistic literature, preclinical data, or clinical evidence, and because the original indication data is entirely missing, no credible pharmacological analogy can be drawn between the original and predicted indications.

Given the very weak evidentiary basis (score-only prediction, TxGNN rank 9202 — far outside typical high-confidence ranges), this prediction should be treated as exploratory only.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Norway Market Information

Ponatinib is currently **not marketed** and holds **0 authorizations**, so no license/product table is available.

---

## Cytotoxicity

Ponatinib's repurposing rationale identifies it as a multi-kinase inhibitor (BCR-ABL/FGFR/PDGFR/VEGFR/KIT/SRC), consistent with a targeted antineoplastic therapy class, so this section is included for completeness.

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (multi-kinase inhibitor: BCR-ABL/FGFR/PDGFR/VEGFR/KIT/SRC) |
| Myelosuppression Risk | Please refer to the package insert warnings and precautions |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | Please refer to the package insert warnings and precautions |
| Handling Protection | Please refer to the package insert warnings and precautions |

---

## Safety Considerations

Please refer to the package insert for safety information. (Regulatory label warnings, contraindications, and DDI data are currently a **blocking** data gap — see DG001.)

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top prediction (gingival fibromatosis) is supported only by the TxGNN score, with no clinical trials or literature (L5) and a low prediction rank (9202), and both original-indication and MOA data are missing — insufficient basis to advance. A secondary candidate in the same evidence pack, **liposarcoma** (score 99.00%, rank 9484), has one preclinical kinase-screening publication (PMID [29132397](https://pubmed.ncbi.nlm.nih.gov/29132397/), L4) suggesting a theoretical kinase-pathway overlap, but it does not test ponatinib directly and is also rated Hold.

**To proceed, the following is needed:**
- TFDA/label warnings and contraindications for ponatinib (DG001, blocking)
- Confirmed mechanism of action data from DrugBank (DG002)
- Original indication and regulatory history for ponatinib
- Mechanistic or preclinical studies directly testing ponatinib in gingival fibromatosis or liposarcoma
- If pursuing the liposarcoma signal, targeted validation of ponatinib (not general kinase inhibitors) against liposarcoma cell lines
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

