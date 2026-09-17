---
layout: default
title: Orlistat
parent: Kun modellprediksjon (L5)
nav_order: 256
evidence_level: L5
indication_count: 1
---

# Orlistat
{: .fs-9 }

Evidensnivå: **L5** | Predikerte indikasjoner: **1** stk.
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

# Orlistat: From Obesity Management to Hypervitaminosis

## One-Sentence Summary

Orlistat is a pancreatic lipase inhibitor generally used for weight management in obesity (not confirmed via the current Taiwan/Norway regulatory dataset, as the drug is not marketed in this evidence pack).
The TxGNN model predicts it may be effective for **Hypervitaminosis**,
but this prediction is currently supported by **0 clinical trials** and **0 publications** — it is a mechanism-only hypothesis.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available in regulatory dataset (drug not marketed); commonly known as an anti-obesity/weight-management agent |
| Predicted New Indication | Hypervitaminosis |
| TxGNN Prediction Score | 99.42% |
| Evidence Level | L5 |
| Norway Market Status | Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed official mechanism-of-action documentation is not available in this evidence pack (`original_moa` = Data Gap). However, based on the drug's known pharmacology, orlistat is a pancreatic/gastric lipase inhibitor that blocks the hydrolysis of dietary triglycerides in the intestinal lumen, thereby reducing the absorption of dietary fat.

Absorption of the fat-soluble vitamins (A, D, E, K) depends on the formation of mixed lipid micelles in the gut — the same process orlistat disrupts. This is why fat-soluble vitamin deficiency is a well-recognized side effect of orlistat therapy in its original obesity indication. The TxGNN prediction essentially proposes the inverse application of this same mechanism: using orlistat's fat-malabsorption effect to lower excessive circulating levels of fat-soluble vitamins in hypervitaminosis.

This is a mechanistically plausible hypothesis, but it has not been tested in any registered clinical trial or published study. The high TxGNN score (99.42%) reflects strong structural/mechanistic similarity inferred by the model, **not** clinical validation.

---

## Clinical Trial Evidence

Currently no related clinical trials registered

---

## Literature Evidence

Currently no related literature available

---

## Norway Market Information

This drug is not currently marketed in this dataset (`market_status`: Not marketed), and no authorization records are available (`total_licenses`: 0).

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests solely on mechanistic reasoning (Evidence Level L5) with no supporting clinical trials or literature, and the drug is not currently marketed in this jurisdiction. This does not meet the evidentiary bar to advance to safety review or clinical evaluation.

**To proceed, the following is needed:**
- Confirmed official mechanism-of-action documentation (DrugBank API query — currently blocked, DG002)
- TFDA/regulatory label warnings and contraindications (Blocking gap, DG001) before any S1 safety screening can occur
- Confirmation of the drug's actual approved original indication(s) from an authoritative regulatory source
- At minimum, preclinical or case-level evidence exploring orlistat's effect on fat-soluble vitamin clearance in hypervitaminosis before considering further evaluation
## Ansvarsfraskrivelse

Dette innholdet er kun til forskningsformål og utgjør ikke medisinsk rådgivning.
Klinisk validering kreves før enhver klinisk anvendelse.

---

