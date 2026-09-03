---
layout: default
title: Cannabidiol
parent: 僅模型預測 (L5)
nav_order: 73
evidence_level: L5
indication_count: 0
---

# Cannabidiol
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

# Cannabidiol: Repurposing Evaluation Pending — Insufficient Data to Complete Analysis

## One-Sentence Summary

Cannabidiol (CBD) is a phytocannabinoid compound (DrugBank ID: DB09061); however, the current Evidence Pack contains no original indication records, no TxGNN-predicted new indications, and no mechanism of action or safety data.
A full repurposing evaluation **cannot be completed at this time** — this report documents the current state of data collection and the gaps that must be resolved before the candidate can advance.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | No data available |
| Predicted New Indication | No TxGNN prediction available |
| TxGNN Prediction Score | N/A |
| Evidence Level | N/A — no predictions generated |
| Taiwan Market Status | ✗ Not marketed (0 authorizations) |
| Number of Authorizations | 0 |
| Recommended Decision | **Hold** |

---

## Why is This Prediction Reasonable?

Currently, no predicted indication has been generated for Cannabidiol in this Evidence Pack. The TxGNN model either has not yet been run for this candidate, or the candidate was filtered out prior to prediction.

Additionally, detailed mechanism of action data is not available in the current dataset. Without MOA information, it is not possible to establish a mechanistic link between Cannabidiol and any proposed new indication.

Until TxGNN predictions are generated and MOA data is retrieved from DrugBank, this section cannot be meaningfully completed.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for any predicted indication.

*(No predicted indications were provided in this Evidence Pack.)*

---

## Literature Evidence

Currently no related literature available for any predicted indication.

*(No predicted indications were provided in this Evidence Pack.)*

---

## Taiwan Market Information

Cannabidiol currently holds **no drug authorizations** in Taiwan. No licensed products are on record.

---

## Safety Considerations

Please refer to the package insert for safety information.

> The current Evidence Pack contains no usable safety data. Key warnings, contraindications, and drug-drug interaction records all require remediation before a safety evaluation can proceed (see **Data Gaps** below).

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The Evidence Pack is incomplete in all critical domains — there are no TxGNN-predicted indications, no mechanism of action data, no original indication records, and no safety data. There is currently no basis on which to evaluate this candidate for drug repurposing.

**To proceed, the following is needed:**

| Priority | Gap ID | Item | Action Required |
|----------|--------|------|-----------------|
| 🔴 Blocking | DG001 | Safety warnings & contraindications | Download and parse TFDA package insert PDF from the TFDA website |
| 🟠 High | DG002 | Mechanism of action (MOA) | Query DrugBank API for DB09061 pharmacology data |
| 🟠 High | — | TxGNN predicted indications | Re-run TxGNN pipeline for Cannabidiol; confirm the candidate was not incorrectly excluded |
| 🟡 Medium | — | Original indication records | Populate `original_indications` from DrugBank approved indications or WHO/EMA label data |
| 🟡 Medium | — | Drug-drug interaction data | Re-query DDI database (current result: `not_found`; verify query parameters) |

Once the Blocking and High-priority gaps are resolved, this candidate should be re-evaluated with a new Evidence Pack version.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

