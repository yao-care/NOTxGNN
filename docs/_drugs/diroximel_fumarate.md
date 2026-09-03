---
layout: default
title: Diroximel Fumarate
parent: 僅模型預測 (L5)
nav_order: 110
evidence_level: L5
indication_count: 10
---

# Diroximel Fumarate
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

Using the provided Evidence Pack (v4, data cutoff 2026-07-14) for DB14783 / Diroximel Fumarate, here is the evaluation report.

---

# Diroximel Fumarate: From Relapsing Multiple Sclerosis to Diabetic Cataract

## One-Sentence Summary

Diroximel fumarate is a fumarate-class agent approved for relapsing forms of multiple sclerosis, acting via Nrf2/ARE antioxidant pathway activation. The TxGNN model predicts it may be effective for **Diabetic Cataract**, but currently **0 clinical trials** and **0 publications** support this specific direction — the prediction rests entirely on a mechanistic analogy plus a very high (score ≈1.0) graph-neural-network score.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Relapsing forms of multiple sclerosis (per repurposing rationale; not independently confirmed by a Taiwan license record — drug is not marketed in Taiwan) |
| Predicted New Indication | Diabetic Cataract |
| TxGNN Prediction Score | 99.9993% (rank 23 among candidate indications) |
| Evidence Level | L5 (model prediction only, no clinical/preclinical study identified) |
| Taiwan Market Status | ✗ Not marketed (未上市) |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed, source-verified mechanism-of-action data for diroximel fumarate is not yet available in this evidence pack (flagged as a High-severity data gap, DG002). Based on the information captured in the repurposing rationale, diroximel fumarate is a prodrug of monomethyl fumarate, and its known pharmacology involves activation of the Nrf2/ARE (nuclear factor erythroid 2–related factor 2 / antioxidant response element) pathway together with anti-inflammatory effects — the basis of its approved use in relapsing multiple sclerosis.

Diabetic cataract pathology centers on oxidative damage to lens epithelial cells and activation of the polyol pathway under chronic hyperglycemia. Because Nrf2 activation is a recognized cellular defense against oxidative stress, there is a theoretical mechanistic bridge between diroximel fumarate's known pharmacology and diabetic cataract pathophysiology. However, this connection is a **cross-indication mechanistic analogy only** — it has not been tested in any diabetic cataract–specific trial, preclinical model, or published study, and the TxGNN score alone should not be read as clinical evidence of efficacy.

It is also worth noting that this candidate sits within a cluster of ten TxGNN-predicted lens/retinal indications with near-identical scores (diabetic retinopathy, severe nonproliferative diabetic retinopathy, and several cataract subtypes such as cortical, nuclear senile, immature, and mature cataract). The rationale text itself flags some of these — notably **tetanic cataract** and **craniostenosis cataract**, whose etiologies (hypocalcemia, craniosynostosis syndromes) have no plausible link to Nrf2 pathway biology — as likely model over-generalization from shared disease-ontology clustering rather than genuine mechanistic signal. Diabetic cataract and diabetic retinopathy are the only two candidates in this list with a directly traceable, biologically coherent hyperglycemia/oxidative-stress rationale.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Taiwan Market Information

Diroximel fumarate is currently **not marketed in Taiwan** — no TFDA license records exist for this product (0 authorizations on file), so no dosage form or approved indication text is available from Taiwan regulatory sources.

---

## Safety Considerations

Please refer to the package insert for safety information.

*(Note: retrieval of TFDA package insert warnings/contraindications is recorded as a Blocking data gap (DG001) in this evidence pack — this specifically prevents the candidate from entering the S1 safety initial-evaluation stage until resolved.)*

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN score is very high, but it is supported by zero clinical trials, zero publications, and no confirmed mechanism-of-action data — this is an L5, Stage S0 "Research Question" candidate. In addition, the missing TFDA warnings/contraindications data is a Blocking gap that independently prevents any safety initial evaluation, regardless of efficacy evidence.

**To proceed, the following is needed:**
- TFDA package insert (warnings, contraindications, DDI) to clear the Blocking safety gap (DG001)
- Verified mechanism-of-action documentation from DrugBank or primary literature (DG002)
- Preclinical/in-vitro evidence testing Nrf2 pathway activation specifically in diabetic lens or retinal microvascular models
- Clarification of Taiwan regulatory pathway, since the drug is not currently marketed locally
- Continued monitoring of diabetic retinopathy as a related, mechanistically comparable candidate, given its similar score and rationale
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

