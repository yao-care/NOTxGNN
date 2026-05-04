---
layout: default
title: Abatacept
parent: 僅模型預測 (L5)
nav_order: 13
evidence_level: L5
indication_count: 10
---

# Abatacept
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

# ABATACEPT: Drug Repurposing Preliminary Assessment

## One-Sentence Summary

Abatacept (DrugBank: DB01281) is a selective T-cell co-stimulation modulator (CTLA4-Ig fusion protein), widely used internationally for rheumatoid arthritis and other autoimmune conditions. Currently, **no TxGNN predicted indications** are available for evaluation, and the drug is **not marketed in Taiwan**. This report serves as a preliminary data inventory; further data collection is required before repurposing assessment can proceed.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available in evidence pack (no Taiwan licenses) |
| Predicted New Indication | None — TxGNN prediction not yet available |
| TxGNN Prediction Score | N/A |
| Evidence Level | L5 (Insufficient data) |
| Taiwan Market Status | ✗ Not marketed (未上市) |
| Number of Authorizations | 0 |
| Recommended Decision | **Hold** |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the evidence pack. Based on publicly known information, Abatacept is a soluble fusion protein consisting of the extracellular domain of human CTLA-4 linked to the modified Fc portion of human IgG1. It functions as a selective T-cell co-stimulation modulator by binding to CD80/CD86 on antigen-presenting cells, thereby blocking the CD28 co-stimulatory signal required for full T-cell activation.

Internationally, Abatacept (brand name: Orencia®) has been approved for rheumatoid arthritis, juvenile idiopathic arthritis, and psoriatic arthritis. However, these indications are **not reflected in the current evidence pack** as the drug holds no Taiwan FDA (TFDA) marketing authorization.

Since no TxGNN-predicted indications have been generated, it is not possible to evaluate mechanistic plausibility for any specific repurposing candidate at this time. The TxGNN model prediction pipeline should be run with Abatacept's knowledge graph data to identify potential new indications.

## Clinical Trial Evidence

No predicted indication is available; therefore, no indication-specific clinical trial search was conducted.

## Literature Evidence

No predicted indication is available; therefore, no indication-specific literature search was conducted.

## Taiwan Market Information

Abatacept currently holds **no marketing authorization** from the Taiwan FDA (TFDA). There are no licensed products in Taiwan.

## Safety Considerations

> Please refer to the package insert for safety information.
>
> Note: TFDA package insert warnings, contraindications, and drug-drug interaction data were not retrievable for this drug (no Taiwan marketing authorization exists). Safety evaluation should reference international labelling (e.g., US FDA, EMA) if a repurposing candidate is identified.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The evidence pack is critically incomplete — there are no TxGNN-predicted indications to evaluate, no Taiwan market authorization data, and no locally available safety labelling. Without a target indication, a repurposing assessment cannot proceed.

**To proceed, the following is needed:**
- **Run TxGNN prediction pipeline** for Abatacept (DB01281) to generate candidate repurposing indications
- **Obtain mechanism of action (MOA) data** from DrugBank API (Data Gap DG002, severity: High)
- **Obtain safety labelling data** — either from TFDA (if future approval occurs) or from international regulatory sources such as the US FDA or EMA (Data Gap DG001, severity: Blocking)
- **Assess Taiwan regulatory pathway** — since Abatacept is not currently marketed in Taiwan, determine whether importation or special access programs would be feasible for any identified repurposing indication
- **Re-evaluate** once predicted indications and safety data are available
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

