---
layout: default
title: Trastuzumab Deruxtecan
parent: 僅模型預測 (L5)
nav_order: 369
evidence_level: L5
indication_count: 1
---

# Trastuzumab Deruxtecan
{: .fs-9 }

證據等級: **L5** | 預測適應症: **1** 個
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

# Trastuzumab Deruxtecan: From HER2-Targeted ADC Therapy to Drug-Induced Osteoporosis

## One-Sentence Summary

> Trastuzumab deruxtecan is a HER2-targeted antibody-drug conjugate (ADC) carrying a cytotoxic topoisomerase I inhibitor payload (DXd); the original approved indication is not documented in this evidence pack.
> The TxGNN model predicts a possible association with **drug-induced osteoporosis**,
> but this is supported by **0 clinical trials** and **0 publications** — the prediction rests entirely on the model score, with no independent evidence.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not documented in evidence pack (data gap — MOA and original indication fields both blank) |
| Predicted New Indication | Drug-induced osteoporosis |
| TxGNN Prediction Score | 99.31% |
| Evidence Level | L5 |
| Norway Market Status | ✗ Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | **Hold** |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in structured form (`original_moa` = data gap). However, the evidence pack's own rationale text identifies trastuzumab deruxtecan as a HER2-targeted antibody-drug conjugate whose payload, DXd, is a topoisomerase I inhibitor — a systemic cytotoxic chemotherapy agent, not a bone-protective agent.

Clinically, cytotoxic chemotherapy and HER2-directed endocrine-adjacent regimens (e.g., aromatase inhibition, ovarian suppression in HER2+ breast cancer) are well-recognized **causes** of drug-induced bone loss, not treatments for it. The predicted link therefore runs in the opposite direction from established pharmacology: the drug is mechanistically more plausible as a *risk factor* for osteoporosis than as a *therapy* for it.

Given this, the prediction should be treated as a likely false positive of the data-driven TxGNN model rather than a biologically grounded repurposing hypothesis. No mechanistic, trial, or literature evidence currently supports pursuing this indication.

---

## Clinical Trial Evidence

Currently no related clinical trials registered

---

## Literature Evidence

Currently no related literature available

---

## Norway Market Information

Trastuzumab deruxtecan is not currently marketed in Norway; no authorizations are on record.

---

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (HER2-directed ADC) with conventional cytotoxic payload (DXd, topoisomerase I inhibitor) |
| Myelosuppression Risk | Please refer to the package insert warnings and precautions |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | Please refer to the package insert warnings and precautions |
| Handling Protection | Must follow cytotoxic/ADC drug handling regulations |

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The predicted indication is unsupported by any clinical trial or literature evidence and is mechanistically implausible — the drug's known cytotoxic ADC profile is more consistent with *causing* bone loss than treating osteoporosis. Combined with blocking data gaps in MOA and TFDA safety labeling, there is no basis to advance this candidate.

**To proceed, the following is needed:**
- Confirmed original approved indication and MOA data (currently missing from evidence pack)
- TFDA/manufacturer package insert (warnings, contraindications) — currently a blocking data gap
- Independent mechanistic or preclinical evidence explaining a plausible bone-protective effect, if any exists, before further evaluation
- Re-review after data gaps DG001/DG002 are remediated
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

