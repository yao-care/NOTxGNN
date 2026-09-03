---
layout: default
title: Riluzole
parent: 僅模型預測 (L5)
nav_order: 305
evidence_level: L5
indication_count: 10
---

# Riluzole
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

# Riluzole: From Amyotrophic Lateral Sclerosis to Bilateral Parasagittal Parieto-Occipital Polymicrogyria

## One-Sentence Summary

Riluzole is the well-established treatment for amyotrophic lateral sclerosis (ALS), acting through inhibition of glutamate release and excitotoxicity in motor neurons. The TxGNN model's top-ranked prediction for this candidate is **Bilateral Parasagittal Parieto-Occipital Polymicrogyria**, a cortical developmental malformation, but this direction is currently supported by **0 clinical trials** and **0 publications** — it is a pure algorithmic signal with no biological or clinical corroboration.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Amyotrophic Lateral Sclerosis (ALS) — formal regulatory indication text unavailable; inferred from literature evidence in this pack |
| Predicted New Indication | Bilateral Parasagittal Parieto-Occipital Polymicrogyria |
| TxGNN Prediction Score | 99.99% (rank 112) |
| Evidence Level | L5 |
| Norway Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed, formally sourced mechanism-of-action data is not available in this evidence pack (flagged as a High-severity data gap). However, literature evidence attached to a lower-ranked prediction in this same pack (PMID 21128691, 20942785, 31108504) consistently describes riluzole as a **glutamate release inhibitor / voltage-gated sodium channel blocker** that reduces excitotoxic injury to cortical and spinal motor neurons — the pharmacological basis for its FDA-approved use in ALS since 1995.

The top-ranked predicted indication here, bilateral parasagittal parieto-occipital polymicrogyria, is a **cortical developmental malformation** rather than a neurodegenerative or excitotoxicity-driven disease. Per the evidence pack's own mechanistic assessment, there is **no clear pathophysiological link** between riluzole's glutamate-modulating action and cortical malformation biology — the rationale explicitly characterizes this as "screening noise" arising from a high TxGNN score without mechanistic support.

By contrast, several other candidates within this same prediction set (e.g., rank 8, "amyotrophic lateral sclerosis, susceptibility to," which reached L1 evidence with 19 supporting publications) sit squarely within the ALS disease spectrum and share strong mechanistic plausibility with riluzole's known pharmacology. This top-ranked candidate does not.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Norway Market Information

Riluzole is not currently marketed in this region, and no authorization records are available in this dataset (0 licenses on file).

---

## Safety Considerations

Please refer to the package insert for safety information.

*(Note: This candidate carries a Blocking-severity data gap — TFDA/regulatory label warnings and contraindications have not yet been retrieved, which by internal scoring rules prevents entry into the S1 safety pre-screen stage.)*

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
This prediction is supported only by a raw TxGNN similarity score (L5), with zero clinical trials, zero literature, and no plausible mechanistic connection between riluzole's glutamate-excitotoxicity pharmacology and a cortical malformation syndrome. The evidence pack's own rationale text labels this as likely algorithmic noise.

**To proceed, the following is needed:**
- Preclinical/mechanistic studies establishing any biological rationale linking glutamate modulation to polymicrogyria pathophysiology
- Formal mechanism-of-action documentation (currently a High-severity data gap)
- TFDA/label-level warnings, contraindications, and DDI data (currently a Blocking-severity data gap preventing safety pre-screen)
- Consider redirecting evaluation effort toward **rank 8 (ALS susceptibility)** within this same prediction set, which already reaches L1 evidence with 19 supporting publications and a "Proceed with Guardrails" recommendation — a substantially stronger candidate than the top-ranked entry reviewed here.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

