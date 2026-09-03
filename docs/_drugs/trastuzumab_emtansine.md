---
layout: default
title: Trastuzumab Emtansine
parent: 僅模型預測 (L5)
nav_order: 370
evidence_level: L5
indication_count: 4
---

# Trastuzumab Emtansine
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

# Trastuzumab Emtansine: From HER2-Positive Breast Cancer to Normal Breast-Like Subtype of Breast Carcinoma

## One-Sentence Summary

> Trastuzumab emtansine (T-DM1) is an antibody-drug conjugate (ADC) that links trastuzumab to the cytotoxic maytansinoid DM1, and per trial-reported context in this evidence pack it is already used as a standard treatment for HER2-positive breast cancer.
> The TxGNN model's top-ranked prediction for this drug is **Normal Breast-Like Subtype of Breast Carcinoma**,
> but currently only **1 indirectly relevant clinical trial** and **no dedicated publications** support this specific direction.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | HER2-positive breast cancer (per trial-reported context, e.g. NCT03203616; not a formally licensed indication in Norway) |
| Predicted New Indication | Normal Breast-Like Subtype of Breast Carcinoma |
| TxGNN Prediction Score | 99.82% |
| Evidence Level | L3 |
| Norway Market Status | Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the regulatory record (`original_moa` is flagged as a data gap). However, the evidence pack's own repurposing rationale describes T-DM1 as an anti-HER2 antibody-drug conjugate: trastuzumab targets HER2-overexpressing tumour cells and delivers the cytotoxic payload DM1 (a maytansinoid) directly into them, combining targeted delivery with cytotoxic cell killing.

"Normal breast-like" is one of the intrinsic molecular subtypes of breast carcinoma, and its HER2 expression status is heterogeneous — some tumours in this subtype may express HER2, others may not. The evidence pack itself notes that there is currently no direct evidence that this specific subtype responds preferentially to T-DM1; the mechanistic link rests on a single variable (HER2 expression) rather than subtype-specific data, which is why the supporting evidence is graded L3 (Research Question stage) rather than stronger.

For context, this same evidence pack also surfaced three closely related TxGNN predictions for T-DM1: **progesterone-receptor (PR) positive breast cancer** and **PR-negative breast cancer** (both L2, "Proceed with Guardrails," backed by multiple Phase 1–3 trials directly testing T-DM1 in HER2-positive populations), and **luminal A/B breast tumour** (L4, "Hold," where the mechanistic link is weaker because luminal tumours are predominantly HER2-negative). Relative to these, the normal breast-like prediction sits at the lower end of directly testable evidence.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT06348134](https://clinicaltrials.gov/study/NCT06348134) | Phase 2 | Recruiting | 74 | Assessing optimal neoadjuvant-to-adjuvant anti-HER2-based therapy in Nigerian women with HER2+ breast cancer; not specific to normal breast-like subtype and does not test T-DM1 as monotherapy — graded as indirectly relevant (Grade B). |

---

## Literature Evidence

Currently no related literature available.

---

## Norway Market Information

Trastuzumab emtansine is currently **not marketed** in Norway, and no marketing authorization records are available in this evidence pack (0 licenses).

---

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy — Antibody-Drug Conjugate (ADC): anti-HER2 trastuzumab linked to the cytotoxic maytansinoid payload DM1 |
| Myelosuppression Risk | Please refer to the package insert warnings and precautions (no drug-specific toxicity data available in this evidence pack) |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | Please refer to the package insert warnings and precautions |
| Handling Protection | Contains a cytotoxic (maytansinoid) payload; standard cytotoxic/hazardous drug handling precautions are expected to apply pending confirmation from the official label |

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The mechanistic link for the "normal breast-like subtype" indication rests on a single shared variable (HER2 expression) rather than subtype-specific evidence, and it is supported by only one indirectly relevant, still-recruiting Phase 2 trial with no dedicated literature — insufficient to advance beyond the research-question stage.

**To proceed, the following is needed:**
- Regulatory label data (TFDA/official package insert warnings and contraindications — currently a Blocking data gap, DG001)
- Confirmed mechanism of action documentation (currently a High-severity data gap, DG002)
- Subtype-specific data on HER2 expression prevalence within the normal breast-like molecular subtype
- Dedicated trials or studies testing T-DM1 specifically in normal breast-like breast carcinoma
- Consider prioritizing the related PR-positive and PR-negative HER2+ breast cancer predictions from the same TxGNN run, which already have L2 evidence and a "Proceed with Guardrails" recommendation
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

