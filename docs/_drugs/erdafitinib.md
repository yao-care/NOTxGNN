---
layout: default
title: Erdafitinib
parent: 僅模型預測 (L5)
nav_order: 138
evidence_level: L5
indication_count: 6
---

# Erdafitinib
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

Using no additional skills — this is a direct report-generation task per the fixed template with the provided Evidence Pack.

---

# Erdafitinib: From FGFR-Altered Malignancy to Pulmonary Hypertension

## One-Sentence Summary

Erdafitinib is a pan-FGFR1-4 tyrosine kinase inhibitor used in oncology; the specific original indication text is not available in this evidence pack, and the drug is currently **not marketed in Norway**.
The TxGNN model predicts it may be effective for **Pulmonary Hypertension**, but this is currently supported by **0 clinical trials** and **0 publications** — the prediction is model-derived only, and even the mechanistic rationale flags that the direction of effect (protective vs. harmful) is unverified.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not documented in evidence pack (drug not marketed in Norway; no license records available) |
| Predicted New Indication | Pulmonary Hypertension |
| TxGNN Prediction Score | 99.38% (rank 6453) |
| Evidence Level | L5 (model prediction only, no clinical/literature support) |
| Norway Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available (flagged as a High-severity data gap, DG002). Based on the information present in this evidence pack, erdafitinib is described as a **pan-FGFR1-4 inhibitor**, and its rationale text notes that FGF/FGFR1 signalling is known to participate in pulmonary vascular remodelling and PAH pathogenesis — a role previously explored with other multi-kinase inhibitors such as imatinib in PAH research.

However, the directionality of this relationship is explicitly uncertain: FGFR signalling could either drive or protect against vascular remodelling depending on context, and the evidence pack itself states that erdafitinib's effect on this pathway "尚待驗證，亦可能有害" (direction unverified, potential for harm). This means the mechanistic link is theoretically plausible but not validated, and should be treated as a research hypothesis rather than an established pharmacological rationale.

No data connecting erdafitinib's (unknown, per this pack) original indication to pulmonary hypertension is available, so similarity-of-indication reasoning cannot be assessed at this time.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Norway Market Information

Erdafitinib currently holds **no marketing authorizations in Norway** (0 licenses, market status: Not Marketed). No product-level data (dosage form, approved indication text) is available.

---

## Cytotoxicity

Erdafitinib is an antineoplastic agent (pan-FGFR1-4 kinase inhibitor used in FGFR-altered malignancies), so this section applies.

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (FGFR1-4 tyrosine kinase inhibitor) |
| Myelosuppression Risk | Please refer to the package insert warnings and precautions |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | Please refer to the package insert warnings and precautions |
| Handling Protection | Please refer to the package insert warnings and precautions |

---

## Safety Considerations

Please refer to the package insert for safety information.

*(Note: TFDA/Norway label warnings and contraindications are flagged as a Blocking data gap (DG001) — this must be resolved before any Stage 1 safety review can proceed.)*

---

## Other Predicted Indications (Lower Confidence, Same Model Run)

For context, TxGNN also flagged five additional candidate indications for erdafitinib, all at evidence level L5 with no supporting clinical trials or literature (except one non-specific review for rheumatoid arthritis). None change the overall recommendation:

| Rank | Disease | Score | Recommendation | Mechanistic Note |
|------|---------|-------|-----------------|-------------------|
| 2 | Kyphoscoliotic heart disease | 99.27% | Hold | No direct mechanistic link; secondary cardiac condition, not FGFR-driven |
| 3 | Amenorrhea | 99.26% | Hold | No known mechanistic link |
| 4 | Rheumatoid arthritis | 99.25% | Hold | One non-specific 2020 kinase-inhibitor review only (PMID 31862477); no RA-specific data |
| 5 | Amyotrophic lateral sclerosis | 99.06% | Hold | Mechanism may run in the opposite direction (FGF/FGFR agonism, not inhibition, is neuroprotective) |
| 6 | Brachydactyly-syndactyly syndrome | 99.03% | Research Question | Strongest mechanistic plausibility (FGFR1-3 gain-of-function drives these skeletal syndromes), but zero clinical/preclinical data |

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The pulmonary hypertension prediction is supported only by a TxGNN score with zero clinical trials and zero literature, and the mechanistic rationale itself acknowledges the direction of effect is unverified and potentially harmful — this is a pure S0/L5 research hypothesis, not an actionable repurposing signal.

**To proceed, the following is needed:**
- Resolve DG001 (TFDA/Norway label warnings and contraindications) — currently Blocking
- Resolve DG002 (confirmed mechanism of action from DrugBank)
- Preclinical evidence establishing whether FGFR inhibition helps or worsens pulmonary vascular remodelling
- A dedicated literature/clinical trial search specific to "erdafitinib + pulmonary hypertension"
- Norway market authorization status confirmation (currently 0 licenses on file)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

