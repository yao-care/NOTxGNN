---
layout: default
title: Plerixafor
parent: 僅模型預測 (L5)
nav_order: 282
evidence_level: L5
indication_count: 7
---

# Plerixafor
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

# Plerixafor: From Stem Cell Mobilization to Myeloid Leukemia (Chemosensitization Adjunct)

## One-Sentence Summary

> Plerixafor is a CXCR4 antagonist originally used to mobilize hematopoietic stem cells for autologous transplantation in multiple myeloma and lymphoma patients.
> Although the TxGNN model's single highest-scoring prediction (indolent plasma cell myeloma) has no supporting trial or literature evidence, a lower-ranked prediction — **Myeloid Leukemia**, used as a chemosensitizing adjunct — is backed by **~30 registered clinical trials** and **20 publications**, including several completed Phase 1/1-2 studies. This report focuses on that better-supported indication.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available from Norway license data (drug not marketed); per repurposing rationale, plerixafor's approved use is HSC mobilization for autologous transplantation (e.g., in multiple myeloma/NHL patients) |
| Predicted New Indication | Myeloid Leukemia (as a CXCR4-blockade chemosensitization adjunct, not monotherapy) |
| TxGNN Prediction Score | 99.02% (rank 9390 of predictions; note this is *not* the top-ranked candidate — see below) |
| Evidence Level | L2 |
| Norway Market Status | ✗ Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

**Note on ranking:** The model's #1-ranked candidate by raw score is *indolent plasma cell myeloma* (99.97%), but it has zero associated clinical trials or literature (Evidence Level L5, decision stage S0). Myeloid leukemia was selected as the subject of this report because it is the only candidate among the seven predictions in this evidence pack with substantive supporting evidence (Evidence Level L2, decision stage S2, "Research Question"). The other five candidates (CMM7, pediatric leptomeningeal melanoma, epithelioid uveal melanoma, bronchitis, vulvar melanoma) are all L5/Hold with no trial or literature support and are not detailed further here.

---

## Why is This Prediction Reasonable?

Detailed formal mechanism-of-action data for plerixafor is not available in this evidence pack (flagged as a High-severity data gap). Based on the information that is available: plerixafor is a **CXCR4 antagonist**. It is approved to mobilize hematopoietic stem cells (HSCs) out of the bone marrow niche by blocking the CXCR4/CXCL12 (SDF-1α) interaction, which normally anchors HSCs — and other CXCR4-expressing cells — within the marrow microenvironment.

In acute myeloid leukemia (AML), leukemic blasts and leukemia stem cells use this same CXCR4/CXCL12 axis to adhere to the bone marrow niche, where the niche shields them from chemotherapy and drives relapse. The repurposing hypothesis is therefore mechanistically direct, not merely analogical: blocking CXCR4 with plerixafor should mobilize leukemic cells out of their protective niche and into circulation, increasing their sensitivity to concurrent chemotherapy ("chemosensitization"). This is a much tighter mechanistic link than the top TxGNN-scored candidate (indolent plasma cell myeloma), where the rationale explicitly notes the evidence for direct anti-tumor extrapolation is weak, since plerixafor's approved myeloma use is adjunctive stem-cell mobilization, not direct anti-myeloma activity.

Multiple research groups have tested this AML chemosensitization hypothesis in Phase 1 and Phase 1/2 trials combining plerixafor with G-CSF and standard AML chemotherapy backbones (cytarabine/daunorubicin, decitabine, sorafenib, fludarabine/idarubicin/cytarabine), generally showing feasibility and blast mobilization, though without a confirmatory Phase 3 efficacy trial to date.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT01319864](https://clinicaltrials.gov/study/NCT01319864) | Phase 1 | Completed | 20 | Plerixafor + cytarabine/etoposide in pediatric relapsed AML/MDS; tested as a chemosensitizer to mobilize leukemic cells out of the protective marrow niche |
| [NCT01141543](https://clinicaltrials.gov/study/NCT01141543) | N/A | Completed | 12 | Plerixafor as part of a myeloablative preparative regimen (fludarabine/busulfan/TBI) before allografting in AML; assessed feasibility of mobilizing residual leukemic stem cells |
| [NCT01352650](https://clinicaltrials.gov/study/NCT01352650) | Phase 1 | Completed | 71 | Decitabine + plerixafor priming as induction/postremission therapy in AML patients ≥60 years |
| [NCT00943943](https://clinicaltrials.gov/study/NCT00943943) | Phase 1 | Completed | 33 | G-CSF + plerixafor + sorafenib in FLT3-mutated AML; established most tolerable combination dose |
| [NCT00822770](https://clinicaltrials.gov/study/NCT00822770) | Phase 1/2 | Completed | 47 | G-CSF + plerixafor with busulfan/fludarabine conditioning before allogeneic transplant in AML/MDS/CML |
| [NCT00512252](https://clinicaltrials.gov/study/NCT00512252) | Phase 1/2 | Completed | 52 | AMD3100 (plerixafor) + mitoxantrone/etoposide/cytarabine (MEC) in relapsed/refractory AML; hypothesized disruption of AML-marrow interaction enhances chemo cytotoxicity |
| [NCT00906945](https://clinicaltrials.gov/study/NCT00906945) | Phase 1/2 | Completed | 39 | Plerixafor + G-CSF chemosensitization in relapsed/refractory AML |
| [NCT01696461](https://clinicaltrials.gov/study/NCT01696461) | Phase 2 | Completed | 127 | Subcutaneous plerixafor for mobilization/transplantation of HLA-matched sibling donor HSCs in hematological malignancies; largest trial in this evidence set |
| [NCT01236144](https://clinicaltrials.gov/study/NCT01236144) | Phase 1/2 | Completed | 113 | NCRI pilot trial testing plerixafor (and other agents) combined with chemotherapy in older AML/high-risk MDS patients |
| [NCT00990054](https://clinicaltrials.gov/study/NCT00990054) | Phase 1 | Completed | 36 | Dose-escalation of plerixafor with cytarabine/daunorubicin ("7+3") in newly diagnosed AML; tested chemosensitization to standard induction |

*Additional trials exist in this program (e.g., NCT01455025, NCT02605460, NCT06141304) but were terminated, of unknown status, or evaluate a different CXCR4 antagonist (POL6326) and are not listed above.*

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [22308295](https://pubmed.ncbi.nlm.nih.gov/22308295/) | 2012 | Phase 1/2 trial | Blood | 52 patients with relapsed/refractory AML treated with plerixafor as chemosensitization; foundational study for the CXCR4-blockade hypothesis in AML |
| [29392425](https://pubmed.ncbi.nlm.nih.gov/29392425/) | 2018 | Phase I-II trial | Annals of Hematology | PLERIFLAG regimen (FLAG-Ida + high-dose IV plerixafor) in first early-relapsed/refractory AML |
| [32697348](https://pubmed.ncbi.nlm.nih.gov/32697348/) | 2020 | Phase 1 trial | American Journal of Hematology | Sorafenib + G-CSF + plerixafor in 28 relapsed/refractory FLT3-ITD-mutated AML patients |
| [29724902](https://pubmed.ncbi.nlm.nih.gov/29724902/) | 2018 | Phase 1 trial | Haematologica | Plerixafor + decitabine in 69 newly diagnosed older AML patients; evaluated effect on leukemia stem cells |
| [30654137](https://pubmed.ncbi.nlm.nih.gov/30654137/) | 2019 | Clinical study | Biology of Blood and Marrow Transplantation | Safety/tolerability of plerixafor with myeloablative conditioning before allogeneic HCT in AML |
| [31723817](https://pubmed.ncbi.nlm.nih.gov/31723817/) | 2019 | Clinical study | HemaSphere | Plerixafor is safe and effective for HSC mobilization in poorly-mobilizing AML patients |
| [32877869](https://pubmed.ncbi.nlm.nih.gov/32877869/) | 2020 | Systematic review & meta-analysis | Leukemia Research | Pooled preclinical and clinical evidence on plerixafor combined with chemotherapy/HCT for acute leukemia |
| [28718760](https://pubmed.ncbi.nlm.nih.gov/28718760/) | 2018 | Clinical study (biomarker analysis) | Leukemia & Lymphoma | CD25 expression associated with resistance/survival in older AML patients treated with plerixafor + decitabine |
| [30150522](https://pubmed.ncbi.nlm.nih.gov/30150522/) | 2018 | Case report | Cancers | Complete remission of refractory pediatric AML (monosomy 7) after plerixafor/cytarabine/melphalan conditioning |
| [39261603](https://pubmed.ncbi.nlm.nih.gov/39261603/) | 2024 | Review | Leukemia | Comprehensive review of the CXCL12-CXCR4 axis and its therapeutic targeting in AML |

---

## Norway Market Information

Plerixafor currently has **no marketing authorizations recorded in Norway** (0 licenses; market status: not marketed). No product name, dosage form, or approved indication text is available for this market.

---

## Safety Considerations

Please refer to the package insert for safety information. No structured warnings, contraindications, or drug interaction data were available in this evidence pack; TFDA-equivalent label data (warnings/contraindications) is flagged as a **Blocking**-severity data gap that must be resolved before formal safety screening can proceed.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The AML chemosensitization hypothesis has a mechanistically direct rationale (CXCR4/CXCL12 blockade releasing leukemic blasts from the protective marrow niche) and is supported by roughly a dozen completed Phase 1 and Phase 1/2 trials plus a systematic review — a meaningfully stronger evidence base than any of the other six TxGNN-flagged indications, including the model's top-scored candidate. However, no completed Phase 3 confirmatory trial exists, the drug is not currently marketed in Norway, and label-level safety data (warnings/contraindications) is a **Blocking** data gap that prevents even a preliminary safety evaluation.

**To proceed, the following is needed:**
- Regulatory-grade safety data (TFDA or equivalent label: warnings, contraindications, DDI) — currently blocking
- Formal mechanism-of-action documentation for the drug record (currently missing)
- Assessment of whether any ongoing/planned Phase 3 trial exists for plerixafor-based AML chemosensitization
- Clarification of route/formulation compatibility with an AML treatment setting (subcutaneous vs. IV use in combination regimens)
- If the top TxGNN-ranked candidate (indolent plasma cell myeloma) is to be pursued instead, dedicated trial and literature evidence must first be sourced, as none currently exists
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

