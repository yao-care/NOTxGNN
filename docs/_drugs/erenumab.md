---
layout: default
title: Erenumab
parent: 僅模型預測 (L5)
nav_order: 139
evidence_level: L5
indication_count: 1
---

# Erenumab
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

# Erenumab: From Migraine Prevention to Migraine with Brainstem Aura

## One-Sentence Summary

Erenumab is a CGRP-receptor-targeting monoclonal antibody internationally approved for migraine prevention (episodic and chronic), though it is **not currently marketed in Norway** per this evidence pack.
The TxGNN model predicts it may be effective for **Migraine with Brainstem Aura**,
a distinct ICHD-3 subtype, but currently **0 clinical trials** and **20 publications** support this specific direction — and none of those publications are trials that specifically enrolled this aura subtype.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Migraine prevention (episodic/chronic) — internationally approved; no Norway market data on file |
| Predicted New Indication | Migraine with Brainstem Aura |
| TxGNN Prediction Score | 99.89% |
| Evidence Level | L4 |
| Norway Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the structured MOA field. Based on available evidence, however, erenumab is a monoclonal antibody that blocks the calcitonin gene-related peptide (CGRP) receptor, thereby inhibiting CGRP-mediated vasodilation and neurogenic inflammation within the trigeminovascular system — the pathway underlying its approved use in general migraine prevention.

The original indication (general migraine prevention) and the predicted indication (migraine with brainstem aura, formerly "basilar-type migraine") converge on the same CGRP pathway. Migraine with brainstem aura is a distinct ICHD-3 subtype whose pathophysiology involves posterior circulation (vertebrobasilar) vascular regulation. Mechanistically, CGRP receptor blockade could plausibly modulate vascular tone in this specific territory, offering a rationale for extending erenumab's use to this subtype.

However, patients with migraine with aura — including brainstem aura — were explicitly **excluded** from the major pivotal trials (STRIVE, ARISE) that established erenumab's efficacy for general migraine prevention. This means existing efficacy and safety data for migraine "with/without aura" (a broader, non-brainstem population) cannot be directly extrapolated to this higher-risk subtype. Given the elevated vascular risk historically associated with brainstem aura, this prediction is mechanistically plausible but **safety-unproven** for the specific target population.

---

## Clinical Trial Evidence

Currently no related clinical trials registered

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [34928306](https://pubmed.ncbi.nlm.nih.gov/34928306/) | 2022 | RCT (post-hoc subgroup) | JAMA Neurology | Secondary analysis of RCTs assessing erenumab safety/efficacy in migraine with vs. without aura; addresses elevated vascular risk in aura patients |
| [32867533](https://pubmed.ncbi.nlm.nih.gov/32867533/) | 2021 | RCT | Cephalalgia | Erenumab did not alter cerebral vasomotor reactivity or endothelial function in migraine without aura |
| [30360965](https://pubmed.ncbi.nlm.nih.gov/30360965/) | 2018 | RCT (Phase 3b) | Lancet | Randomised, double-blind, placebo-controlled trial: erenumab effective/tolerable in treatment-resistant episodic migraine |
| [37012858](https://pubmed.ncbi.nlm.nih.gov/37012858/) | 2023 | Systematic Review | Int Immunopharmacol | Systematic review confirming erenumab efficacy in episodic/chronic migraine prophylaxis |
| [30725283](https://pubmed.ncbi.nlm.nih.gov/30725283/) | 2019 | Review | Handb Exp Pharmacol | Foundational review of CGRP's role in migraine pathophysiology, underpinning CGRP-antibody rationale |
| [41888647](https://pubmed.ncbi.nlm.nih.gov/41888647/) | 2026 | Cohort (REFORM study) | J Headache Pain | Longitudinal study of erenumab's effect on migraine **aura frequency** specifically — most directly relevant to this indication |
| [40275185](https://pubmed.ncbi.nlm.nih.gov/40275185/) | 2025 | Cohort (biomarker) | J Headache Pain | Plasma suPAR (elevated in migraine with aura) associated with erenumab treatment response |
| [36942409](https://pubmed.ncbi.nlm.nih.gov/36942409/) | 2023 | Cohort | Headache | Post hoc pooled analysis of cardiovascular safety in migraine patients with/without aura on long-term erenumab |
| [35151970](https://pubmed.ncbi.nlm.nih.gov/35151970/) | 2022 | Cohort | Clin Neurol Neurosurg | Real-world effectiveness/safety of erenumab in treatment-resistant chronic migraine (Croatia) |
| [32359106](https://pubmed.ncbi.nlm.nih.gov/32359106/) | 2020 | Case series | Headache | Erenumab efficacy on comorbid cluster headache in migraine patients — related CGRP-pathway indication |

---

## Norway Market Information

Currently not marketed in Norway; no market authorization data available.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The mechanistic rationale (CGRP receptor blockade) is plausible, and one directly relevant study (REFORM, PMID 41888647) examined aura frequency under erenumab treatment. However, no clinical trials specifically enrolled migraine-with-brainstem-aura patients — pivotal trials explicitly excluded aura populations — and this subtype carries an elevated vascular risk profile that has not been safety-validated for CGRP receptor blockade in the posterior circulation.

**To proceed, the following is needed:**
- Regulatory safety label data (warnings, contraindications) — currently a **blocking data gap** preventing S1 safety assessment
- Formal MOA documentation from DrugBank/regulatory sources
- Dedicated clinical evidence (trial or case series) enrolling patients specifically diagnosed with migraine with brainstem aura
- Cardiovascular/posterior-circulation vascular risk assessment specific to this subtype
- Confirmation of Norway market authorization status, should commercial availability be pursued
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

