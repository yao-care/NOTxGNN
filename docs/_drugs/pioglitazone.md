---
layout: default
title: Pioglitazone
parent: 僅模型預測 (L5)
nav_order: 279
evidence_level: L5
indication_count: 9
---

# Pioglitazone
{: .fs-9 }

證據等級: **L5** | 預測適應症: **9** 個
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

# Pioglitazone: From Type 2 Diabetes Mellitus to Opsismodysplasia

## One-Sentence Summary

Pioglitazone is a thiazolidinedione (TZD)-class insulin sensitizer historically used for type 2 diabetes mellitus.
The TxGNN model's top-ranked prediction in this evidence pack is **Opsismodysplasia**, a rare skeletal dysplasia,
but this candidate has **0 clinical trials** and **0 supporting publications**, and the model's own rationale flags it as likely knowledge-graph noise rather than a genuine signal.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Type 2 Diabetes Mellitus (based on known pharmacology; no Norway license/indication text available in this evidence pack) |
| Predicted New Indication | Opsismodysplasia |
| TxGNN Prediction Score | 99.59% |
| Evidence Level | L5 |
| Norway Market Status | ✗ Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | **Hold** |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available (data gap DG002, flagged as High severity). Based on known information, pioglitazone is a PPAR-γ agonist that acts as an insulin sensitizer, with established efficacy in type 2 diabetes through improved peripheral glucose uptake and pancreatic beta-cell function preservation.

Opsismodysplasia, however, is a genetic skeletal dysplasia caused by *INPPL1* mutations affecting bone growth-plate signaling. There is no established mechanistic pathway connecting PPAR-γ agonism to *INPPL1*-mediated skeletal development. The evidence pack's own repurposing rationale is explicit on this point: the high TxGNN score likely reflects sparse knowledge-graph connectivity around this rare-disease node rather than a real pharmacological relationship, and the drug's actual rank (4832) among all candidate diseases is far outside any range that would normally support prioritization.

Given the absence of any clinical trial, observational, or mechanistic literature specific to this pairing, this prediction should be treated as a hypothesis-generation artifact rather than an actionable repurposing lead.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Norway Market Information

Pioglitazone is not currently marketed in Norway under this evidence pack (`market_status: 未上市`, `total_licenses: 0`). No authorization records are available for review.

---

## Other Candidate Indications Considered (Not Prioritized)

The evidence pack included 8 additional low-ranked candidates, all similarly assessed as L5 / Hold due to weak or absent mechanistic and clinical support:

| Rank | Disease | TxGNN Score | Key Issue |
|------|---------|-------------|-----------|
| 2 | Focal stiff limb syndrome | 99.50% | Autoimmune/GABA-ergic disease; no mechanistic or empirical link to PPAR-γ |
| 3 | Classic stiff person syndrome | 99.50% | Same as above |
| 4 | Thiamine-responsive dysfunction syndrome | 99.48% | Underlying defect (SLC19A2) not addressed by insulin sensitization |
| 5 | Drug-induced localized lipodystrophy | 99.30% | Mechanistically contradictory — TZDs are also known to *cause* fat redistribution |
| 6 | Centrifugal lipodystrophy | 99.26% | Pediatric, idiopathic; no supporting evidence |
| 7 | Pressure-induced localized lipoatrophy | 99.24% | Mechanical/local etiology; weak systemic PPAR-γ link |
| 8 | Idiopathic localized lipodystrophy | 99.19% | Etiology unknown; no directed evidence |
| 9 | Pancreatic agenesis | 99.18% | 9 retrieved publications are all general T2DM/TZD reviews — keyword mismatch, not disease-specific evidence |

None of the 9 candidates reach beyond L5 evidence, and none currently justify escalation past model-prediction stage.

---

## Safety Considerations

Please refer to the package insert for safety information. (Key warnings, contraindications, and drug interaction data are not available in this evidence pack — DG001 is flagged as a Blocking data gap, preventing initial safety-stage evaluation.)

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
All 9 predicted indications are L5 (model prediction only), with no clinical trials and either no literature or literature that is mismatched to the specific disease. The top-ranked candidate (opsismodysplasia) has no plausible mechanistic pathway and is explicitly flagged by the model's own rationale as likely graph noise. Combined with a Blocking safety data gap (DG001) and absent MOA data (DG002), there is currently no basis to advance any candidate past S0.

**To proceed, the following is needed:**
- Resolve DG001: obtain TFDA/regulatory label warnings and contraindications for pioglitazone
- Resolve DG002: confirm detailed MOA via DrugBank API query
- If pursuing the pancreatic agenesis candidate (rank 9), manually verify whether any of the 9 retrieved publications are truly disease-specific rather than general T2DM/TZD reviews
- Given the uniformly weak signal across all 9 candidates, consider re-running TxGNN with rank-based (not raw score) thresholding before further evidence collection is commissioned
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

