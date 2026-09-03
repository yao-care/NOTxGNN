---
layout: default
title: Levetiracetam
parent: 僅模型預測 (L5)
nav_order: 206
evidence_level: L5
indication_count: 10
---

# Levetiracetam
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

# Levetiracetam: From Epilepsy (Partial-Onset Seizures) to Visual Epilepsy

## One-Sentence Summary

> Levetiracetam is a second-generation antiepileptic drug, most commonly used worldwide as adjunctive (and in some markets monotherapy) treatment for partial-onset seizures, myoclonic seizures in juvenile myoclonic epilepsy, and primary generalized tonic-clonic seizures.
> The TxGNN model predicts it may also be effective for **Visual Epilepsy** (a photosensitive/reflex epilepsy subtype),
> with **9 clinical trials** and **20 publications** currently available as supporting (largely indirect) evidence.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Epilepsy / partial-onset seizures (per literature; no local marketing authorization or approved-indication text is on file) |
| Predicted New Indication | Visual Epilepsy |
| TxGNN Prediction Score | 99.98% |
| Evidence Level | L4 |
| Norway Market Status | Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, structured mechanism-of-action data is not available from DrugBank for this evidence pack. However, the supporting literature indicates that levetiracetam binds synaptic vesicle protein 2A (SV2A) and modulates neurotransmitter release, giving it a broad-spectrum antiseizure effect (PMID 21936590, PMID 34903423). It is already an established treatment across a wide range of seizure types, including partial-onset, myoclonic, and primary generalized tonic-clonic seizures.

Visual (photosensitive) epilepsy is a subtype of idiopathic generalized epilepsy in which seizures — commonly generalized tonic-clonic, myoclonic, or absence seizures — are triggered by flickering light or visual patterns. Because levetiracetam already has documented efficacy against myoclonic and generalized seizure types within idiopathic generalized epilepsy (e.g., PMID 40450767, PMID 37378757), its mechanistic reach plausibly extends to the visual/photosensitive trigger subtype.

That said, none of the clinical trials provided in this evidence pack were conducted specifically in patients with visual/photosensitive epilepsy — most concern neonatal seizures, TBI-related seizure prophylaxis, migraine, or cognitive effects in general epilepsy populations. The mechanistic rationale is therefore inferential rather than directly demonstrated.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT03107507](https://clinicaltrials.gov/study/NCT03107507) | Phase 4 | Unknown | 40 | Levetiracetam evaluated for neonatal seizure control; newer AEDs offer better side-effect profile than phenobarbital (general neonatal population, not photosensitive-specific) |
| [NCT00203216](https://clinicaltrials.gov/study/NCT00203216) | N/A | Completed | 31 | Open-label trial of levetiracetam for migraine prophylaxis with/without visual aura |
| [NCT04277936](https://clinicaltrials.gov/study/NCT04277936) | Phase 2 | Terminated | 1 | Tested whether LEV reduces hippocampal hyperactivity using a visual scene-processing fMRI task in psychosis |
| [NCT07336992](https://clinicaltrials.gov/study/NCT07336992) | Phase 3 | Not Yet Recruiting | 580 | Prophylactic LEV to improve functional outcome in acute intracerebral hemorrhage |
| [NCT00855738](https://clinicaltrials.gov/study/NCT00855738) | Phase 4 | Completed | 111 | Observational study of new AEDs (incl. LEV) as first-choice bitherapy in focal epilepsy |
| [NCT00105040](https://clinicaltrials.gov/study/NCT00105040) | Phase 2 | Completed | 87 | RCT of LEV cognitive/neuropsychological effects as adjunct in pediatric refractory partial-onset seizures |
| [NCT04559529](https://clinicaltrials.gov/study/NCT04559529) | Phase 2 | Completed | 62 | LEV modulation of hippocampal hyperactivity via visual scene-processing fMRI in psychosis (follow-up study) |
| [NCT04573803](https://clinicaltrials.gov/study/NCT04573803) | Phase 3 | Not Yet Recruiting | 1649 | LEV vs. phenytoin for seizure prevention after traumatic brain injury |
| [NCT04833907](https://clinicaltrials.gov/study/NCT04833907) | Phase 1/2 | Enrolling by Invitation | 24 | Gene therapy trial in Canavan disease (background context only, not directly relevant) |

**Note:** None of the above trials specifically enrolled patients with visual/photosensitive epilepsy; relevance grading in the source data classifies most as C (general seizure population) or B (partially overlapping population).

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [32385134](https://pubmed.ncbi.nlm.nih.gov/32385134/) | 2020 | RCT | Pediatrics | Levetiracetam vs. phenobarbital for neonatal seizures |
| [35963261](https://pubmed.ncbi.nlm.nih.gov/35963261/) | 2022 | RCT (Phase 3, PEACH) | Lancet Neurology | Prophylactic levetiracetam for seizure prevention after intracerebral hemorrhage |
| [38678766](https://pubmed.ncbi.nlm.nih.gov/38678766/) | 2024 | RCT | Seizure | Phenytoin vs. levetiracetam for acute symptomatic seizures in children with acute encephalitis syndrome |
| [30487494](https://pubmed.ncbi.nlm.nih.gov/30487494/) | 2018 | RCT | Mymensingh Medical Journal | Phenobarbital vs. levetiracetam in childhood epilepsy |
| [37378757](https://pubmed.ncbi.nlm.nih.gov/37378757/) | 2023 | Systematic Review/Network Meta-analysis | Journal of Neurology | ASM efficacy/safety comparison for idiopathic generalized epilepsies |
| [40450767](https://pubmed.ncbi.nlm.nih.gov/40450767/) | 2025 | Systematic Review/Meta-analysis | Epilepsy & Behavior | Levetiracetam for myoclonic seizures in idiopathic generalized epilepsy (incl. JME) |
| [34286461](https://pubmed.ncbi.nlm.nih.gov/34286461/) | 2022 | Systematic Review/Meta-analysis | Neurocritical Care | Levetiracetam for seizure prophylaxis in neurocritical care |
| [21936590](https://pubmed.ncbi.nlm.nih.gov/21936590/) | 2011 | Review | CNS Drugs | Overview of levetiracetam's approved indications and mechanism (SV2A binding) |
| [34260837](https://pubmed.ncbi.nlm.nih.gov/34260837/) | 2021 | Review | New England Journal of Medicine | Initial management of seizure in adults |
| [35976303](https://pubmed.ncbi.nlm.nih.gov/35976303/) | 2022 | Review | Arquivos de Neuro-Psiquiatria | Diagnosis, monitoring, and treatment of status epilepticus |

---

## Norway Market Information

Currently no marketing authorizations registered for this drug in Norway.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN prediction score is very high, and levetiracetam's broad-spectrum antiseizure mechanism is plausible for visual/photosensitive epilepsy given its established efficacy in related idiopathic generalized epilepsy subtypes (myoclonic seizures, generalized tonic-clonic seizures). However, none of the available clinical trials or literature directly study photosensitive/visual epilepsy populations — the evidence is indirect (general epilepsy, neonatal seizures, TBI, migraine), corresponding to evidence level L4. This is not yet sufficient to move past the research-hypothesis stage.

**To proceed, the following is needed:**
- TFDA/DMP-equivalent label data (warnings, contraindications) — currently a blocking data gap (DG001)
- Confirmed mechanism-of-action data from DrugBank (DG002)
- Targeted clinical or case-series evidence specifically in photosensitive/visual epilepsy patients
- Local (Norway) regulatory and market-authorization status, currently unavailable (0 licenses on file)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

