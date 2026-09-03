---
layout: default
title: Metformin
parent: 僅模型預測 (L5)
nav_order: 226
evidence_level: L5
indication_count: 5
---

# Metformin
{: .fs-9 }

證據等級: **L5** | 預測適應症: **5** 個
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

# Metformin: From Undocumented Original Indication to Focal Stiff Limb Syndrome

## One-Sentence Summary

> The original indication for Metformin is not documented in the current evidence pack (data gap flagged as Blocking/High severity).
> The TxGNN model predicts it may be effective for **Focal Stiff Limb Syndrome**, a rare GAD65-antibody-mediated autoimmune neurological disorder,
> but this prediction is currently supported by **0 clinical trials** and **0 publications** — it is a pure model-driven signal (L5), and the drug's own repurposing rationale flags the mechanistic link as likely indirect rather than causal.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not documented in evidence pack (data gap) |
| Predicted New Indication | Focal Stiff Limb Syndrome |
| TxGNN Prediction Score | 99.45% |
| Evidence Level | L5 (model prediction only, no clinical or literature support) |
| Norway Market Status | Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available for Metformin in this evidence pack (flagged as a High-severity data gap). Metformin's known pharmacology — AMPK activation, suppression of hepatic gluconeogenesis, and improved insulin sensitivity — is well established in the metabolic disease space, but no verified MOA record exists in this dataset to formally link it to the predicted indication.

Notably, the evidence pack's own mechanistic rationale for this prediction is cautionary rather than supportive: Focal Stiff Limb Syndrome is driven by GAD65-antibody-mediated loss of GABAergic inhibitory signaling in the spinal cord/brainstem — a pathway with no established connection to Metformin's known metabolic mechanisms. The high TxGNN score likely reflects an indirect knowledge-graph association (e.g., metabolic comorbidity or drug side-effect edges in the graph) rather than a genuine mechanism-driven signal.

Given the complete absence of clinical trials, literature, or a plausible mechanistic bridge, this prediction should be treated as a low-confidence, exploratory hypothesis rather than a repurposing candidate ready for evaluation.

---

## Clinical Trial Evidence

Currently no related clinical trials registered

---

## Literature Evidence

Currently no related literature available

---

## Norway Market Information

Metformin currently has no marketing authorization recorded in Norway (0 licenses on file); no product/dosage form data is available in this evidence pack.

---

## Safety Considerations

Please refer to the package insert for safety information.

*(Note: TFDA-equivalent warnings/contraindications and drug interaction data are flagged as a Blocking data gap — this prevents any Stage-1 safety evaluation for this candidate.)*

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is supported only by a TxGNN model score (L5, no clinical trials or literature), and the accompanying mechanistic rationale explicitly notes the biological link to GABAergic autoimmune pathology is indirect and not mechanism-driven. Combined with the drug's "not marketed" status in Norway and missing safety data, there is currently no basis to advance this candidate beyond exploratory tracking.

**To proceed, the following is needed:**
- TFDA-equivalent package insert data (warnings, contraindications) — currently a Blocking gap
- Verified Metformin mechanism of action (MOA) record from DrugBank or equivalent source
- Confirmation of Metformin's actual original indication(s), currently undocumented in this evidence pack
- Any preclinical or case-level evidence connecting AMPK/metabolic pathways to GABAergic/autoimmune neurological disease, to justify moving from L5 to L4

---

**Note on related candidates:** This evidence pack (`TW-DB00331-multi`) contains 4 additional predicted indications for Metformin at similarly high TxGNN scores (classic stiff person syndrome, opsismodysplasia, thiamine-responsive dysfunction syndrome, and drug-induced localized lipodystrophy) — all rated L5/Hold with no clinical or literature support. One candidate (thiamine-responsive dysfunction syndrome) carries a flagged **safety concern** rather than therapeutic opportunity, since Metformin's known mitochondrial Complex I inhibition may be mechanistically counterproductive in that condition. None of these five candidates currently meet the threshold for further evaluation.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

