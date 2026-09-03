---
layout: default
title: Axitinib
parent: 僅模型預測 (L5)
nav_order: 43
evidence_level: L5
indication_count: 10
---

# Axitinib
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

# Axitinib: From Renal Cell Carcinoma to Xp11.2 Translocation/TFE3 Fusion-Associated Renal Cell Carcinoma

## One-Sentence Summary

Axitinib is a selective VEGFR1/2/3 tyrosine kinase inhibitor already approved worldwide (as Inlyta) for advanced/metastatic renal cell carcinoma.
The TxGNN model predicts it may also be effective for **renal cell carcinoma associated with Xp11.2 translocations/TFE3 gene fusions**, a rare, genetically distinct RCC subtype seen mainly in children and young adults,
with **1 clinical trial** currently supporting this direction and **no published literature** specific to this subtype yet.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Advanced/metastatic Renal Cell Carcinoma (globally approved as Inlyta; per evidence pack, this is axitinib's existing core indication, not a new use) |
| Predicted New Indication | Renal cell carcinoma associated with Xp11.2 translocations/TFE3 gene fusions |
| TxGNN Prediction Score | 99.90% |
| Evidence Level | L2 |
| Norway Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data for axitinib is not available in this evidence pack (`original_moa`: Data Gap). Based on information embedded in the repurposing rationale, axitinib is a highly selective, potent inhibitor of VEGFR1, VEGFR2, and VEGFR3, and it is already the approved standard of care for advanced/metastatic renal cell carcinoma — this appears in the evidence pack itself as the drug's existing core indication, not a repurposing candidate.

Xp11.2 translocation/TFE3 gene fusion RCC is a genetically and histologically distinct RCC subtype, most common in children, adolescents, and young adults. Despite its distinct molecular driver (TFE3 fusion), tumor biology in this subtype still shows VEGF/mTOR pathway activation, providing a plausible mechanistic rationale for extrapolating axitinib's antiangiogenic activity from classic clear-cell RCC to this subtype. However, subtype-specific efficacy evidence remains sparse — the only supporting trial enrolls a broad translocation/TFE3-RCC population "across all age groups" rather than confirming activity specifically in the Xp11.2 fusion subtype.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT03595124](https://clinicaltrials.gov/study/NCT03595124) | Phase 2 | Active, not recruiting | 15 | Randomized trial of axitinib/nivolumab combination vs. single-agent nivolumab in TFE/translocation RCC across all age groups; small sample, no subtype-specific stratification for Xp11.2 fusion reported. |

---

## Literature Evidence

Currently no related literature available.

---

## Norway Market Information

Axitinib is currently **not marketed in Norway** (0 authorizations recorded). No dosage forms, product names, or approved indication texts are available for this market.

---

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (VEGFR1/2/3 tyrosine kinase inhibitor) |
| Myelosuppression Risk | Please refer to the package insert warnings and precautions |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | Please refer to the package insert warnings and precautions |
| Handling Protection | Please refer to the package insert warnings and precautions |

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The only supporting trial (NCT03595124) is a small (n=15) Phase 2 study covering a broad translocation/TFE3-RCC population rather than confirming activity specifically in Xp11.2 fusion-associated RCC, and no literature currently supports this specific indication. Combined with the drug's unmarketed status in Norway and blocking gaps in TFDA/local safety labeling, evidence is insufficient to advance beyond a research question at this stage.

**To proceed, the following is needed:**
- TFDA/Norwegian package insert data (warnings, contraindications) — currently a **Blocking** data gap (DG001)
- Detailed mechanism of action documentation via DrugBank API (DG002)
- Mature, subtype-stratified results from NCT03595124 confirming efficacy specifically in Xp11.2/TFE3 fusion RCC
- Assessment of the regulatory pathway for Norway market entry, given axitinib currently holds zero local authorizations
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

