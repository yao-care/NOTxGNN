---
layout: default
title: Vilanterol
parent: 僅模型預測 (L5)
nav_order: 384
evidence_level: L5
indication_count: 10
---

# Vilanterol
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

# Vilanterol: From Combination Bronchodilator Component to Obstructive Lung Disease

## One-Sentence Summary

Vilanterol is a long-acting beta2-agonist (LABA) used almost exclusively as a component of fixed-dose combination inhalers (with fluticasone furoate and/or umeclidinium) for COPD and asthma maintenance therapy; no standalone original indication is recorded in this evidence pack. The TxGNN model assigns an extremely high score to **Obstructive Lung Disease**, and this signal is strongly corroborated by real-world evidence, with **50 clinical trials** and **20 publications** — including landmark trials such as IMPACT and FULFIL — currently supporting this direction.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not separately recorded in this evidence pack; Vilanterol is used as a LABA component in COPD/asthma combination inhalers (fluticasone furoate/vilanterol, umeclidinium/vilanterol, fluticasone furoate/umeclidinium/vilanterol) |
| Predicted New Indication | Obstructive Lung Disease |
| TxGNN Prediction Score | 99.97% |
| Evidence Level | L1 |
| Norway Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available (DrugBank MOA field is a data gap). Based on known information, Vilanterol is a long-acting beta2-adrenergic agonist that is never marketed as a single agent — it is always combined with an inhaled corticosteroid (fluticasone furoate) and/or a long-acting muscarinic antagonist (umeclidinium) in products such as Relvar/Breo Ellipta, Anoro Ellipta, and Trelegy Ellipta.

The predicted indication, "obstructive lung disease," is essentially the umbrella category that already covers COPD and asthma — the two conditions these vilanterol-containing combinations are already approved and extensively studied for. This is not a novel mechanistic leap but a confirmatory signal: TxGNN has identified a relationship that is already densely supported by the existing evidence base for the drug class.

This explains both the very high prediction score and the unusually large volume of supporting evidence (50 trials, 20 publications), including a Phase 3 mortality-outcome trial (IMPACT, n=16,568) and multiple large comparative-effectiveness studies. The main caveat is that Vilanterol itself has no recorded monotherapy indication and is not currently marketed in Norway, so any pathway forward would need to address it strictly as part of a combination product.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT01313676](https://clinicaltrials.gov/study/NCT01313676) | Phase 3 | Completed | 16,568 | IMPACT trial: FF/UMEC/VI vs FF/VI vs UMEC/VI on survival in COPD patients with CV risk |
| [NCT01706198](https://clinicaltrials.gov/study/NCT01706198) | Phase 3 | Completed | 4,233 | FF/VI vs usual maintenance therapy — 12-month effectiveness study in asthma |
| [NCT02924688](https://clinicaltrials.gov/study/NCT02924688) | Phase 3 | Completed | 2,436 | FF/UMEC/VI vs FF/VI in inadequately controlled asthma |
| [NCT03034915](https://clinicaltrials.gov/study/NCT03034915) | Phase 4 | Completed | 2,696 | UMEC/VI vs UMEC vs Salmeterol, 24-week COPD comparison |
| [NCT02105974](https://clinicaltrials.gov/study/NCT02105974) | Phase 3 | Completed | 1,621 | FF/VI 100/25 vs VI 25 alone in COPD — lung function contribution study |
| [NCT02345161](https://clinicaltrials.gov/study/NCT02345161) | Phase 3 | Completed | 1,811 | FF/UMEC/VI vs budesonide/formoterol in COPD |
| [NCT01313650](https://clinicaltrials.gov/study/NCT01313650) | Phase 3 | Completed | 1,538 | GSK573719(UMEC)/VI and individual components vs placebo in COPD |
| [NCT04937387](https://clinicaltrials.gov/study/NCT04937387) | Phase 3 | Completed | 359 | FF/UMEC/VI vs FF/VI in Chinese participants with inadequately controlled asthma |
| [NCT05535972](https://clinicaltrials.gov/study/NCT05535972) | Phase 4 | Completed | 463 | Real-world effectiveness of Trelegy Ellipta (FF/UMEC/VI) in symptomatic COPD |
| [NCT03474081](https://clinicaltrials.gov/study/NCT03474081) | Phase 4 | Completed | 800 | Single inhaler triple therapy (FF/UMEC/VI) vs tiotropium monotherapy in COPD |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [29668352](https://pubmed.ncbi.nlm.nih.gov/29668352/) | 2018 | RCT | New England Journal of Medicine | IMPACT trial: once-daily single-inhaler triple vs dual therapy in COPD |
| [28375647](https://pubmed.ncbi.nlm.nih.gov/28375647/) | 2017 | RCT | Am J Respir Crit Care Med | FULFIL trial: once-daily triple therapy for COPD |
| [32918892](https://pubmed.ncbi.nlm.nih.gov/32918892/) | 2021 | RCT | Lancet Respiratory Medicine | CAPTAIN trial: FF/UMEC/VI vs FF/VI in inadequately controlled asthma |
| [32162970](https://pubmed.ncbi.nlm.nih.gov/32162970/) | 2020 | RCT (post-hoc) | Am J Respir Crit Care Med | Reduction in all-cause mortality with FF/UMEC/VI vs UMEC/VI (IMPACT follow-up) |
| [32299860](https://pubmed.ncbi.nlm.nih.gov/32299860/) | 2020 | RCT (subgroup) | European Respiratory Journal | Effect of exacerbation history on outcomes in the IMPACT trial |
| [35849317](https://pubmed.ncbi.nlm.nih.gov/35849317/) | 2022 | Network Meta-Analysis | Advances in Therapy | FF/UMEC/VI vs other triple/dual therapies for COPD |
| [39696097](https://pubmed.ncbi.nlm.nih.gov/39696097/) | 2024 | Systematic Review/Meta-analysis | BMC Pulmonary Medicine | UMEC/VI vs other bronchodilators in COPD management |
| [31389190](https://pubmed.ncbi.nlm.nih.gov/31389190/) | 2019 | Systematic Review | The Clinical Respiratory Journal | Fixed-dose UMEC/VI for COPD |
| [28956463](https://pubmed.ncbi.nlm.nih.gov/28956463/) | 2017 | Review | Expert Review of Respiratory Medicine | FF and vilanterol for treatment of COPD |
| [39797646](https://pubmed.ncbi.nlm.nih.gov/39797646/) | 2024 | Cohort Study | BMJ | Comparative effectiveness/safety of single-inhaler triple therapies in COPD (new-user cohort) |

---

## Norway Market Information

Vilanterol is currently not marketed in Norway, and no product authorizations are recorded (total licenses: 0). No license-level product details (authorization number, product name, dosage form, approved indication) are available in this evidence pack.

---

## Safety Considerations

Please refer to the package insert for safety information. No key warnings, contraindications, or drug-drug interaction data were available for evaluation (DDI query returned no results); this is flagged as a **Blocking** data gap (DG001) preventing a formal S1 safety assessment.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Efficacy evidence is exceptionally strong (L1: multiple large, completed Phase 3 RCTs including the landmark IMPACT and FULFIL trials, plus mortality-benefit data), but this evidence largely reconfirms Vilanterol's established role in COPD/asthma combination therapy rather than revealing a novel indication. Formal safety labeling and Norway market status data are both missing, which blocks a complete regulatory/safety evaluation.

**To proceed, the following is needed:**
- Official product label / SmPC (warnings, contraindications, DDI) to resolve the Blocking data gap (DG001)
- DrugBank/mechanism-of-action confirmation (DG002)
- Clarification of whether any monotherapy or combination-product pathway is planned for the Norway market, since Vilanterol has zero current authorizations there
- Confirmation that any "new indication" framing accounts for the fact that this is largely confirmatory evidence for an already-established combination-therapy use, not a de novo repurposing signal
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

