---
layout: default
title: Atezolizumab
parent: 僅模型預測 (L5)
nav_order: 38
evidence_level: L5
indication_count: 10
---

# Atezolizumab
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

# Atezolizumab: From Urothelial Carcinoma to Prostatic Urethra Urothelial Carcinoma

## One-Sentence Summary

Atezolizumab is a PD-L1 immune checkpoint inhibitor globally approved for urothelial (bladder) carcinoma, NSCLC, and other solid tumours.
The TxGNN model predicts it may be effective for **Prostatic Urethra Urothelial Carcinoma**,
with **2 clinical trials** currently supporting this direction, though no dedicated literature is yet available.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the Norway registry (product not marketed); globally approved for urothelial carcinoma, NSCLC and other solid tumours as PD-L1 immunotherapy |
| Predicted New Indication | Prostatic Urethra Urothelial Carcinoma |
| TxGNN Prediction Score | 99.98% |
| Evidence Level | L2 |
| Norway Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Proceed with Guardrails |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, atezolizumab is a PD-L1 immune checkpoint inhibitor; its efficacy in urothelial carcinoma (bladder cancer) has been proven, and mechanistically it may be applicable to prostatic urethra urothelial carcinoma.

Prostatic urethral urothelial carcinoma belongs to the same histological family as bladder urothelial carcinoma — both are urothelial-lineage cancers that share PD-L1 expression biology. Regulatory labels for atezolizumab in urothelial carcinoma typically do not restrict by anatomical site of origin, meaning the approved mechanism of action could reasonably extend to this rare primary site.

However, prostatic urethral primary tumours are uncommon, and no trial to date has specifically enrolled or stratified this subpopulation. The supporting evidence therefore comes from adjacent urothelial carcinoma trials (non-muscle invasive bladder cancer, multi-tumour-type combination studies) rather than site-specific confirmatory studies.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT02844816](https://clinicaltrials.gov/study/NCT02844816) | Phase 2 | Completed | 172 | Evaluated atezolizumab in BCG-unresponsive recurrent non-muscle invasive bladder cancer; same urothelial carcinoma family but not prostatic urethra-specific |
| [NCT03170960](https://clinicaltrials.gov/study/NCT03170960) | Phase 1 | Active, not recruiting | 914 | Dose-escalation study of cabozantinib ± atezolizumab across multiple urothelial carcinoma sites (bladder, renal pelvis, ureter, urethra), early safety/PK focus |

## Literature Evidence

Currently no related literature available.

## Norway Market Information

No authorizations found in the Norway registry — the product is not currently marketed in Norway.

## Cytotoxicity (Antineoplastic Drugs Only)

| Item | Content |
|------|------|
| Cytotoxicity Classification | Immunotherapy (PD-L1 checkpoint inhibitor) — not a conventional cytotoxic agent |
| Myelosuppression Risk | Low (mechanism is immune-mediated rather than direct bone marrow toxicity; immune-related adverse events (irAEs) are the primary concern instead) |
| Emetogenicity Classification | Low |
| Monitoring Items | Liver function tests, thyroid function, signs of immune-related adverse events (colitis, pneumonitis, hepatitis, endocrinopathies); CBC if combined with cytotoxic agents |
| Handling Protection | Standard IV biologic infusion precautions; not classified as a cytotoxic hazardous drug requiring special chemotherapy handling protocols |

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The prediction is mechanistically plausible and supported by L2-level evidence from adjacent urothelial carcinoma trials, but no trial or literature specifically addresses the prostatic urethra subtype, and the drug is not yet marketed in Norway.

**To proceed, the following is needed:**
- TFDA/label safety data (warnings, contraindications) — currently a blocking data gap (DG001)
- Detailed mechanism of action (MOA) documentation from DrugBank (DG002)
- Site-specific clinical evidence (trial or case series) in prostatic urethral urothelial carcinoma
- Norway market authorization status confirmation before any commercial evaluation
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

