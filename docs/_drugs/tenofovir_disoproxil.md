---
layout: default
title: Tenofovir Disoproxil
parent: 僅模型預測 (L5)
nav_order: 349
evidence_level: L5
indication_count: 4
---

# Tenofovir Disoproxil
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

Using no additional skill — this is a straightforward evidence-pack → Markdown report generation task per the provided template.

# Tenofovir Disoproxil: From Antiretroviral Therapy (HIV) to Simian Immunodeficiency Virus Infection

## One-Sentence Summary

Tenofovir disoproxil is a nucleotide reverse transcriptase inhibitor (NRTI) prodrug used clinically for HIV antiretroviral therapy. The TxGNN model predicts a strong association with **Simian Immunodeficiency Virus (SIV) Infection**, supported by **2 clinical trials** and **19 publications** — however, the underlying evidence largely reconfirms tenofovir's already-known role in HIV/SIV pre-exposure prophylaxis (PrEP) in nonhuman primate models, rather than pointing to a novel human indication.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available — drug has no license record in Norway (0 authorizations); clinically known as part of HIV antiretroviral therapy per underlying evidence |
| Predicted New Indication | Simian Immunodeficiency Virus (SIV) Infection |
| TxGNN Prediction Score | 99.95% |
| Evidence Level | L3 |
| Norway Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available (data gap, DrugBank query pending). Based on the evidence pack's own repurposing rationale, tenofovir disoproxil is the oral prodrug of tenofovir (PMPA), a nucleotide reverse transcriptase inhibitor that blocks the reverse transcriptase enzyme shared across lentiviruses.

SIV and HIV both belong to the lentivirus genus and use structurally similar reverse transcriptase enzymes, which is why tenofovir's antiviral activity extends mechanistically from HIV to SIV. This mechanistic overlap has been extensively validated in nonhuman primate PrEP/PEP (pre- and post-exposure prophylaxis) models over the past two decades.

However, the evidence pack explicitly flags an important caveat: **SIV infection is a nonhuman primate/veterinary disease model, not a human clinical indication.** The underlying literature does not represent a new repurposing opportunity for human patients — it is preclinical validation of tenofovir's already-established HIV PrEP mechanism, observed in the animal model used to study it. The same caveat applies to the rank-2 prediction (feline AIDS/FIV), which is a veterinary-only indication.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00863668](https://clinicaltrials.gov/study/NCT00863668) | Phase NA | Withdrawn | 0 | Studied HIV RNA decay kinetics using raltegravir (not tenofovir); withdrawn with zero enrollment — low relevance |
| [NCT03577782](https://clinicaltrials.gov/study/NCT03577782) | Phase 1/2 | Unknown | 12 | Vedolizumab + antiretroviral therapy for HIV virological remission; tenofovir not the study drug, status unknown — low relevance |

*Note: Both trials were graded "C" (low relevance) in the underlying evidence assessment — neither directly tests tenofovir disoproxil against SIV infection.*

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [20874040](https://pubmed.ncbi.nlm.nih.gov/20874040/) | 2010 | Review | Pharmacotherapy | Reviews systemic pre-exposure prophylaxis (PrEP) strategies for HIV prevention |
| [27465645](https://pubmed.ncbi.nlm.nih.gov/27465645/) | 2016 | Animal Study | J Infect Dis | TAF + FTC combination protects macaques from rectal SHIV infection |
| [36477356](https://pubmed.ncbi.nlm.nih.gov/36477356/) | 2022 | Animal Study | JCI Insight | Hypo-osmolar rectal tenofovir douche formulation prevents SHIV acquisition in macaques |
| [16810108](https://pubmed.ncbi.nlm.nih.gov/16810108/) | 2006 | Animal Study | J Acquir Immune Defic Syndr | Oral TDF and topical GS-7340 protect infant macaques against repeated oral SIV challenge |
| [16960777](https://pubmed.ncbi.nlm.nih.gov/16960777/) | 2006 | Animal Study | J Infect Dis | TDF chemoprophylaxis provides partial protection against SHIV in macaques with multiple challenges |
| [22072766](https://pubmed.ncbi.nlm.nih.gov/22072766/) | 2012 | Animal Study | J Virol | Vaginal 1% tenofovir gel provides durable protection against SHIV infection in macaques |
| [26743846](https://pubmed.ncbi.nlm.nih.gov/26743846/) | 2016 | Animal Study | J Infect Dis | FTC/TDF prevents vaginal SHIV infection even with chlamydia/trichomonas co-infection |
| [38134382](https://pubmed.ncbi.nlm.nih.gov/38134382/) | 2024 | Animal Study | J Infect Dis | TAF/elvitegravir vaginal inserts extend postexposure protection against SHIV in macaques |
| [23633402](https://pubmed.ncbi.nlm.nih.gov/23633402/) | 2013 | Animal Study | J Infect Dis | FTC/TDF prophylaxis effective even against tenofovir-resistant SHIV (K65R mutation) |
| [14557287](https://pubmed.ncbi.nlm.nih.gov/14557287/) | 2003 | Review | Clin Microbiol Rev | Clinical potential of acyclic nucleoside phosphonates (cidofovir, adefovir, tenofovir) against DNA virus/retrovirus infections |

## Norway Market Information

Currently no authorization records — tenofovir disoproxil is **not marketed in Norway** under this evidence pack (0 licenses on file).

## Safety Considerations

Please refer to the package insert for safety information. (Key warnings, contraindications, and drug-interaction data are not currently available in this evidence pack — flagged as a **Blocking** data gap requiring TFDA/official prescribing information before any S1 safety evaluation can proceed.)

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
None of the four TxGNN-predicted indications represent a genuine, actionable human repurposing opportunity: the top two (SIV infection, feline AIDS) are animal/veterinary disease models that merely reconfirm tenofovir's already-known antiretroviral mechanism in nonhuman hosts, while the remaining two (a rare neurodevelopmental disorder and an obsolete hyperlipidemia term) have no supporting evidence and are flagged L5 (model prediction only). In addition, safety data required for even a preliminary review is missing (Blocking gap).

**To proceed, the following is needed:**
- Official TFDA/manufacturer prescribing information (warnings, contraindications) — currently a **Blocking** gap (DG001)
- Confirmed mechanism-of-action data from DrugBank — currently a **High**-severity gap (DG002)
- Clarification of Norway regulatory/market status, since 0 licenses are currently on file
- If pursued further, reframe the search toward genuinely novel *human* indications, since the current top candidates only validate tenofovir's established HIV/PrEP mechanism in animal models
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

