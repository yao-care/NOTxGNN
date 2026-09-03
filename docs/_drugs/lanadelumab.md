---
layout: default
title: Lanadelumab
parent: 僅模型預測 (L5)
nav_order: 198
evidence_level: L5
indication_count: 10
---

# Lanadelumab
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

# Lanadelumab: From Undocumented Original Indication to C1 Inhibitor Deficiency (Hereditary Angioedema)

## One-Sentence Summary

> The Evidence Pack does not record a documented original indication for lanadelumab (DrugBank field empty), though supporting literature within the pack identifies it as a plasma kallikrein inhibitor developed for hereditary angioedema (HAE) prophylaxis.
> The TxGNN model predicts high relevance to **C1 Inhibitor Deficiency**, which is in fact the disease category underlying HAE — meaning this signal largely **confirms an already-established indication rather than a novel repurposing opportunity**.
> Evidence is substantial: **22 clinical trials** (including one completed pivotal Phase 3 RCT) and **20 publications** support this indication, but the drug is currently **not marketed in Norway** and safety documentation is entirely absent.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not documented in DrugBank record (field empty); literature (PMID 30267321) identifies HAE prophylaxis as the drug's known global indication |
| Predicted New Indication | C1 Inhibitor Deficiency |
| TxGNN Prediction Score | 99.996% |
| Evidence Level | L2 (1 completed Phase 3 RCT + extensive supportive Phase 3/real-world/systematic-review evidence) |
| Norway Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the structured `original_moa` field (flagged as data gap DG002). However, literature within this Evidence Pack (PMID 30267321) describes lanadelumab as a fully human monoclonal antibody that inhibits plasma kallikrein. Mutations in the *SERPING1* gene cause C1 inhibitor (C1-INH) deficiency or dysfunction, leading to uncontrolled plasma kallikrein activity and excess bradykinin production — the vasodilator believed to drive angioedema symptoms.

Importantly, "C1 inhibitor deficiency" (the predicted indication) is not a distinct new disease target relative to lanadelumab's mechanism — it is the underlying pathophysiological category of hereditary angioedema, the condition the drug's own mechanism was designed to treat. This suggests the TxGNN prediction here is best interpreted as a **validation signal** (the model correctly recovering a known drug-disease relationship) rather than a true off-label repurposing hypothesis. This is reinforced by the fact that lanadelumab (Takhzyro®) is already approved and marketed for HAE in the US, EU, Japan, China, and South Korea, per the clinical trial and literature evidence below — it simply has not yet obtained authorization in Norway.

Because the "original indication" field in this Evidence Pack is empty, we recommend this be treated as a **data completeness issue** in the source DrugBank extraction rather than genuine absence of an approved indication, and flagged for correction before this candidate proceeds further.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT02586805](https://clinicaltrials.gov/study/NCT02586805) | Phase 3 | Completed | 125 | HELP Study — pivotal randomized, double-blind, placebo-controlled trial of lanadelumab for long-term prophylaxis against HAE attacks (Type I/II) |
| [NCT02741596](https://clinicaltrials.gov/study/NCT02741596) | Phase 3 | Completed | 212 | HELP Study Extension — open-label long-term safety and efficacy follow-up |
| [NCT04070326](https://clinicaltrials.gov/study/NCT04070326) | Phase 3 | Completed | 21 | SPRING Study — PK/PD and efficacy of lanadelumab in pediatric HAE patients (2–<12 years) |
| [NCT04180163](https://clinicaltrials.gov/study/NCT04180163) | Phase 3 | Completed | 12 | Efficacy and safety of lanadelumab in Japanese HAE Type I/II patients |
| [NCT05460325](https://clinicaltrials.gov/study/NCT05460325) | Phase 3 | Completed | 20 | Safety, PK, and efficacy of lanadelumab in Chinese HAE patients over 26 weeks |
| [NCT04444895](https://clinicaltrials.gov/study/NCT04444895) | Phase 3 | Completed | 73 | Long-term safety/efficacy in non-histaminergic angioedema with normal C1-INH |
| [NCT04687137](https://clinicaltrials.gov/study/NCT04687137) | Phase 3 | Completed | 12 | Japan Expanded Access Program prior to local licensure |
| [NCT01923207](https://clinicaltrials.gov/study/NCT01923207) | Phase 1 | Completed | 32 | First-in-human single ascending dose safety/tolerability/PK study |
| [NCT02093923](https://clinicaltrials.gov/study/NCT02093923) | Phase 1 | Completed | 38 | Multiple ascending dose safety/tolerability/PK study in HAE subjects |
| [NCT03845400](https://clinicaltrials.gov/study/NCT03845400) | N/A | Completed | 168 | EMPOWER — real-world observational study of HAE attack rates before/after lanadelumab (US/Canada) |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [30480729](https://pubmed.ncbi.nlm.nih.gov/30480729/) | 2018 | RCT | JAMA | Lanadelumab significantly reduced HAE attack rate vs placebo (HELP Study primary publication) |
| [34287942](https://pubmed.ncbi.nlm.nih.gov/34287942/) | 2022 | Open-label extension | Allergy | Long-term (HELP OLE) prevention of HAE attacks confirmed in patients ≥12 years |
| [40434599](https://pubmed.ncbi.nlm.nih.gov/40434599/) | 2025 | Network Meta-Analysis | Drugs in R&D | Comparative efficacy/safety of lanadelumab vs garadacimab, C1-INH, berotralstat for LTP of HAE |
| [39508959](https://pubmed.ncbi.nlm.nih.gov/39508959/) | 2024 | Systematic Review | Clin Rev Allergy Immunol | Characterizes breakthrough attacks in HAE patients on long-term prophylaxis including lanadelumab |
| [39701274](https://pubmed.ncbi.nlm.nih.gov/39701274/) | 2025 | Real-world observational | JACI In Practice | Multicountry INTEGRATED study confirming real-world effectiveness of lanadelumab |
| [30267321](https://pubmed.ncbi.nlm.nih.gov/30267321/) | 2018 | Review | Drugs | "First Global Approval" review — MOA, development history, and regulatory status |
| [30539362](https://pubmed.ncbi.nlm.nih.gov/30539362/) | 2019 | Review | BioDrugs | Review of preclinical and Phase 1 studies of lanadelumab |
| [32187470](https://pubmed.ncbi.nlm.nih.gov/32187470/) | 2020 | Review | NEJM | General review of hereditary angioedema pathophysiology and treatment |
| [37898409](https://pubmed.ncbi.nlm.nih.gov/37898409/) | 2024 | Review | J Allergy Clin Immunol | Burden of C1-INH-deficient HAE in the Asia-Pacific region |
| [33602658](https://pubmed.ncbi.nlm.nih.gov/33602658/) | 2021 | Review | J Investig Allergol Clin Immunol | Overview of current and emerging HAE treatments including lanadelumab |

---

## Norway Market Information

No authorizations are currently registered in Norway. Lanadelumab has **0 licenses** on file and is classified as **未上市 (not marketed)** in this dataset, despite being approved and marketed elsewhere (US, EU, Japan, China, South Korea) as **Takhzyro®**.

---

## Safety Considerations

Please refer to the package insert for safety information.

> **Note:** This is a blocking data gap (DG001) — no TFDA/local label warnings, contraindications, or drug-drug interaction data are currently available for this candidate, and formal S1 safety evaluation cannot proceed until this is remediated.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Efficacy evidence is strong — a completed pivotal Phase 3 RCT (HELP Study) plus extensive supportive Phase 3, real-world, and systematic-review data across multiple regulatory jurisdictions where the drug is already approved for HAE. However, the drug has zero market authorizations in Norway, and a **blocking data gap** prevents any formal safety review (no label warnings, contraindications, or DDI data available). The predicted indication is also effectively identical to the drug's own established use, so this should be reclassified internally as indication confirmation rather than a repurposing candidate before further action.

**To proceed, the following is needed:**
- Local label/safety data (TFDA-equivalent warnings and contraindications) — download and parse (DG001, blocking)
- Structured mechanism of action data via DrugBank API (DG002)
- Correction of the empty `original_indications` field in the source drug record — confirm and document lanadelumab's established HAE indication
- Confirmation of Norway market authorization application status, if any is planned
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

