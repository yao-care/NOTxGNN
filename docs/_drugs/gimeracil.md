---
layout: default
title: Gimeracil
parent: 僅模型預測 (L5)
nav_order: 160
evidence_level: L5
indication_count: 10
---

# Gimeracil
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

# Gimeracil: From DPD-Inhibiting Component of S-1 to Colonic Neoplasm

## One-Sentence Summary

> Gimeracil has no standalone approved indication — it is the DPD (dihydropyrimidine dehydrogenase) inhibitor component of the S-1 combination (tegafur/gimeracil/oteracil), where it works by blocking the rapid breakdown of 5-FU rather than exerting direct cytotoxicity itself.
> The TxGNN model predicts the S-1 regimen containing gimeracil may be effective for **Colonic Neoplasm**,
> with **8 clinical trials** (including 2 completed Phase 3 RCTs) and **15 publications** currently supporting this direction.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | None independently approved — gimeracil is a pharmacokinetic enhancer within the S-1 combination (tegafur/gimeracil/oteracil), not a standalone antineoplastic agent |
| Predicted New Indication | Colonic Neoplasm |
| TxGNN Prediction Score | 99.88% |
| Evidence Level | L1 (2 completed Phase 3 RCTs) |
| Norway Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Detailed DrugBank-sourced mechanism-of-action data for gimeracil is not currently available (Data Gap). Based on known pharmacology, gimeracil is a competitive DPD inhibitor and is not cytotoxic on its own. Within the S-1 combination, it blocks DPD-mediated degradation of 5-FU (generated from tegafur), thereby prolonging and stabilizing systemic 5-FU exposure. This is a pharmacokinetic-enhancing role, not an independent antitumour mechanism.

Because 5-FU-based chemotherapy is a cornerstone of colorectal cancer treatment, and S-1 has already received regulatory approval for colorectal cancer in Japan and other Asian markets, the mechanistic rationale for extending S-1 (and by extension gimeracil as its enabling component) to colonic neoplasm is well established in oncology practice.

**Important caveat**: This "repurposing" signal actually reflects an existing combination-product use rather than a genuinely novel mechanistic extension. All supporting clinical evidence comes from the S-1 three-drug combination — none isolates gimeracil's independent contribution. Any regulatory or clinical decision should treat this as evidence for the S-1 regimen, not for gimeracil monotherapy.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00660894](https://clinicaltrials.gov/study/NCT00660894) | Phase 3 | Completed | 1535 | S-1 vs UFT+leucovorin as adjuvant therapy for Stage III colon cancer; largest completed head-to-head trial, also investigated gene-expression predictive factors |
| [NCT01918852](https://clinicaltrials.gov/study/NCT01918852) | Phase 3 | Completed | 161 | SALTO trial: S-1 vs capecitabine as first-line treatment for metastatic colorectal cancer; safety evaluation of oral fluoropyrimidines |
| [NCT03448549](https://clinicaltrials.gov/study/NCT03448549) | Phase 3 | Unknown | 1191 | SOX (S-1+oxaliplatin) vs XELOX as adjuvant chemotherapy for Stage III colorectal cancer; large sample but outcome status unreported |
| [NCT02618356](https://clinicaltrials.gov/study/NCT02618356) | Phase 2 | Unknown | 82 | Raltitrexed + S-1 in metastatic colorectal cancer after standard chemotherapy failure; primary endpoint PFS |
| [NCT00524706](https://clinicaltrials.gov/study/NCT00524706) | Phase 1/2 | Unknown | 42 | S-1 + oral leucovorin + oxaliplatin (SOL regimen) in untreated metastatic colorectal cancer |
| [NCT00974389](https://clinicaltrials.gov/study/NCT00974389) | Phase 2 | Unknown | 40 | S-1 + bevacizumab in unresectable/recurrent colorectal cancer after irinotecan/oxaliplatin failure |
| [NCT02216149](https://clinicaltrials.gov/study/NCT02216149) | Phase 2 | Terminated | 20 | Cardiac safety comparison (coronary artery blood flow) of S-1/capecitabine + oxaliplatin in metastatic GI adenocarcinoma |
| [NCT06255379](https://clinicaltrials.gov/study/NCT06255379) | Phase 2 | Not Yet Recruiting | 52 | Furquintinib + S-1 as third-line treatment for advanced metastatic colorectal cancer |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [41724114](https://pubmed.ncbi.nlm.nih.gov/41724114/) | 2026 | Real-world cohort | Eur J Cancer | Population-based study: S-1 feasible and safe after capecitabine-induced HFS/cardiotoxicity in adjuvant colon cancer treatment |
| [21875473](https://pubmed.ncbi.nlm.nih.gov/21875473/) | 2011 | Cohort | Zhonghua Zhong Liu Za Zhi | Efficacy and side effects of oxaliplatin + S-1 combination in postoperative colorectal cancer |
| [21084813](https://pubmed.ncbi.nlm.nih.gov/21084813/) | 2010 | Cohort | Gan To Kagaku Ryoho | Risk factors for grade 3–4 hematological toxicity with S-1 + irinotecan in advanced/recurrent colonic cancer (16.1% incidence) |
| [20811661](https://pubmed.ncbi.nlm.nih.gov/20811661/) | 2010 | Preclinical/xenograft | Oncology Reports | Irinotecan overcomes 5-FU resistance via thymidylate synthase downregulation in S-1-treated colon cancer xenografts |
| [18630468](https://pubmed.ncbi.nlm.nih.gov/18630468/) | 2008 | Case report | Anticancer Research | Complete response obtained and maintained with S-1 + CPT-11 in colon cancer hepatic metastases |
| [29394831](https://pubmed.ncbi.nlm.nih.gov/29394831/) | 2017 | Case report | Gan To Kagaku Ryoho | SOX (S-1+oxaliplatin) + panitumumab downstaging enabling two-stage hepatectomy for irresectable colorectal liver metastases |
| [29483452](https://pubmed.ncbi.nlm.nih.gov/29483452/) | 2018 | Case report | Gan To Kagaku Ryoho | Chemotherapy management of transverse colon cancer with liver metastasis and portal vein tumor thrombosis |
| [20841935](https://pubmed.ncbi.nlm.nih.gov/20841935/) | 2010 | PK study | Gan To Kagaku Ryoho | S-1 pharmacokinetics in a mouse peritoneal metastasis model derived from colon cancer |
| [35444144](https://pubmed.ncbi.nlm.nih.gov/35444144/) | 2022 | Case report | Gan To Kagaku Ryoho | Laparoscopic resection of peritoneal recurrence after colorectal cancer resection with S-1-containing adjuvant therapy |
| [32936722](https://pubmed.ncbi.nlm.nih.gov/32936722/) | 2021 | Case report (toxicity) | J Oncol Pharm Pract | Hypertriglyceridemia induced by S-1 during colorectal cancer treatment — novel toxicity signal |

---

## Norway Market Information

Gimeracil (as part of the S-1 combination) is currently **not marketed in Norway**; no authorization records are available (0 licenses on file).

---

## Cytotoxicity

Gimeracil itself is non-cytotoxic (a DPD inhibitor), but it is always administered as an integral component of the S-1 fluoropyrimidine chemotherapy regimen. It should therefore be managed under conventional cytotoxic chemotherapy protocols.

| Item | Content |
|------|------|
| Cytotoxicity Classification | Non-cytotoxic PK-enhancer within a conventional cytotoxic regimen (fluoropyrimidine class, S-1) |
| Myelosuppression Risk | Moderate — grade 3–4 hematological toxicity reported in ~16.1% of patients receiving S-1 + irinotecan for colonic cancer (PMID 21084813) |
| Emetogenicity Classification | Low to moderate (consistent with oral fluoropyrimidine regimens) |
| Monitoring Items | CBC with differential, liver and renal function, serum triglycerides (hypertriglyceridemia reported, PMID 32936722), skin/mucosal toxicity monitoring |
| Handling Protection | Standard cytotoxic drug handling precautions apply, as gimeracil is co-administered as part of the S-1 cytotoxic regimen |

---

## Safety Considerations

Please refer to the package insert for safety information. Drug-specific warnings, contraindications, and drug-interaction data for gimeracil are not currently available (flagged as a Blocking data gap pending TFDA label acquisition).

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Two completed Phase 3 RCTs (NCT00660894, n=1535; NCT01918852, n=161) support S-1 — the combination containing gimeracil — in colorectal/colon cancer, giving L1 evidence strength. However, all evidence pertains to the S-1 combination product, not gimeracil alone, and product-level safety labeling (warnings/contraindications) is still missing.

**To proceed, the following is needed:**
- TFDA/manufacturer product label with warnings and contraindications (Blocking gap, DG001)
- Confirmed mechanism-of-action documentation from DrugBank (High priority gap, DG002)
- Explicit clarification in any regulatory submission that efficacy evidence applies to the S-1 combination, not gimeracil monotherapy
- Norway market entry/authorization pathway assessment, since the product is not currently marketed there

*Note: Nine additional predicted indications (ranks 2–10) were reviewed but are not detailed here — all but "cardia cancer" (L4, Research Question) carry only TxGNN prediction scores with no supporting trials or literature (L5, Hold), including several biologically implausible candidates (e.g., benign lesions such as lipoma of colon, colonic lymphangioma) that should not be pursued.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

