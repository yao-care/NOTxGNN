---
layout: default
title: Leflunomide
parent: 僅模型預測 (L5)
nav_order: 203
evidence_level: L5
indication_count: 2
---

# Leflunomide
{: .fs-9 }

證據等級: **L5** | 預測適應症: **2** 個
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

# Leflunomide: From DMARD/Immunomodulator to Brachydactyly-Syndactyly Syndrome

## One-Sentence Summary

> Leflunomide is a known dihydroorotate dehydrogenase (DHODH) inhibitor used clinically as a disease-modifying antirheumatic drug (DMARD) / immunomodulator; its specific original indication record is not yet available in this dataset.
> The TxGNN model predicts it may be effective for **brachydactyly-syndactyly syndrome**, a rare developmental limb disorder,
> but this prediction is currently supported by **0 clinical trials** and **0 publications** — it is a model-output-only signal with no independent mechanistic, trial, or literature corroboration.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available in current dataset (drug is a known DHODH inhibitor / DMARD immunomodulator per mechanistic notes; formal indication text pending) |
| Predicted New Indication | Brachydactyly-syndactyly syndrome |
| TxGNN Prediction Score | 99.93% |
| Evidence Level | L5 |
| Market Status | Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data for leflunomide is marked as a data gap in this evidence pack. Based on generally known pharmacology referenced in the model's own rationale notes, leflunomide inhibits dihydroorotate dehydrogenase (DHODH), thereby suppressing pyrimidine synthesis and lymphocyte proliferation — this is the basis for its established use as an immunomodulatory DMARD.

Brachydactyly-syndactyly syndrome, however, is a rare congenital disorder of limb development, typically driven by mutations in developmental patterning genes such as *HOXD* or *GLI3*. There is no known overlap between DHODH/pyrimidine-synthesis inhibition and the developmental gene pathways implicated in this syndrome.

The repurposing rationale for this candidate explicitly states that **no mechanistic link can be established** — the prediction reflects a high-scoring knowledge-graph association from the TxGNN algorithm alone, without biological plausibility support. This should be treated as a hypothesis-generating signal only, not as evidence of therapeutic relevance.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Norway Market Information

Leflunomide currently has no marketing authorizations recorded (0 licenses; market status: Not Marketed). No product table is available.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
This candidate is supported only by an L5 (model-prediction-only) evidence level, with no clinical trials or literature identified, and the repurposing rationale itself states no mechanistic plausibility could be established between leflunomide's known DHODH-inhibitory action and the pathology of brachydactyly-syndactyly syndrome. Combined with a Blocking-severity data gap on TFDA label warnings/contraindications, this candidate cannot proceed to safety pre-screening (S1).

**To proceed, the following is needed:**
- TFDA label (warnings/contraindications) — required before any S1 safety evaluation (DG001, Blocking)
- Confirmed mechanism of action data from DrugBank (DG002, High)
- Independent mechanistic or preclinical rationale linking DHODH/pyrimidine synthesis inhibition to limb developmental disorders
- Any emerging clinical trial or case-report literature for this indication

---

*Note: A second candidate indication, colobomatous microphthalmia-rhizomelic dysplasia syndrome (TxGNN score 99.93%, rank 1084), carries the same L5 evidence level, zero trial/literature support, and an equivalent "no mechanistic link established" conclusion. It is likewise recommended for Hold pending the same data gaps above.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

