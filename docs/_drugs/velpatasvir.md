---
layout: default
title: Velpatasvir
parent: 僅模型預測 (L5)
nav_order: 380
evidence_level: L5
indication_count: 10
---

# Velpatasvir
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

# Velpatasvir: From Hepatitis C Virus Infection to Hepatitis B Virus Infection

## One-Sentence Summary

> Velpatasvir is an NS5A inhibitor originally developed as part of combination antiviral therapy (Sofosbuvir/Velpatasvir, brand Epclusa; and Sofosbuvir/Velpatasvir/Voxilaprevir, brand Vosevi) for chronic **Hepatitis C virus (HCV) infection**.
> The TxGNN model predicts it may also be effective for **Hepatitis B virus (HBV) infection**,
> with **26 clinical trials** and **20 publications** nominally linked to this prediction — however, on closer review nearly all of this evidence actually concerns HCV treatment, not HBV, which substantially weakens the case for repurposing.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Chronic Hepatitis C virus infection (component of Sofosbuvir/Velpatasvir [Epclusa] and Sofosbuvir/Velpatasvir/Voxilaprevir [Vosevi] combination regimens) |
| Predicted New Indication | Hepatitis B virus infection |
| TxGNN Prediction Score | 99.87% (rank 1936) |
| Evidence Level | L4 |
| Norway Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, a validated, structured mechanism-of-action record is not available for Velpatasvir in this evidence pack (flagged as a High-severity data gap). Based on the surrounding trial and literature context, Velpatasvir is known to act as a pangenotypic **HCV NS5A inhibitor**, used exclusively in fixed-dose combination with sofosbuvir (± voxilaprevir) for chronic hepatitis C across genotypes 1–6.

Hepatitis C and Hepatitis B share only a superficial relationship: both are classified as "viral hepatitis" and cause liver inflammation, but they are caused by entirely unrelated viruses — HCV is a single-stranded RNA *Flaviviridae* virus that depends on an NS5A/NS5B replication complex, while HBV is a partially double-stranded DNA *Hepadnaviridae* virus that replicates via reverse transcriptase and a cccDNA reservoir in the nucleus. There is no known structural or functional homolog of NS5A in the HBV replication cycle.

Because of this, the mechanistic rationale for repurposing is explicitly assessed as **weak** in this pack ("HBV 為 DNA 病毒、複製機轉與 HCV 完全不同，無同源標的，機轉關聯薄弱"). Consistent with this, when the underlying evidence is inspected, the large majority of "supporting" trials and publications are in fact HCV treatment studies that happen to co-occur with hepatitis B in the knowledge graph (e.g., HCV/HBV coinfection cohorts, or general "viral hepatitis" review articles) — not direct evidence of anti-HBV activity for Velpatasvir. This pattern is best interpreted as a knowledge-graph co-occurrence artifact rather than a genuine biological signal.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT04997564](https://clinicaltrials.gov/study/NCT04997564) | Phase 4 | Unknown | 120 | 12-week SOF/VEL for HCV/HBV co-infected patients, with prophylactic tenofovir alafenamide (TAF) to prevent HBV reactivation — the only trial in this set that directly addresses HBV management, but as a *reactivation-prevention* strategy, not as a Velpatasvir efficacy study against HBV. |
| [NCT02996682](https://clinicaltrials.gov/study/NCT02996682) | Phase 3 | Completed | 102 | SOF/VEL ± ribavirin for chronic **HCV** infection with decompensated cirrhosis. |
| [NCT02201901](https://clinicaltrials.gov/study/NCT02201901) | Phase 3 | Completed | 268 | SOF/VEL FDC for chronic **HCV** with Child-Pugh Class B cirrhosis. |
| [NCT02625909](https://clinicaltrials.gov/study/NCT02625909) | Phase 3 | Completed | 222 | Shortened SOF/VEL interferon-free therapy for recently acquired **HCV** in people who inject drugs and HIV coinfection. |
| [NCT01858766](https://clinicaltrials.gov/study/NCT01858766) | Phase 2 | Completed | 379 | SOF + VEL ± ribavirin in treatment-naive chronic **HCV** (genotypes 1–6). |
| [NCT04695769](https://clinicaltrials.gov/study/NCT04695769) | Phase 4 | Completed | 281 | Ribavirin + SOF/VEL/VOX in **HCV** non-responder retreatment. |
| [NCT03823911](https://clinicaltrials.gov/study/NCT03823911) | Phase 4 | Completed | 87 | Cardiovascular outcomes after **HCV** eradication with DAAs in HIV/HCV coinfection. |
| [NCT02533427](https://clinicaltrials.gov/study/NCT02533427) | Phase 1 | Completed | 15 | Drug interaction study: effect of SOF/VEL/VOX on a hormonal contraceptive; not disease-specific. |
| [NCT03570112](https://clinicaltrials.gov/study/NCT03570112) | N/A | Completed | 40 | Natural history and vertical transmission of chronic **HCV** in pregnancy, treated postpartum with Epclusa. |
| [NCT05016609](https://clinicaltrials.gov/study/NCT05016609) | Phase 4 | Unknown | 1800 | Point-of-care **HCV** testing/treatment model among people who inject drugs. |

⚠️ **Relevance note:** Of the 26 trials retrieved under this prediction, only one (NCT04997564) touches HBV at all, and even that is a prophylaxis-against-reactivation design, not a treatment trial of Velpatasvir for HBV. All others are HCV-specific trials that were matched to this prediction through shared "viral hepatitis" context rather than direct HBV evidence.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [31542053](https://pubmed.ncbi.nlm.nih.gov/31542053/) | 2019 | Case Report | J Med Case Rep | HBV reactivation (with an HBsAg immune-escape mutant) in an HBcAb-positive patient while being treated with sofosbuvir/velpatasvir for HCV — a safety signal, not evidence of anti-HBV efficacy. |
| [34092970](https://pubmed.ncbi.nlm.nih.gov/34092970/) | 2021 | Review | World J Gastroenterol | Reviews pediatric HBV and HCV management; notes HCV DAAs (including SOF/VEL) are curative, while HBV treatment remains non-curative and mechanistically distinct. |
| [29369303](https://pubmed.ncbi.nlm.nih.gov/29369303/) | 2018 | Conference Report | AIDS Rev | International Conference on Viral Hepatitis 2017 report covering global HBV and HCV burden and eradication roadmaps — general context, no drug-specific HBV data. |
| [41734217](https://pubmed.ncbi.nlm.nih.gov/41734217/) | 2025 | Retrospective | Klin Mikrobiol Infekc Lek | Retrospective review of antiviral treatment for chronic HBV and HCV in children in Ostrava; HBV and HCV therapies discussed separately. |
| [40414600](https://pubmed.ncbi.nlm.nih.gov/40414600/) | 2025 | Cross-sectional | Ann Hepatol | Global pricing comparison of HBV and HCV antiviral therapies; no efficacy data. |
| [32935438](https://pubmed.ncbi.nlm.nih.gov/32935438/) | 2021 | Cohort | J Viral Hepat | Myanmar HCV treatment program; HBV-coinfected participants were treated concurrently with **tenofovir** (not velpatasvir) alongside SOF/VEL for their HCV. |
| [39735164](https://pubmed.ncbi.nlm.nih.gov/39735164/) | 2024 | Real-world Cohort | J Virus Erad | Real-life SOF/VEL effectiveness/safety in Chinese HCV patients, including those with HCV/HBV coinfection; focus remains on HCV clearance. |
| [35248213](https://pubmed.ncbi.nlm.nih.gov/35248213/) | 2022 | Cohort | Lancet Gastroenterol Hepatol | SHARED-3 trial: SOF/VEL safety and efficacy in treatment-naive **HCV** genotype 4 patients in Rwanda. |
| [33217040](https://pubmed.ncbi.nlm.nih.gov/33217040/) | 2021 | Real-world Cohort | J Gastroenterol Hepatol | Real-world SOF/VEL ± ribavirin efficacy/safety in **HCV** genotype 3 patients. |
| [31114957](https://pubmed.ncbi.nlm.nih.gov/31114957/) | 2019 | Review | Clin Pharmacokinet | PK/PD review of HCV DAA regimens including sofosbuvir/velpatasvir; HCV-specific. |

⚠️ **Relevance note:** Only PMID 31542053 discusses HBV directly, and it describes a reactivation risk rather than therapeutic benefit. The remaining literature is either HCV-specific or discusses HBV and HCV in parallel without providing mechanistic or clinical evidence that Velpatasvir treats HBV.

---

## Norway Market Information

Velpatasvir currently has **no marketing authorization on file in Norway** (0 licenses recorded). It is only known globally as a component of fixed-dose combination products (e.g., Epclusa: sofosbuvir/velpatasvir; Vosevi: sofosbuvir/velpatasvir/voxilaprevir), both indicated for chronic hepatitis C — no monotherapy or HBV-indicated product exists.

---

## Safety Considerations

Please refer to the package insert for safety information. (TFDA label warnings/contraindications and DrugBank DDI data are not currently available for this candidate — see Next Steps.)

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Although a substantial volume of trials and publications is nominally linked to this prediction, almost all of it evaluates Velpatasvir's established use in HCV rather than HBV, and there is no known homologous drug target between the HCV NS5A protein and the HBV replication machinery. The evidence level (L4) reflects mechanism-level plausibility at best, not a validated therapeutic signal, and the pack's own scoring assigns this candidate "Hold." The nine lower-ranked candidates in this evidence pack (Hepatitis E, Hepatitis A, animal viral hepatitis, Omsk hemorrhagic fever, Kyasanur forest disease, HIV, feline AIDS, SIV infection, and an unrelated neurodevelopmental disorder) show even weaker or entirely absent direct evidence and are similarly held or flagged as noise/research-question only.

**To proceed, the following is needed:**
- TFDA/regulatory label data (warnings, contraindications) — currently a blocking data gap (DG001)
- Confirmed DrugBank mechanism-of-action record (DG002)
- In vitro or preclinical evidence of Velpatasvir activity against HBV replication (e.g., cccDNA transcription, polymerase inhibition) before any further clinical consideration
- Re-triage of the clinical trial/literature evidence set to remove HCV-only mismatches and identify any genuinely HBV-specific data, if such data exist
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

