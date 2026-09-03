---
layout: default
title: Lorlatinib
parent: 僅模型預測 (L5)
nav_order: 216
evidence_level: L5
indication_count: 10
---

# Lorlatinib
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

# Lorlatinib: From ALK-Positive NSCLC to Gingival Fibromatosis

## One-Sentence Summary

> Lorlatinib is a third-generation ALK/ROS1 tyrosine kinase inhibitor established for the treatment of ALK-positive advanced non-small cell lung cancer (NSCLC), as evidenced by the Phase 3 CROWN trial data included in this evidence pack.
> The TxGNN model's top prediction is **Gingival Fibromatosis** (a benign fibrous gum overgrowth disorder), with a score of **99.81%**,
> but this prediction is currently supported by **zero clinical trials** and **zero publications** — it is a pure embedding-similarity signal with no known mechanistic or clinical basis.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not documented in Norway regulatory data (drug not marketed there). Based on attached literature (CROWN Phase 3 RCT, etc.), the established original indication is **ALK-positive advanced/metastatic NSCLC** |
| Predicted New Indication | Gingival Fibromatosis |
| TxGNN Prediction Score | 99.81% |
| Evidence Level | L5 (model prediction only, no supporting trials or literature) |
| Norway Market Status | Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data for lorlatinib was not available in the structured drug record (`original_moa: [Data Gap]`). However, based on the attached literature (CROWN trial and related publications), lorlatinib is a brain-penetrant, third-generation ALK/ROS1 tyrosine kinase inhibitor with proven efficacy in ALK-positive NSCLC, and broad activity against ALK resistance mutations.

Gingival fibromatosis is a benign, non-neoplastic fibrous overgrowth of gum tissue, most commonly caused by genetic mutations (e.g., *SOS1*, *REST*) or connexin-related pathways, or drug-induced (phenytoin, cyclosporine, calcium channel blockers). It has no established relationship to ALK/ROS1 signaling, tyrosine kinase inhibition, or any oncogenic driver pathway targeted by lorlatinib.

The `repurposing_rationale` attached to this prediction explicitly states there is **no known mechanistic link** — the drug's rationale field describes this as a pure TxGNN embedding-similarity artifact with "no supporting literature or trials." This means the top-ranked prediction in this evidence pack should be treated as biologically implausible rather than a genuine repurposing signal, and the report below reflects that honestly.

**Note on data quality:** Several lower-ranked candidates in this evidence pack (ranks 5, 7, 8, 10) have literature attached that appears mismatched to their disease labels — e.g., NSCLC RCT data (CROWN trial) tagged under "lung benign neoplasm," neuroblastoma/glioma case studies tagged under "lung germ cell tumor," frontotemporal dementia reviews tagged under an unrelated genetic syndrome (IBMPFD), and lorlatinib adverse-event case reports tagged under an unrelated dysmorphology syndrome. These appear to be knowledge-graph/ontology node mapping errors and should not be interpreted as clinical support for those specific candidate indications. Only **rank 4 (lung hilum carcinoma)** shows a plausible mechanistic link, since it is an anatomic-site subtype of ALK+ NSCLC — but is supported by only a single neoadjuvant case report (L4/S1), and arguably represents a restatement of the drug's known indication rather than a novel repurposing target.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Norway Market Information

No authorization data available — Lorlatinib is currently **not marketed** in Norway (`total_licenses: 0`).

---

## Cytotoxicity (Antineoplastic Drugs Only)

Lorlatinib is classified as antineoplastic based on its established use in NSCLC (per attached literature) and its drug class (ALK/ROS1 tyrosine kinase inhibitor).

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (third-generation ALK/ROS1 tyrosine kinase inhibitor) — not a conventional cytotoxic agent |
| Myelosuppression Risk | Low. Reported adverse events in the attached literature are predominantly metabolic and neurological rather than hematologic — hypercholesterolemia, hypertriglyceridemia, weight gain, edema, and CNS/mood effects are the hallmark toxicities (per pharmacovigilance and AE-management literature) |
| Emetogenicity Classification | Low (oral targeted agent; not associated with high emetogenic potential) |
| Monitoring Items | Fasting lipid panel (cholesterol, triglycerides), weight, CNS/cognitive/mood assessment, blood pressure, liver and renal function; rare reports of nephrotic syndrome and pulmonary toxicity warrant monitoring for proteinuria and respiratory symptoms |
| Handling Protection | Oral small-molecule kinase inhibitor — standard oral hazardous-drug handling precautions (e.g., per NIOSH hazardous drug list) are appropriate; does not require IV cytotoxic-drug handling protocols |

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked TxGNN prediction (Gingival Fibromatosis, 99.81% score) has zero corroborating clinical trials or literature, and the model's own rationale confirms no known mechanistic connection between ALK/ROS1 inhibition and this benign, non-oncologic condition. This is an unsupported L5 (model-only) prediction and does not meet the threshold for further evaluation.

**To proceed, the following is needed:**
- DG001 (Blocking): TFDA/regional drug label warnings and contraindications — required before any S1 safety screening can occur
- DG002 (High): Verified MOA data via DrugBank API to properly assess mechanistic plausibility for any future candidate indication
- A data-quality review of the TxGNN-to-literature mapping pipeline, given apparent disease-label mismatches identified in ranks 5, 7, 8, and 10 of this evidence pack
- If further exploration is warranted, prioritize rank 4 (lung hilum carcinoma) as a research question — it is the only candidate with a plausible mechanistic link and case-level clinical evidence, though it likely falls within the drug's already-approved ALK+ NSCLC indication rather than representing a true new indication
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

