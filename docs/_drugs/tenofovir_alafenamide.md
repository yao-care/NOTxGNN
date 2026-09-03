---
layout: default
title: Tenofovir Alafenamide
parent: 僅模型預測 (L5)
nav_order: 348
evidence_level: L5
indication_count: 3
---

# Tenofovir Alafenamide
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

# Tenofovir Alafenamide: From Unclear Original Indication to Simian Immunodeficiency Virus (SIV) Infection

## One-Sentence Summary

> Tenofovir Alafenamide (DB09299) has an unspecified original indication in this evidence pack (data gap), so its established clinical role cannot be confirmed here.
> The TxGNN model's top-ranked prediction — **feline acquired immunodeficiency syndrome** — has **zero supporting evidence** and is a veterinary condition, so it is not clinically actionable.
> Instead, this report focuses on the highest-ranked prediction that has actual supporting data, **Simian Immunodeficiency Virus (SIV) Infection**, backed by **1 clinical trial** and **9 publications**, mostly preclinical macaque studies relevant to HIV pre-exposure prophylaxis research.

> **Note on indication selection:** `predicted_indications[0]` (feline AIDS, score 99.89%) and `predicted_indications[2]` (a rare pediatric neurodevelopmental disorder, score 99.87%) both have no clinical trials or literature attached, and neither represents a human disease context suitable for repurposing evaluation. `predicted_indications[1]` (SIV infection, score 99.89% — statistically indistinguishable from rank 1) is the only prediction with retrievable evidence, so it is used as the primary subject of this report.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not specified in evidence pack (data gap) |
| Predicted New Indication | Simian Immunodeficiency Virus (SIV) Infection |
| TxGNN Prediction Score | 99.89% |
| Evidence Level | L4 (preclinical / mechanism studies) |
| Taiwan Market Status | Not Marketed (未上市) |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available for this drug in the evidence pack. Based on known pharmacological class information, Tenofovir Alafenamide is a nucleotide reverse transcriptase inhibitor (NRTI) prodrug that is intracellularly converted to tenofovir diphosphate, which inhibits retroviral reverse transcriptase.

SIV (simian immunodeficiency virus) and SHIV (simian/human immunodeficiency virus) are the standard non-human-primate models used to study HIV pathogenesis, prevention, and treatment, since HIV itself does not naturally infect macaques. The literature evidence in this pack consists almost entirely of macaque PrEP (pre-exposure prophylaxis) and PEP (post-exposure prophylaxis) studies — vaginal inserts, oral regimens, and biodegradable implants delivering tenofovir alafenamide (alone or combined with emtricitabine/elvitegravir) to block SHIV transmission. This is mechanistically consistent with tenofovir alafenamide's known reverse-transcriptase-inhibiting activity, and the SIV/SHIV model is a translational proxy for HIV — not a distinct new human disease target.

In other words, this "predicted new indication" most likely reflects the model recognizing tenofovir alafenamide's established antiretroviral pharmacology through its animal-model research literature, rather than identifying a genuinely novel therapeutic application. The clinical implication is that this evidence supports the drug's known antiretroviral mechanism rather than a new repurposing opportunity.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT03577782](https://clinicaltrials.gov/study/NCT03577782) | Phase 1/2 | Unknown | 12 | Evaluated vedolizumab combined with antiretroviral therapy (ART) to achieve sustained HIV virological remission after ART interruption; not a direct tenofovir alafenamide efficacy trial, and relevance to this specific indication is unconfirmed |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [39632836](https://pubmed.ncbi.nlm.nih.gov/39632836/) | 2024 | Preclinical | Nature Communications | Early ART initiation with oral emtricitabine/tenofovir alafenamide plus long-acting cabotegravir/rilpivirine achieved SHIV remission in macaques |
| [38134382](https://pubmed.ncbi.nlm.nih.gov/38134382/) | 2024 | Preclinical | J Infect Dis | TAF/elvitegravir vaginal inserts gave extended post-exposure protection against vaginal SHIV in macaques |
| [39559349](https://pubmed.ncbi.nlm.nih.gov/39559349/) | 2024 | Preclinical | Frontiers in Immunology | Described a dual-purpose humanized mouse model for testing antiviral strategies against SIV and HIV |
| [35913838](https://pubmed.ncbi.nlm.nih.gov/35913838/) | 2022 | Preclinical | J Antimicrob Chemother | Biodegradable implant releasing tenofovir alafenamide showed safety and efficacy for vaginal HIV protection in macaques |
| [31362305](https://pubmed.ncbi.nlm.nih.gov/31362305/) | 2019 | Preclinical | J Infect Dis | Oral TAF/emtricitabine or TAF alone protected macaques against vaginal SHIV infection |
| [31730629](https://pubmed.ncbi.nlm.nih.gov/31730629/) | 2019 | Preclinical | PLoS One | Developed a protocol for reliable daily oral ARV dosing in macaques for preclinical HIV prevention/treatment studies |
| [27465645](https://pubmed.ncbi.nlm.nih.gov/27465645/) | 2016 | Preclinical | J Infect Dis | Oral emtricitabine/TAF chemoprophylaxis protected macaques from rectal SHIV infection |
| [22740713](https://pubmed.ncbi.nlm.nih.gov/22740713/) | 2012 | Preclinical | J Infect Dis | Oral pre-exposure prophylaxis reduced inflammation and CD4 loss in acute SHIV breakthrough infection |
| [16810108](https://pubmed.ncbi.nlm.nih.gov/16810108/) | 2006 | Preclinical | J Acquir Immune Defic Syndr | Oral tenofovir disoproxil fumarate and topical GS-7340 (TAF precursor) protected infant macaques against repeated oral SIV challenge |

---

## Taiwan Market Information

Tenofovir Alafenamide currently has **no marketing authorizations recorded in Taiwan** (market status: 未上市 / Not Marketed, 0 licenses). No product-level dosage form or approved-indication data is available.

---

## Safety Considerations

Please refer to the package insert for safety information. Key warnings, contraindications, and drug-interaction data are not currently available in this evidence pack; retrieval of the TFDA-approved label (DG001, Blocking severity) is required before any safety assessment can proceed.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The evidence base for the top-ranked prediction (feline AIDS) is empty, and the best-supported prediction (SIV infection) is backed only by preclinical macaque studies and one early-phase trial of unconfirmed relevance — consistent with Evidence Level L4, not sufficient for a Go decision. The drug is also not currently marketed in Taiwan, and a Blocking-severity data gap (TFDA label warnings/contraindications) prevents any safety evaluation.

**To proceed, the following is needed:**
- TFDA-approved package insert (warnings, contraindications) to resolve the Blocking data gap
- Confirmed original indication(s) and mechanism of action from DrugBank or product labeling
- Clarification of whether "SIV infection" evidence reflects a genuine new indication or simply reconfirms tenofovir alafenamide's known antiretroviral/PrEP mechanism
- Re-review of the rank-1 (feline AIDS) and rank-3 (rare neurodevelopmental disorder) predictions to determine whether they are valid signals or knowledge-graph artifacts, before any further repurposing work is based on them
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

