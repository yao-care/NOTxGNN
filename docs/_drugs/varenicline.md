---
layout: default
title: Varenicline
parent: 僅模型預測 (L5)
nav_order: 379
evidence_level: L5
indication_count: 10
---

# Varenicline
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

# Varenicline: From Smoking Cessation to Migraine Disorder

## One-Sentence Summary

Varenicline is a nicotinic acetylcholine receptor (nAChR) partial agonist historically developed and used as an aid for smoking cessation. The TxGNN model predicts it may be effective for **Migraine Disorder**, but this prediction is currently supported only by a single, unrelated case report — **no clinical trials and no literature directly investigating varenicline for migraine exist** — and other evidence in this dataset shows headache is a recognized *adverse effect* of varenicline rather than a treatment effect.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Smoking cessation (nicotine dependence treatment) — inferred from literature evidence; no Norway regulatory license data available |
| Predicted New Indication | Migraine disorder |
| TxGNN Prediction Score | 99.92% |
| Evidence Level | L5 |
| Norway Market Status | ✗ Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available (Data Gap). Based on known pharmacology, varenicline is a partial agonist at α4β2 nicotinic acetylcholine receptors and a full agonist at α7 nAChRs; its efficacy in smoking cessation is well established across dozens of RCTs. Nicotinic receptors are expressed in the trigeminovascular system and central pain-modulating pathways, which is the theoretical basis TxGNN appears to be using to link varenicline to migraine.

However, this mechanistic link is speculative and the direction of effect is genuinely ambiguous. Nicotinic agents have been reported to *both* trigger and potentially modulate headache-type symptoms, and the dataset itself contains a case report explicitly titled "Bath-related headache induced by varenicline" (PMID 23175211, associated with the separate "headache disorder" candidate), plus a scoring note stating that varenicline is a known **cause** of headache as an adverse event rather than a treatment for it. This directly undercuts the plausibility of the migraine-disorder prediction and should be treated as a safety signal rather than an efficacy signal.

No clinical trials or literature in this evidence pack specifically evaluate varenicline in migraine patients. The single literature record attached to this indication (a fatal cardiac arrest case report) provides no mechanistic or efficacy support at all — it is an incidental adverse-event report, not migraine-related evidence.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [19585710](https://pubmed.ncbi.nlm.nih.gov/19585710/) | 2009 | Case Report | Therapie | Case report of cardiac arrest associated with varenicline use; unrelated to migraine efficacy, provides no supporting evidence for this indication |

---

## Norway Market Information

Varenicline is currently not marketed in Norway (0 authorizations on file); no license or approved-indication data is available.

---

## Safety Considerations

Please refer to the package insert for safety information.

*(Note: Two blocking/high-severity data gaps are on file — TFDA label warnings/contraindications [DG001, Blocking] and mechanism-of-action data [DG002, High] — both required before any S1 safety assessment can proceed.)*

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The migraine-disorder prediction is supported only by a TxGNN score with no corroborating clinical trials or on-topic literature (Evidence Level L5), and internal evidence within this same dataset indicates headache is a known adverse effect of varenicline — directly conflicting with a therapeutic rationale. Combined with the drug's non-marketed status in Norway and missing safety/MOA data, there is insufficient basis to advance this candidate.

**To proceed, the following is needed:**
- Resolve the DG001 (TFDA label warnings/contraindications) and DG002 (MOA) blocking/high-severity data gaps
- Preclinical or mechanistic studies specifically examining nAChR modulation in trigeminovascular migraine pathophysiology
- Clarification of the headache-induction vs. headache-treatment direction of effect (adverse event vs. therapeutic signal) before any further evaluation
- At minimum, observational or case-series data directly involving varenicline in migraine patients
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

