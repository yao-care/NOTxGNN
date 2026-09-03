---
layout: default
title: Delamanid
parent: 僅模型預測 (L5)
nav_order: 104
evidence_level: L5
indication_count: 7
---

# Delamanid
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

# Delamanid: From Multidrug-Resistant Tuberculosis to Bovine Tuberculosis

## One-Sentence Summary

> Delamanid is a nitro-dihydro-imidazooxazole antimycobacterial, established for treating multidrug-resistant pulmonary tuberculosis (MDR-TB) in humans.
> The TxGNN model's top prediction points to **Tuberculosis, Bovine** (caused by *Mycobacterium bovis*, a close relative of *M. tuberculosis*),
> but this specific prediction is currently supported only by **0 clinical trials** and **1 indirect publication** (pathogen genomics, not a drug efficacy study).
> A related, more clinically actionable prediction in the same evidence set — **Inactive Tuberculosis** — is backed by **2 active Phase 2/3 clinical trials on delamanid itself** and **20 publications**, and is flagged below for consideration.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Multidrug-resistant pulmonary tuberculosis (MDR-TB) — known pharmacological use; not present in the current regulatory record (see Data Gaps) |
| Predicted New Indication | Tuberculosis, Bovine |
| TxGNN Prediction Score | 99.91% |
| Evidence Level | L5 (model prediction only; no delamanid-specific clinical or preclinical study for this indication) |
| Taiwan Market Status | ✗ 未上市 (Not marketed) |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this evidence pack (flagged as DG002, High severity). Based on established pharmacological knowledge, delamanid is a nitro-dihydro-imidazooxazole derivative that inhibits mycolic acid biosynthesis in the mycobacterial cell wall, and it is used clinically (outside this jurisdiction) as part of combination therapy for MDR pulmonary tuberculosis caused by *Mycobacterium tuberculosis*.

*Mycobacterium bovis*, the causative agent of bovine (and zoonotic) tuberculosis, is a member of the same *Mycobacterium tuberculosis* complex and shares a nearly identical cell wall architecture, including mycolic acid biosynthesis pathways. Mechanistically, this makes cross-species activity plausible — the same target that delamanid inhibits in *M. tuberculosis* is largely conserved in *M. bovis*.

However, the single supporting publication (PMID 39487429) is a whole-genome sequencing study of drug resistance patterns in *M. bovis* isolates — it characterizes the pathogen, but does **not** test delamanid's efficacy against it. This prediction should therefore be read as a target/pathogen-similarity hypothesis rather than an evidence-backed repurposing opportunity.

**Note:** Within the same evidence pack, rank 2 ("Inactive Tuberculosis") shares the same underlying biology but has direct clinical trial support for delamanid, including an active Phase 2/3 trial (CRUSH-TB) and a Phase 3 prevention trial (PHOENIx MDR-TB) — see below.

---

## Clinical Trial Evidence

**For the top-ranked prediction (Tuberculosis, Bovine): Currently no related clinical trials registered.**

*For reference, the closely related rank-2 prediction ("Inactive Tuberculosis") has direct delamanid trial support:*

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT05766267](https://clinicaltrials.gov/study/NCT05766267) | Phase 2/3 | Active, not recruiting | 288 | 17-week short-course regimens (BMZ + Rifabutin or Delamanid) vs. standard 6-month regimen for pulmonary TB |
| [NCT03568383](https://clinicaltrials.gov/study/NCT03568383) | Phase 3 | Active, not recruiting | 5,832 | 26 weeks delamanid vs. 26 weeks isoniazid for TB prevention in high-risk household contacts of MDR-TB index cases |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [39487429](https://pubmed.ncbi.nlm.nih.gov/39487429/) | 2024 | Molecular epidemiology (WGS) | BMC Genomics | Whole-genome sequencing of zoonotic *M. bovis* isolates characterizing genetic diversity and drug-resistance markers; does not evaluate delamanid directly |

---

## Taiwan Market Information

Delamanid currently holds **no marketing authorization** in this jurisdiction (`total_licenses: 0`, `market_status: 未上市`). No license records are available to summarize.

---

## Safety Considerations

Please refer to the package insert for safety information.

*(Key warnings, contraindications, and drug-drug interaction data are all currently unavailable — flagged as DG001, Blocking severity, since it prevents S1 safety pre-assessment.)*

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked prediction (Tuberculosis, Bovine) is supported only by the TxGNN score and one indirect pathogen-genomics paper — no clinical trials or delamanid-specific studies exist for this indication (Evidence Level L5). Combined with a Blocking data gap on TFDA warnings/contraindications (DG001) and the drug's unmarketed status locally, there is insufficient evidence to advance this specific prediction.

**To proceed, the following is needed:**
- TFDA/manufacturer package insert (warnings, contraindications) to close DG001 before any safety pre-assessment
- DrugBank MOA confirmation to close DG002 and support mechanistic rationale
- Preclinical or *in vitro* efficacy data of delamanid against *M. bovis* specifically
- **Consider re-scoping the repurposing target to "Inactive Tuberculosis" (rank 2)**, which has active Phase 2/3 delamanid-specific trials and substantially more literature support, and would represent a stronger candidate for Guardrails-based evaluation
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

