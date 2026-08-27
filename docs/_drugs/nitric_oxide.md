---
layout: default
title: Nitric Oxide
parent: 僅模型預測 (L5)
nav_order: 54
evidence_level: L5
indication_count: 10
---

# Nitric Oxide
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

# Nitric Oxide (Inhaled): From Neonatal Persistent Pulmonary Hypertension to Pulmonary Arterial Hypertension

> **Note on indication selection:** This Evidence Pack ranked 10 TxGNN-predicted indications by raw similarity score. The top 6 ranked candidates (e.g., "malformation syndrome with odontal/periodontal component," "hypertrichosis," "Dandy-Walker malformation") were explicitly flagged in the pack's own `repurposing_rationale` as likely **knowledge-graph embedding artifacts** with no supporting mechanism, trials, or literature (evidence_level L5, decision_stage S0, recommendation Hold) — the pack itself recommends excluding them from screening. This report therefore focuses on **rank 7 — Pulmonary Arterial Hypertension (PAH)** — the highest-quality, most actionable candidate in the set (Evidence Level L1, decision_stage S3, "Proceed with Guardrails"). Ranks 8–10 (related PAH subtypes) are summarized briefly at the end for completeness.

---

## One-Sentence Summary

> Inhaled Nitric Oxide is an established gas therapy for hypoxic respiratory failure with pulmonary hypertension in neonates. Evidence in this pack strongly supports expanding its pharmacological rationale to **Pulmonary Arterial Hypertension** more broadly (adult/general WHO Group 1 disease), backed by **50 clinical trials** (including completed Phase 3/4 studies) and **20 supporting publications** describing the NO–sGC–cGMP pathway as a core, already-druggable mechanism in PAH.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not formally recorded in the supplied regulatory dataset (data gap); per the trial/literature evidence in this pack, inhaled NO's established clinical use is hypoxic respiratory failure with pulmonary hypertension in neonates (PPHN) |
| Predicted New Indication | Pulmonary Arterial Hypertension |
| TxGNN Prediction Score | 99.41% (rank 6252 of candidate set) |
| Evidence Level | L1 |
| Norway Market Status | ✗ Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data for this DrugBank entry is not available (data gap). However, based on the pharmacology consistently described across the supplied trial and literature evidence, Nitric Oxide (NO) is an endogenous vascular endothelial relaxing factor. Inhaled NO diffuses selectively into pulmonary vascular smooth muscle, activates soluble guanylate cyclase (sGC), and raises intracellular cGMP, producing **selective pulmonary vasodilation** without significant systemic hypotension — the same mechanism exploited by approved oral PAH therapies (PDE-5 inhibitors, sGC stimulators) that act on this identical pathway downstream.

The established original use of inhaled NO — reversing hypoxic respiratory failure caused by elevated pulmonary vascular resistance in neonates — and the predicted new indication, general pulmonary arterial hypertension, are mechanistically the same disease process (elevated pulmonary artery pressure driven by pulmonary vascular tone/remodeling), differing mainly in patient population (neonatal vs. adult/broader PAH etiologies) and route of chronic administration.

Multiple reviews in the evidence set (e.g., PMID 32442078, 23822809, 20051913) directly document that NO pathway deficiency and endothelial dysfunction are central to PAH pathogenesis, and that restoring NO signaling (via inhaled NO or downstream pathway drugs) is one of only three validated therapeutic pathways in PAH (alongside endothelin and prostacyclin pathways). This gives the TxGNN prediction strong, literature-confirmed mechanistic plausibility rather than a purely statistical association.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT01142219](https://clinicaltrials.gov/study/NCT01142219) | Phase 3 | Completed | 40 | RCT of L-arginine (NO precursor) as adjuvant therapy for sickle cell disease-associated PAH; direct evidence of NO-pathway modulation |
| [NCT04231084](https://clinicaltrials.gov/study/NCT04231084) | Phase 4 | Completed | 115 | Head-to-head acute hemodynamic comparison of inhaled NO vs. inhaled epoprostenol across PH phenotypes |
| [NCT00139217](https://clinicaltrials.gov/study/NCT00139217) | N/A | Completed | 400 | Large completed trial of non-invasive inhaled NO in persistent pulmonary hypertension of the newborn |
| [NCT05213676](https://clinicaltrials.gov/study/NCT05213676) | Phase 4 | Recruiting | 600 | Multi-center "NoNO Trial" evaluating de-implementation of iNO in congenital diaphragmatic hernia with PH |
| [NCT01959828](https://clinicaltrials.gov/study/NCT01959828) | Phase 3 | Completed | 18 | Safety/efficacy of inhaled NO (IK-3001) in Japanese patients with PH associated with cardiac surgery |
| [NCT07099144](https://clinicaltrials.gov/study/NCT07099144) | Phase 4 | Recruiting | 120 | Ongoing safety study of INOmax combined with ventilatory support for neonatal hypoxic respiratory failure with PH |
| [NCT00955487](https://clinicaltrials.gov/study/NCT00955487) | Phase 2 | Completed | 124 | Low-dose iNO to reduce bronchopulmonary dysplasia and associated pulmonary hypertension in premature newborns |
| [NCT01265888](https://clinicaltrials.gov/study/NCT01265888) | Phase 2 | Completed | 31 | Dose-escalation study of inhaled GeNOsyl NO in PAH (WHO Group 1) and PH secondary to idiopathic pulmonary fibrosis |
| [NCT06249633](https://clinicaltrials.gov/study/NCT06249633) | Early Phase 1 | Unknown | 20 | Pilot study of early iNO for ARDS-related pulmonary hypertension (small sample, status unknown) |
| [NCT01275339](https://clinicaltrials.gov/study/NCT01275339) | Phase 4 | Terminated | 10 | PDE5 inhibition pilot in aortic stenosis-related pulmonary venous hypertension (terminated, non-direct NO test) |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [32442078](https://pubmed.ncbi.nlm.nih.gov/32442078/) | 2020 | Review | Current Medicinal Chemistry | Details the NO pathway as a core pathomechanism, biomarker source, and drug target in PAH |
| [33836637](https://pubmed.ncbi.nlm.nih.gov/33836637/) | 2021 | Review | J Cardiovasc Pharmacol Ther | Combination PAH therapy targeting NO and prostacyclin pathways together |
| [38054614](https://pubmed.ncbi.nlm.nih.gov/38054614/) | 2024 | Review | Small | Reviews inhalable NO delivery technologies developed specifically for PAH treatment |
| [23822809](https://pubmed.ncbi.nlm.nih.gov/23822809/) | 2013 | Review | Am J Respir Crit Care Med | Landmark review on NO deficiency and endothelial dysfunction as central PAH mechanism |
| [20051913](https://pubmed.ncbi.nlm.nih.gov/20051913/) | 2010 | Review | Journal of Hypertension | NO, oxidative stress and inflammation as drivers of PAH pathophysiology |
| [35412560](https://pubmed.ncbi.nlm.nih.gov/35412560/) | 2022 | Review | JAMA | Contemporary diagnosis and treatment review of PAH |
| [39209476](https://pubmed.ncbi.nlm.nih.gov/39209476/) | 2024 | Review | European Respiratory Journal | Current PAH treatment algorithm across endothelin/NO/prostacyclin/BMP pathways |
| [37516248](https://pubmed.ncbi.nlm.nih.gov/37516248/) | 2023 | Review | Presse Médicale | General PAH review covering diagnosis, pathophysiology and management |
| [38416633](https://pubmed.ncbi.nlm.nih.gov/38416633/) | 2024 | Network meta-analysis | European Heart Journal | Individual participant data network meta-analysis comparing PAH treatment pathways |
| [33773120](https://pubmed.ncbi.nlm.nih.gov/33773120/) | 2021 | RCT | Lancet Respiratory Medicine | REPLACE trial: switching to riociguat (same NO-cGMP pathway) vs. continued PDE5 inhibitor therapy in PAH |

---

## Norway Market Information

Nitric Oxide currently holds **no marketing authorizations in Norway** (market status: Not marketed; total authorizations: 0). No product-level dosage form or approved-indication data is available for this jurisdiction at this time.

---

## Safety Considerations

Please refer to the package insert for safety information. No structured warnings, contraindications, or drug-interaction data were retrievable for this compound in the current evidence pack; this is flagged as a **Blocking** data gap (DG001: TFDA/label warnings and contraindications) that must be resolved before any formal safety pre-assessment (S1) can proceed.

---

## Other Related Candidates Identified in This Evidence Pack

For completeness, two additional high-quality candidates were identified among the 10 TxGNN predictions and may warrant parallel tracking:

- **Pulmonary arterial hypertension associated with congenital heart disease** (rank 8, score 99.41%, Evidence Level L1, decision_stage S3, "Proceed with Guardrails") — iNO is already the clinical standard for acute post-operative PH crises after congenital heart surgery; strong mechanistic and trial overlap with the primary candidate above.
- **PAH associated with connective tissue disease** and **PAH associated with chronic hemolytic anemia** (ranks 9–10, Evidence Level L3, decision_stage S1, "Research Question") — mechanistically plausible (endothelial NO deficiency / NO scavenging by free hemoglobin) but currently supported only by observational/mechanistic literature, with no dedicated interventional trials of NO/iNO in these subgroups yet.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Inhaled Nitric Oxide's proposed expansion to Pulmonary Arterial Hypertension is supported by the strongest evidence tier in this pack (L1) — including completed Phase 3/4 trials directly testing NO or NO-pathway agents in relevant PAH populations — and by a well-established, literature-confirmed mechanism (NO–sGC–cGMP selective pulmonary vasodilation) that is already the basis of approved PAH drug classes (PDE5 inhibitors, sGC stimulators). However, the drug is currently unmarketed in Norway and lacks any formal safety labeling data in this dataset, so guardrails are warranted before advancing further.

**To proceed, the following is needed:**
- Official TFDA/manufacturer package insert data (warnings, contraindications) — currently a Blocking data gap
- Confirmed detailed mechanism of action (MOA) documentation from DrugBank or equivalent source — currently a High-severity data gap
- Formal drug-drug interaction (DDI) profile, currently unretrieved ("not_found")
- Regulatory pathway assessment for Norway market entry, given zero current authorizations
- Clarification of the original approved indication record, since this field was empty in the source data despite iNO's well-documented use in neonatal PPHN
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

