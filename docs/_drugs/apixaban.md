---
layout: default
title: Apixaban
parent: 僅模型預測 (L5)
nav_order: 32
evidence_level: L5
indication_count: 1
---

# Apixaban
{: .fs-9 }

證據等級: **L5** | 預測適應症: **1** 個
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

# Apixaban: From Thromboembolic Disease Prevention to Migraine Disorder

## One-Sentence Summary

Apixaban is a direct oral Factor Xa inhibitor anticoagulant; the evidence pack does not specify its approved indication text, but apixaban is widely classified as a stroke-prevention/VTE anticoagulant.
The TxGNN model predicts it may be effective for **Migraine Disorder**, with a prediction score of **99.02%**,
but currently only **1 indirectly relevant clinical trial** and **4 publications** (mostly case reports) support this direction, and part of the literature actually points in the **opposite** direction.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not specified in evidence pack (apixaban is classified as a Factor Xa inhibitor anticoagulant; no approved-indication text available) |
| Predicted New Indication | Migraine Disorder |
| TxGNN Prediction Score | 99.02% |
| Evidence Level | L4 |
| Norway Market Status | Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available (Data Gap). Based on known information, apixaban belongs to the direct oral anticoagulant (DOAC) class, selectively inhibiting Factor Xa to block the coagulation cascade; its efficacy in thromboembolic disease has been established, but the specific approved indication text is not present in this evidence pack.

The repurposing hypothesis rests on an association between migraine (particularly migraine with aura) and patent foramen ovale (PFO)/microembolism, whereby anticoagulation might reduce paradoxical embolism-triggered cortical spreading depression — the mechanism thought to underlie migraine aura. This provides a plausible mechanistic bridge between an anticoagulant and a neurovascular disorder.

However, the available case-report literature points in the opposite direction: patients whose migraine improved on warfarin experienced *recurrence or worsening* of symptoms after switching to apixaban. This suggests warfarin's apparent anti-migraine effect may act through a pathway other than Factor Xa inhibition (e.g., vitamin K–dependent protein effects or anti-inflammatory action), which apixaban — a selective Factor Xa inhibitor — may not replicate. In other words, the TxGNN model's high score is not currently corroborated by, and is partly contradicted by, real-world case evidence.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00562289](https://clinicaltrials.gov/study/NCT00562289) | Phase 3 | Completed | 664 | CLOSURE-I trial comparing PFO closure vs. anticoagulant (warfarin)/antiplatelet therapy for stroke recurrence prevention. Predates apixaban and does not use apixaban; migraine was not a primary endpoint. Relevance graded **C (indirect)** — population/mechanism overlap only. |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [33402037](https://pubmed.ncbi.nlm.nih.gov/33402037/) | 2021 | Retrospective cohort (small, n=75) | Lupus | Antithrombotic therapy trialed in refractory migraine patients with antiphospholipid antibodies; some symptomatic improvement reported, but not apixaban-specific. |
| [28960288](https://pubmed.ncbi.nlm.nih.gov/28960288/) | 2017 | Case Report | Headache | Migraine with aura in full remission for 12 years on warfarin; symptoms **returned within 3 weeks of switching to apixaban** and resolved again on warfarin resumption — evidence *against* apixaban efficacy. |
| [37582651](https://pubmed.ncbi.nlm.nih.gov/37582651/) | 2023 | Case Report | The Neurologist | Migraine with aura **worsened after starting apixaban**; literature review of DOAC effects on headache frequency/severity, noting current evidence is scarce and controversial. |
| [29611190](https://pubmed.ncbi.nlm.nih.gov/29611190/) | 2018 | Case Report | Headache | Vestibular migraine resolving on warfarin and topiramate; apixaban not evaluated in this case. |

---

## Norway Market Information

Apixaban currently has no marketing authorization on record in Norway in this evidence pack (market status: Not Marketed; 0 authorizations).

---

## Safety Considerations

Please refer to the package insert for safety information. Key warnings, contraindications, and drug-drug interaction data are not currently available in this evidence pack (flagged as Blocking data gap, DG001 — TFDA/label warnings pending retrieval).

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN score is high, but the only clinical trial identified does not directly study apixaban or migraine, and the strongest available literature (case reports) actually shows migraine **worsening** when switching from warfarin to apixaban — directly conflicting with the model's prediction. Evidence level is L4 (mechanism/case-level only), insufficient to support advancing past S0.

**To proceed, the following is needed:**
- Complete MOA data (DG002) to properly evaluate the Factor Xa–migraine mechanistic link
- TFDA/label safety data (DG001) — currently blocking S1 safety pre-assessment
- A prospective study or larger cohort specifically evaluating apixaban (not warfarin) in migraine patients
- Reconciliation of the mechanistic hypothesis with the conflicting case-report direction before any further investment
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

