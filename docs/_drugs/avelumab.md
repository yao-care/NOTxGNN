---
layout: default
title: Avelumab
parent: 僅模型預測 (L5)
nav_order: 41
evidence_level: L5
indication_count: 10
---

# Avelumab
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

# Avelumab: From Merkel Cell Carcinoma to Human Herpesvirus 8-Related Tumor

## One-Sentence Summary

Avelumab is an anti-PD-L1 monoclonal antibody internationally approved for Merkel cell carcinoma and urothelial carcinoma (no Norway license data is available in this evidence pack).
The TxGNN model's top-ranked prediction is **Human Herpesvirus 8-Related Tumor** (e.g. HHV-8-associated Kaposi sarcoma / primary effusion lymphoma),
but this prediction is currently supported by **0 clinical trials** and **0 publications** — it is a pure model output with no corroborating evidence.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not licensed in Norway (0 authorizations); internationally approved for Merkel cell carcinoma and urothelial carcinoma |
| Predicted New Indication | Human Herpesvirus 8-Related Tumor |
| TxGNN Prediction Score | 99.97% |
| Evidence Level | L5 |
| Norway Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available (flagged as a blocking data gap, DG002). Based on the information embedded in this evidence pack, avelumab is an anti-PD-L1 monoclonal antibody, and its efficacy has been established for Merkel cell carcinoma and urothelial carcinoma — both settings where PD-L1-mediated immune evasion drives tumor progression.

The mechanistic rationale for HHV-8-related tumors is that virus-associated malignancies (e.g. Kaposi sarcoma, primary effusion lymphoma) also frequently exploit checkpoint-mediated immune evasion, and blocking PD-L1 could theoretically restore T-cell recognition of viral tumor antigens. However, this population commonly presents with concurrent HIV infection or other immunosuppression, which substantially complicates the risk-benefit profile of checkpoint blockade and is not addressed anywhere in this dataset.

This remains a mechanism-only extrapolation: there is no PD-L1 expression data, no preclinical model, and no clinical or literature evidence specific to HHV-8-related tumors to support the prediction.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Cytotoxicity

Avelumab is an antineoplastic agent (immune checkpoint inhibitor class), so this section is included.

| Item | Content |
|------|------|
| Cytotoxicity Classification | Immunotherapy (anti-PD-L1 monoclonal antibody; not conventional cytotoxic chemotherapy) |
| Myelosuppression Risk | Low — checkpoint inhibitors are not typically myelosuppressive; toxicity is primarily immune-related (irAEs) rather than hematologic |
| Emetogenicity Classification | Low |
| Monitoring Items | Thyroid, liver and renal function; infusion-related reaction monitoring; surveillance for immune-related adverse events (colitis, pneumonitis, endocrinopathies) |
| Handling Protection | No special cytotoxic-drug handling protocol required; standard biologic infusion precautions apply |

Note: No drug-specific toxicity dataset was available (DrugBank toxicity fields empty); the above reflects general class characteristics of PD-L1 inhibitors and should be confirmed against the official package insert once available.

---

## Safety Considerations

Please refer to the package insert for safety information. (Key warnings, contraindications, and DDI data are all flagged as data gaps or "not found" in this evidence pack — DG001 is a blocking gap.)

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked prediction (Human Herpesvirus 8-Related Tumor) has an L5 evidence level — no clinical trials, no literature, and a plausible but unverified mechanistic rationale complicated by the frequent HIV/immunosuppression comorbidity in this population. This does not meet the threshold to advance to safety screening (S1).

**To proceed, the following is needed:**
- Official label data (warnings/contraindications) from TFDA or equivalent regulatory source — currently blocking (DG001)
- Formal MOA documentation from DrugBank or product label (DG002)
- Preclinical or biomarker evidence of PD-L1 expression in HHV-8-associated tumors
- Safety assessment specific to concurrent HIV/immunosuppressed populations before any clinical exploration

**Note:** Among the 10 candidates in this pack, ranks 9–10 (prostatic urethra urothelial carcinoma; kidney pelvis sarcomatoid transitional cell carcinoma) show comparatively stronger mechanistic grounding — both are histological/anatomical extensions of avelumab's already-approved urothelial carcinoma indication, and rank 10 has one completed real-world observational trial (NCT05431777, L3). These may warrant prioritization over the top-ranked HHV-8 prediction for further evaluation.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

