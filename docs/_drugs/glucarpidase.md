---
layout: default
title: Glucarpidase
parent: 僅模型預測 (L5)
nav_order: 165
evidence_level: L5
indication_count: 10
---

# Glucarpidase
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

# Glucarpidase: From Methotrexate Toxicity to Diabetic Cataract

## One-Sentence Summary

> Glucarpidase is a recombinant bacterial carboxypeptidase used clinically to rapidly hydrolyze excess methotrexate in patients with impaired renal clearance.
> The TxGNN model predicts potential efficacy for **Diabetic Cataract**,
> but currently **0 clinical trials** and **0 publications** support this direction — evidence strength is minimal.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | No approved indication data available (drug not marketed in this jurisdiction); known clinical use is methotrexate toxicity rescue in renal impairment |
| Predicted New Indication | Diabetic Cataract |
| TxGNN Prediction Score | 99.85% |
| Evidence Level | L5 |
| Norway Market Status | 未上市 (Not Marketed) |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available (marked as a High-severity data gap). Based on the limited information in this evidence pack, glucarpidase's known clinical role is enzymatic hydrolysis of methotrexate into inactive metabolites (DAMPA and glutamate) to reduce toxicity in patients with delayed renal clearance — a rescue/antidote function, not a disease-modifying therapy.

There is no known biological pathway connecting this folate-analog-metabolizing mechanism to diabetic cataract, which is driven by hyperglycemia-induced polyol pathway activation, osmotic stress, and lens protein glycation/oxidation. No mechanistic bridge is proposed in the evidence pack, and the rationale text explicitly states no known linkage exists.

Notably, all 10 of this drug's top predicted indications cluster tightly around cataract subtypes (diabetic, senile, nuclear, cortical, mature, immature, etc.) and diabetic retinopathy, with nearly identical scores (~0.998) despite having no shared underlying pathology with methotrexate metabolism. This pattern — high score clustering with zero mechanistic, preclinical, or clinical support — is characteristic of an embedding-level artifact rather than a genuine biological signal, likely because glucarpidase is a sparsely connected orphan drug in the underlying knowledge graph.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Norway Market Information

This drug is not marketed in this jurisdiction (0 authorizations on record), so no product license table is available.

---

## Safety Considerations

Please refer to the package insert for safety information. (Note: TFDA/local label warnings and contraindications are flagged as a **Blocking** data gap in this evidence pack — this must be resolved before any safety evaluation can proceed.)

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is supported by TxGNN score alone (L5, no clinical or literature evidence), and all top-10 predicted indications for this drug cluster suspiciously around a single unrelated disease family (cataract/diabetic eye disease) with no plausible mechanistic connection to glucarpidase's known enzymatic function — this pattern suggests a model artifact rather than a credible repurposing signal.

**To proceed, the following is needed:**
- Resolve the Blocking data gap: TFDA/local label warnings and contraindications
- Obtain verified mechanism of action (MOA) data from DrugBank or primary literature
- Independent mechanistic or preclinical evidence linking carboxypeptidase G2 activity to diabetic cataract pathology before further investment
- Given the clustering pattern across all 10 predictions, consider a KG-connectivity review for this orphan drug rather than pursuing individual indications
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

