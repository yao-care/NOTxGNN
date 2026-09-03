---
layout: default
title: Vandetanib
parent: 僅模型預測 (L5)
nav_order: 378
evidence_level: L5
indication_count: 10
---

# Vandetanib
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

# Vandetanib: From Medullary Thyroid Cancer to Renal Cell Carcinoma

## One-Sentence Summary

> Vandetanib is a multi-target tyrosine kinase inhibitor (VEGFR2/EGFR/RET) internationally approved for advanced medullary thyroid cancer (MTC), though it is **not currently marketed in Norway**.
> The TxGNN model predicts it may also be effective for **Renal Cell Carcinoma**,
> with **4 clinical trials** (2 completed, 2 terminated) and **6 publications** currently supporting this direction — though the trial evidence is limited by small sample sizes and early termination.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not marketed in Norway (0 authorizations); internationally approved for Medullary Thyroid Cancer (MTC), per literature evidence (PMID 24451769, 32691271) |
| Predicted New Indication | Renal Cell Carcinoma (disease) |
| TxGNN Prediction Score | 99.92% |
| Evidence Level | L3 (Research Question / Decision Stage S1) |
| Norway Market Status | ✗ Not Marketed (未上市) |
| Number of Authorizations | 0 |
| Recommended Decision | **Hold** |

---

## Why is This Prediction Reasonable?

Formal mechanism-of-action documentation for vandetanib is currently a data gap (DG002, High severity). Based on the information available within this evidence pack, vandetanib is characterized as a **VEGFR2/EGFR/RET multi-target tyrosine kinase inhibitor** — the same antiangiogenic mechanism shared by already-approved RCC drugs such as sunitinib, pazopanib, and cabozantinib (see literature PMID 28477875, 26677336).

Renal cell carcinoma, particularly clear cell and VHL-associated subtypes, is strongly driven by VEGF/HIF pathway overactivation, making VEGFR2 inhibition mechanistically plausible. This is partly supported by a completed Phase 2 trial in VHL-associated renal tumors (NCT00566995, n=37, grade B relevance). However, vandetanib's direct clinical evidence in RCC remains sparse compared to its established, RET-driven mechanism in MTC — most RCC-specific trials for vandetanib were terminated early or severely underpowered (n=3–7), suggesting the mechanistic rationale has not yet translated into robust clinical proof for this specific drug (as opposed to its drug class).

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00566995](https://clinicaltrials.gov/study/NCT00566995) | Phase 2 | Completed | 37 | Vandetanib in VHL-associated renal tumors; single-arm, mechanism-relevant population; no reported efficacy outcome data in this pack (grade B) |
| [NCT02495103](https://clinicaltrials.gov/study/NCT02495103) | Phase 1/2 | Terminated | 7 | Vandetanib + metformin in HLRCC/SDH-associated or sporadic papillary RCC; extremely small sample, rare subtype (grade C) |
| [NCT01372813](https://clinicaltrials.gov/study/NCT01372813) | Phase 2 | Terminated | 3 | Vandetanib monotherapy in advanced clear cell RCC; terminated with n=3, no statistical power (grade C) |
| [NCT01191892](https://clinicaltrials.gov/study/NCT01191892) | Phase 2 | Completed | 82 | Carboplatin/gemcitabine ± vandetanib; regimen is atypical for RCC (more consistent with NSCLC/urothelial protocols) — indication tagging flagged as needing manual verification (grade C) |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [40779213](https://pubmed.ncbi.nlm.nih.gov/40779213/) | 2025 | Review | Clin Exp Metastasis | Targeted/epigenetic strategies in fumarate hydratase-deficient RCC; no direct vandetanib efficacy data |
| [36302175](https://pubmed.ncbi.nlm.nih.gov/36302175/) | 2023 | Phase 2 (other drug) | Clin Cancer Res | Guadecitabine trial in SDH-deficient tumors including HLRCC-RCC; comparator mechanism context only |
| [31043488](https://pubmed.ncbi.nlm.nih.gov/31043488/) | 2019 | Preclinical (mouse model) | Mol Cancer Res | TFE3-RCC mouse model identifies novel therapeutic targets; no vandetanib-specific data |
| [26677336](https://pubmed.ncbi.nlm.nih.gov/26677336/) | 2015 | Review (other drug) | OncoTargets Ther | Antiangiogenic TKI class review (sunitinib, sorafenib, pazopanib, vandetanib) across solid tumors |
| [28477875](https://pubmed.ncbi.nlm.nih.gov/28477875/) | 2017 | Review (other drug) | Bull Cancer | Cabozantinib MOA/efficacy review; contextualizes shared VEGFR2/RET target class |
| [24451769](https://pubmed.ncbi.nlm.nih.gov/24451769/) | 2012 | Review | ASCO Educational Book | Confirms vandetanib's FDA-approved RET-driven mechanism in medullary thyroid cancer — supports original indication context |

---

## Other Predicted Indications (Ranks 2–10, Lower Evidence)

These additional TxGNN-predicted candidates share high prediction scores but lack direct clinical or literature support; all are at decision stage S0 (Hold) except the two entries below.

| Rank | Disease | TxGNN Score | Evidence Level | Recommendation | Note |
|------|---------|------|------|------|------|
| 2 | RCC (Xp11.2/TFE3 fusion) | 99.90% | L5 | Hold | No trials/literature; network-similarity inference only |
| 3 | RCC associated with neuroblastoma | 99.90% | L5 | Hold | No direct evidence; rare disease association |
| 4 | Unclassified RCC | 99.90% | L5 | Hold | No direct evidence |
| 5 | Renal pelvis carcinoma | 99.88% | L4 | Hold | Sole trial (NCT01191892) has questionable indication tagging; histology differs from RCC |
| 6 | Clear cell renal carcinoma | 99.87% | **L3** | **Research Question** | Strongest sub-evidence: VHL-population trial (NCT00566995) + 16 literature items; overlaps with rank-1 rationale |
| 7 | Childhood kidney cell carcinoma | 99.86% | L5 | Hold | No pediatric trials/literature; safety in children unestablished |
| 8 | Renal carcinoma (general) | 99.83% | **L3** | **Research Question** | Aggregates same trials/literature as ranks 1 and 6 |
| 9 | Angiolipoma | 99.82% | L5 | Hold | No known VEGFR/EGFR/RET pathology link; likely network artifact (e.g., tuberous sclerosis co-morbidity) |
| 10 | Familial spontaneous pneumothorax | 99.76% | L5 | Hold | No plausible mechanistic link; likely prediction artifact (e.g., Birt-Hogg-Dubé network proximity); not recommended for further investment |

---

## Norway Market Information

Vandetanib currently holds **0 marketing authorizations** in Norway (market status: 未上市 / Not Marketed). No product listings, dosage forms, or approved indication text are available in the regulatory dataset for this drug.

---

## Cytotoxicity

Vandetanib is an antineoplastic agent (targeted kinase inhibitor class; approved indication involves cancer treatment), so this section applies.

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy — multi-target tyrosine kinase inhibitor (VEGFR2, EGFR, RET) |
| Myelosuppression Risk | Low — TKIs generally cause less myelosuppression than conventional cytotoxics; class-wide hepatotoxicity (PMID 23981115) and proteinuria (PMID 32105149) are more prominent reported risks |
| Emetogenicity Classification | Low to Moderate (typical for oral TKIs) |
| Monitoring Items | Liver function tests, renal function/urinalysis (proteinuria monitoring), blood pressure, baseline CBC; a class-wide treatment-related mortality meta-analysis (PMID 22651902) supports close monitoring during therapy |
| Handling Protection | TFDA package insert is not yet available (Blocking data gap, DG001) — formal handling protocol cannot be confirmed; standard oral antineoplastic handling precautions recommended pending resolution |

---

## Safety Considerations

Please refer to the package insert for safety information. Formal warnings, contraindications, and drug-drug interaction data for vandetanib are not yet available in this evidence pack (DG001, Blocking severity) — this gap currently **prevents completion of the S1 safety pre-assessment**.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The strongest candidate indication (renal cell carcinoma, rank 1) reaches only evidence level L3 (Research Question stage), supported by trials that are largely terminated or severely underpowered (n=3–7), with only one adequately sized completed trial (n=37) in a rare VHL-associated subgroup. Critically, TFDA safety/warning data is a **Blocking** data gap, which prevents the mandatory S1 safety pre-assessment from being completed, and the drug is not currently marketed in Norway.

**To proceed, the following is needed:**
- Resolve DG001 (Blocking): obtain TFDA or equivalent regulatory package insert data on warnings and contraindications
- Resolve DG002 (High): obtain formal MOA documentation from DrugBank or equivalent source
- Clarify apparent indication mislabeling in NCT01191892 (regimen more consistent with NSCLC/urothelial than RCC)
- Identify larger, adequately powered RCC-specific trials for vandetanib (current trials are terminated or underpowered)
- Assess Norway market entry / import pathway feasibility given current "not marketed" status
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

