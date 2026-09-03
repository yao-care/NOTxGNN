---
layout: default
title: Cabotegravir
parent: 僅模型預測 (L5)
nav_order: 67
evidence_level: L5
indication_count: 5
---

# Cabotegravir
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

# Cabotegravir: From Undetermined Original Indication to Rheumatoid Arthritis

## One-Sentence Summary

> Cabotegravir (DrugBank ID: DB11751) currently has no verified original indication or mechanism of action on file, and the drug is not yet marketed in Taiwan (TFDA).
> The TxGNN model predicts a possible new indication for **Rheumatoid Arthritis**,
> but this prediction is supported by **0 clinical trials** and **0 publications**, and the model's own rationale flags no known mechanistic overlap.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available — no license or indication data on file |
| Predicted New Indication | Rheumatoid Arthritis |
| TxGNN Prediction Score | 99.45% |
| Evidence Level | L5 (model prediction only, no supporting studies) |
| Taiwan Market Status | ✗ Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available for cabotegravir in this evidence pack, and no original indication is recorded. Based on general pharmacological class knowledge referenced in the evidence pack's own rationale, cabotegravir is an HIV integrase strand transfer inhibitor (INSTI), acting by blocking viral DNA integration into the host genome.

The evidence pack's own mechanistic rationale for the top prediction explicitly states that this integrase-inhibition mechanism has **no known overlap** with rheumatoid arthritis pathophysiology (TNF-α, IL-6, synovial proliferation pathways). The rationale further notes that the missing original-indication data may have destabilized the model's embedding, which could explain the anomalously high score despite the lack of biological plausibility.

The remaining four ranked candidates (sclerosing cholangitis, bronchitis, colobomatous microphthalmia–rhizomelic dysplasia syndrome, severe nonproliferative diabetic retinopathy) show the same pattern: high TxGNN scores with explicitly stated absence of mechanistic linkage, no clinical trials, and no literature. This is consistent with model noise rather than a credible repurposing signal.

---

## Clinical Trial Evidence

Currently no related clinical trials registered

---

## Literature Evidence

Currently no related literature available

---

## Taiwan Market Information

No approved licenses on file — cabotegravir is not currently marketed in Taiwan (0 authorizations).

---

## Safety Considerations

Safety data is currently unavailable (TFDA label, contraindications, and drug interaction data are all flagged as blocking data gaps — see DG001). Please refer to the package insert once available for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests solely on an L5 model score with no clinical trial or literature support, and the evidence pack's own mechanistic analysis finds no known biological link between HIV integrase inhibition and rheumatoid arthritis. Combined with a blocking safety data gap (no TFDA label) and the drug's unmarketed status in Taiwan, there is no basis to advance this candidate.

**To proceed, the following is needed:**
- TFDA product label (warnings, contraindications) — resolves DG001 (blocking)
- Verified mechanism of action from DrugBank — resolves DG002
- Verified original indication(s) for the drug
- Independent preclinical or mechanistic evidence linking INSTI pharmacology to autoimmune/rheumatologic pathways before any further evaluation stage (S1+)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

