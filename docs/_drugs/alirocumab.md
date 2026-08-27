---
layout: default
title: Alirocumab
parent: 僅模型預測 (L5)
nav_order: 23
evidence_level: L5
indication_count: 10
---

# Alirocumab
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

# Alirocumab: From Hypercholesterolemia to Cholesterol Catabolic Process Disease

## One-Sentence Summary

Alirocumab (DrugBank DB09302) is a PCSK9-inhibitor monoclonal antibody whose established pharmacology lowers LDL-cholesterol by preserving hepatic LDL-receptor recycling. Among the 10 TxGNN-predicted indications supplied in this evidence pack, the only one with real supporting data is **"cholesterol catabolic process disease"** — a cholesterol-clearance disorder category mechanistically adjacent to alirocumab's known LDL-receptor pathway effect — backed by **1 completed Phase 3 trial** and **19 publications**. The other 9 candidates (including the single highest-scoring TxGNN hit, ichthyosis) carry no clinical or literature support and are flagged **Hold**.

> **Note on indication selection:** TxGNN's single highest raw score (99.43%, rank #6127) belongs to "ichthyosis, X-linked" — but the evidence pack's own rationale states this likely reflects semantic proximity in the knowledge graph ("lipid/sterol" neighborhood) rather than a real mechanistic link, and it has zero clinical/literature evidence. This report therefore focuses on the evidence-supported candidate (rank #5) rather than the top raw-score candidate; all 10 predictions are tabulated later in this report for full transparency.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Hypercholesterolemia / mixed dyslipidemia (LDL-C lowering; not confirmed via Taiwan license data — see note below) |
| Predicted New Indication | Cholesterol catabolic process disease |
| TxGNN Prediction Score | 99.36% (rank #6644) |
| Evidence Level | L2 |
| Taiwan Market Status | ✗ Not marketed (未上市) |
| Number of Authorizations | 0 |
| Recommended Decision | Proceed with Guardrails |

*Original Indication note: `drug.original_indications` and Taiwan license records are empty in this evidence pack (data gap DG002, MOA also unconfirmed). The indication above is inferred from the drug's own supporting literature within this pack (e.g., PMID 38185721, 38658193), not from a TFDA-approved label, since alirocumab has no Taiwan market authorization on record.*

*Evidence Level note: the evidence pack's internal scoring tags this candidate "L1," but per this report's determination rules (≥2 completed Phase 3 RCTs = L1), only **one** completed Phase 3 trial is on record here, so it is classified **L2** (1 completed Phase 2/3 trial) rather than L1.*

---

## Why is This Prediction Reasonable?

Detailed DrugBank mechanism-of-action text is flagged as a data gap (DG002) in this evidence pack. Based on the supporting literature it does contain, alirocumab is a human monoclonal antibody that binds circulating PCSK9 (proprotein convertase subtilisin/kexin type 9), blocking PCSK9-mediated degradation of hepatic LDL receptors. This preserves LDL-receptor recycling, increases hepatic clearance of LDL particles, and lowers circulating LDL-cholesterol (PMID 38185721, 39947256). Its established therapeutic role, per the literature in this pack, spans hypercholesterolemia, homozygous/heterozygous familial hypercholesterolemia, and reduction of recurrent cardiovascular events after acute coronary syndrome (ODYSSEY OUTCOMES, PMID 38658193, 39913634).

"Cholesterol catabolic process disease" is a broad ontology category covering disorders of cholesterol degradation and clearance, which overlaps substantially with LDL-receptor-pathway disorders (e.g., familial hypercholesterolemia, HIV-associated dyslipidemia/atherosclerosis). Because alirocumab acts directly on the LDL-receptor recycling step, this predicted indication sits within the drug's known mechanistic neighborhood rather than representing a distant, speculative repurposing signal — unlike most of the other 9 candidates in this pack, which involve unrelated pathways (steroid sulfatase, mitochondrial β-oxidation, skeletal dysplasia, etc.).

The strongest supporting evidence is a completed Phase 3 trial (EPIC-HIV, NCT03207945) evaluating PCSK9 inhibition for cardiovascular risk reduction in antiretroviral-treated HIV patients — a population with atherogenic, non-calcified-plaque-predominant dyslipidemia consistent with impaired cholesterol clearance. This is complemented by a large, consistent body of review literature and one large real-world safety dataset (47,296 patient-years, PMID 38658193) specific to alirocumab, giving this prediction a materially stronger evidentiary basis than the other candidates in this evidence pack.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT03207945](https://clinicaltrials.gov/study/NCT03207945) | Phase 3 | Completed | 118 | EPIC-HIV study: evaluated PCSK9 inhibition's effect on cardiovascular risk in antiretroviral-treated HIV patients, using noninvasive imaging to assess atherosclerosis (increased vascular inflammation, non-calcified plaque) linked to impaired LDL clearance. |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [38658193](https://pubmed.ncbi.nlm.nih.gov/38658193/) | 2024 | Safety cohort (alirocumab-specific) | Eur Heart J Cardiovasc Pharmacother | Real-world safety analysis from 47,296 patient-years (ODYSSEY OUTCOMES); confirms sustained LDL-C lowering and reduced recurrent ischemic events/all-cause death with alirocumab vs placebo. |
| [39913634](https://pubmed.ncbi.nlm.nih.gov/39913634/) | 2025 | Post-hoc RCT analysis (alirocumab-specific) | Diabetes Care | ODYSSEY OUTCOMES post-hoc analysis: alirocumab lowers both Lp(a) and LDL-C without increasing new-onset diabetes risk. |
| [29526502](https://pubmed.ncbi.nlm.nih.gov/29526502/) | 2018 | Cohort (alirocumab-specific) | Kidney International | Alirocumab retains LDL-C-lowering efficacy and safety in patients with impaired renal function (eGFR 30–59) vs preserved function. |
| [38185721](https://pubmed.ncbi.nlm.nih.gov/38185721/) | 2024 | Review | Signal Transduct Target Ther | Comprehensive review of PCSK9's role in lipid metabolism and as a therapeutic target across cardiovascular, liver, infectious, and autoimmune disease. |
| [38277255](https://pubmed.ncbi.nlm.nih.gov/38277255/) | 2024 | Review | Curr Opin Lipidol | Update on PCSK9-directed therapies; two CV outcomes trials of PCSK9 monoclonal antibodies confirmed marked LDL-C and cardiovascular risk reduction. |
| [39751968](https://pubmed.ncbi.nlm.nih.gov/39751968/) | 2025 | Review | Curr Atheroscler Rep | Review of novel pharmacologic therapies, including PCSK9 inhibitors, for homozygous familial hypercholesterolemia (HoFH). |
| [36422206](https://pubmed.ncbi.nlm.nih.gov/36422206/) | 2022 | Review | Medicina (Kaunas) | Review of familial hypercholesterolemia diagnostics and treatment, including PCSK9-targeted options. |
| [36739653](https://pubmed.ncbi.nlm.nih.gov/36739653/) | 2023 | Review | Kardiol Pol | Reviews evidence for PCSK9's role in LDL metabolism and clinical impact of PCSK9 inhibitors on lipid parameters and cardiovascular risk. |
| [37686091](https://pubmed.ncbi.nlm.nih.gov/37686091/) | 2023 | Review | Int J Mol Sci | Broad review of dyslipidemia treatment approaches aimed at normalizing TC, TG, and LDL-C. |
| [39947256](https://pubmed.ncbi.nlm.nih.gov/39947256/) | 2025 | Review | Pharmacol Ther | Compares extracellular PCSK9 inhibition (alirocumab, evolocumab) vs intracellular suppression (inclisiran) as LDL-C-lowering strategies. |

---

## Taiwan Market Information

Alirocumab currently has **no Taiwan Food and Drug Administration (TFDA) market authorization on record** (market status: 未上市 / Not marketed; total licenses: 0). No product license, dosage form, or approved-indication text is available in this evidence pack to tabulate.

---

## Other TxGNN-Predicted Indications (Screened Out)

For transparency, the remaining 9 TxGNN predictions in this evidence pack are summarized below. None have clinical trial or literature support, and one shows a potential **mechanism-conflict signal** worth flagging for pharmacovigilance awareness even though it is not currently actionable.

| Rank | Disease | Evidence Level | Decision | Note |
|------|---------|------|------|------|
| 1 | Ichthyosis, X-linked (without steroid sulfatase deficiency) | L5 | Hold | Highest raw TxGNN score, but no known mechanistic or clinical link; likely a knowledge-graph semantic artifact. |
| 2 | Disorder of other vitamins/cofactors metabolism | L5 | Hold | Disease definition too broad to establish a mechanistic link. |
| 3 | Xanthomatosis (disease) | L3 | Research Question | Indirect support only — cited literature describes disease genotypes (dysbetalipoproteinemia, sitosterolemia), not alirocumab treatment outcomes. |
| 4 | 46,XY DSD due to DHT backdoor pathway defect | L5 | Hold | Speculative link to steroidogenesis; no evidence alirocumab affects steroid enzyme activity. |
| 6 | 46,XY DSD due to cholesterol synthesis defect | L5 | Hold | **Mechanism-conflict flag**: this disease involves cholesterol *under-synthesis* (e.g., Smith-Lemli-Opitz), while alirocumab *lowers* circulating LDL-C — opposite direction, potential safety concern rather than mere lack of evidence. |
| 7 | Dappled diaphyseal dysplasia | L5 | Hold | Skeletal dysplasia; no known link to lipoprotein/PCSK9 pathways. |
| 8 | Neutral lipid storage disease | L5 | Hold | Involves intracellular triglyceride storage defects (e.g., ATGL/CGI-58), mechanistically distinct from PCSK9-LDL receptor pathway. |
| 9 | 3-Hydroxyacyl-CoA dehydrogenase deficiency | L5 | Hold | Mitochondrial fatty-acid β-oxidation disorder; no overlap with PCSK9 pathway. |
| 10 | Spastic paraplegia–optic atrophy–neuropathy spectrum | L5 | Hold | Neurodegenerative disorder; no evidence of CNS penetration or relevance for a peripherally-acting mAb. |

---

## Safety Considerations

Please refer to the package insert for safety information. (Key warnings, contraindications, and drug-interaction data are all marked as data gaps in this evidence pack — DG001, blocking severity — and TFDA package insert parsing is still pending.)

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
One completed Phase 3 trial (EPIC-HIV) plus a substantial, consistent body of review-level literature and real-world safety data (47,296 patient-years) support a mechanistically direct — though broadly-defined — link between alirocumab's LDL-receptor pathway effect and cholesterol catabolic/clearance disorders. This is meaningfully stronger than the other 9 candidates in this evidence pack, none of which have any clinical or literature support, but the indication label itself is an ontology umbrella term rather than a precise clinical diagnosis, and alirocumab has no existing Taiwan market authorization.

**To proceed, the following is needed:**
- TFDA package insert parsing to resolve the blocking safety data gap (DG001) before any S1 safety review can begin
- DrugBank MOA confirmation (DG002) to formally validate the mechanistic rationale
- Clinical disambiguation of "cholesterol catabolic process disease" into an actionable, narrower diagnostic scope (e.g., specific familial hypercholesterolemia subtype or HIV-associated dyslipidemia)
- Assessment of a Taiwan market-entry pathway (named-patient/import basis), since there is currently no local authorization
- A dedicated safety monitoring plan (lipid panel, injection-site reactions, hypersensitivity) given the absence of contraindication/DDI data
- Continued exclusion of rank #6 ("46,XY DSD due to cholesterol synthesis defect") from any repurposing pathway, given its opposite-direction mechanism-conflict signal
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

