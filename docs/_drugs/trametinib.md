---
layout: default
title: Trametinib
parent: 僅模型預測 (L5)
nav_order: 367
evidence_level: L5
indication_count: 10
---

# Trametinib
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

# Trametinib: From Malignant Melanoma to Choroideremia

## One-Sentence Summary

> Trametinib is a MEK1/2 inhibitor developed and used (in combination with dabrafenib) for BRAF V600E/K mutation-positive malignant melanoma.
> The TxGNN model's top-ranked prediction is **Choroideremia**, a rare inherited retinal degeneration,
> but this prediction is currently supported by **0 clinical trials** and **0 publications**, and no known pathophysiological link to the drug's MAPK/MEK mechanism has been identified.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Malignant melanoma, BRAF V600E/K mutation-positive (inferred from international trial records; no locally approved indication text on file) |
| Predicted New Indication | Choroideremia |
| TxGNN Prediction Score | 99.31% |
| Evidence Level | L5 |
| Taiwan Market Status | 未上市 (Not marketed) |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the evidence pack (original_moa flagged as a data gap). Based on information embedded in the supporting trial records provided in this pack, trametinib (GSK1120212) is described as "a reversible and highly selective allosteric inhibitor of MEK1 and MEK2," developed for the treatment of malignant melanoma, typically in combination with the BRAF inhibitor dabrafenib.

Choroideremia is a rare X-linked inherited retinal degenerative disease caused by loss-of-function mutations in the *CHM* gene (encoding Rab escort protein-1), which impairs prenylation of Rab GTPases required for photoreceptor and retinal pigment epithelium trafficking. There is no established connection between this pathway and MAPK/MEK signaling, and the evidence pack's own rationale explicitly flags this: *"與 MAPK/MEK 通路無已知病理生理關聯"* — no known pathophysiological relationship exists.

Given the absence of any supporting clinical trial or literature evidence (evidence level L5, decision stage S0), the high TxGNN score for this candidate most likely reflects a spurious correlation in the model's embedding space rather than a genuine biological signal. This is a useful illustration of a case where raw prediction rank should not be interpreted as clinical priority without independent mechanistic or experimental corroboration.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Taiwan Market Information

Trametinib is currently **not marketed** in Taiwan under this evidence pack (0 authorizations on file). No product license or approved-indication records are available for extraction.

---

## Cytotoxicity

Trametinib is an antineoplastic agent (MEK1/2 inhibitor used in BRAF-mutant melanoma), so this section applies.

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (MEK1/2 inhibitor) |
| Myelosuppression Risk | Please refer to the package insert warnings and precautions |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | Please refer to the package insert warnings and precautions |
| Handling Protection | Please refer to the package insert warnings and precautions |

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The choroideremia prediction has no supporting clinical trials or literature (L5/S0), and no known mechanistic pathway links MEK inhibition to CHM-related retinal degeneration. The high TxGNN score is best treated as a candidate for model-artifact review rather than a repurposing lead.

**To proceed, the following is needed:**
- Preclinical/mechanistic evidence connecting MAPK-MEK signaling to CHM-deficient retinal pathology (if any exists)
- Independent verification of the TxGNN embedding score with the modeling team to rule out spurious correlation
- Trametinib mechanism of action (MOA) and TFDA/local label data to close current data gaps (DG001, DG002)

---

## Note: Other Predicted Indications in This Evidence Pack

This evidence pack is a multi-candidate ("TW-DB08911-multi") output, and ranks 2–9 show notably better-supported (though still early-stage) signals — worth flagging alongside the headline prediction above:

| Rank | Disease | Evidence Level | Decision Stage | Recommendation | Key Support |
|------|---------|----------------|-----------------|-----------------|--------------|
| 2 | Non-cutaneous melanoma | L2 | S2 | Research Question | Phase 3 DREAMseq + multiple Phase 2 trials (BRAF-mutant population, not subtype-specific) |
| 7 | Acral lentiginous melanoma | L2 | S2 | Research Question | [NCT02083354](https://clinicaltrials.gov/study/NCT02083354) — subtype-specific Phase 2 ORR data, n=77 |
| 9 | Superficial spreading melanoma | L3 | S2 | Research Question | Molecular-matched Phase 2 trial + case reports (brain/choroidal metastasis response) |
| 3, 4, 6, 8 | Epithelioid, eyelid, amelanotic, lentigo maligna melanoma | L4 | S1 | Research Question | Case reports/reviews only, no subtype-specific trials |
| 5, 10 | Scrotum melanoma, balloon cell melanoma | L5 | S0 | Hold | No evidence |

**Important caveat:** all of ranks 2–10 are histologic/anatomic **subtypes of melanoma** — the disease space trametinib is already used in (combined with dabrafenib) internationally. These do not represent novel-organ repurposing in the way choroideremia would; they reflect within-indication subtype extrapolation, and their clinical value depends on subtype-specific BRAF mutation prevalence (e.g., acral and mucosal subtypes have markedly lower BRAF V600 mutation rates than classic cutaneous melanoma).
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

