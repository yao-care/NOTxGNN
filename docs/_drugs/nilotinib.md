---
layout: default
title: Nilotinib
parent: 僅模型預測 (L5)
nav_order: 50
evidence_level: L5
indication_count: 1
---

# Nilotinib
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

Using the evidence pack provided, here is the drug repurposing evaluation report.

---

# Nilotinib: From Chronic Myeloid Leukemia to Dermatofibrosarcoma Protuberans

## One-Sentence Summary

Nilotinib is a second-generation tyrosine kinase inhibitor originally developed for Philadelphia chromosome-positive chronic myeloid leukemia (Ph+ CML). The TxGNN model predicts it may be effective for **Dermatofibrosarcoma Protuberans (DFSP)**, but this direction is currently supported by only **0 clinical trials** and **1 publication**, meaning the evidence base is mechanistic rather than clinical at this stage.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Chronic Myeloid Leukemia (Ph+ CML)† |
| Predicted New Indication | Dermatofibrosarcoma Protuberans |
| TxGNN Prediction Score | 99.31% |
| Evidence Level | L4 |
| Norway Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

† Not present in the evidence pack's `original_indications`/`original_moa` fields (flagged as a data gap, DG002). This is based on generally known information about nilotinib rather than the supplied evidence pack.

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the evidence pack (data gap DG002). Based on generally known information, nilotinib is a second-generation BCR-ABL tyrosine kinase inhibitor (TKI) whose efficacy in Ph+ chronic myeloid leukemia is well established; it also has recognized off-target inhibitory activity against PDGFR-α/β and KIT.

Dermatofibrosarcoma protuberans (DFSP) is a soft-tissue sarcoma characteristically driven by a COL1A1-PDGFB gene fusion, which causes constitutive activation of the PDGFR-β signaling pathway. Imatinib, a first-generation TKI in the same pharmacological class as nilotinib, is already an established treatment for unresectable or metastatic DFSP precisely because of its anti-PDGFR activity. This creates a plausible mechanistic bridge between nilotinib's known target profile and DFSP biology.

The single retrieved literature item (PMID 29408302) reviews the broader role of small-molecule PDGFR inhibitors — as a class — in neoplastic disease, which is consistent with this rationale but does not provide nilotinib-specific or DFSP-specific clinical outcome data. The prediction should therefore be regarded as mechanistically plausible but not yet clinically validated.

## Clinical Trial Evidence

Currently no related clinical trials registered

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [29408302](https://pubmed.ncbi.nlm.nih.gov/29408302/) | 2018 | Review | Pharmacological Research | Reviews the role of small-molecule PDGFR inhibitors (a class that includes nilotinib) in treating neoplastic disorders; supports a mechanistic, but not DFSP-specific, rationale for PDGFR-driven tumors |

## Norway Market Information

Nilotinib is currently not marketed in Norway — no marketing authorizations are recorded in the evidence pack.

## Cytotoxicity

Nilotinib is an antineoplastic agent (original indication is a hematologic malignancy, CML), so this section applies.

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (BCR-ABL/PDGFR/KIT tyrosine kinase inhibitor) |
| Myelosuppression Risk | Please refer to the package insert warnings and precautions |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | Please refer to the package insert warnings and precautions |
| Handling Protection | Please refer to the package insert warnings and precautions |

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- The TxGNN score is high, but the underlying evidence base is limited to a single mechanism-class review article with no DFSP-specific or nilotinib-specific clinical data, and zero registered clinical trials — placing this at Evidence Level L4 (mechanism-only).
- Critical safety information (TFDA/product label warnings and contraindications) is marked as a **Blocking** data gap (DG001), which by definition prevents this candidate from entering the S1 safety preliminary evaluation stage.

**To proceed, the following is needed:**
- TFDA package insert data (warnings, contraindications) — currently blocking, must be resolved first
- Confirmed mechanism of action (MOA) detail from DrugBank (data gap DG002)
- Disease-specific evidence for nilotinib in DFSP, particularly in imatinib-resistant or PDGFB-rearranged cases
- Drug-drug interaction (DDI) profile, currently unresolved (`not_found`)
- Confirmation of Norway marketing/import pathway, given the drug is not currently marketed
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

