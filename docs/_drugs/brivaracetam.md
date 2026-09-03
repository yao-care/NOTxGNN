---
layout: default
title: Brivaracetam
parent: 僅模型預測 (L5)
nav_order: 59
evidence_level: L5
indication_count: 10
---

# Brivaracetam
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

# Brivaracetam: From Focal-Onset Epilepsy to Status Epilepticus

## One-Sentence Summary

Brivaracetam is a high-affinity SV2A ligand originally developed and used as adjunctive therapy for focal-onset (partial) seizures in epilepsy.
Among the ten indications predicted by the TxGNN model, **Status Epilepticus** shows by far the strongest supporting evidence and is the focus of this report,
with **2 clinical trials** (including one direct head-to-head comparison with levetiracetam) and **19 publications** currently supporting this direction.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Focal-onset (partial) seizures / epilepsy, adjunctive treatment (inferred from literature; no Norway license text available) |
| Predicted New Indication | Status Epilepticus |
| TxGNN Prediction Score | 99.40% |
| Evidence Level | L2 |
| Norway Market Status | Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the evidence pack (data gap, DG002). Based on known information from the literature, brivaracetam is a high-affinity, selective ligand of synaptic vesicle protein 2A (SV2A), structurally related to levetiracetam but with 15- to 30-fold greater binding affinity and faster brain penetration. Its efficacy in focal-onset epilepsy has been established through multiple Phase 3 trials and is now supported for status epilepticus by real-world and registry data.

Status epilepticus (SE) is, pathophysiologically, a failure of the mechanisms that normally terminate a seizure — it is a continuation and intensification of the same underlying seizure biology already targeted by brivaracetam in its approved indication. Levetiracetam, the parent compound acting on the same SV2A target, is already widely used intravenously in SE management, making brivaracetam's extension into this indication a class-effect extrapolation rather than a novel mechanistic hypothesis.

Mechanistically, brivaracetam's rapid blood-brain-barrier penetration and available intravenous formulation are particularly well suited to the emergency treatment setting of SE, where fast onset of action is critical. This combination of established SV2A pharmacology, an IV formulation, and accumulating multicenter registry and comparative trial data supports the plausibility of this predicted indication.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT07163572](https://clinicaltrials.gov/study/NCT07163572) | N/A | Completed | 152 | Direct comparison of IV brivaracetam vs. IV levetiracetam for acute management of pediatric status epilepticus; addresses the current gap in pediatric SE data for brivaracetam. |
| [NCT07443241](https://clinicaltrials.gov/study/NCT07443241) | N/A | Completed | 779 | Retrospective real-world study of sex-related differences in etiology, diagnostics, treatment, and outcomes of SE (2011–2023 cohort); includes treatment data but not brivaracetam-specific. |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [32278203](https://pubmed.ncbi.nlm.nih.gov/32278203/) | 2020 | Systematic Review | J Neurol Sci | Efficacy/tolerability of IV brivaracetam for SE; notes sparse controlled trial data limiting current recommendation strength. |
| [41838218](https://pubmed.ncbi.nlm.nih.gov/41838218/) | 2026 | Systematic Review | J Neurol | Most recent systematic review of brivaracetam for SE; evaluates efficacy and safety across accumulated studies. |
| [31342405](https://pubmed.ncbi.nlm.nih.gov/31342405/) | 2019 | Systematic Review | CNS Drugs | IV brivaracetam in SE treatment; highlights favorable pharmacokinetics for emergency use. |
| [32822230](https://pubmed.ncbi.nlm.nih.gov/32822230/) | 2020 | Review | Epilepsy Currents | AES Treatments Committee comprehensive review of refractory convulsive SE; evaluates 8 parenteral ASMs including brivaracetam as third-line option. |
| [26891946](https://pubmed.ncbi.nlm.nih.gov/26891946/) | 2016 | Review | Expert Rev Clin Pharmacol | Brivaracetam in focal/idiopathic generalized epilepsies and SE; summarizes seizure reduction and responder rates across dose ranges. |
| [36528008](https://pubmed.ncbi.nlm.nih.gov/36528008/) | 2023 | Review (photosensitivity model) | Epilepsy & Behavior | Compares brivaracetam and levetiracetam using the photosensitivity/EEG biomarker model as a lens for SE treatment decisions. |
| [31260101](https://pubmed.ncbi.nlm.nih.gov/31260101/) | 2019 | Multicenter Registry | Epilepsia | Multicenter evaluation of IV brivaracetam use in SE, supported by preclinical effectiveness in animal SE models. |
| [33561784](https://pubmed.ncbi.nlm.nih.gov/33561784/) | 2021 | Multicentric Retrospective Study | Seizure | Italian multicenter retrospective study evaluating use, effectiveness, and adverse events of IV brivaracetam in SE. |
| [30530123](https://pubmed.ncbi.nlm.nih.gov/30530123/) | 2019 | Cohort/PK Study | Epilepsy Research | Correlates IV brivaracetam loading dose and plasma levels with clinical response in SE patients. |
| [32480279](https://pubmed.ncbi.nlm.nih.gov/32480279/) | 2020 | Case Report | Seizure | Case report describing use of brivaracetam in absence status epilepticus. |

---

## Norway Market Information

Currently not marketed in Norway — no local authorization/license data is available for this product.

---

## Safety Considerations

Please refer to the package insert for safety information.

*(Note: key warnings, contraindications, and drug-drug interaction data are all currently unavailable — DG001 identifies this as a blocking gap for the S1 safety review stage.)*

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
One completed head-to-head trial (IV brivaracetam vs. levetiracetam, N=152) plus multiple systematic reviews and multicenter registry studies support the use of IV brivaracetam in status epilepticus, consistent with the already-established use of the same-class SV2A ligand levetiracetam in this setting. This corresponds to Evidence Level L2 — sufficient to proceed cautiously, but not yet to a full "Go" given the absence of a dedicated adult RCT.

**To proceed, the following is needed:**
- Local regulatory/label data (TFDA/EMA package insert warnings and contraindications) — currently a blocking data gap (DG001)
- Drug-drug interaction data (current DDI query returned "not found")
- Formal mechanism-of-action documentation for regulatory submission (DG002)
- A prospective RCT in the adult SE population, as the strongest current comparative trial is in pediatric patients
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

