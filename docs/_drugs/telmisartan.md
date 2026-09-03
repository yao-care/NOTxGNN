---
layout: default
title: Telmisartan
parent: 僅模型預測 (L5)
nav_order: 343
evidence_level: L5
indication_count: 10
---

# Telmisartan
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

# Telmisartan: From Hypertension (ARB Class) to Cerebral Artery Occlusion

## One-Sentence Summary

Telmisartan is an angiotensin II receptor blocker (ARB), a drug class established for hypertension management and cardiovascular risk reduction. The TxGNN model predicts potential benefit for **Cerebral Artery Occlusion** (ischemic stroke), currently the best-supported candidate among ten TxGNN predictions for this drug, backed by **3 clinical trials** (including one completed Phase 4 study, n=1,228) and **16 preclinical/mechanistic publications**.

> Note: Of the 10 TxGNN-predicted indications in this evidence pack, the top-ranked hit (Prinzmetal angina, score 99.98%) and several others (brain stem infarction, ABri amyloidosis, Braddock syndrome, etc.) have **no supporting trials or literature** (Evidence Level L5, recommendation "Hold"). This report instead focuses on **cerebral artery occlusion (rank 4)**, which has the strongest actual evidence base (L2). A related candidate, intracerebral hemorrhage (rank 9), has comparable evidence and is referenced below for context.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not formally recorded in this evidence pack — DrugBank indication lookup pending (see Data Gap DG002) |
| Predicted New Indication | Cerebral artery occlusion |
| TxGNN Prediction Score | 99.95% |
| Evidence Level | L2 |
| Taiwan Market Status | 未上市 (Not marketed) |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data for telmisartan is not yet available in this evidence pack (Data Gap DG002, High severity — pending DrugBank API query). However, the repurposing rationale accompanying multiple predicted indications consistently describes telmisartan as an **AT1 (angiotensin II type 1) receptor blocker**, with additional **PPAR-γ agonist activity** — a dual profile sometimes referred to in the literature as a "metabosartan." This class is well established for blood pressure control and cardiovascular risk reduction.

Hypertension is a major upstream risk factor for both ischemic stroke (cerebral artery occlusion) and hemorrhagic stroke, so a drug that lowers blood pressure and improves endothelial function has a plausible pathway to benefit in cerebrovascular disease. Beyond blood-pressure lowering, telmisartan's AT1 blockade and PPAR-γ activation are reported in animal models to reduce oxidative stress, neuroinflammation, and infarct volume — mechanisms directly relevant to ischemic brain injury.

This mechanistic plausibility is supported by a substantial body of rodent middle cerebral artery occlusion (MCAO) studies showing reduced infarct volume, attenuated oxidative stress (AGE/4-HNE), and reduced neuroinflammatory markers (MCP-1, TNF-α, Iba-1) with telmisartan treatment. On the clinical side, a completed Phase 4 trial (NCT01075698, n=1,228) evaluated telmisartan's effect on cardiovascular biomarkers and events in high-risk hypertensive patients, providing some human translational support — though it was not designed specifically around cerebral artery occlusion as a primary endpoint. No dedicated Phase 2/3 RCT currently establishes telmisartan's efficacy for treating or preventing cerebral artery occlusion specifically.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT01075698](https://clinicaltrials.gov/study/NCT01075698) | Phase 4 | Completed | 1,228 | Randomized, open-label (PROBE) comparison of telmisartan (ARB) vs. ordinary therapy in high-risk hypertensive patients; assessed cardiovascular biomarkers and long-term cardiovascular events. |
| [NCT03785067](https://clinicaltrials.gov/study/NCT03785067) | Phase 3 | Terminated | 1 | TRIDENT cognitive sub-study on intensive BP control ("Triple Pill") for slowing memory decline post-ICH; terminated with only 1 participant enrolled. |
| [NCT03783754](https://clinicaltrials.gov/study/NCT03783754) | N/A | Terminated | 4 | TRIDENT MRI sub-study evaluating structural brain changes with intensive BP control post-ICH; terminated with only 4 participants enrolled. |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [21901125](https://pubmed.ncbi.nlm.nih.gov/21901125/) | 2011 | Review | PloS One | Head-to-head comparison of telmisartan vs. ramipril (and combination) for stroke prevention and neuroprotection in hypertensive rat stroke models. |
| [24780412](https://pubmed.ncbi.nlm.nih.gov/24780412/) | 2014 | Animal Study | J Stroke Cerebrovasc Dis | Telmisartan reduced progressive oxidative stress and α-synuclein accumulation after transient MCAO in stroke-resistant hypertensive rats. |
| [25307428](https://pubmed.ncbi.nlm.nih.gov/25307428/) | 2014 | Animal Study | J Stroke Cerebrovasc Dis | Long-term telmisartan ameliorated metabolic-syndrome-related molecules (insulin receptor, PPAR-γ, AT1R) after transient MCAO. |
| [19604102](https://pubmed.ncbi.nlm.nih.gov/19604102/) | 2009 | Animal Study | J Neurotrauma | Telmisartan reduced cerebral infarct volume and peri-infarct cytosolic phospholipase A2 in experimental stroke. |
| [28699721](https://pubmed.ncbi.nlm.nih.gov/28699721/) | 2016 | Animal Study | Indian J Exp Biol | Telmisartan + nimodipine combination showed neuroprotective effects when given pre- and post-ischemia in an experimental cerebral ischemia model. |
| [24650592](https://pubmed.ncbi.nlm.nih.gov/24650592/) | 2014 | Animal Study | Pharmacol Biochem Behav | Non-hypotensive dose of telmisartan + nimodipine produced synergistic neuroprotection by attenuating brain cytokine levels after MCAO/reperfusion. |
| [32992165](https://pubmed.ncbi.nlm.nih.gov/32992165/) | 2020 | Animal Study | J Stroke Cerebrovasc Dis | PPAR-γ activation by telmisartan inhibited Egr-1 and reduced brain injury in an experimental ischemic stroke model. |
| [25245484](https://pubmed.ncbi.nlm.nih.gov/25245484/) | 2014 | Animal Study | J Stroke Cerebrovasc Dis | Telmisartan ameliorated inflammatory responses (MCP-1, TNF-α, Iba-1) after transient MCAO in hypertensive rats. |
| [24435631](https://pubmed.ncbi.nlm.nih.gov/24435631/) | 2015 | Animal Study | Transl Stroke Res | Long-term telmisartan reduced Alzheimer's-type amyloid genesis after transient MCAO in stroke-resistant hypertensive rats. |
| [41341617](https://pubmed.ncbi.nlm.nih.gov/41341617/) | 2025 | Animal/In silico Study | Toxicology Reports | Telmisartan (with ertugliflozin and omaveloxolone) attenuated cerebral ischemia-reperfusion neurotoxicity via Nrf2/HO-1 pathway modulation. |

*(6 additional lower-priority animal studies with similar tMCAO/AT1-blockade mechanistic findings are available in the source evidence pack but omitted here for brevity.)*

---

## Taiwan Market Information

Telmisartan currently holds **no drug license records** in this evidence pack and is **not marketed in Taiwan** (0 authorizations). No product/dosage form information is available.

---

## Safety Considerations

Please refer to the package insert for safety information. (Key warnings, contraindications, and drug-interaction data are currently unavailable — TFDA label parsing is flagged as a Blocking data gap; see Conclusion.)

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Evidence for cerebral artery occlusion is more substantial than for any other TxGNN prediction for this drug (L2, one completed Phase 4 trial plus consistent preclinical mechanistic support), but no dedicated Phase 2/3 RCT confirms efficacy for this specific indication, and telmisartan is not currently marketed in Taiwan — so there is no existing regulatory or supply pathway to build on.

**To proceed, the following is needed:**
- Resolve DG001 (Blocking): obtain and parse TFDA label warnings/contraindications before any S1 safety screening can occur
- Resolve DG002 (High): confirm original MOA and indication via DrugBank API query
- Clarify whether NCT01075698 captured cerebral artery occlusion/stroke as a distinct outcome (currently only described as general cardiovascular events/biomarkers)
- Evaluate feasibility and regulatory pathway for introducing telmisartan to the Taiwan market, since 0 licenses currently exist
- Consider whether a dedicated secondary-stroke-prevention RCT is warranted given the strength of preclinical signal
- Monitor intracerebral hemorrhage (rank 9, also L2) as a related candidate sharing the same RAAS-blockade rationale, anchored by the completed TRIDENT trial (NCT02699645, n=1,671)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

