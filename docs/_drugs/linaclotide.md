---
layout: default
title: Linaclotide
parent: 僅模型預測 (L5)
nav_order: 210
evidence_level: L5
indication_count: 3
---

# Linaclotide
{: .fs-9 }

證據等級: **L5** | 預測適應症: **3** 個
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

# Linaclotide: From Not Specified to Cauda Equina Syndrome

## One-Sentence Summary

> Linaclotide's original approved indication is not documented in the current evidence pack (mechanism of action and indication data are unavailable).
> The TxGNN model predicts it may be effective for **Cauda Equina Syndrome**,
> but this prediction is currently supported by **0 clinical trials** and **0 publications**, and the drug is not marketed in Norway.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available in current data |
| Predicted New Indication | Cauda Equina Syndrome |
| TxGNN Prediction Score | 99.96% |
| Evidence Level | L5 |
| Norway Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available for linaclotide in this evidence pack. Based on the drug's known pharmacological class, linaclotide is a guanylate cyclase-C (GC-C) agonist that acts locally on intestinal epithelial receptors, with negligible systemic absorption and no central or peripheral neural mechanism of action.

Cauda equina syndrome is a surgical emergency caused by mechanical compression of the lumbosacral nerve roots, requiring urgent decompression. There is no established physiological link between GI secretory modulation (linaclotide's known mode of action) and nerve root compression pathology.

Given the absence of any supporting clinical trials or literature, this prediction most likely reflects a knowledge-graph artifact — possibly arising from shared comorbidity nodes such as constipation or neurogenic bowel symptoms that commonly co-occur with cauda equina syndrome — rather than a genuine pharmacological signal.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Norway Market Information

Linaclotide is not currently marketed in Norway, and no authorization records are available in this evidence pack.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Additional Predictions Evaluated

Two other TxGNN-predicted indications were reviewed in this evidence pack, both similarly unsupported:

| Rank | Predicted Indication | TxGNN Score | Evidence | Recommendation |
|------|----------------------|-------------|----------|-----------------|
| 2 | Obsolete Neurogenic Bladder (disease) | 99.89% | None | Hold |
| 3 | Insomnia | 99.51% | None | Hold |

Rank 2 is flagged as an obsolete/deprecated disease ontology node, indicating a data-quality issue rather than a valid hypothesis. Rank 3 lacks mechanistic plausibility, as linaclotide has oral bioavailability <0.1% and does not cross the blood-brain barrier, precluding any central action on sleep-regulating pathways.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
All three predicted indications carry L5 evidence (model prediction only), with zero supporting clinical trials or literature, and the top-ranked candidate (cauda equina syndrome) lacks any plausible mechanistic basis given linaclotide's local, non-systemic mode of action. Additionally, this candidate cannot proceed to safety screening (S1) due to a Blocking data gap on TFDA warnings/contraindications.

**To proceed, the following is needed:**
- TFDA package insert (warnings, contraindications) — currently a Blocking data gap (DG001)
- Confirmed mechanism of action data from DrugBank — currently a High-severity data gap (DG002)
- Original approved indication(s) for linaclotide, to establish a baseline for mechanistic comparison
- Any real-world or preclinical evidence directly linking GC-C agonism to the predicted indications before further evaluation is warranted
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

