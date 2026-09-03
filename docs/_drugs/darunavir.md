---
layout: default
title: Darunavir
parent: 僅模型預測 (L5)
nav_order: 97
evidence_level: L5
indication_count: 4
---

# Darunavir
{: .fs-9 }

證據等級: **L5** | 預測適應症: **4** 個
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

# Darunavir: From HIV-1 Infection to Simian Immunodeficiency Virus (SIV) Infection

## One-Sentence Summary

Darunavir is a boosted HIV-1 protease inhibitor used as part of combination antiretroviral therapy (cART) for HIV/AIDS.
The TxGNN model predicts it may be effective for **Simian Immunodeficiency Virus (SIV) Infection** — the primate-model correlate of HIV —
but currently only **4 preclinical animal-model publications** support this direction, none of which specifically test darunavir alone, and **no clinical trials** exist for this indication.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not specified in evidence pack (drug is not marketed in Norway); known pharmacological classification is HIV-1 infection, treated as part of boosted cART regimens |
| Predicted New Indication | Simian Immunodeficiency Virus Infection |
| TxGNN Prediction Score | 99.97% |
| Evidence Level | L4 |
| Norway Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, darunavir is a member of the HIV-1 protease inhibitor (PI) class, its efficacy in HIV-1 infection (as part of boosted cART) has been proven, and mechanistically it may be applicable to SIV infection.

SIV is the retrovirus used to establish AIDS models in non-human primates and is genetically and structurally closely related to HIV-1, including a substantial degree of conservation in the Gag-Pol polyprotein processing pathway that PI-class drugs target. This cross-species mechanistic similarity is a well-established rationale for using HIV antiretrovirals, including PIs, in SIV-infected macaque research models.

However, it is important to note that the four supporting publications describe multi-drug cART regimens (some combined with adjunct agents such as the HDAC inhibitor SAHA or the gold compound auranofin) used in SIV/macaque reservoir and eradication research — darunavir (or PI-class drugs generally) appears only as one backbone component, not as the specific subject of efficacy testing. No study isolates or quantifies darunavir's individual contribution to SIV suppression.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [26150024](https://pubmed.ncbi.nlm.nih.gov/26150024/) | 2016 | Animal Cohort | AIDS Res Hum Retroviruses | Compared two novel injectable coformulated cART regimens (PI-class backbone) for suppressing SIV replication in rhesus macaques |
| [25033210](https://pubmed.ncbi.nlm.nih.gov/25033210/) | 2014 | Animal Cohort | PLoS One | Evaluated suppressive cART plus HDAC inhibitor SAHA on viral reservoirs in SIV-infected Chinese rhesus macaques |
| [22737073](https://pubmed.ncbi.nlm.nih.gov/22737073/) | 2012 | Animal Cohort | PLoS Pathogens | Highly intensified multidrug ART achieved long-term viral suppression and reservoir restriction in SIVmac251-infected macaques |
| [21505294](https://pubmed.ncbi.nlm.nih.gov/21505294/) | 2011 | Animal Cohort | AIDS (London) | Gold compound auranofin, added to ART, restricted the viral reservoir and delayed rebound after ART suspension in SIV-infected macaques |

## Norway Market Information

Darunavir is currently not marketed in Norway; no authorization records are available in the evidence pack.

## Safety Considerations

Please refer to the package insert for safety information.

## Other TxGNN-Predicted Candidates (Reviewed, Not Recommended)

| Rank | Disease | Evidence Level | Reason for Hold |
|------|---------|----------------|------------------|
| 2 | Feline acquired immunodeficiency syndrome | L4 | The single supporting trial (NCT02770508) is a human Phase 4 boosted-darunavir HIV regimen study, not a feline/FIV study — likely a disease-ontology mapping error in the knowledge graph; requires engineering review before further consideration |
| 3 | Neurodevelopmental disorder with ataxic gait, absent speech, and decreased cortical white matter | L5 | No mechanistic rationale, no clinical or literature evidence — model score only |
| 4 | Obsolete familial combined hyperlipidemia | L5 | Mechanistically contradictory: darunavir (especially ritonavir-boosted regimens) is a known cause of dyslipidemia, making it a risk factor rather than a treatment; disease label is also flagged as obsolete |

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The only candidate reaching decision stage S1 (SIV infection) is supported solely by preclinical macaque studies in which darunavir is one component of multi-drug regimens, not the subject of dedicated efficacy testing — this is L4 evidence with no clinical trials. The remaining three candidates carry either a likely data/ontology error, no mechanistic support, or a mechanistically contraindicated relationship, and are all rated Hold.

**To proceed, the following is needed:**
- Darunavir-specific (monotherapy or defined-combination) efficacy data in SIV models, isolating its contribution from co-administered agents
- Resolution of the suspected disease-ontology mapping error for "feline acquired immunodeficiency syndrome" (rank 2) before any further evaluation
- TFDA/regulatory label data (warnings, contraindications, DDI) once available, to support S1 safety screening
- Confirmed original indication and MOA data from DrugBank or product labeling, since both are currently data gaps
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

