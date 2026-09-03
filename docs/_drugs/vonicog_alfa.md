---
layout: default
title: Vonicog Alfa
parent: 僅模型預測 (L5)
nav_order: 387
evidence_level: L5
indication_count: 10
---

# Vonicog Alfa
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

# Vonicog Alfa: From Von Willebrand Disease to Primary Release Disorder of Platelets

## One-Sentence Summary

> Vonicog alfa is a recombinant von Willebrand factor (rVWF), established for the treatment of von Willebrand disease (VWD) — this is evident from the clinical trial and literature context contained in this evidence pack, even though a structured "original indication" field is not populated.
> The TxGNN model predicts it may be effective for **Primary Release Disorder of Platelets**,
> but currently **no clinical trials** and **no publications** support this specific direction, and the pack's own mechanistic review explicitly flags the biological rationale as weak.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Von Willebrand Disease (VWD) — inferred from the drug's established use as rVWF, as reflected throughout the trial/literature evidence in this pack; not independently confirmed via Norway license records (none on file) |
| Predicted New Indication | Primary Release Disorder of Platelets |
| TxGNN Prediction Score | 99.98% |
| Evidence Level | L5 (model prediction only, no supporting trials or literature) |
| Norway Market Status | ✗ Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data for vonicog alfa is not available in this evidence pack (flagged as a High-severity data gap, DG002). Based on the information available, vonicog alfa is a recombinant von Willebrand factor (rVWF) whose established pharmacological role is to mediate platelet **adhesion** to sites of vascular injury and to stabilize circulating Factor VIII — this is the mechanism underlying its proven use in von Willebrand disease.

Primary release disorder of platelets (e.g., platelet storage pool disease) is mechanistically distinct: it involves a defect in platelet **granule release**, not platelet adhesion. The evidence pack's own mechanistic rationale for this candidate states plainly that "vWF primarily mediates platelet adhesion rather than granule release function, and its mechanistic relevance to platelet release disorders is weak — this is purely a high-scoring TxGNN prediction with no direct biological basis supporting therapeutic effect."

In other words, the very high TxGNN score (99.98%) reflects a strong network-level association in the model, but is not corroborated by a plausible causal mechanism, nor by any clinical or literature evidence. This is a textbook case where a high prediction score alone is insufficient to support advancing a candidate.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Norway Market Information

Vonicog alfa currently holds no marketing authorization in Norway (0 licenses on file). No product-level dosage form or approved-indication data is available for this market.

---

## Safety Considerations

Please refer to the package insert for safety information.

*(Note: key warnings, contraindications, and drug-drug interaction data are unavailable in this evidence pack — this is flagged as a Blocking-severity gap, DG001, since TFDA/label safety data has not yet been retrieved. This gap must be resolved before any S1 safety pre-screening can proceed for this drug.)*

---

## Other Predicted Indications Under Evaluation

This evidence pack evaluated 10 TxGNN-predicted indications for vonicog alfa. Most share the same problem as the top-ranked candidate — very high scores with weak or contradictory mechanistic support and no clinical/literature evidence. One candidate stands out as materially different:

| Rank | Disease | Score | Evidence Level | Recommendation | Note |
|------|---------|-------|-----------------|------------------|------|
| 1 | Primary release disorder of platelets | 99.98% | L5 | Hold | Weak mechanism (adhesion vs. release) |
| 2 | Glanzmann thrombasthenia | 99.98% | L5 | Hold | Receptor deficiency, vWF cannot compensate |
| 3 | Pseudo-von Willebrand disease | 99.97% | L5 | Hold | Mechanism runs opposite to therapeutic intent |
| **4** | **Hemophilia** | 99.95% | **L3** | **Research Question** | **4 Phase 3 trials + 1 RCT (Blood, 2022); label/name mismatch with VWD trials — needs disambiguation** |
| 5 | Scott syndrome | 99.95% | L5 | Hold | No mechanistic overlap |
| 6 | Acquired coagulation factor deficiency | 99.94% | L5 | Research Question | Plausible FVIII-stabilization rationale, but no evidence |
| 7 | Von Willebrand disease, X-linked form | 99.92% | L4 | Research Question | Direct target match, but atypical inheritance labeling |
| 8 | Bleeding diathesis (collagen receptor defect) | 99.92% | L5 | Hold | Non-compensable receptor defect |
| 9 | Hemorrhagic disorder (constitutional thrombocytopenia) | 99.92% | L5 | Hold | vWF cannot correct platelet count |
| 10 | "Flood factor deficiency" | 99.90% | L5 | Hold | Likely data entry error; unclear disease entity |

Rank 4 ("hemophilia") is the only candidate in this pack with meaningful clinical trial and literature backing (L3, S1). However, the underlying trials (NCT03879135, NCT02973087, NCT02932618) and the key RCT (PMID 35439298, *Blood*, 2022) all actually enrolled **severe VWD** patients rather than classical hemophilia A/B populations — this suggests a labeling/ontology overlap (VWD type 2N presenting with a hemophilia-like phenotype) rather than a genuine repurposing signal into primary hemophilia. This candidate merits its own focused evaluation rather than being treated as equivalent to the Rank 1 prediction discussed above.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked prediction (primary release disorder of platelets) has no clinical trial or literature support, and the evidence pack's own mechanistic analysis explicitly states there is no direct biological basis for efficacy — the high TxGNN score alone is not sufficient to proceed. In addition, drug-level safety data (TFDA warnings/contraindications) is missing and flagged as a Blocking gap, so even a Research Question–tier candidate could not clear S1 safety pre-screening at this time.

**To proceed, the following is needed:**
- Resolve DG001 (Blocking): retrieve TFDA/label warnings and contraindications before any S1 safety pre-screening
- Resolve DG002 (High): retrieve confirmed MOA data from DrugBank to properly assess mechanistic plausibility
- If pursuing repurposing work on this drug, redirect focus to **Rank 4 (hemophilia)**, which already has L3 evidence, and first clarify whether the underlying trials represent true hemophilia A/B or VWD-hemophilia phenotype overlap
- Preclinical or mechanistic studies specifically testing vWF's role in platelet granule-release pathways, if the platelet-release-disorder hypothesis is to be pursued further
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

