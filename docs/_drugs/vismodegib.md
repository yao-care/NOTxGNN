---
layout: default
title: Vismodegib
parent: 僅模型預測 (L5)
nav_order: 386
evidence_level: L5
indication_count: 10
---

# Vismodegib
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

# Vismodegib: From Basal Cell Carcinoma to Medulloblastoma with Extensive Nodularity

## One-Sentence Summary

> Vismodegib is a Smoothened (SMO) inhibitor whose real-world approved use is for locally advanced/metastatic basal cell carcinoma (BCC) — as reflected in this evidence pack's own rank-9 candidate, which carries strong clinical trial support.
> The TxGNN model's **top-ranked** prediction, however, points to **Medulloblastoma with Extensive Nodularity**, a SHH-pathway-driven brain tumour.
> This specific prediction is currently supported by **0 clinical trials** and **0 publications** in this dataset — the mechanistic rationale is strong, but the evidence chain still needs to be built.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available from Norway licensing data (drug not marketed). Based on evidence-pack context (rank 9 rationale), vismodegib's known real-world approved indication is locally advanced/metastatic basal cell carcinoma (BCC) |
| Predicted New Indication | Medulloblastoma with extensive nodularity |
| TxGNN Prediction Score | 99.93% |
| Evidence Level | L5 |
| Norway Market Status | ✗ Not marketed (未上市) |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Vismodegib is a Smoothened (SMO) antagonist that blocks the Hedgehog (Hh) signaling pathway. This official MOA field is marked as a data gap in this pack, but the mechanism is consistently described across the pack's own rationale texts and cited literature (e.g., PMID 22679179, PMID 24756807): vismodegib binds SMO and prevents aberrant activation of GLI transcription factors, suppressing tumour proliferation in Hh-driven cancers.

The predicted indication — SHH-subtype medulloblastoma — is mechanistically well matched: this brain tumour subtype is directly dependent on constitutive Hedgehog pathway activation, the same pathway vismodegib was designed to block. This is analogous to vismodegib's established real-world approved use in BCC, where PTCH1/SMO pathway mutations drive tumorigenesis (see the rank-9 candidate "skin cancer" in this same pack, which shows large-scale Phase II trial support, e.g. NCT01367665, n=1232).

Notably, the rationale attached to this top-ranked prediction explicitly notes: *"現實世界中 vismodegib 已核准用於成人復發性/轉移性髓母細胞瘤"* (vismodegib is already approved in the real world for adult recurrent/metastatic medulloblastoma). This suggests the TxGNN model has correctly identified a mechanistically and clinically valid signal — the absence of trials/literature in this specific dataset likely reflects a gap in evidence retrieval/indexing for this exact indication term, rather than an absence of real-world evidence. This gap should be closed by targeted literature search before proceeding.

---

## Clinical Trial Evidence

Currently no related clinical trials registered

---

## Literature Evidence

Currently no related literature available

---

## Norway Market Information

No market authorization data available — vismodegib is not currently marketed in Norway (0 authorizations on file).

---

## Cytotoxicity

Vismodegib is an antineoplastic agent (Hedgehog pathway inhibitor used in cancer indications), so this section applies.

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (Hedgehog pathway / Smoothened inhibitor) — not a conventional cytotoxic chemotherapy agent |
| Myelosuppression Risk | Please refer to the package insert warnings and precautions |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | Please refer to the package insert warnings and precautions |
| Handling Protection | Please refer to the package insert warnings and precautions |

---

## Safety Considerations

Please refer to the package insert for safety information.

*(Note: TFDA/label warnings and contraindications are flagged as a **Blocking** data gap [DG001] in this evidence pack — this must be resolved before any S1 safety evaluation can proceed.)*

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN score for this indication is very high (99.93%), and the mechanistic rationale (SHH-pathway dependency in medulloblastoma) is sound and consistent with vismodegib's known real-world use. However, this dataset currently provides **zero clinical trials and zero literature citations** for this specific indication, placing it at evidence level L5 — model prediction only, with no corroborating study evidence assembled yet.

**To proceed, the following is needed:**
- Targeted literature/trial search for "vismodegib + medulloblastoma" (the rationale text itself indicates real-world approval exists — this needs to be sourced and added to the evidence pack)
- TFDA/product label warnings and contraindications (DG001, Blocking severity — currently prevents S1 safety evaluation)
- Formal mechanism of action (MOA) documentation from DrugBank (DG002, High severity)
- Norway market authorization pathway assessment, since the drug is currently not marketed there
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

