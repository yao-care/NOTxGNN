---
layout: default
title: Ritonavir
parent: 僅模型預測 (L5)
nav_order: 310
evidence_level: L5
indication_count: 3
---

# Ritonavir
{: .fs-9 }

證據等級: **L5** | 預測適應症: **3** 個
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

# Ritonavir: From Unspecified Original Indication to Feline Acquired Immunodeficiency Syndrome

## One-Sentence Summary

> Ritonavir's original indication and mechanism of action are not documented in this evidence pack (flagged as data gaps DG001/DG002).
> The TxGNN model predicts a possible association with **Feline Acquired Immunodeficiency Syndrome** (score 99.92%),
> but this is supported by only **1 clinical trial** — which studies human HIV-1, not feline AIDS — and **0 directly relevant publications**.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available in evidence pack (`original_indications: []`) |
| Predicted New Indication | Feline Acquired Immunodeficiency Syndrome |
| TxGNN Prediction Score | 99.92% (rank 1134) |
| Evidence Level | L5 — the only associated trial does not study the predicted (feline) indication; no literature |
| Taiwan Market Status | 未上市 (Not Marketed) |
| Number of Authorizations | 0 |
| Recommended Decision | **Hold** |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the evidence pack (Data Gap **DG002**, High severity). The drug's original indication history is also not documented (`original_indications` is empty), so the relationship between ritonavir's established use and the predicted new indication cannot be verified from the supplied data alone.

Separately, the predicted indication itself — feline acquired immunodeficiency syndrome — is a veterinary disease of cats (caused by feline immunodeficiency virus, FIV), not a human condition. The single clinical trial attached as supporting evidence (NCT02770508) actually enrolls human HIV-1 patients, not cats with FIV infection. This population mismatch suggests the TxGNN score likely reflects knowledge-graph embedding similarity between lentiviral disease nodes (HIV-1 ~ FIV) rather than direct clinical support for using ritonavir in feline AIDS. Without confirmed MOA data and without any veterinary pharmacology or dosing evidence, mechanistic plausibility cannot be independently confirmed here.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT02770508](https://clinicaltrials.gov/study/NCT02770508) | Phase 4 | Completed | 145 | Compared ritonavir-boosted darunavir + lamivudine vs. boosted darunavir + emtricitabine/tenofovir or lamivudine/tenofovir in treatment-naïve **human** HIV-1 patients. *Note: this trial studies human HIV-1, not feline AIDS; relevance grading is still marked "pending" in source data.* |

---

## Literature Evidence

Currently no related literature available for this predicted indication (feline acquired immunodeficiency syndrome).

---

## Taiwan Market Information

No authorization records available — ritonavir is not currently marketed in Taiwan per this evidence pack (`total_licenses: 0`).

---

## Safety Considerations

A **Blocking**-severity data gap (**DG001**) has been identified: TFDA package insert warnings and contraindications have not yet been retrieved, which means this candidate **cannot proceed to S1 safety pre-assessment** until this is remediated. All other safety fields in this evidence pack (key warnings, contraindications, drug-drug interactions) are unpopulated (`query_status: not_found`).

Please refer to the package insert for safety information once available.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- A Blocking data gap (DG001 — missing TFDA label/warnings) explicitly prevents entry into safety pre-assessment (S1).
- The predicted indication is a non-human (feline) disease, and the sole supporting clinical trial does not actually study that indication; overall evidence level is L5.
- The drug is not currently marketed in Taiwan (0 authorizations), and MOA data needed to assess mechanistic plausibility is missing (DG002).

**To proceed, the following is needed:**
- Retrieve TFDA package insert (warnings/contraindications) to close DG001 (Blocking)
- Retrieve DrugBank MOA data to close DG002 (High)
- Clarify whether the TxGNN prediction for "feline acquired immunodeficiency syndrome" reflects a genuine repurposing signal or a cross-species knowledge-graph artifact before further evaluation
- Complete relevance grading for the pending trial/literature classifications (also consider re-reviewing rank 2, "simian immunodeficiency virus infection," which has more literature but remains an animal-model indication)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

