---
layout: default
title: Docetaxel
parent: 僅模型預測 (L5)
nav_order: 39
evidence_level: L5
indication_count: 10
---

# Docetaxel
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

Using the evidence pack's rank-1 predicted indication (female breast carcinoma) as the primary candidate, per the extraction rules. Note: I flag an important data-quality issue that the evidence pack itself surfaces — this "predicted" indication may actually be an already-established use of docetaxel rather than a genuinely novel repurposing signal — and address it transparently in the relevant sections rather than silently following the template.

---

# Docetaxel: From Solid Tumour Chemotherapy to Female Breast Carcinoma

## One-Sentence Summary

> Docetaxel is a taxane chemotherapeutic agent used broadly across solid tumours; local (Norway) registry data on its original approved indication and product labelling is currently unavailable because the product is not marketed there.
> The TxGNN model predicts it may be effective for **Female Breast Carcinoma**, with **68 clinical trials** and **20 publications** currently associated with this candidate.
> **Important caveat:** the evidence itself indicates this is very likely an already-established, globally approved use of docetaxel rather than a truly novel repurposing opportunity — the data gap reflects a local registration/documentation gap, not a genuine evidence gap.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available in local (Norway) registry — product is not currently marketed and no license records exist. (Docetaxel is a globally established taxane chemotherapeutic used across multiple solid tumours.) |
| Predicted New Indication | Female Breast Carcinoma |
| TxGNN Prediction Score | 99.90% |
| Evidence Level | L1 |
| Norway Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Proceed with Guardrails |

## Why is This Prediction Reasonable?

Currently, detailed mechanism-of-action data is not available in the local registry for this product. Based on known pharmacology, docetaxel is a taxane microtubule-stabilizing agent: it binds and stabilizes β-tubulin, blocking microtubule depolymerization, which drives G2/M mitotic arrest and apoptosis in rapidly dividing cells. This mechanism is particularly potent against highly proliferative tumours such as breast cancer.

Breast carcinoma is, in fact, one of docetaxel's longest-established and most extensively validated indications worldwide — it has been used in adjuvant, neoadjuvant, and metastatic breast cancer regimens for over two decades, supported by numerous Phase 3 randomized trials (see below). The predicted "new indication" relationship here should therefore be read carefully: the model has surfaced an indication that is mechanistically sound and clinically proven, but the strength of that support comes from decades of pre-existing global evidence rather than a genuinely novel repurposing signal.

Practically, this means the "repurposing" framing is weaker than it appears at first glance. The local data gaps flagged in this evidence pack (missing package insert, missing MOA record) most likely reflect that docetaxel simply has not yet been registered/marketed in this specific jurisdiction (Norway) — not that breast cancer is an unproven or experimental use of the drug elsewhere.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00193011](https://clinicaltrials.gov/study/NCT00193011) | Phase 3 | Completed | 150 | Randomized multicenter trial comparing weekly docetaxel vs. CMF in adjuvant treatment of high-risk breast cancer patients ≥65 years or unfit for anthracyclines — highest-relevance direct evidence (Grade A) |
| [NCT00002707](https://clinicaltrials.gov/study/NCT00002707) | Phase 3 | Completed | 2,411 | Preoperative AC vs. AC followed by docetaxel (pre- or post-operative) in operable stage II/III breast cancer |
| [NCT01275677](https://clinicaltrials.gov/study/NCT01275677) | Phase 3 | Completed | 3,270 | Adjuvant chemotherapy (docetaxel+cyclophosphamide, or AC→paclitaxel) alone vs. plus trastuzumab in node-positive/high-risk HER2-low invasive breast cancer |
| [NCT00089479](https://clinicaltrials.gov/study/NCT00089479) | Phase 3 | Completed | 2,611 | AC followed by Taxotere alone vs. Taxotere+Xeloda on overall survival in high-risk breast cancer |
| [NCT01354522](https://clinicaltrials.gov/study/NCT01354522) | Phase 3 | Completed | 204 | TAC (docetaxel/doxorubicin/cyclophosphamide) vs. TCX (docetaxel/cyclophosphamide/capecitabine) as adjuvant treatment for high-risk HER2-negative breast cancer |
| [NCT02003209](https://clinicaltrials.gov/study/NCT02003209) | Phase 3 | Completed | 315 | Neoadjuvant TCHP (docetaxel/carboplatin/trastuzumab/pertuzumab) with vs. without estrogen deprivation in HR+/HER2+ breast cancer |
| [NCT00431080](https://clinicaltrials.gov/study/NCT00431080) | Phase 3 | Completed | 478 | Dose-dense G-CSF-supported FE75C followed by docetaxel vs. paclitaxel as adjuvant therapy in axillary node-positive breast cancer |
| [NCT02748213](https://clinicaltrials.gov/study/NCT02748213) | Phase 2 | Completed | 225 | Trastuzumab + docetaxel ± capecitabine in HER2-overexpressing advanced/metastatic breast cancer |
| [NCT04066335](https://clinicaltrials.gov/study/NCT04066335) | N/A | Unknown | 1,498 | Large real-world observational safety study of Nanoxel M (docetaxel-PM formulation) injection |
| [NCT00003565](https://clinicaltrials.gov/study/NCT00003565) | Phase 2 | Completed | 109 | Population pharmacokinetics of docetaxel (Taxotere) in Caucasian and African-American cancer patients |

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [28398846](https://pubmed.ncbi.nlm.nih.gov/28398846/) | 2017 | RCT | J Clin Oncol | ABC Trials: docetaxel/cyclophosphamide (TC) vs. anthracycline-taxane regimens in early breast cancer adjuvant therapy |
| [27997437](https://pubmed.ncbi.nlm.nih.gov/27997437/) | 2017 | Cohort | Anti-Cancer Drugs | Association between adjuvant docetaxel-based chemotherapy and breast cancer-related lymphedema |
| [9364543](https://pubmed.ncbi.nlm.nih.gov/9364543/) | 1997 | Clinical trial report | Oncology (Williston Park) | Combination docetaxel/vinorelbine activity in metastatic breast cancer and NSCLC |
| [19856651](https://pubmed.ncbi.nlm.nih.gov/19856651/) | 2009 | Phase 1/2 dose-finding | Tumori | Docetaxel and gemcitabine dose-finding study in metastatic breast carcinoma |
| [12599222](https://pubmed.ncbi.nlm.nih.gov/12599222/) | 2003 | Clinical trial report | Cancer | Capecitabine + docetaxel + epirubicin (TEX) as first-line therapy in advanced breast carcinoma |
| [15161988](https://pubmed.ncbi.nlm.nih.gov/15161988/) | 2004 | Review | The Oncologist | Docetaxel and paclitaxel in breast cancer treatment: review of clinical experience |
| [7595719](https://pubmed.ncbi.nlm.nih.gov/7595719/) | 1995 | Review | J Clin Oncol | Foundational review of docetaxel's preclinical and clinical profile |
| [9282422](https://pubmed.ncbi.nlm.nih.gov/9282422/) | 1997 | Review | Drug Ther Bull | Paclitaxel and docetaxel in breast and ovarian cancer |
| [25073898](https://pubmed.ncbi.nlm.nih.gov/25073898/) | 2014 | Case report | World J Surg Oncol | Breast carcinoma with choriocarcinomatous features — rare variant case report |
| [15138562](https://pubmed.ncbi.nlm.nih.gov/15138562/) | 2004 | Preclinical/mechanistic | Oncol Rep | Gamma-linolenic acid enhances docetaxel cytotoxicity in breast carcinoma cells |

## Norway Market Information

Docetaxel is currently **not marketed in Norway** in this dataset — there are no marketing authorizations on record (0 licenses), so no product/authorization table can be produced at this time.

## Cytotoxicity

Docetaxel is a conventional cytotoxic antineoplastic agent (taxane class), so this section applies.

| Item | Content |
|------|------|
| Cytotoxicity Classification | Conventional cytotoxic — taxane (microtubule-stabilizing agent) |
| Myelosuppression Risk | High — neutropenia, including febrile neutropenia, is the characteristic dose-limiting toxicity of docetaxel across virtually all approved regimens |
| Emetogenicity Classification | Low to Moderate (typical of the taxane class) |
| Monitoring Items | Complete blood count with differential (neutrophils especially), liver function tests (docetaxel is hepatically metabolized via CYP3A4), and monitoring for fluid retention/peripheral edema |
| Handling Protection | Yes — standard cytotoxic/hazardous drug handling precautions apply (personal protective equipment, closed-system transfer devices where available) |

*Note: Local (Norway) product-specific toxicity data is not currently available. Please refer to the official package insert for detailed warnings and precautions once the product is registered.*

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
- Evidence level is L1, supported by multiple completed Phase 3 RCTs directly evaluating docetaxel in breast cancer. However, this strength largely reflects docetaxel's long-standing, globally established role in breast cancer treatment rather than a genuinely new repurposing discovery — the local data gaps (missing MOA, missing package insert, 0 Norway licenses) appear to be registration/documentation gaps rather than clinical evidence gaps.

**To proceed, the following is needed:**
- Confirm whether docetaxel already holds (or is seeking) a breast cancer marketing authorization in Norway, to clarify whether this candidate should be classified as "repurposing" at all versus a standard registration/market-access case
- Obtain the official package insert / TFDA-equivalent safety documentation (warnings, contraindications, DDI) to close the Blocking data gap (DG001)
- Obtain confirmed DrugBank/regulatory MOA data to close the High-severity data gap (DG002)
- If a genuinely novel repurposing signal is the goal, consider prioritizing rank 2 (Ewing sarcoma) or rank 8 (rhabdomyosarcoma) from this same evidence pack — both carry L2 evidence from real, non-standard-of-care trials (e.g., GEMDOX regimen, JCOG1802) and represent more credible off-label repurposing candidates than breast cancer does
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

