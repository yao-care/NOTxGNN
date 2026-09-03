---
layout: default
title: Rivaroxaban
parent: 僅模型預測 (L5)
nav_order: 311
evidence_level: L5
indication_count: 4
---

# Rivaroxaban
{: .fs-9 }

證據等級: **L5** | 預測適應症: **4** 個
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

# Rivaroxaban: From Anticoagulation (VTE/AF) to Rheumatoid Arthritis

## One-Sentence Summary

> Rivaroxaban is a Factor Xa inhibitor used for anticoagulation (VTE prophylaxis/treatment and stroke prevention in atrial fibrillation), as referenced across the trial and literature evidence in this pack (e.g., EINSTEIN, ACT trials).
> The TxGNN model predicts it may be effective for **Rheumatoid Arthritis**,
> but **0 clinical trials** and only **4 tangentially related publications** currently support this direction, and the mechanistic rationale itself flags this as likely a comorbidity artifact rather than a true treatment signal.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not confirmed via regulatory filing (drug not marketed in Norway); evidence pack context indicates anticoagulation for VTE/AF |
| Predicted New Indication | Rheumatoid Arthritis |
| TxGNN Prediction Score | 99.57% |
| Evidence Level | L4 |
| Norway Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the structured drug record (MOA field is a data gap). Based on evidence within this pack, rivaroxaban is a direct Factor Xa inhibitor used for anticoagulation — it has no known anti-inflammatory or immunomodulatory activity.

Rheumatoid arthritis (RA) is a chronic autoimmune inflammatory disease. RA patients do carry an elevated risk of venous thromboembolism (VTE) due to chronic inflammation, and in clinical practice such patients sometimes require anticoagulant therapy — but this represents **comorbidity management**, not treatment of RA itself.

The evidence pack's own mechanistic assessment is explicit on this point: none of the four supporting publications demonstrate an anti-rheumatic effect of rivaroxaban. The literature instead covers VTE diagnosis/management (including in RA patients as an incidental comorbidity), thrombin generation assays in autoimmune disease, and DOAC adherence patterns. The high TxGNN score most likely reflects a learned RA–VTE comorbidity association in the knowledge graph rather than a causal RA-treatment pathway. This candidate should be interpreted with significant caution.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [33141212](https://pubmed.ncbi.nlm.nih.gov/33141212/) | 2020 | Review | JAMA | General review of lower-extremity DVT diagnosis/treatment; not RA-specific |
| [34175144](https://pubmed.ncbi.nlm.nih.gov/34175144/) | 2021 | Review | La Revue de médecine interne | Thrombin generation assay use in autoimmune disease (incl. antiphospholipid syndrome) for hypercoagulability screening; not a rivaroxaban-RA efficacy study |
| [29621248](https://pubmed.ncbi.nlm.nih.gov/29621248/) | 2018 | Cohort | PLoS One | Adherence comparison of rivaroxaban vs. apixaban in atrial fibrillation; unrelated to RA |
| [41918541](https://pubmed.ncbi.nlm.nih.gov/41918541/) | 2026 | Case Report | Cureus | Case of thromboembolic stroke in an 88-year-old with AF who incidentally had steroid-treated RA; RA is a background detail, not a treatment target |

---

## Norway Market Information

Currently no marketing authorization on file for rivaroxaban in Norway (0 licenses; market status: Not Marketed).

---

## Safety Considerations

Please refer to the package insert for safety information.

*(Note: TFDA/label warnings, contraindications, and DDI data are flagged as a blocking data gap in this evidence pack — see Conclusion.)*

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
There is no clinical trial evidence and no literature directly demonstrating a therapeutic effect of rivaroxaban on rheumatoid arthritis; the drug's known Factor Xa-inhibitor mechanism has no plausible link to RA disease activity, and the supporting literature relates to VTE management in RA patients rather than RA treatment itself. Combined with an S0 decision stage and L4 evidence level, this candidate does not meet the bar to proceed.

**To proceed, the following is needed:**
- TFDA/regulatory label data (warnings, contraindications) — currently a **Blocking** data gap
- Confirmed mechanism of action (MOA) from DrugBank — currently a **High** severity data gap
- Any preclinical/mechanistic study directly linking Factor Xa inhibition to RA disease pathways, if such evidence exists
- Should this candidate be revisited, the other TxGNN-flagged indications for rivaroxaban in this pack (gout, HIV infection, brachydactyly-syndactyly syndrome) were also reviewed and are similarly Hold — gout and the rare skeletal disorder have essentially no supporting evidence, and HIV-related evidence concerns anticoagulant safety in HIV patients (drug-drug interactions with antiretrovirals) rather than antiviral efficacy
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

