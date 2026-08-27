---
layout: default
title: Cabozantinib
parent: 僅模型預測 (L5)
nav_order: 30
evidence_level: L5
indication_count: 10
---

# Cabozantinib
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

# Cabozantinib: From Renal Cell Carcinoma to Liposarcoma

## One-Sentence Summary

Cabozantinib is an oral multi-kinase inhibitor (VEGFR2 / MET / AXL) approved for renal cell carcinoma, where anti-angiogenic and MET-inhibitory activity are its core therapeutic mechanisms.
The TxGNN model predicts it may be effective for **Liposarcoma**,
with **1 clinical trial** and **1 publication** currently supporting this direction.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Renal Cell Carcinoma |
| Predicted New Indication | Liposarcoma |
| TxGNN Prediction Score | 99.83% |
| Evidence Level | L3 |
| Norway Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Research Question |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available from this Evidence Pack. Based on known pharmacological information, Cabozantinib (Cabometyx®) is a small-molecule tyrosine kinase inhibitor that simultaneously suppresses VEGFR2, MET, and AXL — three kinases central to tumor angiogenesis, invasive growth, and immune evasion. Its established efficacy in renal cell carcinoma, where VEGFR/MET co-activation is the primary oncogenic driver, has been confirmed in multiple Phase 3 trials and forms the pharmacological foundation for this repurposing hypothesis.

Liposarcoma — particularly the Dedifferentiated (DDLPS) and Myxoid/Round Cell (MRCLS) subtypes — is characterised by CDK4 amplification and MDM2 amplification, while a subset of tumours also demonstrates MET overexpression and aberrant AXL signalling. Cabozantinib's MET and AXL inhibitory activity may suppress tumour cell proliferation and attenuate immune escape in these subtypes. The mechanistic link is considered moderate: although direct CDK4/MDM2 targeting is outside cabozantinib's pharmacological profile, its anti-angiogenic and MET-inhibitory components provide biologically plausible antitumour activity against the vascular and invasive characteristics common to aggressive liposarcoma subtypes.

The ongoing Phase 2 trial NCT05836571 is evaluating the combination of cabozantinib with ipilimumab and nivolumab in advanced soft tissue sarcoma — a broad category that encompasses liposarcoma as a subtype — and a Phase 1 neoadjuvant study (PMID 41770651) demonstrates that concurrent cabozantinib with radiation therapy is being actively explored in extremity sarcomas. These early signals support the biological rationale, though liposarcoma-specific efficacy data remains absent at present.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|-------------|-------|--------|------------|--------------|
| [NCT05836571](https://clinicaltrials.gov/study/NCT05836571) | Phase 2 | Active, Not Recruiting | 66 | Randomised comparison of cabozantinib + ipilimumab + nivolumab versus ipilimumab + nivolumab alone in advanced soft tissue sarcoma; liposarcoma subtypes may be included but subgroup-specific results are pending — eligibility criteria should be reviewed to confirm liposarcoma representation |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|--------------|
| [41770651](https://pubmed.ncbi.nlm.nih.gov/41770651/) | 2026 | Phase 1 RCT | American Journal of Clinical Oncology | Phase 1 safety study of neoadjuvant cabozantinib combined with concurrent radiation therapy in patients with extremity soft tissue sarcoma; primary objective was to evaluate feasibility and the risk of fistula or perforation — historically a limiting concern for this combination |

---

## Cytotoxicity

| Item | Content |
|------|---------|
| Cytotoxicity Classification | Targeted therapy — Multi-kinase inhibitor (VEGFR2 / MET / AXL) |
| Myelosuppression Risk | Moderate — neutropenia and thrombocytopenia reported in pivotal RCC trials; require close haematological monitoring |
| Emetogenicity Classification | Low to moderate |
| Monitoring Items | CBC with differential, liver function (ALT / AST / bilirubin), renal function, thyroid function, blood pressure, urine protein |
| Handling Protection | Please refer to the package insert warnings and precautions |

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Research Question**

**Rationale:**
Available evidence is limited to one Phase 2 trial in broad soft tissue sarcoma (which may include liposarcoma as a subtype but has not published liposarcoma-specific efficacy outcomes) and one Phase 1 safety study; there are no liposarcoma-specific efficacy endpoints reported to date, making a formal repurposing progression decision premature.

**To proceed, the following is needed:**
- Confirm whether NCT05836571 contains a liposarcoma-specific subgroup with independently analysable efficacy data; request sub-group results from the trial investigators if needed
- Identify or conduct preclinical studies (liposarcoma cell lines, xenograft models) to establish proof-of-concept for MET/AXL-mediated activity in DDLPS or MRCLS subtypes
- Obtain full MOA data via DrugBank API query to complete the mechanistic link analysis
- Retrieve the package insert (Taiwan TFDA or EMA/FDA source) to complete safety profiling: warnings, contraindications, and key drug interactions
- Define the most biologically relevant liposarcoma subtype(s) for prioritisation (Dedifferentiated vs. Myxoid vs. Pleomorphic) based on available MET / AXL expression data from public genomic databases (e.g., COSMIC, cBioPortal)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

