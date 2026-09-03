---
layout: default
title: Evolocumab
parent: 僅模型預測 (L5)
nav_order: 145
evidence_level: L5
indication_count: 6
---

# Evolocumab
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

# Evolocumab: TxGNN-Predicted Link to Symptomatic Hemophilia in Female Carriers (Low-Confidence)

## One-Sentence Summary

> This evidence pack does not record evolocumab's original approved indication, and the drug currently holds no marketing license in Taiwan.
> TxGNN's top-ranked prediction suggests a possible link to **symptomatic form of hemophilia in female carriers** (score 99.82%),
> but this is backed by **zero clinical trials** and **zero publications** — and the pack's own mechanistic analysis flags the link as probable knowledge-graph noise rather than a real pharmacological connection.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not on file (no Taiwan license record; `original_indications` empty in this evidence pack) |
| Predicted New Indication | Symptomatic form of hemophilia in female carriers |
| TxGNN Prediction Score | 99.82% (rank 2444) |
| Evidence Level | L5 (model prediction only, no supporting trials/literature) |
| Taiwan Market Status | 未上市 (Not marketed) |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

According to the mechanistic notes embedded in this evidence pack, evolocumab is a **PCSK9 monoclonal antibody**: it inhibits PCSK9-mediated degradation of LDL receptors, thereby lowering blood LDL-C. This places the drug's known biology firmly within lipid metabolism, not coagulation.

Hemophilia in female carriers arises from Factor VIII (F8) gene deficiency and involves the intrinsic coagulation cascade — a pathway that has **no documented mechanistic overlap** with PCSK9/LDL-receptor biology. The evidence pack's own rationale for this prediction states explicitly that there is no known interaction or shared pathway between the two, and concludes the high TxGNN score most likely reflects **knowledge-graph proximity noise** rather than a genuine pharmacological signal.

This assessment is reinforced by the pattern across the other five ranked candidates in this pack (familial ApoC-II deficiency, thrombocytopenic purpura, Factor XI deficiency, hemophilia A with vascular abnormality, and a non-specific ontology superclass "disease of catalytic activity") — all carry the same L5/Hold status, no trials, no literature, and rationale text that independently argues against mechanistic plausibility. This is not typical of a strong repurposing signal.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Taiwan Market Information

Evolocumab currently holds **no marketing authorization in Taiwan** (0 licenses on file). No dosage form or approved indication text is available for this jurisdiction.

---

## Safety Considerations

Please refer to the package insert for safety information.

*(Note: key warnings, contraindications, and drug-interaction data are all flagged as data gaps in this evidence pack — including TFDA label data, listed as a Blocking gap (DG001). This must be resolved before any S1 safety review can proceed.)*

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN score is high, but there are zero clinical trials, zero publications, and no Taiwan regulatory data to support this prediction. More importantly, the pack's own mechanistic rationale independently concludes that the PCSK9/LDL pathway has no known connection to hemophilia pathophysiology, suggesting the score reflects graph artifact rather than biological signal.

**To proceed, the following is needed:**
- TFDA-equivalent product label (warnings/contraindications) — currently Blocking (DG001)
- Verified mechanism of action data from DrugBank or primary literature (DG002)
- Confirmed original indication(s) for evolocumab in this dataset
- An independent literature/clinical-trial search specifically for evolocumab in bleeding disorders, to confirm or rule out the TxGNN signal before any further scoring
- Consideration of whether this candidate (and its sibling predictions in this pack) should be deprioritized in favor of TxGNN candidates with actual trial/literature support
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

