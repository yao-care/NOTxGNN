---
layout: default
title: Canakinumab
parent: 僅模型預測 (L5)
nav_order: 20
evidence_level: L5
indication_count: 10
---

# Canakinumab
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

# Canakinumab: From Cryopyrin-Associated Periodic Syndromes to Familial Mediterranean Fever

## One-Sentence Summary

Canakinumab (Ilaris) is a fully human anti-IL-1β monoclonal antibody globally approved for Cryopyrin-Associated Periodic Syndromes (CAPS) and several related autoinflammatory conditions, but currently not marketed in Taiwan.
While TxGNN's top-ranked prediction is hepatic infarction (Rank #1, L5, no clinical evidence), the most actionable prediction in this analysis is **Familial Mediterranean Fever, Autosomal Dominant** (Rank #6), supported by **7 clinical trials** (including 5 completed Phase 3 studies) and **20 publications** — among them the landmark Phase 3 CLUSTER trial published in the *New England Journal of Medicine*.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | CAPS (not licensed in Taiwan; globally approved for CAPS, FMF, TRAPS, HIDS/MKD, sJIA) |
| Predicted New Indication (Actionable) | Familial Mediterranean Fever, Autosomal Dominant |
| TxGNN Prediction Score | 99.41% (Rank #6 among analyzed indications; Rank #1 hepatic infarction has no supporting clinical evidence) |
| Evidence Level | L1 |
| Taiwan Market Status | ✗ Not marketed (0 authorizations) |
| Number of Authorizations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Although formal MOA documentation is listed as a data gap in this Evidence Pack, published literature consistently describes Canakinumab's mechanism: it is a fully human IgG1 monoclonal antibody that selectively binds and neutralizes free IL-1β with high affinity. By preventing IL-1β from engaging the IL-1 receptor, it blocks downstream NF-κB signaling and the production of prostaglandins, acute-phase reactants (CRP, SAA), and secondary inflammatory mediators. This mechanism of action was first described in its 2009 FDA approval for CAPS and has been replicated across multiple disease settings.

Familial Mediterranean Fever (FMF) is caused by gain-of-function mutations in the *MEFV* gene encoding pyrin, a key regulator of the pyrin inflammasome. Mutant pyrin leads to uncontrolled inflammasome activation → excess caspase-1 cleavage → uncontrolled IL-1β secretion → recurrent acute sterile serositis (peritonitis, pleuritis, arthritis) and fever attacks lasting 12–72 hours. The mechanistic bridge to Canakinumab is therefore direct: neutralizing IL-1β eliminates the central inflammatory mediator responsible for FMF attacks.

CAPS (the original approved indication) and FMF share the same terminal effector pathway — IL-1β overproduction from inflammasome dysregulation — with the difference lying only in the upstream mutant gene (NLRP3 in CAPS vs. MEFV in FMF). This shared biology makes the TxGNN prediction biologically sound rather than incidental, and it is independently validated by regulatory approval: the FDA approved Canakinumab for colchicine-resistant FMF in 2016 on the strength of the Phase 3 CLUSTER trial.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00685373](https://clinicaltrials.gov/study/NCT00685373) | Phase 3 | Completed | 166 | Largest Phase 3 long-term safety and efficacy database for canakinumab in CAPS (FCAS, MWS, NOMID); enrolled patients from prior studies plus newly identified patients; ≥6 months treatment |
| [NCT00465985](https://clinicaltrials.gov/study/NCT00465985) | Phase 3 | Completed | 35 | Three-part trial with double-blind, placebo-controlled withdrawal design (Part II) in Muckle-Wells Syndrome; confirmed durable efficacy and identified responders for long-term therapy |
| [NCT01302860](https://clinicaltrials.gov/study/NCT01302860) | Phase 3 | Completed | 17 | 1-year open-label multicenter trial in CAPS patients aged ≤4 years; assessed efficacy, tolerability, and compatibility with childhood vaccination schedules |
| [NCT01576367](https://clinicaltrials.gov/study/NCT01576367) | Phase 3 | Completed | 17 | Open-label extension of NCT01302860; generated long-term safety and tolerability data for young CAPS patients continuing from the parent study |
| [NCT00991146](https://clinicaltrials.gov/study/NCT00991146) | Phase 3 | Completed | 19 | Open-label efficacy and safety study in Japanese CAPS patients (FCAS, MWS, NOMID); 6-month core treatment with extension until Japan market approval in 2012 |
| [NCT01242813](https://clinicaltrials.gov/study/NCT01242813) | Phase 2 | Completed | 20 | Open-label 4-month canakinumab treatment plus 6-month drug-free follow-up in TRAPS patients; established dosing strategy and efficacy signals in related periodic fever syndromes |
| [NCT06838143](https://clinicaltrials.gov/study/NCT06838143) | Observational | Recruiting | 25 | REASSURE study (2025–2028): non-interventional real-world safety and effectiveness of Ilaris 150 mg in CAPS, crFMF, TRAPS, HIDS/MKD, and sJIA in routine clinical practice |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|---------|
| [29768139](https://pubmed.ncbi.nlm.nih.gov/29768139/) | 2018 | Phase 3 RCT (CLUSTER) | N Engl J Med | Pivotal CLUSTER trial: canakinumab significantly reduced attack rates across FMF, TRAPS, and HIDS/MKD vs. placebo; formed the primary basis for FDA/EMA approval in these indications |
| [35874710](https://pubmed.ncbi.nlm.nih.gov/35874710/) | 2022 | Systematic Review | Front Immunol | First systematic review covering all approved IL-1 blockers; confirmed canakinumab's efficacy and manageable safety profile across the full spectrum of autoinflammatory disorders |
| [37769252](https://pubmed.ncbi.nlm.nih.gov/37769252/) | 2024 | Systematic Review & Meta-analysis | Rheumatology (Oxford) | Quantified efficacy and safety of anti-IL-1 agents specifically in FMF across multiple international cohorts; strongly supported use in colchicine-resistant patients |
| [40040547](https://pubmed.ncbi.nlm.nih.gov/40040547/) | 2025 | Cohort Study | Int J Rheum Dis | Compared canakinumab with and without concomitant colchicine in FMF; characterized effects on attack frequency, CRP/SAA levels, and renal outcomes |
| [34568239](https://pubmed.ncbi.nlm.nih.gov/34568239/) | 2021 | Retrospective Cohort | Front Pediatr | 65 colchicine-resistant pediatric FMF patients: complete remission achieved with monthly canakinumab dosing; dose tapering successfully implemented in sustained responders |
| [36961326](https://pubmed.ncbi.nlm.nih.gov/36961326/) | 2023 | Cohort Study | Rheumatology (Oxford) | Established a treatment tapering and discontinuation protocol for canakinumab in pediatric colchicine-resistant FMF; critical for long-term management decisions |
| [31463794](https://pubmed.ncbi.nlm.nih.gov/31463794/) | 2019 | Retrospective Analysis | Paediatric Drugs | Single-center experience with canakinumab in pediatric FMF patients; documented clinical and laboratory responses in children unresponsive to colchicine |
| [28362189](https://pubmed.ncbi.nlm.nih.gov/28362189/) | 2017 | Clinical Review | Expert Rev Clin Immunol | Comprehensive evidence review for canakinumab in FMF; summarized key clinical trials and discussed positioning relative to other anti-IL-1 agents |
| [36062765](https://pubmed.ncbi.nlm.nih.gov/36062765/) | 2022 | Review | Clin Exp Rheumatol | Compared clinical outcomes of IL-1 inhibition in FMF; discussed treatment expectations, colchicine combination strategies, and long-term remission data |
| [32806879](https://pubmed.ncbi.nlm.nih.gov/32806879/) | 2020 | Review | Turk J Med Sci | Contemporary pathogenesis-to-treatment review of FMF; contextualized IL-1 blockade within modern management guidelines and MEFV mutation spectrum |

---

## Taiwan Market Information

Canakinumab currently has **no marketing authorizations in Taiwan** (0 licenses; market status: not marketed as of 2026-04-20).

The drug is marketed internationally under the brand name **Ilaris** (Novartis) with the following globally approved indications for reference:

| Region | Approved Indications |
|--------|---------------------|
| FDA (USA) | CAPS (FCAS, MWS, NOMID), FMF (colchicine-resistant), TRAPS, HIDS/MKD, sJIA, Adult-onset Still's disease |
| EMA (Europe) | CAPS, FMF (colchicine-resistant or intolerant), TRAPS, HIDS/MKD, sJIA |

Any use in Taiwan would require a full NDA submission to the TFDA, including bridging clinical data for the relevant patient population if required.

---

## Safety Considerations

Please refer to the package insert for safety information.

> **Important note:** Taiwan-specific package insert data (warnings and contraindications) was not available in this Evidence Pack and is classified as a **blocking data gap** — it must be obtained from the EMA/FDA label or Novartis before any formal safety evaluation. No drug-drug interaction records were identified in the DDI database query. Given canakinumab's class as an immunomodulatory biologic, known class-level concerns include serious infections (including opportunistic infections and tuberculosis reactivation) and potential interference with vaccines.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Canakinumab's mechanism of action precisely targets the pathophysiological effector of FMF — the IL-1β overflow downstream of mutant pyrin inflammasome hyperactivation. This is not speculative repurposing: the drug holds active FDA and EMA approvals for FMF, backed by a Phase 3 RCT published in the New England Journal of Medicine. The Taiwan opportunity is best characterized as a **market access gap** rather than an unproven repurposing hypothesis.

**To proceed, the following is needed:**

- Obtain the TFDA package insert (or EMA/FDA label as proxy) to resolve the blocking safety data gap before regulatory submission planning
- Secure formal MOA documentation from DrugBank or the prescribing information for dossier completeness
- Conduct a Taiwan FMF patient population estimate — FMF is a rare disease with ethnic clustering (Mediterranean/Middle Eastern heritage); estimate local disease burden to support orphan drug pathway feasibility
- Perform a health economic assessment: as a subcutaneous biologic with high unit cost, canakinumab will require rare disease pricing justification and potential NHI reimbursement negotiation
- Review pediatric dosing data in the Taiwan context (age cutoffs for sJIA vs. periodic fever indications differ)
- Design a safety monitoring plan covering infection surveillance, TB screening (prior to initiation), and long-term immunosuppression follow-up consistent with biologic therapy standards
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

