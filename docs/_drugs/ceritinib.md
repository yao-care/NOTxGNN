---
layout: default
title: Ceritinib
parent: 僅模型預測 (L5)
nav_order: 81
evidence_level: L5
indication_count: 10
---

# Ceritinib
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

# Ceritinib: From ALK-Positive NSCLC to Gingival Fibromatosis

## One-Sentence Summary

> Ceritinib is a second-generation ALK/ROS1 tyrosine kinase inhibitor originally developed for ALK-positive non-small cell lung cancer (NSCLC).
> The TxGNN model predicts it may be effective for **Gingival Fibromatosis**,
> but this candidate currently has **0 clinical trials** and **0 publications** supporting it — it is an unverified model hypothesis, and the model's own rationale flags the mechanistic link as weak.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | ALK-positive non-small cell lung cancer (NSCLC) — inferred from literature context; not recorded as structured data in this evidence pack |
| Predicted New Indication | Gingival Fibromatosis |
| TxGNN Prediction Score | 99.86% |
| Evidence Level | L5 (model prediction only, no supporting studies) |
| Norway Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | **Hold** |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data is not available for ceritinib in this evidence pack (flagged as a High-severity data gap, DG002). Based on the model's own generated rationale, ceritinib is known to be an ALK/ROS1 tyrosine kinase inhibitor whose efficacy in ALK-positive NSCLC is well established.

Gingival fibromatosis, however, is a benign fibrous overgrowth condition driven by SOS1/REST mutations or cyclosporine-associated fibroblast proliferation. It has no established relationship to ALK signaling. The model's own rationale explicitly states that the high score likely reflects semantic proximity in embedding space (shared "tumor/proliferation" language) rather than a genuine shared biological mechanism. No clinical trial or literature evidence exists for this specific pairing, so this prediction should be treated as an unverified hypothesis rather than an actionable repurposing signal.

**A note on the broader candidate set:** among the 10 TxGNN-predicted indications provided for ceritinib, one (rank 5, "lung benign neoplasm") carries unusually strong evidence — 1 completed Phase 3 RCT (ASCEND-4) and 20 publications. On inspection, however, all of that evidence concerns ALK-rearranged **malignant** NSCLC, which is ceritinib's *already-approved* indication, not a benign neoplasm. This indicates a disease-label mapping error in the underlying knowledge graph rather than a genuine new-indication signal, and should be reported back to the pipeline/data team as a data-quality issue rather than advanced as a repurposing candidate.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Norway Market Information

Ceritinib currently holds no marketing authorization in Norway (`market_status`: Not Marketed, 0 licenses on file). No product/dosage-form data is available for this evidence pack.

---

## Cytotoxicity

Ceritinib is an antineoplastic agent (ALK/ROS1 tyrosine kinase inhibitor used in oncology). DrugBank-level toxicity data was not provided in this evidence pack; the entries below are derived from literature associated with ceritinib elsewhere in this pack, cited for transparency.

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (small-molecule ALK/ROS1 tyrosine kinase inhibitor) |
| Myelosuppression Risk | Low — safety literature on ALK-TKIs (PMID [37597303](https://pubmed.ncbi.nlm.nih.gov/37597303/), [34864500](https://pubmed.ncbi.nlm.nih.gov/34864500/)) emphasizes non-hematologic toxicities (GI, hepatic, cardiac) rather than myelosuppression |
| Emetogenicity Classification | Moderate to High — GI toxicity (nausea, vomiting, diarrhea) is a well-documented, dose-related toxicity of ceritinib (PMID [35344649](https://pubmed.ncbi.nlm.nih.gov/35344649/), ASCEND-8) |
| Monitoring Items | Liver function tests; ECG/QTc interval (PMID [29413968](https://pubmed.ncbi.nlm.nih.gov/29413968/), [26008987](https://pubmed.ncbi.nlm.nih.gov/26008987/)); CBC; GI symptoms; thromboembolism risk (PMID [39349372](https://pubmed.ncbi.nlm.nih.gov/39349372/)) |
| Handling Protection | Oral small-molecule antineoplastic — handle per institutional hazardous/antineoplastic drug handling protocols; no DrugBank-specific handling data available in this evidence pack |

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
All 10 TxGNN-predicted indications for ceritinib in this evidence pack carry a "Hold" recommendation. The top-ranked candidate (gingival fibromatosis) has zero supporting clinical or literature evidence (L5) and an acknowledged implausible mechanistic link. The candidate with the strongest evidence in the set (lung benign neoplasm, L1) is actually a disease-label mismatch pointing back to ceritinib's existing approved indication (ALK+ NSCLC), not a genuine new indication.

**To proceed, the following is needed:**
- TFDA/regulatory-grade package insert warnings and contraindications (currently a Blocking data gap, DG001)
- A confirmed mechanism-of-action record from DrugBank (currently a High-severity data gap, DG002)
- Correction of the disease-label mapping in the TxGNN pipeline for the "lung benign neoplasm" and "lung germ cell tumor" candidates, which are evidencing ceritinib's existing indication rather than a new one
- If gingival fibromatosis is to be pursued further, dedicated preclinical/mechanistic studies establishing biological plausibility, since none currently exist
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

