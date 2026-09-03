---
layout: default
title: Emtricitabine
parent: 僅模型預測 (L5)
nav_order: 130
evidence_level: L5
indication_count: 3
---

# Emtricitabine
{: .fs-9 }

證據等級: **L5** | 預測適應症: **3** 個
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

# Emtricitabine: From HIV-1 Infection to Feline Acquired Immunodeficiency Syndrome

## One-Sentence Summary

> Emtricitabine is a nucleoside reverse transcriptase inhibitor (NRTI) used as part of combination antiretroviral therapy for HIV-1 infection.
> The TxGNN model predicts it may be effective for **Feline Acquired Immunodeficiency Syndrome (FIV)**,
> with **4 clinical trials** and **1 publication** currently attached as supporting evidence — though only the publication directly studies the predicted (feline) indication; the trials are human HIV-1 studies of the drug's original use.

⚠️ **Important caveat**: The top-ranked predicted indication is a *veterinary* condition (feline AIDS caused by Feline Immunodeficiency Virus, FIV — a lentivirus related to but distinct from HIV). This likely reflects FIV/HIV similarity in the underlying knowledge graph rather than a human-indication signal. Rank 2 ("simian immunodeficiency virus infection") is also a non-human condition. Both should be interpreted as **mechanistic/model artifacts**, not ready-to-use human repurposing candidates.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not provided in structured data; based on established pharmacology, HIV-1 infection (antiretroviral therapy, typically combined with tenofovir) |
| Predicted New Indication | Feline Acquired Immunodeficiency Syndrome (FIV) — veterinary condition |
| TxGNN Prediction Score | 99.92% |
| Evidence Level | L4 (single preclinical/animal PK-outcomes study directly on-target; attached clinical trials are for the original human HIV-1 indication, not FIV) |
| Norway Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, emtricitabine is a cytidine-analog NRTI that inhibits HIV-1 reverse transcriptase, and it is a core component of first-line combination antiretroviral therapy (cART) for human HIV-1 infection.

Mechanistically, the predicted link to FIV is plausible: FIV is a lentivirus closely related to HIV, and NRTIs targeting reverse transcriptase can theoretically inhibit FIV replication in the same way they inhibit HIV. This is supported by the one directly relevant publication in the evidence pack, which evaluated emtricitabine as part of a cART regimen in FIV-infected domestic cats.

However, the four clinical trials listed under this "indication" are all human HIV-1 treatment-naive trials evaluating emtricitabine/tenofovir-containing regimens against comparator ART (dolutegravir, raltegravir, darunavir combinations) — they support emtricitabine's established human HIV-1 use, not the FIV indication itself. This distinction should be made explicit to any reviewer relying on this report, since counting them as "FIV evidence" would overstate the evidence base.

## Clinical Trial Evidence

*Note: the trials below evaluate emtricitabine in human HIV-1 infection (its established use), not the predicted feline indication. They are included as they appear in the evidence pack for indication rank 1.*

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT01263015](https://clinicaltrials.gov/study/NCT01263015) | Phase 3 | Completed | 844 | Dolutegravir + abacavir/lamivudine vs. Atripla (efavirenz/emtricitabine/tenofovir) in ART-naive HIV-1 adults, 96-week non-inferiority |
| [NCT01227824](https://clinicaltrials.gov/study/NCT01227824) | Phase 3 | Completed | 828 | Dolutegravir vs. raltegravir, both with fixed-dose dual NRTI (including emtricitabine/tenofovir), in ART-naive HIV-1 adults |
| [NCT02770508](https://clinicaltrials.gov/study/NCT02770508) | Phase 4 | Completed | 145 | Boosted darunavir + lamivudine vs. + emtricitabine/tenofovir or lamivudine/tenofovir in ART-naive HIV-1 patients |
| [NCT00951015](https://clinicaltrials.gov/study/NCT00951015) | Phase 2 | Completed | 208 | Dose-finding for dolutegravir with abacavir/lamivudine or tenofovir/emtricitabine in ART-naive HIV-1 adults |

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [37112803](https://pubmed.ncbi.nlm.nih.gov/37112803/) | 2023 | Preclinical (animal) | Viruses | Combination ART (dolutegravir, tenofovir, emtricitabine) evaluated for pharmacokinetics and clinical/immunophenotypic outcomes in FIV-infected domestic cats — the only study directly on the predicted indication |

## Norway Market Information

Emtricitabine currently holds no marketing authorization in Norway (0 licenses on record); no product/dosage-form data is available for this market.

## Safety Considerations

Please refer to the package insert for safety information. No structured warnings, contraindications, or drug interaction data were available in this evidence pack (DDI query returned no results).

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked predicted indication is a veterinary condition (feline AIDS/FIV), and the attached clinical trial evidence supports only the drug's existing human HIV-1 use rather than the new indication itself — leaving just one preclinical animal study as direct evidence. Combined with the absence of MOA, safety, and Norway market data, the evidence base is not sufficient to support a repurposing recommendation as-is.

**To proceed, the following is needed:**
- Clarify whether the TxGNN prediction is intended as a human-relevant signal (e.g., via FIV/HIV mechanistic homology) or should be excluded as a cross-species knowledge-graph artifact
- Obtain emtricitabine mechanism of action (MOA) data from DrugBank (DG002)
- Obtain formal product label warnings/contraindications/DDI data — currently a blocking gap for safety review (DG001)
- If pursuing a human repurposing angle, re-run evidence review against human-relevant indications (e.g., other lentivirus/retrovirus-related conditions) rather than the FIV-labeled node
- Confirm regulatory pathway options given the drug is not currently marketed in Norway
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

