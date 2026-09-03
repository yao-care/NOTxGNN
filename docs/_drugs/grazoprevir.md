---
layout: default
title: Grazoprevir
parent: 僅模型預測 (L5)
nav_order: 168
evidence_level: L5
indication_count: 10
---

# Grazoprevir
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

# Grazoprevir: From Chronic Hepatitis C to HIV Infectious Disease

## One-Sentence Summary

> Grazoprevir is an HCV NS3/4A protease inhibitor, marketed in combination with elbasvir (e.g., Zepatier) for chronic hepatitis C genotype 1/4/6 infection.
> The TxGNN model predicts it may be effective for **HIV infectious disease**, with a very high score (**99.73%**) and **14 clinical trials** plus **20 publications** superficially linked to this indication.
> However, on closer inspection, essentially all of this evidence concerns treating **HCV in HIV/HCV co-infected patients** — not treating HIV itself — and the drug has no known mechanistic target in HIV. This prediction should be treated as a likely **confounded/false-positive signal**, not a genuine repurposing candidate.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not captured in structured data (see Data Gap DG002). Based on literature in this pack, grazoprevir is used as part of the elbasvir/grazoprevir combination for chronic hepatitis C (genotype 1, 4, 6) |
| Predicted New Indication | HIV infectious disease |
| TxGNN Prediction Score | 99.73% |
| Evidence Level | L4 |
| Norway Market Status | Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this evidence pack (Data Gap DG002). Based on the literature that is available, grazoprevir is an **HCV NS3/4A serine protease inhibitor**, formulated together with elbasvir (an NS5A inhibitor) as a fixed-dose combination for chronic HCV genotype 1, 4, and 6 infection.

Critically, HIV does not have a homologous target: HIV relies on an **aspartic protease** (HIV protease) for viral maturation, structurally and catalytically unrelated to the HCV NS3/4A serine protease that grazoprevir inhibits. There is no known biochemical mechanism by which grazoprevir would inhibit HIV replication.

The 14 clinical trials and 20 publications associated with this prediction almost entirely describe studies of **HCV treatment in patients who are also HIV-positive** (i.e., HIV/HCV co-infection populations), with virologic endpoints defined by HCV RNA clearance (SVR12), not HIV viral suppression. The repurposing rationale supplied with this evidence pack explicitly flags this: the high TxGNN score likely reflects a **confounded association** — grazoprevir and "HIV" co-occur frequently in the training corpus because trials enroll HIV/HCV co-infected subjects, not because grazoprevir has anti-HIV activity. This prediction should be interpreted as a probable **embedding artifact of co-occurrence**, not a mechanistically grounded repurposing hypothesis.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT02897596](https://clinicaltrials.gov/study/NCT02897596) | Phase 3 | Unknown | 62 | GZR/EBR for early chronic HCV GT1/4 in HIV/HCV co-infected patients; endpoint is HCV cure, not HIV treatment |
| [NCT02785666](https://clinicaltrials.gov/study/NCT02785666) | Phase 3 | Completed | 150 | Swiss HIV Cohort "treat, counsel, cure" strategy for HCV in HIV-positive MSM |
| [NCT03037151](https://clinicaltrials.gov/study/NCT03037151) | Phase 4 | Unknown | 100 | GZR+EBR safety/fibrosis outcomes in HCV GT1/GT6 with or without HIV |
| [NCT02105662](https://clinicaltrials.gov/study/NCT02105662) | Phase 3 | Completed | 218 | GZR+EBR efficacy/safety for chronic HCV GT1/4/6 in HIV co-infected, treatment-naïve subjects |
| [NCT03823911](https://clinicaltrials.gov/study/NCT03823911) | Phase 4 | Completed | 87 | Cardiovascular risk after HCV eradication in HIV mono- vs HIV/HCV co-infected patients; not an HIV efficacy endpoint |
| [NCT02252016](https://clinicaltrials.gov/study/NCT02252016) | Phase 3 | Completed | 159 | GZR+EBR in HCV GT1/4/6 patients with inherited blood disorders, with/without HIV co-infection |
| [NCT02057003](https://clinicaltrials.gov/study/NCT02057003) | N/A | Unknown | 1000 | HEPAVIR real-world cohort: DAA regimens (incl. GZR-based) in HIV/HCV co-infected patients |
| [NCT03098121](https://clinicaltrials.gov/study/NCT03098121) | Phase 4 | Completed | 40 | GZR+EBR in PWID/MSM with GT1 HCV and HIV co-infection, prior peginterferon/ribavirin experience |
| [NCT02600325](https://clinicaltrials.gov/study/NCT02600325) | Phase 3 | Completed | 80 | DAHHS-2: GZR+EBR for acute HCV GT1/4 in HIV-positive patients |
| [NCT03407703](https://clinicaltrials.gov/study/NCT03407703) | N/A | Unknown | 50 | Kidney function impact of EBR/GZR HCV treatment in adults with/without HIV |

*All 10 trials above evaluate HCV treatment outcomes in HIV/HCV co-infected populations; none report an HIV virologic or immunologic endpoint for grazoprevir.*

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [26423374](https://pubmed.ncbi.nlm.nih.gov/26423374/) | 2015 | Non-randomised trial | The Lancet HIV | C-EDGE CO-INFECTION: efficacy/safety of GZR+EBR for HCV in HIV/HCV co-infected patients |
| [25467560](https://pubmed.ncbi.nlm.nih.gov/25467560/) | 2015 | Phase 2 RCT | The Lancet | C-WORTHY: 8 vs 12 weeks GZR+EBR ± ribavirin in HCV mono-infection and HIV/HCV co-infection |
| [32246857](https://pubmed.ncbi.nlm.nih.gov/32246857/) | 2020 | Systematic review / network meta-analysis | J Gastroenterol Hepatol | Efficacy/safety of DAA regimens (incl. GZR-based) for HCV in HIV/HCV co-infection |
| [28689442](https://pubmed.ncbi.nlm.nih.gov/28689442/) | 2017 | Review | Expert Opin Drug Metab Toxicol | Drug-drug interactions between DAAs (incl. grazoprevir) and antiretrovirals in HIV-infected HCV patients |
| [30745392](https://pubmed.ncbi.nlm.nih.gov/30745392/) | 2019 | PK study | Antimicrob Agents Chemother | Pharmacokinetic interactions between elbasvir/grazoprevir and HIV protease inhibitors (ritonavir, atazanavir, lopinavir, darunavir) |
| [30541077](https://pubmed.ncbi.nlm.nih.gov/30541077/) | 2019 | PK study | J Antimicrob Chemother | Drug interaction potential between elbasvir/grazoprevir and HIV integrase inhibitors (raltegravir, dolutegravir) |
| [28417245](https://pubmed.ncbi.nlm.nih.gov/28417245/) | 2017 | Review | Drugs | Elbasvir/grazoprevir review, including use in chronic HCV genotype 1/4 with HIV co-infection |
| [27091555](https://pubmed.ncbi.nlm.nih.gov/27091555/) | 2016 | Review | Expert Opin Drug Saf | Safety and efficacy of elbasvir/grazoprevir for HCV genotypes 1, 4, 6 |
| [30233138](https://pubmed.ncbi.nlm.nih.gov/30233138/) | 2018 | Review | Drug Des Devel Ther | Current evidence on safety/efficacy of elbasvir/grazoprevir for chronic HCV |
| [26849059](https://pubmed.ncbi.nlm.nih.gov/26849059/) | 2016 | Review | Expert Opin Drug Metab Toxicol | Pharmacodynamics/pharmacokinetics of elbasvir and grazoprevir in HCV treatment |

*None of the above literature reports a direct antiviral effect of grazoprevir against HIV; the recurring theme is HCV treatment efficacy and DDI management in HIV-positive/co-infected patients.*

---

## Norway Market Information

No Norway marketing authorizations were found for grazoprevir in this evidence pack (`market_status`: 未上市 / Not Marketed; `total_licenses`: 0; `licenses`: empty).

---

## Safety Considerations

Please refer to the package insert for safety information.

*(All fields in `safety.key_warnings`, `safety.contraindications`, and `safety.ddi` are marked as Data Gap / not found in this evidence pack — see DG001, "Blocking" severity, which prevents entry into the S1 safety pre-assessment stage.)*

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN score (99.73%) is high, but the supporting clinical trial and literature evidence is systematically confounded — it reflects HCV treatment in HIV/HCV co-infected populations, not any demonstrated anti-HIV activity. Grazoprevir has no known mechanistic target in HIV (its target, HCV NS3/4A serine protease, has no HIV homolog). Combined with the absence of Norway market presence, MOA data, and TFDA safety data (a Blocking data gap), this candidate does not meet the threshold to advance beyond S0.

**To proceed, the following is needed:**
- Confirmed original indication and MOA data from DrugBank (DG002)
- TFDA/regulatory package insert warnings and contraindications (DG001, Blocking — required before any S1 safety pre-assessment)
- Independent mechanistic or in vitro evidence of anti-HIV activity, if any exists, to distinguish true signal from co-occurrence confounding
- Re-classification of relevance grades for the "pending" trials/literature to confirm none report a direct HIV virologic endpoint
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

