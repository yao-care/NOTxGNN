---
layout: default
title: Nelarabine
parent: 僅模型預測 (L5)
nav_order: 238
evidence_level: L5
indication_count: 1
---

# Nelarabine
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

# Nelarabine: From T-cell Acute Lymphoblastic Leukemia to Relapsing-Remitting Multiple Sclerosis

## One-Sentence Summary

Nelarabine is a purine nucleoside analog chemotherapy agent originally developed for relapsed/refractory T-cell acute lymphoblastic leukemia and T-cell lymphoblastic lymphoma. The TxGNN model predicts it may be effective for **relapsing-remitting multiple sclerosis**, but this prediction is currently supported by **no registered clinical trials** and **no published literature** — it rests on the model score alone.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | T-cell acute lymphoblastic leukemia (T-ALL) / T-cell lymphoblastic lymphoma (T-LBL) *(general background knowledge — not present in the Norway license data, as the drug is not marketed there)* |
| Predicted New Indication | Relapsing-remitting multiple sclerosis |
| TxGNN Prediction Score | 99.43% |
| Evidence Level | L5 |
| Norway Market Status | Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the evidence pack. Based on general background knowledge, nelarabine is a prodrug of 9-β-D-arabinofuranosylguanine (ara-G), a purine nucleoside analog that is selectively phosphorylated and accumulates in T-lymphoblasts, causing DNA-strand breaks and cell death. Its clinical efficacy in T-ALL/T-LBL is well established, but this mechanism is directed at proliferating malignant T-cells rather than the autoimmune/neuroinflammatory processes underlying multiple sclerosis.

There is no direct mechanistic or clinical rationale in the evidence pack linking nelarabine's cytotoxic, T-cell-depleting activity to relapsing-remitting MS. While selective T-cell cytotoxicity is a shared theme with some MS immunomodulators (e.g., cladribine, another purine analog approved for MS), nelarabine's known neurotoxicity profile is a significant concern for use in a neurological disease population. This prediction should be treated as a model-generated hypothesis requiring substantial mechanistic and preclinical validation before further consideration.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Norway Market Information

Nelarabine currently has no marketing authorization in Norway (0 licenses on record); no product or indication data is available for this market.

---

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Conventional cytotoxic (purine nucleoside analog / antimetabolite — prodrug of ara-G) |
| Myelosuppression Risk | High — neutropenia, thrombocytopenia, and anemia are commonly reported; nelarabine also carries a distinct risk of severe neurotoxicity (peripheral neuropathy, somnolence, seizures) |
| Emetogenicity Classification | Low to moderate |
| Monitoring Items | CBC with differential, neurological status assessment (due to neurotoxicity risk), liver and renal function |
| Handling Protection | Must follow cytotoxic/hazardous drug handling regulations (USP <800> or equivalent) |

*Note: The above is based on general pharmacological knowledge of nelarabine, as no drug-specific toxicity data was provided in this evidence pack (see Data Gap DG002).*

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is supported only by a TxGNN model score (L5), with zero clinical trials or literature evidence, no MOA data, no Norway market presence, and unresolved safety data gaps (including TFDA-equivalent labeling, a Blocking-severity gap). There is currently no basis to move this candidate forward.

**To proceed, the following is needed:**
- Mechanism of action data to assess plausibility for a neuroinflammatory indication (DG002)
- Official warnings/contraindications/label data (DG001, Blocking)
- Any preclinical or exploratory clinical evidence linking nelarabine to MS or related autoimmune neurological conditions
- Confirmation of original indication and regulatory status from a validated source
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

