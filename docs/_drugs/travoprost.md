---
layout: default
title: Travoprost
parent: 僅模型預測 (L5)
nav_order: 371
evidence_level: L5
indication_count: 10
---

# Travoprost
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

# Travoprost: From Open-Angle Glaucoma/Ocular Hypertension to Visceral Calciphylaxis

## One-Sentence Summary

> Travoprost is a prostaglandin F2α (FP receptor) analogue used topically for open-angle glaucoma and ocular hypertension (inferred from clinical trial context, as no `original_indications` were recorded).
> The TxGNN model's top prediction is **Visceral Calciphylaxis**,
> but this candidate currently has **0 clinical trials** and **0 publications** supporting it — the score reflects graph-embedding similarity only, with no mechanistic or clinical corroboration.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Open-angle glaucoma / ocular hypertension (inferred from trial evidence; not present in `taiwan_regulatory.licenses`) |
| Predicted New Indication | Visceral Calciphylaxis |
| TxGNN Prediction Score | 99.9998% |
| Evidence Level | L5 (model prediction only, no supporting studies) |
| Norway Market Status | ✗ Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available (`original_moa`: [Data Gap]). Based on known pharmacology, travoprost is a synthetic prostaglandin F2α analogue and FP receptor agonist; its established clinical use is lowering intraocular pressure via increased uveoscleral outflow in glaucoma/ocular hypertension.

For the top-ranked candidate, **visceral calciphylaxis**, the evidence pack's own rationale explicitly states there is no direct or indirect clinical evidence, and no known mechanistic link — calciphylaxis pathology centers on vascular calcification and microthrombosis, which is not connected to FP receptor signaling. The high TxGNN score reflects graph-embedding similarity in the knowledge graph, not a validated pharmacological hypothesis.

It is worth noting that among the other nine predicted indications in this pack, only rank 5 ("vascular disease") has any clinical trial/literature attached, and even those are indirect (ocular vasoactivity findings, hyperemia adverse-event studies) rather than treatment evidence for a systemic vascular disease. Rank 10 ("hemangioendothelioma") is supported only by a case report of travoprost-induced uveal effusion — an adverse-event signal, not a therapeutic one. None of the ten predictions in this pack currently meet a credible mechanistic or clinical bar.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Norway Market Information

Travoprost currently has no marketing authorization on record (`market_status`: 未上市 / Not marketed; `total_licenses`: 0). No license entries are available to summarize.

---

## Safety Considerations

Please refer to the package insert for safety information. (Key warnings, contraindications, and drug interaction data are all currently unavailable — see data gaps DG001/DG002 below.)

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked prediction (visceral calciphylaxis) has zero clinical trials, zero literature, and an explicitly stated absence of mechanistic plausibility in the evidence pack itself — this is a pure model-similarity signal (L5) with no corroborating evidence of any kind.

**To proceed, the following is needed:**
- TFDA label warnings/contraindications (DG001, Blocking — currently blocks S1 safety screening)
- Verified mechanism of action data from DrugBank (DG002, High priority)
- Preclinical or mechanistic studies linking FP receptor agonism to vascular calcification pathology
- If pursuing rank 5 ("vascular disease") instead, systemic (non-ocular) pharmacokinetic/exposure data, since current evidence is limited to topical ocular effects
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

