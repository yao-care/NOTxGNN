---
layout: default
title: Inclisiran
parent: 僅模型預測 (L5)
nav_order: 180
evidence_level: L5
indication_count: 10
---

# Inclisiran
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

# Inclisiran: From Hypercholesterolemia to Potassium Deficiency Disease

## One-Sentence Summary

> Inclisiran (DB14901) is a PCSK9-targeted siRNA; its originally approved indication is not captured in this evidence pack (Norway licensing data is empty — the drug is currently **not marketed**).
> TxGNN's top-ranked prediction in this batch is **Potassium Deficiency Disease** (score 99.93%),
> but this signal is supported by **0 clinical trials** and **0 publications** — it is a pure model artifact with no biological rationale, and the internal scoring engine itself flags it as **Hold**.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available — `taiwan_regulatory.licenses` is empty in this evidence pack. (General pharmacological background, not from this dataset: inclisiran is a PCSK9-directed siRNA used for LDL-C lowering/ASCVD risk reduction.) |
| Predicted New Indication | Potassium deficiency disease |
| TxGNN Prediction Score | 99.93% |
| Evidence Level | L5 (model prediction only, no supporting studies) |
| Norway Market Status | ✗ Not Marketed (未上市) |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available for inclisiran in this evidence pack (`original_moa: [Data Gap]`). Based on general pharmacological knowledge, inclisiran is a small interfering RNA (siRNA) that silences hepatic PCSK9 mRNA translation, thereby increasing LDL-receptor recycling and lowering circulating LDL cholesterol.

For the top-ranked prediction in this batch — **potassium deficiency disease** — the evidence pack's own mechanistic assessment explicitly states there is **no known biological relationship** between the PCSK9/LDL-receptor pathway and potassium homeostasis, and **no trial or literature evidence** exists to support the link. This is consistent with a high TxGNN embedding-similarity score that does not correspond to plausible pharmacology — a known failure mode of pure graph-embedding predictions when unconstrained by mechanistic filters.

Given this, the prediction should **not** be interpreted as a genuine repurposing signal. It is retained in this report for transparency and audit purposes only.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Norway Market Information

Inclisiran is currently **not marketed** in Norway — `taiwan_regulatory.market_status = "未上市"`, with **0 authorizations** on file. No license records are available to summarize.

---

## Other Candidates in This Batch (Context)

This evidence pack ("TW-DB14901-multi") contains 10 TxGNN-ranked predictions for inclisiran, most of which share the same problem as the top hit — high score, zero evidence, "Hold." One candidate stands out as materially different and warrants separate follow-up:

| Rank | Disease | TxGNN Score | Evidence Level | Decision Stage | Recommendation | Note |
|------|---------|-------------|-----------------|------------------|-----------------|------|
| 1 | Potassium deficiency disease | 99.93% | L5 | S0 | Hold | No mechanistic link, no evidence |
| 2 | Esophageal disease | 99.87% | L5 | S0 | Hold | No evidence |
| 4 | Migraine disorder | 99.83% | L5 | S0 | Hold | No evidence |
| 7 | Migraine w/ or w/o aura, susceptibility | 99.78% | L5 | S0 | Hold | 20 papers retrieved, but all on epilepsy/migraine genetics — none address PCSK9/lipid pathways |
| **8** | **Aortic malformation** | **99.76%** | **L4** | **S1** | **Research Question** | **2 active Phase 3 pediatric FH trials (NCT06597006, NCT06597019); plausible mechanistic link via LDL-C-driven vascular/valvular lipid deposition, but trial inclusion criteria (HoFH/HeFH) need manual verification against "aortic malformation" as a MeSH-level term** |
| 9 | Esophageal ulcer | 99.73% | L5 | S0 | Hold | No evidence |
| 10 | Raynaud disease | 99.73% | L5 | S0 | Hold | No evidence |

Rank 8 ("aortic malformation") is the only candidate in this batch that reached decision stage S1 with real clinical trial backing, and is the more appropriate target for a dedicated follow-up evaluation report — not the top-ranked "potassium deficiency disease" entry.

---

## Safety Considerations

Please refer to the package insert for safety information. `safety.key_warnings`, `safety.contraindications`, and `safety.ddi` are all marked as data gaps in this evidence pack (see DG001, "Blocking" severity — TFDA/label warnings not yet retrieved).

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked prediction (potassium deficiency disease) has a very high TxGNN score but zero corroborating clinical or literature evidence, and the pack's own rationale confirms no biological plausibility. This is a model-artifact signal, not a genuine repurposing candidate.

**To proceed, the following is needed:**
- Resolve DG001 (Blocking): retrieve TFDA/Norway label warnings and contraindications before any S1 safety screening can begin for this drug
- Resolve DG002 (High): pull structured MOA data from DrugBank to properly evaluate mechanistic plausibility across all candidates
- If continuing repurposing exploration for inclisiran, redirect focus to **rank 8 (aortic malformation)** — verify actual inclusion criteria of NCT06597006/NCT06597019 against the predicted indication term before advancing to S2
- Populate `taiwan_regulatory.licenses` / `original_indications` — currently empty, blocking a complete original-vs-new indication comparison
- Do not advance "potassium deficiency disease," "esophageal disease/ulcer/malformation," "migraine," or "Raynaud disease" without new supporting evidence — all currently L5/Hold
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

