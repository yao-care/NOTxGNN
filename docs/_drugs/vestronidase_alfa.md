---
layout: default
title: Vestronidase Alfa
parent: 僅模型預測 (L5)
nav_order: 383
evidence_level: L5
indication_count: 9
---

# Vestronidase Alfa
{: .fs-9 }

證據等級: **L5** | 預測適應症: **9** 個
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

# Vestronidase Alfa: From Mucopolysaccharidosis VII (Sly Syndrome) to Scheie Syndrome

## One-Sentence Summary

> Vestronidase alfa is a recombinant human β-glucuronidase (GUS) enzyme replacement therapy, originally developed for Mucopolysaccharidosis VII (MPS VII, Sly syndrome).
> The TxGNN model predicts it may be effective for **Scheie syndrome**, but this prediction is currently supported by **0 clinical trials** and **0 publications**, and the underlying enzyme deficiency in Scheie syndrome does not match the drug's target.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Mucopolysaccharidosis VII (MPS VII, Sly syndrome) — inferred from supporting literature in this evidence pack |
| Predicted New Indication | Scheie syndrome |
| TxGNN Prediction Score | 99.90% |
| Evidence Level | L5 |
| Norway Market Status | Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available (Data Gap: DG002). Based on information available in this evidence pack, vestronidase alfa is a recombinant human β-glucuronidase (GUS) enzyme replacement therapy. Its approved and clinically studied use is Mucopolysaccharidosis VII (Sly syndrome), a lysosomal storage disorder caused specifically by GUS deficiency; the Phase 3 pivotal trial (UX003-CL301, NCT02377921) demonstrated reduced urinary glycosaminoglycans (GAG) in this population.

Scheie syndrome, however, is a mild form of Mucopolysaccharidosis I (MPS I), caused by deficiency of **α-L-iduronidase**, not GUS. The standard enzyme replacement therapy for MPS I is laronidase — a different recombinant enzyme entirely. TxGNN's prediction appears to be driven by broad semantic similarity between "lysosomal storage diseases" in the knowledge graph, rather than by any shared enzymatic or metabolic pathway. The repurposing rationale in this evidence pack explicitly flags this as a mechanistic mismatch: vestronidase alfa is not a candidate therapy for α-L-iduronidase deficiency.

Given this, the prediction should be treated as a hypothesis-generation signal only, not as a mechanistically grounded lead.

---

## Clinical Trial Evidence

Currently no related clinical trials registered

---

## Literature Evidence

Currently no related literature available

---

## Norway Market Information

Vestronidase alfa currently has no marketing authorization in Norway (market status: not marketed; 0 authorizations on file).

---

## Safety Considerations

Please refer to the package insert for safety information.

*(Note: TFDA/label warnings and contraindications data are currently a **Blocking** data gap — DG001 — preventing entry into the S1 safety pre-assessment stage.)*

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The predicted indication (Scheie syndrome) has no supporting clinical trials or literature, and the enzyme deficiency underlying Scheie syndrome (α-L-iduronidase) does not match vestronidase alfa's target (GUS) — there is no mechanistic basis for repurposing. In addition, a Blocking data gap (missing TFDA label/warnings) prevents this candidate from entering safety pre-assessment regardless of efficacy evidence.

**To proceed, the following is needed:**
- TFDA package insert / label with warnings and contraindications (DG001, Blocking)
- Confirmed mechanism of action documentation from DrugBank (DG002, High)
- Direct genetic or enzymatic evidence linking GUS replacement therapy to α-L-iduronidase-deficient disease before further evaluation
- Consider re-evaluating lower-ranked candidates in this pack (e.g., Hurler syndrome, Sanfilippo syndrome) only after confirming they do not share the same GUS/α-L-iduronidase mismatch identified here — both currently also show mechanistic incompatibility per the repurposing rationale
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

