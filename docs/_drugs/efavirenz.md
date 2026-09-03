---
layout: default
title: Efavirenz
parent: 僅模型預測 (L5)
nav_order: 120
evidence_level: L5
indication_count: 3
---

# Efavirenz
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

# Efavirenz: From HIV-1 Infection to Simian Immunodeficiency Virus Infection

## One-Sentence Summary

Efavirenz is a non-nucleoside reverse transcriptase inhibitor (NNRTI) established for HIV-1 infection treatment (reflected consistently across the supporting literature, though not explicitly listed in this evidence pack).
The TxGNN model predicts it may be relevant to **Simian Immunodeficiency Virus (SIV) infection**,
but the supporting evidence base consists almost entirely of **preclinical macaque-model studies (16 publications)** and a single **withdrawn, enrollment-zero trial**, with no confirmed human clinical development for this specific indication.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | HIV-1 infection (inferred from consistent literature context; not explicitly captured in `taiwan_regulatory` data) |
| Predicted New Indication | Simian immunodeficiency virus infection |
| TxGNN Prediction Score | 99.80% |
| Evidence Level | L4 (preclinical/mechanistic studies only) |
| Norway Market Status | Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in this evidence pack (`original_moa: [Data Gap]`). Based on the supporting literature, efavirenz is a well-characterized NNRTI that inhibits HIV-1 reverse transcriptase, and its clinical use for HIV-1 infection is well established in the broader literature context accompanying this evidence pack.

The predicted indication, "simian immunodeficiency virus infection," is not a human disease — SIV is the macaque analog of HIV used to build the RT-SHIV chimeric virus model (SIV backbone with HIV-1 reverse transcriptase inserted) specifically so that HIV-targeted NNRTIs like efavirenz can be tested in nonhuman primates. Mechanistically, this is coherent: because efavirenz's target (HIV-1 RT) is deliberately engineered into the RT-SHIV virus, efavirenz is pharmacologically active against it. However, this represents a **research/animal-model use case rather than a novel human therapeutic indication**, and should not be interpreted as a new clinical repurposing opportunity in the conventional sense.

It is worth noting that the second-ranked prediction ("feline acquired immunodeficiency syndrome," i.e., FIV in cats) shows the same pattern — real efavirenz-containing HIV trials (e.g., ATRIPLA in NCT01263015) appear in the evidence set, but only because ATRIPLA is the human comparator drug in trials of *unrelated* investigational compounds (dolutegravir/GSK1349572), not because of an FIV-specific human study.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00863668](https://clinicaltrials.gov/study/NCT00863668) | NA | Withdrawn | 0 | Study of HIV/SIV viral decay kinetics with integrase inhibitor raltegravir in nonhuman primate models; withdrawn with zero enrollment, providing no usable efficacy data for efavirenz specifically |

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [35856680](https://pubmed.ncbi.nlm.nih.gov/35856680/) | 2022 | Preclinical (NHP model) | Antimicrob Agents Chemother | Mass spectrometry imaging of antiretroviral (incl. efavirenz) tissue distribution vs. viral RNA and fibrosis in RT-SHIV-infected macaque spleens |
| [24777106](https://pubmed.ncbi.nlm.nih.gov/24777106/) | 2014 | Preclinical (NHP model) | Antimicrob Agents Chemother | Enhanced 4–5 drug HAART regimens improve RT-SHIV viral decay kinetics in rhesus macaques |
| [24505452](https://pubmed.ncbi.nlm.nih.gov/24505452/) | 2014 | Preclinical (NHP model) | PLoS One | Characterizes residual viremia and lack of viral evolution in RT-SHIV macaque HAART model |
| [26559632](https://pubmed.ncbi.nlm.nih.gov/26559632/) | 2015 | Preclinical (NHP model) | Retrovirology | Well-mixed plasma/tissue viral populations in RT-SHIV macaques suggest no ongoing tissue replication during ART |
| [22933296](https://pubmed.ncbi.nlm.nih.gov/22933296/) | 2012 | Preclinical (NHP model) | J Virol | Ultrasensitive PCR detects pre-existing drug-resistant RT-SHIV variants in macaques prior to ART |
| [21084490](https://pubmed.ncbi.nlm.nih.gov/21084490/) | 2011 | Preclinical (NHP model) | J Virol | Genetic diversity of RT-SHIV persists in macaques despite efavirenz-containing ART |
| [21289110](https://pubmed.ncbi.nlm.nih.gov/21289110/) | 2011 | Preclinical (mechanistic) | J Virol | Gag-Pol/clathrin interaction study in HIV-1 and related primate lentiviruses |
| [20032180](https://pubmed.ncbi.nlm.nih.gov/20032180/) | 2010 | Preclinical (NHP model) | J Virol | Identifies viral sanctuaries persisting during HAART in the RT-SHIV macaque AIDS model |
| [20668516](https://pubmed.ncbi.nlm.nih.gov/20668516/) | 2010 | Preclinical (NHP model) | PLoS One | Viral decay kinetics characterized in HAART-treated RT-SHIV macaque model |
| [19889213](https://pubmed.ncbi.nlm.nih.gov/19889213/) | 2009 | Preclinical (NHP model) | Retrovirology | RT-SHIV subpopulation dynamics in macaques during short-course efavirenz monotherapy followed by combination ART |

*Additional publications (e.g., PMID 15328115, 15564466, 15919889, 19195672, 15040537, 17045247) further support the RT-SHIV/efavirenz macaque model but are omitted here for brevity.*

## Norway Market Information

No marketing authorization data is available — efavirenz is currently **not marketed** in this jurisdiction (`total_licenses: 0`).

## Safety Considerations

Please refer to the package insert for safety information. (All safety fields in this evidence pack — key warnings, contraindications, and drug interactions — are currently data gaps.)

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked predicted indication ("simian immunodeficiency virus infection") is an animal-model disease rather than a human clinical indication, and the sole associated clinical trial was withdrawn with zero enrollment. Evidence Level L4 (preclinical only), combined with a **Blocking** data gap on TFDA/label safety information and missing MOA data, means this candidate is not ready for further evaluation.

**To proceed, the following is needed:**
- Resolve DG001 (Blocking): obtain official label warnings/contraindications before any S1 safety screening
- Resolve DG002: obtain formal MOA data from DrugBank to support mechanistic rationale
- Clarify the actual human-relevant indication being targeted — the current "SIV infection" and "feline AIDS" predictions reflect nonhuman research models, not repurposable human diseases; re-run or re-map TxGNN output against a human-disease ontology filter
- Confirm real-world marketing/regulatory status, since 0 authorizations are currently on file
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

