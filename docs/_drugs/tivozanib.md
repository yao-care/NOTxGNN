---
layout: default
title: Tivozanib
parent: 僅模型預測 (L5)
nav_order: 358
evidence_level: L5
indication_count: 10
---

# Tivozanib
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

# Tivozanib: From Renal Cell Carcinoma to Endocervical Carcinoma

## One-Sentence Summary

> Tivozanib is a highly selective VEGFR-1/2/3 tyrosine kinase inhibitor, originally developed as an antiangiogenic therapy for renal cell carcinoma.
> The TxGNN model predicts it may also be effective for **Endocervical Carcinoma**,
> but this signal is currently supported by **no registered clinical trials** and **no published literature** — it is a model-derived hypothesis only.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Renal cell carcinoma (based on known drug class information; not confirmed in Norway regulatory data — drug is unmarketed) |
| Predicted New Indication | Endocervical Carcinoma |
| TxGNN Prediction Score | 99.81% |
| Evidence Level | L5 |
| Norway Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the evidence pack (Data Gap DG002). Based on the mechanistic rationale accompanying this prediction, Tivozanib is a highly selective VEGFR-1/2/3 tyrosine kinase inhibitor — its antiangiogenic activity has been established in the treatment of solid tumours such as renal cell carcinoma.

Endocervical carcinoma is also a solid tumour, and antiangiogenic mechanisms are theoretically applicable across tumour types, since most solid tumours depend on VEGF-driven neovascularization to sustain growth. However, this mechanistic link is entirely extrapolated — there is no cervical-cancer-specific pharmacodynamic, translational, or clinical data confirming that Tivozanib's antiangiogenic effect translates into benefit for this indication.

This is one of ten TxGNN-predicted indications for Tivozanib, nearly all clustered around rare cervical/uterine adenocarcinoma subtypes with scores between 99.76%–99.81%. The tight score clustering across rare histological variants, combined with the complete absence of supporting trials or literature, suggests this reflects a broad "antiangiogenic-agent-for-gynecologic-tumour" pattern learned by the model rather than a specific, validated biological relationship.

---

## Clinical Trial Evidence

Currently no related clinical trials registered

---

## Literature Evidence

Currently no related literature available

---

## Norway Market Information

Tivozanib is currently **not marketed in Norway** (0 authorizations on file). No product, dosage form, or approved indication data is available for this market.

---

## Cytotoxicity

Tivozanib is an antineoplastic agent (VEGFR tyrosine kinase inhibitor class).

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (VEGFR-1/2/3 tyrosine kinase inhibitor) |
| Myelosuppression Risk | Low — TKIs of this class are generally less myelosuppressive than conventional cytotoxics; drug-specific toxicity data not yet available |
| Emetogenicity Classification | Low |
| Monitoring Items | Blood pressure, urinalysis (proteinuria), thyroid function, liver function tests, CBC |
| Handling Protection | Please refer to the package insert warnings and precautions once available (TFDA label data is a blocking gap — DG001) |

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on Evidence Level L5 (model prediction only) with zero supporting clinical trials or literature, and a critical safety data gap (TFDA label/warnings, DG001) blocks even a preliminary S1 safety assessment. There is no basis to advance this candidate at this time.

**To proceed, the following is needed:**
- TFDA/manufacturer package insert data — warnings, contraindications, and drug interactions (DG001, blocking)
- Confirmed original indication and regulatory approval history for Tivozanib
- Targeted literature and trial search for VEGFR inhibitors in cervical/gynecologic adenocarcinoma to assess whether a biological rationale exists beyond generic antiangiogenic extrapolation
- Reassessment of Norway market entry pathway, since the drug currently holds no local authorization
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

