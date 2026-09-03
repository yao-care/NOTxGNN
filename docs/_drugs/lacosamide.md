---
layout: default
title: Lacosamide
parent: 僅模型預測 (L5)
nav_order: 196
evidence_level: L5
indication_count: 10
---

# Lacosamide
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

# Lacosamide: From Epilepsy to Manic Bipolar Affective Disorder

## One-Sentence Summary

Lacosamide is an antiepileptic drug used for partial-onset (focal) seizures, acting via selective enhancement of slow inactivation of voltage-gated sodium channels. The TxGNN model's top-ranked prediction is efficacy in **manic bipolar affective disorder**, but the supporting evidence base — **1 clinical trial** and **14 publications** — is thin and largely addresses bipolar *depression* rather than the manic phase specifically predicted. This is a mechanistically plausible but evidence-mismatched signal that requires further clarification before advancing.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Epilepsy (partial-onset/focal seizures) — inferred from antiepileptic drug classification in the evidence pack; no Norway-approved indication text available (drug not marketed) |
| Predicted New Indication | Manic Bipolar Affective Disorder |
| TxGNN Prediction Score | 99.96% (rank 711) |
| Evidence Level | L3 |
| Norway Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

The structured `original_moa` field for lacosamide is marked as a data gap. However, literature within this evidence pack describes lacosamide's mechanism as selective enhancement of the *slow* inactivation state of voltage-gated sodium channels, producing extended neuronal membrane stabilization (PMID 28845834). This is the same general mechanistic class shared by established mood stabilizers such as lamotrigine and valproate, both of which have approved or well-documented roles in bipolar disorder — providing a plausible pharmacological rationale for exploring lacosamide as a mood stabilizer.

That said, there is a notable **evidence-direction mismatch**. The only registered trial (NCT07412132) explicitly targets "Major Depressive Episodes of Bipolar Disorder," not mania, and is justified by prior open-label data on depressive/manic symptom improvement rather than a manic-specific hypothesis. The retrospective and open-label literature identified (PMID 30251375, 33666402) similarly focuses on bipolar *depression*. One case report (PMID 30275630) documents lacosamide-precipitated neutropenia in a bipolar patient — an unrelated safety signal rather than efficacy evidence.

In short: the sodium-channel mood-stabilizing rationale is biologically reasonable by analogy to other AEDs used in bipolar disorder, but no identified study directly evaluates lacosamide for the *manic* phase specifically flagged by TxGNN. The prediction should be treated as a hypothesis-generating signal, not a validated indication.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT07412132](https://clinicaltrials.gov/study/NCT07412132) | Phase 3 | Recruiting | 40 | Evaluates lacosamide as augmentation therapy for **major depressive episodes** in Bipolar I/II disorder (not manic episodes); rationale drawn from earlier open-label observations of improved depressive/manic symptoms in epilepsy and BD populations |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [30251375](https://pubmed.ncbi.nlm.nih.gov/30251375/) | 2018 | Retrospective cohort | Psychiatry Clin Neurosci | 30-day comparison of lacosamide vs. other antiepileptics in bipolar disorder patients without epilepsy — first direct lacosamide-in-BD data |
| [33666402](https://pubmed.ncbi.nlm.nih.gov/33666402/) | 2021 | Open-label pilot trial | J Clin Psychopharmacol | 12-week pilot trial of lacosamide specifically for bipolar **depression** |
| [28845834](https://pubmed.ncbi.nlm.nih.gov/28845834/) | 2017 | Case report | Acta Biomed | Clinical mood stabilization with lacosamide in a patient with comorbid PTSD and fronto-temporal epilepsy; describes slow Na+ channel inactivation mechanism |
| [30275630](https://pubmed.ncbi.nlm.nih.gov/30275630/) | 2018 | Case report (adverse event) | Indian J Psychol Med | Lacosamide-precipitated neutropenia in a bipolar disorder patient with comorbid epilepsy — safety signal |
| [38304661](https://pubmed.ncbi.nlm.nih.gov/38304661/) | 2024 | Case report | Cureus | Complex case of bipolar I disorder with multiple comorbidities including seizure-like activity |
| [40777679](https://pubmed.ncbi.nlm.nih.gov/40777679/) | 2025 | Case report | Cureus | Xylazine withdrawal in a patient with comorbid bipolar disorder; largely tangential to efficacy |
| [32693579](https://pubmed.ncbi.nlm.nih.gov/32693579/) | 2020 | Mechanistic review | ACS Chem Neurosci | CRMP2 druggability review — relevant to lacosamide's secondary (non-Nav) mechanism |
| [37782796](https://pubmed.ncbi.nlm.nih.gov/37782796/) | 2023 | Structural/mechanistic | PNAS | Cryo-EM structural basis of Nav channel inhibition by AEDs (lamotrigine), supporting class mechanism relevant to lacosamide |
| [29957667](https://pubmed.ncbi.nlm.nih.gov/29957667/) | 2018 | Review | Ther Drug Monit | TDM update on AEDs, notes expanding use of AEDs beyond epilepsy including bipolar disorder |
| [22210279](https://pubmed.ncbi.nlm.nih.gov/22210279/) | 2012 | Review | Adv Drug Deliv Rev | Chemical/pharmacokinetic properties of newer AEDs including lacosamide — background pharmacology only |

---

## Norway Market Information

Lacosamide currently holds **no marketing authorization in Norway** (market status: Not Marketed; 0 authorizations on file as of data cutoff 2026-09-03). No product-level licensing or approved indication text is available for extraction.

---

## Safety Considerations

Please refer to the package insert for safety information.

*(Note: Structured warnings, contraindications, and DDI data were not retrievable for this evidence pack — flagged as a Blocking data gap (DG001) requiring TFDA/Norway label sourcing before any safety-relevant decision.)*

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The mechanistic rationale (sodium-channel-mediated mood stabilization, paralleling lamotrigine/valproate) is plausible, but the only completed/ongoing evidence addresses bipolar **depression**, not the manic phase specifically predicted by TxGNN. With only L3 evidence, a single small (n=40), still-recruiting, non-manic-specific trial, and no formal safety labeling available, the evidence does not yet support proceeding.

**To proceed, the following is needed:**
- Direct clinical evidence (trial or retrospective analysis) evaluating lacosamide specifically in manic/hypomanic episodes, not only bipolar depression
- Resolution of Blocking gap DG001 (TFDA/Norway warnings and contraindications) before any S1 safety screening can occur
- Formal MOA documentation from DrugBank (High-priority gap DG002)
- Confirmation of Norway market/import pathway, given the drug currently has no local authorization

**Additional note:** Among the 10 TxGNN-predicted indications evaluated for lacosamide in this evidence pack, **migraine disorder** (rank 5) shows substantially stronger evidence — Evidence Level L1, including a completed head-to-head Phase 3 RCT vs. propranolol (n=600) and mechanistic CGRP-lowering data — and carries a "Proceed with Guardrails" recommendation. This candidate may warrant a separate, dedicated evaluation report.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

