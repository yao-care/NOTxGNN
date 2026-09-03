---
layout: default
title: Lusutrombopag
parent: 僅模型預測 (L5)
nav_order: 220
evidence_level: L5
indication_count: 10
---

# Lusutrombopag
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

# Lusutrombopag: From Thrombocytopenia (TPO-RA Therapy) to Hereditary Thrombocytopenia with Normal Platelets

## One-Sentence Summary

> Lusutrombopag is a thrombopoietin receptor (TPO/MPL) agonist; its original approved indication is not documented in this evidence pack (no Norway license records exist).
> The TxGNN model predicts it may be effective for **Hereditary Thrombocytopenia with Normal Platelets**,
> but this prediction is currently supported by **0 clinical trials** and **0 publications** — it is a pure model-generated hypothesis.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available — no Norway license records exist for this product |
| Predicted New Indication | Hereditary Thrombocytopenia with Normal Platelets |
| TxGNN Prediction Score | 99.995% (overall rank 88) |
| Evidence Level | L5 |
| Norway Market Status | ✗ Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

The structured `original_moa` field for this drug is currently a data gap (DG002, High severity). However, the model's own rationale text identifies lusutrombopag as a **TPO receptor (MPL) agonist** — a drug class that stimulates megakaryocyte proliferation and differentiation to increase platelet counts.

Mechanistically, this places lusutrombopag on the same pharmacological axis as **platelet-production-deficiency disorders**. Hereditary thrombocytopenia with normal platelets (i.e., low platelet count without accompanying structural/functional platelet defects) is, in principle, a plausible extension of TPO-receptor agonism, since the underlying deficit is quantitative (insufficient production) rather than qualitative (defective platelet function).

That said, this is a genetic/hereditary condition, and no clinical trial or published evidence currently exists to confirm efficacy or safety of a TPO-RA in this specific population. The link should be treated as a mechanistically plausible research hypothesis only, not a validated therapeutic pathway.

---

## Clinical Trial Evidence

Currently no related clinical trials registered

---

## Literature Evidence

Currently no related literature available

---

## Norway Market Information

Lusutrombopag has **no marketing authorizations recorded in Norway** (`total_licenses: 0`, `market_status: 未上市`). No product/license table can be generated from the current evidence pack.

---

## Safety Considerations

Please refer to the package insert for safety information.

*(Note: TFDA/label warnings, contraindications, and DDI data are currently unavailable — flagged as DG001, Blocking severity, in the evidence pack. This gap must be closed before any Stage 1 safety assessment can proceed.)*

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction score is high, and the TPO-receptor-agonist mechanism offers a plausible biological rationale, but there is zero clinical trial or literature support, no confirmed mechanism-of-action record, no safety/label data, and the drug is not currently marketed in Norway. This falls squarely in Evidence Level L5 (model prediction only) and does not meet the bar to advance past Stage 0/1.

**To proceed, the following is needed:**
- Resolve DG001 (Blocking): obtain and parse the official label (warnings, contraindications) from the relevant regulatory authority
- Resolve DG002 (High): confirm mechanism of action via DrugBank API or primary literature
- Identify and document the drug's actual original approved indication(s)
- Search for any preclinical or case-level evidence specific to hereditary thrombocytopenia (normal-platelet subtype) before considering further investment
- Re-evaluate market/registration status if commercial availability becomes relevant to feasibility
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

