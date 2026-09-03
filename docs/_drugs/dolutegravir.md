---
layout: default
title: Dolutegravir
parent: 僅模型預測 (L5)
nav_order: 112
evidence_level: L5
indication_count: 3
---

# Dolutegravir
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

# Dolutegravir: From HIV-1 Infection to Simian Immunodeficiency Virus Infection

## One-Sentence Summary

Dolutegravir is a widely used HIV integrase strand transfer inhibitor (INSTI), publicly known as a first-line treatment for HIV-1 infection, though this evidence pack does not itself contain a formal indication/MOA record (flagged as data gaps DG001/DG002). The TxGNN model's top-ranked prediction is **Simian Immunodeficiency Virus (SIV) Infection** — a non-human-primate research disease rather than a human clinical indication — currently supported by only **1 loosely related clinical trial** and **16 preclinical/animal-virology publications**. Two lower-ranked predictions (feline immunodeficiency virus infection, and a rare neurodevelopmental disorder) are markedly weaker and are not addressed further below beyond the caveats noted in the rationale and conclusion sections.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | HIV-1 infection (publicly known use of dolutegravir; not present as structured data in this evidence pack — see DG002) |
| Predicted New Indication | Simian Immunodeficiency Virus (SIV) Infection — non-human-primate disease model |
| TxGNN Prediction Score | 99.85% |
| Evidence Level | L3 |
| Norway Market Status | ✗ Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data is not available in this evidence pack (flagged as data gap DG002, High severity). Based on publicly known pharmacology, dolutegravir is a second-generation HIV integrase strand transfer inhibitor (INSTI): it blocks the strand-transfer step of retroviral integrase, preventing viral DNA from inserting into the host genome. Its efficacy in HIV-1 infection is well established in clinical use.

HIV-1 and simian immunodeficiency virus (SIV) are both lentiviruses, and their integrase enzymes are structurally highly conserved across species. Published intasome structural studies confirm that dolutegravir binds and inhibits SIV integrase in addition to HIV integrase, and multiple rhesus-macaque studies have directly used dolutegravir-containing antiretroviral regimens to suppress SIV replication as a research model for studying HIV pathogenesis, latency, and drug resistance.

However, this mechanistic link exists entirely within an *animal-model research* context — SIV-infected macaques are a surrogate model used to study HIV, not a distinct human disease. SIV does not infect humans, so this prediction does not represent a new human-labeled indication in the conventional drug-repurposing sense; it instead reflects TxGNN identifying dolutegravir's already-known antiviral activity being reused within the existing macaque disease-model literature. For context, the model's second and third-ranked predictions for this drug carry even weaker translational value: feline immunodeficiency virus infection (L4, pure mechanistic extrapolation with no direct dolutegravir–FIV data) and a rare neurodevelopmental disorder (L5, zero supporting trials or literature). Taken together, this prediction set should be read as a signal of embedding-space similarity in the model rather than a validated new human indication.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT03577782](https://clinicaltrials.gov/study/NCT03577782) | Phase 1/2 | Unknown | 12 | Evaluated vedolizumab plus antiretroviral therapy for HIV virologic remission after treatment interruption in humans. Dolutegravir is not the primary study intervention and the trial status is unknown; graded low relevance (C) to the SIV indication. |

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [30381490](https://pubmed.ncbi.nlm.nih.gov/30381490/) | 2019 | In vivo animal efficacy/resistance study | Journal of Virology | Dolutegravir monotherapy in SIV-infected macaques selected several distinct resistance-mutation patterns with variable virological outcomes, directly characterizing DTG's in vivo resistance barrier. |
| [26378179](https://pubmed.ncbi.nlm.nih.gov/26378179/) | 2015 | In vivo animal resistance characterization | Journal of Virology | Characterized INSTI resistance profiles using SIVmac239 in rhesus macaque PBMCs; resistance mutations paralleled those seen in HIV. |
| [32166319](https://pubmed.ncbi.nlm.nih.gov/32166319/) | 2020 | In vivo animal mechanism/metabolic toxicity study | Clinical Infectious Diseases | Dolutegravir and raltegravir showed proadipogenic and profibrotic effects and induced insulin resistance in human/simian adipose tissue models. |
| [32506843](https://pubmed.ncbi.nlm.nih.gov/32506843/) | 2021 | Structural biology (intasome structure) | The FEBS Journal | Reviewed HIV/SIV intasome crystal structures explaining how INSTIs, including dolutegravir, bind integrase and how resistance mutations drive viral escape. |
| [34903055](https://pubmed.ncbi.nlm.nih.gov/34903055/) | 2021 | Animal model cohort (CNS reservoir) | mBio | Found that lentiviral (HIV/SIV) infection persists in brain tissue despite effective antiretroviral therapy, indicating a CNS reservoir not addressed by current regimens. |
| [41959211](https://pubmed.ncbi.nlm.nih.gov/41959211/) | 2026 | Animal histology study (not DTG-specific) | bioRxiv (preprint) | Characterized SIV- and ART-induced disruption of brain lipid distribution in rhesus macaques; not specific to dolutegravir. |
| [31619550](https://pubmed.ncbi.nlm.nih.gov/31619550/) | 2019 | Mechanism study (Wnt pathway, not virology-specific) | Journal of Virology | Showed Wnt/β-catenin pathway modulation affects memory CD4+ T-cell dynamics in ART-suppressed, SIV-infected macaques — relevant to viral reservoir persistence, not to dolutegravir activity itself. |
| [39509655](https://pubmed.ncbi.nlm.nih.gov/39509655/) | 2024 | Review/epidemiology (human HIV, not directly relevant) | AIDS Reviews | Reviewed the HIV-1/HIV-2 epidemic burden in Ivory Coast; SIV is mentioned only as the evolutionary origin of HIV, not as a treatment target. |
| [28576126](https://pubmed.ncbi.nlm.nih.gov/28576126/) | 2017 | Case report (captive chimpanzee SIVcpz) | Retrovirology | Described successful antiretroviral treatment of SIVcpz-induced immunodeficiency in a single captive chimpanzee. |
| [26150024](https://pubmed.ncbi.nlm.nih.gov/26150024/) | 2016 | Comparative ART regimen study (not DTG-specific) | AIDS Research and Human Retroviruses | Compared coformulated injectable antiretroviral regimens (not including dolutegravir) for viral suppression in SIV-infected rhesus macaques. |

## Norway Market Information

Dolutegravir currently holds **0 marketing authorizations** in Norway and is recorded as **not marketed** in this evidence pack. No product-level license records are available to populate a market information table.

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- The top-ranked TxGNN prediction (SIV infection) is a non-human-primate disease model, not an actionable human indication; its L3 evidence level is built entirely from animal/preclinical virology literature plus a single loosely related human clinical trial that does not test dolutegravir directly.
- The two lower-ranked predictions for this drug are even weaker — feline immunodeficiency virus infection (L4, mechanistic extrapolation only, no direct dolutegravir–FIV data) and a rare neurodevelopmental disorder (L5, zero supporting trials or literature) — reinforcing that this prediction set does not currently point to a viable new human indication.
- Drug-level data gaps compound the uncertainty: DG001 (local regulatory package insert warnings/contraindications) is a Blocking gap that prevents S1 safety evaluation, and DG002 (mechanism-of-action documentation) is a High-severity gap affecting mechanistic-relevance analysis.

**To proceed, the following is needed:**
- Local regulatory package insert data (warnings, contraindications) to clear the Blocking gap DG001 before any S1 safety review can begin
- Confirmed DrugBank/MOA documentation to close gap DG002
- If a human-relevant indication is the goal, direct efficacy/PK data for dolutegravir in an actual human disease context — none of the three current predictions (SIV, FIV, the neurodevelopmental disorder) are human-approvable indications under existing evidence
- A review of the underlying TxGNN disease-ontology mapping for this drug, since two of the three top-ranked predictions resolve to non-human/veterinary disease concepts — this may indicate an embedding or ontology-matching issue worth investigating upstream in the pipeline rather than a genuine repurposing signal
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

