---
layout: default
title: Pazopanib
parent: 僅模型預測 (L5)
nav_order: 267
evidence_level: L5
indication_count: 10
---

# Pazopanib
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

# Pazopanib: From Non-Adipocytic Soft Tissue Sarcoma to Liposarcoma

## One-Sentence Summary

> Pazopanib is a multi-target tyrosine kinase inhibitor with established efficacy in clear-cell renal cell carcinoma and non-adipocytic soft tissue sarcoma.
> The TxGNN model predicts it may also be effective for **Liposarcoma**, a soft-tissue sarcoma subtype currently outside its labeled use,
> with **9 clinical trials** and **20 publications** currently supporting this direction, including two dedicated completed Phase 2 studies.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Clear-cell renal cell carcinoma; non-adipocytic soft tissue sarcoma (derived from literature context — no formal regulatory record available) |
| Predicted New Indication | Liposarcoma |
| TxGNN Prediction Score | 99.59% |
| Evidence Level | L2 |
| Norway Market Status | Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data for pazopanib is not available from the primary sources queried (DrugBank query returned a data gap). Based on information embedded in the clinical trial and literature evidence, pazopanib is a multi-target tyrosine kinase inhibitor (VEGFR, PDGFR-α/β, c-KIT) with anti-angiogenic and antitumorigenic properties. Its efficacy in clear-cell renal cell carcinoma and non-adipocytic advanced/metastatic soft tissue sarcoma is well established — it is already approved for these uses and cited repeatedly across the literature as "a standard first-line treatment" in these settings.

Liposarcoma is a soft tissue sarcoma subtype that was historically excluded from pazopanib's approved label (the pivotal PALETTE trial excluded adipocytic sarcomas), but it shares the same mesenchymal lineage and overlapping molecular drivers as non-adipocytic STS. PDGFR-α/β signaling is implicated in liposarcoma proliferation, particularly in the dedifferentiated subtype, and VEGFR-driven angiogenesis supports tumor growth across STS subtypes generally. This provides a plausible mechanistic bridge from the approved indication to the predicted one.

Supporting this rationale, two dedicated Phase 2 trials (NCT01506596, NCT01692496) specifically enrolled unresectable/metastatic liposarcoma patients to test single-agent pazopanib, and their results were published in peer-reviewed literature (PMID 28832986, Cancer 2017). Preclinical xenograft data (PMID 25500074) further demonstrate pazopanib-mediated tumor regression through anti-angiogenic action in dedifferentiated liposarcoma models, reinforcing the biological plausibility of the prediction.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT01506596](https://clinicaltrials.gov/study/NCT01506596) | Phase 2 | Completed | 42 | Single-agent pazopanib efficacy and safety in unresectable or metastatic liposarcoma |
| [NCT01532687](https://clinicaltrials.gov/study/NCT01532687) | Phase 2 | Completed | 54 | Gemcitabine ± pazopanib in refractory soft tissue sarcoma, including a liposarcoma subgroup |
| [NCT02180867](https://clinicaltrials.gov/study/NCT02180867) | Phase 2/3 | Active, not recruiting | 140 | Preoperative chemoradiation ± pazopanib in non-rhabdomyosarcoma STS (includes liposarcoma subtype) |
| [NCT06239272](https://clinicaltrials.gov/study/NCT06239272) | Phase 1/2 | Recruiting | 139 | Maintenance pazopanib with dose-escalated radiation and selinexor in non-rhabdomyosarcoma STS |
| [NCT02357810](https://clinicaltrials.gov/study/NCT02357810) | Phase 2 | Completed | 178 | Pazopanib + oral topotecan in metastatic/non-resectable soft tissue and bone sarcomas |
| [NCT06263231](https://clinicaltrials.gov/study/NCT06263231) | Phase 3 | Active, not recruiting | 333 | INT230-6 vs. US standard of care in liposarcoma/UPS/leiomyosarcoma (pazopanib not the study drug) |
| [NCT01692496](https://clinicaltrials.gov/study/NCT01692496) | Phase 2 | Completed | 52 | Pazopanib activity/tolerability in advanced/metastatic liposarcoma relapsed after standard therapy |
| [NCT01900743](https://clinicaltrials.gov/study/NCT01900743) | Phase 2 | Completed | 219 | Regorafenib vs. placebo in metastatic STS after anthracycline failure (liposarcoma cohort; pazopanib not the study drug) |
| [NCT02048371](https://clinicaltrials.gov/study/NCT02048371) | Phase 2 | Completed | 131 | SARC024: oral regorafenib across selected sarcoma subtypes, referencing prior pazopanib activity in STS |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [34050255](https://pubmed.ncbi.nlm.nih.gov/34050255/) | 2021 | RCT | British Journal of Cancer | Pazopanib is active in refractory STS and significantly prolongs progression-free survival; combination with topotecan studied |
| [31010343](https://pubmed.ncbi.nlm.nih.gov/31010343/) | 2019 | Cohort (Phase 2 subgroup) | Expert Opinion on Investigational Drugs | Reviews pazopanib's anti-angiogenic/antitumorigenic activity specifically in liposarcoma, a subtype lacking effective treatment options |
| [33355646](https://pubmed.ncbi.nlm.nih.gov/33355646/) | 2021 | Cohort | JAMA Oncology | PAPAGEMO trial final results: pazopanib ± gemcitabine in anthracycline/ifosfamide-refractory STS |
| [28832986](https://pubmed.ncbi.nlm.nih.gov/28832986/) | 2017 | Phase 2 study | Cancer | Prospective single-arm Phase 2 study determining treatment activity and safety of single-agent pazopanib in unresectable/metastatic liposarcoma |
| [28844815](https://pubmed.ncbi.nlm.nih.gov/28844815/) | 2017 | Review | The Lancet Oncology | Commentary on pazopanib's role for advanced liposarcoma |
| [35609512](https://pubmed.ncbi.nlm.nih.gov/35609512/) | 2022 | Review | Oncology Research and Treatment | Established and experimental systemic treatment options across liposarcoma subtypes |
| [32026050](https://pubmed.ncbi.nlm.nih.gov/32026050/) | 2020 | Review | Current Treatment Options in Oncology | Systemic therapy options for dedifferentiated liposarcoma |
| [37298520](https://pubmed.ncbi.nlm.nih.gov/37298520/) | 2023 | Review | International Journal of Molecular Sciences | Treatment landscape for dedifferentiated liposarcoma in the immunotherapy era |
| [25500074](https://pubmed.ncbi.nlm.nih.gov/25500074/) | 2014 | Preclinical | Translational Oncology | Pazopanib suppresses tumor growth via anti-angiogenesis in dedifferentiated liposarcoma xenograft models |
| [30060824](https://pubmed.ncbi.nlm.nih.gov/30060824/) | 2018 | Case report | Tissue & Cell | PDGFRA-amplified pleomorphic liposarcoma PDOX model regressed by pazopanib after doxorubicin resistance |

---

## Norway Market Information

Pazopanib is currently **not marketed** in Norway; no authorization or license records are available in the evidence pack (`total_licenses: 0`).

---

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy — multi-target tyrosine kinase inhibitor (VEGFR/PDGFR/c-KIT) with anti-angiogenic activity (per literature context in evidence pack) |
| Myelosuppression Risk | Not available in current evidence pack — please refer to the package insert warnings and precautions |
| Emetogenicity Classification | Not available in current evidence pack — please refer to the package insert warnings and precautions |
| Monitoring Items | Not available in current evidence pack — please refer to the package insert warnings and precautions |
| Handling Protection | Not available in current evidence pack — please refer to the package insert warnings and precautions |

---

## Safety Considerations

Please refer to the package insert for safety information. (Key warnings, contraindications, and drug interaction data were flagged as data gaps in this evidence pack — TFDA label parsing is required to close this gap.)

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Two dedicated completed Phase 2 trials (NCT01506596, NCT01692496) and their published results (PMID 28832986) directly support single-agent pazopanib activity in unresectable/metastatic liposarcoma, reinforced by preclinical mechanistic data and multiple supportive reviews — meeting the L2 evidence bar, but falling short of confirmatory Phase 3 data.

**To proceed, the following is needed:**
- TFDA/Norwegian label data (warnings, contraindications, DDI) — currently a **blocking** data gap for safety pre-screening
- Formal DrugBank MOA confirmation to substantiate the PDGFR/VEGFR mechanistic rationale
- A confirmatory randomized trial in liposarcoma (current evidence is single-arm Phase 2 only)
- Norway/EU market authorization pathway assessment, as the drug is not currently marketed in this jurisdiction

*Note: This TxGNN screen also flagged dermatofibrosarcoma protuberans (rank 10, evidence level L2, "Proceed with Guardrails") as a second candidate with comparable evidence strength (a dedicated Phase 2 trial and a multicenter Phase 2 publication), driven by the same PDGFR-targeting mechanism. This may warrant a separate evaluation.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

