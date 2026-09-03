---
layout: default
title: Oteracil
parent: 僅模型預測 (L5)
nav_order: 257
evidence_level: L5
indication_count: 10
---

# Oteracil
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

# Oteracil: From Chemotherapy Toxicity Modulator to Colonic Neoplasm

## One-Sentence Summary

Oteracil (potassium oxonate) is a fixed component of the oral combination product S-1 (tegafur/gimeracil/oteracil), where it works by inhibiting intestinal OPRT to reduce gastrointestinal toxicity from tegafur-derived 5-FU rather than acting as an independent anticancer agent. The TxGNN model predicts potential efficacy for **Colonic Neoplasm**, supported by **8 clinical trials** (including 3 completed Phase 3 RCTs) and **20 publications**. Importantly, this evidence applies to the S-1 combination as a whole — oteracil itself has no standalone antitumor activity.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available — no Norway marketing authorization on record for oteracil monotherapy; per literature, it is used exclusively as a fixed component of the S-1 combination for gastrointestinal cancers |
| Predicted New Indication | Colonic Neoplasm |
| TxGNN Prediction Score | 99.99% |
| Evidence Level | L1 |
| Norway Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Detailed standalone mechanism-of-action data for oteracil is not available (`original_moa: [Data Gap]`), but the evidence pack's repurposing rationale provides substantial mechanistic context. Oteracil (potassium oxonate) has **no independent antitumor activity**. Its pharmacological role is to inhibit orotate phosphoribosyltransferase (OPRT) in the intestinal mucosa, which reduces local activation of 5-FU and thereby lowers the gastrointestinal toxicity caused by tegafur (a 5-FU prodrug). It is one of three fixed components of S-1 (tegafur/gimeracil/oteracil, brand name TS-1).

S-1 has already been approved and widely used in Japan and other Asian countries for colorectal cancer, both as adjuvant therapy for resected Stage III colon/rectal cancer and as first-line/later-line treatment for metastatic colorectal cancer. Since gastric and colorectal cancers are both fluoropyrimidine-sensitive gastrointestinal malignancies, and S-1 is a validated fluoropyrimidine-based regimen across this tumor family, the TxGNN prediction of colonic neoplasm is mechanistically plausible.

**Key caveat**: because oteracil is never administered as monotherapy, all clinical and mechanistic support for this indication is evidence for the S-1 combination product, not for oteracil in isolation. Any repurposing decision needs to be made at the combination-product level, and this distinction should be treated as a structural limitation of the evidence rather than a gap that can be closed with more oteracil-specific data.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00660894](https://clinicaltrials.gov/study/NCT00660894) | Phase 3 | Completed | 1,535 | UFT+LV vs TS-1 as adjuvant therapy for Stage III colon cancer; direct head-to-head Phase 3 RCT for this indication (Grade A) |
| [NCT01918852](https://clinicaltrials.gov/study/NCT01918852) | Phase 3 | Completed | 161 | SALTO trial — S-1 vs capecitabine first-line for metastatic colorectal cancer, comparable efficacy (Grade A) |
| [NCT03448549](https://clinicaltrials.gov/study/NCT03448549) | Phase 3 | Unknown | 1,191 | SOX vs XELOX as adjuvant chemotherapy for Stage III colorectal cancer; well-designed RCT, results status unclear (Grade B) |
| [NCT02618356](https://clinicaltrials.gov/study/NCT02618356) | Phase 2 | Unknown | 82 | Raltitrexed + S-1 in metastatic CRC after failure of standard chemotherapy (Grade B) |
| [NCT00524706](https://clinicaltrials.gov/study/NCT00524706) | Phase 1/2 | Unknown | 42 | S-1 + oral leucovorin + oxaliplatin (SOL) in untreated metastatic colorectal cancer (Grade B) |
| [NCT00974389](https://clinicaltrials.gov/study/NCT00974389) | Phase 2 | Unknown | 40 | S-1 + bevacizumab in unresectable/recurrent CRC after irinotecan/oxaliplatin failure (Grade B) |
| [NCT02216149](https://clinicaltrials.gov/study/NCT02216149) | Phase 2 | Terminated | 20 | S-1/capecitabine + oxaliplatin, coronary blood-flow safety endpoint (cardiotoxicity focus, not efficacy) (Grade C) |
| [NCT06255379](https://clinicaltrials.gov/study/NCT06255379) | Phase 2 | Not yet recruiting | 52 | Fuquinitinib + S-1 (tegafur/gimeracil/oteracil) as third-line therapy in advanced metastatic CRC (Grade C) |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [31917122](https://pubmed.ncbi.nlm.nih.gov/31917122/) | 2020 | RCT | Clin Colorectal Cancer | ACTS-CC 02: SOX (S-1+oxaliplatin) vs UFT/LV as adjuvant therapy in high-risk Stage III colon cancer |
| [27056996](https://pubmed.ncbi.nlm.nih.gov/27056996/) | 2016 | RCT | Annals of Oncology | JFMC35-C1 (ACTS-RC): S-1 vs UFT as adjuvant chemotherapy for Stage II/III rectal cancer |
| [24942277](https://pubmed.ncbi.nlm.nih.gov/24942277/) | 2014 | RCT | Annals of Oncology | ACTS-CC trial: S-1 non-inferior to UFT/LV as adjuvant therapy for Stage III colon cancer |
| [25209093](https://pubmed.ncbi.nlm.nih.gov/25209093/) | 2014 | Review/Guideline | Clin Colorectal Cancer | Asian consensus guidelines for metastatic colorectal cancer management |
| [17496461](https://pubmed.ncbi.nlm.nih.gov/17496461/) | 2007 | Review | Gan To Kagaku Ryoho | Overview of adjuvant chemotherapy for colorectal cancer in Japan |
| [22415232](https://pubmed.ncbi.nlm.nih.gov/22415232/) | 2012 | Clinical study (safety analysis) | Br J Cancer | ACTS-CC trial planned safety analysis of UFT/LV vs S-1 as Stage III colon cancer adjuvant therapy |
| [32189156](https://pubmed.ncbi.nlm.nih.gov/32189156/) | 2020 | Clinical study | Int J Clin Oncol | KSCC1303: C-SOX (S-1+oxaliplatin) adjuvant therapy for Stage III colon cancer, 3-year DFS final analysis |
| [26036466](https://pubmed.ncbi.nlm.nih.gov/26036466/) | 2015 | RCT (Phase 2) | BMC Cancer | Randomized study of S-1 dosing schedule for resected colorectal cancer |
| [21875473](https://pubmed.ncbi.nlm.nih.gov/21875473/) | 2011 | Clinical study | Chin J Oncology | Efficacy and side effects of oxaliplatin + S-1 in colorectal cancer |
| [20500514](https://pubmed.ncbi.nlm.nih.gov/20500514/) | 2010 | Preclinical | Cancer Science | Anti-lymph-node-metastasis efficacy comparison of S-1 vs UFT/LV in a colonic cancer xenograft model |

---

## Norway Market Information

Oteracil currently has **no marketing authorization in Norway** (`total_licenses: 0`), and no S-1 combination product license records are present in this evidence pack. No authorization table can be generated at this time.

---

## Cytotoxicity

**This section applies because oteracil is a fixed component of the cytotoxic S-1 fluoropyrimidine combination**, though oteracil itself is not independently cytotoxic.

| Item | Content |
|------|------|
| Cytotoxicity Classification | Not independently cytotoxic — functions as a biochemical modulator (intestinal OPRT inhibitor) within the S-1 fluoropyrimidine combination (tegafur/gimeracil/oteracil); the cytotoxic activity of S-1 derives from tegafur (5-FU prodrug) |
| Myelosuppression Risk | Moderate — attributable to the tegafur/5-FU component of S-1; oteracil itself does not cause myelosuppression and is included specifically to reduce GI toxicity of the combination |
| Emetogenicity Classification | Low to moderate (typical of oral fluoropyrimidine regimens) |
| Monitoring Items | CBC with differential, liver and renal function, electrolytes — per standard S-1 combination monitoring protocols |
| Handling Protection | If pursued via the S-1 combination product, standard cytotoxic drug handling precautions apply; oteracil alone has not been evaluated as a standalone hazardous handling concern |

---

## Safety Considerations

Please refer to the package insert for safety information. No key warnings, contraindications, or drug-drug interaction data are currently available for oteracil in this evidence pack (`DG001`, marked as a blocking data gap for safety pre-screening).

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Multiple completed Phase 3 RCTs (ACTS-CC, ACTS-RC, SALTO) demonstrate that the S-1 combination — of which oteracil is a fixed component — is effective in both adjuvant and metastatic colorectal/colon cancer settings, and S-1 already holds regulatory approval for this indication in Japan and other Asian markets. However, since oteracil has no independent antitumor activity and is never used as monotherapy, this recommendation should be understood as applying to the **S-1 combination product**, not to oteracil as a standalone repurposing candidate.

**To proceed, the following is needed:**
- TFDA/Norway package insert safety data for oteracil and/or the S-1 combination (DG001, blocking)
- Confirmed mechanism-of-action documentation from DrugBank or equivalent source (DG002)
- Clarification of regulatory pathway: repurposing should target the S-1 combination product (tegafur/gimeracil/oteracil) rather than oteracil alone, given its non-independent pharmacological role
- Verification of Norway/EU marketing authorization status for the S-1 combination product, since oteracil itself currently has zero registered licenses
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

