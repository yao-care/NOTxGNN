---
layout: default
title: Zidovudine
parent: 僅模型預測 (L5)
nav_order: 392
evidence_level: L5
indication_count: 6
---

# Zidovudine
{: .fs-9 }

證據等級: **L5** | 預測適應症: **6** 個
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

Using none of the specialized coding/debugging skills here — this is a direct content-generation task with a fully specified template, so I'll proceed straight to drafting the report.

# Zidovudine: From HIV/AIDS Antiretroviral Therapy to Feline Acquired Immunodeficiency Syndrome

## One-Sentence Summary

> Zidovudine (AZT/ZDV) is the original nucleoside reverse transcriptase inhibitor (NRTI), globally established as an antiretroviral for HIV/AIDS in humans — though this specific evidence pack contains no formal record of that original indication.
> The TxGNN model's top-ranked prediction is **feline acquired immunodeficiency syndrome (FIV/FAIDS)**, a veterinary (non-human) disease, supported only by **20 preclinical animal-model publications** and **zero clinical trials**.
> Because the top-scoring candidate is not a human indication, this signal is not actionable for human drug repurposing in its current form.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in source data (drug not locally marketed); zidovudine is internationally documented as the first NRTI antiretroviral for HIV/AIDS |
| Predicted New Indication | Feline Acquired Immunodeficiency Syndrome (veterinary indication — not applicable to human patients) |
| TxGNN Prediction Score | 99.96% |
| Evidence Level | L4 (preclinical/animal-model literature only; not translatable to human indication) |
| Norway Market Status | Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data is not available in this evidence pack (`original_moa`: Data Gap). Based on the extensive literature returned across all ranked indications, zidovudine is consistently described as a thymidine-analogue nucleoside reverse transcriptase inhibitor (NRTI) — it is phosphorylated intracellularly and incorporated by retroviral reverse transcriptase, terminating proviral DNA synthesis. This mechanism is species-agnostic at the enzyme level, which explains why the drug shows anti-retroviral activity not only against HIV-1 in humans but also against related lentiviruses in other species.

This mechanistic non-specificity is exactly why the top two TxGNN predictions — **feline acquired immunodeficiency syndrome** (rank 1, score 0.9996) and **simian immunodeficiency virus infection** (rank 2, nearly identical score 0.9996) — score so highly: the knowledge graph links zidovudine to these entities through decades of comparative-virology literature in which cats and macaques were used as *experimental animal models* for HIV/AIDS drug development, not because zidovudine is a clinically indicated therapy for pet or primate disease. In other words, the model is picking up literature co-occurrence from preclinical model systems, not a genuine new human therapeutic opportunity.

By contrast, ranks 5 and 6 in this same evidence pack — **AIDS related complex** and **congenital human immunodeficiency virus** — are strongly supported by dozens of completed Phase 1–3 human trials (including the landmark ACTG 076 trial for perinatal transmission prevention) and are, in fact, *already established* human uses of zidovudine rather than novel repurposing candidates. Ranks 3 and 4 (a rare neurodevelopmental syndrome and "obsolete familial combined hyperlipidemia") have already been internally flagged with no mechanistic link, and for rank 4 the plausible relationship runs in the *opposite* direction — NRTI therapy is associated with lipodystrophy/dyslipidemia as an adverse effect, not a treatment benefit. Taken together, this candidate bundle illustrates a case where raw TxGNN ranking, without species and clinical-context filtering, surfaces model artifacts rather than viable repurposing signals.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for feline acquired immunodeficiency syndrome (as expected — this is a veterinary indication and would not appear in ClinicalTrials.gov/ICTRP for human subjects).

---

## Literature Evidence

All available literature for this indication consists of preclinical animal-model studies in domestic cats; none are human clinical trials, RCTs, or reviews.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [2475068](https://pubmed.ncbi.nlm.nih.gov/2475068/) | 1989 | Preclinical (feline model) | Antimicrob Agents Chemother | Established FIV as a model for AZT-based reverse-transcriptase-targeted chemotherapy for human AIDS |
| [3034403](https://pubmed.ncbi.nlm.nih.gov/3034403/) | 1987 | Preclinical (feline model) | Cancer Research | Early evaluation of AZT in FeLV-infected cats as a therapy/prophylaxis model for AIDS |
| [2178336](https://pubmed.ncbi.nlm.nih.gov/2178336/) | 1990 | Preclinical (feline model) | Antimicrob Agents Chemother | Interferon-alpha plus AZT evaluated in presymptomatic feline leukemia virus-induced AIDS (FAIDS) |
| [2163339](https://pubmed.ncbi.nlm.nih.gov/2163339/) | 1990 | Preclinical (feline model, toxicology) | Fundam Appl Toxicol | Dose-ranging toxicity study of AZT in FeLV-infected cats |
| [8381867](https://pubmed.ncbi.nlm.nih.gov/8381867/) | 1993 | Preclinical (feline model) | J Acquir Immune Defic Syndr | Prophylactic AZT reduced early viremia and lymphocyte decline but did not prevent primary FIV infection |
| [7688949](https://pubmed.ncbi.nlm.nih.gov/7688949/) | 1993 | Preclinical (feline model) | Arch Virol | AZT and cyclosporine reduced plasma (but not PBMC) FIV titers |
| [11943320](https://pubmed.ncbi.nlm.nih.gov/11943320/) | 2002 | Preclinical (feline model) | Vet Immunol Immunopathol | AZT/3TC combination showed additive-to-synergistic anti-FIV activity in vitro; questioned efficacy in chronic infection |
| [18550661](https://pubmed.ncbi.nlm.nih.gov/18550661/) | 2008 | Preclinical (feline model, genetics) | J Virol | Phylogenetic analysis of FIV genes in cats undergoing AZT treatment vs. treatment-naïve cats |
| [22816032](https://pubmed.ncbi.nlm.nih.gov/22816032/) | 2012 | Preclinical (feline model) | Viruses | Compared AZT alone vs. AZT combinations (IFN-α, 3TC, valproic acid) in naturally FIV-infected cats over one year |
| [25855689](https://pubmed.ncbi.nlm.nih.gov/25855689/) | 2016 | Preclinical (feline model, long-term) | J Feline Med Surg | Long-term (5–6 year) follow-up of AZT-based antiretroviral therapy in FIV-infected cats |

---

## Norway Market Information

This drug currently has no authorizations on file for this market (`market_status`: Not Marketed; `total_licenses`: 0). No product listings are available to summarize.

---

## Safety Considerations

Please refer to the package insert for safety information. No structured warnings, contraindications, or drug-interaction data are currently available in the evidence pack (`key_warnings`, `contraindications`, and DDI queries all returned no data). This is flagged as a **Blocking** data gap (DG001) — official label/monograph data must be sourced before this candidate can proceed through initial safety screening (S1).

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The highest-ranked TxGNN prediction (feline acquired immunodeficiency syndrome) is a veterinary, non-human indication with no clinical trial evidence and only preclinical animal-model literature — it is not actionable as a human drug repurposing candidate. Combined with a Blocking safety data gap (no label/warnings data) and the drug's absence from the local market, there is insufficient basis to advance.

**To proceed, the following is needed:**
- Official product label / TFDA-equivalent monograph data (warnings, contraindications, DDIs) to close the Blocking data gap (DG001)
- Confirmed mechanism-of-action documentation (DG002)
- Species/entity filtering on TxGNN outputs to exclude non-human disease terms before ranking is presented for human repurposing review
- If pursued further, reassessment should focus on the lower-ranked but clinically grounded signals in this pack (AIDS related complex, congenital HIV infection) — noting these reflect zidovudine's *already established* human use rather than a novel repurposing opportunity, so they would not qualify as new indications either
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

