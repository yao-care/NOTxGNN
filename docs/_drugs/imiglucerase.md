---
layout: default
title: Imiglucerase
parent: 僅模型預測 (L5)
nav_order: 178
evidence_level: L5
indication_count: 5
---

# Imiglucerase
{: .fs-9 }

證據等級: **L5** | 預測適應症: **5** 個
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

# Imiglucerase: From Gaucher Disease to Hurler Syndrome

## One-Sentence Summary

> Imiglucerase is a recombinant enzyme replacement therapy originally developed for Gaucher disease (glucocerebrosidase deficiency).
> The TxGNN model predicts it may be effective for **Hurler syndrome (MPS I)**,
> but this prediction is supported only by **2 general review articles** and **no clinical trials**, and the mechanistic evidence pack itself flags a likely enzyme mismatch.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Gaucher disease (inferred from mechanistic rationale text; no formal license indication text available) |
| Predicted New Indication | Hurler syndrome |
| TxGNN Prediction Score | 99.52% |
| Evidence Level | L4 |
| Norway Market Status | ✗ Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not formally available (MOA field flagged as a data gap). Based on known pharmacology, imiglucerase is a recombinant form of **glucocerebrosidase (GBA)**, used to replace the enzyme deficient in Gaucher disease patients.

Hurler syndrome, however, is caused by deficiency of a **different enzyme, alpha‑L‑iduronidase (IDUA)** — the two conditions are both lysosomal storage diseases but result from distinct genetic defects and require different replacement enzymes. There is no known mechanistic pathway by which imiglucerase could compensate for IDUA deficiency. The evidence pack's own rationale concludes this TxGNN score likely reflects a **category-level false positive** — the model may be clustering diseases by the broad "lysosomal storage disease" label rather than by enzyme-specific target matching. The correct enzyme-replacement drug for Hurler syndrome would be **laronidase**, not imiglucerase.

This same category-level mismatch pattern recurs across the other four TxGNN-ranked candidates for this drug (Scheie syndrome, benign adrenal neoplasm, autosomal ichthyosis syndrome, and cholesteryl ester storage disease) — none of which share imiglucerase's specific GBA-targeted mechanism, and none have supporting clinical trial or literature evidence beyond general ERT review articles or nothing at all.

## Clinical Trial Evidence

Currently no related clinical trials registered

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [20534487](https://pubmed.ncbi.nlm.nih.gov/20534487/) | 2010 | Review | PNAS | General review of PET imaging for enzyme replacement therapy (ERT) across multiple lysosomal storage diseases, including Gaucher, Fabry, Hurler, Hunter, Maroteaux-Lamy, and Pompe; not specific to imiglucerase efficacy in Hurler syndrome |
| [21211680](https://pubmed.ncbi.nlm.nih.gov/21211680/) | 2010 | Review | La Revue de médecine interne | General review of ERT history for lysosomal storage diseases (alglucerase/imiglucerase for Gaucher disease, agalsidase for Fabry disease); does not report imiglucerase use in Hurler syndrome |

## Norway Market Information

Imiglucerase currently has no market authorizations recorded (Norway market status: Not marketed; 0 authorizations on file).

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked prediction (Hurler syndrome) and all four subsequent candidates lack a valid enzyme-level mechanistic link to imiglucerase's known mode of action, and are supported only by general ERT review literature (Tier 3) with no clinical trials — evidence level L4–L5 across the board. This pattern is consistent with a TxGNN false positive driven by broad disease-category clustering rather than target specificity.

**To proceed, the following is needed:**
- Confirmed drug MOA data from DrugBank (currently a data gap, severity: High)
- TFDA/regulatory label safety data — warnings and contraindications (currently a blocking data gap)
- Enzyme-specific target validation to rule out knowledge-graph category confounding (e.g., compare against laronidase, the IDUA-specific therapy actually indicated for Hurler syndrome)
- If pursued further, disease-specific (not general ERT) literature or preclinical data directly evaluating imiglucerase in MPS I models
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

