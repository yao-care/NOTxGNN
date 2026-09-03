---
layout: default
title: Rasagiline
parent: 僅模型預測 (L5)
nav_order: 296
evidence_level: L5
indication_count: 6
---

# Rasagiline
{: .fs-9 }

證據等級: **L5** | 預測適應症: **6** 個
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

# Rasagiline: From Parkinson's Disease (MAO‑B Inhibition) to PLA2G6‑Associated Neurodegeneration

## One-Sentence Summary

> Rasagiline's original indication is not recorded in the current dataset, though it is clinically known as a selective, irreversible MAO‑B inhibitor used in Parkinson's disease.
> The TxGNN model's top prediction is **PLA2G6‑Associated Neurodegeneration**, a rare neurodegenerative disorder with a parkinsonism phenotype.
> This is a **pure computational prediction** — **0 clinical trials** and **0 publications** currently support this direction.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not documented in this dataset (data gap). Clinically known use: MAO‑B inhibitor therapy in Parkinson's disease |
| Predicted New Indication | PLA2G6-Associated Neurodegeneration |
| TxGNN Prediction Score | 99.71% |
| Evidence Level | L5 |
| Norway Market Status | Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in this dataset (marked as a High-severity data gap). Based on general pharmacological knowledge referenced within the evidence pack itself, Rasagiline is a selective, irreversible MAO‑B inhibitor, a drug class established for reducing dopamine breakdown and providing neuroprotection in Parkinson's disease.

The top-ranked candidate, PLA2G6‑Associated Neurodegeneration (PLAN), has an adult-onset subtype (PARK14) that presents with dystonia‑parkinsonism and basal ganglia dopaminergic degeneration. This creates a plausible, though purely theoretical, mechanistic bridge: reduced dopamine catabolism via MAO‑B inhibition could in principle offer symptomatic or neuroprotective benefit in this parkinsonism-spectrum phenotype.

It is important to note this mechanistic link has **no dedicated clinical trial or literature support** — it is inferred by TxGNN from network structure and general disease-class similarity, not from any direct evidence of efficacy in PLAN.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Norway Market Information

Rasagiline is not currently marketed in Norway, and no marketing authorization records are available in this dataset (0 licenses).

---

## Safety Considerations

Please refer to the package insert for safety information. Note: TFDA labeling data (warnings and contraindications) is currently a **blocking data gap** and has not been reviewed — no formal safety (S1) assessment can be completed until this is resolved.

---

## Other Predicted Indications (For Context)

The evidence pack includes 5 additional TxGNN candidates, all at evidence level L5 with no supporting trials or literature:

| Rank | Disease | TxGNN Score | Mechanistic Plausibility | Recommendation |
|------|---------|-------------|--------------------------|-----------------|
| 2 | Rasmussen subacute encephalitis | 99.56% | None (autoimmune/inflammatory, unrelated to MAO‑B pathway) | Hold |
| 3 | Myelitis | 99.32% | None (inflammatory/infectious spinal cord disease) | Hold |
| 4 | Paralysis agitans, juvenile, of Hunt | 99.25% | **Strong** — historical term for juvenile parkinsonism, same disease spectrum as Rasagiline's known use | Research Question |
| 5 | Transaldolase deficiency | 99.19% | None (pentose phosphate pathway defect) | Hold |
| 6 | Polymicrogyria, perisylvian, with cerebellar hypoplasia and arthrogryposis | 99.01% | None (structural developmental brain malformation) | Hold |

Rank 4 ("Hunt's juvenile paralysis agitans") is mechanistically the most coherent candidate, since it falls within the same parkinsonism spectrum as Rasagiline's established pharmacology, but it lacks any subtype-specific trial or case-report evidence and remains a research hypothesis only.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
All six predicted indications are at evidence level L5 (model prediction only, no clinical or literature support). In addition, TFDA safety labeling data is a blocking gap, preventing any formal safety review, and the drug is not marketed in Norway.

**To proceed, the following is needed:**
- TFDA/regulatory label data (warnings, contraindications) to resolve the blocking safety data gap (DG001)
- Confirmed mechanism of action data from DrugBank (DG002)
- Original indication history for the drug (currently missing from dataset)
- Preclinical or mechanistic studies specifically addressing MAO‑B inhibition in PLAN or juvenile parkinsonism-spectrum disorders before advancing beyond hypothesis stage
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

