---
layout: default
title: Letermovir
parent: 僅模型預測 (L5)
nav_order: 205
evidence_level: L5
indication_count: 1
---

# Letermovir
{: .fs-9 }

證據等級: **L5** | 預測適應症: **1** 個
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

# Letermovir: From Cytomegalovirus (CMV) Infection to Vulvovaginal Candidiasis

## One-Sentence Summary

Letermovir is a CMV DNA terminase complex inhibitor, known for its antiviral activity against cytomegalovirus infection. The TxGNN model predicts it may be effective for **Vulvovaginal Candidiasis**, but this prediction is currently supported by **0 clinical trials** and **0 publications**, and the underlying mechanistic rationale argues against biological plausibility.

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Not available in evidence pack (no license/indication text on file — see data gap DG002) |
| Predicted New Indication | Vulvovaginal Candidiasis |
| TxGNN Prediction Score | 99.88% |
| Evidence Level | L5 |
| Norway Market Status | ✗ Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed formal mechanism-of-action data is not available in this evidence pack (data gap DG002, High severity). However, the evidence pack's own mechanistic analysis indicates that letermovir acts as a **CMV DNA terminase complex inhibitor**, targeting the pUL51/pUL56/pUL89 viral packaging complex — a mechanism specific to the Herpesviridae family and consistent with its known role in CMV prophylaxis/treatment.

This mechanism has no known relationship to the pathways relevant to vulvovaginal candidiasis, which is a fungal (Candida) infection driven by cell wall/cell membrane synthesis, the ergosterol pathway, and CYP51-related targets. No in vitro or in vivo antifungal activity has been reported for letermovir in any available source.

Given this lack of biological plausibility, the very high TxGNN prediction score (99.88%) is most likely attributable to indirect knowledge-graph connections or relational noise rather than a genuine pharmacological signal. This prediction should be treated with significant caution and is not currently corroborated by any independent clinical or literature evidence.

## Clinical Trial Evidence

Currently no related clinical trials registered

## Literature Evidence

Currently no related literature available

## Norway Market Information

Letermovir is not currently marketed in Norway. No authorizations, product listings, or approved-indication text are on file (`total_licenses: 0`).

## Safety Considerations

Please refer to the package insert for safety information. (TFDA-equivalent label warnings/contraindications are flagged as a **Blocking** data gap — DG001 — and drug interaction data was not found in this evidence pack.)

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
There is no clinical trial or literature evidence supporting letermovir for vulvovaginal candidiasis, and the mechanistic rationale provided actively argues against biological plausibility (antiviral terminase inhibitor vs. antifungal target pathways). Combined with a blocking safety data gap (DG001) and the drug's current unmarketed status in Norway, this candidate does not meet the threshold to advance.

**To proceed, the following is needed:**
- Resolve DG001 (TFDA-equivalent label warnings/contraindications) — currently blocking any S1 safety review
- Resolve DG002 (formal DrugBank MOA confirmation) to validate or refute the mechanistic rationale
- Any preclinical (in vitro antifungal susceptibility) or case-level evidence to establish biological plausibility before further evaluation
- Re-screen this prediction against TxGNN model confidence calibration, given the apparent mechanistic mismatch
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

