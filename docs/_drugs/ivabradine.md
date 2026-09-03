---
layout: default
title: Ivabradine
parent: 僅模型預測 (L5)
nav_order: 192
evidence_level: L5
indication_count: 6
---

# Ivabradine
{: .fs-9 }

證據等級: **L5** | 預測適應症: **6** 個
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

# Ivabradine: From Chronic Heart Failure/Angina to Hypertrichosis

## One-Sentence Summary

Ivabradine is a selective HCN (If, "funny current") channel blocker that slows sinoatrial node firing, used clinically for chronic heart failure and stable angina. The TxGNN model predicts it may be effective for **Hypertrichosis (disease)**, but this prediction is currently supported by **0 clinical trials** and **0 publications**, and the evidence pack itself notes no known mechanistic link between HCN-channel inhibition and hair growth regulation.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not specified in evidence pack (drugbank `original_indications` field empty) |
| Predicted New Indication | Hypertrichosis (disease) |
| TxGNN Prediction Score | 99.79% |
| Evidence Level | L5 |
| Norway Market Status | ✗ Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed original-indication and formal MOA fields are not populated in this evidence pack. However, the pack's own repurposing rationale describes ivabradine as a selective HCN channel blocker acting at the sinoatrial node to reduce heart rate, used for chronic heart failure and stable angina.

There is no established biological pathway connecting sinoatrial HCN-channel inhibition to hair follicle growth regulation (e.g., Wnt/β-catenin signaling or androgen receptor pathways implicated in hypertrichosis). The evidence pack explicitly states this candidate arises purely from graph-embedding similarity in the TxGNN model, without direct or indirect clinical or mechanistic support.

The same pattern holds across all six predicted indications in this pack — hypertrichosis, Ambras syndrome, periodontal malformation syndrome, Dandy-Walker malformation, hair shaft abnormality, and nephrogenic syndrome of inappropriate antidiuresis. Each rationale text independently flags the lack of a plausible mechanistic connection to HCN-channel pharmacology, and the periodontal-disease literature retrieved (rank 3) consists of general periodontology reviews that never mention ivabradine, indicating keyword-matching noise rather than drug-specific evidence.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Norway Market Information

Ivabradine is not marketed in Norway under this evidence pack (`market_status: 未上市`, 0 total licenses). No authorization records are available to list.

---

## Safety Considerations

Please refer to the package insert for safety information.

*(Note: the underlying evidence pack flags TFDA warnings/contraindications data as a **Blocking** data gap (DG001), meaning a formal safety screen (S1) cannot currently be performed for this candidate.)*

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
All six TxGNN-predicted indications for ivabradine are rated L5 (model prediction only), with zero supporting clinical trials and no drug-specific literature. The evidence pack's own mechanistic rationale for the top-ranked prediction (hypertrichosis) explicitly states there is no known biological link to ivabradine's HCN-channel mechanism. Combined with the drug's unmarketed status in Norway and a Blocking-severity gap in TFDA safety labeling data, there is no basis to advance this candidate beyond the discovery stage.

**To proceed, the following is needed:**
- TFDA/regulatory label data (warnings, contraindications) — currently Blocking gap (DG001)
- Confirmed mechanism of action data from DrugBank (DG002)
- Any preclinical or mechanistic study directly linking HCN-channel modulation to hair follicle biology or the other predicted phenotypes
- Re-evaluation if future TxGNN model updates surface higher-confidence, mechanistically plausible indications for this compound
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

