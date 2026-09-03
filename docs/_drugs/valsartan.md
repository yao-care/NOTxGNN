---
layout: default
title: Valsartan
parent: 僅模型預測 (L5)
nav_order: 377
evidence_level: L5
indication_count: 7
---

# Valsartan
{: .fs-9 }

證據等級: **L5** | 預測適應症: **7** 個
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

# Valsartan: From Hypertension to Malignant Hypertensive Renal Disease

## One-Sentence Summary

> Valsartan is an angiotensin II type 1 (AT1) receptor blocker (ARB) globally used to treat hypertension and heart failure, though it is not currently marketed in this jurisdiction. The TxGNN model predicts it may be effective for **malignant hypertensive renal disease**, but this direction is currently supported by only **0 clinical trials** and **1 indirect preclinical publication** (studying a different drug class), making the evidence base very weak at this stage.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Hypertension (ARB class; globally approved indication — not yet marketed in this jurisdiction, so no local approval text is available) |
| Predicted New Indication | Malignant Hypertensive Renal Disease |
| TxGNN Prediction Score | 99.97% |
| Evidence Level | L5 |
| Norway Market Status | ✗ Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Formal DrugBank-sourced mechanism of action data is currently unavailable (Data Gap DG002). However, based on the mechanistic rationale accompanying this evidence pack, valsartan is understood to act as an AT1 receptor antagonist, blocking the renin-angiotensin-aldosterone system (RAAS). This is the same pharmacological class widely used to slow progression of hypertensive kidney damage.

Malignant hypertensive renal disease is, by definition, a severe complication of uncontrolled hypertension with marked RAAS activation and renal microvascular injury. Since valsartan's established indication (hypertension) directly targets the RAAS pathway believed to drive this renal complication, there is a plausible mechanistic rationale for extending its use to this more severe, related condition.

That said, the only literature currently linked to this specific prediction (PMID 24368192) does **not** study valsartan or ARBs directly — it examines avosentan, an endothelin receptor antagonist, in a rat model of hypertensive nephropathy. This is class-level, indirect supporting evidence at best, not drug-specific proof. A closely related prediction in this evidence pack — "malignant renovascular hypertension" (rank 2) — does have literature directly testing AT1 receptor blockade (the valsartan mechanism) in a malignant hypertension animal model (PMID 11560862), which lends indirect cross-support to the biological plausibility of this class of predictions, though still only at the preclinical level.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [24368192](https://pubmed.ncbi.nlm.nih.gov/24368192/) | 2014 | Preclinical/Animal | Pharmacological Research | In double transgenic rats (dTGR) with hypertensive nephropathy, avosentan (an endothelin receptor antagonist — **not** valsartan) was protective against renal injury at doses below those causing fluid retention. Provides indirect, class-adjacent (not drug-specific) mechanistic support only. |

---

## Norway Market Information

Valsartan is currently **not marketed** in this jurisdiction (0 authorizations on record). No local product license or approved-indication text is available.

---

## Safety Considerations

Please refer to the package insert for safety information. Note: local prescribing-label warnings and contraindications data (Data Gap DG001) are currently unavailable and are flagged as a **blocking** gap for any formal safety pre-assessment (S1) of this candidate.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The evidence supporting valsartan for malignant hypertensive renal disease is currently limited to a single preclinical study of a different drug class (endothelin antagonist), with no clinical trials and no drug-specific human or animal data. Combined with the absence of confirmed MOA data and local safety labeling, this candidate does not yet meet the threshold to proceed past model-prediction stage (L5/S0).

**To proceed, the following is needed:**
- Confirmed DrugBank mechanism-of-action data for valsartan (Data Gap DG002)
- TFDA/local prescribing information — warnings, contraindications (Data Gap DG001, blocking for S1 safety assessment)
- Drug-specific (valsartan/ARB) preclinical or clinical evidence in hypertensive nephropathy or malignant hypertensive renal disease, rather than indirect class-adjacent literature
- Consideration of the closely related "malignant renovascular hypertension" prediction (rank 2), which has more direct AT1-blockade mechanistic literature and may warrant prioritization as a research question over this candidate
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

