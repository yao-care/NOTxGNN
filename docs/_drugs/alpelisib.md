---
layout: default
title: Alpelisib
parent: 僅模型預測 (L5)
nav_order: 25
evidence_level: L5
indication_count: 1
---

# Alpelisib
{: .fs-9 }

證據等級: **L5** | 預測適應症: **1** 個
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

# Alpelisib: From Breast Cancer to Pulmonary Hypertension

## One-Sentence Summary

> Alpelisib is a PI3Kα inhibitor whose real-world use context in the evidence pack points to HR+/HER2-negative advanced or metastatic breast cancer (formal original-indication and MOA fields are not populated in this dataset).
> The TxGNN model predicts it may be effective for **Pulmonary Hypertension**, with a prediction score of **99.03%**, but currently **0 directly relevant clinical trials** and **2 publications** support this direction — and both publications describe drug-induced pulmonary/cardiac toxicity rather than therapeutic benefit.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Breast cancer (HR+/HER2-negative, advanced/metastatic) — inferred from clinical trial context; not formally recorded in `taiwan_regulatory`/`original_indications` |
| Predicted New Indication | Pulmonary Hypertension |
| TxGNN Prediction Score | 99.03% |
| Evidence Level | L5 |
| Taiwan Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available for alpelisib in this evidence pack (`original_moa: [Data Gap]`). Based on the retrieved literature context, alpelisib is a PI3Kα (phosphoinositide 3-kinase alpha) inhibitor used in oncology, and its efficacy in HR+/HER2-negative breast cancer is well established in the clinical trial ecosystem referenced here (e.g., the REASSURE real-world study).

The biological rationale behind the TxGNN model's high score (0.99) appears to rest on the PI3Kα/AKT/mTOR signaling pathway, which has been implicated in preclinical literature as a contributor to pulmonary vascular remodeling — a core pathological mechanism in pulmonary arterial hypertension (PAH). This shared pathway is a plausible reason the model links a breast cancer drug to a pulmonary vascular disease.

However, the actual evidence retrieved for this candidate does **not** support a therapeutic benefit — it points in the opposite direction. The single clinical trial identified evaluates a different drug (ribociclib) in breast cancer and has no bearing on alpelisib or pulmonary hypertension. The two literature sources describe alpelisib-induced **interstitial lung disease** and **PI3Kα-pathway-inhibition-associated biventricular cardiac atrophy/dysfunction** — both of which suggest alpelisib may pose cardiopulmonary risk in a population that already has compromised cardiopulmonary reserve (PH patients), rather than offering benefit. This is a case of a "prediction-driven, mechanism-only" signal with no clinical support and a countervailing safety signal.

---

## Clinical Trial Evidence

Currently no clinical trials directly supporting alpelisib for pulmonary hypertension are registered.

*(One trial, [NCT06705504](https://clinicaltrials.gov/study/NCT06705504), was retrieved by the search but excluded — it is a retrospective real-world study of ribociclib and alpelisib in HR+/HER2-negative breast cancer patients, unrelated to alpelisib or pulmonary hypertension; graded "C — not relevant" in the evidence review.)*

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [35730191](https://pubmed.ncbi.nlm.nih.gov/35730191/) | 2023 | Case Report | Journal of Oncology Pharmacy Practice | Reports a case of alpelisib-induced interstitial lung disease (progressive pulmonary fibrosis) in a patient being treated for advanced breast cancer — a safety signal, not efficacy evidence, for pulmonary indications |
| [31039672](https://pubmed.ncbi.nlm.nih.gov/31039672/) | 2019 | Preclinical/Translational | Journal of the American Heart Association | Preclinical study showing PI3Kα pathway inhibition (the mechanistic class alpelisib belongs to) causes distinct biventricular cardiac atrophy, remodeling, and right ventricular dysfunction — right ventricular dysfunction is a key concern in pulmonary hypertension management |

---

## Taiwan Market Information

Alpelisib is currently **not marketed** in Taiwan — `taiwan_regulatory.total_licenses = 0`, and no authorization records are available in the evidence pack.

---

## Cytotoxicity

*(Included because alpelisib is an oncology agent per its known clinical use context in the retrieved trial evidence.)*

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (PI3Kα inhibitor) — not a conventional cytotoxic chemotherapy agent, based on available context |
| Myelosuppression Risk | No myelosuppression data available in this evidence pack — please refer to the package insert |
| Emetogenicity Classification | No data available in this evidence pack — please refer to the package insert |
| Monitoring Items | Beyond routine CBC/liver/renal monitoring, the retrieved literature signals suggest pulmonary function/imaging surveillance (risk of interstitial lung disease) and cardiac function monitoring (risk of biventricular atrophy/right ventricular dysfunction) warrant attention |
| Handling Protection | Oral small-molecule targeted therapy; no cytotoxic-drug handling requirement is established in this evidence pack — refer to institutional oncology drug handling policy |

---

## Safety Considerations

Please refer to the package insert for safety information.

*(Note: TFDA package insert warnings and contraindications are flagged as a **Blocking** data gap (DG001) in this evidence pack — safety review for this candidate cannot proceed to Stage 1 until this is resolved. DDI query also returned no data.)*

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
This candidate rests entirely on a model prediction (Evidence Level L5) with no supporting clinical trials and no efficacy literature; the only clinical trial retrieved is unrelated, and the two available publications instead describe alpelisib-induced pulmonary and cardiac toxicity — a safety signal that runs counter to use in pulmonary hypertension. Combined with a blocking gap in TFDA safety data, this candidate does not currently meet the bar to advance past initial safety screening (S0).

**To proceed, the following is needed:**
- TFDA package insert / safety warnings and contraindications (resolves blocking gap DG001)
- Confirmed mechanism of action (MOA) documentation from DrugBank (DG002)
- Dedicated preclinical or clinical studies evaluating alpelisib specifically in pulmonary hypertension models or patients
- A cardiopulmonary safety monitoring plan addressing the interstitial lung disease and right ventricular dysfunction signals identified in existing literature
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

