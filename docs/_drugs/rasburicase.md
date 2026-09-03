---
layout: default
title: Rasburicase
parent: 僅模型預測 (L5)
nav_order: 297
evidence_level: L5
indication_count: 10
---

# Rasburicase
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

# Rasburicase: From Tumor Lysis Syndrome-Associated Hyperuricemia to Renal Hypouricemia

## One-Sentence Summary

Rasburicase is a recombinant urate oxidase used to manage hyperuricemia associated with tumor lysis syndrome. The TxGNN model's top prediction is **Renal Hypouricemia**, but this candidate has **zero clinical trials and zero publications** supporting it, and is mechanistically inconsistent with the drug's known pharmacology — the target disease is a condition of *abnormally low* uric acid, while Rasburicase's known effect is to *lower* uric acid further.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Tumor lysis syndrome-associated hyperuricemia (from known pharmacology; no Norway license record available) |
| Predicted New Indication | Renal Hypouricemia |
| TxGNN Prediction Score | 99.99% |
| Evidence Level | L5 |
| Norway Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Formal structured mechanism-of-action (MOA) data is currently a Data Gap (DG002). However, based on the pharmacological description available in the evidence pack, Rasburicase is a recombinant urate oxidase (uricase) enzyme that catalyzes the oxidation of uric acid to allantoin, thereby **lowering** serum uric acid concentration. It is clinically used to manage hyperuricemia associated with tumor lysis syndrome in oncology patients.

The top-ranked TxGNN candidate, renal hypouricemia, is a condition characterized by **abnormally low** serum uric acid, typically caused by defective renal urate reabsorption (e.g., URAT1/GLUT9 transporter dysfunction). This is pharmacologically **opposite** in direction to Rasburicase's known uric-acid-lowering effect — there is no plausible clinical rationale for administering a uric-acid-lowering enzyme to a patient who already has pathologically low uric acid. This mechanistic contradiction is explicitly flagged in the evidence pack itself.

The high TxGNN score most likely reflects graph-embedding proximity between uric acid/purine-metabolism-related genes and pathways in the knowledge graph, rather than a genuine treatment relationship. Among the 10 candidates in this evidence pack, rank #2 (hypoxanthine-guanine phosphoribosyltransferase partial deficiency / Kelley-Seegmiller syndrome) has a more biochemically coherent rationale, since that condition causes purine-pathway-driven *hyperuricemia* — the direction Rasburicase is actually known to treat. However, it too currently has no supporting clinical trials or literature.

---

## Clinical Trial Evidence

Currently no related clinical trials registered

---

## Literature Evidence

Currently no related literature available

---

## Norway Market Information

Rasburicase is **not marketed** in Norway; no product authorization records are available (0 licenses on file).

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
This is a pure model prediction (L5) with no clinical trial or literature support, and the top-ranked candidate indication is mechanistically implausible — it reverses the direction of Rasburicase's known pharmacological effect. There is insufficient basis to advance this candidate.

**To proceed, the following is needed:**
- TFDA/regulatory package insert warnings and contraindications (DG001, **Blocking** — currently prevents entry into S1 safety review)
- Structured MOA and DrugBank category data (DG002, High severity)
- Independent biochemical/preclinical validation of a mechanistically coherent target — rank #2 (HGPRT partial deficiency) warrants closer review before rank #1
- If pursued, a Norway regulatory pathway assessment, since the drug currently holds no local market authorization
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

