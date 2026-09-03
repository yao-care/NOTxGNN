---
layout: default
title: Bexarotene
parent: 僅模型預測 (L5)
nav_order: 51
evidence_level: L5
indication_count: 3
---

# Bexarotene
{: .fs-9 }

證據等級: **L5** | 預測適應症: **3** 個
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

# Bexarotene: From Cutaneous T-Cell Lymphoma to Primary Cutaneous B-Cell Lymphoma

## One-Sentence Summary

> Bexarotene is a synthetic RXR-selective retinoid whose established use, per the accompanying literature evidence, is advanced/refractory cutaneous T-cell lymphoma (CTCL, including mycosis fungoides and Sézary syndrome).
> The TxGNN model predicts it may also be effective for **Primary Cutaneous B-Cell Lymphoma**,
> currently supported by **2 clinical trials** and **12 publications** — though none of these directly test bexarotene efficacy in a B-cell lymphoma population.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Cutaneous T-cell Lymphoma (CTCL) / Mycosis fungoides — inferred from supporting literature; not confirmed via structured regulatory data |
| Predicted New Indication | Primary Cutaneous B-Cell Lymphoma |
| TxGNN Prediction Score | 99.44% |
| Evidence Level | L4 |
| Norway Market Status | ✗ Not marketed (未上市) |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data for bexarotene is not available in this Evidence Pack (flagged as a High-severity data gap, DG002). Based on supporting literature (e.g., PMID 11702369), bexarotene is a selective retinoid X receptor (RXR) agonist that binds to and activates RXRs, which function as ligand-activated transcription factors controlling gene expression — this modulates cell growth, apoptosis, and differentiation in malignant lymphocytes. This mechanism underlies its established efficacy in cutaneous T-cell lymphoma (CTCL).

Primary cutaneous B-cell lymphoma and CTCL are both primary cutaneous lymphomas that share overlapping diagnostic, staging, and management frameworks (WHO/EORTC classification), and both are managed within the same "cutaneous lymphoma" clinical pathway. This shared disease-family context is the likely basis for the TxGNN model's prediction.

However, the mechanistic rationale linking RXR agonism specifically to malignant B-cell (rather than T-cell) biology is not established in the evidence provided — the clinical trials and literature retrieved for this indication largely describe cutaneous lymphoma diagnosis/management in general, or bexarotene's efficacy in T-cell disease, rather than direct evidence of B-cell lymphoma response to bexarotene.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT05106192](https://clinicaltrials.gov/study/NCT05106192) | NA | Withdrawn | 0 | Planned comparison of a needle-free triamcinolone delivery system vs. standard care in cutaneous T-cell and B-cell lymphoma plaques; trial withdrawn, no data generated |
| [NCT01134341](https://clinicaltrials.gov/study/NCT01134341) | Phase 1 | Completed | 34 | Dose-finding study of pralatrexate + oral bexarotene in relapsed/refractory CTCL; population is CTCL, not specifically B-cell lymphoma |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [31466585](https://pubmed.ncbi.nlm.nih.gov/31466585/) | 2019 | Review | Dermatologic Clinics | Overview of diagnosis and management of primary cutaneous B-cell lymphomas; notes limited treatment-guideline data and preference for localized therapies |
| [34059248](https://pubmed.ncbi.nlm.nih.gov/34059248/) | 2021 | Review | Medical Clinics of North America | Diagnosis/management of cutaneous lymphomas including CTCL; general disease-class overview |
| [31932947](https://pubmed.ncbi.nlm.nih.gov/31932947/) | 2020 | Review | Der Pathologe | Notes bexarotene as a systemic therapy option in advanced-stage cutaneous lymphoma (context: Sézary syndrome, not B-cell) |
| [31511903](https://pubmed.ncbi.nlm.nih.gov/31511903/) | 2019 | Review | Der Hautarzt | Same authors/topic; bexarotene listed among systemic therapies for advanced cutaneous T-cell disease |
| [14616487](https://pubmed.ncbi.nlm.nih.gov/14616487/) | 2003 | Review | Australasian Journal of Dermatology | Management strategies across primary cutaneous lymphomas (T- and B-cell subtypes), including retinoids |
| [20806174](https://pubmed.ncbi.nlm.nih.gov/20806174/) | 2010 | Review | Therapeutische Umschau | WHO/EORTC classification and general management of cutaneous T- and B-cell lymphomas |
| [29881891](https://pubmed.ncbi.nlm.nih.gov/29881891/) | 2018 | Case Series | Der Hautarzt | 163-patient case series of primary cutaneous lymphoma from routine clinical practice |
| [19786826](https://pubmed.ncbi.nlm.nih.gov/19786826/) | 2009 | Review | Skin Pharmacology and Physiology | New/experimental skin-directed therapies for cutaneous lymphomas (T- and B-cell) |
| [23941646](https://pubmed.ncbi.nlm.nih.gov/23941646/) | 2013 | Case Report | Journal of Cutaneous Pathology | Diagnostic pitfalls distinguishing a rare T-cell lymphoma subtype from B-cell lymphoma |
| [22508770](https://pubmed.ncbi.nlm.nih.gov/22508770/) | 2012 | Case Series | Archives of Dermatology | 5-case series describing a T-cell lymphoma subtype with B-cell-mimicking features |

None of the above literature reports direct clinical outcomes of bexarotene treatment in primary cutaneous B-cell lymphoma patients.

---

## Norway Market Information

Bexarotene currently holds **no marketing authorization in Norway** (`market_status: 未上市`, 0 licenses on file). No product-level dosage form or approved-indication data is available to report.

---

## Cytotoxicity

Bexarotene is included here because its established/inferred original use is an oncologic indication (cutaneous T-cell lymphoma).

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (RXR-selective retinoid; not a conventional cytotoxic agent) |
| Myelosuppression Risk | Low–Medium — neutropenia has been reported with bexarotene capsules (per supporting literature, e.g., PMID 24099070) |
| Emetogenicity Classification | Low |
| Monitoring Items | Fasting lipid panel (hypertriglyceridemia is a common, sometimes severe adverse effect), thyroid function (central hypothyroidism), CBC (neutropenia), liver function |
| Handling Protection | Not classified as a conventional cytotoxic chemotherapy agent; standard oncology-drug handling precautions apply, with additional caution for teratogenicity typical of retinoids |

---

## Safety Considerations

Please refer to the package insert for safety information. Structured safety data (key warnings, contraindications, drug interactions) were not available in this Evidence Pack — TFDA label warnings/contraindications are flagged as a **Blocking** data gap (DG001), which currently prevents completion of the S1 safety initial assessment.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The predicted indication (primary cutaneous B-cell lymphoma) lacks direct clinical trial or literature evidence — available trials and publications address cutaneous lymphoma broadly or CTCL/Sézary syndrome specifically, not bexarotene efficacy in B-cell disease. Combined with a Blocking-severity gap in TFDA safety/label data and the drug's non-marketed status in Norway, the evidence base is insufficient to proceed.

**To proceed, the following is needed:**
- TFDA package insert data (warnings, contraindications) to complete the S1 safety assessment (Blocking gap, DG001)
- Confirmed mechanism of action detail to support the B-cell mechanistic rationale (DG002)
- Dedicated preclinical or early-phase clinical evidence evaluating bexarotene specifically in primary cutaneous B-cell lymphoma (current evidence is indirect, drawn from the general cutaneous-lymphoma literature)
- Clarification of Norway/regional regulatory pathway, given the drug currently holds no marketing authorization
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

