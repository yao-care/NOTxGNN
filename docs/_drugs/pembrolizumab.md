---
layout: default
title: Pembrolizumab
parent: 僅模型預測 (L5)
nav_order: 272
evidence_level: L5
indication_count: 10
---

# Pembrolizumab
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

Using no additional tooling — this is a direct content-generation task against the provided Evidence Pack, following the fixed report template.

# Pembrolizumab: From PD-1–Directed Oncology Immunotherapy (Indication Text Not Provided) to Gingival Fibromatosis

## One-Sentence Summary

Pembrolizumab is a PD-1–blocking monoclonal antibody used broadly in oncology (the evidence pack's cited literature references NSCLC, melanoma, MSI-H/dMMR cancers, and hepatocellular carcinoma, though the structured `original_indications` field itself is empty).
The TxGNN model's top-ranked prediction is **Gingival Fibromatosis**, but this is supported by **0 clinical trials** and **0 publications**, and the drug's own repurposing rationale states the mechanism does not apply to this benign condition.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not specified in the evidence pack (`original_indications` is empty); literature context indicates broad PD-1 checkpoint–inhibitor oncology use |
| Predicted New Indication | Fibromatosis, Gingival |
| TxGNN Prediction Score | 99.40% (rank 6326 among all predictions) |
| Evidence Level | L5 |
| Norway Market Status | ✗ Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available for this drug in the evidence pack (Data Gap DG002, High severity). Based on known pharmacology, pembrolizumab blocks the PD-1 receptor on T cells, disinhibiting anti-tumour immune responses in immunogenic, immune-evasive malignancies.

Gingival fibromatosis, however, is a benign fibrous tissue overgrowth condition — typically hereditary or drug-induced (e.g., by phenytoin, cyclosporine, calcium channel blockers) — and is not a malignancy with an immune-evasion phenotype. The repurposing rationale supplied with this prediction states explicitly that there is **no mechanistic link** between PD-1 blockade and gingival fibromatosis, and no clinical or literature evidence supports the association.

This prediction appears to be a network-based artifact of the TxGNN model (a high similarity score without a plausible biological basis), rather than a genuine repurposing signal. By contrast, other lower-ranked candidates in this same batch — *lung hilum carcinoma*, *lung germ cell tumor*, and *pulmonary sulcus neoplasm* — are anatomical/positional subtypes of lung malignancy where pembrolizumab's class-level NSCLC mechanism is at least theoretically extendable, and these were scored at decision stage S1 ("Research Question") rather than S0 ("Hold"). These may warrant separate evaluation ahead of the top-ranked candidate discussed here.

## Clinical Trial Evidence

Currently no related clinical trials registered

## Literature Evidence

Currently no related literature available

## Norway Market Information

Pembrolizumab is currently **not marketed** in Norway under this evidence pack (0 authorizations on record; `market_status` = 未上市). No product licenses are available to list.

## Cytotoxicity

*(Section included: although the structured `original_indications` field is empty, the cited literature throughout this evidence pack consistently identifies pembrolizumab as an antineoplastic PD-1 immune checkpoint inhibitor used across multiple cancer types.)*

| Item | Content |
|------|------|
| Cytotoxicity Classification | Immunotherapy (anti-PD-1 immune checkpoint inhibitor) — not a conventional cytotoxic agent |
| Myelosuppression Risk | Low — pembrolizumab does not act via direct cytotoxicity to marrow precursors; the dominant toxicity pattern is immune-related adverse events (irAEs) rather than classical myelosuppression |
| Emetogenicity Classification | Low |
| Monitoring Items | Baseline and periodic thyroid function (TSH/free T4), liver function, renal function, cortisol/ACTH (for hypophysitis), cardiac enzymes if myocarditis suspected, and clinical surveillance for irAEs (colitis, pneumonitis, dermatologic reactions, myositis/myasthenia gravis) |
| Handling Protection | As a monoclonal antibody biologic, pembrolizumab does not require the closed-system/cytotoxic hazardous-drug handling precautions used for conventional chemotherapy; administer per institutional oncology infusion protocol and the package insert |

## Safety Considerations

Please refer to the package insert for safety information. (Key warnings, contraindications, and DDI data are all recorded as Data Gaps in this evidence pack — DG001 is flagged as **Blocking**, meaning TFDA/label-level warnings and contraindications must be obtained before this candidate can even enter the S1 safety review stage.)

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked predicted indication (gingival fibromatosis) has zero clinical trial or literature support, and the supplied mechanistic rationale directly contradicts biological plausibility — a benign fibrous overgrowth condition has no established relationship to PD-1-mediated tumour immune evasion. Separately, a Blocking-severity data gap (missing TFDA label warnings/contraindications) prevents this candidate from formally entering the S1 safety evaluation stage regardless of indication-level evidence.

**To proceed, the following is needed:**
- Resolve DG001 (Blocking): obtain and parse the official TFDA/Norwegian label for warnings and contraindications
- Resolve DG002: obtain confirmed mechanism-of-action data from DrugBank
- Reconsider prioritizing the higher-plausibility candidates in this same prediction batch (lung hilum carcinoma, lung germ cell tumor, pulmonary sulcus neoplasm — currently at decision stage S1) rather than the top TxGNN-score candidate, which lacks biological plausibility
- If gingival fibromatosis is to be pursued further despite the above, dedicated preclinical/mechanistic studies would be required, as no clinical or literature evidence currently exists
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

