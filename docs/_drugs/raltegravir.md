---
layout: default
title: Raltegravir
parent: 僅模型預測 (L5)
nav_order: 292
evidence_level: L5
indication_count: 3
---

# Raltegravir
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

# Raltegravir: From HIV-1 Infection to Feline Acquired Immunodeficiency Syndrome

## One-Sentence Summary

> Raltegravir is an HIV-1 integrase strand transfer inhibitor (INSTI), originally studied and used for treating HIV-1 infection in humans.
> The TxGNN model predicts it may be effective for **Feline Acquired Immunodeficiency Syndrome**,
> but the **2 clinical trials** currently linked to this prediction are Phase 3 studies conducted in **human** HIV-1 patients, not in cats, and **no literature** specific to the feline indication was found.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | HIV-1 infection (inferred from linked trial descriptions; no formal `original_indications` or market-label text was provided in the evidence pack) |
| Predicted New Indication | Feline Acquired Immunodeficiency Syndrome |
| TxGNN Prediction Score | 99.78% |
| Evidence Level | L4 (the linked trials are mechanistic/analogous — human HIV-1 studies — not direct feline-indication studies) |
| Norway Market Status | Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available (marked as a High-severity data gap). Based on the clinical trial evidence linked to this candidate, raltegravir is described as an integrase strand transfer inhibitor (INSTI) used in combination antiretroviral regimens for HIV-1 infected patients — this is stated directly in the trial descriptions (e.g., "raltegravir (RAL) 400 mg twice daily" as background therapy for HIV-1 infected adults).

Mechanistically, the rationale for extending raltegravir to Feline Acquired Immunodeficiency Syndrome would rest on the fact that both HIV (in humans) and FIV-associated feline AIDS are caused by lentiviruses that depend on a viral integrase enzyme to insert proviral DNA into the host genome. An integrase inhibitor effective against HIV-1 integrase could, in principle, be evaluated against the analogous feline lentiviral integrase.

However, this rationale remains theoretical at this stage: the two Phase 3 trials attached as "evidence" for this indication (NCT01231516, NCT01227824) are actually human HIV-1 studies comparing raltegravir to dolutegravir — they do not involve cats or FIV. No feline-specific trial or publication was identified. The prediction should therefore be read as a cross-species mechanistic hypothesis rather than one currently backed by direct experimental or clinical data in the target species.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT01231516](https://clinicaltrials.gov/study/NCT01231516) | Phase 3 | Completed | 724 | Human HIV-1 study: dolutegravir 50mg QD vs. raltegravir 400mg BID, both with investigator-selected background regimen, in integrase-inhibitor-naïve, ART-experienced adults. Not a feline study. |
| [NCT01227824](https://clinicaltrials.gov/study/NCT01227824) | Phase 3 | Completed | 828 | Human HIV-1 study: dolutegravir 50mg QD vs. raltegravir 400mg BID with fixed-dose dual NRTI therapy in ART-naïve adults. Not a feline study. |

*Note: These trials establish raltegravir's antiviral efficacy against HIV-1 in humans but do not directly test the predicted feline indication.*

## Literature Evidence

Currently no related literature available.

## Norway Market Information

Raltegravir is not currently marketed in Norway; no market authorizations are on record in the evidence pack.

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The predicted indication (Feline Acquired Immunodeficiency Syndrome) targets a non-human species, and the only clinical trials currently linked to this candidate are human HIV-1 studies rather than feline-specific studies — direct relevance has not yet been established. Combined with a Blocking data gap on regulatory safety information and a High-severity gap on mechanism of action, there is insufficient basis to advance this candidate at this time.

**To proceed, the following is needed:**
- Verification of whether any preclinical or veterinary (FIV) in vitro/in vivo data exist for raltegravir, separate from the human HIV-1 trial evidence currently attached
- Package insert / SPC data to close the Blocking safety data gap (key warnings, contraindications, DDI)
- Detailed mechanism of action documentation from DrugBank
- Clarification of relevance grading for the linked trials and literature (currently marked "pending" in the evidence pack) to confirm whether the KG-derived indication mapping is a genuine signal or an ontology/text-matching artifact (e.g., "acquired immunodeficiency syndrome" string overlap between human and feline terms)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

