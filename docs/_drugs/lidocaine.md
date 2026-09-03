---
layout: default
title: Lidocaine
parent: 僅模型預測 (L5)
nav_order: 209
evidence_level: L5
indication_count: 10
---

# Lidocaine
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

# Lidocaine: From Local Anesthesia to Punctate Epithelial Keratoconjunctivitis

## One-Sentence Summary

Lidocaine is a widely used amide-type local anesthetic; formal indication and mechanism-of-action data for this drug are not available in the current evidence pack. TxGNN's top prediction suggests possible relevance to **Punctate Epithelial Keratoconjunctivitis**, but this prediction is supported by **zero clinical trials** and **zero publications**, and the drug's own pharmacology argues against benefit rather than for it.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not documented in this evidence pack (Lidocaine is generally known as a local anesthetic; formal approved-indication text is a flagged data gap) |
| Predicted New Indication | Punctate Epithelial Keratoconjunctivitis |
| TxGNN Prediction Score | 99.99% |
| Evidence Level | L5 |
| Norway Market Status | ✗ Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data for lidocaine is not available in this evidence pack (flagged as a High-severity data gap). Based on general pharmacological knowledge, lidocaine is an amide-type local anesthetic that blocks voltage-gated Na⁺ channels in nerve terminals, producing reversible loss of sensation — it has no known epithelial-repair or anti-inflammatory mechanism.

For the top-ranked prediction, punctate epithelial keratoconjunctivitis is a corneal epithelial surface disease. The repurposing rationale provided alongside the prediction explicitly notes that repeated or prolonged use of topical anesthetics is a **known risk factor for "anesthetic abuse keratopathy,"** meaning lidocaine could plausibly *worsen* rather than improve this condition. There is no supporting clinical trial or literature evidence for this specific pairing — the prediction is a pure model output (TxGNN score only, Evidence Level L5, Decision Stage S0).

It is worth noting that other, lower-ranked candidates in this evidence pack carry stronger (though still preliminary) support: **conjunctival disorder** (rank 6, Evidence Level L3, multiple Phase 4 trials using lidocaine as ocular surface/perioperative anesthesia) and **atopic conjunctivitis** (rank 5, Evidence Level L4, mechanistic literature on neurogenic modulation of allergic conjunctival responses). These reflect lidocaine's established role as an ocular anesthetic adjunct rather than a primary disease-modifying therapy, and neither constitutes direct evidence for treating the disease itself.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Norway Market Information

No marketing authorizations are on record for lidocaine in this dataset (`market_status`: not marketed; `total_licenses`: 0).

## Safety Considerations

Please refer to the package insert for safety information. (No key warnings, contraindications, or drug-interaction data were available in this evidence pack; the TFDA/label warning data gap is flagged as Blocking, meaning safety review cannot proceed until this is resolved.)

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked prediction (punctate epithelial keratoconjunctivitis) has no clinical or literature support and is mechanistically questionable — repeated topical anesthetic use is a recognized cause of corneal epithelial toxicity, so the risk-benefit direction is unclear at best and unfavorable at worst. This candidate should not proceed.

**To proceed, the following is needed:**
- Resolve the Blocking data gap: obtain TFDA/label warnings, contraindications, and DDI data before any safety evaluation is possible
- Obtain documented mechanism-of-action and original approved indication data for lidocaine
- If this repurposing line is still of interest, redirect evaluation toward the better-evidenced candidates in this same evidence pack — **conjunctival disorder** (L3, multiple completed Phase 4 trials) and **atopic conjunctivitis** (L4, mechanistic support) — rather than the top TxGNN-score candidate, which lacks any supporting evidence
- If pursued, any future ophthalmic use of lidocaine should be framed as a perioperative/procedural anesthetic adjunct, not as disease-modifying therapy, given the absence of a repair or anti-inflammatory mechanism
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

