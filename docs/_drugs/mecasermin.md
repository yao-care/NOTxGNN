---
layout: default
title: Mecasermin
parent: 僅模型預測 (L5)
nav_order: 223
evidence_level: L5
indication_count: 5
---

# Mecasermin
{: .fs-9 }

證據等級: **L5** | 預測適應症: **5** 個
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

Using no specialized skill — this is a direct report-generation task with an explicit template; producing the deliverable per the given schema and evidence pack.

# Mecasermin: From Unspecified Original Indication to Monosomy X

## One-Sentence Summary

> The original approved indication for Mecasermin is not documented in the available regulatory data source, and mechanism-of-action data is currently missing.
> The TxGNN model's top-ranked prediction is **Monosomy X**, but this signal is supported by **0 clinical trials** and **0 publications**, and the underlying rationale is an indirect analogy rather than a validated mechanistic link.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not documented in current data source |
| Predicted New Indication | Monosomy X |
| TxGNN Prediction Score | 99.59% |
| Evidence Level | L5 |
| Norway Market Status | Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism-of-action data for Mecasermin is not available, and no original indication is recorded in the current data source. This is flagged as a **blocking data gap** (missing TFDA/package-insert warnings and contraindications) and a **high-severity gap** (missing MOA), both of which limit any confident mechanistic assessment.

For the top-ranked prediction, Monosomy X (commonly associated with Turner syndrome), the model's own rationale states that this condition is often accompanied by partial GH/IGF-1 axis insufficiency and growth delay, so IGF-1 supplementation could theoretically offer growth benefit. However, this is explicitly noted as an **indirect analogy** — Turner syndrome is conventionally managed with growth hormone (GH), not mecasermin (recombinant IGF-1), and there is no direct mechanistic evidence chain linking mecasermin specifically to this condition. The prediction should be treated as a graph-derived signal rather than a substantiated hypothesis.

Notably, a lower-ranked candidate in this evidence pack — **growth hormone insensitivity syndrome with immune dysregulation 2, autosomal dominant** (rank 3, score 99.06%) — has a considerably stronger mechanistic basis: it falls within the family of GH-insensitivity/Laron-type syndromes, which is the pharmacological space mecasermin (rhIGF-1) is designed to address by bypassing a defective GH receptor pathway. This candidate has already advanced to decision stage **S1 (Research Question)**, versus S0 (Hold) for Monosomy X, and may warrant closer review despite its lower TxGNN score.

## Clinical Trial Evidence

Currently no related clinical trials registered

## Literature Evidence

Currently no related literature available

## Norway Market Information

Mecasermin currently holds **no marketing authorizations in Norway** (total licenses: 0; market status: Not Marketed). No product, dosage form, or approved indication data is available in the current data source.

## Safety Considerations

Please refer to the package insert for safety information. (Package-insert warnings, contraindications, and drug-drug interaction data are currently unavailable and are flagged as a blocking data gap requiring TFDA label retrieval before any safety-stage evaluation can proceed.)

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked predicted indication (Monosomy X) has only Evidence Level L5 (model prediction only, no clinical trials or literature) and is based on an indirect mechanistic analogy rather than a validated pathway. Combined with the absence of Norway market authorization and a blocking gap in package-insert safety data, there is currently insufficient basis to advance beyond preliminary research.

**To proceed, the following is needed:**
- TFDA/package-insert warnings and contraindications (blocking gap, DG001)
- Confirmed mechanism-of-action documentation from DrugBank or equivalent source (DG002)
- Documentation of Mecasermin's original approved indication(s)
- Targeted literature/clinical trial search for the mechanistically stronger candidate (growth hormone insensitivity syndrome with immune dysregulation 2, autosomal dominant), given its closer alignment with mecasermin's known pharmacology
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

