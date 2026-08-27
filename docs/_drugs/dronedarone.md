---
layout: default
title: Dronedarone
parent: 僅模型預測 (L5)
nav_order: 42
evidence_level: L5
indication_count: 10
---

# Dronedarone
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

# Dronedarone: From Atrial Fibrillation to Stroke

## One-Sentence Summary

Dronedarone is a Class III antiarrhythmic agent originally developed to maintain sinus rhythm in patients with atrial fibrillation/atrial flutter. The TxGNN model predicts it may also reduce the risk of **stroke** (as a downstream consequence of AF-related cardioembolism), with **19 clinical trials** and **20 publications** currently supporting this direction — though several of the strongest sources also flag important safety caveats.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Atrial Fibrillation / Atrial Flutter (per literature evidence; no Norway license record exists) |
| Predicted New Indication | Stroke (stroke disorder) |
| TxGNN Prediction Score | 99.97% |
| Evidence Level | L1 |
| Norway Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Currently, no structured MOA record is available for dronedarone (data gap DG002). However, the evidence pack's own literature and rationale content describe it as a **multi-channel blocker / Class III antiarrhythmic agent** (a non-iodinated benzofuran analogue of amiodarone) that restores and maintains sinus rhythm in atrial fibrillation and atrial flutter. Interestingly, mechanistic work (PMID 28992468) suggests dronedarone also exerts **direct anticoagulant and antiplatelet effects independent of its antiarrhythmic action**, which may explain why it reduces thromboembolic events beyond what rhythm control alone would predict.

Atrial fibrillation is the leading cardiac cause of cardioembolic stroke — thrombi form in the left atrial appendage during AF and can embolize to the brain. By restoring and maintaining sinus rhythm (and via the pleiotropic antithrombotic effect noted above), dronedarone plausibly reduces this embolic risk chain. Multiple post-hoc analyses of the pivotal ATHENA trial (referenced across the literature set, e.g., PMID 20730068, PMID 22149318 equivalent findings, PMID 21296333) directly reported a reduction in stroke incidence among patients with paroxysmal or persistent AF treated with dronedarone.

This mechanistic link is not without an important boundary condition: the PALLAS trial (NCT01151137, terminated; publication PMID 22082198, *NEJM*) found that in patients with **permanent** AF and additional cardiovascular risk factors, dronedarone was associated with *increased* rates of stroke, heart failure, and cardiovascular death, leading to trial termination. This means the "stroke-reduction" signal is population-specific — it applies to paroxysmal/persistent AF, not to permanent AF or patients with decompensated heart failure, who represent a contraindicated subgroup.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT01856075](https://clinicaltrials.gov/study/NCT01856075) | N/A (observational) | Completed | 1,015 | Real-world comparative effectiveness of dronedarone vs. other antiarrhythmics in AF |
| [NCT05279833](https://clinicaltrials.gov/study/NCT05279833) | N/A (SLR/NMA) | Completed | 87,810 | Systematic review/network meta-analysis: dronedarone (Multaq) vs. sotalol safety in AF |
| [NCT05130268](https://clinicaltrials.gov/study/NCT05130268) | Phase 4 | Completed | 339 | Pragmatic RCT: early dronedarone vs. usual care in first-detected AF |
| [NCT01151137](https://clinicaltrials.gov/study/NCT01151137) | Phase 3 | Terminated | 3,236 | PALLAS trial: dronedarone in permanent AF — terminated early due to increased CV events/stroke; defines a contraindicated population |
| [NCT04704050](https://clinicaltrials.gov/study/NCT04704050) | Phase 4 | Terminated | 22 | EDORA trial: dronedarone vs. placebo on atrial fibrosis/AF recurrence post-ablation |
| [NCT07270848](https://clinicaltrials.gov/study/NCT07270848) | Phase 4 | Not yet recruiting | 1,898 | Planned multicenter study on efficacy/safety/QoL of dronedarone for early rhythm control |
| [NCT06096337](https://clinicaltrials.gov/study/NCT06096337) | N/A | Active, not recruiting | 484 | Pulsed field ablation vs. antiarrhythmic drug therapy (may include dronedarone) as first-line AF treatment |
| [NCT07242326](https://clinicaltrials.gov/study/NCT07242326) | N/A (observational) | Enrolling by invitation | 1,000 | Registry on label-concordant dosing/adherence of oral anticoagulants and AF medications in elderly patients |
| [NCT01266681](https://clinicaltrials.gov/study/NCT01266681) | N/A | Unknown | 100 | Amiodarone vs. dronedarone for maintenance of sinus rhythm post-cardioversion |
| [NCT01288352](https://clinicaltrials.gov/study/NCT01288352) | Phase 4 | Completed | 2,789 | EAST trial: early structured rhythm control (including antiarrhythmics) vs. usual care to prevent AF-related complications, including stroke |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [22082198](https://pubmed.ncbi.nlm.nih.gov/22082198/) | 2011 | RCT (PALLAS) | New England Journal of Medicine | Dronedarone in high-risk permanent AF increased major vascular events including stroke — defines contraindicated population |
| [28992468](https://pubmed.ncbi.nlm.nih.gov/28992468/) | 2017 | Mechanistic | Atherosclerosis | Dronedarone exerts direct anticoagulant/antiplatelet effects independent of its antiarrhythmic action, supporting a stroke-reduction mechanism |
| [20730068](https://pubmed.ncbi.nlm.nih.gov/20730068/) | 2010 | Review | Vascular Health and Risk Management | Reviews FDA approval of dronedarone; post-hoc ATHENA analysis suggested decreased stroke risk |
| [28496906](https://pubmed.ncbi.nlm.nih.gov/28496906/) | 2013 | Cohort | Journal of Atrial Fibrillation | Real-world comparison of CV events, stroke, CHF, and liver injury risk: dronedarone vs. amiodarone and other antiarrhythmics |
| [40387892](https://pubmed.ncbi.nlm.nih.gov/40387892/) | 2025 | Cohort (EAST-AFNET 4 sub-analysis) | Clinical Research in Cardiology | Long-term safety/efficacy of amiodarone and dronedarone for early rhythm control |
| [37485722](https://pubmed.ncbi.nlm.nih.gov/37485722/) | 2023 | Cohort | Circulation: Arrhythmia and Electrophysiology | Retrospective comparison of dronedarone vs. sotalol effectiveness/safety in antiarrhythmic-naive veterans |
| [35293087](https://pubmed.ncbi.nlm.nih.gov/35293087/) | 2022 | Post-hoc RCT (ATHENA) | European Journal of Heart Failure | Dronedarone in AF with concomitant HFpEF/HFmrEF |
| [33888353](https://pubmed.ncbi.nlm.nih.gov/33888353/) | 2021 | Real-world data study | Clinical Therapeutics | Risk of digitalis intoxication with concomitant dronedarone and digoxin use — relevant drug interaction signal |
| [22166900](https://pubmed.ncbi.nlm.nih.gov/22166900/) | 2012 | Review | Lancet | General overview of AF management and stroke risk stratification |
| [25428811](https://pubmed.ncbi.nlm.nih.gov/25428811/) | 2015 | Cost-effectiveness analysis | Kardiologia Polska | Cost-effectiveness of dronedarone vs. amiodarone, propafenone, and sotalol in AF |

---

## Norway Market Information

Dronedarone is currently **not marketed in Norway** — no market authorizations are on record (0 licenses).

---

## Safety Considerations

Please refer to the package insert for safety information.

*(Note: TFDA package insert warnings/contraindications remain an unresolved blocking data gap — see Next Steps below. Separately, the evidence itself flags two population-level cautions worth carrying forward operationally: increased risk of stroke/CV events in permanent AF or heart failure patients per the PALLAS trial, and a digoxin interaction signal per PMID 33888353.)*

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The evidence level is L1, anchored by a completed Phase 4 RCT (NCT05130268) and a large systematic review/NMA (NCT05279833), with a coherent mechanistic story (post-hoc ATHENA stroke reduction, direct antithrombotic effect) supporting benefit in paroxysmal/persistent AF. However, the same evidence base (PALLAS trial) shows harm in permanent AF/heart failure populations, so any pathway forward must explicitly exclude that subgroup and cannot proceed on efficacy data alone without resolving safety documentation.

**To proceed, the following is needed:**
- TFDA package insert warnings/contraindications (Blocking gap, DG001) — required before any S1 safety pre-assessment
- Confirmed mechanism of action data from DrugBank (High priority gap, DG002)
- Explicit exclusion criteria for permanent AF and heart failure patients, based on the PALLAS trial signal
- DDI review, particularly the digoxin interaction (PMID 33888353), given DDI query currently returns "not found"
- A market authorization pathway assessment for Norway, since the drug is not currently marketed there
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

