---
layout: default
title: Posaconazole
parent: 僅模型預測 (L5)
nav_order: 285
evidence_level: L5
indication_count: 1
---

# Posaconazole
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

# Posaconazole: From Invasive Fungal Infection Prophylaxis to Pneumocystosis

## One-Sentence Summary

Posaconazole is a triazole antifungal used in known clinical practice for prophylaxis of invasive fungal infections (e.g., aspergillosis, candidiasis) in high-risk immunocompromised patients.
The TxGNN model predicts it may be effective for **Pneumocystosis (Pneumocystis jirovecii pneumonia, PCP)**,
with **2 clinical trials** and **5 publications** currently identified, though none directly and specifically validate posaconazole use in PCP.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Prophylaxis of invasive fungal infections (Aspergillus/Candida) in high-risk immunocompromised patients (based on known drug-class use; no Norway license data available) |
| Predicted New Indication | Pneumocystosis |
| TxGNN Prediction Score | 99.77% |
| Evidence Level | L4 |
| Norway Market Status | ✗ Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the evidence pack. Based on known pharmacology, posaconazole is a triazole antifungal that inhibits fungal CYP51 (14α-demethylase), blocking ergosterol synthesis in the fungal cell membrane. It is established for prevention of invasive fungal infections in high-risk populations such as patients with hematologic malignancy, prolonged neutropenia, or graft-versus-host disease (GVHD) after stem cell transplantation.

Pneumocystis jirovecii is an atypical fungal organism with a distinct membrane sterol composition, and its susceptibility to conventional triazoles has historically been uncertain. However, posaconazole has documented off-label use as PCP prophylaxis/salvage therapy in patients intolerant of first-line TMP-SMX.

This represents a mechanistic extension rather than a direct pharmacological indication — the same high-risk transplant/hematology-oncology patient population that receives posaconazole for mold/yeast prophylaxis is also at elevated risk for PCP, providing an epidemiological rationale that runs parallel to, but does not substitute for, direct clinical validation.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT04368559](https://clinicaltrials.gov/study/NCT04368559) | Phase 3 | Completed | 602 | Compared IV rezafungin (an echinocandin, not posaconazole) vs. standard antimicrobial regimen for prevention of invasive fungal disease in allogeneic HSCT recipients. Relevance is indirect — different drug class, and target indication was invasive candidiasis, not PCP. |
| [NCT06859424](https://clinicaltrials.gov/study/NCT06859424) | Phase 2 | Recruiting | 358 | Platform trial evaluating post-transplant cyclophosphamide-based GVHD prophylaxis regimens in mismatched unrelated donor PBSC transplant. Does not specify posaconazole or PCP as primary endpoints; relevance limited to the shared high-risk transplant population background. |

Both trials are graded **C (indirect relevance)** — neither directly studies posaconazole for pneumocystosis.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [41232547](https://pubmed.ncbi.nlm.nih.gov/41232547/) | 2025 | Review/Guideline | Lancet Infectious Diseases | UK best-practice update on diagnosis of serious fungal diseases, covering non-culture diagnostic methods across invasive fungal disease categories including PCP. |
| [26901377](https://pubmed.ncbi.nlm.nih.gov/26901377/) | 2016 | Review | Swiss Medical Weekly | Overview of invasive candidiasis, aspergillosis, cryptococcosis, and Pneumocystis pneumonia; notes posaconazole's established role in reducing invasive candidiasis in high-risk hemato-oncology patients, without direct PCP treatment data. |
| [41362140](https://pubmed.ncbi.nlm.nih.gov/41362140/) | 2025 | Review/Guideline | Chinese Journal of Tuberculosis and Respiratory Diseases | 2025 clinical practice guideline for diagnosis/management of invasive pulmonary fungal disease in China, covering broad antifungal management principles. |
| [21973267](https://pubmed.ncbi.nlm.nih.gov/21973267/) | 2011 | PK Study | Clinical Pharmacokinetics | Reviews pulmonary epithelial lining fluid penetration of antifungal agents, relevant to posaconazole's lung tissue distribution but not disease-specific efficacy. |
| [35596686](https://pubmed.ncbi.nlm.nih.gov/35596686/) | 2022 | Cohort | Transplant Infectious Disease | Retrospective cohort on infectious complications (including fungal) in GVHD after liver transplantation; provides population context but no posaconazole-PCP outcome data. |

No publication in the current evidence pack reports a direct clinical outcome of posaconazole used specifically to treat or prevent pneumocystosis.

## Norway Market Information

Posaconazole is currently **not marketed in Norway**, and no drug authorization (marketing license) records are available in this evidence pack.

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Evidence is limited to mechanistic plausibility (L4) — the identified clinical trials are only indirectly related (different drug or different primary indication), and the literature consists of reviews/guidelines and background cohort data rather than direct evidence of posaconazole efficacy in pneumocystosis. The drug is also not currently marketed in Norway, and a blocking safety data gap (product label warnings/contraindications) prevents a complete S1 safety assessment.

**To proceed, the following is needed:**
- Norway/TFDA-equivalent package insert data (warnings, contraindications, DDI) to close the blocking data gap (DG001)
- Confirmed mechanism of action data from DrugBank (DG002)
- Direct clinical or in vitro evidence of posaconazole activity against *Pneumocystis jirovecii*, ideally dedicated PCP prophylaxis/treatment trials
- Route of administration and dosing feasibility assessment for the PCP patient population
- Clarification of original approved indication(s) and license status, since no Norway license records currently exist
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

