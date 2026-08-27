---
layout: default
title: Aflibercept
parent: 僅模型預測 (L5)
nav_order: 19
evidence_level: L5
indication_count: 1
---

# Aflibercept
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

Using the Evidence Pack as provided, here is the evaluation report.

---

# Aflibercept: From Neovascular Eye Disease to Esotropia

## One-Sentence Summary

> Aflibercept is a VEGF-A/VEGF-B/PlGF trap protein originally developed for neovascular eye diseases such as wet AMD, DME, and RVO.
> The TxGNN model predicts it may be effective for **Esotropia**, but this prediction is currently supported by **0 clinical trials** and **0 publications**,
> and the proposed mechanistic link between anti-VEGF activity and esotropia (an extraocular muscle/neuromuscular disorder) is not well established.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available in regulatory license data (drug not marketed); based on the drug's known mechanism, it is described in this evidence pack as used for neovascular eye diseases (e.g., wet AMD, DME, RVO) |
| Predicted New Indication | Esotropia |
| TxGNN Prediction Score | 99.38% |
| Evidence Level | L5 (model prediction only, no supporting trials or literature) |
| Norway Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

The formal `original_moa` field for this drug is marked as a data gap, so a fully sourced mechanism-of-action statement is not currently available. However, the evidence pack's own repurposing rationale describes aflibercept as a VEGF-A/VEGF-B/PlGF trap protein that blocks angiogenic signaling, and notes it is used for neovascular eye diseases such as wet AMD, diabetic macular edema (DME), and retinal vein occlusion (RVO). All of these are conditions driven by pathological blood vessel growth in the retina/choroid.

Esotropia, by contrast, is a form of strabismus caused by extraocular muscle tone imbalance, accommodative convergence abnormalities, or cranial nerve (typically CN VI) dysfunction — a neuromuscular/ocular-motor control problem, not a vascular or angiogenic one. There is no established pharmacological pathway connecting VEGF-trap activity to extraocular muscle balance or nerve function.

Based on the rationale provided in this evidence pack, the two conditions appear to share only a broad "ophthalmic disease" classification in the knowledge graph. The high TxGNN score (99.38%) most likely reflects topological similarity between disease nodes in the knowledge graph rather than a genuine pharmacological connection, and should be treated as a **high-risk candidate false positive**. This assessment is further limited by the unresolved MOA data gap and the fact that the drug is not currently marketed in this jurisdiction, both of which reduce confidence in any causal inference.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Norway Market Information

This drug is not currently marketed in Norway (market status: Not Marketed), and no marketing authorization records are available in this evidence pack.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Despite a high TxGNN prediction score, this candidate has zero supporting clinical trials and zero supporting literature, and the proposed mechanistic link between anti-VEGF activity and esotropia is not pharmacologically well-supported — it likely reflects a knowledge-graph topological artifact rather than a genuine biological relationship. Combined with an unresolved blocking data gap on TFDA package insert warnings/contraindications and a missing confirmed MOA, this candidate does not currently meet the threshold to advance past initial screening.

**To proceed, the following is needed:**
- TFDA package insert (warnings, contraindications) — currently a Blocking data gap (DG001)
- Confirmed mechanism of action from DrugBank or another authoritative source — currently a High-severity data gap (DG002)
- An independent mechanistic plausibility review specifically addressing the VEGF-pathway-to-strabismus link before further evidence collection is prioritized
- Any available preclinical or case-level evidence connecting VEGF signaling to extraocular muscle/neuromuscular function, if it exists
- Updated market/regulatory status confirmation, since the drug is currently unmarketed in this jurisdiction
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

