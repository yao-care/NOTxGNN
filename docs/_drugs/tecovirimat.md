---
layout: default
title: Tecovirimat
parent: 僅模型預測 (L5)
nav_order: 341
evidence_level: L5
indication_count: 10
---

# Tecovirimat
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

# Tecovirimat: From Smallpox to Vaccinia-Related Complications

## One-Sentence Summary

Tecovirimat (TPOXX) was originally developed and approved to treat smallpox caused by variola virus, an Orthopoxvirus. Among the ten TxGNN-predicted indications in this evidence pack, most (hordeolum, vibrio infection, Klebsiella infection, noma, HTLV-1-associated dermatitis, Arterivirus infection, arbovirus infection, E. coli infection) are flagged by the model's own rationale as mechanistically implausible false positives with zero supporting evidence. The one candidate with real support is **Vaccinia** (rank 5), backed by **3 clinical trials** (including an active Phase 2 drug-vaccine interaction study and a completed expanded access protocol) and **18 publications**, making it the only indication in this set warranting further evaluation.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Smallpox (variola virus) — not present in the regulatory dataset (Norway: unlicensed), but documented in supporting literature (FDA approval, July 2018) |
| Predicted New Indication | Vaccinia (Orthopoxvirus infection/complications, incl. post-vaccination adverse events) |
| TxGNN Prediction Score | 99.62% |
| Evidence Level | L2 |
| Norway Market Status | ✗ Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Proceed with Guardrails |

## Why is This Prediction Reasonable?

The `original_moa` field in the regulatory dataset is a data gap, but the mechanism can be reconstructed from the supporting literature: tecovirimat inhibits the Orthopoxvirus VP37 envelope-wrapping protein, blocking formation of the extracellular enveloped virus (EEV) and thereby preventing cell-to-cell and systemic viral spread. This mechanism is intrinsic to the Orthopoxvirus genus as a whole, not specific to variola.

Vaccinia virus belongs to the same genus as variola (smallpox), sharing the VP37-dependent EEV assembly pathway that tecovirimat targets. This is a near-neighbor extension rather than a mechanistically distant repurposing candidate: vaccinia is used as the live smallpox vaccine (e.g., ACAM2000, JYNNEOS), and tecovirimat is already used in real-world practice to manage severe or progressive vaccinia complications following vaccination, secondary transmission, or occupational exposure — as reflected in the FDA-sanctioned expanded access protocol (NCT05380752) and a completed drug-vaccine interaction trial (NCT04957485).

**Note on other TxGNN-ranked candidates:** Ranks 1–4 and 7–10 (hordeolum, vibrio infection, Klebsiella infection, noma, HTLV-1-associated dermatitis, Arterivirus infection, arbovirus infection, E. coli infection) scored similarly high (~99.6%) but each carries an explicit "no biological plausibility" assessment and no supporting trials or literature (L5/Hold) — these are not discussed further. Rank 6, "coinfection," is a broader, less specific signal (L4/S1, Research Question): the underlying evidence supports tecovirimat's role specifically against the orthopoxvirus component of mpox/HIV or mpox/syphilis co-infections in immunocompromised hosts, not a standalone approvable indication.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT04957485](https://clinicaltrials.gov/study/NCT04957485) | Phase 2 | Active, not recruiting | 100 | RCT evaluating whether concomitant oral tecovirimat (TPOXX, BID × 28 days) interferes with JYNNEOS vaccine immunogenicity vs. placebo |
| [NCT05380752](https://clinicaltrials.gov/study/NCT05380752) | N/A (Expanded Access) | No longer available | N/A | Provided IV tecovirimat to patients with confirmed/suspected orthopoxvirus infection or severe vaccinia adverse reactions unable to tolerate oral formulation |
| [NCT05976100](https://clinicaltrials.gov/study/NCT05976100) | Phase 1 | Completed | 90 | Safety, tolerability, and PK study of NIOCH-14, a comparator anti-orthopoxvirus agent; supportive of the drug class rationale rather than tecovirimat itself |

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [32882158](https://pubmed.ncbi.nlm.nih.gov/32882158/) | 2021 | Review | Expert Rev Anti Infect Ther | Overview of tecovirimat's approval for smallpox and its expanded anti-orthopoxvirus (incl. vaccinia) applications |
| [22904336](https://pubmed.ncbi.nlm.nih.gov/22904336/) | 2012 | Case Report | J Infect Dis | Progressive vaccinia in an immunocompromised smallpox vaccinee successfully managed with VIG plus ST-246 (tecovirimat) and CMX001 |
| [31677948](https://pubmed.ncbi.nlm.nih.gov/31677948/) | 2020 | Preclinical | Vaccine | Co-administration of tecovirimat with ACAM2000 vaccine in non-human primates; assessed impact on vaccine immunogenicity and efficacy against lethal monkeypox challenge |
| [36374026](https://pubmed.ncbi.nlm.nih.gov/36374026/) | 2022 | Review | Antimicrob Agents Chemother | Mechanism and clinical role of tecovirimat against orthopoxviruses including vaccinia and human monkeypox virus |
| [36961984](https://pubmed.ncbi.nlm.nih.gov/36961984/) | 2023 | Review | J Med Chem | Overview of antiviral agents, including tecovirimat, active against monkeypox virus and other orthopoxviruses |
| [35763248](https://pubmed.ncbi.nlm.nih.gov/35763248/) | 2022 | Review | Drugs | Prevention and treatment strategies for monkeypox, including tecovirimat's stockpile role for orthopoxvirus countermeasures |
| [36403582](https://pubmed.ncbi.nlm.nih.gov/36403582/) | 2023 | Review | Lancet | Comprehensive review of monkeypox as an Orthopoxvirus disease, contextualizing tecovirimat's use |
| [39401235](https://pubmed.ncbi.nlm.nih.gov/39401235/) | 2024 | Review | JAMA | Mpox clinical presentation, diagnosis, and treatment strategies, including antiviral therapy |
| [36130588](https://pubmed.ncbi.nlm.nih.gov/36130588/) | 2022 | Review | J Pharm Pharm Sci | Monkeypox virology, pathophysiology, and treatment landscape |
| [37131608](https://pubmed.ncbi.nlm.nih.gov/37131608/) | 2023 | Review | bioRxiv | Survey of antivirals (tecovirimat, brincidofovir) against monkeypox and related orthopoxvirus infections |

## Norway Market Information

Tecovirimat is currently **not marketed** in Norway (market status: 未上市), and no marketing authorization records are present in the evidence pack.

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Tecovirimat's mechanism (VP37/EEV inhibition) is directly applicable to vaccinia given its shared Orthopoxvirus genus with variola, and this extension is already supported by real-world regulatory precedent (FDA expanded access) and an active Phase 2 interaction trial — but the evidence base is still limited to one ongoing RCT, one closed expanded-access program, and no completed efficacy trial specific to vaccinia.

**To proceed, the following is needed:**
- Official TFDA/EMA package insert (warnings, contraindications) — currently a Blocking data gap (DG001), required before any S1 safety screening
- Structured DrugBank mechanism-of-action record — currently a High-severity data gap (DG002), needed to formally document the mechanistic rationale beyond literature inference
- Readout of NCT04957485 (estimated completion 2027) to confirm no immunological interference with JYNNEOS and to characterize safety in the target population
- If repurposing is pursued, clarification of a regulatory pathway for a currently unlicensed product in Norway
- If "coinfection" (rank 6) is explored further, the indication should be narrowed to "orthopoxvirus infection in immunocompromised hosts (e.g., HIV+)" rather than the generic label, to remain clinically and regulatorily meaningful
- No further action needed on ranks 1–4 and 7–10 (hordeolum, vibrio infection, Klebsiella infection, noma, HTLV-1-associated dermatitis, Arterivirus infection, arbovirus infection, E. coli infection) — correctly scored Hold due to absence of mechanistic plausibility or evidence
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

