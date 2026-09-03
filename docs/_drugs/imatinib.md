---
layout: default
title: Imatinib
parent: 僅模型預測 (L5)
nav_order: 177
evidence_level: L5
indication_count: 10
---

# Imatinib
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

# Imatinib: From Chronic Myeloid Leukaemia/GIST to Heart Fibrosarcoma

## One-Sentence Summary

> Imatinib was originally marketed for chronic myeloid leukaemia and certain gastrointestinal stromal tumours (GIST) as a tyrosine kinase inhibitor.
> The TxGNN model predicts it may be effective for **Heart Fibrosarcoma**,
> but currently only **0 clinical trials** and **1 publication** (a review/commentary) support this specific direction.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Chronic myeloid leukaemia; gastrointestinal stromal tumour (GIST) — per literature reference (PMID 18623899) |
| Predicted New Indication | Heart Fibrosarcoma |
| TxGNN Prediction Score | 99.94% |
| Evidence Level | L4 |
| Norway Market Status | ✗ Not Marketed (未上市) |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data (`original_moa`) is not available in the structured drug record. Based on the repurposing rationale provided in this evidence pack, imatinib inhibits BCR-ABL, KIT, and PDGFR tyrosine kinases — the same mechanism underlying its approved use in CML and GIST.

The proposed link to heart fibrosarcoma is purely mechanistic inference: **if** a given heart fibrosarcoma tumour harbours a PDGFR-driven genotype, it could theoretically be sensitive to imatinib. However, there is no cardiac tumour–specific data (preclinical or clinical) confirming this, and no evidence that heart fibrosarcomas commonly express PDGFR/KIT alterations. This is explicitly flagged in the evidence pack as an inferential (not confirmed) mechanistic link, which is why the evidence level is rated L4 rather than higher.

By contrast, other fibrosarcoma-family predictions in this same evidence pack (e.g., dermatofibrosarcoma protuberans / "fibroblastic neoplasm" and "conventional fibrosarcoma") have much stronger mechanistic and clinical support, since DFSP is driven by a COL1A1-PDGFB fusion that is a well-established, direct imatinib target. Heart fibrosarcoma does not currently have this level of molecular characterization in the supplied evidence.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [18623899](https://pubmed.ncbi.nlm.nih.gov/18623899/) | 2008 | Review/Commentary | Prescrire International | Discusses imatinib's expanding indications since its original approval for CML and GIST; notes that newer indications, while promising, are not always supported by robust comparative evidence (e.g., non-comparative trial data in Ph+ ALL). Does not specifically address heart fibrosarcoma. |

---

## Norway Market Information

Currently no marketing authorization records available in Norway (0 licenses on file; market status: 未上市 / Not Marketed).

---

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (tyrosine kinase inhibitor targeting BCR-ABL/KIT/PDGFR) |
| Myelosuppression Risk | Please refer to the package insert warnings and precautions |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | Please refer to the package insert warnings and precautions |
| Handling Protection | Please refer to the package insert warnings and precautions |

---

## Safety Considerations

Please refer to the package insert for safety information.

*(Note: TFDA-equivalent label warnings/contraindications are flagged as a Blocking data gap (DG001) in this evidence pack and must be resolved before any S1 safety review can proceed.)*

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The mechanistic link between imatinib and heart fibrosarcoma is inferential rather than confirmed — there are no clinical trials and only a single non-specific review-level publication. Combined with the missing regulatory label/safety data (Blocking gap DG001), the evidence does not meet the bar to advance this candidate past S1.

**To proceed, the following is needed:**
- TFDA-equivalent product label (warnings, contraindications) to clear the Blocking safety gap (DG001)
- Confirmed mechanism of action data (currently marked as Data Gap) (DG002)
- Molecular/genomic characterization data confirming PDGFR/KIT/BCR-ABL alterations specifically in heart fibrosarcoma cohorts
- Preclinical (in vitro/in vivo) or case-level clinical evidence specific to cardiac fibrosarcoma before considering trial design

*For reference: within this same evidence pack, "conventional fibrosarcoma" (rank 3, L2, Research Question) and "fibroblastic neoplasm"/DFSP (rank 2, L3, Research Question) show substantially stronger mechanistic and trial-level support for imatinib repurposing and may be more actionable candidates for further evaluation.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

