---
layout: default
title: Pretomanid
parent: 僅模型預測 (L5)
nav_order: 290
evidence_level: L5
indication_count: 5
---

# Pretomanid
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

# Pretomanid: From Tuberculosis to Candidiasis

## One-Sentence Summary

Pretomanid is a nitroimidazooxazine antimycobacterial developed for drug-resistant tuberculosis (used as part of the BPaL/BPaLM regimen with bedaquiline, linezolid, and moxifloxacin). The TxGNN model's top prediction suggests possible activity against **Candidiasis**, but this pairing has **zero supporting clinical trials or literature** and, per mechanistic review, lacks biological plausibility — Candida species do not possess the Ddn/F420 nitroreductase system that pretomanid requires for activation.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Drug-resistant pulmonary tuberculosis (BPaL/BPaLM regimen) — not present in Norway licensing data; drawn from literature context |
| Predicted New Indication | Candidiasis |
| TxGNN Prediction Score | 99.69% |
| Evidence Level | L5 (model prediction only, no clinical or literature evidence) |
| Norway Market Status | 未上市 (Not marketed) |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed DrugBank mechanism-of-action data is not available for pretomanid in this evidence pack. However, cross-referencing the supplied literature and mechanistic annotations shows that pretomanid is a nitroimidazooxazine (PA-824) that requires activation by the mycobacteria-specific **Ddn/F420 deazaflavin-dependent nitroreductase system** to generate its bactericidal effect. This activation pathway is unique to mycobacteria and is the basis for pretomanid's role in the BPaL regimen for extensively drug-resistant and treatment-intolerant multidrug-resistant TB.

Candidiasis is caused by *Candida* fungal species, which do not express the Ddn/F420 nitroreductase system. Nitroimidazole-class drugs are broadly known to lack antifungal activity through this mechanism. This means the TxGNN association is most likely driven by embedding similarity rather than any real pharmacological or clinical signal — consistent with the complete absence of clinical trials or publications linking pretomanid to candidiasis in this dataset.

For context, a biologically more plausible candidate in this dataset is **leprosy** (rank 2, *M. leprae*, same genus as *M. tuberculosis*), which shares the same nitroreductase activation pathway in theory. However, the strongest piece of direct evidence available (PMID 17005816, "*Mycobacterium leprae is naturally resistant to PA-824*") directly **refutes** efficacy — animal model data show no bactericidal activity against *M. leprae* despite the shared genus. This underscores that genus-level mechanistic similarity does not guarantee functional equivalence, and reinforces caution around the top-ranked candidiasis prediction as well.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Norway Market Information

Pretomanid is not currently marketed in Norway (0 authorizations on record). No product license, dosage form, or approved indication data is available.

---

## Safety Considerations

Structured safety data (warnings, contraindications, DDI) is not currently available for pretomanid in this evidence pack (TFDA label data collection is a blocking data gap — DG001).

One safety signal did surface indirectly through the mechanistic review across other candidate indications in this dataset: pretomanid carries a known **QT-interval prolongation risk**, a cardiac safety concern that should be factored into any future clinical development regardless of target indication.

Please refer to the package insert for complete safety information once available.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked prediction (candidiasis) has no clinical trial or literature support and lacks mechanistic plausibility, since *Candida* species do not possess the mycobacteria-specific nitroreductase activation pathway pretomanid depends on. The next-best candidate in this dataset (leprosy) does have a partially plausible shared-genus mechanism, but is directly contradicted by existing preclinical evidence showing *M. leprae* is naturally resistant to pretomanid (PA-824). No candidate in this evidence pack currently meets a bar for further development.

**To proceed, the following is needed:**
- TFDA label/warnings and contraindications data (DG001, blocking — required before any S1 safety screening)
- DrugBank-sourced detailed MOA data (DG002) to properly assess mechanistic overlap for future candidates
- If repurposing is still of interest, prioritize candidate diseases with an actual mycobacterial or nitroreductase-dependent pathogenesis rather than the current TxGNN top-ranked outputs
- Independent in vitro confirmation before considering any candidate in this list for further evaluation
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

