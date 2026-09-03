---
layout: default
title: Memantine
parent: 僅模型預測 (L5)
nav_order: 224
evidence_level: L5
indication_count: 4
---

# Memantine
{: .fs-9 }

證據等級: **L5** | 預測適應症: **4** 個
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

# Memantine: From an Undocumented Original Indication to Potential Migraine Prophylaxis

## One-Sentence Summary

Memantine (DrugBank DB01043) is an NMDA receptor antagonist; the evidence pack does not document its original approved indication or mechanism of action in this dataset (both flagged as data gaps). Across four TxGNN-predicted indications, **migraine disorder** shows by far the strongest supporting evidence — **2 clinical trials** and **20 publications**, including a meta-analysis, a systematic review, and randomized placebo-controlled trials — while the highest-scoring prediction (pulmonary hypertension) has essentially no direct clinical support for memantine itself.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available in evidence pack (no licenses on file; DG002 flags MOA as a High-severity gap) |
| Predicted New Indication | Migraine disorder (strongest-evidence candidate; see multi-indication table below) |
| TxGNN Prediction Score | 99.52% (rank #5315) |
| Evidence Level | L1 |
| Norway Market Status | ✗ Not marketed (未上市) |
| Number of Authorizations | 0 |
| Recommended Decision | **Hold** |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism-of-action data is not available in this evidence pack (DG002). Based on general pharmacology, memantine is a known NMDA (N-methyl-D-aspartate) receptor antagonist. For the migraine prediction specifically, the rationale supplied is mechanistically coherent: excess glutamatergic signaling and NMDA-receptor-mediated cortical spreading depression are core elements of migraine pathophysiology, and NMDA antagonism is a plausible route to reducing central sensitization. This is supported by a substantial independent literature base (meta-analysis, systematic review, network meta-analysis, and a completed Phase 3 RCT vs. sodium valproate).

By contrast, the top-ranked prediction by raw TxGNN score — pulmonary hypertension — has no direct clinical evidence for memantine; the single relevant clinical study identified concerns **MN-08**, a nitrate derivative of memantine, not memantine itself, and the mechanistic link is described in the evidence pack as speculative. The third and fourth predictions (kyphoscoliotic heart disease, migraine with brainstem aura) either lack any supporting evidence or rely on extrapolation from the general migraine literature without indication-specific data.

Because the original indication and MOA are undocumented in this dataset, the mechanistic comparison between "original use" and "predicted new use" cannot be fully constructed here — this itself is a data gap that should be resolved (see Conclusion).

---

## All Predicted Indications (Overview)

| Rank | Disease | TxGNN Score | Evidence Level | Decision Stage | Recommendation |
|------|---------|-------------|-----------------|------------------|------------------|
| 1 | Pulmonary hypertension | 99.54% | L5 | S0 | Hold |
| 2 | **Migraine disorder** | 99.52% | **L1** | S2 | Research Question |
| 3 | Kyphoscoliotic heart disease | 99.43% | L5 | S0 | Hold |
| 4 | Migraine with brainstem aura | 99.41% | L4 | S1 | Research Question |

---

## Clinical Trial Evidence (Migraine Disorder)

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT04698525](https://clinicaltrials.gov/study/NCT04698525) | Phase 3 | Completed | 33 | Compared memantine vs. sodium valproate for prophylactic treatment of episodic migraine; direct head-to-head trial but small sample size limits statistical power |
| [NCT02670161](https://clinicaltrials.gov/study/NCT02670161) | Phase 4 | Enrolling by invitation | 3300 | EMR-based pragmatic registry across 10 common neurological disorders; not a memantine-specific intervention trial, low direct relevance |

---

## Literature Evidence (Migraine Disorder)

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [33961371](https://pubmed.ncbi.nlm.nih.gov/33961371/) | 2021 | Meta-analysis of RCTs | Clin Neuropharmacol | Systematic review/meta-analysis of memantine vs. placebo for migraine treatment |
| [34352118](https://pubmed.ncbi.nlm.nih.gov/34352118/) | 2021 | Systematic Review | Headache | Assesses efficacy and safety of memantine for prophylactic treatment of episodic migraine |
| [40978493](https://pubmed.ncbi.nlm.nih.gov/40978493/) | 2025 | Network Meta-analysis | Front Pharmacol | Compares oral preventive medications for migraine in adults 18–65, including memantine |
| [26638119](https://pubmed.ncbi.nlm.nih.gov/26638119/) | 2016 | RCT (double-blind, placebo-controlled) | Headache | Memantine for prophylactic treatment of migraine without aura |
| [39467289](https://pubmed.ncbi.nlm.nih.gov/39467289/) | 2024 | Clinical Practice Guideline | Ann Intern Med | 2023 VA/DoD CPG for management of headache, covering preventive options |
| [17901918](https://pubmed.ncbi.nlm.nih.gov/17901918/) | 2007 | Retrospective Study | J Headache Pain | Retrospective review of 60 cases treated with memantine for migraine prevention |
| [36869904](https://pubmed.ncbi.nlm.nih.gov/36869904/) | 2023 | Review | Naunyn Schmiedebergs Arch Pharmacol | Reviews memantine and ketamine as NMDA-receptor-based anti-migraine agents |
| [29508147](https://pubmed.ncbi.nlm.nih.gov/29508147/) | 2018 | Review | Neurotherapeutics | Reviews glutamate/NMDA receptor as therapeutic target for migraine |
| [34048395](https://pubmed.ncbi.nlm.nih.gov/34048395/) | 2021 | Review | Continuum (Minneap Minn) | Overview of preventive migraine treatment options including glutamatergic agents |
| [19280698](https://pubmed.ncbi.nlm.nih.gov/19280698/) | 2009 | Open-label Case Series | Headache | Memantine in preventive treatment for migraine and refractory migraine |

Note: A separate commentary, [34510445](https://pubmed.ncbi.nlm.nih.gov/34510445/) ("Memantine for migraine — Big promise but little evidence," *Headache*, 2021), offers a cautionary counterpoint and should be reviewed alongside the above.

---

## Norway Market Information

Memantine currently holds **0 marketing authorizations** in Norway (`market_status: 未上市 / Not marketed`). No license records are available to summarize.

---

## Safety Considerations

Please refer to the package insert for safety information.

*(Key warnings, contraindications, and drug interaction data are not populated in this evidence pack — see DG001, flagged as a Blocking-severity gap.)*

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Migraine disorder is a scientifically credible repurposing candidate for memantine, supported by L1-level evidence (meta-analysis, systematic review, RCTs). However, this evidence pack has a **Blocking-severity data gap (DG001)** — TFDA label warnings/contraindications are unavailable — which prevents even the initial S1 safety evaluation. Combined with memantine having **zero existing marketing authorizations in Norway**, there is currently no safety basis or regulatory pathway to support a "Go" or "Proceed with Guardrails" decision.

**To proceed, the following is needed:**
- Resolve DG001: obtain TFDA/equivalent label (warnings, contraindications) to enable S1 safety screening
- Resolve DG002: confirm mechanism of action and original approved indication(s) via DrugBank or manufacturer labeling
- For the migraine indication: commission or identify a larger, adequately powered confirmatory RCT (current largest completed trial: n=33)
- Clarify Norway market-entry strategy, since the drug is not currently marketed there
- For the pulmonary hypertension signal: monitor development of MN-08 (nitrate derivative of memantine) separately — current data does not support extrapolation to memantine itself
- Deprioritize kyphoscoliotic heart disease (no supporting evidence) and migraine with brainstem aura (indication-specific evidence still lacking) pending new data
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

