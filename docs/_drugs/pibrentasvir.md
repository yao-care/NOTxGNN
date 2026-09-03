---
layout: default
title: Pibrentasvir
parent: 僅模型預測 (L5)
nav_order: 278
evidence_level: L5
indication_count: 10
---

# Pibrentasvir
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

# Pibrentasvir: From Hepatitis C Virus Infection to Hepatitis B Virus Infection

## One-Sentence Summary

> Pibrentasvir is an NS5A inhibitor marketed only as part of the fixed-dose combination glecaprevir/pibrentasvir, used to treat chronic Hepatitis C virus (HCV) infection.
> The TxGNN model predicts it may also be effective for **Hepatitis B virus infection**, with a very high similarity score (**99.84%**),
> but on inspection **none of the 14 supporting clinical trials or 20 literature citations actually test pibrentasvir against HBV** — all are HCV studies. This prediction should be treated as a likely knowledge-graph artifact rather than a genuine repurposing signal.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Chronic Hepatitis C virus (HCV) infection, genotype 1–6 (as component of glecaprevir/pibrentasvir combination) |
| Predicted New Indication | Hepatitis B virus infection |
| TxGNN Prediction Score | 99.84% |
| Evidence Level | L5 (model prediction only — no study directly evaluates pibrentasvir in HBV) |
| Norway Market Status | ✗ Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data for pibrentasvir is not available from the structured DrugBank record (Data Gap). Based on known information, pibrentasvir is the NS5A-inhibitor component of the fixed-dose combination glecaprevir/pibrentasvir (Maviret/Mavyret), and its efficacy has been established specifically for chronic HCV infection through the large ENDURANCE, EXPEDITION, SURVEYOR, and CERTAIN Phase 2/3 programs.

Mechanistically, pibrentasvir is highly selective for the HCV NS5A protein, which is essential for HCV replication-complex assembly and virion packaging. HBV is a hepadnavirus that replicates via reverse transcription of a pregenomic RNA using its own polymerase and does not encode an NS5A homolog — there is no known molecular target shared between the two viruses. Consistent with this, every clinical trial and nearly every publication retrieved under this "predicted indication" is in fact an HCV trial (in some cases in patients co-infected with, or screened for, HBV/HIV as a safety consideration), not a trial evaluating antiviral activity against HBV itself.

This pattern is not isolated to HBV: the same evidence pack shows equally high TxGNN scores for HIV, hepatitis A, hepatitis E, animal viral hepatitis, Omsk hemorrhagic fever, Kyasanur forest disease, simian/feline immunodeficiency virus infection, and even an unrelated rare neurodevelopmental disorder — none supported by mechanistically plausible or disease-specific evidence. This suggests the model is clustering pibrentasvir with a broad "viral hepatitis / co-infection" node neighborhood in the knowledge graph rather than identifying a real pharmacological relationship to HBV.

---

## Clinical Trial Evidence

All trials below were retrieved as "top evidence" for the HBV prediction, but per the evidence pack's own relevance grading (grade C), every one is actually an HCV trial for glecaprevir/pibrentasvir — none enrolled or evaluated HBV-infected patients for antiviral efficacy.

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT01995071](https://clinicaltrials.gov/study/NCT01995071) | Phase 2 | Completed | 89 | Dose-ranging safety/antiviral activity of ABT-493+ABT-530 (glecaprevir/pibrentasvir) in **HCV** genotype 1 — not an HBV trial |
| [NCT02640157](https://clinicaltrials.gov/study/NCT02640157) | Phase 3 | Completed | 506 | ENDURANCE-3: G/P vs sofosbuvir+daclatasvir in **HCV** genotype 3 — not an HBV trial |
| [NCT03823911](https://clinicaltrials.gov/study/NCT03823911) | Phase 4 | Completed | 87 | Cardiovascular outcomes after **HCV** cure in HIV co-infected patients — not an HBV trial |
| [NCT02707952](https://clinicaltrials.gov/study/NCT02707952) | Phase 3 | Completed | 295 | CERTAIN-1: G/P efficacy/safety in Japanese **HCV** patients — not an HBV trial |
| [NCT03092375](https://clinicaltrials.gov/study/NCT03092375) | Phase 3 | Completed | 177 | G/P ± ribavirin in NS5A-inhibitor-experienced **HCV** GT1 patients — not an HBV trial |
| [NCT03219216](https://clinicaltrials.gov/study/NCT03219216) | Phase 3 | Completed | 100 | G/P in treatment-naïve Brazilian **HCV** GT1–6 patients — not an HBV trial |
| [NCT02441283](https://clinicaltrials.gov/study/NCT02441283) | Phase 2/3 | Completed | 384 | Long-term durability/resistance follow-up of glecaprevir/pibrentasvir in **HCV** — not an HBV trial |
| [NCT02446717](https://clinicaltrials.gov/study/NCT02446717) | Phase 2/3 | Completed | 141 | G/P ± ribavirin in **HCV** patients who failed prior DAA therapy — not an HBV trial |
| [NCT02243280](https://clinicaltrials.gov/study/NCT02243280) | Phase 2 | Completed | 174 | SURVEYOR-I: G/P PK/efficacy in **HCV** GT1,4,5,6 — not an HBV trial |
| [NCT02640482](https://clinicaltrials.gov/study/NCT02640482) | Phase 3 | Completed | 304 | ENDURANCE-2: placebo-controlled G/P trial in **HCV** GT2 — not an HBV trial |

**No trial in this evidence set enrolled patients for the purpose of treating or evaluating HBV infection.**

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [29485084](https://pubmed.ncbi.nlm.nih.gov/29485084/) | 2018 | Review | Lancet Infect Dis | Discusses need for HBV vaccination *after* successful HCV treatment — a co-infection/prevention topic, not evidence of pibrentasvir activity against HBV |
| [34092970](https://pubmed.ncbi.nlm.nih.gov/34092970/) | 2021 | Review | World J Gastroenterol | Overview of pediatric HBV/HCV management; notes current HBV therapies are not curative — contextual background only |
| [41734217](https://pubmed.ncbi.nlm.nih.gov/41734217/) | 2025 | Retrospective | Klin Mikrobiol Infekc Lek | Retrospective review of antiviral treatment frequency/efficacy for chronic HBV and HCV in children — does not test pibrentasvir in HBV |
| [40414600](https://pubmed.ncbi.nlm.nih.gov/40414600/) | 2025 | Cross-sectional | Annals of Hepatology | Compares HBV vs HCV drug **pricing** across countries — economic analysis, no efficacy data |
| [31981264](https://pubmed.ncbi.nlm.nih.gov/31981264/) | 2020 | Cohort | J Viral Hepatitis | Real-world GLE/PIB effectiveness/safety in **HCV** patients with severe renal impairment (Taiwan) — HCV only |
| [35431505](https://pubmed.ncbi.nlm.nih.gov/35431505/) | 2022 | Cohort | World J Gastroenterol | Real-world DAA effectiveness in HIV/**HCV** genotype 6 co-infection — HCV only |
| [30982721](https://pubmed.ncbi.nlm.nih.gov/30982721/) | 2019 | Review | Lancet Gastroenterol Hepatol | HCV treatment in children/adolescents within global viral hepatitis elimination strategy — HCV-focused |
| [35579223](https://pubmed.ncbi.nlm.nih.gov/35579223/) | 2022 | Review | Eur J Gen Pract | General overview of chronic HCV diagnosis and treatment — HCV only |
| [34298832](https://pubmed.ncbi.nlm.nih.gov/34298832/) | 2021 | Review | Cancers | Hepatocellular carcinoma risk in chronic kidney disease — not specific to pibrentasvir or HBV |
| [31114957](https://pubmed.ncbi.nlm.nih.gov/31114957/) | 2019 | Review | Clin Pharmacokinetics | PK/PD review of HCV DAA regimens including glecaprevir/pibrentasvir — HCV only |

**No publication in this set reports direct antiviral efficacy or clinical outcome data for pibrentasvir against HBV.**

---

## Norway Market Information

Pibrentasvir currently has **no marketing authorization in Norway** (0 licenses on file; market status: Not marketed). No product/authorization records are available to summarize.

---

## Safety Considerations

Please refer to the package insert for safety information. (Key warnings, contraindications, and drug interaction data are not yet available in this evidence pack — retrieval of the TFDA/manufacturer label is flagged as a **Blocking** data gap.)

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Despite a high TxGNN similarity score, every clinical trial and nearly every publication supporting this "HBV" prediction is actually evidence for pibrentasvir's established HCV indication — none test HBV-specific antiviral activity. Pibrentasvir's mechanism (selective HCV NS5A inhibition) has no known counterpart target in HBV, and the same implausible pattern (HIV, hepatitis A/E, veterinary lentivirus infections, even an unrelated neurodevelopmental disorder) appears across this drug's entire top-10 prediction list, indicating a likely knowledge-graph clustering artifact rather than a genuine repurposing signal. Combined with the drug being unmarketed in Norway and a Blocking gap on core safety labeling, there is no basis to advance this candidate at this time.

**To proceed, the following is needed:**
- Genuine in vitro/in vivo evidence of pibrentasvir antiviral activity against HBV (currently none exists)
- TFDA/manufacturer package insert for warnings and contraindications (Blocking data gap)
- Verified mechanism-of-action documentation from DrugBank (High-severity data gap)
- A sanity check on TxGNN's disease-embedding neighborhood for this drug, given the pattern of implausible high-scoring predictions across the full candidate list
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

