---
layout: default
title: Tasimelteon
parent: 僅模型預測 (L5)
nav_order: 339
evidence_level: L5
indication_count: 10
---

# Tasimelteon
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

# Tasimelteon: From Non-24-Hour Sleep-Wake Disorder to Insomnia

## One-Sentence Summary

> Tasimelteon is a selective MT1/MT2 melatonin receptor agonist originally developed and approved for Non-24-Hour Sleep-Wake Disorder in circadian rhythm regulation.
> The TxGNN model predicts it may also be effective for **Insomnia**,
> with **4 clinical trials** (including one completed Phase 3 RCT) and **6 supporting publications** currently backing this direction.

*(Note: TxGNN's single highest-scoring prediction, "bilateral parasagittal parieto-occipital polymicrogyria," is flagged in the evidence pack itself as a likely embedding-similarity artifact with zero supporting clinical or literature evidence — it is not carried forward into this report. Insomnia is the highest-scored prediction with substantive clinical evidence and is the focus below.)*

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Non-24-Hour Sleep-Wake Disorder (per repurposing rationale; not formally documented in Norway market records) |
| Predicted New Indication | Insomnia (disease) |
| TxGNN Prediction Score | 99.47% |
| Evidence Level | L1 |
| Norway Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Currently, detailed structured mechanism of action (MOA) data is not available from DrugBank for this evidence pack. Based on the repurposing rationale attached to this prediction, tasimelteon is a **selective MT1/MT2 melatonin receptor agonist** that acts directly on the suprachiasmatic nucleus (SCN) to regulate circadian rhythm. This is the same core mechanism that underlies its approved use in Non-24-Hour Sleep-Wake Disorder.

Non-24-Hour Sleep-Wake Disorder and Insomnia are both circadian/sleep-onset disturbances, and mechanistically the same MT1/MT2 agonism that resets the circadian pacemaker and promotes sleep onset is directly applicable to insomnia. This is not a distant repurposing leap — it is an extension within the same pharmacological class and target population, similar to how ramelteon (another MT1/MT2 agonist) is already approved for insomnia.

The supporting literature further reinforces this: multiple reviews describe tasimelteon alongside ramelteon and agomelatine as melatonergic agonists effective for insomnia and circadian rhythm sleep-wake disorders, with mechanism of action centered on sleep-onset latency reduction and circadian phase-shifting demonstrated in prior Phase 2/3 trials.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00548340](https://clinicaltrials.gov/study/NCT00548340) | Phase 3 | Completed | 322 | Randomized, double-blind, placebo-controlled trial of tasimelteon (VEC-162) 20mg/50mg vs. placebo for primary insomnia; direct efficacy/safety evaluation. |
| [NCT06953869](https://clinicaltrials.gov/study/NCT06953869) | Phase 3 | Recruiting | 420 | Multicenter, double-blind RCT evaluating tasimelteon vs. placebo for pediatric insomnia disorder; ongoing, not yet completed. |
| [NCT03291041](https://clinicaltrials.gov/study/NCT03291041) | Phase 2 | Completed | 25 | Proof-of-concept study of tasimelteon vs. placebo in travelers with jet lag disorder, a related circadian sleep disturbance. |
| [NCT05922995](https://clinicaltrials.gov/study/NCT05922995) | Early Phase 1 | Terminated | 20 | Open-label pilot evaluating tasimelteon 20mg in REM Behavior Disorder, with insomnia symptoms assessed via ISI/PSQI/ESS; low evidentiary value (terminated, small n). |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [25207602](https://pubmed.ncbi.nlm.nih.gov/25207602/) | 2014 | Review | Int J Mol Sci | Reviews therapeutic efficacy and safety of melatonin receptor agonists (including tasimelteon) for insomnia and circadian rhythm sleep-wake disorders. |
| [19557144](https://pubmed.ncbi.nlm.nih.gov/19557144/) | 2009 | Review | Neuropsychiatr Dis Treat | Describes melatoninergic agonist mechanism (MT1/MT2, SCN) as fundamentally distinct from GABAergic hypnotics, favoring sleep initiation and circadian resetting. |
| [35585820](https://pubmed.ncbi.nlm.nih.gov/35585820/) | 2023 | Review | Curr Drug Saf | Discusses melatonin/tasimelteon relevance to insomnia and behavioral symptoms in neurodegenerative disease context. |
| [24228714](https://pubmed.ncbi.nlm.nih.gov/24228714/) | 2014 | Review | J Med Chem | Reviews MT1/MT2 receptor pharmacology, identifying tasimelteon as a high-affinity nonselective MT1/MT2 agonist relevant to sleep disorder treatment. |
| [22010042](https://pubmed.ncbi.nlm.nih.gov/22010042/) | 2011 | Review | Ther Adv Neurol Disord | Reviews melatonin/analog therapeutic potential for sleep disturbance, including REM sleep behavior disorder overlapping with insomnia symptomatology. |
| [22167135](https://pubmed.ncbi.nlm.nih.gov/22167135/) | 2011 | Review | Neuro Endocrinol Lett | Discusses disrupted sleep chronobiology and therapeutic value of melatonin/melatonergic agents for sleep-wake cycle disorders. |

---

## Norway Market Information

Tasimelteon is currently **not marketed in Norway** (0 authorizations on record). No product license or approved-indication text is available for this evidence pack.

---

## Safety Considerations

Please refer to the package insert for safety information. *(No structured warnings, contraindications, or drug-interaction data were available in this evidence pack — TFDA label data is flagged as a Blocking data gap (DG001) and must be resolved before any safety-stage evaluation proceeds.)*

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
One completed Phase 3 RCT (n=322) directly demonstrates efficacy of tasimelteon in primary insomnia, supported by a mechanistically coherent MT1/MT2 agonist rationale and a second ongoing Phase 3 pediatric RCT (n=420). Evidence is meaningful but not yet duplicated by a second completed Phase 3 trial, and Norway market/safety documentation is entirely absent.

**To proceed, the following is needed:**
- TFDA/Norway package insert data (warnings, contraindications, DDI) — currently a Blocking data gap (DG001)
- Structured DrugBank MOA confirmation (DG002)
- Completion and results of ongoing Phase 3 pediatric insomnia trial (NCT06953869)
- Norway regulatory pathway assessment, since the drug is not currently marketed there (0 licenses)

*Other TxGNN-predicted indications for this drug (ALS and related motor neuron diseases, polymicrogyria, skeletal dysplasia, endogenous depression) were screened but held at L4–L5 evidence level due to absent or purely mechanistic/speculative support, and are not recommended for further action at this time.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

