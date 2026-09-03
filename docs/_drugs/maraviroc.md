---
layout: default
title: Maraviroc
parent: 僅模型預測 (L5)
nav_order: 222
evidence_level: L5
indication_count: 10
---

# Maraviroc
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

# Maraviroc: From HIV-1 Infection (Known Indication, Not in Evidence Pack) to Multiple Endocrine Neoplasia

## One-Sentence Summary

> Maraviroc is a CCR5 antagonist used in antiretroviral therapy for HIV-1 infection; however, the original indication and mechanism of action are not documented in this evidence pack (data gap).
> The TxGNN model predicts it may be effective for **Multiple Endocrine Neoplasia**,
> but this prediction is currently supported by **0 clinical trials** and **0 publications**, and the model's own rationale explicitly states there is no known biological link between the CCR5–CCL5 axis and MEN pathology.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in evidence pack (`original_indications` empty) — publicly known as HIV-1 infection, unverified within this dataset |
| Predicted New Indication | Multiple Endocrine Neoplasia |
| TxGNN Prediction Score | 99.82% |
| Evidence Level | L5 (model prediction only, no supporting trials or literature) |
| Norway Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available (Data Gap DG002). Based on general knowledge of the drug class, maraviroc is a CCR5 (C-C chemokine receptor type 5) antagonist that blocks viral entry in antiretroviral therapy. Its established clinical use is not recorded in this evidence pack, so this context should be treated as background only, not as verified data supporting this repurposing candidate.

The relationship between the drug's known mechanism and the predicted indication is weak. Multiple endocrine neoplasia (MEN) is a hereditary endocrine tumour syndrome driven by *RET* or *MEN1* gene mutations, and — per the model's own repurposing rationale — has **no known biological relationship** to the CCR5–CCL5 signalling axis. The rationale text explicitly states this is a TxGNN score-only prediction, with no mechanistic support or literature corroboration.

Given this, the top-ranked prediction should be interpreted as a candidate flagged purely by the model's learned embedding similarity, not by any pharmacological or clinical rationale. This does not necessarily invalidate the model output, but it means the prediction currently sits at the lowest confidence tier (L5) and requires substantial independent validation before any further action.

---

## Clinical Trial Evidence

Currently no related clinical trials registered

---

## Literature Evidence

Currently no related literature available

---

## Norway Market Information

Maraviroc currently holds **no marketing authorization in Norway** (`market_status`: 未上市 / Not Marketed; `total_licenses`: 0). No license records are available to summarize.

---

## Safety Considerations

Please refer to the package insert for safety information.

(Note: Key warnings, contraindications, and drug interaction data are all flagged as Data Gaps (DG001, Blocking severity) in this evidence pack — this is a prerequisite gap that must be resolved before any safety evaluation, per the pack's own S1-stage gating logic.)

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked predicted indication (Multiple Endocrine Neoplasia) has no supporting clinical trials, no supporting literature, and the model's own mechanistic rationale explicitly states there is no known biological link between CCR5 signalling and MEN pathology. Combined with the blocking data gap on safety labeling (DG001) and the missing MOA data (DG002), there is currently no basis to advance this candidate beyond model output.

**To proceed, the following is needed:**
- Resolve DG001 (TFDA/regulatory label warnings and contraindications) — currently blocking any safety evaluation
- Resolve DG002 (verified mechanism of action from DrugBank or primary literature)
- Independent in vitro or bioinformatic validation of a CCR5–MEN pathway link before further evidence collection is prioritized
- Consider redirecting evidence-gathering effort toward the pack's higher-evidence candidates instead of the top TxGNN-score item: **HER2-positive breast carcinoma** (rank 10, L4, decision stage S1 "Research Question" — supported by a concrete preclinical mechanism paper on CCL5–CCR5-mediated trastuzumab resistance) and **cytomegalovirus infection** (rank 9, L4, S1 — supported by two immunology cohort/review papers), both of which currently have stronger mechanistic and evidentiary grounding than the top-ranked MEN prediction
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

