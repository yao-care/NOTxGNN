---
layout: default
title: Latanoprost
parent: 僅模型預測 (L5)
nav_order: 201
evidence_level: L5
indication_count: 10
---

# Latanoprost
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

# Latanoprost: From Ophthalmic Glaucoma Use to Primary Hereditary Glaucoma

## One-Sentence Summary

> Latanoprost is a prostaglandin F2α analogue used to lower intraocular pressure in glaucoma; the evidence pack does not carry a formally recorded original indication (drug is not yet marketed in Norway), but its established pharmacology already targets the glaucoma disease spectrum.
> The TxGNN model's top prediction — **Primary Hereditary Glaucoma** — is essentially a genetic subtype within that same spectrum rather than a novel disease area, and is supported by **1 completed Phase 2 clinical trial** and **0 publications**.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available in evidence pack (no Norway license record; drug is a prostaglandin analogue known for IOP-lowering / glaucoma use, per mechanistic notes) |
| Predicted New Indication | Primary Hereditary Glaucoma |
| TxGNN Prediction Score | 99.88% |
| Evidence Level | L2 |
| Norway Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data (`original_moa`) is not available as a structured field. However, the repurposing rationale confirms that latanoprost is a **prostaglandin F2α analogue (FP receptor agonist)** that lowers intraocular pressure by increasing **uveoscleral outflow** — the standard mechanism underlying all approved prostaglandin-analogue glaucoma therapies.

Primary hereditary glaucoma is a genetically-defined subtype within the broader glaucoma disease spectrum. Because the predicted indication shares the same underlying pathophysiology (elevated intraocular pressure) as the drug's known pharmacological target, this is better characterized as an **extension of an existing indication class** rather than a true cross-disease repurposing hypothesis — a point explicitly noted in the model's own rationale.

The remaining 9 predicted indications in this evidence pack (e.g., visceral calciphylaxis, thoracic outlet syndrome subtypes, angiodysplasia, blue toe syndrome, lymphangiectasis) have **no identified mechanistic link** to FP-receptor agonism and are flagged as statistical knowledge-graph associations without biological plausibility — all rated L5/Hold and excluded from further evidence review below.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT01527682](https://clinicaltrials.gov/study/NCT01527682) | Phase 2 | Completed | 37 | Assessed ocular hypotensive effect and safety of latanoprost combined with dorzolamide in pediatric primary glaucoma refractory to surgery |

---

## Literature Evidence

Currently no related literature available.

---

## Norway Market Information

Latanoprost currently holds **no marketing authorization in Norway** (market status: Not Marketed, 0 licenses on record). No product/dosage-form information is available for this evidence pack.

---

## Safety Considerations

Please refer to the package insert for safety information. No key warnings, contraindications, or drug-drug interaction data were retrievable at this time (DDI query returned no results).

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
One completed Phase 2 trial directly supports use of latanoprost (and combination therapy) in a related pediatric glaucoma population, and the mechanistic link to primary hereditary glaucoma is strong since both fall within the same IOP-lowering therapeutic rationale. However, the drug has no current Norway market authorization and lacks formal safety/label data, so guardrails are required before any commercial or clinical advancement.

**To proceed, the following is needed:**
- TFDA/regulatory label data (warnings, contraindications) — currently blocking per data gap DG001
- Confirmed mechanism-of-action documentation from DrugBank (DG002)
- Clarification of the drug's actual original/approved indication history, since no license records exist in Norway
- Assessment of whether "primary hereditary glaucoma" requires a distinct regulatory pathway from general glaucoma indications, or whether this is more appropriately treated as label extension rather than repurposing
- The 9 lower-ranked predictions (L5/Hold) require no further action unless new mechanistic or trial evidence emerges
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

