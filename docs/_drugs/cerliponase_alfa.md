---
layout: default
title: Cerliponase Alfa
parent: 僅模型預測 (L5)
nav_order: 82
evidence_level: L5
indication_count: 10
---

# Cerliponase Alfa
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

# Cerliponase Alfa: From CLN2 Disease to Scheie Syndrome

## One-Sentence Summary

> Cerliponase alfa is a recombinant human TPP1 enzyme replacement therapy originally developed for CLN2 disease (a form of neuronal ceroid lipofuscinosis / Batten disease).
> The TxGNN model predicts it may be effective for **Scheie Syndrome** (a subtype of MPS I),
> but this prediction is currently supported by **0 clinical trials** and **0 publications**, and the underlying mechanistic basis appears weak.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in evidence pack (drug not marketed in Norway). Based on the drug's known mechanism referenced in the repurposing rationale, cerliponase alfa is used for **CLN2 disease** (TPP1 enzyme deficiency) |
| Predicted New Indication | Scheie Syndrome |
| TxGNN Prediction Score | 99.98% |
| Evidence Level | L5 (model prediction only, no supporting studies) |
| Norway Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available for cerliponase alfa (`original_moa` = Data Gap). Based on information embedded in the repurposing rationale, cerliponase alfa is a **recombinant human TPP1 (tripeptidyl peptidase 1) enzyme replacement therapy**, specifically indicated to supplement the TPP1 enzyme deficient in CLN2 disease patients.

The top-ranked prediction, Scheie syndrome, is a mild form of Mucopolysaccharidosis type I (MPS I), caused by deficiency of **alpha‑L‑iduronidase (IDUA)** — a completely different enzyme with no substrate overlap with TPP1. The same pattern holds for most of the other top-10 candidates (Hurler syndrome, cholesteryl ester storage disease, Gaucher disease, Wolman disease): each is a distinct lysosomal storage disorder driven by a different causative enzyme (IDUA, LAL, glucocerebrosidase). The high TxGNN scores most likely reflect **knowledge-graph proximity between lysosomal storage disorders as a disease class**, rather than a validated enzymatic or pharmacological cross-reactivity.

One partial exception is worth flagging: rank 8, "juvenile myoclonic epilepsy, susceptibility to," was separately classified by the model as a **Research Question** rather than "Hold." Progressive myoclonic epilepsy is a well-known clinical feature of CLN2 disease itself, so this connection may reflect a genuine phenotype-level link between TPP1/CLN2 biology and epilepsy networks — though it still lacks any clinical trial or literature validation and should not be interpreted as evidence for Scheie syndrome (the top-ranked candidate).

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Norway Market Information

No Norway market authorizations are currently registered for cerliponase alfa (`market_status`: 未上市 / Not Marketed; `total_licenses`: 0).

---

## Safety Considerations

Please refer to the package insert for safety information. (Key warnings, contraindications, and drug-drug interaction data are all flagged as Data Gaps in the evidence pack; TFDA label retrieval is listed as a **Blocking** data gap — DG001.)

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN score is high, but there is zero clinical trial or literature support for the top-ranked candidate (Scheie syndrome), and the mechanistic link is weak — Scheie syndrome and CLN2 disease are driven by entirely different enzymes (IDUA vs. TPP1) with no known substrate overlap. This pattern of graph-proximity-without-mechanism repeats across 9 of the top 10 candidates, indicating the prediction reflects disease-class clustering rather than a validated biological hypothesis.

**To proceed, the following is needed:**
- TFDA/label warnings and contraindications (DG001, Blocking) — required before any S1 safety pre-assessment can begin
- Verified mechanism of action data from DrugBank (DG002, High priority) — needed to properly assess mechanistic plausibility
- If pursuing further, prioritize the rank 8 "juvenile myoclonic epilepsy" signal as a research hypothesis (phenotype-level link to CLN2 disease) rather than the top-ranked Scheie syndrome candidate, which currently has no mechanistic or empirical support
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

