---
layout: default
title: Iloprost
parent: 僅模型預測 (L5)
nav_order: 176
evidence_level: L5
indication_count: 9
---

# Iloprost
{: .fs-9 }

證據等級: **L5** | 預測適應症: **9** 個
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

# Iloprost: From Pulmonary Arterial Hypertension to Hypotrichosis Simplex of the Scalp

## One-Sentence Summary

> Iloprost is a synthetic prostacyclin (PGI2) analogue with well-established global use in pulmonary arterial hypertension (PAH); it has never been marketed in Taiwan.
> The TxGNN model's top-ranked prediction is **Hypotrichosis Simplex of the Scalp**, a hereditary follicular keratinization disorder,
> but this signal is supported by **0 clinical trials** and **0 publications** — it is a pure model-embedding artifact with no biological rationale.
> Separately, this run also flagged several biologically coherent PAH-subtype expansions (see "Other Candidate Indications" below) that merit independent evaluation.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not on file in Taiwan evidence pack (drug unmarketed, 0 licenses); internationally, iloprost is indicated for pulmonary arterial hypertension (WHO Group 1) |
| Predicted New Indication | Hypotrichosis Simplex of the Scalp |
| TxGNN Prediction Score | 99.45% |
| Evidence Level | L5 |
| Taiwan Market Status | ✗ Not Marketed (未上市) |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available (data gap DG002 — MOA pending DrugBank query). Based on known pharmacological information, iloprost activates the prostacyclin IP receptor / cAMP pathway, producing vasodilation and inhibition of platelet aggregation. Clinically, this mechanism underlies its established use (outside Taiwan) in pulmonary arterial hypertension and, in some markets, critical limb ischemia.

Hypotrichosis simplex of the scalp is a hereditary disorder of hair follicle keratinization, associated with genes such as *APCDD1*, and its pathology is unrelated to vascular tone or platelet function. There is no known pathway connecting PGI2/IP-receptor signaling to this condition. This is reflected directly in the model's own rationale, which states the link is based purely on embedding similarity with "no biological support" (無生物學支持).

Notably, this same TxGNN run also predicted several pulmonary arterial hypertension subtypes for iloprost (associated with congenital heart disease, connective tissue disease, HIV infection, chronic hemolytic anemia, and schistosomiasis) — all mechanistically consistent with iloprost's known PGI2 pharmacology and, in some cases, backed by completed Phase 3 trial data. These represent materially stronger repurposing signals than the top-ranked hypotrichosis prediction (see "Other Candidate Indications" below).

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Taiwan Market Information

Iloprost is not currently marketed in Taiwan. No product authorizations are on file (0 licenses).

## Other Candidate Indications (Same Model Run)

For context, the same evidence pack scored 8 additional TxGNN predictions for iloprost. Unlike hypotrichosis, most of these fall within iloprost's established PAH pharmacology and carry meaningfully stronger evidence:

| Rank | Disease | TxGNN Score | Evidence Level | Recommendation | Key Support |
|------|---------|-------------|-----------------|-----------------|-------------|
| 6 | PAH associated with HIV infection | 99.21% | L1 | Proceed with Guardrails | Completed Phase 3 double-blind, placebo-controlled crossover RCT (NCT00709956, n=64) |
| 3 | PAH associated with congenital heart disease | 99.32% | L2 | Proceed with Guardrails | 1 trial (NCT01383083, n=42, status unknown) + 17 supporting publications |
| 5 | PAH associated with connective tissue disease | 99.21% | L2 | Proceed with Guardrails | Long-term IV iloprost cohort data (PMID 27651181) + 20 supporting publications |
| 7 | PAH associated with chronic hemolytic anemia | 99.21% | L4 | Research Question | Mechanistic plausibility only, no direct evidence |
| 8 | PAH associated with schistosomiasis | 99.21% | L4 | Research Question | 1 indirect pediatric case series |
| 4 | Pulmonary arteriovenous malformation | 99.31% | L4 | Hold | 1 indirect HHT-related case report |
| 2 | Congenital hypotrichosis milia | 99.33% | L5 | Hold | No evidence, no mechanistic link |
| 9 | Diffuse alopecia areata | 99.10% | L5 | Hold | No evidence, no mechanistic link |

If pursuing repurposing for iloprost, we recommend redirecting evaluation toward **PAH associated with HIV infection** (rank 6, L1) as the primary candidate, with congenital-heart-disease-PAH and connective-tissue-disease-PAH (rank 3 & 5, L2) as secondary candidates.

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked prediction, hypotrichosis simplex of the scalp, has no supporting clinical trials, no supporting literature, and no known biological mechanism connecting iloprost's prostacyclin pathway to this hereditary follicular disorder — this is a pure model-similarity artifact, not a credible repurposing signal.

**To proceed, the following is needed:**
- TFDA label warnings/contraindications data (DG001, blocking — required before any S1 safety screening)
- Confirmed mechanism of action from DrugBank (DG002)
- If repurposing interest continues, re-scope evaluation to the PAH-subtype candidates identified above (particularly HIV-associated PAH, L1 evidence), rather than hypotrichosis simplex
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

