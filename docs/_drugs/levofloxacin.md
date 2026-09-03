---
layout: default
title: Levofloxacin
parent: 僅模型預測 (L5)
nav_order: 208
evidence_level: L5
indication_count: 10
---

# Levofloxacin
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

# Levofloxacin: From Bacterial Infections to Punctate Epithelial Keratoconjunctivitis

## One-Sentence Summary

Levofloxacin is a broad-spectrum fluoroquinolone antibiotic originally developed for bacterial infections. The TxGNN model's top-ranked prediction suggests possible effectiveness for **Punctate Epithelial Keratoconjunctivitis**, but this direction is currently supported by only **1 publication** and **no clinical trials**, and the available literature describes a parasitic (not bacterial) etiology — so the mechanistic fit is questionable.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Bacterial infections (fluoroquinolone antibacterial class) — no Norway-specific indication text available |
| Predicted New Indication | Punctate Epithelial Keratoconjunctivitis |
| TxGNN Prediction Score | 99.92% |
| Evidence Level | L4 |
| Norway Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on general pharmacological knowledge, levofloxacin belongs to the fluoroquinolone antibiotic class, which inhibits bacterial DNA gyrase and topoisomerase IV. Its efficacy against a broad range of Gram-positive and Gram-negative bacterial infections — including ocular surface infections such as bacterial conjunctivitis and keratitis — is well established, which is the basis for the TxGNN model linking it to keratoconjunctivitis.

However, the single supporting publication for this prediction describes an **outbreak of microsporidial (parasitic) keratoconjunctivitis** linked to swimming-pool water contamination in Taiwan — not a bacterial pathogen. Levofloxacin has no established direct antiparasitic mechanism against microsporidia, so its applicability to this specific disease entity is mechanistically weak. The prediction likely reflects the model associating levofloxacin with "keratoconjunctivitis" as a disease category broadly (via its known ophthalmic antibacterial use) rather than a validated mechanism against this particular pathogen.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [30055152](https://pubmed.ncbi.nlm.nih.gov/30055152/) | 2018 | Outbreak Report/Case Series | American Journal of Ophthalmology | Describes an outbreak of microsporidial keratoconjunctivitis linked to contaminated swimming pool water in Taiwan; does not evaluate levofloxacin efficacy directly. |

---

## Norway Market Information

Levofloxacin is not currently marketed in Norway (0 active authorizations); no license or approved-indication data is available in this evidence pack.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The only literature support describes a parasitic (microsporidial) etiology rather than a bacterial one, so the mechanistic rationale for levofloxacin in this indication is weak. With no clinical trials and only a single non-interventional case series, the evidence base (L4) is insufficient to support further development.

**To proceed, the following is needed:**
- Confirmed mechanism of action data (currently a data gap)
- In vitro or preclinical evidence of levofloxacin activity against microsporidia specifically
- TFDA/regulatory label warnings and contraindications (currently a blocking data gap per meta.data_gaps)
- Additional literature or trial data directly evaluating levofloxacin treatment outcomes in keratoconjunctivitis

---

**Additional Note:** This evidence pack contains 10 TxGNN-predicted indications for levofloxacin. Two other candidates show materially stronger evidence than the top-ranked prediction above and may warrant separate evaluation:
- **Septicemic plague** (rank 9, L3, *Proceed with Guardrails*) — levofloxacin is FDA-approved for plague under the Animal Rule, backed by nonhuman primate efficacy data.
- **Monoclonal gammopathy** (rank 7, L2, *Research Question*) — supported by the TEAMM Phase 3 RCT and multiple cohort studies, though these evaluate levofloxacin as infection prophylaxis in multiple myeloma specifically, not treatment of monoclonal gammopathy broadly (including MGUS), so the disease-scope match needs clarification.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

