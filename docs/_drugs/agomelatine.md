---
layout: default
title: Agomelatine
parent: 僅模型預測 (L5)
nav_order: 20
evidence_level: L5
indication_count: 10
---

# Agomelatine
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

Using the report as directly requested — this is a self-contained content-generation task against a fully-specified template, not a coding/debugging/creative-design task, so no skill applies here.

One judgment call worth flagging before the report: the evidence pack contains **10** TxGNN-predicted indications for agomelatine, ranked purely by raw model score. The literal #1-ranked candidate ("benign paroxysmal torticollis of infancy") has **zero** clinical trials, **zero** literature, and its own `repurposing_rationale` explicitly states there is no known mechanistic link and recommends **Hold**. Writing a full evaluation report centered on that candidate would be actively misleading. Per the evidence pack's own computed `scoring` fields, the strongest, most defensible candidate is **Melancholia** (rank 4, evidence level L2, decision stage S3, recommendation "Proceed with Guardrails") — a severe MDD subtype mechanistically coherent with agomelatine's established antidepressant profile and backed by agomelatine-specific meta-analyses. I used that as the report's focal predicted indication rather than blindly following array index 0.

---

# Agomelatine: From Major Depressive Disorder to Melancholia

## One-Sentence Summary

> Agomelatine is a melatonergic antidepressant (MT1/MT2 receptor agonist and 5-HT2C receptor antagonist) with an established evidence base in Major Depressive Disorder (MDD).
> The TxGNN model predicts it may be effective for **Melancholia**, a severe/endogenous MDD subtype,
> with **0 dedicated clinical trials** but **20 supporting publications**, several of which are agomelatine-specific meta-analyses and mechanistic reviews.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Major Depressive Disorder (MDD) in adults *(derived from literature, e.g. PMID 19777735; not confirmed by structured regulatory data — Norway license records are unavailable)* |
| Predicted New Indication | Melancholia |
| TxGNN Prediction Score | 99.88% |
| Evidence Level | L2 |
| Norway Market Status | Not Marketed (未上市) |
| Number of Authorizations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

The structured mechanism-of-action field for this drug is a data gap (DG002), but the literature captured in this evidence pack consistently and specifically describes agomelatine's pharmacology: it is a melatonergic MT1/MT2 receptor agonist combined with a 5‑HT2C serotonin receptor antagonist (PMID 23484857, PMID 36097970, PMID 19777735). This dual action resynchronizes disrupted circadian rhythms and enhances dopamine/noradrenaline release in the prefrontal cortex, producing antidepressant, sleep-normalizing, and anxiolytic effects — a mechanism distinct from purely monoaminergic antidepressants (SSRIs/SNRIs/TCAs).

Melancholia is a clinically severe, historically "endogenous" subtype of MDD characterized by pronounced anhedonia, psychomotor disturbance, diurnal mood variation, and marked sleep/circadian disruption. These are precisely the symptom domains agomelatine's circadian-resynchronizing mechanism is designed to address, which is why the two are mechanistically close rather than a novel biological hypothesis. Consistent with this, the literature set includes agomelatine-specific systematic reviews and meta-analyses spanning discovery through clinical use (PMID 32568567 preclinical-to-clinical development; PMID 39684343 and PMID 37960759 efficacy/safety meta-analyses), plus network meta-analyses situating agomelatine among 21 antidepressants for acute MDD treatment (PMID 29477251). No trial or publication in this pack specifically targets "melancholia" as a labeled diagnostic entity — the supporting evidence is drawn from the broader MDD literature in which agomelatine is already a studied agent, so this should be read as an extension within an established therapeutic class rather than an entirely new indication.

A closely related predicted indication, "neurotic depression" (rank 5, also L2/Proceed with Guardrails), shares nearly identical supporting literature and reflects overlapping legacy nosology (older ICD-style classification of the depressive spectrum) rather than a distinct disease mechanism.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [29477251](https://pubmed.ncbi.nlm.nih.gov/29477251/) | 2018 | Network Meta-analysis | Lancet | Compares and ranks 21 antidepressants (including agomelatine) for acute treatment of adult MDD; foundational efficacy/acceptability reference. |
| [39684343](https://pubmed.ncbi.nlm.nih.gov/39684343/) | 2024 | Systematic Review/Meta-analysis | Int J Mol Sci | Agomelatine-specific meta-analysis of efficacy and safety in depressed patients with comorbid diabetes. |
| [37960759](https://pubmed.ncbi.nlm.nih.gov/37960759/) | 2023 | Meta-analysis | Medicine | Systematic assessment of agomelatine efficacy and safety in patients with depressive disorder. |
| [32568567](https://pubmed.ncbi.nlm.nih.gov/32568567/) | 2020 | Review (translational) | Expert Opin Drug Discov | Traces agomelatine's preclinical discovery through clinical development as the first antidepressant with a non-monoaminergic mechanism. |
| [36253442](https://pubmed.ncbi.nlm.nih.gov/36253442/) | 2023 | Systematic Review/Network Meta-analysis | Molecular Psychiatry | Compares antidepressants (agomelatine included) for maintenance-phase treatment of adult MDD using double-blind RCT data. |
| [41135546](https://pubmed.ncbi.nlm.nih.gov/41135546/) | 2025 | Systematic Review/Network Meta-analysis | Lancet | Ranks antidepressants, including agomelatine, on cardiometabolic and physiological side-effect profiles from RCT data. |
| [23484857](https://pubmed.ncbi.nlm.nih.gov/23484857/) | 2013 | Review | Expert Opin Investig Drugs | Reviews the mechanistic link between melatonin/circadian disruption and depressive disorder, framing agomelatine's rationale. |
| [24833894](https://pubmed.ncbi.nlm.nih.gov/24833894/) | 2014 | Review | Patient Prefer Adherence | Reviews efficacy and tolerability of agomelatine in depression treatment, including adherence considerations. |
| [19777735](https://pubmed.ncbi.nlm.nih.gov/19777735/) | 2009 | Review | Med Monatsschr Pharm | Documents 2009 EMEA approval of agomelatine (Valdoxan) for adult MDD and summarizes its melatonergic/5-HT2C mechanism. |
| [25911132](https://pubmed.ncbi.nlm.nih.gov/25911132/) | 2015 | Meta-analysis (RCT-based) | J Affect Disord | Establishes evidence-based antidepressant dose equivalence, including agomelatine, from randomized controlled trials. |

---

## Norway Market Information

Agomelatine currently holds no marketing authorization in Norway (0 licenses on record; market status: Not Marketed).

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Melancholia is mechanistically well-aligned with agomelatine's circadian-resynchronizing, MT1/MT2-agonist/5-HT2C-antagonist profile, and the drug already has a substantial evidence base — including agomelatine-specific meta-analyses — as an antidepressant. However, none of the identified literature or trials specifically studies "melancholia" as a defined diagnostic entity, and no clinical trial evidence exists for this indication, so this remains an extrapolated, not directly validated, extension.

**To proceed, the following is needed:**
- TFDA/local package insert safety data (Blocking data gap DG001 — warnings and contraindications are currently unavailable, precluding a full safety assessment)
- Structured mechanism-of-action confirmation from DrugBank (High-severity data gap DG002)
- Confirmed Norway regulatory/licensing documentation, since the product is not currently marketed there
- A melancholia-specific clinical operational definition aligned to current DSM/ICD criteria, given the term's legacy nosological origin
- Completion of the drug-drug interaction dataset (current query status: not found)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

