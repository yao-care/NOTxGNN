---
layout: default
title: Tipranavir
parent: 僅模型預測 (L5)
nav_order: 357
evidence_level: L5
indication_count: 10
---

# Tipranavir
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

# Tipranavir: From HIV-1 Infection to Feline Acquired Immunodeficiency Syndrome

## One-Sentence Summary

> Tipranavir (DB00932) is publicly known as a non-peptidic HIV-1 protease inhibitor, though the evidence pack itself contains a data gap for both the original indication and mechanism of action.
> The TxGNN model's top-ranked prediction is **Feline Acquired Immunodeficiency Syndrome (FIV)**, a veterinary disease — this is **not a viable human indication** and reflects a species-specificity artifact in the knowledge graph rather than a genuine repurposing signal.
> No clinical trials or literature directly support this top prediction; the only substantively evidenced candidates (ranked #5–#6) are simply restatements of tipranavir's already-known HIV/AIDS indication, not new indications.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available in dataset (data gap — no `approved_indication_text` on file; tipranavir is publicly known as an HIV-1 protease inhibitor for treatment-experienced patients) |
| Predicted New Indication | Feline Acquired Immunodeficiency Syndrome (veterinary; not human-applicable) |
| TxGNN Prediction Score | 99.99% |
| Evidence Level | L5 |
| Norway Market Status | Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data is not available in this evidence pack (flagged as a Blocking/High-severity data gap, DG001/DG002). Based on publicly known pharmacology referenced consistently throughout the evidence pack's own rationale text, tipranavir is a non-peptidic HIV-1 protease inhibitor that blocks cleavage of the viral Gag-Pol polyprotein, historically indicated for treatment-experienced HIV-1 infected adults.

The top-ranked prediction, feline acquired immunodeficiency syndrome (FIV), scores extremely high in TxGNN but is a **veterinary, species-specific disease**. The similarity driving this score is a structural homology between HIV-1 and lentiviral (FIV) proteases — a known graph-embedding artifact where the model conflates cross-species protease homology with therapeutic relevance. This pathway has no human clinical development route and should not be interpreted as a genuine repurposing opportunity. The same pattern explains ranks #2–#4 and #7–#10 (SIV infection, a rare neurodevelopmental disorder, an obsolete hyperlipidemia diagnosis, and several unrelated benign tumors): none have a plausible mechanistic link to protease inhibition, and several (e.g., hyperlipidemia) are mechanistically *contradicted* by tipranavir's known lipid-related adverse effect profile.

The only candidates with any substantive evidence base are ranked #5 ("AIDS related complex") and #6 ("congenital human immunodeficiency virus"), both scored L4/S1 ("Research Question"). However, these are not new indications — they are historical/pediatric classifications within HIV/AIDS, the disease area tipranavir is already known to treat. Rank #6's supporting trials are almost entirely for *other* antiretrovirals (cabotegravir, dolutegravir, rilpivirine) and provide only class-level, not drug-specific, support.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

*(Note: the top-ranked prediction, FIV, has no clinical trial evidence, as expected for a non-human disease. The more mechanistically coherent but non-novel candidate "congenital human immunodeficiency virus" has 9 associated trials, none specific to tipranavir — see rationale above.)*

---

## Literature Evidence

Currently no related literature available.

---

## Norway Market Information

Tipranavir is not currently marketed in Norway (`market_status: 未上市`) and has 0 registered authorizations. No license records are available for this evidence pack.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked TxGNN prediction (FIV) is a veterinary disease with no plausible human development pathway, and none of the remaining top-10 predictions constitute a credible, evidence-backed *new* human indication — the only scientifically coherent candidates (AIDS related complex, congenital HIV) simply restate tipranavir's known HIV/AIDS indication rather than reveal novel therapeutic potential. Combined with the Blocking-severity absence of TFDA/official label data, this candidate does not meet the bar to advance past S1 screening.

**To proceed, the following is needed:**
- Official label/monograph data (TFDA or equivalent) to resolve DG001 (warnings/contraindications) and DG002 (MOA)
- Confirmed original indication data to enable a valid MOA-to-new-indication comparison
- Re-run of TxGNN filtering to exclude non-human disease nodes and restatements of the drug's known indication before ranking is considered actionable
- If a genuinely novel indication is desired, evaluate lower-ranked candidates with independent mechanistic plausibility beyond protease-homology artifacts
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

