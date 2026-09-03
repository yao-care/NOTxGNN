---
layout: default
title: Zanubrutinib
parent: 僅模型預測 (L5)
nav_order: 390
evidence_level: L5
indication_count: 6
---

# Zanubrutinib
{: .fs-9 }

證據等級: **L5** | 預測適應症: **6** 個
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

# Zanubrutinib: From B-Cell Lymphoid Malignancies to Myeloid Leukemia

## One-Sentence Summary

> Zanubrutinib is a selective Bruton's tyrosine kinase (BTK) inhibitor currently used for B-cell lymphoid malignancies such as CLL/SLL and Waldenström macroglobulinemia.
> The TxGNN model predicts it may be effective for **Myeloid Leukemia**,
> but only **2 clinical trials** (neither testing zanubrutinib itself) and **9 publications** (none specific to myeloid leukemia) are currently available, and the mechanistic rationale is weak.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | B-cell lymphoid malignancies (CLL/SLL, Waldenström macroglobulinemia) — no formal Norway license record available |
| Predicted New Indication | Myeloid Leukemia |
| TxGNN Prediction Score | 99.65% |
| Evidence Level | L4 |
| Norway Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available (data gap DG002). Based on known information contained in this evidence pack, zanubrutinib is a highly selective, next-generation BTK inhibitor that blocks B-cell receptor (BCR) signaling, and its clinical benefit has been established in B-cell lymphoid malignancies (CLL/SLL, Waldenström macroglobulinemia, and other B-cell disorders).

Myeloid leukemia, however, is a myeloid-lineage rather than lymphoid-lineage malignancy, and its pathogenesis is predominantly driven by FLT3, KIT, and BCR-ABL kinase signaling — none of which are established targets of BTK inhibition. There is no recognized mechanistic overlap between the BTK/BCR pathway and myeloid leukemogenesis.

Given this, the TxGNN prediction likely reflects a broad-category over-generalization (grouping all "leukemia" subtypes together) rather than a biologically grounded signal. This assessment is reinforced by the fact that the two retrieved clinical trials test unrelated compounds (PRT2527, a CDK9 inhibitor; and CG-806/luxeptinib, a multi-kinase inhibitor) rather than zanubrutinib itself, and no literature specifically addresses zanubrutinib in myeloid leukemia.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT05665530](https://clinicaltrials.gov/study/NCT05665530) | Phase 1 | Completed | 86 | Study of PRT2527 (a CDK9 inhibitor), evaluated as monotherapy and in combination with zanubrutinib or venetoclax, in relapsed/refractory hematologic malignancies. **Relevance grade C** — the investigational drug is PRT2527, not zanubrutinib; only the disease domain (hematologic malignancy) overlaps. Does not constitute direct evidence for zanubrutinib in myeloid leukemia. |
| [NCT04477291](https://clinicaltrials.gov/study/NCT04477291) | Phase 1a/b | Terminated | 45 | Evaluated CG-806 (luxeptinib, a multi-kinase inhibitor) in relapsed/refractory AML or higher-risk MDS. **Relevance grade C** — different drug and mechanism than zanubrutinib; trial was terminated. Background context only. |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [39647999](https://pubmed.ncbi.nlm.nih.gov/39647999/) | 2025 | RCT | J Clin Oncol | SEQUOIA 5-year follow-up: zanubrutinib vs bendamustine+rituximab in treatment-naïve CLL/SLL — supports established indication, not myeloid leukemia. |
| [40334067](https://pubmed.ncbi.nlm.nih.gov/40334067/) | 2025 | Cohort | Blood Advances | Zanubrutinib well tolerated/effective in CLL/SLL patients intolerant of ibrutinib/acalabrutinib (BGB-3111-215 study). |
| [40829104](https://pubmed.ncbi.nlm.nih.gov/40829104/) | 2026 | Cohort (pooled analysis) | Blood Advances | Pooled analysis (SEQUOIA/ALPINE) of zanubrutinib efficacy/safety in del(17p)/TP53-mutated CLL/SLL. |
| [36400069](https://pubmed.ncbi.nlm.nih.gov/36400069/) | 2023 | Cohort | Lancet Haematol | Phase 2 single-arm study of zanubrutinib in BTK-inhibitor-intolerant B-cell malignancies. |
| [34959482](https://pubmed.ncbi.nlm.nih.gov/34959482/) | 2021 | Review | Pharmaceutics | Review of tyrosine kinase inhibitors in chronic leukemias (CML, CLL) — general background, not zanubrutinib-specific myeloid data. |
| [36402930](https://pubmed.ncbi.nlm.nih.gov/36402930/) | 2023 | Review | Leukemia | Review of BTK inhibitors (including zanubrutinib) in Waldenström macroglobulinemia management. |
| [37150651](https://pubmed.ncbi.nlm.nih.gov/37150651/) | 2023 | Review | Clin Lymphoma Myeloma Leuk | HBV reactivation risk review in patients on BTK inhibitors (ibrutinib, acalabrutinib, zanubrutinib). |
| [38288815](https://pubmed.ncbi.nlm.nih.gov/38288815/) | 2024 | Review | Anticancer Agents Med Chem | Synthetic chemistry review of FDA-approved anticancer drugs (2018–2021); mentions zanubrutinib only in a chemistry-synthesis context, not clinical efficacy. |
| [36325357](https://pubmed.ncbi.nlm.nih.gov/36325357/) | 2022 | Case Report | Front Immunol | Case report of coexisting Waldenström macroglobulinemia and B-ALL — disease background only, no zanubrutinib treatment data. |

**Note:** None of the above literature reports zanubrutinib efficacy or safety data specifically in myeloid leukemia; all directly relevant studies pertain to its established B-cell lymphoid malignancy indications.

---

## Norway Market Information

Zanubrutinib is currently **not marketed** in Norway, and no authorization records are available in this evidence pack.

---

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (selective BTK inhibitor) |
| Myelosuppression Risk | Please refer to the package insert warnings and precautions |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | Please refer to the package insert warnings and precautions |
| Handling Protection | Please refer to the package insert warnings and precautions |

---

## Safety Considerations

Please refer to the package insert for safety information.

*(Note: TFDA label warnings/contraindications data are currently missing — see DG001, classified as Blocking, which prevents entry into the S1 safety pre-assessment stage.)*

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked candidate indication (myeloid leukemia, L4) lacks any clinical trial or literature evidence directly testing zanubrutinib in this disease, and the mechanistic link is biologically weak — BTK is not a recognized driver in myeloid leukemogenesis, whereas the retrieved trials/literature only test unrelated compounds or support zanubrutinib's already-established B-cell lymphoid indications. The remaining five candidates (ranks 2–6) are all L5 (pure model prediction with zero supporting evidence), and the drug is not yet marketed in Norway.

**To proceed, the following is needed:**
- TFDA/regulatory label data (warnings, contraindications) — currently a Blocking data gap (DG001)
- Confirmed mechanism of action documentation (DG002)
- Direct preclinical or clinical evidence linking BTK inhibition to myeloid leukemia pathophysiology, if this indication is to be pursued further
- If pursuing repurposing research, prioritize re-scoring or excluding rank 2–6 candidates given the complete absence of supporting evidence
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

