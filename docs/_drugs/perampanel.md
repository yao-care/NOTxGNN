---
layout: default
title: Perampanel
parent: 僅模型預測 (L5)
nav_order: 275
evidence_level: L5
indication_count: 10
---

# Perampanel
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

# Perampanel: From Focal-Onset Seizures to Visual Epilepsy

## One-Sentence Summary

> Perampanel is a third-generation antiepileptic drug used for focal-onset seizures (with or without secondary generalization) and, as an adjunct, primary generalized tonic-clonic seizures.
> The TxGNN model predicts it may also be effective for **Visual Epilepsy** (a photosensitive reflex epilepsy subtype),
> but the supporting evidence base — **3 clinical trials** and **20 publications** — is entirely general antiepileptic evidence for perampanel, with **none specifically studying visual/photosensitive seizures**.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Focal-onset seizures (± secondary generalization); adjunctive therapy for primary generalized tonic-clonic seizures *(derived from literature context — not available from local license data; drug is not currently marketed here)* |
| Predicted New Indication | Visual epilepsy |
| TxGNN Prediction Score | 99.92% |
| Evidence Level | L5 |
| Norway Market Status | 未上市 (Not marketed) |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this evidence pack (flagged as a High-severity data gap, DG002). Based on known information from the supporting literature, perampanel is a **selective, non-competitive AMPA-receptor antagonist** — the first approved antiepileptic drug to act via this mechanism, reducing glutamate-mediated postsynaptic excitation. It is established as a broad-spectrum antiseizure medication for focal-onset and generalized tonic-clonic seizures.

Visual (photosensitive) epilepsy is a reflex epilepsy syndrome in which seizures are triggered by visual stimuli (e.g., flashing lights) acting through the same underlying cortical hyperexcitability and excessive glutamatergic transmission seen in other epilepsy subtypes. Because AMPA receptors mediate the excitatory signalling that underlies seizure generation and propagation broadly, there is a plausible mechanistic rationale for perampanel to suppress photically-triggered seizures as well.

However, **no clinical trial or publication in this evidence pack specifically studies perampanel in visual/photosensitive epilepsy**. The three retrieved trials and twenty publications document perampanel's efficacy across focal-onset seizures, generalized seizures, pediatric epilepsy, and status epilepticus — general antiepileptic evidence, not disease-specific confirmation for this reflex seizure subtype. One trial (NCT03653741) does examine perampanel's effect on visual evoked potentials (VEP), but this tests a neurophysiological biomarker, not treatment efficacy against visually-triggered seizures. The prediction should therefore be read as a mechanistic hypothesis extrapolated by the model, not as an evidence-confirmed indication.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT03780907](https://clinicaltrials.gov/study/NCT03780907) | Phase 2 | Completed | 18 | Tolerability, safety, and pharmacokinetics of perampanel in patients with refractory partial or generalised seizures; general epilepsy population, not visual-seizure specific |
| [NCT03653741](https://clinicaltrials.gov/study/NCT03653741) | Phase 4 | Completed | 12 | Examined perampanel's effect on neurophysiology tests (EEG, SEP, BAEP, and **VEP**) in healthy volunteers — tests a biomarker, not treatment of visually-triggered seizures |
| [NCT02900755](https://clinicaltrials.gov/study/NCT02900755) | Phase 4 | Completed | 30 | Evaluated cognition and EEG effects of perampanel as a newly authorized AED with a novel AMPA-antagonist mechanism; general refractory partial-onset seizure population |

*Note: none of the above trials specifically enrolled or evaluated patients with visual/photosensitive epilepsy.*

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [37059702](https://pubmed.ncbi.nlm.nih.gov/37059702/) | 2023 | Cochrane Systematic Review | Cochrane Database Syst Rev | Add-on perampanel for drug-resistant focal epilepsy; general efficacy/safety evidence base |
| [36206645](https://pubmed.ncbi.nlm.nih.gov/36206645/) | 2022 | Systematic Review & Meta-analysis of RCTs | Seizure | Confirms efficacy and safety of perampanel across focal and primary generalized tonic-clonic seizures |
| [35061214](https://pubmed.ncbi.nlm.nih.gov/35061214/) | 2022 | Network Meta-analysis | Drugs | Compares third-generation ASMs (including perampanel) for adjunctive treatment of focal-onset seizures |
| [37378757](https://pubmed.ncbi.nlm.nih.gov/37378757/) | 2023 | Systematic Review & Network Meta-analysis | J Neurol | Evaluates ASMs, including perampanel, for idiopathic generalized epilepsies |
| [36878742](https://pubmed.ncbi.nlm.nih.gov/36878742/) | 2023 | Systematic Review & Meta-analysis | Brain Dev | Efficacy, tolerability, and safety of perampanel in children/adolescents with epilepsy |
| [29898971](https://pubmed.ncbi.nlm.nih.gov/29898971/) | 2018 | Practice Guideline | Neurology | AAN/AES update on efficacy/tolerability of newer AEDs, including perampanel, for new-onset epilepsy |
| [24559052](https://pubmed.ncbi.nlm.nih.gov/24559052/) | 2014 | Review (MOA & development) | Expert Opin Drug Discov | Describes perampanel as first AMPA-receptor antagonist AED; approved in 35+ countries for partial-onset seizures |
| [36150304](https://pubmed.ncbi.nlm.nih.gov/36150304/) | 2022 | Review (Clinical trial + real-world) | Epilepsy Behav | Reviews perampanel monotherapy for focal-onset and generalized tonic-clonic seizures |
| [37684052](https://pubmed.ncbi.nlm.nih.gov/37684052/) | 2023 | Review | BMJ | General ASM safety profile discussion including perampanel, in pregnancy/lactation context |
| [38602656](https://pubmed.ncbi.nlm.nih.gov/38602656/) | 2024 | Preclinical/Mechanism Study | Mol Neurobiol | Investigates perampanel's effect on autophagy-mediated GluA2/PSD95 regulation in epilepsy models |

*None of the above directly study visual/photosensitive epilepsy as a distinct indication.*

---

## Norway Market Information

Perampanel is currently **not marketed** in this jurisdiction (market status: 未上市; 0 authorizations on record), so no license/product table is available.

---

## Safety Considerations

Please refer to the package insert for safety information. *(Key warnings, contraindications, and drug-drug interaction data are flagged in the evidence pack as a Blocking data gap — DG001 — preventing a formal S1 safety review at this time.)*

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- The TxGNN score for visual epilepsy is high, but no clinical trial or publication in the evidence pack directly studies perampanel in this photosensitive reflex epilepsy subtype — all supporting evidence is general antiepileptic data, meeting only L5 (model prediction without disease-specific study). This mirrors the pattern seen across most other reflex-epilepsy predictions in this evidence pack (startle, orgasm-induced, audiogenic, micturition-induced, eating, thinking, reading seizures — all also scored L5/Hold).
- Separately, a Blocking data gap (DG001: missing local label warnings/contraindications) means this candidate cannot yet proceed to a formal S1 safety review regardless of indication-level evidence.
- For context: among the 10 predicted indications in this pack, **status epilepticus** (rank 10) shows substantially stronger, disease-specific evidence (systematic reviews, cohort studies, and 5 dedicated clinical trials) and was independently scored L3 / "Proceed with Guardrails" — this may be a more promising repurposing candidate to prioritize ahead of visual epilepsy.

**To proceed, the following is needed:**
- Retrieve local (TFDA-equivalent) label warnings/contraindications to close DG001 before any safety review
- Obtain confirmed MOA documentation from DrugBank to close DG002
- Seek disease-specific preclinical or clinical evidence (e.g., photosensitivity/EEG photoparoxysmal response models) before advancing the visual epilepsy indication further
- Consider re-scoping repurposing priority toward status epilepticus, which has materially stronger direct evidence
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

