---
layout: default
title: Turoctocog Alfa
parent: 僅模型預測 (L5)
nav_order: 373
evidence_level: L5
indication_count: 10
---

# Turoctocog Alfa
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

# Turoctocog Alfa: From Factor VIII Replacement to Primary Release Disorder of Platelets

## One-Sentence Summary

Turoctocog alfa is a recombinant Factor VIII (FVIII) product; per the evidence pack's own mechanistic annotations, its established therapeutic role is FVIII replacement (e.g., Factor VIII deficiency/Hemophilia A), though this evidence pack does not contain confirmed original-indication or MOA data. TxGNN's top prediction is **Primary Release Disorder of Platelets**, but **0 clinical trials** and **0 publications** currently support this direction, and the model's own rationale states the mechanistic link is weak (a platelet granule-release defect, not a coagulation-factor pathway defect).

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not specified in evidence pack (data gap). Rationale annotations describe the drug as recombinant FVIII, typically used for Factor VIII deficiency (Hemophilia A) |
| Predicted New Indication | Primary Release Disorder of Platelets |
| TxGNN Prediction Score | 99.99% |
| Evidence Level | L5 |
| Norway Market Status | 未上市 (Not marketed) |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available for turoctocog alfa in this evidence pack (MOA = Data Gap). Based on the mechanistic rationale annotations attached to each prediction, the drug is understood to be a recombinant Factor VIII (FVIII) replacement product, whose established pharmacology operates in the secondary hemostasis pathway (thrombin generation).

The top-ranked predicted indication, Primary Release Disorder of Platelets, involves a defect in platelet granule release — a **primary hemostasis** mechanism unrelated to the coagulation-factor cascade that FVIII acts on. The evidence pack's own `repurposing_rationale.mechanistic_link` field states this explicitly: *"為血小板顆粒釋放機制缺陷，非凝血因子路徑異常，FVIII 補充無直接治療機轉"* (a platelet granule-release defect, not a coagulation-factor pathway abnormality; FVIII supplementation has no direct therapeutic mechanism).

This is an important caveat: despite a very high TxGNN similarity score (99.99%), the mechanistic annotation for this specific prediction argues **against** biological plausibility rather than for it. This pattern repeats across most of the top 10 predictions for this drug (see below) — several are platelet-function or platelet-count disorders unrelated to the FVIII pathway, and one (thrombotic thrombocytopenic purpura) is flagged as a potential **safety concern in the opposite direction** (FVIII/vWF pathway is pathologically elevated in TTP; further FVIII supplementation could theoretically worsen thrombotic risk). Only rank 5 (acquired coagulation factor deficiency) shows a plausible mechanistic overlap, and even that is qualified as weak due to the typical presence of FVIII inhibitors in that population, where bypassing agents rather than FVIII replacement are standard care.

---

## Clinical Trial Evidence

Currently no related clinical trials registered

---

## Literature Evidence

Currently no related literature available

---

## Norway Market Information

This drug is not currently marketed in Norway (未上市); no authorization records are available in the evidence pack.

---

## Other Predicted Indications (Not Prioritized)

For transparency, the remaining top-10 TxGNN predictions and their mechanistic rationale are summarized below. All carry evidence level L5 (model prediction only) with no supporting trials or literature, and all are scored "Hold."

| Rank | Predicted Indication | Score | Mechanistic Assessment (per evidence pack) |
|------|----------------------|-------|---------------------------------------------|
| 2 | Pseudo-von Willebrand disease | 99.99% | Platelet GPIbα gain-of-function defect, not FVIII/vWF deficiency — weak link |
| 3 | Glanzmann thrombasthenia | 99.99% | Platelet GPIIb/IIIa receptor defect, not coagulation-factor deficiency — unrelated |
| 4 | Scott syndrome | 99.95% | Platelet membrane scramblase defect, not FVIII deficiency — unrelated |
| 5 | Acquired coagulation factor deficiency | 99.95% | Plausible overlap with acquired hemophilia A, but inhibitors typically require bypassing agents rather than FVIII alone — moderate but unconfirmed |
| 6 | Bleeding diathesis due to collagen receptor defect | 99.91% | Platelet GPVI (primary hemostasis) defect, distinct from FVIII's secondary hemostasis role — unrelated |
| 7 | Hemorrhagic disorder due to constitutional thrombocytopenia | 99.91% | Platelet count/production defect; FVIII does not affect platelet generation — unrelated |
| 8 | "Flood factor deficiency" | 99.61% | Disease label unclear/possible database naming artifact; no basis for mechanistic assessment |
| 9 | Thrombotic thrombocytopenic purpura | 99.54% | FVIII/vWF axis already pathologically elevated in TTP; additional FVIII could theoretically worsen thrombotic risk — potential safety concern |
| 10 | Hereditary thrombocytosis with transverse limb defect | 99.52% | Rare congenital syndrome linked to hematopoietic/skeletal genes, not FVIII pathway — unrelated |

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
All 10 top-ranked predictions are evidence level L5 (model prediction only), with zero supporting clinical trials or literature. More importantly, the evidence pack's own mechanistic rationale argues against biological plausibility for 8 of the 10 candidates (platelet-function/count disorders unrelated to the FVIII coagulation pathway), and flags one candidate (TTP) as a potential safety risk in the opposite therapeutic direction.

**To proceed, the following is needed:**
- TFDA/regulatory label data (warnings, contraindications) — currently a Blocking data gap (DG001)
- Confirmed original indication and MOA for turoctocog alfa (DG002)
- If pursuing rank 5 (acquired coagulation factor deficiency) as the most mechanistically plausible candidate, dedicated literature/trial search specific to acquired hemophilia A and inhibitor status
- Independent pharmacological review before any further evaluation stage, given the self-contradictory nature of the current prediction set
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

