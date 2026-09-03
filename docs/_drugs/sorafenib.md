---
layout: default
title: Sorafenib
parent: 僅模型預測 (L5)
nav_order: 330
evidence_level: L5
indication_count: 10
---

# Sorafenib
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

# Sorafenib: From Renal Cell/Hepatocellular Carcinoma to Liposarcoma

## One-Sentence Summary

Sorafenib is a multi-targeted kinase inhibitor originally established for renal cell carcinoma and hepatocellular carcinoma. The TxGNN model predicts it may also be effective for **Liposarcoma**, with **2 clinical trials** and **8 publications** currently supporting this direction.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the Norway licensing database (sorafenib is currently not marketed there); evidence within this pack (clinical trial and literature text) identifies its established indications as hepatocellular carcinoma and renal cell carcinoma |
| Predicted New Indication | Liposarcoma |
| TxGNN Prediction Score | 99.82% |
| Evidence Level | L2 |
| Norway Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Proceed with Guardrails |

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data from DrugBank is not available for this drug (data gap). Based on descriptions embedded in the clinical trial evidence within this pack, sorafenib is a multi-targeted kinase inhibitor that blocks RAF/MEK/ERK signal transduction and inhibits VEGFR-1/2/3 and PDGFR-mediated angiogenesis ("Sorafenib may stop the growth of tumor cells by blocking some of the enzymes needed for cell growth and by blocking blood flow to the tumor" — NCT00217620). This dual anti-proliferative/anti-angiogenic mechanism underlies its established use in renal cell carcinoma and hepatocellular carcinoma, both of which are highly vascularized, angiogenesis-dependent tumors.

Soft tissue sarcomas, including liposarcoma, similarly show frequent PDGFR pathway activation and tumor vascular dependence, providing a plausible mechanistic bridge. Dedifferentiated liposarcoma additionally shows PTEN down-regulation, which may interact with RAF/AKT signaling (PMID 23416162). This mechanistic overlap is reflected in the completed Phase 2 SWOG trial (S0505) that directly tested sorafenib in advanced soft tissue sarcoma populations including liposarcoma subtypes.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00217620](https://clinicaltrials.gov/study/NCT00217620) | Phase 2 | Completed | 51 | Sorafenib (BAY 43-9006) tested in advanced soft tissue sarcomas including liposarcoma subtypes; direct drug-disease evidence |
| [NCT02048371](https://clinicaltrials.gov/study/NCT02048371) | Phase 2 | Completed | 131 | SARC024 blanket protocol on oral regorafenib (structurally related, not sorafenib) in selected sarcoma subtypes — indirect supportive precedent only |

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [21751200](https://pubmed.ncbi.nlm.nih.gov/21751200/) | 2012 | Phase 2 trial (SWOG S0505) | Cancer | Sorafenib tested in advanced soft tissue sarcoma patients with limited therapeutic options; a multitargeted kinase inhibitor of RAF, VEGFR1-3, PDGFR-β, and c-kit |
| [24554062](https://pubmed.ncbi.nlm.nih.gov/24554062/) | 2014 | Phase 1 trial | Annals of Surgical Oncology | Neoadjuvant sorafenib + conformal radiotherapy in extremity soft tissue sarcoma; synergy hypothesis with antiangiogenic therapy |
| [22987955](https://pubmed.ncbi.nlm.nih.gov/22987955/) | 2012 | Review | Annals of Oncology | Histology-driven medical therapy in soft tissue sarcomas, including liposarcoma-specific agent activity |
| [24712007](https://pubmed.ncbi.nlm.nih.gov/24712007/) | 2014 | Review | Magyar Onkologia | Histological subtype-based medical treatment approach for soft tissue sarcomas |
| [36003796](https://pubmed.ncbi.nlm.nih.gov/36003796/) | 2022 | Review | Frontiers in Oncology | PDOX models identify effective combination therapies (CDK inhibitor palbociclib) for sarcoma |
| [18413802](https://pubmed.ncbi.nlm.nih.gov/18413802/) | 2008 | Preclinical | Molecular Cancer Therapeutics | Sorafenib inhibits growth/MAPK signaling in malignant peripheral nerve sheath and dedifferentiated liposarcoma cell lines |
| [23416162](https://pubmed.ncbi.nlm.nih.gov/23416162/) | 2013 | Preclinical (xenograft) | American Journal of Pathology | Dedifferentiated liposarcoma xenograft models reveal PTEN down-regulation as a malignant signature, relevant to PI3K/RAF pathway inhibition |
| [25075796](https://pubmed.ncbi.nlm.nih.gov/25075796/) | 2014 | Case report | Anti-Cancer Drugs | Response to trabectedin (different drug) in advanced synovial sarcoma — indirect sarcoma-class precedent only |

## Norway Market Information

Sorafenib is currently **not marketed in Norway** — no active authorizations are on record in the regulatory database (0 licenses).

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (multi-kinase inhibitor targeting RAF/VEGFR/PDGFR), not conventional cytotoxic chemotherapy |
| Myelosuppression Risk | Please refer to the package insert warnings and precautions |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | Please refer to the package insert warnings and precautions |
| Handling Protection | Please refer to the package insert warnings and precautions |

## Safety Considerations

Please refer to the package insert for safety information. Note: TFDA/regulatory-agency-level warning and contraindication data for this drug is flagged as a **blocking data gap** (DG001) — this must be resolved before a formal S1 safety assessment can proceed.

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
A completed Phase 2 trial (SWOG S0505) and multiple mechanistically consistent preclinical studies support biological plausibility of sorafenib in soft tissue sarcoma/liposarcoma, but no liposarcoma-subtype-specific confirmatory trial exists, and formal safety-label data is currently unavailable.

**To proceed, the following is needed:**
- TFDA/Norway package insert warnings and contraindications (DG001, blocking — required before S1 safety evaluation)
- Formal DrugBank-sourced mechanism of action documentation (DG002)
- Liposarcoma-subtype-specific trial data or subgroup analysis from existing sarcoma trials
- A defined safety monitoring plan given the drug's antiangiogenic/kinase-inhibitor toxicity profile
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

