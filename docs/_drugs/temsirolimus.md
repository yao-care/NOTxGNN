---
layout: default
title: Temsirolimus
parent: 僅模型預測 (L5)
nav_order: 346
evidence_level: L5
indication_count: 3
---

# Temsirolimus
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

# Temsirolimus: From mTOR-Targeted Oncology Therapy to Liposarcoma

## One-Sentence Summary

Temsirolimus is an mTOR inhibitor (a prodrug of sirolimus) used in oncology; its specific original approved indication is not recorded in this evidence pack.
The TxGNN model predicts it may be effective for **Liposarcoma**,
with **5 clinical trials** (2 using temsirolimus directly, Grade A) and **1 publication** currently supporting this direction.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available in evidence pack (no approved indication text on file; drug not marketed in Norway) |
| Predicted New Indication | Liposarcoma |
| TxGNN Prediction Score | 99.54% |
| Evidence Level | L3 |
| Norway Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data for temsirolimus is not available in this evidence pack. Based on the drug repurposing rationale provided, temsirolimus is an mTOR inhibitor (prodrug of sirolimus) that blocks the PI3K/AKT/mTOR signaling pathway. This pathway is a well-established target in oncology, and the evidence pack notes it is frequently dysregulated in dedifferentiated and myxoid liposarcoma subtypes (e.g., through CDK4/MDM2 amplification-driven downstream signaling or PTEN loss).

The relationship between temsirolimus's original use and liposarcoma is mechanistic rather than indication-based, since no original approved indication is recorded here. However, two of the five identified clinical trials used temsirolimus itself (brand name Torisel) directly in sarcoma populations — one in combination with liposomal doxorubicin, and one in pediatric recurrent/refractory sarcoma with cixutumumab — both rated Grade A relevance by the evidence pipeline.

The remaining three trials use related mTOR pathway inhibitors (sirolimus, ridaforolimus, everolimus) rather than temsirolimus itself, providing class-level rather than drug-specific support. Historically, single-agent mTOR inhibition has shown only limited, non-definitive efficacy in liposarcoma trials, suggesting that combination regimens (with cytotoxic chemotherapy or IGF-1R inhibitors) are more likely to be clinically meaningful than monotherapy.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00949325](https://clinicaltrials.gov/study/NCT00949325) | Phase 1/2 | Completed | 24 | Torisel (temsirolimus) + liposomal doxorubicin in recurrent soft tissue/bone sarcoma; dose-finding and efficacy assessment. Direct drug evidence. |
| [NCT01614795](https://clinicaltrials.gov/study/NCT01614795) | Phase 2 | Completed | 46 | Temsirolimus + cixutumumab (IMC-A12) in pediatric recurrent/refractory sarcoma. Direct drug evidence. |
| [NCT02821507](https://clinicaltrials.gov/study/NCT02821507) | Phase 2 | Completed | 70 | Sirolimus + cyclophosphamide in metastatic/unresectable myxoid liposarcoma and chondrosarcoma. Class-effect (sirolimus, not temsirolimus). |
| [NCT00093080](https://clinicaltrials.gov/study/NCT00093080) | Phase 2 | Completed | 216 | Ridaforolimus (AP23573), an mTOR inhibitor, in advanced sarcoma. Class-effect evidence, largest cohort. |
| [NCT03114527](https://clinicaltrials.gov/study/NCT03114527) | Phase 2 | Active, not recruiting | 48 | Ribociclib + everolimus in advanced dedifferentiated liposarcoma and leiomyosarcoma. Class-effect (everolimus, not temsirolimus). |

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [20497911](https://pubmed.ncbi.nlm.nih.gov/20497911/) | 2010 | Review | Bulletin du cancer | Review of targeted treatments for rare connective tissue tumors and sarcomas, covering molecular subtyping and pathway-directed therapy approaches. |

## Norway Market Information

Temsirolimus currently holds no marketing authorization in Norway (0 authorizations on file); no product or dosage form data is available.

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (mTOR inhibitor) |
| Myelosuppression Risk | Please refer to the package insert warnings and precautions |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | Please refer to the package insert warnings and precautions |
| Handling Protection | Please refer to the package insert warnings and precautions |

## Safety Considerations

Please refer to the package insert for safety information. Note: TFDA-equivalent labeling data (warnings/contraindications) for this drug is currently a **blocking data gap**, which prevents completion of the standard S1 safety pre-assessment.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
While two trials use temsirolimus directly in sarcoma populations (Grade A relevance) and the mTOR pathway has a plausible mechanistic role in liposarcoma, the evidence is limited to Phase 1/2 studies with no confirmatory Phase 3 data, and the drug is not marketed in Norway. Critically, the missing TFDA-equivalent labeling data is a blocking gap that prevents a safety pre-assessment (S1), so the candidate cannot yet advance to Go or Proceed with Guardrails.

**To proceed, the following is needed:**
- TFDA (or equivalent) label warnings/contraindications, to unblock the S1 safety assessment (DG001)
- Confirmed mechanism-of-action and DrugBank category/toxicity data (DG002)
- Original approved indication(s) for temsirolimus, to properly frame the repurposing rationale
- Additional liposarcoma-specific trial data, ideally combination-regimen Phase 2/3 results, given monotherapy's historically limited efficacy in this tumor type
- Route-of-administration compatibility assessment (currently pending)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

