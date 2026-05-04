---
layout: default
title: Abaloparatide
parent: 僅模型預測 (L5)
nav_order: 12
evidence_level: L5
indication_count: 4
---

# Abaloparatide
{: .fs-9 }

證據等級: **L5** | 預測適應症: **4** 個
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

# ABALOPARATIDE: Drug Repurposing Evaluation Report

## One-Sentence Summary

Abaloparatide (DB05084) is a synthetic analog of parathyroid hormone-related protein (PTHrP), primarily used for the treatment of postmenopausal osteoporosis at high risk of fracture. The TxGNN model currently has **no predicted new indications** for this drug, and the evidence pack contains significant data gaps that prevent a full evaluation.

---

## Quick Overview

| Item | Content |
|------|------|
| Drug Name (INN) | ABALOPARATIDE |
| DrugBank ID | DB05084 |
| Original Indication | Not recorded in evidence pack (known use: postmenopausal osteoporosis) |
| Predicted New Indication | — (No TxGNN prediction available) |
| TxGNN Prediction Score | — |
| Evidence Level | L5 (No prediction, no supporting studies) |
| Taiwan Market Status | ✗ Not marketed (未上市) |
| Number of Authorizations | 0 |
| Recommended Decision | **Hold** |

---

## Why is This Prediction Reasonable?

Currently, the TxGNN model has not generated any repurposing predictions for abaloparatide. Without a predicted indication, mechanism-based plausibility analysis cannot be performed.

Based on publicly available knowledge, abaloparatide is a synthetic 34-amino-acid peptide analog of human parathyroid hormone-related protein (PTHrP(1-34)). It selectively activates the PTH1 receptor in its RG conformation, stimulating osteoblast-mediated bone formation while having a relatively lower effect on bone resorption compared to teriparatide. This anabolic mechanism increases bone mineral density and reduces fracture risk.

> ⚠️ The evidence pack lists the mechanism of action (MOA) as a data gap. The description above is based on established pharmacological literature. A formal MOA entry from DrugBank should be obtained to support any future analysis.

---

## Clinical Trial Evidence

Currently no TxGNN-predicted indication is available; therefore, no targeted clinical trial search was conducted for repurposing candidates.

---

## Literature Evidence

Currently no TxGNN-predicted indication is available; therefore, no targeted literature search was conducted for repurposing candidates.

---

## Taiwan Market Information

Abaloparatide is **not marketed in Taiwan**. No TFDA drug licenses were found.

| Item | Detail |
|------|--------|
| TFDA License Count | 0 |
| Market Status | 未上市 (Not marketed) |
| Dosage Forms Available | None |

---

## Safety Considerations

> Please refer to the package insert for safety information.
>
> All safety fields (key warnings, contraindications, and drug-drug interactions) returned as data gaps or not found in the current evidence pack. A TFDA package insert or international reference (e.g., US FDA Tymlos label) should be consulted before any clinical evaluation proceeds.

**Known data gaps:**
- TFDA package insert warnings/contraindications (Severity: **Blocking** — prevents Stage 1 safety screening)
- Drug-drug interaction profile: query returned no results

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
There are no TxGNN-predicted new indications for abaloparatide at this time, and the drug is not marketed in Taiwan. Multiple critical data gaps (MOA, safety profile) further prevent meaningful evaluation. The candidate cannot proceed to any stage of repurposing assessment in its current state.

**To proceed, the following is needed:**
1. **TxGNN prediction rerun** — Confirm whether abaloparatide is included in the knowledge graph; if not, evaluate whether its drug–disease edges can be incorporated
2. **Mechanism of action (MOA)** — Retrieve formal MOA data from DrugBank API (Data Gap DG002, severity: High)
3. **Safety profile** — Obtain TFDA package insert or reference international labeling (Data Gap DG001, severity: Blocking)
4. **Regulatory pathway assessment** — Since abaloparatide has zero Taiwan licenses, any repurposing effort would require a full new drug application or special import pathway rather than indication expansion

---

*Report generated: 2026-04-03 | Evidence Pack version: v4 | Candidate ID: TW-DB05084-multi*

*⚠️ This report is for research reference only and does not constitute medical advice. Any drug repurposing candidate requires clinical validation before application.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

