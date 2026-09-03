---
layout: default
title: Elbasvir
parent: 僅模型預測 (L5)
nav_order: 125
evidence_level: L5
indication_count: 10
---

# Elbasvir
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

# Elbasvir: From Hepatitis C Virus Infection to Hepatitis B Virus Infection

## One-Sentence Summary

Elbasvir is an NS5A inhibitor originally developed as a component of the fixed-dose combination Zepatier® (elbasvir/grazoprevir) for chronic hepatitis C virus (HCV) infection. The TxGNN model's top prediction suggests possible efficacy against **Hepatitis B virus infection**, but this is supported by **0 HBV-specific clinical trials** and **essentially no HBV-specific literature** — the underlying evidence base consists entirely of HCV trials and reviews, with the model's own rationale flagging the connection as likely a knowledge-graph artifact rather than a real pharmacological link.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Chronic hepatitis C virus (HCV) infection (as NS5A-inhibitor component of the grazoprevir/elbasvir combination, Zepatier®) |
| Predicted New Indication | Hepatitis B virus infection |
| TxGNN Prediction Score | 99.71% |
| Evidence Level | L4 |
| Norway Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Elbasvir is a hepatitis C virus (HCV)-specific NS5A protein inhibitor that acts on the Hepacivirus replication complex. Its efficacy has been extensively demonstrated in combination with the NS3/4A protease inhibitor grazoprevir for HCV genotypes 1, 4, and 6, including in cirrhotic, HIV-coinfected, renally impaired, and transplant populations.

Hepatitis B virus (HBV), however, belongs to the Hepadnaviridae family and replicates via a reverse transcriptase mechanism entirely distinct from HCV's RNA-dependent RNA polymerase / NS5A-based replication complex. HBV does not express an NS5A homolog, so there is no known direct molecular target overlap between elbasvir's mechanism of action and HBV biology.

The evidence pack's own repurposing rationale is explicit on this point: the high TxGNN score most likely reflects semantic proximity of "viral hepatitis" as a disease category within the knowledge graph, rather than a genuine pharmacological signal. This is corroborated by the fact that all associated clinical trials and literature in the evidence pack pertain to HCV (and its comorbidities — HIV, chronic kidney disease, transplantation), with no experimental or clinical data testing elbasvir against HBV. Notably, the remaining 9 TxGNN candidates for this drug (hepatitis E, hepatitis A, animal viral hepatitis, Omsk hemorrhagic fever, Kyasanur forest disease, HIV, feline AIDS, SIV, and an unrelated neurodevelopmental disorder) show comparably weak or absent mechanistic support, suggesting the model's overall prediction set for elbasvir clusters around a "viral/hepatitis" semantic neighborhood rather than validated drug-target biology.

---

## Clinical Trial Evidence

*(Extracted from the top-ranked candidate: Hepatitis B virus infection — note: all trials below studied elbasvir for HCV, not HBV; none directly test HBV efficacy)*

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT02332720](https://clinicaltrials.gov/study/NCT02332720) | Phase 2 | Completed | 413 | Grazoprevir + uprifosbuvir with elbasvir or ruzasvir ± ribavirin in chronic HCV GT3/4/5/6; graded "C" — HCV population, not HBV |
| [NCT03423641](https://clinicaltrials.gov/study/NCT03423641) | N/A | Completed | 33,808 | Real-world safety comparison of DAA-treated vs. untreated HCV patients; no HBV arm |
| [NCT03823911](https://clinicaltrials.gov/study/NCT03823911) | Phase 4 | Completed | 87 | Cardiovascular risk outcomes after HCV eradication in HIV/HCV coinfection; not HBV-related |
| [NCT01532973](https://clinicaltrials.gov/study/NCT01532973) | Phase 1 | Completed | 48 | PK/PD study of elbasvir monotherapy in HCV-infected males (GT1/GT3); no HBV cohort |
| [NCT02105688](https://clinicaltrials.gov/study/NCT02105688) | Phase 3 | Completed | 301 | Grazoprevir/elbasvir in treatment-naïve HCV GT1/4/6 on opiate substitution therapy; graded "C" — HCV only |
| [NCT03797066](https://clinicaltrials.gov/study/NCT03797066) | Phase 4 | Terminated | 13 | Point-of-care test-and-treat with grazoprevir/elbasvir in homeless HCV GT1/4 population |
| [NCT02332707](https://clinicaltrials.gov/study/NCT02332707) | Phase 2 | Completed | 443 | Grazoprevir/uprifosbuvir with elbasvir or ruzasvir in HCV GT1/2 |
| [NCT02600325](https://clinicaltrials.gov/study/NCT02600325) | Phase 3 | Completed | 80 | Grazoprevir/elbasvir for acute HCV GT1/4 in HIV-positive patients (DAHHS-2); graded "C" — HCV only |
| [NCT01717326](https://clinicaltrials.gov/study/NCT01717326) | Phase 2 | Completed | 573 | Grazoprevir/elbasvir ± ribavirin, SVR12 as primary endpoint in chronic HCV |
| [NCT01932762](https://clinicaltrials.gov/study/NCT01932762) | Phase 2 | Completed | 98 | Grazoprevir ± elbasvir ± ribavirin in treatment-naïve HCV GT2/4/5/6 |

**None of the listed trials enrolled HBV-infected patients or tested elbasvir's antiviral activity against HBV.**

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [25529080](https://pubmed.ncbi.nlm.nih.gov/25529080/) | 2015 | Review | Liver International | Discusses progress toward HCV eradication and HBV "functional cure" strategies as parallel but mechanistically distinct goals; does not propose elbasvir for HBV |
| [41734217](https://pubmed.ncbi.nlm.nih.gov/41734217/) | 2025 | Review | Klinicka mikrobiologie a infekcni lekarstvi | Retrospective review of antiviral treatment patterns for chronic HBV and HCV in children (Ostrava); covers standard-of-care agents, not elbasvir-specific HBV data |
| [26904396](https://pubmed.ncbi.nlm.nih.gov/26904396/) | 2016 | Review (pending classification) | Acta Pharmaceutica Sinica B | Explicitly distinguishes HCV (curable, DAA-targetable via NS3/4A, NS5B, NS5A) from HBV and HIV, which lack these same druggable targets — directly supports the mechanistic implausibility noted above |
| [32039536](https://pubmed.ncbi.nlm.nih.gov/32039536/) | 2020 | pending | Journal of Viral Hepatitis | Real-world Taiwan cohort on liver/renal adverse effects of elbasvir/grazoprevir in HCV GT1 patients; safety data only, no HBV relevance |
| [31114957](https://pubmed.ncbi.nlm.nih.gov/31114957/) | 2019 | pending | Clinical Pharmacokinetics | 2019 update on HCV DAA pharmacokinetics/pharmacodynamics, including elbasvir/grazoprevir; HCV-focused |

**No literature reports elbasvir efficacy, in vitro activity, or clinical experience specifically against HBV.**

---

## Norway Market Information

No marketing authorizations are currently registered in Norway. The drug (elbasvir, DrugBank ID DB11574) has a market status of "Not Marketed" with 0 total licenses on file.

---

## Safety Considerations

Please refer to the package insert for safety information. (Key warnings, contraindications, and drug interaction data are currently unavailable — DDI query returned no results, and TFDA/label warning data collection is flagged as a blocking data gap pending PDF label retrieval and parsing.)

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Elbasvir's mechanism (HCV-specific NS5A inhibition of the Hepacivirus replication complex) has no known target overlap with HBV, which replicates via a distinct reverse-transcriptase-dependent pathway. All available clinical trial and literature evidence in the pack concerns HCV (and its comorbidities), with zero direct evidence — clinical, in vitro, or mechanistic — of anti-HBV activity. The remaining 9 TxGNN candidates for this drug show similarly weak or non-existent support, suggesting the prediction set reflects knowledge-graph clustering around "viral hepatitis" rather than validated pharmacology.

**To proceed, the following is needed:**
- Formal MOA and drug classification data from DrugBank (currently a High-severity data gap, DG002)
- TFDA/Norwegian label warnings and contraindications (currently a Blocking data gap, DG001), required before any S1 safety screening
- In vitro or preclinical evidence of elbasvir activity against HBV replication (e.g., HBV cell culture or animal model data) before further evidence escalation is warranted
- If no such preclinical signal emerges, this candidate should be deprioritized in favor of ranks with stronger mechanistic plausibility
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

