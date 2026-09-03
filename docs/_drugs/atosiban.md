---
layout: default
title: Atosiban
parent: 僅模型預測 (L5)
nav_order: 39
evidence_level: L5
indication_count: 10
---

# Atosiban
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

# Atosiban: From Preterm Labor to Primary Hereditary Glaucoma

## One-Sentence Summary

Atosiban is an oxytocin/vasopressin V1A receptor antagonist used clinically as a tocolytic to suppress uterine contractions in preterm labor. TxGNN predicts a possible new application in **Primary Hereditary Glaucoma**, but this is the top-ranked of ten low-confidence predictions for this drug, none of which is supported by any registered clinical trial or mechanistic literature. Given the model-only nature of the evidence, this candidate does not currently support further development.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Preterm labor (tocolytic) — based on drug class/mechanism only; not documented in Norway regulatory records |
| Predicted New Indication | Primary Hereditary Glaucoma |
| TxGNN Prediction Score | 99.92% |
| Evidence Level | L5 |
| Norway Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data for atosiban is not available from DrugBank (Data Gap DG002). Based on the rationale accompanying this prediction, atosiban's only well-established clinical action is competitive antagonism of the oxytocin receptor and vasopressin V1A receptor, used to inhibit uterine smooth muscle contraction in threatened preterm labor.

There is no established or biologically plausible pathway connecting oxytocin/V1A receptor antagonism to aqueous humor dynamics or intraocular pressure regulation, which underlie primary hereditary glaucoma and open-angle glaucoma (ranks 1–2). The TxGNN score for this indication is very high (99.92%), but it is not corroborated by any clinical trial or published literature — this pattern strongly suggests the prediction reflects graph-embedding similarity in the knowledge graph rather than genuine pharmacological plausibility.

Across the other predicted indications in this evidence pack, the same pattern holds: hair/follicle-related predictions (ranks 3, 4, 5, 7), thoracic outlet syndrome (ranks 8, 9), and calciphylaxis (rank 10) all lack any mechanistic or clinical rationale. The one exception — "vascular disease" (rank 6) — has literature evidence, but it points in the **opposite direction**: cardioprotective effects reported in the literature are attributed to oxytocin receptor **agonism**, whereas atosiban is a receptor **antagonist**, and a separate cohort study associates tocolytic exposure with increased neonatal intraventricular hemorrhage and death. This is a safety signal, not supporting evidence.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

*(No trials are associated with the top-ranked indication, primary hereditary glaucoma. Note: rank 9, "venous thoracic outlet syndrome," lists NCT03570294, but this trial evaluates oxidative stress in preterm women receiving atosiban and has no direct relevance to thoracic outlet syndrome — it is a mismatched pairing per the evidence pack's own relevance grading (Grade C).)*

---

## Literature Evidence

Currently no related literature available for primary hereditary glaucoma.

---

## Norway Market Information

Atosiban is **not marketed** in Norway (`taiwan_regulatory.market_status = 未上市`), with **0 registered authorizations**. No product, dosage form, or approved indication text is available for this drug in the current dataset.

---

## Other Predicted Indications (For Reference)

The evidence pack scores ten indications for atosiban; none currently reaches an actionable evidence level. Summary:

| Rank | Disease | TxGNN Score | Evidence Level | Note |
|------|---------|-------------|-----------------|------|
| 1 | Primary hereditary glaucoma | 99.92% | L5 | No mechanistic or clinical support |
| 2 | Open-angle glaucoma | 99.92% | L5 | No mechanistic or clinical support |
| 3 | Congenital hypotrichosis milia | 99.89% | L5 | No mechanistic or clinical support |
| 4 | Alopecia | 99.89% | L5 | No direct study; only indirect oxytocin/skin biology speculation |
| 5 | Hypotrichosis simplex of the scalp | 99.89% | L5 | No mechanistic or clinical support |
| 6 | Vascular disease | 99.87% | L4 | **Mechanistically contradictory** (antagonist vs. protective agonist effects) + a safety signal (neonatal IVH/death with tocolytic exposure) |
| 7 | Diffuse alopecia areata | 99.86% | L5 | No mechanistic or clinical support |
| 8 | Arterial thoracic outlet syndrome | 99.86% | L5 | No mechanistic or clinical support |
| 9 | Venous thoracic outlet syndrome | 99.86% | L5 | Only trial listed is a mismatched pairing (Grade C relevance) |
| 10 | Visceral calciphylaxis | 99.84% | L5 | No mechanistic or clinical support |

None of these indications meet the threshold for progression beyond S0/S1 hold status.

---

## Safety Considerations

No safety data (key warnings, contraindications, or drug interactions) are currently available for atosiban in this evidence pack — this is flagged as a **Blocking** data gap (DG001) that prevents any S1 safety assessment. Please refer to the manufacturer's product information or regulatory sources in markets where atosiban is approved (e.g., EU/EMA) before any further evaluation.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
All ten TxGNN-predicted indications for atosiban are unsupported by clinical trials or credible mechanistic literature (nine at L5). The single indication reaching L4 ("vascular disease") is undermined by opposing receptor pharmacology and an associated safety signal (neonatal IVH/death with tocolytic exposure) rather than genuine supporting evidence. Atosiban is also not marketed in Norway, and both safety labeling (DG001, Blocking) and mechanism-of-action data (DG002, High) are missing.

**To proceed, the following is needed:**
- Obtain atosiban's approved product labeling (warnings/contraindications) from a market where it is registered (e.g., EMA/EU SmPC), to resolve DG001
- Obtain confirmed MOA detail from DrugBank API to resolve DG002
- If pursuing glaucoma-related indications: commission dedicated preclinical studies on oxytocin/V1A receptor pathways in aqueous humor dynamics, since no literature currently exists
- Before considering any cardiovascular-related repurposing (rank 6), specifically investigate the antagonist-vs-agonist mechanistic conflict and the neonatal IVH/death safety signal in PMID 30646165
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

