---
layout: default
title: Lomitapide
parent: 僅模型預測 (L5)
nav_order: 212
evidence_level: L5
indication_count: 10
---

# Lomitapide
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

Using no additional skill — this is a direct content-generation task with an explicit, fully-specified output format, not a coding/debugging/build task.

# Lomitapide: From Homozygous Familial Hypercholesterolemia to Macrothrombocytopenia with Mitral Valve Insufficiency

## One-Sentence Summary

> Lomitapide is a microsomal triglyceride transfer protein (MTP) inhibitor already approved abroad for **homozygous familial hypercholesterolemia (HoFH)** — though this original indication is missing from the structured drug record and only surfaces indirectly in the evidence pack's literature.
> The TxGNN model's top-ranked new prediction is **macrothrombocytopenia with mitral valve insufficiency**, a rare inherited platelet disorder.
> This prediction is supported by **zero clinical trials and zero publications** — it is a pure model score with no mechanistic rationale.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not present in structured data (`original_indications` is empty). Homozygous Familial Hypercholesterolemia (HoFH) is inferable from the literature/trial evidence attached to a *different* ranked entry (see note below), but is not confirmed in the drug record. |
| Predicted New Indication | Macrothrombocytopenia with mitral valve insufficiency |
| TxGNN Prediction Score | 99.92% |
| Evidence Level | L5 (model prediction only, no supporting studies) |
| Taiwan Market Status | 未上市 (Not marketed) |
| Number of Authorizations | 0 |
| Recommended Decision | **Hold** |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data is officially flagged as a data gap (DG002) in this evidence pack. Based on information surfacing elsewhere in the pack, lomitapide is known to act as an **MTP inhibitor**, blocking hepatic and intestinal apoB-lipoprotein assembly to lower LDL-C/VLDL — the basis of its established use in severe hypercholesterolemia.

For the top-ranked predicted indication, macrothrombocytopenia with mitral valve insufficiency, the evidence pack's own rationale is explicit: *"an extremely rare hereditary disorder with no known pathological link to MTP inhibition. This is purely a graph neural network prediction score, unsupported by any mechanism, trial, or literature."* There is no plausible pharmacological bridge between apoB/lipoprotein assembly inhibition and inherited platelet/valvular pathology. The high TxGNN score likely reflects an indirect graph association (e.g., shared lipid-metabolism nodes) rather than a genuine biological signal.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Taiwan Market Information

Lomitapide is **not currently marketed in Taiwan** (0 authorizations, 0 licenses on record). No product/dosage form/indication data is available to tabulate.

---

## Safety Considerations

Please refer to the package insert for safety information. (TFDA label warnings/contraindications are flagged as a **Blocking** data gap — DG001 — and must be obtained before any S1 safety evaluation can proceed.)

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked predicted indication (macrothrombocytopenia with mitral valve insufficiency) has no clinical trials, no literature, and no plausible mechanistic link — evidence level L5, decision stage S0. There is no basis to advance this candidate.

**To proceed, the following is needed:**
- TFDA label (warnings/contraindications) — currently a Blocking data gap (DG001)
- Confirmed mechanism of action and original approved indication(s) for lomitapide — currently missing from the drug record (DG002)
- Re-evaluation of ranks 2–8 and 10 in this same prediction set, all of which are likewise L5/Hold with no supporting evidence

**⚠️ Data quality note (important for upstream correction):** Rank 9 in this same prediction batch, *hyperlipoproteinemia*, carries strong evidence (12 clinical trials including multiple completed Phase 3 studies, 19 publications) and is the only L1/S3 entry in the set. However, its own rationale flags that this is very likely **not a novel repurposing signal** — it corresponds to lomitapide's already-approved indication (HoFH, marketed as Juxtapid/Lojuxta, FDA-approved 2012), miscategorized as "new" only because the `original_indications` field is empty. This should be corrected at the data source before the candidate is scored again, to avoid conflating "confirmed original indication" with "repurposing discovery" in future reports.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

