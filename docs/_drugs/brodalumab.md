---
layout: default
title: Brodalumab
parent: 僅模型預測 (L5)
nav_order: 60
evidence_level: L5
indication_count: 10
---

# Brodalumab
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

# Brodalumab: From an Unspecified Original Indication to Strongyloidiasis (Flagged as a Reversed-Direction Signal)

## One-Sentence Summary

> Brodalumab's original indication is not recorded in this evidence pack, though it is known to act as an **IL-17RA antagonist**.
> The TxGNN model's top prediction — **Strongyloidiasis** — is not supported by any clinical trials or literature, and the model's own mechanistic rationale indicates the association runs in the *opposite* direction: IL-17 blockade is a known **risk factor** for strongyloidiasis, not a treatment for it.
> This is best read as a safety signal miscaptured as a repurposing opportunity, not a viable candidate.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not provided in this evidence pack (`original_indications` empty) |
| Predicted New Indication | Strongyloidiasis ⚠️ (mechanistically reversed — see below) |
| TxGNN Prediction Score | 99.84% |
| Evidence Level | L5 (no clinical trials, no literature) |
| Norway Market Status | Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | **Hold** |

---

## Why is This Prediction Reasonable?

Formal mechanism-of-action data (DrugBank `original_moa`) is not available in this evidence pack. However, the model's own rationale annotations identify brodalumab as an **IL-17RA (interleukin-17 receptor A) antagonist**, which blocks IL-17-mediated signaling. IL-17RA-targeting biologics as a class are used to suppress IL-17-driven inflammatory responses.

The original indication field is empty in this pack, so no direct comparison to the predicted indication can be made from the structured data. What *can* be assessed is the mechanistic plausibility of the top-ranked prediction on its own terms — and here the evidence pack flags a critical problem.

**This prediction is not reasonable, and the evidence pack itself says so.** IL-17 is a key host-defense cytokine against intestinal nematodes, including *Strongyloides stercoralis*. Clinically, IL-17 pathway inhibitors (brodalumab, secukinumab, and related agents) are known to *increase* the risk of strongyloidiasis reactivation/hyperinfection — package inserts for this drug class typically require screening and treatment of latent strongyloidiasis *before* initiating therapy. TxGNN's topological similarity scoring appears to have picked up a real biological relationship (IL-17RA ↔ strongyloidiasis) but assigned it the wrong causal direction — a known failure mode where "risk association" and "therapeutic indication" edges are conflated in the knowledge graph. This should be treated as a **contraindication signal**, not a repurposing lead.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Norway Market Information

Brodalumab has **0 authorizations** on record and is **not marketed** in Norway (`未上市`) per this evidence pack. No license entries are available to tabulate.

---

## Safety Considerations

- **Mechanistic Safety Signal (from prediction rationale, not formal labeling):** The evidence pack's own analysis notes that IL-17 pathway blockade — the mechanism of brodalumab — is associated with an *increased* risk of *Strongyloides* infection/hyperinfection syndrome. This mirrors known class-level guidance for IL-17 inhibitors requiring strongyloidiasis screening prior to treatment initiation.
- Formal package insert warnings, contraindications, and drug-drug interaction data are not available in this evidence pack (flagged as a **Blocking** data gap, DG001). Please refer to the official package insert for complete safety information once available.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked prediction (strongyloidiasis) is directionally inverted — it describes a known risk of the drug's mechanism, not a therapeutic opportunity — and carries zero supporting clinical trials or literature (L5). No other candidate in the top 10 (ranks 2–10, all ophthalmic/inflammatory conditions) reaches beyond L4/L5, and several (e.g., isolated optic neuritis) carry their own directional uncertainty, since IL-17 inhibitors have been associated with case reports of CNS demyelinating disease exacerbation.

**To proceed, the following is needed:**
- Formal DrugBank/TFDA data for original indication and MOA, to establish a true baseline for mechanistic comparison
- TFDA package insert (warnings, contraindications, DDI) to close Blocking data gap DG001
- Any brodalumab-specific (not class-level) case reports or pharmacovigilance data on strongyloidiasis, to confirm risk directionality rather than infer it
- If pursuing the optic neuritis/CRION cluster (ranks 5–8) as a longer-shot hypothesis, targeted literature search for Th17/IL-17 involvement in demyelinating optic neuropathies, alongside explicit review of CNS demyelination risk associated with IL-17 inhibitor use
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

