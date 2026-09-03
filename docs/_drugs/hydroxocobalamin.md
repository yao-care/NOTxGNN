---
layout: default
title: Hydroxocobalamin
parent: 僅模型預測 (L5)
nav_order: 170
evidence_level: L5
indication_count: 2
---

# Hydroxocobalamin
{: .fs-9 }

證據等級: **L5** | 預測適應症: **2** 個
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

# Hydroxocobalamin: From Unspecified Original Indication to Esophageal Varices (Without Bleeding)

## One-Sentence Summary

Hydroxocobalamin's original approved indication is not available in the current dataset (DrugBank extract lists no original indications and no Taiwan/Norway market license exists).
The TxGNN model predicts potential efficacy for **Esophageal Varices without Bleeding** (and, at an essentially identical score, **Esophageal Varices with Bleeding**),
but this is currently supported by **0 clinical trials** and **0 publications** — this is a pure model-prediction signal with no direct clinical or preclinical evidence.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available — no original indications recorded, and the drug is not yet licensed in Norway |
| Predicted New Indication | Esophageal Varices without Bleeding (rank 1); Esophageal Varices with Bleeding (rank 2, same score) |
| TxGNN Prediction Score | 99.23% |
| Evidence Level | L5 (model prediction only, no supporting trials or literature) |
| Norway Market Status | 未上市 (Not marketed) |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data for hydroxocobalamin is currently marked as a data gap (DG002) and not available from this evidence pack. However, the model's own rationale field provides a mechanistic hypothesis: hydroxocobalamin is known to scavenge nitric oxide (NO-scavenging), producing systemic vasoconstriction — a property already exploited clinically for conditions such as vasoplegic shock and refractory hypotension.

This same vasoconstrictive mechanism is the pharmacological basis for established esophageal varices therapies (e.g., vasopressin, terlipressin, somatostatin), which reduce portal pressure. This gives the "with bleeding" prediction a plausible physiological rationale. The "without bleeding" prediction (primary prophylaxis) extends this logic to long-term, non-acute use, which raises additional concerns — chronic vasoconstrictor exposure (hypertension risk) and hydroxocobalamin's known interference with certain laboratory colorimetric assays would need separate evaluation.

Importantly, this mechanistic link is explicitly flagged in the evidence pack as inferential, not evidence-based: there are no preclinical or clinical studies directly testing hydroxocobalamin in either esophageal varices indication. The connection should be treated as a hypothesis-generating signal only.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Norway Market Information

Hydroxocobalamin is currently **not marketed in Norway** (market status: 未上市) and has **0 authorizations** on record — no license or approved-indication data exists to summarize.

## Safety Considerations

Please refer to the package insert for safety information. (Key warnings, contraindications, and drug-drug interaction data are all currently unavailable — DDI query returned no results, and TFDA label warnings/contraindications are marked as a **blocking** data gap, DG001.)

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- Both predictions are L5 (model prediction only) with zero supporting trials or literature, and a blocking data gap (missing TFDA label/warnings) prevents even an initial safety screen (S1).

**To proceed, the following is needed:**
- Resolve DG001 (Blocking): obtain and parse the TFDA/product label for warnings, contraindications, and precautions.
- Resolve DG002: retrieve confirmed mechanism of action via DrugBank API.
- Establish the drug's actual original indication(s) and any existing market licenses (currently none identified).
- Conduct a targeted literature/clinical trial search specific to hydroxocobalamin and portal hypertension/esophageal varices to move beyond model-only evidence (L5 → higher tier).
- If evidence emerges, evaluate route compatibility (IV formulation vs. required route for varices management) and long-term safety (hypertension, lab assay interference) before advancing past S0.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

