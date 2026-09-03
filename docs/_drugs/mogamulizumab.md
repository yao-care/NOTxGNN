---
layout: default
title: Mogamulizumab
parent: 僅模型預測 (L5)
nav_order: 233
evidence_level: L5
indication_count: 7
---

# Mogamulizumab
{: .fs-9 }

證據等級: **L5** | 預測適應症: **7** 個
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

# Mogamulizumab: From Cutaneous T-Cell Lymphoma to Prostatic Urethra Urothelial Carcinoma

## One-Sentence Summary

> Mogamulizumab is a humanized anti-CCR4 monoclonal antibody historically associated with cutaneous T-cell lymphoma (CTCL)/Sézary syndrome (per the evidence pack's mechanistic notes; not present in the structured indication record).
> The TxGNN model predicts it may be effective for **prostatic urethra urothelial carcinoma**,
> but **0 clinical trials** and **0 publications** currently support this direction — this is a pure computational prediction.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Cutaneous T-cell lymphoma (CTCL) / Sézary syndrome — referenced only in the evidence-pack rationale text; not captured in the structured `original_indications` field |
| Predicted New Indication | Prostatic urethra urothelial carcinoma |
| TxGNN Prediction Score | 99.44% (rank 5955) |
| Evidence Level | L5 |
| Norway Market Status | Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Structured mechanism-of-action data is not available for this drug (`original_moa: [Data Gap]`). However, the repurposing rationale attached to each candidate consistently describes mogamulizumab as a humanized anti-CCR4 monoclonal antibody that depletes CCR4-positive tumor-infiltrating regulatory T cells (Tregs) via antibody-dependent cellular cytotoxicity (ADCC), thereby relieving tumor-mediated immune suppression.

The predicted new indications — urothelial carcinomas of the prostatic urethra, renal pelvis, and bladder, plus several rare tumors (HHV8-related tumors, ectomesenchymoma, malignant granular cell skin tumor) — are linked to the original mechanism only through a general biological hypothesis: many solid tumors show CCR4+ Treg infiltration, and depleting these cells could theoretically restore anti-tumor immunity. None of the seven candidates have specific biomarker data, preclinical models, or clinical experience cited in this evidence pack to confirm CCR4/Treg involvement in these specific tumor types.

In short, this is a mechanistically plausible but entirely unvalidated extrapolation. The TxGNN score reflects network-based similarity in the knowledge graph, not experimental or clinical evidence.

## Clinical Trial Evidence

Currently no related clinical trials registered

## Literature Evidence

Currently no related literature available

## Norway Market Information

Mogamulizumab currently holds **no market authorizations in Norway** (`total_licenses: 0`, `market_status: 未上市`). No product listings, dosage forms, or approved indication text are available in the evidence pack.

## Cytotoxicity

Mogamulizumab is an antineoplastic biologic (anti-CCR4 monoclonal antibody, immunotherapy class); the section below is included accordingly.

| Item | Content |
|------|------|
| Cytotoxicity Classification | Immunotherapy (anti-CCR4 monoclonal antibody; Treg-depleting mechanism, not a conventional cytotoxic agent) |
| Myelosuppression Risk | Not characterized in this evidence pack. Please refer to the package insert warnings and precautions |
| Emetogenicity Classification | Low (typical for antibody-based immunotherapies, which generally carry minimal direct emetogenic potential) |
| Monitoring Items | CBC, skin/mucocutaneous examination, infusion-reaction monitoring, and surveillance for immune-related adverse events (liver function, thyroid function, GI symptoms) — consistent with monoclonal antibody immunotherapy class |
| Handling Protection | No cytotoxic hazardous-drug data provided; confirm handling requirements against institutional biologics/monoclonal antibody infusion protocols |

## Safety Considerations

Please refer to the package insert for safety information.

> Note: This is a **Blocking** data gap (DG001 — TFDA/label warnings and contraindications unavailable), which by itself is sufficient to prevent progression past initial safety screening (S1).

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
All seven predicted indications sit at evidence level L5 (model prediction only, no trials or literature), the drug is not marketed in Norway, and a Blocking safety data gap (TFDA/label warnings and contraindications) prevents any safety pre-screening. There is currently no basis to advance beyond the hypothesis stage.

**To proceed, the following is needed:**
- Resolve DG001: obtain TFDA/regulatory label data (warnings, contraindications, DDI)
- Resolve DG002: confirm mechanism of action via DrugBank API (beyond the rationale-text description)
- Confirm the drug's actual original approved indication(s) in structured form
- Targeted literature/trial search for CCR4 expression or Treg infiltration in urothelial carcinoma and the other candidate tumor types
- If any signal emerges, prioritize preclinical/biomarker studies before considering clinical evaluation
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

