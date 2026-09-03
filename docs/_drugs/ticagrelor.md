---
layout: default
title: Ticagrelor
parent: 僅模型預測 (L5)
nav_order: 355
evidence_level: L5
indication_count: 10
---

# Ticagrelor
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

# TICAGRELOR: From Acute Coronary Syndrome to Intracranial Arteriosclerosis

## One-Sentence Summary

> Ticagrelor is an oral P2Y12 receptor antagonist established for antiplatelet therapy in acute coronary syndrome (ACS) and post-PCI thrombosis prevention.
> The TxGNN model predicts it may be effective for **Intracranial Arteriosclerosis** (intracranial arterial stenosis),
> with **11 clinical trials** and **3 publications** currently supporting this direction, including a dedicated Phase 3 RCT (CAPTIVA).

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Acute Coronary Syndrome (ACS) / post-PCI antiplatelet therapy — based on established clinical use; no Norway license record available in this dataset |
| Predicted New Indication | Intracranial Arteriosclerosis |
| TxGNN Prediction Score | 99.97% |
| Evidence Level | L2 |
| Norway Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Detailed structured MOA data for ticagrelor was flagged as a data gap (DG002) in this evidence pack. However, the literature evidence collected does describe its pharmacology: ticagrelor is a cyclopentyl-triazolopyrimidine, a reversible, direct-acting oral P2Y12 receptor antagonist that blocks a central amplification pathway of platelet activation. Unlike thienopyridines (e.g., clopidogrel), it does not require hepatic bioactivation, giving it a faster and more predictable onset/offset of antiplatelet effect.

Ticagrelor's original indication — ACS and post-PCI thrombosis prevention — is fundamentally an arterial, platelet-dependent thrombotic disease process. Intracranial arteriosclerosis (intracranial atherosclerotic stenosis, ICAS) shares the same underlying pathophysiology: plaque rupture or endothelial injury triggers platelet-dependent thrombus formation, which is the dominant mechanism behind ischemic stroke in ICAS patients. This mechanistic overlap is the basis for extrapolating P2Y12 inhibition from coronary to intracranial arterial beds.

That said, the repurposing rationale explicitly flags an important caveat: intracranial vessels carry a higher bleeding (intracerebral hemorrhage) risk than coronary vessels, so the mechanistic plausibility does not automatically translate to an equivalent risk-benefit profile. This is reflected in the evidence level (L2) and the "Proceed with Guardrails" recommendation — the direction is biologically sound and already being tested in a dedicated Phase 3 trial, but confirmatory efficacy/safety data specific to the intracranial vasculature is still pending.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT05047172](https://clinicaltrials.gov/study/NCT05047172) | Phase 3 | Active, not recruiting | 1,683 | CAPTIVA trial: directly compares rivaroxaban, ticagrelor, and both vs. clopidogrel for lowering 1-year ischemic stroke/ICH/vascular death in intracranial arterial stenosis — the most directly relevant trial for this indication |
| [NCT04948749](https://clinicaltrials.gov/study/NCT04948749) | N/A | Recruiting | 792 | DREAM-PRIDE: drug-eluting stent + aggressive medical therapy vs. standard medical therapy alone for preventing 1-year stroke recurrence in symptomatic intracranial atherosclerotic disease |
| [NCT06714526](https://clinicaltrials.gov/study/NCT06714526) | N/A | Recruiting | 100 | Pilot RCT comparing genotype-guided P2Y12 inhibitor selection vs. conventional clopidogrel in symptomatic intracranial atherosclerotic disease (ICAD) |
| [NCT06857045](https://clinicaltrials.gov/study/NCT06857045) | N/A | Withdrawn | 0 | Planned RCT of 3- vs 6-month DAPT after NOVA intracranial sirolimus-eluting stent implantation; trial was withdrawn |
| [NCT01732822](https://clinicaltrials.gov/study/NCT01732822) | Phase 3 | Completed | 13,885 | EUCLID: ticagrelor vs. clopidogrel in peripheral artery disease for reducing cardiovascular death/MI/ischemic stroke — large Phase 3 dataset, general PAD population (not intracranial-specific) |
| [NCT02605447](https://clinicaltrials.gov/study/NCT02605447) | Phase 4 | Completed | 2,009 | EVOLVE Short DAPT: safety of 3-month DAPT in high-bleeding-risk patients after PCI with an everolimus-eluting stent |
| [NCT01813435](https://clinicaltrials.gov/study/NCT01813435) | Phase 3 | Completed | 15,991 | GLOBAL LEADERS: ticagrelor+aspirin (1 month) then ticagrelor monotherapy (23 months) vs. standard DAPT after stent implantation |
| [NCT07354828](https://clinicaltrials.gov/study/NCT07354828) | N/A | Not yet recruiting | 3,500 | Quality control standard system for DAPT-based coronary revascularization in high-bleeding-risk ACS patients (China) |
| [NCT07164859](https://clinicaltrials.gov/study/NCT07164859) | Phase 3 | Not yet recruiting | 1,700 | SOLOPCI: very short DAPT (stopping aspirin at day 7) vs. standard DAPT duration in elderly PCI patients |
| [NCT06058130](https://clinicaltrials.gov/study/NCT06058130) | N/A | Unknown | 2,171 | Anticoagulation alone vs. anticoagulation + antiplatelet therapy in acute ischemic stroke with concomitant AF and extracranial/intracranial artery stenosis |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [39862061](https://pubmed.ncbi.nlm.nih.gov/39862061/) | 2025 | RCT (trial design) | International Journal of Stroke | Design paper for the CAPTIVA trial: standard clopidogrel+aspirin for symptomatic intracranial atherosclerotic stenosis (ICAS) leaves high residual stroke risk up to 12 months; CAPTIVA tests whether alternative dual antithrombotic combinations (including ticagrelor) outperform clopidogrel+aspirin |
| [38252758](https://pubmed.ncbi.nlm.nih.gov/38252758/) | 2024 | Review | Stroke | Focused update on intracranial atherosclerosis — introduces current knowledge gaps and highlights in ICAS management |
| [39658130](https://pubmed.ncbi.nlm.nih.gov/39658130/) | 2025 | Cohort | Journal of NeuroInterventional Surgery | Real-world experience with ticagrelor 60 mg BID + aspirin 81 mg vs. standard aspirin+clopidogrel for neurointerventional procedures (intracranial stenting), suggesting ticagrelor as a viable DAPT alternative in this setting |

---

## Norway Market Information

Ticagrelor is currently **not marketed in Norway** according to this dataset (market status: 未上市 / Not Marketed; total authorizations: 0). No product license records are available to summarize.

---

## Safety Considerations

Please refer to the package insert for safety information. Key warnings, contraindications, and drug-drug interaction data were not available in this evidence pack (flagged as a **Blocking** data gap — TFDA/regulatory package insert has not yet been retrieved).

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The mechanistic rationale is strong (shared platelet-dependent arterial thrombosis pathway between ACS and intracranial arteriosclerosis) and is already being tested in a large, ongoing Phase 3 RCT (CAPTIVA, n=1,683) specifically in this population. However, the intracranial vasculature carries materially higher bleeding/ICH risk than the coronary circulation, and confirmatory outcome data from CAPTIVA (expected completion 2027-01) is not yet available — so this cannot yet advance without additional safety guardrails.

**To proceed, the following is needed:**
- TFDA/regulatory package insert (warnings, contraindications) — currently a **Blocking** data gap (DG001)
- Confirmed structured MOA documentation from DrugBank (DG002)
- CAPTIVA trial primary results (ischemic stroke/ICH/vascular death outcomes) once available
- Intracranial-hemorrhage-specific risk stratification and monitoring plan before any clinical positioning
- Confirmation of Norway/local market and licensing pathway, since the drug is currently unmarketed in this jurisdiction
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

