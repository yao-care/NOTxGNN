---
layout: default
title: Bictegravir
parent: 僅模型預測 (L5)
nav_order: 53
evidence_level: L5
indication_count: 3
---

# Bictegravir
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

Using the provided Evidence Pack, here is the drug repurposing evaluation report. Note: `taiwan_regulatory` data (not Norway) was used for the market-status sections, since the underlying dataset is Taiwan-specific (TFDA, "TW-DB11799").

---

# Bictegravir: From HIV-1 Infection to Feline Acquired Immunodeficiency Syndrome

## One-Sentence Summary

> Bictegravir (as part of the fixed-dose combination Biktarvy) is an integrase strand transfer inhibitor internationally used for HIV-1 infection, though it is not currently registered in Taiwan and drug-level indication/MOA data are not available in this evidence pack.
> The TxGNN model predicts it may be effective for **Feline Acquired Immunodeficiency Syndrome**,
> but this top-ranked prediction currently has **no supporting clinical trials or literature** — evidence exists only for a closely related, similarly-scored prediction (simian immunodeficiency virus infection).

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available in Taiwan regulatory data (no licenses on file); internationally, bictegravir is used for HIV-1 infection as part of Biktarvy |
| Predicted New Indication | Feline Acquired Immunodeficiency Syndrome |
| TxGNN Prediction Score | 99.82% |
| Evidence Level | L5 (model prediction only, no clinical trials or literature identified) |
| Taiwan Market Status | Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available (blocking data gap, DG002). Based on known pharmacology, bictegravir is an HIV-1 **integrase strand transfer inhibitor (INSTI)**, marketed internationally as a component of Biktarvy (bictegravir/emtricitabine/tenofovir alafenamide) for HIV-1 infection. It is not currently registered or marketed in Taiwan.

The top-ranked predicted indication, feline acquired immunodeficiency syndrome, is caused by feline immunodeficiency virus (FIV) — a lentivirus structurally and mechanistically related to HIV, also dependent on a viral integrase to insert its genome into host DNA. This provides a plausible mechanistic rationale (cross-lentivirus integrase inhibition) for the TxGNN prediction, even though no dedicated FIV/veterinary study data exists to confirm it.

Notably, a second, equally-scored prediction — simian immunodeficiency virus (SIV) infection — is supported by actual literature (see below) describing bictegravir's *in vitro* antiviral activity against SIV and INSTI-resistant HIV-1 strains in nonhuman primate models. While SIV infection is not a human clinical indication, this literature strengthens the underlying biological plausibility that bictegravir's integrase-inhibition mechanism extends across related lentiviruses, indirectly supporting (but not proving) the feline AIDS prediction. Both predicted indications are non-human/veterinary in nature, which is an important caveat for a human drug repurposing evaluation.

---

## Clinical Trial Evidence

Currently no related clinical trials registered

---

## Literature Evidence

Currently no related literature available for the top-ranked prediction (feline acquired immunodeficiency syndrome).

*For context, the closely related, equally-scored prediction ("simian immunodeficiency virus infection," rank 2) is supported by 3 publications on bictegravir's antiviral activity against SIV/HIV-1 integrase-inhibitor-resistant strains (PMID [28923862](https://pubmed.ncbi.nlm.nih.gov/28923862/), [32506843](https://pubmed.ncbi.nlm.nih.gov/32506843/), [39559349](https://pubmed.ncbi.nlm.nih.gov/39559349/)), all preclinical/mechanistic in nature — none are human RCTs.*

---

## Taiwan Market Information

Bictegravir is not currently marketed in Taiwan; no authorization records are available.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked prediction (feline acquired immunodeficiency syndrome) has zero supporting clinical trials or literature (L5), targets a non-human/veterinary condition rather than a human indication, and the drug carries a blocking data gap on TFDA warnings/contraindications (DG001) plus a high-impact MOA data gap (DG002) — together insufficient to support any human repurposing decision.

**To proceed, the following is needed:**
- TFDA label data (warnings, contraindications) to clear the blocking safety data gap
- Confirmed MOA data from DrugBank
- Clarification of whether a human-relevant analog indication exists (e.g., retroviral/lentiviral disease in humans), since current top predictions are veterinary/nonhuman
- If pursuing the feline AIDS or SIV angle, this would need to be reframed as a veterinary drug repurposing evaluation rather than a human one
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

