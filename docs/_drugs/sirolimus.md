---
layout: default
title: Sirolimus
parent: 僅模型預測 (L5)
nav_order: 327
evidence_level: L5
indication_count: 10
---

# Sirolimus
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

# Sirolimus: From Renal Transplant Rejection Prophylaxis to Liposarcoma

## One-Sentence Summary

Sirolimus (rapamycin) is an mTOR inhibitor originally developed to prevent organ rejection after renal transplantation. The TxGNN model predicts it may be effective for **Liposarcoma**, with **5 clinical trials** and **12 publications** currently supporting this direction — though most of the strongest trial data comes from sirolimus analogs (temsirolimus, everolimus, ridaforolimus) rather than sirolimus itself.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Prophylaxis of renal transplant rejection (immunosuppressant) — not captured in Norway regulatory data, inferred from the drug's established clinical use and supporting literature in this evidence pack |
| Predicted New Indication | Liposarcoma |
| TxGNN Prediction Score | 99.89% |
| Evidence Level | L2 |
| Norway Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in DrugBank for this candidate. Based on the supporting literature in this evidence pack, Sirolimus is a mammalian target of rapamycin (mTOR) inhibitor — it binds FKBP12 and blocks mTORC1 signaling, which regulates cell growth, proliferation, and survival. Its efficacy in preventing renal transplant rejection is well established, and several of the included publications (e.g., studies on renal transplant recipients, PMID 16434506, 26093731) note that sirolimus-based immunosuppression is associated with a *reduced* incidence of malignancy compared with calcineurin inhibitors, pointing toward antiproliferative activity beyond immune suppression.

Liposarcoma, particularly the dedifferentiated subtype, has been shown to exhibit aberrant activation of the Akt-mTOR and MAPK pathways (PMID 26518767), providing a direct mechanistic rationale for mTOR blockade as an antitumor strategy. This is mechanistically distinct from sirolimus's original transplant indication but converges on the same molecular pathway (mTORC1 inhibition), which is the core biological link supporting this repurposing hypothesis.

Importantly, the bulk of clinical evidence in liposarcoma comes from sirolimus *analogs* (temsirolimus, everolimus, ridaforolimus) rather than sirolimus itself. Only one trial (NCT02821507) directly tests sirolimus in this population, and it was a single-arm Phase 2 study rather than a randomized controlled trial. This class-level extrapolation strengthens the biological plausibility but leaves a gap in drug-specific efficacy and safety evidence.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT02821507](https://clinicaltrials.gov/study/NCT02821507) | Phase 2 | Completed | 70 | Single-arm trial of sirolimus + cyclophosphamide in metastatic/unresectable myxoid liposarcoma and chondrosarcoma; direct use of sirolimus |
| [NCT00949325](https://clinicaltrials.gov/study/NCT00949325) | Phase 1/2 | Completed | 24 | Torisel (temsirolimus, sirolimus analog) + liposomal doxorubicin in advanced soft tissue and bone sarcomas |
| [NCT01614795](https://clinicaltrials.gov/study/NCT01614795) | Phase 2 | Completed | 46 | Cixutumumab + temsirolimus in pediatric recurrent/refractory sarcoma |
| [NCT00093080](https://clinicaltrials.gov/study/NCT00093080) | Phase 2 | Completed | 216 | Ridaforolimus (mTOR inhibitor analog) in advanced sarcoma; largest trial in this indication but not sirolimus itself |
| [NCT03114527](https://clinicaltrials.gov/study/NCT03114527) | Phase 2 | Active, not recruiting | 48 | Ribociclib + everolimus in advanced dedifferentiated liposarcoma and leiomyosarcoma |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [37967116](https://pubmed.ncbi.nlm.nih.gov/37967116/) | 2024 | RCT (Phase 2) | Clin Cancer Res | Ribociclib + everolimus showed synergistic growth inhibition in dedifferentiated liposarcoma and leiomyosarcoma models, supporting mTOR-pathway targeting |
| [16434506](https://pubmed.ncbi.nlm.nih.gov/16434506/) | 2006 | Cohort (transplant population) | J Am Soc Nephrol | Sirolimus after cyclosporine withdrawal reduced cancer risk in renal transplant recipients, suggesting antitumor activity of sirolimus beyond immunosuppression |
| [39796641](https://pubmed.ncbi.nlm.nih.gov/39796641/) | 2024 | Review | Cancers | Overview of novel therapeutics in soft tissue sarcoma, including mTOR-pathway-targeted agents |
| [37400145](https://pubmed.ncbi.nlm.nih.gov/37400145/) | 2023 | Preclinical | Cancer Genomics Proteomics | Combination of chloroquine and rapamycin (sirolimus) synergistically inhibited autophagy and was effective against well-differentiated liposarcoma models |
| [26518767](https://pubmed.ncbi.nlm.nih.gov/26518767/) | 2016 | Mechanism study | Tumour Biol | Demonstrated activation of the Akt-mTOR and MAPK pathways in dedifferentiated liposarcoma specimens, providing the mechanistic basis for mTOR inhibition |
| [37222206](https://pubmed.ncbi.nlm.nih.gov/37222206/) | 2023 | Review | Curr Opin Oncol | Summary of recent clinical trials on molecular-targeted agents, including mTOR inhibitors, in advanced sarcomas |
| [26093731](https://pubmed.ncbi.nlm.nih.gov/26093731/) | 2015 | Cohort (transplant population) | Transplant Proc | Evaluated effects of immunosuppressive drugs, including sirolimus, on malignancy development in long-term transplant patients |
| [36309387](https://pubmed.ncbi.nlm.nih.gov/36309387/) | 2022 | Preclinical (PDOX model) | In Vivo | Chloroquine combined with rapamycin arrested tumor growth in a patient-derived orthotopic xenograft model of dedifferentiated liposarcoma |
| [25519700](https://pubmed.ncbi.nlm.nih.gov/25519700/) | 2015 | Preclinical | Mol Cancer Ther | Described dysregulation of the PI3K/Akt/mTOR pathway across multiple sarcoma subtypes and limitations of first-generation rapalogues |
| [20497911](https://pubmed.ncbi.nlm.nih.gov/20497911/) | 2010 | Review | Bull Cancer | Discussed targeted treatment approaches, including mTOR-pathway inhibition, for rare connective tissue tumors and sarcomas |

---

## Norway Market Information

Sirolimus currently holds **no market authorizations in Norway** (total licenses: 0). No product-level dosage form or approved indication data is available for this drug in the Norwegian regulatory dataset.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
While the mechanistic rationale (mTOR pathway activation in liposarcoma) is biologically plausible and supported by class-level evidence (L2), sirolimus itself has only one completed single-arm Phase 2 trial in this indication, most efficacy data comes from analog compounds, and the drug is not currently marketed in Norway. Critically, TFDA/Norway package insert data (warnings, contraindications) are entirely unavailable, which blocks even a preliminary safety assessment.

**To proceed, the following is needed:**
- TFDA/Norwegian package insert data (warnings, contraindications, DDI) to complete a baseline safety review
- DrugBank-confirmed mechanism of action data for sirolimus
- A sirolimus-specific (not analog) randomized controlled trial in liposarcoma to upgrade evidence level beyond single-arm Phase 2
- Route of administration and formulation compatibility assessment for an oncology treatment setting
- Consideration of related higher-confidence candidates in this same evidence pack (e.g., lung PEComa, rank 9, "Proceed with Guardrails") which may warrant parallel evaluation given stronger direct sirolimus trial support (MIDAS, RESULT, MILES trials)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

