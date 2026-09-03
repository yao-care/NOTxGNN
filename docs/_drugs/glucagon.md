---
layout: default
title: Glucagon
parent: 僅模型預測 (L5)
nav_order: 164
evidence_level: L5
indication_count: 1
---

# Glucagon
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

# Glucagon: TxGNN Signal for Irritable Bowel Syndrome — Evidence Mismatch Alert

## One-Sentence Summary

> Glucagon (DrugBank DB00040) has no original indication or mechanism-of-action data available in this evidence pack, and it is not currently marketed in Norway.
> TxGNN assigns it a **99.24%** score for **Irritable Bowel Syndrome (IBS)**, but nearly all of the supporting **11 clinical trials** and **20 publications** actually concern **GLP-1 receptor agonists** (liraglutide, ROSE-010, exendin-4) — a hormone that shares a gene family with glucagon but acts through a different receptor with the **opposite physiological effect**. This looks like a name-based confounding signal rather than a genuine repurposing opportunity.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not provided in evidence pack (no Norway license record; MOA data gap logged as DG002) |
| Predicted New Indication | Irritable Bowel Syndrome (IBS) |
| TxGNN Prediction Score | 99.24% |
| Evidence Level | L5 |
| Norway Market Status | Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism-of-action data for glucagon is not available (DG002). Based on general pharmacology, glucagon and GLP-1 (glucagon-like peptide-1) are both cleavage products of the same precursor, proglucagon, but they act on distinct receptors — GCGR for glucagon versus GLP-1R for GLP-1 — and produce **opposite metabolic effects**: glucagon raises blood glucose via hepatic glycogenolysis, while GLP-1 receptor agonists lower glucose, slow gastric emptying, and reduce gut motility.

Reviewing the actual evidence pack, **every clinical trial and nearly every publication supporting this prediction is about GLP-1 receptor agonists** (liraglutide, ROSE-010, exendin-4), not glucagon itself. The repurposing rationale field explicitly flags this as likely "name-based confounding" between the proglucagon gene family members. No trial or paper in this pack tests glucagon administration for IBS, and there is no mechanistic pathway proposed by which glucagon (a hyperglycemic hormone) would relieve IBS symptoms the way its receptor-opposite cousin GLP-1 does.

**In short: this is very likely a false-positive signal driven by shared naming/gene-family ancestry, not a valid drug repurposing lead for glucagon.**

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT05249023](https://clinicaltrials.gov/study/NCT05249023) | NA | Completed | 37 | Butyrate's role in colon health — no glucagon or GLP-1 link |
| [NCT03256266](https://clinicaltrials.gov/study/NCT03256266) | N/A | Active, not recruiting | 375 | Small intestinal organoid response to nutrients/agents — unrelated to glucagon |
| [NCT04763564](https://clinicaltrials.gov/study/NCT04763564) | Phase 2 | Terminated | 8 | Liraglutide (a GLP-1 agonist, **not glucagon**) in ileal pouch patients; trial terminated early with only 8 subjects |
| [NCT06333717](https://clinicaltrials.gov/study/NCT06333717) | NA | Completed | 33 | Whole grain rye bread effect on gut-brain axis — unrelated to glucagon |
| [NCT00802971](https://clinicaltrials.gov/study/NCT00802971) | NA | Completed | 12 | Fructo-oligosaccharide supplementation and reactive hypoglycemia — not IBS/glucagon therapy |
| [NCT04230655](https://clinicaltrials.gov/study/NCT04230655) | NA | Unknown | 110 | Low energy diet + gastric balloon for obesity — unrelated |
| [NCT06113146](https://clinicaltrials.gov/study/NCT06113146) | NA | Completed | 41 | Eating rate of ultra-processed foods on metabolism — unrelated |
| [NCT06408610](https://clinicaltrials.gov/study/NCT06408610) | NA | Completed | 66 | Exercise training effect on gut dysbiosis and **GLP-1** in IBS patients — again GLP-1, not glucagon |
| [NCT02731664](https://clinicaltrials.gov/study/NCT02731664) | Phase 1 | Completed | 12 | Native **GLP-1** inhibits GI motility — mechanistically opposite to glucagon |
| [NCT01056107](https://clinicaltrials.gov/study/NCT01056107) | Phase 1/2 | Completed | 52 | ROSE-010 (a **GLP-1 analog**, not glucagon) in constipation-predominant IBS |

**None of the trials above administer glucagon itself for IBS.**

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [40134805](https://pubmed.ncbi.nlm.nih.gov/40134805/) | 2025 | Systematic Review/Meta-analysis | Frontiers in Endocrinology | GLP-1 receptor agonists improve IBS symptoms — evidence is for GLP-1RAs, not glucagon |
| [35234561](https://pubmed.ncbi.nlm.nih.gov/35234561/) | 2022 | RCT (sub-analysis) | Scandinavian Journal of Gastroenterology | ROSE-010 (GLP-1 analog) reduces pain during IBS attacks in a specific subpopulation |
| [22517769](https://pubmed.ncbi.nlm.nih.gov/22517769/) | 2012 | RCT | Am J Physiol Gastrointest Liver Physiol | Randomized, double-blind, placebo-controlled dose-response study of ROSE-010 (GLP-1 analog) on GI motor function in IBS-C |
| [30444291](https://pubmed.ncbi.nlm.nih.gov/30444291/) | 2019 | Review | Experimental Physiology | Proposes a role for GLP-1-secreting L-cells in IBS pathophysiology |
| [28215540](https://pubmed.ncbi.nlm.nih.gov/28215540/) | 2017 | Clinical study | Clinics and Research in Hepatology and Gastroenterology | Lower serum GLP-1 correlates with abdominal pain in IBS-C patients |
| [31602785](https://pubmed.ncbi.nlm.nih.gov/31602785/) | 2020 | Animal study | Neurogastroenterology and Motility | Exendin-4 (a GLP-1 agonist) improved GI dysfunction in an IBS rat model |
| [23338623](https://pubmed.ncbi.nlm.nih.gov/23338623/) | 2013 | Animal study | International Journal of Molecular Medicine | GLP-1's role in the pathogenesis of experimental IBS rat models |
| [40880735](https://pubmed.ncbi.nlm.nih.gov/40880735/) | 2025 | Clinical study | Frontiers in Nutrition | Low FODMAP diet increases circulating GLP-1 in IBS patients |
| [21694813](https://pubmed.ncbi.nlm.nih.gov/21694813/) | 2011 | Review | Therapeutic Advances in Gastroenterology | General IBS treatment landscape (5-HT agents, antidepressants); does not discuss glucagon |
| [30023410](https://pubmed.ncbi.nlm.nih.gov/30023410/) | 2018 | Review | Cellular and Molecular Gastroenterology and Hepatology | Brain-gut-microbiome axis overview; general background, not glucagon-specific |

**Every relevant paper discusses GLP-1 or its analogs — none study glucagon itself in IBS.**

## Norway Market Information

Glucagon (DB00040) has **no Norway market authorization** in this evidence pack (0 licenses, status: not marketed).

## Safety Considerations

Please refer to the package insert for safety information. Detailed warnings, contraindications, and drug interaction data for glucagon could not be retrieved for this evaluation (data gap DG001 — TFDA label warnings/contraindications; blocking for S1 safety review).

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN score is high, but essentially all supporting clinical and literature evidence pertains to GLP-1 receptor agonists rather than glucagon itself. Glucagon and GLP-1, despite sharing a gene-family origin (proglucagon), act on different receptors with opposing physiological effects, so this evidence cannot be extrapolated to support glucagon repurposing. This is consistent with the model's own evidence-level rating (L5 — prediction only, no direct supporting studies) and the pack's own repurposing rationale, which explicitly flags likely gene-family name confusion.

**To proceed, the following is needed:**
- Resolve DG001 (TFDA/official label warnings and contraindications) and DG002 (glucagon MOA) before any further safety-stage review
- Run a targeted literature/trial search restricted to glucagon (GCGR agonism), excluding GLP-1/GLP-1R agonists, to check whether any direct evidence exists
- If no direct glucagon-specific evidence is found, deprioritize this candidate and log it as a likely TxGNN false positive due to proglucagon gene-family confounding, for model QA feedback
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

