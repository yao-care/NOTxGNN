---
layout: default
title: Rimegepant
parent: 僅模型預測 (L5)
nav_order: 306
evidence_level: L5
indication_count: 6
---

# Rimegepant
{: .fs-9 }

證據等級: **L5** | 預測適應症: **6** 個
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

# Rimegepant: From Migraine to Migraine with Brainstem Aura

## One-Sentence Summary

Rimegepant is a CGRP (calcitonin gene-related peptide) receptor antagonist already established for the acute and preventive treatment of migraine. The TxGNN model predicts it may also be effective for **migraine with brainstem aura**, a rarer migraine subtype, with **99.94% prediction confidence** and **14 supporting publications**, though no dedicated clinical trials for this specific subtype currently exist.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Acute treatment of migraine (with/without aura) and preventive treatment of episodic migraine — inferred from literature; formal Norway label text unavailable (drug not marketed) |
| Predicted New Indication | Migraine with brainstem aura |
| TxGNN Prediction Score | 99.94% |
| Evidence Level | L2 |
| Norway Market Status | ✗ Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available from DrugBank in this evidence pack. Based on the literature evidence collected, rimegepant is known to be a small-molecule, highly selective CGRP receptor antagonist ("gepant" class) approved for acute treatment of migraine with or without aura and for prevention of episodic migraine in adults.

Migraine with brainstem aura is a clinical subtype of migraine in which CGRP-mediated neurovascular pathophysiology is presumed to play a similarly central role as in typical migraine. Since CGRP antagonism is already validated as effective across the broader migraine population — including migraine with aura — extending this mechanism to the brainstem aura subtype is biologically plausible.

However, this subtype has historically been excluded from, or not separately analyzed in, most pivotal rimegepant RCTs due to its rarity and the presence of brainstem-localizing symptoms (which are also exclusion criteria in some triptan trials due to vasoconstrictive safety concerns — a concern rimegepant's non-vasoconstrictive mechanism may specifically address, per the mechanistic hypothesis in PMID 41574090). Therefore, current supporting evidence is extrapolated from the general migraine population rather than subtype-specific trials.

---

## Clinical Trial Evidence

Currently no related clinical trials registered specifically for migraine with brainstem aura.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [41066271](https://pubmed.ncbi.nlm.nih.gov/41066271/) | 2025 | RCT | Cephalalgia | Phase 3 open-label, single-arm study in Chinese adults confirming long-term safety, tolerability and effectiveness of rimegepant 75mg ODT for acute migraine treatment |
| [36808268](https://pubmed.ncbi.nlm.nih.gov/36808268/) | 2023 | RCT (randomized, placebo-controlled) | Clin Pharmacol Drug Dev | Phase 1 PK/safety study of single and multiple 75mg doses in healthy Chinese adults; confirms consistent PK/safety profile |
| [41366286](https://pubmed.ncbi.nlm.nih.gov/41366286/) | 2025 | RCT (open-label safety) | J Headache Pain | Phase 4, 24-week study of once-daily 75mg rimegepant for episodic migraine prevention; establishes long-term tolerability |
| [35790906](https://pubmed.ncbi.nlm.nih.gov/35790906/) | 2022 | Meta-analysis (network) | J Headache Pain | Network meta-analysis comparing rimegepant, ubrogepant, and lasmiditan for acute migraine treatment efficacy onset |
| [36739335](https://pubmed.ncbi.nlm.nih.gov/36739335/) | 2023 | Review | CNS Drugs | Comprehensive review of rimegepant's acute and preventive efficacy vs. placebo in phase III trials |
| [32270407](https://pubmed.ncbi.nlm.nih.gov/32270407/) | 2020 | Review (approval summary) | Drugs | First approval summary; ODT formulation development for acute migraine treatment, later expanded to prevention and refractory trigeminal neuralgia investigation |
| [38307667](https://pubmed.ncbi.nlm.nih.gov/38307667/) | 2024 | Review | Handbook Clin Neurol | Overview of CGRP receptor antagonist (gepant) class development and current approved uses |
| [33550872](https://pubmed.ncbi.nlm.nih.gov/33550872/) | 2021 | Review | Pain Management | Review of rimegepant within the broader landscape of new acute migraine treatments |
| [41652664](https://pubmed.ncbi.nlm.nih.gov/41652664/) | 2026 | Cohort (retrospective) | Headache | Retrospective analysis of off-label rimegepant use in adolescents; supports tolerability/effectiveness signal outside approved adult population |
| [41133671](https://pubmed.ncbi.nlm.nih.gov/41133671/) | 2026 | Phase 1 PK study | Headache | PK, safety, and tolerability of weight-adjusted rimegepant ODT dose in children aged 6–<12 years |

---

## Norway Market Information

Rimegepant is **not currently marketed in Norway** (`market_status: 未上市`, 0 authorizations on record). No product- or label-level data is available from this evidence pack.

---

## Safety Considerations

Please refer to the package insert for safety information. No structured warnings, contraindications, or drug-interaction data were available in this evidence pack (regulatory label data collection is flagged as a **Blocking** data gap — see Conclusion below).

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Rimegepant's CGRP-antagonist mechanism has plausible extension to migraine with brainstem aura, and general-population migraine evidence is reasonably strong (L2), but the drug is not yet marketed in Norway and has **no dedicated clinical evidence for this specific subtype**. Critically, official safety/label data (warnings, contraindications) is completely absent, which blocks progression past the S1 safety-review stage per internal scoring.

**To proceed, the following is needed:**
- TFDA/Norway-equivalent regulatory label data (warnings, contraindications) — currently a Blocking gap (DG001)
- DrugBank-confirmed mechanism of action (DG001/DG002 remediation via DrugBank API query)
- Subtype-specific clinical evidence (trial or subgroup analysis) for migraine with brainstem aura, rather than extrapolation from general migraine population
- Confirmation of Norway market entry timeline/regulatory filing status
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

