---
layout: default
title: Lamivudine
parent: 僅模型預測 (L5)
nav_order: 197
evidence_level: L5
indication_count: 5
---

# Lamivudine
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

# Lamivudine: From Antiretroviral Therapy to Feline Acquired Immunodeficiency Syndrome

## One-Sentence Summary

> Lamivudine (3TC) is a nucleoside reverse transcriptase inhibitor publicly known for treating HIV-1 and chronic hepatitis B, though this evidence pack does not itself document the original indication (flagged as a data gap).
> The TxGNN model's top-ranked prediction is **Feline Acquired Immunodeficiency Syndrome** — a disease that occurs only in cats, not humans —
> supported by **5 clinical trials** (all actually about human HIV-1, not feline disease) and **5 publications** (all in vitro/animal studies in cats).
> This is not a viable human repurposing candidate; it reflects a species-mismatch artifact in the prediction pipeline.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not documented in this evidence pack (`original_indications` empty, `original_moa` flagged as Data Gap DG002). Lamivudine is publicly known as an NRTI antiretroviral for HIV-1/chronic hepatitis B, but this is not sourced from the pack. |
| Predicted New Indication | Feline Acquired Immunodeficiency Syndrome (FIV infection in cats) |
| TxGNN Prediction Score | 99.93% (rank 1070) |
| Evidence Level | L4 (preclinical/animal studies only; no human clinical evidence for this indication exists or can exist) |
| Norway Market Status | 未上市 (Not marketed) |
| Number of Authorizations | 0 |
| Recommended Decision | **Hold** |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this evidence pack (DG002). Based on public pharmacological knowledge, lamivudine inhibits retroviral reverse transcriptase and is used in humans against HIV-1 and hepatitis B virus.

The mechanistic logic behind this prediction is real: Feline Immunodeficiency Virus (FIV) is a lentivirus closely related to HIV, and lamivudine (often combined with zidovudine) has been studied experimentally in cats as a veterinary analog of human antiretroviral therapy. This is a well-established use of the HIV/FIV animal model in retrovirology research.

However, **"feline acquired immunodeficiency syndrome" is a disease of domestic cats, not humans**, and cannot be pursued as a human drug repurposing indication through any regulatory pathway. The high TxGNN score most likely reflects the drug's genuine antiretroviral mechanism being correctly linked to a lentiviral disease in the knowledge graph, without a species filter. This candidate should be treated as a research/veterinary-pharmacology curiosity rather than a human indication for repurposing evaluation.

---

## Clinical Trial Evidence

⚠ Note: none of the trials below actually study feline AIDS (impossible in a human trial). They are lamivudine/HIV-1 trials in humans that were retrieved by drug-name match, not disease match, and do not constitute evidence for the predicted indication.

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT01499199](https://clinicaltrials.gov/study/NCT01499199) | Phase 3 | Completed | 13 | Dolutegravir + abacavir/lamivudine in ART-naive HIV-1 adults; CNS/plasma PK over 96 weeks |
| [NCT01263015](https://clinicaltrials.gov/study/NCT01263015) | Phase 3 | Completed | 844 | Dolutegravir + abacavir/lamivudine vs Atripla in ART-naive HIV-1 adults, non-inferiority over 96 weeks |
| [NCT00951015](https://clinicaltrials.gov/study/NCT00951015) | Phase 2 | Completed | 208 | Dose-selection of dolutegravir with abacavir/lamivudine or tenofovir/emtricitabine in ART-naive HIV-1 adults |
| [NCT02770508](https://clinicaltrials.gov/study/NCT02770508) | Phase 4 | Completed | 145 | Boosted darunavir + lamivudine vs darunavir + emtricitabine/tenofovir or lamivudine/tenofovir in naive HIV-1 patients |
| [NCT01227824](https://clinicaltrials.gov/study/NCT01227824) | Phase 3 | Completed | 828 | Dolutegravir vs raltegravir, both with dual NRTI backbone (ABC/3TC or TDF/FTC), in ART-naive HIV-1 adults |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [22816032](https://pubmed.ncbi.nlm.nih.gov/22816032/) | 2012 | Animal study | Viruses | Evaluated ZDV, ZDV+IFN-α, ZDV+lamivudine, and ZDV+valproic acid in naturally FIV-infected cats over 1 year |
| [25855689](https://pubmed.ncbi.nlm.nih.gov/25855689/) | 2016 | Case series (animal) | J Feline Med Surg | Long-term antiretroviral therapy follow-up in FIV-infected domestic cats |
| [11943320](https://pubmed.ncbi.nlm.nih.gov/11943320/) | 2002 | In vitro/in vivo | Vet Immunol Immunopathol | AZT/3TC combination showed additive-to-synergistic anti-FIV activity in PBMCs |
| [11684314](https://pubmed.ncbi.nlm.nih.gov/11684314/) | 2002 | In vitro | Antiviral Res | Combined zidovudine/lamivudine/abacavir suppressed FIV replication in vitro |
| [11327469](https://pubmed.ncbi.nlm.nih.gov/11327469/) | 2001 | In vitro | Am J Vet Res | Characterized 3TC-resistant FIV mutants and replication kinetics |

---

## Norway Market Information

Not marketed — 0 authorizations on record, no license entries available in the evidence pack.

---

## Safety Considerations

Please refer to the package insert for safety information. (All key warnings, contraindications, and DDI fields in this evidence pack are flagged as data gaps; TFDA/label data was not retrievable — see DG001, classified as a **Blocking** severity gap.)

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked TxGNN prediction (feline acquired immunodeficiency syndrome) is a veterinary disease with no human equivalent, so it cannot proceed through a human drug repurposing pathway regardless of prediction score. The clinical trial evidence attached to it is mismatched (human HIV trials, not FIV), and the literature is limited to in vitro/animal studies. Additionally, a Blocking-severity data gap (missing TFDA label/warnings) prevents any Stage 1 safety review even if a valid human indication were substituted.

**To proceed, the following is needed:**
- Re-run indication filtering to exclude non-human/veterinary disease terms from the candidate list
- Resolve DG001 (TFDA label/warnings) and DG002 (MOA) before evaluating any remaining candidate
- Note: ranks 2–5 in this same evidence pack (SIV infection, an ultra-rare neurodevelopmental disorder, an obsolete lipid disorder term, and a likely HBV/HCV mislabeling) were already independently assessed as **Hold** — this drug currently has no actionable repurposing candidate in the pack.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

