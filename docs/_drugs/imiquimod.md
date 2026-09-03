---
layout: default
title: Imiquimod
parent: 僅模型預測 (L5)
nav_order: 179
evidence_level: L5
indication_count: 10
---

# Imiquimod
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

# Imiquimod: From an Unspecified Original Indication to Pre-malignant Neoplasm

## One-Sentence Summary

> The evidence pack does not document an approved original indication for imiquimod (no marketing licenses on file), but it is widely used off-label/investigationally as a topical immune response modifier for premalignant epithelial lesions.
> The TxGNN model predicts it may be effective for **Pre-malignant Neoplasm**,
> with **20 clinical trials** and **9 publications** currently supporting this direction.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not documented in evidence pack (no approved indication text on file; drug currently not marketed) |
| Predicted New Indication | Pre-malignant neoplasm |
| TxGNN Prediction Score | 99.92% |
| Evidence Level | L2 |
| Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Detailed, formally sourced mechanism-of-action data (DrugBank) is currently a flagged data gap (DG002). Based on the mechanistic rationale captured alongside the TxGNN prediction, imiquimod is a **Toll-like receptor 7 (TLR7) agonist**: topical application activates TLR7 signaling in epithelial and infiltrating immune cells, triggering local IFN-α and cytokine release. This recruits immune cells capable of recognizing and clearing dysplastic epithelial cells expressing abnormal (including HPV-associated) antigens.

This mechanism is not a novel hypothesis for the "pre-malignant neoplasm" category — it is already the basis for imiquimod's established/investigational use in site-specific premalignant conditions such as actinic keratosis, cervical intraepithelial neoplasia (CIN), vulvar intraepithelial neoplasia (VIN), and lentigo maligna. In effect, the TxGNN prediction largely consolidates evidence that already exists across multiple anatomical sites into the broader "pre-malignant neoplasm" category, rather than proposing an entirely new mechanistic application.

The main caveat is heterogeneity: several of the highest-relevance trials were terminated early or had very small enrollment (e.g., n=9), and a portion of the broader trial set uses imiquimod only as a vaccine adjuvant rather than as direct premalignant-lesion therapy — those adjuvant-context trials are mechanistically weaker evidence and were deprioritized below.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT02329171](https://clinicaltrials.gov/study/NCT02329171) | Phase 3 | Terminated | 9 | RCT of topical imiquimod vs. LLETZ for high-grade CIN, aiming to avoid surgical complications; terminated with very limited enrollment |
| [NCT04219358](https://clinicaltrials.gov/study/NCT04219358) | Phase 1 | Terminated | 49 | Compared 5% imiquimod, 0.05% imiquimod, and 0.05% nanoencapsulated imiquimod gel for actinic cheilitis (premalignant lip lesion) |
| [NCT03233412](https://clinicaltrials.gov/study/NCT03233412) | Phase 2 | Completed | 90 | RCT evaluating topical imiquimod efficacy in high-grade cervical intraepithelial lesions |
| [NCT01720407](https://clinicaltrials.gov/study/NCT01720407) | Phase 3 | Completed | 259 | Neoadjuvant imiquimod prior to surgery for facial lentigo maligna; aimed to reduce excision size and risk of intralesional excision |
| [NCT00941811](https://clinicaltrials.gov/study/NCT00941811) | Phase 2 | Completed | 5 | Explored immune escape mechanisms of HPV-associated lesions and imiquimod efficacy in VIN 2/3 and anogenital warts |
| [NCT00175643](https://clinicaltrials.gov/study/NCT00175643) | Phase 3 | Completed | 20 | Open-label study of imiquimod 5% cream, 3 days/week, for actinic keratoses of the head |
| [NCT01229319](https://clinicaltrials.gov/study/NCT01229319) | Phase 4 | Unknown | 20 | Imiquimod 3.75% cream after cryotherapy for hypertrophic actinic keratoses on hands/forearms |
| [NCT02242929](https://clinicaltrials.gov/study/NCT02242929) | Phase 3 | Unknown | 145 | Non-inferiority RCT: surgical excision vs. curettage + imiquimod for nodular basal cell carcinoma |
| [NCT04883645](https://clinicaltrials.gov/study/NCT04883645) | Early Phase 1 | Completed | 16 | Neoadjuvant TLR7 agonist (imiquimod) in early-stage oral squamous cell carcinoma; direct drug testing, not adjuvant use |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [23235673](https://pubmed.ncbi.nlm.nih.gov/23235673/) | 2012 | Systematic Review (Cochrane) | Cochrane Database Syst Rev | Reviews interventions, including imiquimod, for anal canal intraepithelial neoplasia (AIN), an HPV-associated premalignant condition |
| [21491403](https://pubmed.ncbi.nlm.nih.gov/21491403/) | 2011 | Systematic Review (Cochrane) | Cochrane Database Syst Rev | Reviews medical interventions for high-grade vulval intraepithelial neoplasia (VIN), including imiquimod |
| [26516853](https://pubmed.ncbi.nlm.nih.gov/26516853/) | 2015 | Review | Int J Mol Sci | Discusses combined photodynamic therapy approaches for non-melanoma skin cancer, contextualizing topical field therapies |
| [20505896](https://pubmed.ncbi.nlm.nih.gov/20505896/) | 2010 | Review | Skin Therapy Lett | Reviews current management of actinic keratoses, including topical field therapy options |
| [15584683](https://pubmed.ncbi.nlm.nih.gov/15584683/) | 2004 | Review | Semin Cutan Med Surg | Reviews topical treatment strategies (including imiquimod) for non-melanoma skin cancer and precursor lesions |
| [29500135](https://pubmed.ncbi.nlm.nih.gov/29500135/) | 2018 | Preclinical PK/PD (animal) | Urol Oncol | Compares TLR7 agonists (related class) in a rat model for intravesical use in premalignant/early bladder lesions |
| [30284955](https://pubmed.ncbi.nlm.nih.gov/30284955/) | 2019 | Case Report | Int J STD AIDS | Successful treatment of high-grade VIN with imiquimod 5% in an immunosuppressed renal transplant recipient |
| [18931984](https://pubmed.ncbi.nlm.nih.gov/18931984/) | 2008 | Imaging Case Study | Hautarzt | OCT imaging case describing multiple (pre)malignant skin lesions including actinic keratoses resistant to topical treatment |
| [15601490](https://pubmed.ncbi.nlm.nih.gov/15601490/) | 2004 | Case Report | Int J STD AIDS | Successful clearance of Bowenoid papulosis (premalignant anogenital condition) with topical imiquimod 5% cream |

---

## Norway Market Information

No marketing authorization records are available in the evidence pack. Imiquimod currently has **0 registered licenses** in this jurisdiction (market status: Not Marketed).

---

## Safety Considerations

Please refer to the package insert for safety information. Formal warnings, contraindications, and drug-drug interaction data are not yet available in this evidence pack (flagged as a **Blocking** data gap — DG001: regulatory label warnings/contraindications not yet retrieved from the source authority).

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The TxGNN score is very high (99.92%) and is corroborated by multiple completed Phase 2/3 trials and Cochrane systematic reviews across related premalignant conditions (CIN, VIN, AIN, actinic keratosis, lentigo maligna), supporting evidence level L2. However, enrollment sizes in the most directly relevant trials are small and several were terminated early, so guardrails are warranted before advancing further.

**To proceed, the following is needed:**
- Retrieve TFDA/regulatory label warnings and contraindications (DG001, blocking)
- Obtain a formal DrugBank-sourced mechanism of action summary (DG002)
- Confirm drug-drug interaction profile (currently not found)
- Clarify current marketing/licensing status in this jurisdiction, since no authorizations are on file
- Seek trials or literature specifically using the umbrella term "pre-malignant neoplasm" rather than only site-specific proxies, to directly validate the TxGNN-predicted category
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

