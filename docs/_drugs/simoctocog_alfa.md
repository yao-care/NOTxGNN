---
layout: default
title: Simoctocog Alfa
parent: Kun modellprediksjon (L5)
nav_order: 325
evidence_level: L5
indication_count: 10
---

# Simoctocog Alfa
{: .fs-9 }

Evidensnivå: **L5** | Predikerte indikasjoner: **10** stk.
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

# Simoctocog Alfa: From Haemophilia A to Pseudo-von Willebrand Disease

## One-Sentence Summary

> Simoctocog alfa is a recombinant human coagulation factor VIII (rFVIII) product, known for use in Haemophilia A.
> The TxGNN model's top prediction is **Pseudo-von Willebrand Disease**, with a score of **99.99%**,
> but this prediction is currently supported by **0 clinical trials** and **0 publications**, and the mechanistic rationale itself is weak.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Haemophilia A (bleeding prophylaxis/treatment) — not present in this Evidence Pack's license data, based on known rFVIII product class |
| Predicted New Indication | Pseudo-von Willebrand disease |
| TxGNN Prediction Score | 99.99% |
| Evidence Level | L5 |
| Norway Market Status | Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available (flagged as a High-severity data gap). Based on known information, simoctocog alfa is a recombinant human factor VIII (rFVIII) product, used to replace deficient endogenous FVIII and restore the intrinsic coagulation pathway in Haemophilia A patients.

However, the top-ranked predicted indication — pseudo-von Willebrand disease — is caused by an abnormal platelet GPIbα receptor with excessive affinity for von Willebrand factor (vWF), **not** by FVIII deficiency. Per the evidence pack's own mechanistic assessment, rFVIII replacement has no direct pathophysiological role in correcting this platelet-receptor defect. The high TxGNN score most likely reflects the close graph proximity of the FVIII–vWF complex in the knowledge graph, rather than a causal treatment relationship.

Notably, among the 10 candidates in this evidence pack, **rank 9 ("Haemophilia A with vascular abnormality")** carries the strongest genuine mechanistic plausibility, since it falls within the known FVIII replacement indication space — yet it scored far lower and has zero supporting trials or literature. This divergence between mechanistic plausibility and model score is an important caveat: the top-ranked prediction should not be treated as clinically actionable without independent mechanistic and label verification.

---

## Clinical Trial Evidence

Currently no related clinical trials registered

---

## Literature Evidence

Currently no related literature available

---

## Norway Market Information

This product is not currently marketed in Norway; no marketing authorizations (0 licenses) have been issued, so no license-level indication text is available for cross-reference.

---

## Safety Considerations

Please refer to the package insert for safety information.

*(Note: TFDA/label-level warnings and contraindications are marked as a Blocking data gap — this must be resolved before any safety pre-assessment (S1) can proceed.)*

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The evidence level is L5 (model prediction only, no clinical trials or literature), and the top-ranked indication's own mechanistic rationale suggests it reflects knowledge-graph proximity rather than a causal treatment effect. A Blocking data gap on product labeling (warnings/contraindications) also prevents the case from entering safety pre-assessment.

**To proceed, the following is needed:**
- Confirmed mechanism of action (MOA) data from DrugBank/manufacturer to validate or refute the FVIII–vWF proximity hypothesis
- TFDA/EMA label PDF parsing to resolve the Blocking safety data gap (warnings, contraindications)
- Manual clinical/haematology expert review of whether "pseudo-von Willebrand disease" has any documented off-label FVIII response, given the mechanistic mismatch
- Re-evaluate rank 9 ("Haemophilia A with vascular abnormality") as a mechanistically stronger candidate, despite its lower TxGNN score, once literature search is expanded
- Literature/clinical trial search using disease-specific terms (current search returned zero hits across all 10 candidates, suggesting search strategy may need broadening)
## Ansvarsfraskrivelse

Dette innholdet er kun til forskningsformål og utgjør ikke medisinsk rådgivning.
Klinisk validering kreves før enhver klinisk anvendelse.

---

