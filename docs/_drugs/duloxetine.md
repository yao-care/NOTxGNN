---
layout: default
title: Duloxetine
parent: 僅模型預測 (L5)
nav_order: 43
evidence_level: L5
indication_count: 10
---

# Duloxetine
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

Using the report as directly specified by the provided evaluation-report prompt/template (this is a report-authoring task with its own embedded instructions, not a coding task — no other skill applies).

Note on candidate selection: `predicted_indications` is sorted by raw TxGNN score, not by evidence quality. Rank 1 ("benign paroxysmal torticollis of infancy") and ranks 4–10 all carry **L5 / Hold**, zero trials, zero literature, and the pack's own rationale explicitly flags them as likely knowledge-graph noise. The only candidate with real clinical and literature support is **rank 3 — Obsessive-Compulsive Disorder (L2 / S2 / Proceed with Guardrails)**. As a repurposing evaluation, that is the candidate worth reporting on; the report below is built on it, with the low-evidence candidates summarized briefly at the end for completeness.

---

# Duloxetine: From Depression/Anxiety Disorders to Obsessive-Compulsive Disorder

## One-Sentence Summary

> Duloxetine is a serotonin-norepinephrine reuptake inhibitor (SNRI) originally used for mood and anxiety disorders (per literature evidence; no formal Norway license record exists, as the drug is currently **not marketed** there).
> The TxGNN model predicts it may also be effective for **Obsessive-Compulsive Disorder (OCD)**,
> with **5 clinical trials** (1 directly on-topic, Phase 4, completed) and **20 publications** — including a double-blind RCT — currently supporting this direction.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available from an official license record (drug not marketed in Norway, 0 licenses). Literature (PMID 31749717) describes duloxetine as approved elsewhere for major depressive disorder, generalized anxiety disorder, diabetic peripheral neuropathic pain, fibromyalgia, and chronic musculoskeletal pain |
| Predicted New Indication | Obsessive-Compulsive Disorder |
| TxGNN Prediction Score | 99.84% |
| Evidence Level | L2 |
| Norway Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in structured form (DrugBank MOA field: Data Gap). Based on known pharmacology, duloxetine is a serotonin-norepinephrine reuptake inhibitor (SNRI) whose efficacy in mood and anxiety disorders is well established; mechanistically this dual-reuptake action may extend to OCD.

The current first-line pharmacotherapy for OCD is SSRIs (serotonin-pathway only). Duloxetine's SNRI mechanism adds enhanced noradrenergic transmission on top of the serotonergic effect, which provides a theoretical basis for use as an **augmentation or alternative option in patients who do not respond adequately to standard serotonin reuptake inhibitors (SRIs)**.

This extension is not purely theoretical: a double-blind controlled trial (PMID 27811556) demonstrated an augmentation benefit, a completed Phase 4 trial (NCT00464698) was specifically designed to test duloxetine in OCD, and multiple open-label studies, case series, and reviews reinforce the signal. Taken together, the mechanistic extension has moderate-to-high plausibility, but it remains an **off-label extension** — it is not an original approved indication, and no large Phase 3 monotherapy RCT exists yet.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00464698](https://clinicaltrials.gov/study/NCT00464698) | Phase 4 | Completed | 20 | Directly designed to assess duloxetine efficacy in OCD; small sample, no placebo arm reported in summary |
| [NCT01404871](https://clinicaltrials.gov/study/NCT01404871) | N/A | Completed | 26 | Predicts differential medication response in OCD (clomipramine, escitalopram, or duloxetine); relevant population but not a pure efficacy trial |
| [NCT02476136](https://clinicaltrials.gov/study/NCT02476136) | N/A | Unknown | 8,800 | Large IPD meta-analysis of antidepressant efficacy across anxiety disorders by baseline severity; may include OCD subgroup but not OCD-specific |
| [NCT01944657](https://clinicaltrials.gov/study/NCT01944657) | N/A | Withdrawn | 0 | TMS vs. medication monotherapy for major depression — withdrawn, no enrollment; low relevance to OCD (database keyword overlap only) |
| [NCT05930912](https://clinicaltrials.gov/study/NCT05930912) | N/A | Unknown | 1 | Psychoanalytic treatment case study in autism spectrum disorder; N=1, low relevance (keyword overlap only) |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [27811556](https://pubmed.ncbi.nlm.nih.gov/27811556/) | 2016 | RCT | J Clin Psychopharmacol | Double-blind controlled trial evaluating duloxetine **augmentation** in treatment-resistant OCD |
| [25637377](https://pubmed.ncbi.nlm.nih.gov/25637377/) | 2015 | Open-label | Int J Neuropsychopharmacol | Open-label study of duloxetine monotherapy for DSM-IV OCD |
| [18208931](https://pubmed.ncbi.nlm.nih.gov/18208931/) | 2008 | Case series | J Psychopharmacol | Case series switching from SSRIs to duloxetine in resistant OCD, building on the SNRI rationale seen with venlafaxine |
| [21779536](https://pubmed.ncbi.nlm.nih.gov/21779536/) | 2011 | Review | Innov Clin Neurosci | Reviews SNRIs as pharmacological alternatives for OCD when SSRIs/clomipramine are inadequate |
| [16669725](https://pubmed.ncbi.nlm.nih.gov/16669725/) | 2006 | Critical Review | J Clin Psychiatry | Critical review of SNRIs (venlafaxine, clomipramine) in OCD as an alternative to first-line SSRIs |
| [24766145](https://pubmed.ncbi.nlm.nih.gov/24766145/) | 2014 | Review | Expert Opin Pharmacother | Updated review of serotonergic antidepressants, including SNRIs, in OCD pathophysiology and treatment |
| [31749717](https://pubmed.ncbi.nlm.nih.gov/31749717/) | 2019 | Review | Front Psychiatry | Systematic review of duloxetine use beyond MDD/GAD, covering psychiatric indications including OCD |
| [19483491](https://pubmed.ncbi.nlm.nih.gov/19483491/) | 2009 | Case report | Clin Neuropharmacol | High-dose duloxetine in treatment-resistant OCD with sustained full remission |
| [17632660](https://pubmed.ncbi.nlm.nih.gov/17632660/) | 2007 | Case report | Prim Care Companion J Clin Psychiatry | Case of OCD responding to duloxetine treatment |
| [39735048](https://pubmed.ncbi.nlm.nih.gov/39735048/) | 2024 | Case report | Cureus | Supratherapeutic duloxetine combined with CBT in severe treatment-resistant OCD with comorbid depression |

---

## Norway Market Information

Duloxetine currently holds **no marketing authorization in Norway** (0 licenses on record; market status: Not Marketed). No product/dosage-form/indication data is available to tabulate.

---

## Safety Considerations

Please refer to the package insert for safety information. Structured safety data (key warnings, contraindications, drug-drug interactions) is not currently available in this evidence pack — this is flagged as a **Blocking** data gap (DG001: TFDA/package-insert warnings and contraindications) that must be resolved before this candidate can enter the S1 safety review stage.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Duloxetine's SNRI mechanism, supported by a double-blind RCT (PMID 27811556) and a completed Phase 4 trial (NCT00464698) specifically designed around OCD, gives this candidate moderate-to-high plausibility as an augmentation/alternative option for SRI-refractory OCD patients. However, it lacks large Phase 3 monotherapy RCTs, is not a formally approved indication anywhere reviewed, and the drug is not currently marketed in Norway.

**To proceed, the following is needed:**
- TFDA/Norway package-insert warnings and contraindications (Blocking data gap, DG001) — required before any S1 safety evaluation
- Formal mechanism-of-action documentation from DrugBank (High-priority data gap, DG002)
- Drug-drug interaction data (current DDI query status: not_found)
- A larger, controlled monotherapy trial in a primary (non-augmentation) OCD population
- Regulatory pathway/market-access assessment, since duloxetine is not currently marketed in Norway

---

### Appendix: Other Predicted Indications (Not Recommended for Further Action)

The remaining 9 predicted indications for duloxetine all scored **L5 (model prediction only)** with **zero clinical trials and zero literature**, and are recommended **Hold**:

- Agoraphobia (rank 2, L4/S1, "Research Question") — indirect evidence only, via panic disorder/GAD literature; no agoraphobia-specific study
- Benign paroxysmal torticollis of infancy, paranoid/schizotypal/histrionic/schizoid personality disorders, Ohdo syndrome and variants, ligneous conjunctivitis, blepharophimosis–intellectual disability syndrome (Ohdo type) — all L5/Hold, with the evidence pack's own rationale describing these as mechanistically implausible or likely knowledge-graph noise (e.g., Ohdo syndrome and ligneous conjunctivitis have no biological connection to monoamine reuptake inhibition).

These are not recommended for pharmacist reporting or further evaluation at this time.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

