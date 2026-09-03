---
layout: default
title: Clopidogrel
parent: 僅模型預測 (L5)
nav_order: 90
evidence_level: L5
indication_count: 8
---

# Clopidogrel
{: .fs-9 }

證據等級: **L5** | 預測適應症: **8** 個
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

# Clopidogrel: From Antiplatelet Therapy to Migraine with Brainstem Aura

## One-Sentence Summary

> Clopidogrel is an antiplatelet agent, best known for reducing atherothrombotic events in cardiovascular and cerebrovascular disease.
> The TxGNN model predicts it may be effective for **Migraine with Brainstem Aura**,
> but currently **0 registered clinical trials** and **16 publications** support this specific direction — and most of that literature is indirect (PFO/ASD-related cohorts and case reports), making the evidence largely mechanistic rather than confirmatory.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Antiplatelet therapy for prevention of atherothrombotic events (general pharmacological knowledge; not provided in the evidence pack — no Norway license records exist for this drug) |
| Predicted New Indication | Migraine with Brainstem Aura |
| TxGNN Prediction Score | 99.44% |
| Evidence Level | L3 |
| Norway Market Status | Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available (flagged as a data gap in this evidence pack). Based on general pharmacological knowledge, clopidogrel is a thienopyridine-class P2Y12/ADP-receptor antagonist that irreversibly inhibits platelet aggregation; its efficacy in reducing atherothrombotic events (MI, ischemic stroke, PAD) is well established. Whether this mechanism translates into a migraine benefit is a separate, unproven question.

The proposed mechanistic link for this specific subtype is that migraine with aura is associated with right-to-left shunting (e.g., patent foramen ovale, PFO), through which venous microemboli or platelet-activation products may cross into the arterial circulation and trigger cortical spreading depression — the physiological correlate of aura. Clopidogrel's antiplatelet effect could theoretically reduce these microembolic triggering events. However, this is a **shunt-dependent hypothesis**, not a mechanism expected to apply broadly to all brainstem-aura migraine patients, and it has no direct connection to the core migraine pathways (CGRP, 5-HT) implicated in most migraine pathophysiology.

Notably, the strongest supporting evidence in this evidence pack (a completed Phase 4 RCT, CANOA — NCT00799045, PMID 26551304/32965476) actually pertains to the closely related but distinct indication "migraine disorder" (rank 2 in this evidence pack), and specifically to the narrow clinical context of new-onset migraine following transcatheter atrial septal defect (ASD) closure — not to unselected patients presenting with brainstem aura. This suggests the underlying biology may be real, but the specific diagnosis targeted here ("migraine with brainstem aura") has not itself been directly tested.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [26908949](https://pubmed.ncbi.nlm.nih.gov/26908949/) | 2016 | RCT | European Heart Journal | PRIMA trial: percutaneous PFO closure device (not clopidogrel) in migraine with aura refractory to medical therapy |
| [24836213](https://pubmed.ncbi.nlm.nih.gov/24836213/) | 2014 | RCT (pilot) | Cephalalgia | Pilot randomised controlled study testing clopidogrel as migraine prophylaxis |
| [39989443](https://pubmed.ncbi.nlm.nih.gov/39989443/) | 2025 | Systematic Review | Headache | Systematic review on the role of antithrombotic drugs in migraine prevention |
| [16103551](https://pubmed.ncbi.nlm.nih.gov/16103551/) | 2005 | Cohort | Heart | Clopidogrel reduced migraine with aura after transcatheter closure of PFO/ASD |
| [32848048](https://pubmed.ncbi.nlm.nih.gov/32848048/) | 2020 | Cohort | J Investig Med | Clopidogrel as complementary prophylactic for drug-refractory migraine with PFO |
| [30478067](https://pubmed.ncbi.nlm.nih.gov/30478067/) | 2018 | Cohort (open-label pilot) | Neurology | TRACTOR pilot study; follows earlier observation that thienopyridines (clopidogrel/prasugrel) reduced migraine in PFO patients |
| [30478066](https://pubmed.ncbi.nlm.nih.gov/30478066/) | 2018 | Cohort (retrospective) | Neurology | Retrospective review of thienopyridine therapy (including clopidogrel) in migraineurs with PFO |
| [24770421](https://pubmed.ncbi.nlm.nih.gov/24770421/) | 2014 | Cohort (retrospective) | Cephalalgia | Retrospective review of clopidogrel as primary therapy for migraineurs with right-to-left shunt lesions |
| [33815258](https://pubmed.ncbi.nlm.nih.gov/33815258/) | 2021 | Case Report | Frontiers in Neurology | Migraine-like headache with visual aura triggered by endovascular coiling (mechanistic parallel, not a clopidogrel study) |
| [36588875](https://pubmed.ncbi.nlm.nih.gov/36588875/) | 2022 | Case Report | Frontiers in Neurology | Aura migraine elicited by pulmonary arteriovenous fistula (right-to-left shunt mechanism parallel, not a clopidogrel study) |

---

## Norway Market Information

No license records exist — clopidogrel has 0 registered authorizations and is **not marketed** in Norway according to the evidence pack (`market_status: 未上市`, `total_licenses: 0`).

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- No clinical trial directly tests clopidogrel in "migraine with brainstem aura"; the evidence base is limited to mechanistic hypothesis and indirect PFO/ASD-related cohort and case-report literature (L3, "Research Question" stage). The one completed RCT with positive, directly relevant results (CANOA) targets a related but distinct, narrower population (post-ASD-closure migraine), not this specific diagnosis.

**To proceed, the following is needed:**
- A trial (or subgroup analysis) specifically enrolling brainstem-aura migraine patients, ideally stratified by PFO/right-to-left shunt status
- Formal mechanism of action data (currently a flagged data gap)
- TFDA/Norway regulatory safety data (warnings, contraindications, DDI) — currently unavailable
- Consider prioritizing "migraine disorder" (rank 2 in this evidence pack) instead, which has stronger, direct RCT-level evidence (CANOA, completed Phase 4, n=220) and an L2/"Proceed with Guardrails" rating, albeit still limited to the PFO/ASD-closure subgroup
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

