---
layout: default
title: Siltuximab
parent: 僅模型預測 (L5)
nav_order: 324
evidence_level: L5
indication_count: 8
---

# Siltuximab
{: .fs-9 }

證據等級: **L5** | 預測適應症: **8** 個
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

# Siltuximab: From Multicentric Castleman Disease to Extracutaneous Mastocytoma

## One-Sentence Summary

> Siltuximab is an anti-IL-6 chimeric monoclonal antibody, established for the treatment of HHV-8-negative multicentric Castleman disease.
> The TxGNN model predicts it may be effective for **Extracutaneous Mastocytoma**,
> but this direction is currently supported by **0 clinical trials** and **0 publications** — it is a pure model prediction with no mechanistic or clinical corroboration.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Multicentric Castleman Disease (HHV-8 negative) *(not present in the drug/regulatory record; inferred from the mechanistic rationale provided for the Kaposi's sarcoma candidate)* |
| Predicted New Indication | Extracutaneous Mastocytoma |
| TxGNN Prediction Score | 99.64% |
| Evidence Level | L5 (model prediction only) |
| Norway Market Status | Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available (flagged as a High-severity data gap). Based on the mechanistic notes accompanying this evidence pack, siltuximab is an anti-IL-6 chimeric monoclonal antibody that blocks IL-6/STAT3 signaling, and its efficacy in multicentric Castleman disease — a cytokine-driven lymphoproliferative disorder — is well established.

Extracutaneous mastocytoma is a rare, localized mast-cell tumor. There is a loose biological rationale in that IL-6 levels have been observed to correlate with disease burden in some mast-cell disorders, but the evidence pack explicitly notes that **no direct mechanistic data support IL-6 as a key driver of this specific, rare tumor subtype**. This prediction is therefore a high-scoring model output without any corroborating mechanistic, clinical, or literature evidence, consistent with its L5 evidence level and "Hold" recommendation.

It is worth noting that other predictions in this pack — particularly hepatic veno-occlusive disease (rank 3, endothelial injury with IL-6 elevation post-HSCT) and Kaposi's sarcoma (rank 5, viral IL-6 from KSHV/HHV-8 overlapping with siltuximab's approved Castleman disease indication) — carry somewhat stronger biological plausibility than the top-ranked extracutaneous mastocytoma prediction, though none currently have direct clinical evidence for siltuximab use.

---

## Clinical Trial Evidence

Currently no related clinical trials registered

---

## Literature Evidence

Currently no related literature available

---

## Norway Market Information

Siltuximab currently has no marketing authorization records in Norway (0 authorizations; market status: Not Marketed).

---

## Safety Considerations

Please refer to the package insert for safety information. (TFDA label warnings/contraindications are flagged as a Blocking data gap — see Next Steps.)

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked prediction (extracutaneous mastocytoma) has no supporting clinical trials or literature, and the drug's own mechanism-of-action data is missing — evidence is insufficient to proceed beyond model-prediction stage (L5).

**To proceed, the following is needed:**
- TFDA label data (warnings/contraindications) — currently a Blocking gap preventing S1 safety pre-screening
- Confirmed mechanism-of-action (MOA) data from DrugBank to support mechanistic-link analysis
- Disease-specific preclinical or case-level evidence for extracutaneous mastocytoma before any further evaluation
- Consider re-prioritizing evaluation toward candidates with stronger mechanistic plausibility already noted in this pack (e.g., hepatic veno-occlusive disease, Kaposi's sarcoma), pending dedicated evidence searches for those indications
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

