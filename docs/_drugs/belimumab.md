---
layout: default
title: Belimumab
parent: 僅模型預測 (L5)
nav_order: 47
evidence_level: L5
indication_count: 6
---

# Belimumab
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

# Belimumab: From Systemic Lupus Erythematosus to Primary Release Disorder of Platelets

## One-Sentence Summary

> Belimumab is a monoclonal antibody targeting BAFF/BLyS, known to be approved for systemic lupus erythematosus (SLE), though detailed regulatory and mechanism-of-action data for this evidence pack are currently unavailable.
> The TxGNN model predicts it may be effective for **Primary Release Disorder of Platelets**,
> but this direction is currently supported by **0 relevant clinical trials** and **0 publications** — the one linked trial concerns an unrelated disease entity.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Systemic Lupus Erythematosus (SLE) — based on known clinical use; not confirmed by regulatory data in this pack |
| Predicted New Indication | Primary Release Disorder of Platelets |
| TxGNN Prediction Score | 99.96% |
| Evidence Level | L5 (model prediction only; no supportive clinical or literature evidence) |
| Norway Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available for belimumab in this evidence pack (marked as a High-severity data gap). Based on known information, belimumab is a monoclonal antibody that inhibits BAFF/BLyS, thereby suppressing B-cell survival and reducing autoantibody production — a mechanism consistent with its established use in autoimmune conditions such as SLE.

Primary release disorder of platelets, however, is an intrinsic platelet granule secretion defect and is not a B-cell– or autoantibody-mediated disease. There is no established biological pathway connecting BAFF inhibition to correction of platelet granule release function. The single clinical trial linked to this prediction (NCT01610492) actually studied idiopathic membranous glomerulonephropathy — a completely different disease entity — and was flagged as a disease-entity mismatch, not genuine supporting evidence.

Given the absence of a plausible mechanistic link and the lack of any on-target clinical or literature evidence, this top-ranked TxGNN prediction should be treated as a low-confidence, algorithm-only signal at this stage.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT01610492](https://clinicaltrials.gov/study/NCT01610492) | Phase 2 | Completed | 14 | Mechanistic study of belimumab in idiopathic membranous glomerulonephropathy — **disease entity mismatch**, not related to platelet release disorder; does not constitute supporting evidence |

No clinical trials directly targeting primary release disorder of platelets were identified.

---

## Literature Evidence

Currently no related literature available.

---

## Norway Market Information

Belimumab currently holds no marketing authorizations in Norway (market status: Not marketed; total authorizations: 0).

---

## Safety Considerations

Please refer to the package insert for safety information.

*(Note: TFDA/Norway label warnings and contraindications are marked as a Blocking data gap in this evidence pack and could not be retrieved for this evaluation.)*

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked predicted indication (primary release disorder of platelets) lacks a plausible mechanistic connection to belimumab's known BAFF-inhibition pathway, and has no supporting clinical trial or literature evidence — the only linked trial addresses an unrelated disease. Combined with a Blocking data gap on regulatory safety information (DG001), this candidate cannot proceed past S0.

**To proceed, the following is needed:**
- TFDA/Norway package insert data (warnings, contraindications) — required before any S1 safety screening (DG001, Blocking)
- Confirmed mechanism of action and approved indication data from DrugBank (DG002, High)
- Disease-entity-matched clinical trials or literature specifically studying belimumab in platelet release/granule disorders
- If pursuing alternative candidates, rank 4 (fetal and neonatal alloimmune thrombocytopenia) shows relatively stronger mechanistic plausibility (B-cell/alloantibody-mediated pathology) and may warrant reprioritization, though it also currently lacks any clinical or literature evidence
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

