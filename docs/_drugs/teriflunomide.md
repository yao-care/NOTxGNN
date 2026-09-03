---
layout: default
title: Teriflunomide
parent: 僅模型預測 (L5)
nav_order: 351
evidence_level: L5
indication_count: 1
---

# Teriflunomide
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

# Teriflunomide: From Established Use to TxGNN-Confirmed Relapsing-Remitting Multiple Sclerosis

## One-Sentence Summary

> Teriflunomide (DrugBank DB08880) is the active oral disease-modifying therapy marketed internationally as Aubagio®; structured original-indication data is not available in the local regulatory dataset, but published literature confirms it has been licensed in the EU/US for relapsing-remitting multiple sclerosis (RRMS) since 2013.
> The TxGNN model independently predicts **RRMS** as its top indication with a **99.24%** confidence score — this is a case where the model recovers the drug's own established indication rather than surfacing a genuinely new one.
> The prediction is backed by **30 clinical trials** (including multiple completed Phase 3 pivotal/comparator RCTs) and **20 publications**, representing very strong evidence, though the drug is currently not marketed locally and a critical local safety-label data gap remains unresolved.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not documented in local regulatory data (drug not marketed locally); publicly known internationally as relapsing-remitting multiple sclerosis (Aubagio®, EU-approved since 2013) |
| Predicted New Indication | Relapsing-remitting multiple sclerosis |
| TxGNN Prediction Score | 99.24% |
| Evidence Level | L1 |
| Norway Market Status | ✗ Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

The structured `original_moa` field is not populated, but the supporting literature is consistent and specific: teriflunomide is an oral, selective and reversible inhibitor of the mitochondrial enzyme **dihydro-orotate dehydrogenase (DHODH)**. By blocking de novo pyrimidine synthesis, it reduces proliferation and activation of rapidly dividing lymphocytes (both T- and B-cells), producing an anti-inflammatory, immunomodulatory effect (PMID 31098896, PMID 32757523).

The predicted indication — RRMS — is not a novel therapeutic area for teriflunomide; it is the drug's own established, globally approved use (marketed as Aubagio® in the EU since August 2013, per PMID 26758290, and used as the active comparator in numerous head-to-head Phase 3 trials against newer DMTs). This means the TxGNN score here should be interpreted as a **validation signal** — the model correctly recovers a well-known drug–disease relationship with very high confidence — rather than as a genuine repurposing opportunity.

Because the local (Taiwan/Norway) regulatory dataset shows zero licenses and no recorded original indication, this candidate's practical value is less about scientific novelty and more about flagging that **teriflunomide currently has no local market authorization**, despite robust global efficacy and safety data for RRMS.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00134563](https://clinicaltrials.gov/study/NCT00134563) | Phase 3 | Completed | 1088 | Pivotal RCT (TEMSO) — teriflunomide reduced relapse frequency and disability accumulation vs placebo in RMS |
| [NCT00883337](https://clinicaltrials.gov/study/NCT00883337) | Phase 3 | Completed | 324 | TENERE study — compared teriflunomide (two doses) vs interferon beta-1a on time-to-failure and relapse frequency |
| [NCT00803049](https://clinicaltrials.gov/study/NCT00803049) | Phase 3 | Completed | 742 | Long-term extension documenting safety/tolerability of teriflunomide 7 mg and 14 mg over time |
| [NCT04788615](https://clinicaltrials.gov/study/NCT04788615) | Phase 3 | Completed | 185 | Ofatumumab vs physician-choice first-line DMT (incl. teriflunomide) in newly diagnosed RMS |
| [NCT07189325](https://clinicaltrials.gov/study/NCT07189325) | Phase 3 | Not yet recruiting | 250 | Anti-CD20 maintenance vs de-escalation strategy in RRMS (teriflunomide-context trial) |
| [NCT00228163](https://clinicaltrials.gov/study/NCT00228163) | Phase 2 | Completed | 147 | Long-term safety/efficacy extension of early Phase 2 teriflunomide study |
| [NCT02490982](https://clinicaltrials.gov/study/NCT02490982) | N/A | Completed | 106 | Observational effectiveness study of teriflunomide in real-world RRMS practice |
| [NCT03464448](https://clinicaltrials.gov/study/NCT03464448) | N/A | Completed | 30 | Mechanistic Phase 4 study on regulatory B-lymphocytes as mediators of teriflunomide's therapeutic effect |
| [NCT04129736](https://clinicaltrials.gov/study/NCT04129736) | Phase 4 | Completed | 12 | Measured teriflunomide 14 mg concentration in serum and cerebrospinal fluid |
| [NCT01881191](https://clinicaltrials.gov/study/NCT01881191) | N/A | Completed | 50 | 12-month MRI study of teriflunomide's effect on gray matter pathology |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [32757523](https://pubmed.ncbi.nlm.nih.gov/32757523/) | 2020 | RCT | NEJM | Ofatumumab vs teriflunomide head-to-head trial; describes teriflunomide's mechanism (pyrimidine synthesis inhibition, reduced T/B-cell activation) |
| [40202623](https://pubmed.ncbi.nlm.nih.gov/40202623/) | 2025 | RCT | NEJM | Tolebrutinib (BTK inhibitor) vs teriflunomide in relapsing MS |
| [36001711](https://pubmed.ncbi.nlm.nih.gov/36001711/) | 2022 | RCT | NEJM | Ublituximab vs teriflunomide in relapsing MS |
| [33779698](https://pubmed.ncbi.nlm.nih.gov/33779698/) | 2021 | RCT | JAMA Neurology | OPTIMUM trial — ponesimod vs teriflunomide, first Phase 3 head-to-head of two oral DMTs |
| [39307151](https://pubmed.ncbi.nlm.nih.gov/39307151/) | 2024 | RCT | Lancet Neurology | Evobrutinib (BTK inhibitor) vs teriflunomide, Phase 3 evolutionRMS1/2 trials |
| [35266417](https://pubmed.ncbi.nlm.nih.gov/35266417/) | 2022 | RCT | Mult Scler | ASCLEPIOS I/II — ofatumumab vs teriflunomide in treatment-naive MS patients |
| [38174776](https://pubmed.ncbi.nlm.nih.gov/38174776/) | 2024 | Systematic Review | Cochrane Database Syst Rev | Network meta-analysis of immunomodulators/immunosuppressants (incl. teriflunomide) for RRMS |
| [31098896](https://pubmed.ncbi.nlm.nih.gov/31098896/) | 2019 | Review | Drugs | Comprehensive review of teriflunomide's mechanism, RCT and real-world evidence in RRMS |
| [33620411](https://pubmed.ncbi.nlm.nih.gov/33620411/) | 2021 | Review | JAMA | General MS diagnosis and treatment review referencing teriflunomide as a first-line DMT |
| [26758290](https://pubmed.ncbi.nlm.nih.gov/26758290/) | 2016 | Review | CNS Drugs | Review of EU Summary of Product Characteristics for teriflunomide, including safety outcomes |

---

## Norway Market Information

Teriflunomide currently holds **no marketing authorization** in the local (Taiwan/Norway) regulatory dataset (0 licenses recorded). No product, dosage form, or approved indication text is available to summarize.

---

## Safety Considerations

Please refer to the package insert for safety information.

*Note: A local regulatory label (TFDA warnings/contraindications) has not yet been retrieved and is flagged as a blocking data gap — see Conclusion below.*

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- Global clinical evidence for teriflunomide in RRMS is extensive and strong (L1: multiple completed Phase 3 RCTs, extensive comparator literature, long-established international approval), but the predicted indication is essentially the drug's **already-known primary indication** rather than a novel repurposing signal — this candidate confirms the model rather than identifying new value.
- More critically, a **Blocking**-severity data gap (DG001: TFDA label warnings/contraindications) prevents the candidate from entering the S1 safety pre-assessment stage, and the drug has zero local market authorizations.

**To proceed, the following is needed:**
- Retrieve and parse the official local product label (warnings, contraindications) — required to clear the Blocking gap (DG001)
- Obtain structured MOA confirmation from DrugBank (DG002)
- Clarify whether a local market authorization filing is planned, given teriflunomide's established international approval (Aubagio®) for this same indication
- Because this prediction largely reproduces a known indication, consider re-running TxGNN with known indications excluded to identify genuinely novel repurposing candidates for this drug
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

