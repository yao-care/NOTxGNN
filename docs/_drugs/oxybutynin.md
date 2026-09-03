---
layout: default
title: Oxybutynin
parent: 僅模型預測 (L5)
nav_order: 258
evidence_level: L5
indication_count: 3
---

# Oxybutynin
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

# Oxybutynin: From Overactive Bladder to Restless Legs Syndrome

## One-Sentence Summary

> Oxybutynin is an M3 muscarinic receptor antagonist whose established antispasmodic action targets bladder detrusor smooth muscle (consistent with its classic use in overactive bladder/urinary incontinence).
> TxGNN's top-ranked prediction for this compound is **Restless Legs Syndrome**, but this candidate has **zero clinical trials and zero literature citations**, and the model's own mechanistic rationale explicitly states there is no known biological link between anticholinergic activity and RLS pathophysiology.
> Two lower-ranked candidates (gastroduodenitis, peptic ulcer disease) were also evaluated in this pack — only peptic ulcer disease has any supporting literature, and it consists solely of pre-1990 case reports and reviews predating modern PPI/H2-blocker therapy.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Overactive bladder / urinary incontinence (inferred from M3-antagonist mechanism described in the evidence; formal approved-indication text unavailable — drug is not marketed) |
| Predicted New Indication | Restless Legs Syndrome |
| TxGNN Prediction Score | 99.74% |
| Evidence Level | L5 (model prediction only — no clinical trials or literature) |
| Norway Market Status | Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

### Other Predicted Indications in This Pack

| Rank | Disease | TxGNN Score | Evidence Level | Decision |
|------|---------|-------------|-----------------|----------|
| 2 | Gastroduodenitis | 99.62% | L5 (no trials/literature) | Hold |
| 3 | Peptic ulcer disease | 99.31% | L3 (3 historical publications, no trials) | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data for oxybutynin is marked as a data gap in this pack, but the evidence itself describes oxybutynin as an M3 muscarinic receptor antagonist with antispasmodic/anticholinergic activity, acting primarily on bladder detrusor smooth muscle — consistent with its well-known original use in overactive bladder.

For the top-ranked candidate, **Restless Legs Syndrome**, the model's own rationale states there is **no plausible mechanistic link**: RLS pathophysiology is driven by central dopaminergic dysfunction and iron metabolism abnormalities, neither of which intersects with peripheral/central anticholinergic activity. The high TxGNN score here reflects graph-embedding similarity rather than biological plausibility, and is not corroborated by any clinical trial or publication.

The third-ranked candidate, **peptic ulcer disease**, has a more coherent (though outdated) mechanistic story: anticholinergic agents were historically used to reduce vagally-mediated gastric acid secretion and GI smooth muscle spasm — a rationale that predates H2-blockers and PPIs, which have since become standard of care and are far more targeted at the actual etiologies of PUD (H. pylori, NSAID use). Notably, one case report in the evidence (PMID 2360335) documents oxybutynin-induced reflux esophagitis via lower esophageal sphincter relaxation — a mechanism that could plausibly **worsen** GERD, a common PUD comorbidity, rather than help it.

---

## Clinical Trial Evidence

*(Restless Legs Syndrome — top-ranked candidate)*

Currently no related clinical trials registered.

---

## Literature Evidence

*(Restless Legs Syndrome — top-ranked candidate)*

Currently no related literature available.

### Supporting Literature for Peptic Ulcer Disease (Rank 3 Candidate)

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [14173506](https://pubmed.ncbi.nlm.nih.gov/14173506/) | 1964 | Cohort/Clinical Evaluation | Curr Ther Res Clin Exp | Early clinical evaluation of oxybutynin chloride in gastrointestinal disease |
| [4380481](https://pubmed.ncbi.nlm.nih.gov/4380481/) | 1965 | Review | Arch Int Pharmacodyn Ther | Characterizes oxybutynin as a musculotropic antispasmodic with moderate anticholinergic action |
| [2360335](https://pubmed.ncbi.nlm.nih.gov/2360335/) | 1990 | Case Report | DICP | Reports oxybutynin-induced reflux esophagitis via reduced lower esophageal sphincter tone — a potential contraindication signal for GI use |

No literature was returned for the gastroduodenitis candidate (Rank 2).

---

## Norway Market Information

This drug is currently **not marketed** on the market covered by this dataset. No authorization/license records are available (`total_licenses = 0`).

---

## Safety Considerations

Please refer to the package insert for safety information. This pack flags TFDA-equivalent label warnings/contraindications as a **Blocking data gap (DG001)** — this must be resolved before any S1 safety assessment can proceed.

Separately, the literature review above (PMID 2360335) surfaced a specific adverse-effect signal relevant to GI repurposing candidates: oxybutynin can induce reflux esophagitis via LES relaxation, which is a mechanistic concern for the peptic ulcer disease candidate specifically.

---

## Conclusion and Next Steps

**Decision: Hold** (all three candidates in this pack)

**Rationale:**
- The top-ranked candidate (RLS, 99.74%) has no clinical trials, no literature, and no biological plausibility per the model's own rationale — this is a pure graph-similarity artifact, not a repurposing signal.
- The peptic ulcer disease candidate has some historical evidence (L3) but it predates modern PUD standard-of-care and carries a plausible aggravation risk (reflux esophagitis) rather than a therapeutic benefit.
- The drug is not marketed in this jurisdiction, and TFDA-equivalent label/safety data is a **Blocking** gap (DG001), so no candidate here can advance past S0/S1 regardless of prediction score.

**To proceed, the following is needed:**
- Resolve DG001 (label warnings/contraindications) via TFDA-equivalent regulatory source — blocking for any further evaluation
- Resolve DG002 (confirmed MOA via DrugBank API) to validate or refute mechanistic rationale for any candidate
- If RLS is to be pursued further, independent literature/trial search is required — this pack currently contains none
- Re-evaluate peptic ulcer disease only if modern comparative evidence (vs. PPI/H2-blocker) emerges; current evidence is insufficient and carries a competing safety signal
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

