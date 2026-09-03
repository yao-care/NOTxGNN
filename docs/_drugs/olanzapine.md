---
layout: default
title: Olanzapine
parent: 僅模型預測 (L5)
nav_order: 252
evidence_level: L5
indication_count: 3
---

# Olanzapine
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

# Olanzapine: From Schizophrenia/Bipolar Disorder to Agoraphobia (Treatment-Resistant Panic Disorder)

## One-Sentence Summary

Olanzapine is a well-established atypical antipsychotic used for schizophrenia and bipolar I disorder. Among three TxGNN-predicted new indications in this evidence pack, the most clinically credible signal points to **Agoraphobia**, specifically as an augmentation therapy in treatment-resistant panic disorder, supported by **7 publications** (no dedicated clinical trials yet). Evidence level is **L3**, and a critical safety data gap (TFDA warnings/contraindications) currently blocks full risk assessment.

> Note: This evidence pack contains 3 TxGNN-predicted indications for olanzapine. The top TxGNN-ranked prediction ("benign paroxysmal torticollis of infancy") is explicitly flagged in its own rationale as having no mechanistic support and a serious pediatric safety concern, so it is **not** used as the lead indication in this report. See "Other Predicted Indications" below.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the evidence pack. (General pharmacology background: olanzapine is an atypical antipsychotic typically approved for schizophrenia and bipolar I disorder — not sourced from this evidence pack.) |
| Predicted New Indication | Agoraphobia (as augmentation in treatment-resistant panic disorder) |
| TxGNN Prediction Score | 99.47% (rank 5685) |
| Evidence Level | L3 |
| Market Status | ✗ Not marketed (0 authorizations on record) |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed formal MOA data for olanzapine (`original_moa`) is flagged as a data gap in this evidence pack (DG002). Based on the mechanistic rationale extracted from the literature evidence itself, olanzapine acts as a **D2/5-HT2A receptor antagonist**. This dual dopaminergic-serotonergic modulation is theorized to reduce anxiety and catastrophic cognitive interpretation in patients with treatment-resistant panic disorder and agoraphobia.

Critically, the literature does **not** support olanzapine as monotherapy for agoraphobia. Rather, the strongest study (Sepede et al., 2006, 12-week open-label fixed-dose trial) evaluated low-dose olanzapine (5 mg/d) as an **add-on to SSRIs** in patients who had already failed SSRI monotherapy. This is consistent with the broader literature theme: olanzapine augmentation in SSRI/SNRI-resistant panic disorder with agoraphobia, not first-line or standalone treatment.

Because the original approved use (schizophrenia/bipolar disorder) and the predicted new use (anxiety/panic-spectrum disorder) both involve modulation of dopaminergic-serotonergic circuitry implicated in mood and anxiety regulation, the mechanistic extension to a treatment-resistant anxiety indication is biologically plausible, though it remains supported only by small open-label and case-level evidence rather than confirmatory RCTs.

---

## Clinical Trial Evidence

Currently no related clinical trials registered

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [16415705](https://pubmed.ncbi.nlm.nih.gov/16415705/) | 2006 | Open-label trial (12-week, fixed-dose) | Journal of Clinical Psychopharmacology | Low-dose olanzapine (5 mg/d) added to SSRI in 31 SSRI-resistant panic disorder patients (with/without agoraphobia); assessed via Panic Attack and Anticipatory Anxiety Scale |
| [40946318](https://pubmed.ncbi.nlm.nih.gov/40946318/) | 2025 | Integrative Systematic Review | Psychotherapy and Psychosomatics | Reviews pharmacological, psychotherapeutic, and neurostimulatory options for treatment-resistant anxiety disorders |
| [26635099](https://pubmed.ncbi.nlm.nih.gov/26635099/) | 2016 | Systematic Review | Expert Opinion on Pharmacotherapy | Reviews treatment options for treatment-resistant panic disorder, a population with persistent symptoms despite standard therapy |
| [25012437](https://pubmed.ncbi.nlm.nih.gov/25012437/) | 2014 | Cohort (24-month naturalistic outcome) | Journal of Affective Disorders | Comorbid agoraphobia/panic/OCD/GAD worsen 24-month clinical outcomes in bipolar I disorder |
| [10739446](https://pubmed.ncbi.nlm.nih.gov/10739446/) | 2000 | Case Report | The American Journal of Psychiatry | Early case report describing olanzapine's effect on panic attacks |
| [15470803](https://pubmed.ncbi.nlm.nih.gov/15470803/) | 2004 | Case Report | Pharmacopsychiatry | Chronic, treatment-refractory panic disorder patient remitted on olanzapine + paroxetine combination |
| [17099612](https://pubmed.ncbi.nlm.nih.gov/17099612/) | 2006 | Case Report (CBT case series) | Psychiatria Danubina | Case of comorbid panic disorder with agoraphobia and psychosis, successfully treated with CBT; olanzapine context discussed |

---

## Norway Market Information

Not currently marketed. The evidence pack lists **0 authorizations**, so no license table is available.

---

## Safety Considerations

Please refer to the package insert for safety information.

> ⚠ **Blocking Data Gap (DG001):** TFDA-equivalent label warnings and contraindications for olanzapine are not available in this evidence pack. This is flagged as a *Blocking* severity gap — it prevents this candidate from progressing to the S1 safety review stage. No drug-drug interaction data was found (`query_status: not_found`).

---

## Other Predicted Indications (Lower Priority)

| Rank | Indication | TxGNN Score | Evidence Level | Recommendation | Note |
|------|-----------|------------|----------------|-----------------|------|
| 1 | Benign paroxysmal torticollis of infancy | 99.54% | L5 | Hold | No mechanistic link identified; this is a pediatric migraine-spectrum condition with no pathophysiological connection to D2/5-HT2A antagonism. Using an antipsychotic in infants raises serious safety concerns. TxGNN score reflects graph-based association only, not clinical plausibility. |
| 3 | Dysthymic disorder | 99.28% | L4 | Hold | Evidence is indirect — one open-label trial in comorbid borderline personality disorder + dysthymia, plus class-level (second-generation antipsychotic) reviews for MDD/dysthymia, and unrelated-drug (amisulpride, substituted benzamides) evidence. No olanzapine-specific controlled trial for dysthymia exists. |

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The agoraphobia signal has the most credible mechanistic and literature support among the three predicted indications (D2/5-HT2A augmentation therapy in SSRI-resistant panic disorder/agoraphobia), but it rests on evidence level L3 with no controlled trials — only one 12-week open-label study and several case reports/reviews. More importantly, the **blocking data gap on TFDA safety information (DG001)** means this candidate cannot yet pass initial safety screening (S1), regardless of the promising efficacy signal.

**To proceed, the following is needed:**
- Resolve DG001: obtain TFDA-equivalent label (warnings, contraindications) via official regulatory source
- Resolve DG002: obtain formal MOA/pharmacology data via DrugBank API
- Identify or commission a controlled trial (RCT) specifically evaluating olanzapine augmentation in treatment-resistant agoraphobia/panic disorder
- If pursuing lower-ranked predictions (dysthymic disorder, torticollis), first establish a credible mechanistic rationale and pediatric-specific safety data before any further evaluation
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

