---
layout: default
title: Brinzolamide
parent: 僅模型預測 (L5)
nav_order: 58
evidence_level: L5
indication_count: 1
---

# Brinzolamide
{: .fs-9 }

證據等級: **L5** | 預測適應症: **1** 個
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

# Brinzolamide: From Glaucoma to Primary Hereditary Glaucoma

## One-Sentence Summary

Brinzolamide is a carbonic anhydrase (CA-II/CA-IV) inhibitor used topically to lower intraocular pressure in glaucoma and ocular hypertension. The TxGNN model predicts it may also be effective for **Primary Hereditary Glaucoma**, a genetically distinct glaucoma subtype, but this prediction is currently supported by **no clinical trials or published literature** — it is a model-only signal.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available in current data source (DrugBank field empty) |
| Predicted New Indication | Primary Hereditary Glaucoma |
| TxGNN Prediction Score | 99.48% |
| Evidence Level | L5 |
| Taiwan Market Status | ✗ Not marketed (未上市) |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the structured `original_moa` field. However, based on the repurposing rationale supplied with this evidence pack, brinzolamide is known to act as a carbonic anhydrase (CA-II/CA-IV) inhibitor, acting locally on the ciliary body epithelium to reduce aqueous humor production and lower intraocular pressure — the established pharmacological basis for treating primary open-angle glaucoma and ocular hypertension.

The predicted new indication, primary hereditary glaucoma, shares the same downstream pathophysiology (elevated intraocular pressure from aqueous humor dynamics imbalance) as the drug's established use. This makes the mechanistic link plausible at the level of intraocular pressure control.

However, primary hereditary glaucoma is a genetically defined subtype (e.g., associated with *MYOC* or *CYP1B1* mutations) with a distinct etiology from sporadic open-angle glaucoma. Whether CA inhibition adequately addresses the underlying disease process in these genetic subtypes — rather than simply managing a shared downstream symptom (elevated IOP) — has not been established. This should therefore not be treated as a straightforward extension of an existing approved indication, but as a hypothesis requiring dedicated evidence.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Taiwan Market Information

Brinzolamide currently holds no marketing authorization in this jurisdiction (0 licenses on record); no product listing is available.

---

## Safety Considerations

Please refer to the package insert for safety information. Note: TFDA label warnings/contraindications data has not yet been retrieved (data gap, blocking severity — required before any Stage 1 safety assessment can proceed).

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN prediction score is high, but there is zero clinical trial or literature evidence, and the predicted indication (a genetic glaucoma subtype) is mechanistically distinct enough from the drug's established use that mechanism alone is insufficient support. This is an L5, model-only signal.

**To proceed, the following is needed:**
- TFDA label warnings/contraindications (blocking gap — required before any safety evaluation)
- Confirmed original indication and MOA from DrugBank or label source
- Preclinical or genetic-subtype-specific evidence linking CA inhibition to hereditary glaucoma pathophysiology (not just IOP control)
- Any case reports, registries, or trials specifically in hereditary/genetic glaucoma populations
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

