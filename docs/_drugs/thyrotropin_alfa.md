---
layout: default
title: Thyrotropin Alfa
parent: Kun modellprediksjon (L5)
nav_order: 354
evidence_level: L5
indication_count: 10
---

# Thyrotropin Alfa
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

# Thyrotropin Alfa: From Undocumented Original Indication to Migraine Disorder

## One-Sentence Summary

> Thyrotropin alfa's original approved indication is not documented in the current evidence pack, and the drug is not marketed in Taiwan.
> The TxGNN model predicts a possible new indication for **Migraine Disorder** with a prediction score of **99.98%**,
> but this prediction is currently supported by **zero clinical trials** and **zero publications**, and the evidence pack's own mechanistic review finds no biological rationale linking exogenous TSH to migraine.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not documented in evidence pack |
| Predicted New Indication | Migraine Disorder |
| TxGNN Prediction Score | 99.98% |
| Evidence Level | L5 (model prediction only, no supporting studies) |
| Taiwan Market Status | ✗ Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data for thyrotropin alfa is not available in this evidence pack. No original indication text was captured either, so a direct pharmacological bridge between the known use of this drug and migraine disorder cannot be constructed from the supplied data.

More importantly, the evidence pack's own repurposing rationale for this top-ranked candidate explicitly states that there is **no experimental or known mechanistic basis** connecting exogenous TSH (thyrotropin alfa) to migraine. While thyroid dysfunction is occasionally associated with headache in the clinical literature, there is no direct evidential chain supporting this specific drug-disease pair. The assessment concludes that the high TxGNN score most likely reflects **topological similarity within the knowledge graph** rather than a validated biological mechanism.

This pattern repeats across nearly all top-10 predictions in this pack (migraine with brainstem aura, Raynaud disease, atrophoderma vermiculata, pulmonary hypertension, POTS, etc.) — none have supporting trials or literature, and several (pulmonary hypertension, POTS) are flagged as having a mechanistically **opposite** direction, since thyrotropin alfa stimulates thyroid hormone output rather than suppressing it. The one candidate with higher-tier evidence (hyperthyroidism, rank 10, L2) was found on inspection to involve trials using rhTSH for **diagnostic pre-treatment before radioiodine imaging/ablation**, not therapeutic treatment of hyperthyroidism — and the cited literature concerns interferon-alpha-induced thyroiditis, which is unrelated to thyrotropin alfa. In short, no candidate in this pack currently has a coherent, drug-specific mechanistic case.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Taiwan Market Information

Thyrotropin alfa is currently **not marketed** in Taiwan (0 authorizations on record), so no product/authorization table is available.

---

## Safety Considerations

Please refer to the package insert for safety information. (Key warnings, contraindications, and drug interaction data are not currently available in this evidence pack.)

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top predicted indication (migraine disorder) has an evidence level of L5 — a model-only prediction with zero clinical trials, zero literature, and an explicitly acknowledged absence of mechanistic support. No other candidate in this pack reaches an actionable evidence tier either; the one L2-evidence candidate (hyperthyroidism) turned out to be a mechanistic mismatch on closer review. Combined with the drug not being marketed in Taiwan and missing MOA/safety data, there is currently no basis to advance any candidate beyond hypothesis stage.

**To proceed, the following is needed:**
- TFDA-equivalent safety data (warnings, contraindications) — currently a **blocking** gap preventing entry into S1 safety pre-assessment (DG001)
- Confirmed original indication and mechanism of action (DrugBank or manufacturer labeling) (DG002)
- Independent mechanistic or preclinical validation for any candidate indication before further data collection is prioritized
- If pursuing hyperthyroidism further, re-scope evidence search specifically for therapeutic (not diagnostic pre-treatment) use of rhTSH
## Ansvarsfraskrivelse

Dette innholdet er kun til forskningsformål og utgjør ikke medisinsk rådgivning.
Klinisk validering kreves før enhver klinisk anvendelse.

---

