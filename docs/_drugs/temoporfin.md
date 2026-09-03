---
layout: default
title: Temoporfin
parent: 僅模型預測 (L5)
nav_order: 344
evidence_level: L5
indication_count: 10
---

# Temoporfin
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

# Temoporfin: From Head and Neck Squamous Cell Carcinoma (PDT) to Nasopharyngeal Teratoma

## One-Sentence Summary

Temoporfin (mTHPC/Foscan) is a photosensitizer originally used for photodynamic therapy (PDT) of head and neck squamous cell carcinoma. The TxGNN model predicts potential efficacy for **Nasopharyngeal Teratoma**, but currently **no clinical trials** and **no literature** support this specific prediction.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Head and neck squamous cell carcinoma (photodynamic therapy) — inferred from evidence-pack rationale; no Norway license record on file |
| Predicted New Indication | Nasopharyngeal Teratoma |
| TxGNN Prediction Score | 99.78% |
| Evidence Level | L5 |
| Norway Market Status | ✗ Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed DrugBank mechanism-of-action data is currently unavailable (data gap). Based on information embedded in the evidence pack, temoporfin is a photosensitizer that, upon light activation at a specific wavelength, generates singlet oxygen causing tumor cell necrosis/apoptosis — the established mechanism behind its approved use in photodynamic therapy for head and neck squamous cell carcinoma.

Nasopharyngeal teratoma, however, is predominantly a germ-cell-derived tumor rather than a superficial mucosal squamous lesion. The evidence pack's own mechanistic assessment for this candidate is weak: teratomas are not a typical PDT target, and light delivery to this tumor type is not well established.

This is reflected in the pack's mechanistic-link note: *"畸胎瘤非典型光動力治療標的（多為生殖細胞來源腫瘤，非黏膜表淺鱗狀上皮病灶），機轉關聯薄弱，無實證支持。"* No clinical trials or publications currently support extending temoporfin PDT to this indication.

## Clinical Trial Evidence

Currently no related clinical trials registered

## Literature Evidence

Currently no related literature available

## Norway Market Information

Temoporfin currently holds **no marketing authorization** in Norway (market status: not marketed; 0 authorizations on file). No product/dosage-form data is available for this market.

## Cytotoxicity

Temoporfin is used as a photosensitizing agent for cancer photodynamic therapy, so cytotoxicity considerations are noted, though its mechanism (light-activated singlet-oxygen generation) differs from conventional systemic cytotoxic chemotherapy.

| Item | Content |
|------|------|
| Cytotoxicity Classification | Photodynamic therapy agent (photosensitizer) — does not map cleanly to conventional cytotoxic/targeted/immunotherapy categories; localized, light-dependent cytotoxicity |
| Myelosuppression Risk | Not expected to be significant — mechanism is local phototoxicity rather than systemic bone-marrow-active cytotoxicity; formal toxicity data not available (data gap), please confirm against package insert |
| Emetogenicity Classification | Low (localized phototoxic mechanism; not typical of emetogenic systemic chemotherapy) |
| Monitoring Items | Skin/eye photosensitivity precautions (light avoidance post-injection), airway patency monitoring for head/neck PDT (post-treatment swelling risk noted in related literature), liver function |
| Handling Protection | Patient-level light-protection protocol required post-administration; standard cytotoxic-drug handling classification not confirmed (data gap) — please refer to the package insert |

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked prediction (Nasopharyngeal Teratoma) has no supporting clinical trials or literature, and the mechanistic rationale itself is assessed as weak (non-mucosal, non-squamous tumor type mismatched with PDT's superficial-illumination mechanism).

**To proceed, the following is needed:**
- Formal DrugBank/TFDA-equivalent MOA, warnings, and contraindication data (currently blocking safety pre-assessment per DG001/DG002)
- Any preclinical or case-level evidence specifically addressing light delivery feasibility to nasopharyngeal/germ-cell tumors
- Consider redirecting research priority toward the pipeline's higher-evidence candidates (e.g., benign neoplasm of tongue, benign neoplasm of floor of mouth, cystic neoplasm — all L3, S2, with cohort/case-series PDT literature), which are mechanistically consistent with temoporfin's established head-and-neck mucosal PDT use
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

