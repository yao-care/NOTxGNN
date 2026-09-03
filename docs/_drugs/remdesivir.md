---
layout: default
title: Remdesivir
parent: 僅模型預測 (L5)
nav_order: 301
evidence_level: L5
indication_count: 6
---

# Remdesivir
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

Using the provided Evidence Pack, here is the evaluation report.

---

# Remdesivir: From COVID-19 (SARS-CoV-2 Infection) to Multiple Endocrine Neoplasia

## One-Sentence Summary

Remdesivir is a nucleotide-analog antiviral originally developed and clinically used against RNA viruses, most extensively documented in this evidence pack through large-scale COVID-19 (SARS-CoV-2) trials. The TxGNN model's top-ranked prediction is **Multiple Endocrine Neoplasia**, but this candidate is supported by **zero clinical trials** and **zero publications**, and the model's second-ranked candidate (HIV infection) turns out — on evidence review — to be built entirely on mislabeled COVID-19 trial data rather than genuine HIV evidence. Overall, this candidate set does not currently support a repurposing decision.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not documented in Taiwan regulatory filings (drug not marketed); clinical trial evidence in this pack consistently identifies remdesivir's established use as treatment of COVID-19 (SARS-CoV-2 infection) |
| Predicted New Indication | Multiple Endocrine Neoplasia |
| TxGNN Prediction Score | 99.50% |
| Evidence Level | L5 |
| Taiwan Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed, verified mechanism-of-action data for remdesivir is not available from DrugBank in this evidence pack (flagged as a High-severity data gap). Based on the repurposing rationale accompanying the predictions, remdesivir is a nucleotide analog that inhibits the viral RNA-dependent RNA polymerase (RdRp), the replication enzyme used by RNA viruses such as SARS-CoV-2 and Ebola virus.

Multiple Endocrine Neoplasia (MEN) is a hereditary tumor syndrome driven by germline mutations in genes such as *RET* and *MEN1*, with a pathophysiology centered on endocrine cell proliferation rather than viral replication. There is no known mechanistic pathway connecting RdRp inhibition to MEN pathogenesis, and no clinical trials or literature were retrieved to support this link. The evidence pack's own rationale explicitly characterizes this prediction as likely **graph-embedding noise** in the TxGNN knowledge graph rather than a biologically grounded signal.

A related pattern appears in the model's second-ranked prediction, HIV infection: although 23 clinical trials and 20 publications were retrieved, manual review shows nearly all of them are COVID-19/SARS-CoV-2 studies that were mismatched to the "HIV infectious disease" label in the source database, not genuine remdesivir-for-HIV evidence. This reinforces that this candidate set, as currently derived, does not represent a validated repurposing signal.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for the top-ranked predicted indication (Multiple Endocrine Neoplasia).

---

## Literature Evidence

Currently no related literature available for the top-ranked predicted indication (Multiple Endocrine Neoplasia).

---

## Other Predicted Indications Screened Out (Context)

The evidence pack included five additional candidates beyond the top rank. All were reviewed and rejected for the same reasons — mechanistic implausibility, absent evidence, or database mislabeling:

| Rank | Disease | Score | Evidence | Key Issue |
|------|---------|-------|----------|-----------|
| 2 | HIV infectious disease | 99.32% | 23 trials / 20 papers (all COVID-19-related) | Database mislabeling — no genuine HIV evidence; RdRp inhibitor does not target reverse transcriptase |
| 3 | Feline acquired immunodeficiency syndrome | 99.07% | None | Likely confusion with feline coronavirus (FIP) graph neighbors; FIV is a retrovirus, mechanism mismatch |
| 4 | Simian immunodeficiency virus infection | 99.07% | None | Retrovirus, same mechanism mismatch as HIV/FIV |
| 5 | Neurodevelopmental disorder (ataxic gait, absent speech, decreased white matter) | 99.03% | None | Rare genetic disorder, no plausible biological link to antiviral RdRp inhibition |
| 6 | Homozygous familial hypercholesterolemia | 99.03% | None | Lipid metabolism disorder (LDLR/APOB/PCSK9), no plausible link to antiviral mechanism |

All six candidates were assigned a **Hold** recommendation by the scoring system.

---

## Taiwan Market Information

Remdesivir is currently **not marketed** in Taiwan — no drug licenses are on file, so no approved indication text, dosage form, or authorization number is available for reference.

---

## Safety Considerations

Please refer to the package insert for safety information. TFDA-specific warnings and contraindications for remdesivir could not be retrieved in this evidence pack (flagged as a Blocking-severity data gap), and no drug-drug interaction records were found.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked predicted indication (Multiple Endocrine Neoplasia) has no supporting clinical trials, literature, or plausible mechanistic rationale (Evidence Level L5). The next most "evidenced" candidate (HIV) is an artifact of database mislabeling — the underlying trials and publications are almost entirely COVID-19 studies, not genuine HIV evidence. None of the six candidates in this evidence pack meet a bar sufficient for further clinical evaluation.

**To proceed, the following is needed:**
- TFDA package insert data (warnings, contraindications) — currently a Blocking data gap
- Verified mechanism-of-action data from DrugBank — currently a High-severity data gap
- Correction of disease-label mapping errors in the underlying trial/literature database (the HIV mislabeling should be flagged upstream so it does not recur in future candidate generation)
- If any future TxGNN run produces a mechanistically plausible RNA-virus-related indication for remdesivir, that candidate should be re-evaluated on its own merits
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

