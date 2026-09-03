---
layout: default
title: Lurasidone
parent: 僅模型預測 (L5)
nav_order: 219
evidence_level: L5
indication_count: 10
---

# Lurasidone
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

# Lurasidone: From Bipolar Depression/Schizophrenia to Manic Bipolar Affective Disorder

## One-Sentence Summary

Lurasidone is an atypical antipsychotic internationally approved for schizophrenia and bipolar I depression. The TxGNN model predicts it may also be effective for **manic episodes of bipolar affective disorder**, with **15 clinical trials** and **19 publications** currently supporting the broader bipolar I disorder indication — though very few of these directly address the acute manic phase itself.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not documented in local regulatory filings (drug not marketed); internationally established for schizophrenia and bipolar I depression |
| Predicted New Indication | Manic Bipolar Affective Disorder |
| TxGNN Prediction Score | 99.98% |
| Evidence Level | L1 |
| Norway Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this evidence pack. Based on known pharmacology, lurasidone is a D2/5‑HT2A/5‑HT7 receptor antagonist — a receptor profile shared by other atypical antipsychotics used across the full spectrum of bipolar disorder (manic, mixed, and depressive episodes, as well as maintenance therapy).

Lurasidone's established indications (schizophrenia, bipolar I depression) and the predicted new indication (manic bipolar affective disorder) sit within the same disease category — bipolar I disorder — just different mood phases. Since D2/5‑HT2A antagonism is the pharmacological basis for antimanic efficacy in essentially all approved second-generation antipsychotics, there is reasonable mechanistic plausibility for extending lurasidone's use to the manic phase.

However, the evidence base has an important caveat: the highest-quality completed Phase 3 trials for lurasidone specifically studied **bipolar I depression** and **maintenance/relapse-prevention** (adjunctive to lithium/divalproex), not acute mania as a standalone indication. One review (PMID 31957501) explicitly notes that "lurasidone has not been studied in patients with mania or bipolar psychosis." A dedicated pediatric mania trial (NCT01932541) was withdrawn with zero enrollment. This means the prediction is directionally reasonable (same disease category, same drug class mechanism) but requires confirmatory acute-mania efficacy data before being treated as clinically validated.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT01986114](https://clinicaltrials.gov/study/NCT01986114) | Phase 3 | Completed | 495 | Long-term efficacy and safety of lurasidone (SM-13496) in Bipolar I Disorder — direct drug-disease evidence |
| [NCT01358357](https://clinicaltrials.gov/study/NCT01358357) | Phase 3 | Completed | 965 | PREVAIL series: lurasidone adjunctive to lithium/divalproex for prevention of recurrence in Bipolar I Disorder (with/without rapid cycling or psychotic features) |
| [NCT01914393](https://clinicaltrials.gov/study/NCT01914393) | Phase 3 | Completed | 702 | 104-week open-label extension evaluating long-term safety/effectiveness of flexibly-dosed lurasidone in pediatric subjects |
| [NCT04383691](https://clinicaltrials.gov/study/NCT04383691) | Phase 3 | Terminated | 124 | RCT of lurasidone vs placebo for Bipolar I Depression — terminated, reason not specified in this evidence pack |
| [NCT02046369](https://clinicaltrials.gov/study/NCT02046369) | Phase 3 | Completed | 350 | Efficacy and safety of lurasidone in children/adolescents with Bipolar I Depression |
| [NCT01575561](https://clinicaltrials.gov/study/NCT01575561) | Phase 3 | Completed | 377 | Open-label extension of lurasidone adjunctive to lithium/divalproex in Bipolar I Disorder |
| [NCT02731612](https://clinicaltrials.gov/study/NCT02731612) | Phase 3 | Completed | 100 | ELICE-BD: lurasidone adjunctive therapy for cognitive functioning in euthymic Bipolar I/II patients |
| [NCT02147379](https://clinicaltrials.gov/study/NCT02147379) | Phase 3 | Completed | 53 | Cognitive functioning changes with lurasidone vs treatment-as-usual in euthymic Bipolar I patients |
| [NCT01986101](https://clinicaltrials.gov/study/NCT01986101) | Phase 3 | Completed | 525 | RCT of lurasidone (SM-13496) vs placebo for Bipolar I Depression |
| [NCT01932541](https://clinicaltrials.gov/study/NCT01932541) | Phase 4 | Withdrawn | 0 | Open-label trial of lurasidone specifically for **mania** in children/adolescents — withdrawn before enrollment, no data generated |

*Note: Additional trials in the evidence pack involve other drugs (vortioxetine, cariprazine, ketamine/D-cycloserine) or are only indirectly related (antenatal antipsychotic exposure, SMART trial design) and were excluded from this table as lower relevance (Grade C).*

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [39557452](https://pubmed.ncbi.nlm.nih.gov/39557452/) | 2024 | Systematic Review / Dose-Response Meta-analysis | BMJ Mental Health | Dose-response relationship for lurasidone efficacy, acceptability, and metabolic/endocrine profile in bipolar depression |
| [31957501](https://pubmed.ncbi.nlm.nih.gov/31957501/) | 2020 | Review | Expert Opin Pharmacother | Evaluates lurasidone in bipolar disorder; explicitly notes it has **not** been studied in mania or bipolar psychosis |
| [33177610](https://pubmed.ncbi.nlm.nih.gov/33177610/) | 2021 | Systematic Review / Network Meta-analysis | Molecular Psychiatry | Compares antipsychotics/mood stabilizers (incl. lurasidone) for bipolar disorder maintenance phase |
| [37595997](https://pubmed.ncbi.nlm.nih.gov/37595997/) | 2023 | Network Meta-analysis | Lancet Psychiatry | Comparative efficacy/tolerability of pharmacological interventions for acute bipolar depression |
| [29536616](https://pubmed.ncbi.nlm.nih.gov/29536616/) | 2018 | Guideline (CANMAT/ISBD) | Bipolar Disorders | Standard treatment guideline for bipolar disorder management |
| [34599629](https://pubmed.ncbi.nlm.nih.gov/34599629/) | 2021 | Guideline (CANMAT/ISBD) | Bipolar Disorders | Recommendations for bipolar disorder with mixed presentations (closer to manic/mixed phase) |
| [24170243](https://pubmed.ncbi.nlm.nih.gov/24170243/) | 2014 | Commentary | Am J Psychiatry | "Lurasidone and bipolar disorder" |
| [39243127](https://pubmed.ncbi.nlm.nih.gov/39243127/) | 2024 | Review | Med Sci Monit | Narrative review of new antipsychotics/mood stabilizers for bipolar disorder and schizophrenia, incl. lurasidone |
| [25963405](https://pubmed.ncbi.nlm.nih.gov/25963405/) | 2016 | Review | Asia-Pac Psychiatry | Antipsychotics as antidepressants; notes lurasidone approved specifically for bipolar depression |
| [37815563](https://pubmed.ncbi.nlm.nih.gov/37815563/) | 2023 | Review | JAMA | General diagnosis and treatment review of bipolar disorder |

---

## Norway Market Information

Lurasidone is currently **not marketed** in Norway (market status: 未上市, 0 authorizations). No product license or approved indication text is available for this drug in the local regulatory dataset.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Lurasidone has a substantial body of completed Phase 3 evidence (L1) supporting its use across bipolar I disorder — including depression treatment and maintenance/relapse prevention — which shares mechanistic and diagnostic overlap with the manic phase. However, evidence specifically demonstrating efficacy in **acute mania** is weak (the only dedicated pediatric mania trial was withdrawn), and the drug is not currently marketed locally, so no local safety labeling exists yet.

**To proceed, the following is needed:**
- Local regulatory/package insert data (warnings, contraindications, DDI) — currently blocking (DG001)
- Confirmed mechanism of action detail from DrugBank (DG002)
- Dedicated efficacy/safety data for lurasidone in acute manic or mixed episodes (current evidence is predominantly for the depressive/maintenance phase)
- Regulatory pathway assessment for market entry, since lurasidone holds zero authorizations in this market
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

