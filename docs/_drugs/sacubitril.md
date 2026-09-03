---
layout: default
title: Sacubitril
parent: 僅模型預測 (L5)
nav_order: 319
evidence_level: L5
indication_count: 5
---

# Sacubitril
{: .fs-9 }

證據等級: **L5** | 預測適應症: **5** 個
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

# Sacubitril: From Heart Failure to Diabetic Nephropathy

## One-Sentence Summary

> Sacubitril, marketed only in combination with valsartan (ARNI, e.g. Entresto), is internationally established for heart failure with reduced ejection fraction (HFrEF). Among five TxGNN-predicted indications, **Diabetic Nephropathy** is the only one supported by actual evidence — **2 clinical trials** and **17 publications** — while the model's two highest-ranked predictions are assessed as mechanistic false positives with no supporting data.

**Note on candidate selection:** TxGNN's top-ranked prediction (score 99.58%, "brain small vessel disease 1 with or without ocular anomalies") and second-ranked prediction (score 99.57%, a COL4A1-related hematuria/retinal syndrome) are excluded from this report. Both are flagged in the evidence pack itself as false positives — the associated literature consists entirely of unrelated congenital ophthalmologic case reports, and no mechanistic link to neprilysin inhibition exists. This report instead evaluates rank 3, **Diabetic Nephropathy**, which is the highest-ranked prediction with genuine clinical trial and literature support.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Heart failure with reduced ejection fraction (HFrEF), as sacubitril/valsartan combination — not captured in Norway regulatory data since the product is currently unlicensed there |
| Predicted New Indication | Diabetic Nephropathy |
| TxGNN Prediction Score | 99.50% |
| Evidence Level | L3 |
| Norway Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not yet available in DrugBank for this record (data gap DG002). Based on known pharmacology, sacubitril is the prodrug component of the ARNI (angiotensin receptor–neprilysin inhibitor) combination sacubitril/valsartan. Sacubitril inhibits neprilysin, an enzyme that degrades natriuretic peptides, thereby raising natriuretic peptide levels; the valsartan component blocks the angiotensin II type 1 receptor. Together these actions reduce cardiac wall stress and blood pressure, which underlies the drug's proven efficacy in HFrEF.

The link between heart failure and diabetic nephropathy is pharmacologically plausible rather than coincidental: both conditions share overlapping pathophysiology involving the renin-angiotensin-aldosterone system (RAAS), glomerular hyperfiltration, and volume/pressure overload. Elevated natriuretic peptide activity from neprilysin inhibition is hypothesized to reduce intraglomerular pressure and glomerulosclerosis, while the ARB component already has established renoprotective effects in diabetic kidney disease independent of the ARNI combination.

Multiple animal models (db/db mice, streptozotocin-induced diabetic rats, Zucker Obese rats) consistently show that sacubitril/valsartan reduces proteinuria, oxidative stress, and inflammatory markers (including NLRP3 inflammasome and Nrf2/HO-1 pathway modulation) more effectively than ARB monotherapy. A secondary analysis of the PARADIGM-HF trial (PMID 29661699) found neprilysin inhibition slowed renal function decline in patients with type 2 diabetes and HFrEF. However, no completed trial has used diabetic nephropathy as its primary endpoint — the dedicated Phase 4 trial (NCT06501651) has not yet begun recruiting.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT06501651](https://clinicaltrials.gov/study/NCT06501651) | Phase 4 | Not yet recruiting | 297 | Randomized, controlled, multicenter trial comparing sacubitril/valsartan vs. valsartan alone in patients with essential hypertension and type 2 diabetic nephropathy; 12-week treatment period, 2:1 randomization. Directly targets the indication but has no results yet. |
| [NCT04735354](https://clinicaltrials.gov/study/NCT04735354) | N/A | Completed | 268 | Retrospective, non-interventional real-world EMR study in India of HFrEF patients on sacubitril/valsartan; provides only indirect metabolic/renal safety signal, not a diabetic nephropathy efficacy trial. |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [29661699](https://pubmed.ncbi.nlm.nih.gov/29661699/) | 2018 | RCT (secondary analysis) | Lancet Diabetes Endocrinol | Secondary analysis of PARADIGM-HF trial: neprilysin inhibition slowed renal function decline in type 2 diabetics with HFrEF on background RAAS blockade. |
| [37549515](https://pubmed.ncbi.nlm.nih.gov/37549515/) | 2023 | Cohort (randomized) | Int Immunopharmacol | 112 diabetic nephropathy patients with hypertension; sacubitril/valsartan combined with nifedipine improved renal function vs. valsartan combination. |
| [40416927](https://pubmed.ncbi.nlm.nih.gov/40416927/) | 2025 | Clinical study | Diabetes Metab Syndr Obes | BOLD-MRI study evaluating renal protective effects of sacubitril/valsartan in type 2 diabetics. |
| [37625003](https://pubmed.ncbi.nlm.nih.gov/37625003/) | 2023 | Review | Diabetes Care | Overview of diabetic kidney disease therapy pillars, situating RAAS/neprilysin-targeting agents among evolving treatment options. |
| [34431635](https://pubmed.ncbi.nlm.nih.gov/34431635/) | 2021 | Review | Rev Med Suisse | Discusses potential role of sacubitril/valsartan in type 2 diabetes, including glycemic and renal effects. |
| [35992034](https://pubmed.ncbi.nlm.nih.gov/35992034/) | 2022 | Animal study | Diabetes Metab Syndr Obes | Sacubitril/valsartan improved early diabetic nephropathy progression in rats via NLRP3 inflammasome inhibition. |
| [36589853](https://pubmed.ncbi.nlm.nih.gov/36589853/) | 2022 | Animal study | Front Endocrinol | Sacubitril/valsartan improved diabetic kidney disease and regulated gut microbiota in mice. |
| [32596035](https://pubmed.ncbi.nlm.nih.gov/32596035/) | 2020 | Animal study | PeerJ | LCZ696 mitigated diabetic nephropathy via reduced oxidative stress, NF-κB inflammation, and glomerulosclerosis in rats. |
| [33870733](https://pubmed.ncbi.nlm.nih.gov/33870733/) | 2021 | Animal study | Am J Physiol Renal Physiol | Differential renoprotective effects of sacubitril/valsartan vs. valsartan alone in db/db and KKAy diabetic mouse models. |
| [37202215](https://pubmed.ncbi.nlm.nih.gov/37202215/) | 2023 | Animal study | Nephrol Dial Transplant | Sacubitril/valsartan ameliorated renal tubulointerstitial injury via increased renal plasma flow in a mouse model of diabetes with aldosterone excess. |

---

## Norway Market Information

Currently no marketing authorizations recorded in Norway — sacubitril (as sacubitril/valsartan) is not marketed under this regulatory dataset (0 licenses).

---

## Safety Considerations

Please refer to the package insert for safety information. Key warnings, contraindications, and drug-drug interaction data are not currently available in this evidence pack (data gap DG001, flagged as **Blocking** — required before initial safety assessment can proceed).

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The mechanistic rationale and preclinical/observational evidence for sacubitril/valsartan in diabetic nephropathy are reasonably consistent (L3), but no completed trial has used renal outcomes as a primary endpoint, and the only purpose-built Phase 4 RCT (NCT06501651) has not yet started recruiting. Combined with the drug's currently unlicensed status in Norway and a blocking gap in labeling/safety data, a "Go" or "Guardrails" recommendation is premature.

**To proceed, the following is needed:**
- Results from NCT06501651 (Hyper-Save Study) once recruitment and follow-up are complete
- TFDA/Norwegian product labeling (warnings, contraindications, DDI) to close blocking gap DG001
- DrugBank-sourced mechanism of action detail to close gap DG002
- Confirmation of whether/when a Norway marketing authorization application is planned, given current unmarketed status
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

