---
layout: default
title: Trabectedin
parent: 僅模型預測 (L5)
nav_order: 366
evidence_level: L5
indication_count: 1
---

# Trabectedin
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

# Trabectedin: From Soft Tissue Sarcoma / Ovarian Cancer to Female Breast Carcinoma

## One-Sentence Summary

> Trabectedin is a marine-derived cytotoxic agent currently used internationally for advanced soft tissue sarcoma and, in combination with pegylated liposomal doxorubicin (PLD), for platinum-sensitive relapsed ovarian cancer.
> The TxGNN model predicts it may also be effective for **Female Breast Carcinoma**, particularly in BRCA1/2-mutated or homologous-recombination-deficient tumours,
> with **2 registered clinical trials** and **20 publications** currently identified, including two early-phase breast cancer trials.
> The drug is **not currently marketed in Norway**, and several safety data fields remain unresolved.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | No Norway license on file (drug not marketed). Per international literature, trabectedin is EU-approved for second-line soft tissue sarcoma and, combined with PLD, for platinum-sensitive relapsed ovarian cancer. |
| Predicted New Indication | Female Breast Carcinoma |
| TxGNN Prediction Score | 99.73% (rank 3480) |
| Evidence Level | L2 |
| Norway Market Status | ✗ Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in this evidence pack (flagged as a High-severity data gap). Based on published pharmacology literature, trabectedin is a DNA minor-groove alkylator that preferentially binds GC-rich sequences and interferes with transcription-coupled nucleotide excision repair (TC-NER). This produces selective cytotoxicity in tumours with nucleotide excision repair (NER) or homologous recombination (HR) deficiencies — most notably *BRCA1/2*-mutated cells — and separately modulates the tumour microenvironment by depleting tumour-associated macrophages.

This mechanism plausibly extends from sarcoma and ovarian cancer to breast cancer because a meaningful subset of breast tumours, especially triple-negative and hereditary *BRCA1/2*-mutated cases, share the same HR-deficient (synthetic-lethal) biology that underlies trabectedin's activity in ovarian cancer. Several identified trials and publications directly test this hypothesis, including a phase II study restricted to germline *BRCA1/2*-mutated metastatic breast cancer and an olaparib maintenance study following trabectedin+PLD response, reinforcing the mechanistic rationale for the TxGNN prediction rather than establishing it as a novel, unexplained signal.

It should be noted that the reported *BRCA*/HR-pathway rationale above is derived from external literature, not from the structured `original_moa` field, which remains a data gap in this evidence pack.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00786838](https://clinicaltrials.gov/study/NCT00786838) | Phase 2 | Completed | 76 | Single-blind, multicenter, placebo-controlled, sequential-design study evaluating trabectedin's effect on QT/QTc interval in patients with advanced solid tumor malignancies (cardiac safety study, not breast-cancer efficacy). |
| [NCT03470805](https://clinicaltrials.gov/study/NCT03470805) | Phase 2 | Completed | 9 | Olaparib maintenance therapy after response to trabectedin + pegylated liposomal doxorubicin in recurrent ovarian carcinoma; tests the BRCA/HR-deficiency rationale relevant to breast cancer, but extremely small sample size (n=9). |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [25239225](https://pubmed.ncbi.nlm.nih.gov/25239225/) | 2014 | Phase 2 RCT | Clinical Breast Cancer | Multicenter, randomized phase II study of single-agent trabectedin in advanced breast cancer after anthracycline/taxane failure, comparing two administration regimens. |
| [24692579](https://pubmed.ncbi.nlm.nih.gov/24692579/) | 2014 | Phase 2 | Ann Oncol | First-in-class phase II study of trabectedin in germline *BRCA1/2*-mutated metastatic breast cancer; direct clinical support for the HR-deficiency mechanistic link. |
| [27266804](https://pubmed.ncbi.nlm.nih.gov/27266804/) | 2016 | Phase 2 | Clinical Breast Cancer | Phase 2 study of trabectedin in HR-positive, HER2-negative advanced breast cancer stratified by XPG gene expression as a predictive biomarker. |
| [25722380](https://pubmed.ncbi.nlm.nih.gov/25722380/) | 2015 | Phase 3 (exploratory) | Ann Oncol | Exploratory analysis of the phase 3 OVA-301 trial showing *BRCA1*/XPG mutation status predicts response to trabectedin + PLD, supporting the biomarker-driven rationale. |
| [39777457](https://pubmed.ncbi.nlm.nih.gov/39777457/) | 2025 | Preclinical | Cancer Immunol Res | Trabectedin depletes immunosuppressive myeloid cells and enhances IL-12-driven NK-cell cytotoxicity in triple-negative breast cancer models. |
| [26592307](https://pubmed.ncbi.nlm.nih.gov/26592307/) | 2016 | Review | Expert Opin Investig Drugs | Reviews trabectedin's investigational use in breast cancer, including its dual cytotoxic and tumour-microenvironment-modulating mechanisms. |
| [27710871](https://pubmed.ncbi.nlm.nih.gov/27710871/) | 2016 | Review | Cancer Treat Rev | Discusses trabectedin as a chemotherapy option specifically for patients with BRCA deficiency across tumour types. |
| [23792433](https://pubmed.ncbi.nlm.nih.gov/23792433/) | 2013 | Preclinical | Toxicology Letters | Trabectedin induces apoptosis via distinct pathways in HER2-/ER+ (MCF-7) and HER2+/ER- (MDA-MB-453) breast cancer cell lines. |
| [24941346](https://pubmed.ncbi.nlm.nih.gov/24941346/) | 2014 | Preclinical | Eur Cytokine Netw | Demonstrates anti-angiogenic effects of trabectedin in human breast cancer cell lines and endothelial cells. |
| [19114300](https://pubmed.ncbi.nlm.nih.gov/19114300/) | 2009 | Phase 1 | Eur J Cancer | Phase I pharmacokinetic study of trabectedin plus doxorubicin in advanced soft tissue sarcoma and breast cancer (mixed population, feasibility data). |

---

## Norway Market Information

Trabectedin currently holds **no marketing authorization in Norway** (0 licenses on file). No dosage forms or authorization numbers are available for extraction.

---

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Conventional cytotoxic — marine-derived DNA minor-groove alkylator (tetrahydroisoquinoline alkaloid), interferes with transcription-coupled DNA repair |
| Myelosuppression Risk | High — literature (PMID 19496709) reports grade 3–4 neutropenia in ~50% and thrombocytopenia in ~20% of patients; hepatic transaminase elevation is also common |
| Emetogenicity Classification | Moderate (based on general oncology literature for trabectedin; not confirmed against a Norwegian/local package insert, which is currently a data gap) |
| Monitoring Items | CBC with differential, liver function tests (AST/ALT/bilirubin), renal function, creatine phosphokinase |
| Handling Protection | Yes — must follow standard cytotoxic drug handling and disposal protocols (IV infusion, closed-system transfer where available) |

---

## Safety Considerations

Formal safety data (key warnings, contraindications, drug-drug interactions) are not yet available for this candidate — this is flagged as a **Blocking** data gap (DG001: TFDA/local label warnings and contraindications pending). Please refer to the package insert once available for definitive safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The mechanistic rationale (HR/BRCA-deficiency synthetic lethality) is biologically sound and supported by early-phase clinical data, but evidence for breast cancer specifically remains limited to small, single-arm or biomarker-stratified phase II studies (largest breast-cancer-specific cohort: proof-of-concept scale). Combined with the drug's non-marketed status in Norway and a **Blocking** safety data gap (no TFDA/local warnings or contraindications on file), this candidate is not yet ready for indication-expansion evaluation.

**To proceed, the following is needed:**
- Resolve DG001 (blocking): obtain TFDA/local package insert warnings and contraindications
- Resolve DG002 (high): confirm original mechanism of action from DrugBank API to validate the mechanistic rationale presented here
- Larger, randomized breast-cancer-specific trial data, ideally enriched for BRCA1/2-mutated or HR-deficient populations
- Assessment of feasibility for Norway market entry, since the drug currently holds no local authorization
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

