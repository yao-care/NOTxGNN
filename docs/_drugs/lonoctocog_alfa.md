---
layout: default
title: Lonoctocog Alfa
parent: Kun modellprediksjon (L5)
nav_order: 214
evidence_level: L5
indication_count: 4
---

# Lonoctocog Alfa
{: .fs-9 }

Evidensnivå: **L5** | Predikerte indikasjoner: **4** stk.
{: .fs-6 .fw-300 }

---

## Innholdsfortegnelse
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## Farmasøytens vurderingsrapport

</div>

# Lonoctocog Alfa: From Hemophilia A to Pseudo-von Willebrand Disease

## One-Sentence Summary

Lonoctocog alfa is a recombinant single-chain Factor VIII product, used as replacement therapy for Hemophilia A. The TxGNN model predicts it may be effective for **Pseudo-von Willebrand Disease**, but this prediction is supported by **0 clinical trials** and **0 publications**, and the accompanying mechanistic analysis explicitly finds no meaningful pharmacological link between the drug and this platelet-receptor disorder.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Hemophilia A (Factor VIII replacement therapy) — not present in the evidence pack itself; inferred from the drug's known classification as a recombinant FVIII product (DrugBank DB13998) |
| Predicted New Indication | Pseudo-von Willebrand disease |
| TxGNN Prediction Score | 99.85% |
| Evidence Level | L5 (model prediction only, no supporting studies) |
| Taiwan Market Status | Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available for lonoctocog alfa in this evidence pack (flagged as a High-severity data gap). Based on general pharmacological knowledge, it functions as a recombinant Factor VIII replacement, restoring intrinsic-pathway tenase complex activity in patients with FVIII deficiency.

However, the repurposing rationale supplied for the top-ranked predicted indication directly argues against mechanistic plausibility: pseudo-von Willebrand disease is caused by a gain-of-function mutation in the platelet GPIb receptor, leading to abnormally high affinity for VWF and accelerated platelet/VWF clearance. FVIII levels are typically normal in this condition, and the standard treatment approach is antiplatelet therapy — not factor replacement. The evidence pack itself states "無機轉關聯" (no mechanistic link) for this candidate.

The other three predicted indications in this pack show the same pattern: primary platelet release disorder (granule secretion defect), Glanzmann thrombasthenia (GPIIb/IIIa deficiency), and Scott syndrome (ANO6/TMEM16F phospholipid-scramblase defect) are all platelet-function disorders where FVIII is not the deficient factor. Scott syndrome has the closest conceptual proximity (it affects the phospholipid platform on which FVIIIa/FIXa complexes assemble), but even there the rationale concludes FVIII supplementation cannot correct the underlying defect. In short, the high TxGNN similarity scores appear to be driven by graph-level proximity in the knowledge graph (all are inherited bleeding disorders) rather than by an actual actionable mechanism.

## Clinical Trial Evidence

Currently no related clinical trials registered

## Literature Evidence

Currently no related literature available

## Taiwan Market Information

Not marketed in Taiwan — no product authorizations are on record (total_licenses = 0).

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
This candidate is at decision stage S0 with Evidence Level L5 — a TxGNN score alone, with zero clinical trials, zero literature, and a mechanistic rationale that explicitly refutes pharmacological relevance to the top-ranked predicted indication (pseudo-von Willebrand disease is a platelet-receptor disorder, not an FVIII deficiency). The three next-ranked predictions (primary platelet release disorder, Glanzmann thrombasthenia, Scott syndrome) share the same disqualifying pattern. There is no basis to advance this candidate past initial screening.

**To proceed, the following is needed:**
- Actual MOA data from DrugBank (DG002) to properly characterize FVIII pharmacology
- TFDA label warnings/contraindications (DG001) — currently a Blocking gap preventing any S1 safety review
- Any real-world or mechanistic evidence that would reconcile the TxGNN prediction with the documented lack of pharmacological overlap, before this candidate could be reconsidered
## Ansvarsfraskrivelse

Dette innholdet er kun til forskningsformål og utgjør ikke medisinsk rådgivning.
Klinisk validering kreves før enhver klinisk anvendelse.

---

