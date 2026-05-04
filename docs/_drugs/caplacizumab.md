---
layout: default
title: Caplacizumab
parent: 僅模型預測 (L5)
nav_order: 24
evidence_level: L5
indication_count: 10
---

# Caplacizumab
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

# Caplacizumab: From Anti-vWF Nanobody to Thrombotic Thrombocytopenic Purpura

## One-Sentence Summary

Caplacizumab is a humanized, bivalent anti-von Willebrand factor (anti-vWF) nanobody approved in the US and EU for acquired thrombotic thrombocytopenic purpura (aTTP), but not yet registered in Norway.
The TxGNN model predicts it may be effective for **Thrombotic Thrombocytopenic Purpura** (ranked 5th among 10 platelet-disorder predictions; TxGNN score 99.9965%), which is the most evidence-rich indication in this analysis, supported by **14 clinical trials** and **20 publications**.
Of note, the top TxGNN prediction by score is *primary release disorder of platelets* (99.9998%), but no clinical or literature evidence currently supports that direction; TTP is selected as the primary focus of this report given its L1-level evidence and actionable recommendation.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | No approved indication in Norway (not yet marketed) |
| Predicted New Indication (Primary Focus) | Thrombotic Thrombocytopenic Purpura (TTP) |
| TxGNN Prediction Score | 99.9965% |
| Evidence Level | L1 |
| Norway Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Currently, formal mechanism of action data is not available in the local database (DrugBank query returned a data gap). However, based on information published in peer-reviewed literature, caplacizumab belongs to the nanobody class of biologics and binds specifically to the A1 domain of von Willebrand factor (vWF), competitively blocking the interaction between vWF ultra-large multimers and platelet glycoprotein Ib (GPIb). This prevents the initial platelet-adhesion step that triggers microvascular thrombosis under high shear conditions.

In acquired TTP, an autoantibody-mediated severe deficiency of ADAMTS13 — the protease responsible for cleaving vWF — leads to accumulation of ultra-large vWF multimers in the circulation. These multimers spontaneously capture platelets via GPIb, forming widespread microvascular platelet-rich thrombi. The resulting clinical picture is microangiopathic hemolytic anemia, severe thrombocytopenia, and ischemic end-organ damage, with untreated mortality exceeding 90%. Caplacizumab's mechanism directly interrupts the most upstream pathological step in this cascade, making the mechanistic link to TTP extremely high.

This prediction is strongly supported by regulatory precedent: the EMA granted approval in 2018 and the US FDA in 2019 for caplacizumab in adults with acquired TTP, based on the Phase 2 TITAN trial (NCT01151423) and the Phase 3 HERCULES trial (NCT02553317). More recently, emerging data suggest caplacizumab may enable TTP management without first-line therapeutic plasma exchange in selected patients, representing a significant shift in standard of care.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|-------------|-------|--------|------------|--------------|
| [NCT01151423](https://clinicaltrials.gov/study/NCT01151423) | Phase 2 | Completed | 75 | TITAN trial: Single-blind, randomized, placebo-controlled RCT; caplacizumab as adjunct to plasma exchange in aTTP; established foundational efficacy and safety data |
| [NCT02553317](https://clinicaltrials.gov/study/NCT02553317) | Phase 3 | Completed | 145 | HERCULES trial: Double-blind, placebo-controlled RCT; caplacizumab significantly reduced time to platelet normalization, TTP-related mortality, major thromboembolic events, and disease exacerbations |
| [NCT05468320](https://clinicaltrials.gov/study/NCT05468320) | Phase 3 | Completed | 51 | Open-label, single-arm, multicenter Phase 3 study evaluating caplacizumab + immunosuppression without first-line therapeutic plasma exchange; primary endpoint: remission |
| [NCT04074187](https://clinicaltrials.gov/study/NCT04074187) | Phase 2/3 | Completed | 21 | Japanese Phase 2/3 trial; evaluated prevention of aTTP recurrence and composite endpoints in Asian patients, supporting cross-ethnic applicability |
| [NCT02878603](https://clinicaltrials.gov/study/NCT02878603) | Phase 3 | Completed | 104 | Post-HERCULES long-term follow-up study; assessed long-term safety, repeated-use efficacy, and characterization of aTTP outcomes beyond acute treatment |
| [NCT05876221](https://clinicaltrials.gov/study/NCT05876221) | N/A | Completed | 223 | Large real-world observational study; evaluated platelet count dynamics under caplacizumab and its uncoupling from ADAMTS13 activity, identifying clinical implications for over- and under-treatment |
| [NCT04985318](https://clinicaltrials.gov/study/NCT04985318) | N/A | Recruiting | 350 | REACT-2020: German national prospective real-world study; describes prescription practices, confirms efficacy, and identifies predictors of persistent autoimmune activity and complications in iTTP |
| [NCT06291025](https://clinicaltrials.gov/study/NCT06291025) | N/A | Recruiting | 131 | Multicenter non-inferiority single-arm study exploring caplacizumab + immunosuppression + plasma infusion without therapeutic plasma exchange as an alternative treatment strategy |
| [NCT06376786](https://clinicaltrials.gov/study/NCT06376786) | N/A | Recruiting | 132 | Italian iTTP prospective national registry; aims to define natural history, disease severity, and long-term clinical outcomes over up to 6 years of follow-up |
| [NCT07205861](https://clinicaltrials.gov/study/NCT07205861) | N/A | Recruiting | 1,200 | TWI-LIGHT: Large-scale French retrospective epidemiological study (n=1,200) in the national TMA cohort; characterizes iTTP patient demographics, treatment patterns, and outcomes at a population level |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|--------------|
| [30625070](https://pubmed.ncbi.nlm.nih.gov/30625070/) | 2019 | Phase 3 RCT | N Engl J Med | HERCULES trial: caplacizumab significantly reduced TTP-related deaths, recurrences, and major thromboembolic events; time to platelet count response was shorter vs placebo |
| [26863353](https://pubmed.ncbi.nlm.nih.gov/26863353/) | 2016 | Phase 2 RCT | N Engl J Med | TITAN trial: anti-vWF nanobody reduced time to response and number of exacerbations; safety profile comparable to placebo in aTTP patients |
| [32914526](https://pubmed.ncbi.nlm.nih.gov/32914526/) | 2020 | Clinical Guideline | J Thromb Haemost | ISTH guidelines for treatment of TTP; recommends caplacizumab as part of triple therapy (plasma exchange + immunosuppression + caplacizumab) |
| [40533296](https://pubmed.ncbi.nlm.nih.gov/40533296/) | 2025 | Guideline Update | J Thromb Haemost | 2025 ISTH focused update: incorporates new evidence on both immune-mediated and congenital TTP; updates treatment algorithms based on post-caplacizumab era data |
| [32914582](https://pubmed.ncbi.nlm.nih.gov/32914582/) | 2020 | Clinical Guideline | J Thromb Haemost | ISTH guidelines for diagnosis of TTP; standardizes ADAMTS13 testing and diagnostic criteria, underpinning evidence-based patient selection for caplacizumab |
| [36053773](https://pubmed.ncbi.nlm.nih.gov/36053773/) | 2023 | Systematic Review & Meta-analysis | Blood Advances | Systematic review and meta-analysis combining RCT and real-world data; confirms faster platelet response and reduced adverse outcomes with caplacizumab added to standard of care |
| [37045600](https://pubmed.ncbi.nlm.nih.gov/37045600/) | 2023 | Systematic Review | Expert Rev Hematol | Systematic review and meta-analysis of caplacizumab efficacy and safety across diverse patient populations; notes consistent benefit with manageable bleeding risk |
| [40388146](https://pubmed.ncbi.nlm.nih.gov/40388146/) | 2025 | Review | JAMA | Current comprehensive review of iTTP: incidence (2–6 per million/year), pathophysiology, diagnostic criteria, and 2025 management recommendations including caplacizumab |
| [34266669](https://pubmed.ncbi.nlm.nih.gov/34266669/) | 2022 | Expert Consensus | Medicina Clinica | Spanish national expert consensus for TTP diagnosis and treatment; endorses caplacizumab-based triple therapy and ADAMTS13-guided treatment duration |
| [28416507](https://pubmed.ncbi.nlm.nih.gov/28416507/) | 2017 | Review | Blood | Foundational review of TTP pathophysiology; explains ADAMTS13 deficiency, ultra-large vWF multimer accumulation, and the mechanistic rationale for targeting vWF-GPIb interaction |

---

## Norway Market Information

Caplacizumab is currently not marketed in Norway and holds no registered marketing authorizations. There are no product licenses to display.

> For reference: caplacizumab is commercially available as **Cablivi** (Sanofi/Ablynx) in the EU and the US, approved for adults with acquired TTP in combination with plasma exchange and immunosuppression.

---

## Safety Considerations

Please refer to the package insert for safety information.

> **Note for evaluators**: Based on caplacizumab's established pharmacological mechanism (inhibition of vWF-GPIb-mediated platelet adhesion), the following considerations are clinically relevant even in the absence of local safety data:
> - **Bleeding risk**: Anti-platelet adhesion activity can increase hemorrhagic complications, particularly in patients with additional bleeding risk factors
> - **Rebound thrombosis**: Premature discontinuation before ADAMTS13 activity recovery may trigger TTP exacerbation
> - **Special populations**: Data in pediatric patients is limited (one retrospective study, n=4); pregnancy and lactation data are not available

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Caplacizumab has L1-level evidence for acquired TTP, supported by two completed Phase 3 RCTs (HERCULES and a no-TPE Phase 3 study), an Asian-population Phase 2/3 trial, long-term follow-up data, and a rapidly growing body of real-world evidence across multiple countries. The mechanistic fit is extremely high — the drug's core mechanism directly addresses the primary pathological event in TTP. EMA and FDA approval provides additional regulatory validation, and the 2025 ISTH guideline update continues to endorse its use.

**To proceed, the following is needed:**
- Formal marketing authorization application for Norway (EMA-approved dossier available as basis)
- Mechanism of action documentation sourced from DrugBank or regulatory submission files
- Local safety data: Norwegian-language package insert and pharmacovigilance plan
- Drug-drug interaction assessment (current data gap)
- Rare disease patient access pathway evaluation (TTP incidence ~2–6 per million/year)
- Pharmacoeconomic analysis within the Norwegian healthcare reimbursement framework
- Clarification of treatment pathway: whether first-line TPE-free strategy (NCT05468320) changes the required clinical infrastructure
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

