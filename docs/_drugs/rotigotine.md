---
layout: default
title: Rotigotine
parent: 僅模型預測 (L5)
nav_order: 315
evidence_level: L5
indication_count: 10
---

# Rotigotine
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

# Rotigotine: From Parkinson's Disease/Restless Legs Syndrome to Attention Deficit-Hyperactivity Disorder

## One-Sentence Summary

Rotigotine is a non-ergoline dopamine agonist currently used to treat Parkinson's disease and restless legs syndrome (RLS).
The TxGNN model predicts it may be effective for **Attention Deficit-Hyperactivity Disorder (ADHD)**,
but currently **no clinical trials** and only **3 loosely related publications** (mostly about RLS, not ADHD) support this direction.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Parkinson's disease, Restless legs syndrome (RLS) — per supporting literature; no formal Norway license data available |
| Predicted New Indication | Attention Deficit-Hyperactivity Disorder (ADHD) |
| TxGNN Prediction Score | 99.99% |
| Evidence Level | L5 |
| Norway Market Status | ✗ Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action (MOA) data for rotigotine is not available in this evidence pack. Based on information contained in the supporting literature (PMID 37221270), rotigotine is a non-ergoline dopamine agonist that activates all five dopamine receptor subtypes (D1–D5), with particularly high affinity for D3, and is clinically used to treat Parkinson's disease and RLS.

The theoretical link to ADHD rests on a shared "dopamine hypoactivity" framework: Parkinson's disease and RLS involve reduced nigrostriatal/diencephalic dopaminergic tone, while ADHD is hypothesized to arise from insufficient prefrontal-striatal dopamine transmission. This shared mechanistic theme is likely what drives the TxGNN association.

However, the actual evidence is thin. Two of the three cited papers (PMID 18656214, PMID 21476956) are reviews entirely about RLS with no discussion of ADHD. The only paper with genuine ADHD relevance (PMID 34182128, 2021) links ADHD to dopamine D4 receptor polymorphisms and α2A-adrenoceptor heteromerization — an indirect receptor-genetics argument, not direct pharmacological or clinical evidence that rotigotine treats ADHD. No clinical trials of rotigotine in ADHD have been registered. This is consistent with the assigned **L5 (model prediction only)** evidence level and a **Hold** recommendation.

## Clinical Trial Evidence

Currently no related clinical trials registered

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [21476956](https://pubmed.ncbi.nlm.nih.gov/21476956/) | 2011 | Review | Current Pharmaceutical Design | Review of pharmacological treatment options for RLS in children; does not address ADHD |
| [18656214](https://pubmed.ncbi.nlm.nih.gov/18656214/) | 2008 | Review | Revue Neurologique | General review of RLS pathophysiology and treatment (French); does not address ADHD |
| [34182128](https://pubmed.ncbi.nlm.nih.gov/34182128/) | 2021 | Mechanistic/Receptor pharmacology | Pharmacological Research | Describes α2A-adrenoceptor/dopamine D4 receptor heteromerization and its relevance to ADHD via D4 polymorphic variants — an indirect receptor-genetics link, not a direct rotigotine-ADHD study |

## Norway Market Information

Rotigotine currently holds **no marketing authorization in Norway** (market status: 未上市/Not marketed; 0 licenses on record). No product or dosage form data is available.

## Safety Considerations

Please refer to the package insert for safety information.

> Note: A blocking data gap (DG001) exists for TFDA/regulatory warnings and contraindications, which is required before any Stage 1 (S1) safety evaluation can proceed.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
No clinical trials support rotigotine's use in ADHD, and the available literature is either off-topic (RLS reviews) or only indirectly relevant (receptor-genetics mechanism paper). The evidence level is L5 — model prediction only — which does not meet the threshold to advance.

**To proceed, the following is needed:**
- Direct preclinical or clinical evidence evaluating rotigotine specifically in ADHD populations
- Rotigotine mechanism of action (MOA) data from DrugBank or primary literature
- TFDA/regulatory package insert warnings and contraindications (currently a blocking data gap)
- Confirmation of formal original indication and licensing status (Parkinson's disease/RLS) from a regulatory source
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

