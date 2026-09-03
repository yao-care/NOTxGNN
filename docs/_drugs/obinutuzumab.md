---
layout: default
title: Obinutuzumab
parent: 僅模型預測 (L5)
nav_order: 249
evidence_level: L5
indication_count: 3
---

# Obinutuzumab
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

# Obinutuzumab: From Chronic Lymphocytic Leukemia to Follicular Lymphoma

## One-Sentence Summary

> Obinutuzumab is a glycoengineered anti-CD20 monoclonal antibody originally established for chronic lymphocytic leukemia (CLL) treatment.
> The TxGNN model predicts it is effective for **Follicular Lymphoma**,
> a finding already substantiated by **10+ clinical trials (including 2 completed Phase 3 RCTs)** and **10+ publications**, indicating this signal largely reflects an already-established indication rather than a purely novel repurposing hypothesis.
> Note: this evidence pack also flags two additional CLL/SLL molecular-subtype predictions (pregerminal-center and IGHV-hypermutated) with comparably high model scores (~99.2%) but **zero** supporting trials or literature — these remain in Hold status and are not further developed below.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not on record in Norway market data (drug not marketed). Per clinical trial documentation (NCT02877550), obinutuzumab was originally approved for chronic lymphocytic leukemia (CLL) in combination with chlorambucil |
| Predicted New Indication | Follicular Lymphoma |
| TxGNN Prediction Score | 99.18% |
| Evidence Level | L1 |
| Norway Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available (flagged as a High-severity data gap in this evidence pack). Based on known clinical trial documentation, Obinutuzumab is a fully humanized, glycoengineered Type II anti-CD20 monoclonal antibody; its efficacy in CD20-positive B-cell malignancies such as CLL has been established, and mechanistically it is broadly applicable to other CD20-expressing B-cell cancers, including follicular lymphoma.

Obinutuzumab works by enhancing antibody-dependent cellular cytotoxicity (ADCC), antibody-dependent cellular phagocytosis (ADCP), and direct B-cell killing of CD20-positive malignant cells — a mechanism shared across the B-cell lymphoma/leukemia disease family. Follicular lymphoma is a CD20-positive indolent B-cell lymphoma, so the mechanistic overlap with the drug's established CLL activity is strong. This is reinforced by the large, completed Phase 3 GALLIUM trial (NCT01332968, n=1,401), which demonstrated that obinutuzumab-based immunochemotherapy significantly prolonged progression-free survival compared with rituximab-based immunochemotherapy in previously untreated advanced follicular lymphoma — meaning this indication functions more as an **already-validated use** than a speculative new signal, and the TxGNN prediction here largely serves as model face-validation.

The `original_indications` field being empty in the source database is most likely a data-registration gap rather than evidence that the drug has no approved uses; obinutuzumab is a well-characterized, globally marketed biologic. By contrast, the two co-ranked CLL/SLL molecular-subtype predictions in this evidence pack (pregerminal-center IGHV-unmutated and IGHV-hypermutated subtypes) have no corresponding trials or literature at all, so their mechanistic plausibility (broad anti-CD20 activity in CLL/SLL) cannot currently be verified against real-world evidence and they remain purely model-driven (L5, Hold).

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT01332968](https://clinicaltrials.gov/study/NCT01332968) | Phase 3 | Completed | 1401 | GALLIUM: obinutuzumab + chemotherapy vs. rituximab + chemotherapy followed by maintenance in untreated advanced indolent NHL; established obinutuzumab superiority in PFS |
| [NCT01059630](https://clinicaltrials.gov/study/NCT01059630) | Phase 3 | Completed | 413 | Bendamustine alone vs. bendamustine + obinutuzumab (GA101) in rituximab-refractory indolent NHL |
| [NCT03332017](https://clinicaltrials.gov/study/NCT03332017) | Phase 2 | Completed | 217 | ROSEWOOD: zanubrutinib + obinutuzumab vs. obinutuzumab monotherapy in relapsed/refractory follicular lymphoma |
| [NCT03817853](https://clinicaltrials.gov/study/NCT03817853) | Phase 4 | Completed | 114 | Safety of obinutuzumab short-duration (90-minute) infusion combined with chemotherapy in previously untreated advanced FL |
| [NCT01582776](https://clinicaltrials.gov/study/NCT01582776) | Phase 1/2 | Completed | 317 | GALEN: obinutuzumab + lenalidomide in follicular and relapsed/refractory aggressive (DLBCL/MCL) B-cell lymphoma |
| [NCT04034056](https://clinicaltrials.gov/study/NCT04034056) | N/A (non-interventional) | Completed | 299 | Real-world effectiveness and safety of obinutuzumab in previously untreated advanced follicular lymphoma |
| [NCT02611323](https://clinicaltrials.gov/study/NCT02611323) | Phase 1/2 | Completed | 133 | Obinutuzumab + polatuzumab vedotin + venetoclax in relapsed/refractory follicular lymphoma |
| [NCT02600897](https://clinicaltrials.gov/study/NCT02600897) | Phase 1/2 | Completed | 114 | Obinutuzumab + polatuzumab vedotin + lenalidomide in relapsed/refractory follicular lymphoma |
| [NCT03113422](https://clinicaltrials.gov/study/NCT03113422) | Phase 2 | Completed | 56 | Venetoclax + obinutuzumab + bendamustine as front-line therapy in high tumor-burden follicular lymphoma |
| [NCT03341520](https://clinicaltrials.gov/study/NCT03341520) | Phase 2 | Completed | 89 | GAZAI: obinutuzumab + low-dose involved-site radiotherapy in early-stage nodal follicular lymphoma |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [28976863](https://pubmed.ncbi.nlm.nih.gov/28976863/) | 2017 | RCT | NEJM | Primary GALLIUM report: obinutuzumab-based chemoimmunotherapy vs. rituximab-based in untreated advanced FL |
| [29856692](https://pubmed.ncbi.nlm.nih.gov/29856692/) | 2018 | RCT | J Clin Oncol | GALLIUM sub-analysis: influence of chemotherapy backbone on obinutuzumab efficacy and safety |
| [37506346](https://pubmed.ncbi.nlm.nih.gov/37506346/) | 2023 | RCT | J Clin Oncol | ROSEWOOD Phase 2: zanubrutinib + obinutuzumab vs. obinutuzumab monotherapy in relapsed/refractory FL |
| [31296423](https://pubmed.ncbi.nlm.nih.gov/31296423/) | 2019 | RCT | Lancet Haematol | GALEN: obinutuzumab + lenalidomide in relapsed/refractory follicular B-cell lymphoma |
| [37767550](https://pubmed.ncbi.nlm.nih.gov/37767550/) | 2024 | RCT | Haematologica | Polatuzumab vedotin + bendamustine/rituximab or obinutuzumab in relapsed/refractory FL (Phase Ib/II) |
| [31360086](https://pubmed.ncbi.nlm.nih.gov/31360086/) | 2017 | Review | Blood Lymphat Cancer | Impact of obinutuzumab alone and in combination for follicular lymphoma |
| [38660754](https://pubmed.ncbi.nlm.nih.gov/38660754/) | 2024 | Review | Turk J Haematol | Comprehensive review of FL management, including obinutuzumab-based regimens |
| [39830356](https://pubmed.ncbi.nlm.nih.gov/39830356/) | 2024 | Review | Front Pharmacol | Rapid review of efficacy, safety, and cost-effectiveness of obinutuzumab in FL |
| [28276536](https://pubmed.ncbi.nlm.nih.gov/28276536/) | 2016 | Review | Drugs Today | Overview of obinutuzumab's role in follicular lymphoma |
| [35180337](https://pubmed.ncbi.nlm.nih.gov/35180337/) | 2022 | Review | Oncology | Follicular lymphoma: current and emerging therapies, including anti-CD20 antibodies |

---

## Norway Market Information

Currently no Norway market authorization on record. `taiwan_regulatory.market_status` for this candidate is reported as **未上市 (Not Marketed)**, with 0 registered authorizations and no license entries available for extraction.

---

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy / Immunotherapy — anti-CD20 monoclonal antibody (glycoengineered Type II); not a conventional cytotoxic chemotherapeutic |
| Myelosuppression Risk | Not established in this dataset — please refer to the package insert warnings and precautions |
| Emetogenicity Classification | Not established in this dataset — please refer to the package insert warnings and precautions |
| Monitoring Items | Please refer to the package insert warnings and precautions |
| Handling Protection | Please refer to the package insert warnings and precautions; as a monoclonal antibody biologic, it is not typically subject to conventional cytotoxic drug handling protocols, but this cannot be confirmed without label data |

---

## Safety Considerations

Please refer to the package insert for safety information. (Key warnings, contraindications, and drug interaction data are all currently unavailable for this candidate — flagged as a Blocking-severity data gap pending TFDA/local package insert acquisition.)

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
- The follicular lymphoma signal is backed by two completed Phase 3 RCTs (including the pivotal GALLIUM trial) and a broad base of Phase 1/2 combination-therapy data, meeting L1 evidence criteria — this is a well-established, not speculative, use of obinutuzumab. However, the absence of local (Norway) market authorization and package insert safety data prevents a full "Go" determination.

**To proceed, the following is needed:**
- TFDA/local package insert data (key warnings, contraindications) — currently a Blocking-severity gap
- Confirmed mechanism of action documentation from DrugBank or equivalent source
- Clarification on Norway market/registration status, given the drug's established use elsewhere
- Reconciliation of the `original_indications` field gap in the source database against known approved uses (e.g., CLL)
- Continued monitoring for emerging trial/literature evidence on the two CLL/SLL molecular-subtype predictions (pregerminal-center and IGHV-hypermutated), both currently Hold/L5 with no supporting data
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

