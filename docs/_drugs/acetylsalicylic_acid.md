---
layout: default
title: Acetylsalicylic Acid
parent: 僅模型預測 (L5)
nav_order: 17
evidence_level: L5
indication_count: 9
---

# Acetylsalicylic Acid
{: .fs-9 }

證據等級: **L5** | 預測適應症: **9** 個
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

Using the drug-repurposing report template to produce the requested output directly from the evidence pack (no specialized skill applies to this pure content-generation task).

Note up front: I'm treating `predicted_indications[0]` (rank 1: "migraine with brainstem aura") as the primary predicted indication per the template's extraction rules, since that's the array's first entry. The evidence pack also contains 8 additional candidate indications (including a much stronger `thrombotic disease` signal at L1/S3) that fall outside this template's single-indication scope — flagging that here in case a follow-up report on that candidate is wanted.

---

# Acetylsalicylic Acid: From Pain, Fever, and Inflammation to Migraine with Brainstem Aura

## One-Sentence Summary

Acetylsalicylic acid (aspirin) is a long-established analgesic, antipyretic, anti-inflammatory, and antiplatelet agent, though its specific original indication is not documented in the current regulatory dataset. The TxGNN model predicts it may be effective for **Migraine with Brainstem Aura**, a rare migraine subtype, with **0 dedicated clinical trials** but **19 supporting publications**, most of which address migraine or migraine-with-aura broadly rather than this specific subtype.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not documented in the Norway regulatory dataset (no license records on file); generically known as an analgesic, antipyretic, anti-inflammatory, and antiplatelet agent |
| Predicted New Indication | Migraine with Brainstem Aura |
| TxGNN Prediction Score | 99.94% |
| Evidence Level | L3 |
| Norway Market Status | ✗ Not Marketed (未上市) |
| Number of Authorizations | 0 |
| Recommended Decision | Proceed with Guardrails |

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data for acetylsalicylic acid is not available in the current DrugBank extract (flagged in this evidence pack as a High-severity data gap). Based on well-established pharmacology, however, aspirin irreversibly inhibits cyclooxygenase (COX-1/COX-2), blocking prostaglandin and thromboxane A2 synthesis. This reduces platelet aggregation and dampens prostaglandin-mediated neurogenic inflammation and vascular dilation — mechanisms implicated in migraine pathophysiology.

Migraine with aura, including the rarer brainstem-aura subtype, is driven substantially by cortical spreading depression and associated neurogenic-inflammatory/vascular changes. The American Headache Society's evidence assessment already rates aspirin as Level A (well-established) for acute migraine treatment in general, and smaller retrospective and observational studies specifically in migraine-with-aura populations (e.g., a 203-patient retrospective cohort and a dedicated observational case series) suggest a possible prophylactic benefit. Because aspirin is not a vasoconstrictor — unlike triptans — it does not carry the same theoretical contraindication concerns that limit triptan use in brainstem aura.

That said, essentially all of the supporting literature addresses migraine or migraine-with-aura as a whole; no trial or publication in this pack specifically enrolled or confirmed patients with brainstem aura. The rationale is therefore a reasonable mechanistic extrapolation from the broader migraine-with-aura literature, not direct evidence for this specific, rare subtype — consistent with the L3 (observational/no RCT) evidence level assigned.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [10448545](https://pubmed.ncbi.nlm.nih.gov/10448545/) | 1999 | RCT | Cephalalgia | Double-blind, double-dummy, multicenter RCT (n=278): IV lysine acetylsalicylate (≈1g ASA) vs. SC sumatriptan vs. placebo in acute migraine attacks (with or without aura) |
| [26908949](https://pubmed.ncbi.nlm.nih.gov/26908949/) | 2016 | RCT | European Heart Journal | PRIMA trial: randomized evaluation of percutaneous PFO closure in migraine-with-aura patients refractory to medical treatment |
| [25729594](https://pubmed.ncbi.nlm.nih.gov/25729594/) | 2014 | Retrospective Cohort | Current Health Sciences Journal | Retrospective review of 203 migraine-with-aura patients; 46.8% treated with low-dose ASA prophylaxis vs. other standard preventive therapies |
| [29017164](https://pubmed.ncbi.nlm.nih.gov/29017164/) | 2017 | Observational Case Series | European Neurology | Aspirin used specifically as prophylaxis in patients with migraine with aura |
| [39989443](https://pubmed.ncbi.nlm.nih.gov/39989443/) | 2025 | Systematic Review | Headache | Systematic review of antithrombotic drugs, including aspirin, as migraine preventive medication |
| [25600718](https://pubmed.ncbi.nlm.nih.gov/25600718/) | 2015 | Guideline (AHS Evidence Assessment) | Headache | American Headache Society assessment classifies aspirin as Level A evidence for acute migraine pharmacotherapy |
| [30291554](https://pubmed.ncbi.nlm.nih.gov/30291554/) | 2018 | Review | Current Pain and Headache Reports | Reviews pathophysiologic and clinical differences between episodic migraine with and without aura |
| [34384631](https://pubmed.ncbi.nlm.nih.gov/34384631/) | 2021 | Review | Revue Neurologique | Describes cortical spreading depression as the pivotal mechanism underlying migraine aura |
| [11139754](https://pubmed.ncbi.nlm.nih.gov/11139754/) | 2000 | Review | Revue Neurologique | Reviews prophylactic treatment strategies and indications for preventive therapy in migraine |
| [16103551](https://pubmed.ncbi.nlm.nih.gov/16103551/) | 2005 | Case Report | Heart (British Cardiac Society) | Clopidogrel (an antiplatelet agent) reduced migraine-with-aura recurrence after transcatheter PFO/ASD closure |

## Norway Market Information

No marketing authorization records are currently on file for acetylsalicylic acid in Norway (0 licenses; market status "未上市/Not Marketed" in this dataset). Given that aspirin is a globally available generic, this likely reflects a gap in the specific regulatory data source rather than confirmed true market absence — this should be verified directly before any go/no-go decision.

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
- Aspirin has a mechanistically plausible role in migraine with aura — supported by one RCT (IV ASA vs. sumatriptan vs. placebo), a retrospective cohort, and an observational case series specifically studying aspirin in migraine-with-aura patients, plus a Level A general-migraine rating from the American Headache Society. However, no evidence in this pack directly addresses the brainstem-aura subtype, and overall evidence strength is L3 (observational, no dedicated RCT for this indication).

**To proceed, the following is needed:**
- Resolve DG001 (Blocking): obtain TFDA/regulatory package insert warnings and contraindications — currently a complete data gap that blocks entry into the S1 safety pre-screening stage
- Resolve DG002 (High): obtain detailed mechanism-of-action data via the DrugBank API to strengthen the mechanistic-relevance analysis
- Confirm Norway marketing/regulatory status, since 0 authorizations are on record despite aspirin's status as a widely marketed generic drug
- Seek or commission a study specifically enrolling migraine-with-brainstem-aura patients, since current evidence is extrapolated from the broader migraine-with-aura population
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

