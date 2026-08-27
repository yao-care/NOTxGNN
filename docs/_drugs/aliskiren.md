---
layout: default
title: Aliskiren
parent: 僅模型預測 (L5)
nav_order: 24
evidence_level: L5
indication_count: 7
---

# Aliskiren
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

Using the TxGNN evidence-pack fields directly (no fabrication) to produce the report below. Since `original_indications` and `licenses` are empty and `original_moa` is `[Data Gap]`, I've flagged those explicitly rather than inventing data, and I focus the templated sections on `predicted_indications[0]` (the highest-scoring candidate) as the format specifies.

---

# Aliskiren: From Hypertension to Pulmonary Hypertension Owing to Lung Disease and/or Hypoxia

*Note: the evidence pack contains no `original_indications` text and no Norway license records for aliskiren, so the "original indication" below is stated from the drug's known pharmacological class (direct renin inhibitor, indicated for essential hypertension), not from pack data.*

## One-Sentence Summary

Aliskiren is a direct renin inhibitor originally developed for essential hypertension. The TxGNN model predicts it may be effective for **pulmonary hypertension owing to lung disease and/or hypoxia**, but this direction is currently supported only by the model's score — **0 clinical trials** and none of the **20 retrieved publications** actually study aliskiren, RAAS inhibition, or pulmonary hypertension. This is an algorithm-only signal, not a drug-specific finding.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Essential hypertension (from known drug class; not present in evidence pack — no `original_indications` or Norway license text supplied) |
| Predicted New Indication | Pulmonary hypertension owing to lung disease and/or hypoxia |
| TxGNN Prediction Score | 99.98% |
| Evidence Level | L5 (model prediction only) |
| Norway Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available (marked as a High-severity data gap, DG002). Based on known pharmacology, aliskiren is a direct renin inhibitor (DRI) that blocks the rate-limiting step of the renin-angiotensin-aldosterone system (RAAS), and its efficacy in essential hypertension is well established.

The theoretical link to pulmonary hypertension is that chronic hypoxia can locally activate RAAS and promote pulmonary vascular remodeling, which in principle could make renin inhibition a plausible intervention point. This is a biologically coherent hypothesis, not a proven one.

Critically, none of the 20 literature records returned for this pairing mention aliskiren, RAAS inhibitors, or pulmonary hypertension treatment — they are general hypoxia-biology and neurodegeneration literature (e.g., high-altitude physiology, cognitive impairment under hypoxia, tumor hypoxia signaling). No clinical trials were identified either. The TxGNN score therefore reflects a pure graph-based association, with no drug-specific mechanistic or clinical corroboration in the current evidence pack.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

All 20 retrieved publications concern hypoxia biology in general and **do not specifically address aliskiren, RAAS inhibition, or pulmonary hypertension**. They are listed below for transparency, prioritized by review-type classification (no RCTs were returned):

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [33862277](https://pubmed.ncbi.nlm.nih.gov/33862277/) | 2021 | Review | Ageing Research Reviews | Hypoxia's dual role in neurodegeneration vs. potential neuroprotection at altitude/in disease; no drug-specific content |
| [34618295](https://pubmed.ncbi.nlm.nih.gov/34618295/) | 2022 | Review | Metabolic Brain Disease | Cognitive impairment mechanisms under acute vs. chronic hypoxia |
| [21328446](https://pubmed.ncbi.nlm.nih.gov/21328446/) | 2011 | Review | Journal of Cellular Biochemistry | General hypoxia-mediated biological control (metabolism, angiogenesis, disease) |
| [11172576](https://pubmed.ncbi.nlm.nih.gov/11172576/) | 2000 | Review | Respiratory Care Clinics of North America | Mechanisms of hypoxemia (V/Q mismatch, shunt, hypoventilation) — general respiratory physiology |
| [34535359](https://pubmed.ncbi.nlm.nih.gov/34535359/) | 2021 | Review | Clinical Oncology | Therapeutic modification of tumor hypoxia (radiotherapy resistance context) |
| [31961750](https://pubmed.ncbi.nlm.nih.gov/31961750/) | 2020 | Review | Annual Review of Immunology | HIF pathway role in innate immunity/inflammation |
| [28219680](https://pubmed.ncbi.nlm.nih.gov/28219680/) | 2017 | Review | Experimental Cell Research | Transcriptional repression mechanisms under hypoxia (HIF regulation) |
| [40347693](https://pubmed.ncbi.nlm.nih.gov/40347693/) | 2025 | Review | Redox Biology | Hypoxia's role in multiple sclerosis pathology |
| [27146279](https://pubmed.ncbi.nlm.nih.gov/27146279/) | 2017 | Review | Cephalalgia | Hypoxic mechanisms in primary headache disorders |
| [36100192](https://pubmed.ncbi.nlm.nih.gov/36100192/) | 2022 | Review | Journal of Controlled Release | Tumor hypoxia-associated nanomedicine strategies |

*10 of 20 records shown (prioritized by Review classification); the remaining 10 are lower-tier/uncategorized ("pending") records on unrelated hypoxia topics (e.g., cancer HIF signaling, cerebral anoxia case reports) and add no additional relevance.*

## Norway Market Information

Aliskiren currently has **no marketing authorization in Norway** (status: Not Marketed; 0 licenses on file). No product, dosage form, or approved-indication data is available from Norwegian regulatory records.

## Safety Considerations

Please refer to the package insert for safety information. Note that the evidence pack flags TFDA/label-equivalent warnings and contraindications as a **Blocking** data gap (DG001) — this specifically prevents the candidate from entering the S1 safety pre-assessment stage, independent of the efficacy evidence discussed above.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN score is high, but the supporting evidence is L5 (model prediction only) — there are no clinical trials and no literature that actually studies aliskiren, RAAS inhibition, or pulmonary hypertension. Combined with a Blocking gap on safety/label data and no market presence in Norway, there is no basis to advance this indication pairing beyond hypothesis stage.

**To proceed, the following is needed:**
- TFDA-equivalent package insert data (warnings, contraindications) to clear the Blocking gap (DG001) and allow entry into S1 safety pre-assessment
- Detailed mechanism-of-action documentation (DG002) to substantiate the RAAS–hypoxia–pulmonary vascular remodeling rationale
- Aliskiren- or RAAS-inhibitor-specific preclinical or clinical studies in pulmonary hypertension (none currently exist in the retrieved literature)
- For context: the evidence pack also lists 6 other predicted indications for aliskiren with substantially different evidence profiles — notably "cerebrovascular disorder" (L2, includes ALTITUDE-trial post-hoc data), though that evidence shows an *increased* risk of stroke/hypotension with aliskiren + ACEI/ARB combination therapy rather than benefit, and should be reviewed as a safety signal, not a repurposing opportunity, before any further action on this drug
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

