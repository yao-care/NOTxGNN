---
layout: default
title: Pirfenidone
parent: 僅模型預測 (L5)
nav_order: 280
evidence_level: L5
indication_count: 10
---

# Pirfenidone
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

# Pirfenidone: From Idiopathic Pulmonary Fibrosis to Extracutaneous Mastocytoma

## One-Sentence Summary

> Pirfenidone is an oral antifibrotic agent established for the treatment of idiopathic pulmonary fibrosis (IPF), acting through inhibition of TGF-β1- and PDGF-mediated fibroblast proliferation and collagen synthesis.
> The TxGNN model predicts it may be effective for **Extracutaneous Mastocytoma**, with a prediction score of **99.71%**,
> but currently **no clinical trials** and **no publications** support this specific direction — the prediction is model-derived only.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Idiopathic Pulmonary Fibrosis (IPF) — not recorded in the evidence pack; inferred from established drug identity |
| Predicted New Indication | Extracutaneous Mastocytoma |
| TxGNN Prediction Score | 99.71% |
| Evidence Level | L5 |
| Norway Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data for pirfenidone is not available in this evidence pack (flagged as a High-severity data gap, DG002). Based on information surfaced elsewhere in this pack (literature cited under a separate predicted indication), pirfenidone is known to inhibit TGF-β1, PDGF, EGF and FGF signaling, thereby reducing fibroblast proliferation and collagen deposition — the mechanism underlying its approved use in IPF.

Extracutaneous mastocytoma is a rare neoplastic proliferation of mast cells driven primarily by **KIT mutations**, a pathway mechanistically unrelated to TGF-β-driven fibrosis. The repurposing rationale attached to this prediction explicitly notes that the high TxGNN score likely reflects a shared "fibrosis/stromal remodeling" graph neighborhood rather than a genuine mechanistic connection, and states there is **no direct link** between anti-TGF-β activity and KIT-driven mast cell pathology.

Given the absence of any preclinical, clinical trial, or literature support, this prediction should be interpreted as a graph-similarity signal rather than a mechanistically grounded hypothesis.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Norway Market Information

Pirfenidone is **not currently marketed in Norway** (0 authorizations on record). No license or product information is available in this evidence pack.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction score is high, but it is unsupported by any clinical trial, real-world, or literature evidence (Evidence Level L5), and the proposed mechanistic link between anti-fibrotic TGF-β inhibition and KIT-driven mast cell pathology is not established. TFDA/label-level safety data (warnings, contraindications) is also missing (Blocking data gap DG001), which independently prevents any safety pre-assessment.

**To proceed, the following is needed:**
- TFDA-equivalent product labeling — warnings and contraindications (DG001, Blocking)
- Confirmed mechanism of action data for pirfenidone (DG002, High)
- Preclinical evidence directly linking anti-fibrotic activity to mast cell tumor biology
- **Note:** a separate candidate in this pack, *fibroblastic neoplasm* (rank 9, Evidence Level L4/S1), has meaningfully more support (6 publications, including a pilot cohort on desmoid tumors) but also carries a safety red flag — two case reports of sarcoma progression and dermatofibroma aggravation following pirfenidone use. This candidate warrants separate causality review and may be a more actionable priority than the current top-ranked prediction.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

