---
layout: default
title: Interferon Beta-1B
parent: 僅模型預測 (L5)
nav_order: 189
evidence_level: L5
indication_count: 2
---

# Interferon Beta-1B
{: .fs-9 }

證據等級: **L5** | 預測適應症: **2** 個
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

Using the drug-repurposing evaluation report format to produce the Norway-market evidence pack report for Interferon Beta-1b.

# Interferon Beta-1b: From Multiple Sclerosis (Established Use) to Hairy Cell Leukemia

## One-Sentence Summary

> Interferon beta-1b is a Type I interferon whose established clinical use — per the mechanistic evidence in this pack — is in multiple sclerosis; formal regulatory records for original indication and market authorization are not available in this dataset.
> The TxGNN model predicts a repurposing signal for **Hairy Cell Leukemia**,
> currently supported by **0 registered clinical trials** and **4 older publications (1987–1990)**, with no Norway market presence on file.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available in regulatory dataset (0 licenses on file; see Data Gap DG001) |
| Predicted New Indication | Hairy Cell Leukemia |
| TxGNN Prediction Score | 99.16% |
| Evidence Level | L3 |
| Norway Market Status | Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data for this drug is currently not available (Data Gap DG002). Based on the mechanistic rationale supplied with this evidence pack, interferon beta-1b is a Type I interferon (IFN-β) with antiproliferative and immune-modulatory activity, signaling through the IFNAR receptor pathway. It belongs to the same Type I interferon family as interferon alpha, which is an already-established treatment for hairy cell leukemia.

The rationale for this prediction rests on drug-class analogy rather than a direct indication overlap: because IFN-α and IFN-β share the same receptor and downstream antiproliferative signaling in lymphoid/myeloid precursor cells, IFN-β-1b's activity against hairy cell leukemia has biological plausibility. This is corroborated by older clinical literature (1987–1990) directly testing IFN-β-ser in hairy cell leukemia patients, some of whom had failed or preceded standard alpha-interferon therapy.

However, this body of evidence predates modern standard-of-care agents for hairy cell leukemia (e.g., purine analogues such as cladribine/pentostatin), and no clinical trials have been registered on ClinicalTrials.gov to re-confirm this signal in a contemporary setting. The prediction should therefore be read as a plausible, mechanistically grounded hypothesis rather than a validated repurposing pathway.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [2736487](https://pubmed.ncbi.nlm.nih.gov/2736487/) | 1989 | Prospective comparative study | Cancer | 10 HCL patients treated with recombinant IFN-β-ser (90×10⁶ U SC, 3x/week); 63% normalized peripheral blood counts, 25% partial hematologic improvement, compared prospectively with IFN-α outcomes. |
| [2198792](https://pubmed.ncbi.nlm.nih.gov/2198792/) | 1990 | Case series (post-IFN failure) | American Journal of Clinical Oncology | 3 HCL patients who failed IFN-α or IFN-β achieved complete response with pentostatin (DCF), demonstrating a salvage option after IFN-β failure. |
| [2082943](https://pubmed.ncbi.nlm.nih.gov/2082943/) | 1990 | Case series/small trial | American Journal of Hematology | 12 heavily pretreated HCL patients (90–100% marrow hairy cells) treated with IV beta-ser IFN 90 MU 3x/week; describes dosing and tolerability. |
| [3312839](https://pubmed.ncbi.nlm.nih.gov/3312839/) | 1987 | Retrospective cohort/experience | Leukemia | UCLA experience across 51 HCL patients on type I IFN trials; hematologic improvement in ~71% of patients starting recombinant beta-ser-IFN, comparable to alpha-IFN response rates. |

---

## Norway Market Information

This product currently has no authorization records on file in Norway (0 licenses; market status: Not Marketed).

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Additional Signal (Supplementary): Autoimmune Disease of the Central Nervous System

Separately from the primary repurposing candidate above, this evidence pack also contains a second, much stronger-evidence prediction for interferon beta-1b: **autoimmune disease of central nervous system** (TxGNN score 99.02%), supported by **24 clinical trials** (including multiple completed Phase 3/Phase 4 studies such as BENEFIT and BENEFIT 11, n=278–2,878) and **18 publications**, including a Cochrane network meta-analysis. Evidence level is **L1**, decision stage **S3**, with a pack-recommended decision of **Proceed with Guardrails**.

This signal is consistent with interferon beta-1b's mechanistic rationale of modulating Th1/Th17–Treg balance and inhibiting T-cell migration across the blood–brain barrier — the established mode of action in multiple sclerosis — and most likely reflects confirmation of an already well-established therapeutic use rather than a novel repurposing opportunity. It is noted here for completeness but is not the subject of this report's primary Go/Hold decision, since it does not represent a new indication.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The hairy cell leukemia signal rests entirely on small, decades-old (1987–1990) case series and cohort literature with no registered clinical trials and no evidence generated against modern standard-of-care comparators. Combined with the L3 evidence level and "Research Question" stage flagged in the source data, the evidence is insufficient to justify proceeding at this time.

**To proceed, the following is needed:**
- TFDA/Norway package insert data — warnings, contraindications, DDI (Data Gap DG001, currently blocking safety screening)
- Confirmed mechanism-of-action documentation (Data Gap DG002)
- Contemporary clinical trial data for interferon beta-1b in hairy cell leukemia, ideally benchmarked against purine analogue therapy
- Route-of-administration compatibility assessment (currently "pending" in the evidence pack)
- Confirmation of original approved indication(s) and market history, which are currently absent from the regulatory dataset
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

