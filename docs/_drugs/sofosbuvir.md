---
layout: default
title: Sofosbuvir
parent: 僅模型預測 (L5)
nav_order: 329
evidence_level: L5
indication_count: 8
---

# Sofosbuvir
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

# Sofosbuvir: From Chronic Hepatitis C Virus Infection to Hepatitis B Virus Infection

## One-Sentence Summary

> Sofosbuvir is a nucleotide NS5B polymerase inhibitor originally developed for chronic hepatitis C virus (HCV) infection.
> The TxGNN model predicts it may also be effective for **Hepatitis B Virus Infection**,
> with **111 clinical trials** and **18 publications** indexed against this candidate — however, closer review shows almost none of this evidence directly tests antiviral efficacy against HBV itself.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Chronic Hepatitis C Virus (HCV) Infection *(inferred from mechanistic evidence in this pack; no Taiwan/Norway label data available)* |
| Predicted New Indication | Hepatitis B Virus Infection |
| TxGNN Prediction Score | 99.77% (rank 2917) |
| Evidence Level | L4 |
| Norway Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Sofosbuvir is a prodrug that is metabolized intracellularly into its active triphosphate form (GS-461203), which competitively inhibits the HCV NS5B RNA-dependent RNA polymerase (RdRp) and causes chain termination during viral RNA replication. This mechanism is highly specific to HCV, a positive-strand RNA virus.

HBV, by contrast, is a partially double-stranded DNA virus that replicates via reverse transcription of an RNA pregenome, using a viral reverse transcriptase rather than an RdRp. There is no established structural or catalytic overlap between sofosbuvir's target and HBV's replication machinery, so the mechanistic case for direct antiviral activity against HBV is weak.

The high TxGNN score for this candidate appears to be driven largely by **confounded evidence**: the majority of indexed trials and publications involve patients with **HCV/HBV coinfection**, where sofosbuvir-based regimens are used to treat the HCV component, while HBV outcomes (viral load, HBsAg, reactivation) are measured only as a secondary safety signal — not as the primary treatment target. The one genuinely HBV-specific study identified (NCT03312023 / PMID 36045503) tested ledipasvir/sofosbuvir in HBV mono-infected subjects and observed only a **modest reduction in HBsAg**, insufficient to establish therapeutic efficacy. Multiple other publications instead describe **HBV reactivation** occurring *during* sofosbuvir-based HCV treatment — an adverse safety signal, not evidence of benefit.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT03312023](https://clinicaltrials.gov/study/NCT03312023) | Phase 2 | Completed | 21 | The only trial directly testing ledipasvir/sofosbuvir in HBV **mono-infected** subjects; endpoints were HBsAg/HBV DNA decline at Week 12 (result: modest HBsAg reduction only) |
| [NCT02555943](https://clinicaltrials.gov/study/NCT02555943) | Phase 2/3 | Completed | 23 | HCV/HBV coinfection cohort assessing incidence and predictors of **HBV reactivation** during DAA treatment of HCV (relevance grade B) |
| [NCT02613871](https://clinicaltrials.gov/study/NCT02613871) | Phase 3 | Completed | 111 | LDV/SOF FDC in Taiwanese HCV genotype 1/2 patients coinfected with HBV; primary endpoint is HCV antiviral efficacy, not HBV (relevance grade C) |
| [NCT04997564](https://clinicaltrials.gov/study/NCT04997564) | Phase 4 | Unknown | 120 | SOF/VEL plus prophylactic TAF in HCV/HBV-coinfected patients in China, designed to prevent HBV reactivation during HCV treatment |
| [NCT02219685](https://clinicaltrials.gov/study/NCT02219685) | Phase 2 | Completed | 40 | Placebo-controlled study of LDV/SOF on cerebral metabolism/neurocognition in chronic HCV; mechanistically unrelated to HBV (relevance grade C) |
| [NCT02605304](https://clinicaltrials.gov/study/NCT02605304) | Phase 2 | Terminated | 7 | Retreatment strategies for DAA-failed HCV patients; indexed via drug overlap only |
| [NCT03572140](https://clinicaltrials.gov/study/NCT03572140) | N/A | Unknown | 297 | Safety and resistance-associated variant assessment of sofosbuvir + daclatasvir in chronic HCV genotype 4 |
| [NCT02483156](https://clinicaltrials.gov/study/NCT02483156) | Phase 2/3 | Completed | 80 | Sofosbuvir + ribavirin vs. an investigational combination in Egyptian adults with HCV genotype 4 |
| [NCT01805882](https://clinicaltrials.gov/study/NCT01805882) | Phase 2 | Completed | 229 | Pilot study of multiple sofosbuvir-based combination regimens for chronic HCV |
| [NCT03687229](https://clinicaltrials.gov/study/NCT03687229) | N/A | Unknown | 60 | Effect of DAA therapy on miRNA-122 and insulin resistance in chronic HCV patients |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [36045503](https://pubmed.ncbi.nlm.nih.gov/36045503/) | 2023 | Phase 2 open-label | J Med Virol | Only direct HBV-treatment study of LDV/SOF; showed modest HBsAg decline but no strong virologic response in HBV mono-infected subjects |
| [33031326](https://pubmed.ncbi.nlm.nih.gov/33031326/) | 2020 | Case report / review | Medicine | HBV reactivation following successful HCV treatment with sofosbuvir + ribavirin |
| [31632097](https://pubmed.ncbi.nlm.nih.gov/31632097/) | 2019 | Cohort | Infection and Drug Resistance | Management of HBV reactivation post-DAA treatment in HCV-HBV coinfected patients with pretreatment HBeAg seroconversion |
| [29334502](https://pubmed.ncbi.nlm.nih.gov/29334502/) | 2018 | Cohort | J Clin Gastroenterol | Examines risk of HBV reactivation among patients treated with ledipasvir-sofosbuvir for HCV |
| [31542053](https://pubmed.ncbi.nlm.nih.gov/31542053/) | 2019 | Case report | J Med Case Reports | HBV reactivation via immune-escape mutant in an anti-HBc-positive patient during SOF/VEL therapy for HCV |
| [33523503](https://pubmed.ncbi.nlm.nih.gov/33523503/) | 2021 | Prospective observational | J Viral Hepat | HBV reactivation in cancer patients receiving DAAs for HCV treatment |
| [27621502](https://pubmed.ncbi.nlm.nih.gov/27621502/) | 2015 | ADR report | Hospital Pharmacy | Reports HBV reactivation associated with simeprevir + sofosbuvir treatment of HCV |
| [37517414](https://pubmed.ncbi.nlm.nih.gov/37517414/) | 2023 | Review/modelling | Lancet Gastroenterol Hepatol | Global epidemiological modelling of HBV prevalence and care cascade; no drug-specific data |
| [39914746](https://pubmed.ncbi.nlm.nih.gov/39914746/) | 2025 | Review | J Hepatology | Discusses lessons from HCV DAA treatment uptake applicable to future HBV/HDV therapies (not sofosbuvir-specific) |
| [40242313](https://pubmed.ncbi.nlm.nih.gov/40242313/) | 2025 | In vitro model | JHEP Reports | Novel in vitro co-infection system for HBV/HCV/HDV/HEV; methodological tool, not efficacy data |

---

## Norway Market Information

Sofosbuvir currently holds **no marketing authorization in Norway** (`market_status: 未上市`, 0 licenses on record). No approved indication text, dosage form, or product information is available for this evaluation.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Despite the high TxGNN prediction score, the mechanistic basis for sofosbuvir's activity against HBV is not supported — sofosbuvir targets the HCV RdRp, while HBV replicates via a distinct reverse transcriptase pathway. Nearly all indexed clinical and literature evidence involves HCV/HBV coinfection populations where sofosbuvir is treating the HCV component, or describes HBV **reactivation** as an adverse event during HCV therapy. The single HBV mono-infection trial (NCT03312023/PMID 36045503) showed only a modest HBsAg reduction, well short of a clinically meaningful antiviral effect.

**To proceed, the following is needed:**
- Confirmed drug mechanism of action (MOA) data from DrugBank (currently a data gap, DG002)
- TFDA/regulatory label warnings and contraindications (currently a blocking data gap, DG001)
- Mature efficacy results (HBV DNA/HBsAg seroconversion) from further dedicated HBV mono-infection trials, since existing data is a single small Phase 2 study
- Re-evaluation of trial/literature relevance grading to systematically exclude coinfection-safety studies from the efficacy evidence base

**Note:** Among this drug's other predicted indications, **Hepatitis E virus infection** (rank 2, TxGNN score 99.49%, Evidence Level L3, decision stage S1 – "Research Question") shows a stronger biological rationale (in vitro RdRp inhibition, resistance-variant characterization, and case series in ribavirin-refractory transplant patients) and may warrant separate evaluation as a more promising repurposing candidate than HBV.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

