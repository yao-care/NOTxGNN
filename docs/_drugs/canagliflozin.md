---
layout: default
title: Canagliflozin
parent: 僅模型預測 (L5)
nav_order: 70
evidence_level: L5
indication_count: 0
---

# Canagliflozin
{: .fs-9 }

證據等級: **L5** | 預測適應症: **0** 個
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

# Canagliflozin: Drug Repurposing Evaluation — Prediction Data Unavailable

## One-Sentence Summary

Canagliflozin (DrugBank DB08907) is a drug under evaluation for repurposing potential via the TxGNN model. However, **this Evidence Pack contains no TxGNN prediction results**, and both the original indication data and mechanism of action are currently absent. This report serves as a **data gap summary** and remediation roadmap rather than a full repurposing evaluation.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | No data available in this Evidence Pack |
| Predicted New Indication | No TxGNN prediction results available |
| TxGNN Prediction Score | — |
| Evidence Level | L5 (model prediction not yet available) |
| Norway Market Status | Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | **Hold** |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this Evidence Pack (Data Gap DG002). The `original_moa` field is missing, and no original indications have been recorded in the regulatory data.

Based on publicly available pharmacological knowledge, Canagliflozin belongs to the sodium-glucose cotransporter-2 (SGLT2) inhibitor class. This class acts by blocking glucose reabsorption in the proximal tubule of the kidney, leading to glucosuria and blood glucose reduction. Beyond glycaemic control, SGLT2 inhibitors have demonstrated cardiovascular and renal protective effects that are partially independent of their glucose-lowering mechanism — making them of interest in metabolic, cardiac, and renal repurposing contexts.

However, because the `predicted_indications` array in this Evidence Pack is empty, **no formal TxGNN repurposing prediction has been loaded**. A mechanistic rationale for any specific new indication cannot be confirmed from this data alone. Re-running the TxGNN pipeline with complete drug–disease graph embeddings is required before proceeding with repurposing evaluation.

---

## Clinical Trial Evidence

Currently no related clinical trials registered in this Evidence Pack.

---

## Literature Evidence

Currently no related literature available in this Evidence Pack.

---

## Norway Market Information

Canagliflozin has **no registered authorizations** in Norway based on the current Evidence Pack. No license records are available.

---

## Safety Considerations

Please refer to the package insert for safety information.

> **Note:** Key warnings, contraindications, and drug–drug interaction data are all absent from this Evidence Pack. The data gap DG001 (TFDA package insert warnings) is classified as **Blocking severity**, meaning safety assessment cannot proceed until this gap is resolved.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
This Evidence Pack is critically incomplete — the `predicted_indications` array is empty, MOA data is missing, safety data is unavailable, and there are no Norwegian regulatory records. There is insufficient basis to evaluate any repurposing hypothesis at this stage.

**To proceed, the following is needed:**

- **[Blocking — DG001]** Obtain and parse the TFDA package insert PDF to extract key warnings and contraindications
- **[High — DG002]** Query DrugBank API for Canagliflozin MOA, pharmacodynamics, and drug categories
- **[Critical]** Re-run the TxGNN prediction pipeline to populate `predicted_indications` — this is the core deliverable without which no repurposing evaluation is possible
- Verify Norway/EMA regulatory status via the Norwegian Medicines Agency (NoMA / Legemiddelverket) to confirm whether any authorizations exist under brand names (e.g., Invokana, Vokanamet)
- After obtaining DDI data, perform drug interaction screening against common co-medications relevant to the candidate indication
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

