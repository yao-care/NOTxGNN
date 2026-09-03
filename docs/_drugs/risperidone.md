---
layout: default
title: Risperidone
parent: 僅模型預測 (L5)
nav_order: 309
evidence_level: L5
indication_count: 6
---

# Risperidone
{: .fs-9 }

證據等級: **L5** | 預測適應症: **6** 個
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

# Risperidone: From Schizophrenia/Bipolar Disorder to Major Affective Disorder

## One-Sentence Summary

Risperidone is a well-established atypical antipsychotic (serotonin-dopamine antagonist) originally used for schizophrenia and bipolar mania.
The TxGNN model predicts it may also be effective for **Major Affective Disorder** — covering bipolar maintenance and augmentation therapy for treatment-resistant depression —
with **35+ clinical trials** and **20 publications** currently supporting this direction, including multiple completed Phase 3 RCTs.

> Note: TxGNN also flagged five other candidate indications for this drug (see "Other Predicted Indications" below). Three of them are ultra-rare genetic syndromes with no plausible mechanistic link and no supporting trials or literature — these are most likely knowledge-graph noise rather than real signals. This report focuses on the one candidate with substantive clinical evidence.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Schizophrenia / Bipolar Mania (well-established use, referenced within trial records; formal local regulatory text not available) |
| Predicted New Indication | Major Affective Disorder (bipolar disorder & treatment-resistant depression) |
| TxGNN Prediction Score | 99.11% |
| Evidence Level | L1 |
| Norway Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the source records for this drug. Based on known information, risperidone is a second-generation ("atypical") antipsychotic acting as a serotonin-dopamine antagonist (D2 and 5-HT2A receptor antagonism). Its efficacy in schizophrenia and bipolar mania is well established — this is explicitly referenced in trial NCT00277654, which notes risperidone "is currently approved by the United States Food and Drug Administration (FDA) for the treatment of schizophrenia and bipolar mania."

Major affective disorder (bipolar disorder and major depressive disorder) shares overlapping neurobiology with the psychotic and manic states risperidone already treats — dysregulated dopaminergic and serotonergic signaling in cortico-limbic circuits. This mechanistic overlap explains why risperidone has long been used clinically as an adjunct: as monotherapy for bipolar maintenance (preventing manic/depressive relapse) and as an SSRI-augmentation strategy in treatment-resistant depression (TRD), consistent with the broader class effect seen with other second-generation antipsychotics (aripiprazole, quetiapine, olanzapine) approved for MDD augmentation.

The volume and quality of supporting evidence — including large randomized, placebo-controlled Phase 3 trials in both bipolar maintenance (n=585) and TRD augmentation (n=630, n=258) — indicate this is not a speculative model artifact but a reflection of an already-recognized, clinically practiced use pattern.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00095134](https://clinicaltrials.gov/study/NCT00095134) | Phase 3 | Completed | 630 | Double-blind adjunctive risperidone vs. placebo in MDD with sub-optimal response to antidepressant therapy |
| [NCT00044681](https://clinicaltrials.gov/study/NCT00044681) | Phase 3 | Completed | 258 | Efficacy, safety and long-term maintenance of risperidone augmentation of SSRI monotherapy in unipolar treatment-resistant depression |
| [NCT00391222](https://clinicaltrials.gov/study/NCT00391222) | Phase 3 | Completed | 585 | Risperidone long-acting injectable (LAI) monotherapy vs. placebo for prevention of mood episodes in Bipolar I disorder |
| [NCT00057681](https://clinicaltrials.gov/study/NCT00057681) | Phase 3 | Completed | 379 | TEAM study: lithium vs. valproate vs. risperidone for early-onset mania in children/adolescents with bipolar disorder |
| [NCT00277654](https://clinicaltrials.gov/study/NCT00277654) | Phase 3 | Completed | 111 | Randomized, double-blind, placebo-controlled risperidone monotherapy in bipolar disorder with comorbid anxiety |
| [NCT00167479](https://clinicaltrials.gov/study/NCT00167479) | Phase 4 | Completed | 60 | Risperidone monotherapy for bipolar disorder with moderate-to-severe anxiety; efficacy, tolerability and safety |
| [NCT00203723](https://clinicaltrials.gov/study/NCT00203723) | Phase 4 | Terminated | 45 | Combined ECT + risperidone vs. ECT alone for treatment-resistant depression |
| [NCT00176202](https://clinicaltrials.gov/study/NCT00176202) | Phase 3 | Completed | 65 | Risperidone vs. divalproex sodium in pediatric bipolar disorder, with MRI-based circuitry assessment |
| [NCT00221403](https://clinicaltrials.gov/study/NCT00221403) | Phase 3 | Completed | 46 | Placebo-controlled trial of valproate and risperidone in young children (ages 3-7) with bipolar disorder |
| [NCT01282632](https://clinicaltrials.gov/study/NCT01282632) | Phase 1/2 | Completed | 42 | Pilot trial: risperidone vs. olanzapine as add-on to failed SSRI therapy in treatment-resistant depression |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [17975181](https://pubmed.ncbi.nlm.nih.gov/17975181/) | 2007 | RCT | Annals of Internal Medicine | Randomized trial of risperidone augmentation for treatment-refractory major depressive disorder |
| [34986373](https://pubmed.ncbi.nlm.nih.gov/34986373/) | 2022 | Systematic Review + NMA | J Affective Disorders | Network meta-analysis comparing augmentation agents (including risperidone) for treatment-resistant depression |
| [35861202](https://pubmed.ncbi.nlm.nih.gov/35861202/) | 2023 | Systematic Review + Meta-analysis | J Psychopharmacology | Augmentation/combination treatments for early-stage treatment-resistant depression |
| [24919175](https://pubmed.ncbi.nlm.nih.gov/24919175/) | 2014 | Meta-analysis | Braz J Med Biol Res | Efficacy/tolerability of atypical antipsychotic augmentation (17 trials, 3807 patients) of antidepressants in MDD |
| [23554581](https://pubmed.ncbi.nlm.nih.gov/23554581/) | 2013 | Meta-analysis | PLoS Medicine | Risk-benefit profile of adjunctive atypical antipsychotics for depression |
| [35510505](https://pubmed.ncbi.nlm.nih.gov/35510505/) | 2023 | Systematic Review + Meta-analysis | Psychological Medicine | Efficacy and safety/tolerability of antipsychotics (mono- and adjunctive) in adult MDD |
| [21154393](https://pubmed.ncbi.nlm.nih.gov/21154393/) | 2010 | Cochrane Review | Cochrane Database Syst Rev | Second-generation antipsychotics added to antidepressants for MDD and dysthymia |
| [25295435](https://pubmed.ncbi.nlm.nih.gov/25295435/) | 2014 | Nationwide Population-Based Study | J Clinical Psychiatry | Real-world effectiveness of SGA (including risperidone) augmentation for MDD |
| [21189367](https://pubmed.ncbi.nlm.nih.gov/21189367/) | 2011 | Review | Annals of Pharmacotherapy | Efficacy and safety of risperidone augmentation in major depressive disorder |
| [20486830](https://pubmed.ncbi.nlm.nih.gov/20486830/) | 2010 | Review | Expert Opin Pharmacotherapy | Risperidone LAI as monotherapy and adjunctive therapy for maintenance treatment of bipolar I disorder |

---

## Other Predicted Indications (Lower Priority / Screened Out)

The Evidence Pack also flagged five additional candidates. These are summarized for transparency but are not recommended for further action at this time:

| Rank | Disease | TxGNN Score | Evidence Level | Recommendation | Comment |
|------|---------|------|------|------|---------|
| 1 | Gaze palsy, familial horizontal, with progressive scoliosis | 99.76% | L5 | Hold | ROBO3-related skeletal/neurological disorder; no plausible mechanistic link to D2/5-HT2A antagonism. Likely graph noise. |
| 2 | Asperger syndrome, susceptibility to | 99.74% | L5 | Hold | Risperidone is used off-label for irritability in autism spectrum disorder, but this entry is a "susceptibility" label, not a treatable clinical diagnosis, and has zero supporting trials/literature. |
| 3 | Amelocerebrohypohidrotic syndrome | 99.69% | L5 | Hold | Ultra-rare genetic syndrome (enamel/CNS/sweat gland). No known pathophysiological connection. Likely graph noise. |
| 4 | Phelan-McDermid syndrome | 99.59% | L4 | Research Question | SHANK3-related neurodevelopmental disorder with comorbid ASD/bipolar features; risperidone is used clinically for comorbid behavioral/mood symptoms, but evidence is limited to case reports and a preclinical zebrafish model. |
| 5 | Trichotillomania | 99.51% | L3 | Research Question | Multiple case reports/series (1997–2025) support risperidone as an SSRI-augmentation strategy for treatment-resistant hair-pulling disorder, but no RCTs exist. |

---

## Safety Considerations

Please refer to the package insert for safety information. No structured warnings, contraindications, or drug-interaction data were available in this Evidence Pack (flagged as a **Blocking** data gap — see Conclusion below).

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Major affective disorder is supported by an unusually strong evidence base for a TxGNN-predicted indication — multiple completed Phase 3 RCTs in both bipolar maintenance and treatment-resistant depression augmentation, corroborated by systematic reviews, network meta-analyses, and a Cochrane review. This reflects an already-recognized clinical use pattern rather than a novel, unvalidated hypothesis. However, this drug is not currently marketed in this jurisdiction, and critical safety documentation is missing, so proceeding requires explicit guardrails rather than an unconditional go.

**To proceed, the following is needed:**
- TFDA/local package insert warnings and contraindications (currently a **Blocking** data gap — required before any safety screening can begin)
- Confirmed mechanism of action documentation from DrugBank (currently a **High**-severity data gap)
- A defined local regulatory pathway, since the drug currently has zero authorizations and "Not Marketed" status
- Safety monitoring plan addressing known antipsychotic-class risks (metabolic syndrome, extrapyramidal symptoms, prolactin elevation) given the drug's established but currently undocumented safety profile
- Further prospective/controlled evidence for the lower-tier candidates (trichotillomania, Phelan-McDermid syndrome) before considering escalation beyond "Research Question" status
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

