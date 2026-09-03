---
layout: default
title: Ofatumumab
parent: 僅模型預測 (L5)
nav_order: 251
evidence_level: L5
indication_count: 8
---

# Ofatumumab
{: .fs-9 }

證據等級: **L5** | 預測適應症: **8** 個
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

# Ofatumumab: From Chronic Lymphocytic Leukemia to Follicular Lymphoma

## One-Sentence Summary

Ofatumumab is a fully human anti-CD20 monoclonal antibody whose efficacy is well established in chronic lymphocytic leukemia/small lymphocytic lymphoma (CLL/SLL), though the drug is **not currently marketed in Taiwan**. The TxGNN model predicts it may also be effective for **Follicular Lymphoma**, a related CD20-positive B-cell malignancy, with **15 clinical trials** and **20 publications** currently supporting this direction.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Chronic Lymphocytic Leukemia/Small Lymphocytic Lymphoma (CLL/SLL) — internationally established anti-CD20 indication; not yet approved in Taiwan |
| Predicted New Indication | Follicular Lymphoma |
| TxGNN Prediction Score | 99.70% |
| Evidence Level | L2 |
| Taiwan Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this evidence pack. Based on known information from the collected literature, ofatumumab is a fully human IgG1κ monoclonal antibody that binds a distinct small-loop epitope on the CD20 antigen, distinct from rituximab's binding site. It eliminates CD20-positive B cells primarily via complement-dependent cytotoxicity (CDC) and antibody-dependent cellular cytotoxicity (ADCC). This mechanism has been proven effective in CLL/SLL, where it is the drug's core, globally recognized indication.

Follicular lymphoma (FL) is, like CLL/SLL, a CD20-positive B-cell malignancy, meaning the same target antigen is expressed on the malignant cell population. This shared molecular target provides a direct mechanistic rationale for extending ofatumumab's use from CLL/SLL to FL — the same rationale that has already supported rituximab's dual approval across both diseases.

The strength of this prediction is reinforced by an unusually large clinical trial footprint: ofatumumab has been studied as monotherapy, in combination with CHOP, bendamustine, and bortezomib, and in radiotherapy-combination settings, across newly diagnosed, relapsed, and rituximab-refractory FL populations. While no Phase 3 confirmatory trial specific to FL exists yet, the depth of completed Phase 2 evidence (including a randomized Phase 2 trial) is substantial.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT01294579](https://clinicaltrials.gov/study/NCT01294579) | Phase 2 | Completed | 49 | Ofatumumab + bendamustine followed by ofatumumab maintenance in indolent B-NHL relapsed after rituximab therapy |
| [NCT01286272](https://clinicaltrials.gov/study/NCT01286272) | Phase 2 (Randomized) | Completed | 135 | Head-to-head: ofatumumab + bendamustine vs. ofatumumab + bendamustine + bortezomib in untreated FL |
| [NCT00394836](https://clinicaltrials.gov/study/NCT00394836) | Phase 2 | Completed | 116 | International multicenter single-arm trial of ofatumumab monotherapy in rituximab-refractory FL |
| [NCT00494780](https://clinicaltrials.gov/study/NCT00494780) | Phase 2 | Completed | 59 | Two-dose regimens of ofatumumab + CHOP in previously untreated FL |
| [NCT01239394](https://clinicaltrials.gov/study/NCT01239394) | Phase 2 | Completed | 43 | Ofatumumab as initial systemic treatment for indolent B-cell lymphoma |
| [NCT01190449](https://clinicaltrials.gov/study/NCT01190449) | Phase 2 | Completed | 51 | Ofatumumab monotherapy in previously untreated stage II–IV follicular NHL (CALGB) |
| [NCT00742144](https://clinicaltrials.gov/study/NCT00742144) | Phase 1 | Completed | 6 | Japanese patients with CD20+ FL or CLL; PK/safety/tolerability profile |
| [NCT02710643](https://clinicaltrials.gov/study/NCT02710643) | Phase 2 | Completed | 110 | MIRO trial: involved-field radiotherapy ± ofatumumab in stage I/II FL, Bcl-2-guided follow-up |
| [NCT01263418](https://clinicaltrials.gov/study/NCT01263418) | Phase 2 | Withdrawn | 0 | Planned safety study in older patients with indolent NHL (FL/MZL); withdrawn before enrollment |
| [NCT01397591](https://clinicaltrials.gov/study/NCT01397591) | Phase 2 | Terminated | 3 | Ofatumumab + bortezomib in relapsed CD20+ DLBCL/FL/MCL; terminated early, underpowered |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [31174236](https://pubmed.ncbi.nlm.nih.gov/31174236/) | 2019 | RCT | Cancer | CALGB 50904: randomized comparison of ofatumumab+bendamustine ± bortezomib in previously untreated high-risk FL |
| [22389254](https://pubmed.ncbi.nlm.nih.gov/22389254/) | 2012 | Multicenter Study | Blood | Ofatumumab monotherapy in rituximab-refractory FL (n=116); ORR 13% |
| [30723894](https://pubmed.ncbi.nlm.nih.gov/30723894/) | 2019 | Phase 2 Multicentre Trial | British Journal of Haematology | CALGB 50901: single-agent ofatumumab in untreated, low/intermediate-risk advanced-stage FL |
| [38937025](https://pubmed.ncbi.nlm.nih.gov/38937025/) | 2024 | MRD-Driven Clinical Study | The Lancet Haematology | FIL MIRO trial final results: local radiotherapy ± ofatumumab in early-stage FL |
| [22409295](https://pubmed.ncbi.nlm.nih.gov/22409295/) | 2012 | Phase 2 Combination Trial | British Journal of Haematology | Ofatumumab + CHOP (O-CHOP) as frontline treatment for FL, two-dose comparison |
| [24443277](https://pubmed.ncbi.nlm.nih.gov/24443277/) | 2014 | Population PK Analysis | Journal of Clinical Pharmacology | Population pharmacokinetics of ofatumumab across CLL, FL, and rheumatoid arthritis |
| [28983798](https://pubmed.ncbi.nlm.nih.gov/28983798/) | 2017 | Review | Advances in Therapy | 20-year review of anti-CD20 therapy (rituximab) across B-cell hematologic malignancies |
| [21083037](https://pubmed.ncbi.nlm.nih.gov/21083037/) | 2010 | Review | Expert Review of Hematology | Emerging therapeutic strategies in follicular lymphoma |
| [35663281](https://pubmed.ncbi.nlm.nih.gov/35663281/) | 2022 | Review | Leukemia Research Reports | Immunotherapy in indolent non-Hodgkin lymphoma, including FL |
| [18390837](https://pubmed.ncbi.nlm.nih.gov/18390837/) | 2008 | Phase 1/2 Trial | Blood | First clinical use of ofatumumab in relapsed/refractory FL |

---

## Taiwan Market Information

Ofatumumab is currently **not marketed in Taiwan** (0 licenses on record). No authorization data is available to summarize.

---

## Cytotoxicity

Ofatumumab is included in this section as its established indication (CLL/SLL) is a hematologic malignancy, though it is a **targeted biologic rather than a conventional cytotoxic chemotherapy agent**.

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy / Immunotherapy (anti-CD20 monoclonal antibody) |
| Myelosuppression Risk | Low–Moderate — neutropenia has been reported in CLL/FL trials, but this is distinct from classic cytotoxic-agent myelosuppression |
| Emetogenicity Classification | Low (monoclonal antibodies are generally minimally emetogenic) |
| Monitoring Items | CBC with differential, infusion-related reaction monitoring, hepatitis B screening (anti-CD20 reactivation risk), immunoglobulin levels |
| Handling Protection | Standard IV biologic infusion precautions with premedication; does not require cytotoxic chemotherapy handling protocols |

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Multiple completed Phase 2 trials — including a randomized Phase 2 study (NCT01286272/CALGB 50904) — consistently support ofatumumab's activity in follicular lymphoma, leveraging the same CD20-targeting mechanism already validated in its established CLL/SLL indication. However, no FL-specific Phase 3 confirmatory trial exists, and the drug is not currently marketed in Taiwan.

**To proceed, the following is needed:**
- TFDA/import registration pathway assessment, since ofatumumab has 0 current Taiwan authorizations
- Package insert warnings, contraindications, and DDI data (currently a Blocking data gap)
- Detailed mechanism of action documentation from DrugBank
- Confirmation of whether a Phase 3 FL-specific trial is planned or needed before market entry
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

