---
layout: default
title: Abiraterone Acetate
parent: 僅模型預測 (L5)
nav_order: 15
evidence_level: L5
indication_count: 0
---

# Abiraterone Acetate
{: .fs-9 }

證據等級: **L5** | 預測適應症: **0** 個
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

# Abiraterone Acetate: Evaluation Pending — No Predicted Indication Available

## One-Sentence Summary

Abiraterone acetate is a CYP17A1 inhibitor originally developed for the treatment of metastatic castration-resistant prostate cancer (mCRPC). The TxGNN model has **not yet generated a predicted new indication** for this drug. The current evidence pack contains significant data gaps that must be resolved before evaluation can proceed.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Metastatic castration-resistant prostate cancer (mCRPC)¹ |
| Predicted New Indication | — (No prediction available) |
| TxGNN Prediction Score | — |
| Evidence Level | L5 (No prediction or supporting studies) |
| Taiwan Market Status | ✗ Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | **Hold** |

> ¹ Based on globally established use; no TFDA licence data available in this evidence pack.

## Why is This Prediction Reasonable?

Currently, no new indication has been predicted by TxGNN for abiraterone acetate, so mechanistic plausibility cannot be assessed at this time.

For context, abiraterone acetate is a prodrug of abiraterone, which irreversibly inhibits CYP17A1 (17α-hydroxylase/C17,20-lyase), a key enzyme in androgen biosynthesis. By blocking androgen production in the testes, adrenal glands, and prostate tumour tissue, it suppresses tumour growth driven by androgen receptor signalling. It is globally approved (FDA, EMA) for use in combination with prednisone for mCRPC and metastatic high-risk castration-sensitive prostate cancer (mCSPC).

Detailed mechanism of action data was not included in the evidence pack (identified as Data Gap DG002). Once TxGNN generates a predicted indication, the MOA data should be retrieved from DrugBank to assess whether the CYP17A1 inhibition pathway — or secondary pharmacological effects — could be relevant to the new target disease.

## Clinical Trial Evidence

Currently no predicted indication has been generated; therefore, no indication-specific clinical trial search was performed.

## Literature Evidence

Currently no predicted indication has been generated; therefore, no indication-specific literature search was performed.

## Taiwan Market Information

Abiraterone acetate has **no TFDA-approved licences** recorded in this evidence pack. The drug is listed as "Not marketed" in Taiwan.

## Cytotoxicity

Abiraterone acetate is an antineoplastic agent (androgen biosynthesis inhibitor) and therefore requires cytotoxicity consideration.

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (Hormonal / Androgen biosynthesis inhibitor) |
| Myelosuppression Risk | Low (not a conventional cytotoxic; anaemia is a known adverse effect) |
| Emetogenicity Classification | Low |
| Monitoring Items | Liver function (ALT/AST — hepatotoxicity risk), blood pressure, serum potassium, serum cortisol, CBC, cardiac function |
| Handling Protection | Standard precautions; not classified as conventional cytotoxic — no special closed-system handling required, but pregnant women should avoid handling crushed/broken tablets |

## Safety Considerations

No TFDA package insert data, warnings, contraindications, or drug–drug interaction data were available in this evidence pack.

> Please refer to the package insert for safety information. Key safety concerns known globally include:
> - **Hepatotoxicity** — ALT/AST elevations requiring monitoring
> - **Mineralocorticoid excess** — Hypertension, hypokalaemia, fluid retention (due to CYP17A1 blockade upstream of mineralocorticoid synthesis)
> - **Adrenocortical insufficiency** — Requires concomitant corticosteroid administration
> - **Cardiac disorders** — Cardiac failure, atrial fibrillation reported

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN model has not yet produced a predicted new indication for abiraterone acetate, and there are multiple blocking data gaps (TFDA labelling, MOA data). Without a target indication, no evidence-level assessment or go/no-go recommendation can be made.

**To proceed, the following is needed:**
- Run TxGNN prediction pipeline for abiraterone acetate to generate candidate indications
- Resolve **DG001** (Blocking): Retrieve TFDA package insert warnings and contraindications, or note that the drug is not marketed in Taiwan and source safety data from FDA/EMA labels instead
- Resolve **DG002** (High): Query DrugBank for MOA and pharmacological classification (DrugBank ID: [DB05812](https://go.drugbank.com/drugs/DB05812))
- Clarify Taiwan regulatory pathway — if the drug is not marketed in Taiwan, determine whether a TFDA import pathway or special access scheme applies
- Re-generate the evidence pack once the above gaps are filled and TxGNN predictions are available
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

