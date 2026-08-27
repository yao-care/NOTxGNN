---
layout: default
title: Amifampridine
parent: 僅模型預測 (L5)
nav_order: 27
evidence_level: L5
indication_count: 2
---

# Amifampridine
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

# Amifampridine: From Lambert-Eaton Myasthenic Syndrome to Glaucoma

## One-Sentence Summary

Amifampridine (DrugBank DB11640) is a broad-spectrum Kv1.x voltage-gated potassium channel blocker whose established clinical use — referenced in the underlying mechanistic rationale — is Lambert-Eaton myasthenic syndrome (LEMS), where it boosts acetylcholine release at the neuromuscular junction. The TxGNN model predicts it may be effective for **Glaucoma**, but this prediction is currently supported by **0 clinical trials** and **0 publications** — it is a pure computational signal (TxGNN score 99.71%) with no drug-specific evidence behind it.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Lambert-Eaton myasthenic syndrome (LEMS) — inferred from the mechanistic rationale text (known NMJ pharmacology); no formal Norway license record confirms this, as the drug has 0 registered authorizations |
| Predicted New Indication | Glaucoma |
| TxGNN Prediction Score | 99.71% |
| Evidence Level | L5 |
| Norway Market Status | ✗ Not Marketed (未上市) |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, a formally confirmed mechanism-of-action record is not available (flagged as a data gap, DG002). Based on the information captured in the repurposing rationale, amifampridine is known to act as a broad-spectrum Kv1.x voltage-dependent potassium channel blocker at the neuromuscular junction, where it increases acetylcholine release — the pharmacological basis for its use in LEMS.

The proposed link to glaucoma rests on the fact that potassium and water channel activity in the ciliary body epithelium does influence aqueous humor production and intraocular pressure regulation, and potassium channels have a theoretical role in that pathway. However, this is a **family-level** inference (drugs that block potassium channels in general) rather than a **drug-specific** one: there is currently no published data, animal model, or human intraocular-pressure study demonstrating that amifampridine acts on ciliary-body potassium channels.

The evidence pack itself flags this connection as low-confidence, non-specific, and possibly a false-positive artifact of the TxGNN embedding space rather than a biologically grounded hypothesis. It should be treated as a hypothesis-generating signal only, not as mechanistic support for advancing the candidate.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Other TxGNN-Predicted Indication (Lower Priority)

A second candidate indication was also flagged by the model: **Acute Intermittent Porphyria** (TxGNN score 99.32%, rank 6919; Evidence Level L5; Recommendation: Hold). No clinical trials or literature were found for this pairing either. The rationale explicitly notes that amifampridine's mechanism (potassium channel blockade / NMJ acetylcholine release) has no known intersection with heme biosynthesis or ALA/PBG metabolism — the only plausible link is a symptom-level coincidence (peripheral neuropathy/weakness seen in both AIP and NMJ disorders), which the evidence pack itself characterizes as a likely false positive. This candidate is not pursued further in this report.

---

## Safety Considerations

Please refer to the package insert for safety information.

*(Note: a full Norway/TFDA-equivalent package insert with warnings and contraindications has not yet been obtained — this is logged as a Blocking data gap (DG001) and prevents the candidate from entering the S1 safety pre-screen stage.)*

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
This candidate sits at Evidence Level L5 — a model-only prediction with zero supporting clinical trials or literature, no confirmed mechanism-of-action record, and no Norway market presence (0 authorizations, not marketed). A Blocking data gap on the package insert (warnings/contraindications) also prevents any safety pre-screening. The mechanistic link to glaucoma is itself described as a weak, non-specific, family-level inference that may be a false positive, so there is currently no basis to advance beyond monitoring.

**To proceed, the following is needed:**
- Resolve DG001 (Blocking): obtain the official package insert/label (warnings, contraindications) to enable initial safety screening
- Resolve DG002 (High): confirm detailed mechanism-of-action data via DrugBank or primary pharmacology sources
- Preclinical or mechanistic evidence linking amifampridine (or Kv1.x blockade specifically) to ciliary body ion transport, aqueous humor dynamics, or intraocular pressure
- Any drug-specific clinical trial, case report, or pharmacovigilance signal for amifampridine in glaucoma
- Clarification of Norway regulatory pathway, since the drug is currently not marketed (0 licenses) and would require an import/named-patient or new-application route before any exploratory use
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

