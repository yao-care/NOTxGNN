---
layout: default
title: Tenecteplase
parent: 僅模型預測 (L5)
nav_order: 347
evidence_level: L5
indication_count: 10
---

# Tenecteplase
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

# Tenecteplase: From [Data Gap] to Posteroinferior Myocardial Infarction

## One-Sentence Summary

> Tenecteplase is a genetically engineered tissue plasminogen activator (tPA); this evidence pack does not confirm its original approved indication (flagged as a data gap), though it is clinically well known as a fibrinolytic agent for acute myocardial infarction.
> The TxGNN model predicts it may be relevant for **Posteroinferior Myocardial Infarction**, an anatomical STEMI subtype,
> but currently **no clinical trials** and **no literature** specifically support this subtype — the evidence is mechanistic inference only.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available in this evidence pack (MOA/indication data flagged as gap — see DG002) |
| Predicted New Indication | Posteroinferior Myocardial Infarction |
| TxGNN Prediction Score | 99.87% |
| Evidence Level | L4 |
| Taiwan Market Status | 未上市 (Not marketed) |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available (flagged as Data Gap DG002, High severity). Based on known clinical information, tenecteplase is a fibrin-specific, genetically engineered variant of tissue plasminogen activator (tPA), which activates plasminogen to plasmin to degrade fibrin within thrombi. Its established role in fibrinolytic therapy for ST-elevation myocardial infarction (STEMI) is well documented in general terms.

Posteroinferior myocardial infarction is not a distinct disease entity but rather an anatomical/ECG-lead-based subtype of STEMI, defined by the location of the culprit coronary lesion. Mechanistically, the same fibrinolytic action that benefits STEMI overall should, in principle, extend to this subtype. However, this evidence pack contains **zero subtype-specific clinical trials or literature**, so the prediction represents TxGNN essentially re-identifying a known drug-class relationship at finer anatomical granularity, rather than surfacing genuinely new therapeutic evidence.

It is worth noting that elsewhere in this prediction set, a mechanistically related and better-evidenced signal exists: **coronary stenosis** (rank 5) is supported by a completed Phase 2 RCT (NCT00604695 / ICE-T-TIMI-49) evaluating low-dose intracoronary tenecteplase during primary PCI. This reinforces the general biological plausibility of tenecteplase's fibrinolytic mechanism in adjacent coronary applications, even though it does not directly validate the posteroinferior MI subtype specifically.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Taiwan Market Information

Tenecteplase currently holds **0 authorizations** in Taiwan and is **not marketed** (未上市). No license records are available in this evidence pack.

---

## Safety Considerations

Detailed safety data (key warnings, contraindications, drug-drug interactions) could not be retrieved for this evaluation. This is flagged in the evidence pack as **Data Gap DG001** (Blocking severity): TFDA label warnings/contraindications are unavailable, and their absence directly prevents completion of the S1 safety pre-screening stage.

> Please refer to the package insert for safety information once TFDA label data is obtained.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- The top-ranked prediction (posteroinferior MI) has no subtype-specific clinical trial or literature support — only a general mechanistic argument extrapolated from tenecteplase's known role in STEMI. Combined with a Blocking-severity safety data gap (TFDA label unavailable), this candidate cannot yet advance past S1.
- Note: within this same prediction set, **coronary stenosis** (adjunctive low-dose intracoronary tenecteplase during PCI) shows meaningfully stronger evidence (completed Phase 2 RCT, L2, S2) and may independently warrant a "Proceed with Guardrails" evaluation as a separate candidate.
- Several lower-ranked predictions (e.g., chromosomal deletion syndromes, thalassemia, red cell enzymopathies) show no plausible mechanistic link and no supporting evidence — these are assessed as likely TxGNN embedding-space false positives and should not be pursued.

**To proceed, the following is needed:**
- TFDA-approved package insert (warnings, contraindications, DDI) to unblock S1 safety screening (DG001)
- Confirmed drug mechanism of action and original approved indication(s) from DrugBank or equivalent source (DG002)
- Subtype-specific clinical evidence (trials or case series) for posteroinferior MI, or a decision to reclassify this prediction as a known-class extension rather than a novel repurposing candidate
- If pursuing the adjacent coronary stenosis signal, a dedicated evaluation package built around NCT00604695/ICE-T-TIMI-49 data
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

