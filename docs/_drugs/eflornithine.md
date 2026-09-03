---
layout: default
title: Eflornithine
parent: 僅模型預測 (L5)
nav_order: 121
evidence_level: L5
indication_count: 2
---

# Eflornithine
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

# Eflornithine: From African Trypanosomiasis/Hirsutism to Esotropia (Low-Confidence Prediction)

## One-Sentence Summary

Eflornithine is an irreversible ornithine decarboxylase (ODC) inhibitor known clinically for treating African trypanosomiasis and, topically, facial hirsutism. TxGNN predicts a possible new indication for **Esotropia**, but this is supported by **0 clinical trials** and **0 publications**, and the model's own rationale flags no plausible pharmacological link — this is a model-only signal, not evidence-backed.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not on record in this dataset (no Taiwan license/formal indication text available); known clinical uses per available evidence: African trypanosomiasis, topical treatment of facial hirsutism |
| Predicted New Indication | Esotropia |
| TxGNN Prediction Score | 99.85% |
| Evidence Level | L5 |
| Taiwan Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action (MOA) data is not available in the formal `original_moa` field for this candidate (flagged as a **Blocking** data gap, DG001/DG002). Based on the supplementary evidence attached to this prediction, eflornithine is understood to irreversibly inhibit ornithine decarboxylase (ODC), blocking polyamine synthesis — a mechanism underlying its established use in African trypanosomiasis (antiparasitic) and topical suppression of facial hair growth (antiproliferative effect on hair follicles).

Esotropia is a disorder of extraocular muscle tone/neuromuscular control, not a proliferative, parasitic, or polyamine-dependent condition. The model's own repurposing rationale explicitly states there is **no known physiological or pharmacological mechanism** connecting ODC inhibition/polyamine blockade to esotropia, and assesses this prediction as most likely an artifact ("noise") of the TxGNN embedding space rather than a biologically grounded signal.

A secondary candidate, neurotrophic keratopathy (rank 2, score 99.38%), was also evaluated but shows a similarly unsupported — and potentially mechanistically **unfavorable** — link: ODC inhibition would be expected to *reduce* polyamine-driven corneal epithelial regeneration rather than improve it. Neither candidate has any corroborating trial or literature evidence.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Taiwan Market Information

Eflornithine is not currently marketed in Taiwan; no license records are available (`total_licenses = 0`).

## Safety Considerations

Please refer to the package insert for safety information. (Key warnings, contraindications, and drug-drug interaction data are not available in this evidence pack — resolving this is a **Blocking** gap, DG001, required before any S1 safety evaluation can proceed.)

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests solely on a TxGNN model score (L5) with no clinical trials, no literature, and no plausible mechanistic pathway identified by the model's own rationale — in fact, the mechanism plausibly points the opposite direction for the secondary candidate. Combined with a Blocking gap on TFDA/label safety data (DG001) and a missing formal MOA (DG002), this candidate cannot advance past S0.

**To proceed, the following is needed:**
- Confirmed original MOA and approved indication(s) from DrugBank/regulatory source (resolve DG002)
- TFDA (or equivalent) label warnings/contraindications (resolve DG001, Blocking — required before any S1 safety review)
- Independent pharmacological plausibility review for esotropia given the absence of a mechanistic rationale
- Ongoing literature/trial surveillance in case new evidence emerges, given the current absence of any supporting study
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

