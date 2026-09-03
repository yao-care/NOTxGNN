---
layout: default
title: Tadalafil
parent: 僅模型預測 (L5)
nav_order: 336
evidence_level: L5
indication_count: 8
---

# Tadalafil
{: .fs-9 }

證據等級: **L5** | 預測適應症: **8** 個
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

# Tadalafil: From PDE5-Mediated Vascular Indications to Ambras Type Hypertrichosis Universalis Congenita — Evidence Insufficient

## One-Sentence Summary

> Tadalafil is a PDE5 (phosphodiesterase type 5) inhibitor whose established pharmacology acts on vascular smooth muscle and corpus cavernosum tissue, but no approved indication or MOA record is present in this evidence pack.
> The TxGNN model's top prediction — **Ambras type hypertrichosis universalis congenita** — has **no clinical trials and no supporting literature**, and the model's own rationale flags it as a likely embedding artifact rather than a biologically plausible signal.
> Across all 8 candidate indications screened, none reach a defensible evidence tier; the single most clinically relevant literature hit (a case report) actually describes tadalafil-*induced* migraine aura, i.e. an adverse effect, not a therapeutic signal.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in evidence pack (no approved indications on file); known PDE5-inhibitor pharmacology targets vascular smooth muscle / corpus cavernosum |
| Predicted New Indication | Ambras type hypertrichosis universalis congenita |
| TxGNN Prediction Score | 99.98% |
| Evidence Level | L5 |
| Norway Market Status | Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available (flagged as a Blocking/High-severity data gap in this pack). Based on the fragments available, tadalafil is known to act as a **PDE5 inhibitor**, with pharmacological effects on vascular smooth muscle and corpus cavernosum tissue — the mechanistic basis typically cited for tadalafil's established uses (erectile dysfunction, BPH, pulmonary arterial hypertension), though the specific original indication is not itself recorded in this evidence pack.

The top-ranked prediction, Ambras type hypertrichosis universalis congenita, is a rare congenital hair-growth disorder. There is no known or hypothesized pathway connecting PDE5/cGMP-mediated vasodilation to follicular growth regulation. The model's own rationale explicitly states this score reflects an "embedding similarity artifact" rather than a biologically grounded signal — a conclusion echoed for ranks #2, #4, #5, and #6 (hypertrichosis, Dandy-Walker–associated syndrome, hair shaft abnormality, trichomegaly), all of which score >99.6% with **zero clinical trials and zero literature** support.

Rank #3 (a periodontal/odontal malformation syndrome) initially looks better supported with 20 literature hits, but on inspection every article addresses general periodontal pathophysiology or treatment — **none mention tadalafil or PDE5 inhibitors at all**. This is disease-term co-occurrence noise, not drug-relevant evidence. Rank #7 (kyphoscoliotic heart disease) has a theoretically coherent hypothesis (PDE5 inhibitors are used in pulmonary hypertension, which can complicate kyphoscoliosis) but zero supporting trials or literature. Overall, no candidate in this pack clears even a preliminary mechanistic-plausibility bar with real-world evidence.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available for the top-ranked indication (Ambras type hypertrichosis universalis congenita).

---

## Norway Market Information

No marketing authorizations are on file for tadalafil in this evidence pack. Market status is recorded as **"Not marketed"** with **0 total licenses** and no dosage forms/routes listed.

---

## Other Candidate Indications Screened (Context)

Since this evidence pack evaluated 8 candidates for tadalafil, the table below summarizes why each was screened out, for completeness:

| Rank | Disease | TxGNN Score | Evidence | Verdict |
|------|---------|-------------|----------|---------|
| 2 | Hypertrichosis (disease) | 99.98% | None | No mechanistic link |
| 3 | Odontal/periodontal malformation syndrome | 99.97% | 20 papers, none drug-specific | Co-occurrence noise |
| 4 | Dandy-Walker malformation syndrome | 99.97% | None | No mechanistic link |
| 5 | Isolated genetic hair shaft abnormality | 99.96% | None | No mechanistic link |
| 6 | Familial isolated trichomegaly | 99.65% | None | No mechanistic link |
| 7 | Kyphoscoliotic heart disease | 99.43% | None | Theoretical PAH-overlap hypothesis only, unconfirmed |
| 8 | Migraine with brainstem aura | 99.08% | 1 case report ([PMID 17059442](https://pubmed.ncbi.nlm.nih.gov/17059442/)) | **Adverse-effect signal, not therapeutic evidence** — see Safety below |

---

## Safety Considerations

- **Key Warnings / Contraindications**: Not available in this evidence pack (TFDA/label data flagged as a Blocking data gap — DG001).
- **Drug Interactions**: No DDI data returned (query status: not found).
- **Literature-derived safety signal**: A case report ([PMID 17059442](https://pubmed.ncbi.nlm.nih.gov/17059442/), *Cephalalgia*, 2006) describes tadalafil-associated typical migraine aura without headache. This suggests PDE5-inhibitor–mediated cerebral vasodilation can *provoke* migraine-aura-like events — the opposite of a therapeutic effect for migraine, and worth noting as a precaution rather than a repurposing lead.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
All 8 candidate indications sit at Evidence Level L5 (or L4 for a single adverse-event case report), with `decision_stage: S0` and no clinical trial or drug-specific literature support. The highest-scoring predictions are explicitly flagged by the model's own rationale as embedding artifacts. No candidate in this pack meets the threshold to advance past initial screening.

**To proceed, the following is needed:**
- Resolve DG001 (Blocking): obtain TFDA/label warnings and contraindications — required before any S1 safety pre-assessment can begin.
- Resolve DG002 (High): obtain confirmed MOA and approved indications from DrugBank — required to establish a genuine mechanistic rationale for any candidate.
- If pursuing rank #7 (kyphoscoliotic heart disease / pulmonary hypertension overlap) further, commission a targeted literature search for tadalafil in kyphoscoliosis-associated pulmonary hypertension specifically, since the current pack found no drug-specific studies.
- No further action recommended on ranks #1–6, #8 without new experimental or clinical data — these are not viable repurposing leads based on current evidence.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

