---
layout: default
title: Eribulin
parent: 僅模型預測 (L5)
nav_order: 140
evidence_level: L5
indication_count: 10
---

# Eribulin
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

# Eribulin: From Liposarcoma to Fibroblastic Neoplasm (Solitary Fibrous Tumor)

## One-Sentence Summary

> Eribulin is a microtubule inhibitor chemotherapy agent, with FDA-approved use in unresectable liposarcoma referenced in the underlying evidence.
> The TxGNN model generated 10 candidate indications for this drug; among them, **Fibroblastic Neoplasm (Solitary Fibrous Tumor)** stands out as the only candidate backed by a **completed Phase II clinical trial** and **multiple supporting publications**, while 7 of the other 9 candidates (including the model's #1-ranked prediction, "familial Mediterranean fever") have zero clinical or literature support and are flagged by the evidence pack itself as likely model noise.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Unresectable liposarcoma (soft tissue sarcoma) — noted in evidence pack rationale; no formal indication list was returned for this drug |
| Predicted New Indication | Fibroblastic Neoplasm (Solitary Fibrous Tumor) |
| TxGNN Prediction Score | 99.36% |
| Evidence Level | L3 (one completed, single-arm Phase II trial specific to this indication + supportive preclinical literature; not yet a randomized Phase 2/3 trial, so short of L2) |
| Norway Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Proceed with Guardrails |

**Note on selection:** This report evaluates the *best-evidenced* candidate from the 10 TxGNN predictions supplied, not the top-ranked one. The #1 ranked prediction ("autosomal recessive familial Mediterranean fever," score 99.82%) has no clinical or literature evidence at all, and its own mechanistic rationale explicitly states it is "very likely TxGNN model noise/false positive." Fibroblastic neoplasm (model rank 8, score 99.36%) is the only candidate with a dedicated completed trial.

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism-of-action data for eribulin is not available in this evidence pack (flagged as a High-severity data gap, DG002). Based on the information that is available, eribulin is a microtubule dynamics inhibitor (halichondrin B analog class) used as cytotoxic chemotherapy, with an established, FDA-approved role in unresectable liposarcoma — a soft-tissue sarcoma.

Fibroblastic neoplasms, and specifically Solitary Fibrous Tumor (SFT), belong to the same broad soft-tissue sarcoma family as liposarcoma. Multiple preclinical studies in the evidence pack demonstrate eribulin activity and resistance mechanisms specifically in fibrosarcoma cell lines (e.g., HT1080), and a patient-derived xenograft (PDX) study (PMID 28284173) explicitly identified eribulin and trabectedin as effective candidates against SFT — a finding that appears to have directly motivated the dedicated ERASING Phase II trial (NCT03840772).

This gives fibroblastic neoplasm/SFT a stronger and more mechanistically coherent rationale than most of the other 9 TxGNN predictions in this pack, most of which (mesothelioma subtypes, pleural adenomatoid tumor, familial Mediterranean fever) have no clinical trials, no literature, and mechanistic rationales that acknowledge the connection is speculative.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT03840772](https://clinicaltrials.gov/study/NCT03840772) | Phase 2 | Completed | 16 | ERASING trial (Italian Sarcoma Group): single-arm Phase II study of eribulin in advanced Solitary Fibrous Tumor |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [28284173](https://pubmed.ncbi.nlm.nih.gov/28284173/) | 2017 | Preclinical (PDX) | European Journal of Cancer | Patient-derived SFT xenografts show high sensitivity to doxorubicin/dacarbazine; also highlight eribulin and trabectedin as effective candidates — basis for later clinical testing |
| [38136399](https://pubmed.ncbi.nlm.nih.gov/38136399/) | 2023 | Review | Cancers | Overview of diagnosis and treatment of extrameningeal Solitary Fibrous Tumor |
| [40295012](https://pubmed.ncbi.nlm.nih.gov/40295012/) | 2025 | Preclinical (in vivo) | In Vivo | Eribulin-resistant HT1080 fibrosarcoma cells become more malignant; combination with methionine restriction overcomes resistance in mouse models |
| [39197933](https://pubmed.ncbi.nlm.nih.gov/39197933/) | 2024 | Preclinical (in vitro) | Anticancer Research | Recombinant methioninase increases eribulin efficacy 16-fold in eribulin-resistant HT1080 fibrosarcoma cells |
| [38423656](https://pubmed.ncbi.nlm.nih.gov/38423656/) | 2024 | Preclinical (in vitro) | Anticancer Research | Strong synergy between recombinant methioninase and eribulin against fibrosarcoma cells, sparing normal fibroblasts |

---

## Norway Market Information

No marketing authorization records were found for Eribulin in Norway (0 authorizations; market status: not marketed).

---

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Conventional cytotoxic (microtubule inhibitor, halichondrin B analog class) |
| Myelosuppression Risk | Please refer to the package insert warnings and precautions |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | Please refer to the package insert warnings and precautions |
| Handling Protection | Standard cytotoxic drug handling precautions apply, consistent with other antineoplastic chemotherapy agents |

---

## Safety Considerations

Please refer to the package insert for safety information. Note: retrieval of TFDA-equivalent label warnings and contraindications for this drug is currently a **blocking data gap (DG001)** — this must be resolved before any clinical safety assessment (S1 stage) can proceed.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Fibroblastic neoplasm/Solitary Fibrous Tumor is supported by a completed, dedicated Phase II trial (ERASING, n=16) and consistent preclinical mechanistic evidence, making it the only credible candidate among the 10 TxGNN predictions supplied. However, the trial is small and single-arm (not randomized), and drug-level safety/label data is entirely missing, so this cannot yet support a full "Go" decision.

**To proceed, the following is needed:**
- Resolve blocking data gap DG001: obtain package insert warnings, contraindications, and DDI data
- Resolve data gap DG002: obtain formal mechanism-of-action data from DrugBank
- Seek confirmatory or larger-cohort data beyond the 16-patient ERASING trial before considering formal repurposing
- Deprioritize (Hold) the 7 low-evidence TxGNN candidates in this pack (mesothelioma subtypes, pleural adenomatoid tumor, familial Mediterranean fever) unless new clinical or literature evidence emerges
- Continue monitoring dermatofibrosarcoma protuberans and ovarian myxoid liposarcoma as secondary "Research Question" leads (currently L4, mechanism-only support)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

