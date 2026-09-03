---
layout: default
title: Aripiprazole
parent: 僅模型預測 (L5)
nav_order: 34
evidence_level: L5
indication_count: 10
---

# Aripiprazole
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

# Aripiprazole: From Schizophrenia and Bipolar Disorder to Major Affective Disorder

## One-Sentence Summary

> Aripiprazole is a second-generation antipsychotic historically used for schizophrenia, bipolar I disorder (mania), and adjunctive treatment of major depressive disorder (MDD), among other approved uses.
> The TxGNN model predicts it may be effective for **Major Affective Disorder**,
> with **50 clinical trials** and **20 publications** currently supporting this direction — including multiple completed Phase 3 RCTs and Tier 1 systematic reviews/network meta-analyses.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Schizophrenia, bipolar I disorder (mania), adjunctive treatment of major depressive disorder, and irritability associated with autism (per literature evidence, PMID 21254788). Norway-specific label text is not available in this data pack (see Data Gap DG001). |
| Predicted New Indication | Major Affective Disorder |
| TxGNN Prediction Score | 99.62% |
| Evidence Level | L1 |
| Norway Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data from DrugBank was not available in this data pack (Data Gap DG002). However, based on information embedded in the supporting literature, aripiprazole is a D2/D3 dopamine receptor partial agonist and a 5-HT1A partial agonist / 5-HT2A antagonist. This dopamine–serotonin system modulation has already been clinically demonstrated to be effective in bipolar disorder (mania and maintenance treatment) and in treatment-resistant major depressive disorder, where it is used as an adjunctive therapy to antidepressants.

Because "major affective disorder" as an umbrella term overlaps substantially with aripiprazole's already-documented uses in bipolar depression and MDD augmentation, this prediction largely represents a **re-confirmation of an established pharmacological role** rather than a novel repurposing hypothesis. This distinction matters for interpretation: the strength of the evidence base reflects decades of clinical use in mood disorders, not an early-stage signal.

It should be noted that the `original_indications` field in this evidence pack is empty, so it is not possible to confirm from structured regulatory data alone whether major affective disorder is already an approved indication in some markets. This should be clarified before treating the TxGNN score as a "new" repurposing finding.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00683852](https://clinicaltrials.gov/study/NCT00683852) | Phase 3 | Completed | 225 | Double-blind, placebo-controlled study of adjunctive aripiprazole (reduced dose) added to antidepressant therapy in MDD; direct efficacy evidence |
| [NCT00876343](https://clinicaltrials.gov/study/NCT00876343) | Phase 3 | Completed | 586 | Placebo-controlled, parallel-group study of adjunctive aripiprazole co-administered with SSRI/SNRI in MDD |
| [NCT00105196](https://clinicaltrials.gov/study/NCT00105196) | Phase 3 | Completed | 349 | 14-week randomized, double-blind, placebo-controlled study of adjunctive aripiprazole vs. placebo in MDD with inadequate antidepressant response |
| [NCT02046564](https://clinicaltrials.gov/study/NCT02046564) | Phase 3 | Completed | 412 | ASC-01 (aripiprazole/sertraline combination) vs. sertraline monotherapy in MDD patients with incomplete response |
| [NCT00873795](https://clinicaltrials.gov/study/NCT00873795) | N/A | Completed | 41 | Aripiprazole 2.5 mg + sertraline 50 mg vs. sertraline alone in newly diagnosed MDD; efficacy and tolerability comparison |
| [NCT01567527](https://clinicaltrials.gov/study/NCT01567527) | Phase 3 | Completed | 731 | 52-week randomized, double-blind, placebo-controlled trial of IM depot aripiprazole as maintenance treatment in bipolar I disorder |
| [NCT03423680](https://clinicaltrials.gov/study/NCT03423680) | Phase 3 | Recruiting | 390 | Multicenter, double-blind, placebo-controlled confirmatory study of adjunctive aripiprazole for major depressive episode in bipolar I/II disorder |
| [NCT02918370](https://clinicaltrials.gov/study/NCT02918370) | Phase 3 | Completed | 75 | Randomized, double-blind, placebo-controlled trial of aripiprazole in bipolar disorder with comorbid alcohol use disorder |
| [NCT00110461](https://clinicaltrials.gov/study/NCT00110461) | Phase 3 | Completed | 296 | Safety and efficacy of two aripiprazole doses in child/adolescent bipolar I disorder, manic or mixed episode |
| [NCT00953745](https://clinicaltrials.gov/study/NCT00953745) | N/A | Completed | 43 | PET/fMRI study testing dopaminergic mechanism of adjunctive aripiprazole in treatment-resistant depression |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [34986373](https://pubmed.ncbi.nlm.nih.gov/34986373/) | 2022 | Systematic Review/NMA | Journal of Affective Disorders | Network meta-analysis comparing augmentation agents (including aripiprazole) for treatment-resistant depression |
| [38219278](https://pubmed.ncbi.nlm.nih.gov/38219278/) | 2024 | Systematic Review/NMA | Neuropsychopharmacology Reports | Network meta-analysis comparing brexpiprazole vs. aripiprazole vs. placebo in Japanese patients with MDD |
| [38669232](https://pubmed.ncbi.nlm.nih.gov/38669232/) | 2024 | Systematic Review/Meta-analysis of RCTs | PLoS One | Efficacy and safety of aripiprazole or bupropion augmentation/switching in TRD/MDD |
| [36961650](https://pubmed.ncbi.nlm.nih.gov/36961650/) | 2023 | RCT | CNS Drugs | Safety, tolerability, and PK of a 2-month long-acting injectable aripiprazole formulation in schizophrenia/bipolar I disorder |
| [34167174](https://pubmed.ncbi.nlm.nih.gov/34167174/) | 2021 | Systematic Review/Meta-analysis | Primary Care Companion for CNS Disorders | Long-term (≥6 months) efficacy and tolerability of adjunctive aripiprazole for MDD |
| [35510505](https://pubmed.ncbi.nlm.nih.gov/35510505/) | 2023 | Systematic Review/Meta-analysis | Psychological Medicine | Efficacy and safety/tolerability of antipsychotics (monotherapy and adjunctive) in adult MDD |
| [35861202](https://pubmed.ncbi.nlm.nih.gov/35861202/) | 2023 | Systematic Review/Meta-analysis | Journal of Psychopharmacology | Augmentation and combination treatments for early-stage treatment-resistant depression |
| [36239033](https://pubmed.ncbi.nlm.nih.gov/36239033/) | 2023 | RCT | Journal of Psychopharmacology | Randomized, double-blind, placebo-controlled trial of adjunctive aripiprazole for MDD with somatic symptoms, with EEG evidence |
| [37149344](https://pubmed.ncbi.nlm.nih.gov/37149344/) | 2023 | Review | The Psychiatric Clinics of North America | Overview of pharmacotherapy for treatment-resistant depression, including atypical antipsychotics such as aripiprazole |
| [21254788](https://pubmed.ncbi.nlm.nih.gov/21254788/) | 2011 | Review | CNS Drugs | Overview of aripiprazole's regulatory history and clinical trial data as adjunctive therapy for MDD |

---

## Norway Market Information

Aripiprazole is currently **not marketed** in Norway according to this data pack, and no marketing authorization records are available (total authorizations: 0).

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The evidence level is L1, supported by multiple completed Phase 3 RCTs and Tier 1 systematic reviews/network meta-analyses demonstrating adjunctive aripiprazole efficacy in MDD and bipolar depression. However, because the drug's original approved indications overlap substantially with the predicted indication, this should be treated as reinforcing an established clinical role rather than a novel repurposing signal, and Norway-specific regulatory and safety data are currently missing.

**To proceed, the following is needed:**
- TFDA/Norway package insert warnings, contraindications, and DDI data (Data Gap DG001, currently blocking S1 safety review)
- Confirmed DrugBank mechanism of action data (Data Gap DG002)
- Clarification of whether major affective disorder (or its component diagnoses) is already an approved indication in any reference market, to correctly classify this as re-confirmation vs. new repurposing
- If pursuing market entry in Norway, a full marketing authorization dossier, as no current license exists
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

