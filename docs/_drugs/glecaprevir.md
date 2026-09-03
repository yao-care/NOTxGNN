---
layout: default
title: Glecaprevir
parent: 僅模型預測 (L5)
nav_order: 162
evidence_level: L5
indication_count: 10
---

# Glecaprevir
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

# Glecaprevir: From Hepatitis C Virus Infection to HIV Infectious Disease

## One-Sentence Summary

> Glecaprevir is an NS3/4A protease inhibitor originally developed (as the glecaprevir/pibrentasvir combination, e.g. Mavyret/Maviret) for chronic hepatitis C virus (HCV) infection.
> The TxGNN model ranks **HIV infectious disease** as its #1 predicted new indication with a **99.87% score**,
> but the supporting evidence — **15 clinical trials** and **19 publications** — almost entirely describes HCV treatment in HIV/HCV co-infected populations, not direct antiretroviral activity, and the drug's own repurposing rationale flags this as a likely false positive.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Chronic Hepatitis C Virus (HCV) infection *(inferred from clinical trial corpus in this evidence pack — DrugBank `original_indications` and `original_moa` fields were empty/Data Gap)* |
| Predicted New Indication | HIV infectious disease |
| TxGNN Prediction Score | 99.87% (rank 1845) |
| Evidence Level | L4 |
| Norway Market Status | ✗ Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | **Hold** |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data for glecaprevir is not available in the supplied DrugBank record (Data Gap). Based on the clinical trial evidence in this pack, glecaprevir is well established as an **NS3/4A serine protease inhibitor**, co-formulated with the NS5A inhibitor pibrentasvir, for pan-genotypic chronic HCV infection. It has no documented affinity for HIV protease or any other HIV replication target.

Mechanistically, HCV (Flaviviridae) and HIV (Retroviridae) belong to unrelated viral families with structurally distinct protease enzymes; there is no known cross-reactivity. The high TxGNN score most plausibly reflects a **comorbidity confounder** rather than a genuine pharmacological signal: nearly every trial retrieved for this candidate enrolled HIV/HCV co-infected patients in whom glecaprevir/pibrentasvir was used to cure the *HCV* component, while HIV was managed separately with antiretroviral therapy. One retrieved trial (NCT02634008) does not even involve glecaprevir — it tested a different regimen (paritaprevir/ritonavir/ombitasvir/dasabuvir).

This pattern is consistent across the full top-10 prediction list: alongside HIV, TxGNN also ranks feline AIDS, simian immunodeficiency virus infection, hepatitis A/B/E, and two rare Flaviviridae hemorrhagic fevers — none of which have direct supporting evidence for glecaprevir's antiviral activity. This suggests the model is picking up a "viral infection" / "co-morbid population" pattern in the knowledge graph rather than a specific, mechanistically grounded repurposing signal for HIV.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT02634008](https://clinicaltrials.gov/study/NCT02634008) | Phase 3 | Completed | 83 | Pilot study in recent HCV infection ± HIV co-infection; **uses a different regimen (paritaprevir/ritonavir/ombitasvir/dasabuvir)**, not glecaprevir — graded low relevance |
| [NCT05108935](https://clinicaltrials.gov/study/NCT05108935) | N/A | Completed | 17 | Telemedicine delivery of MOUD, HIV PrEP, and HCV treatment at needle exchanges; not a glecaprevir efficacy trial for HIV |
| [NCT04577482](https://clinicaltrials.gov/study/NCT04577482) | N/A | Completed | 42 | Real-world SVR outcomes with glecaprevir/pibrentasvir in DAA-experienced chronic HCV patients (Russia); HIV status not the endpoint |
| [NCT07040319](https://clinicaltrials.gov/study/NCT07040319) | Phase 1/2 | Not yet recruiting | 30 | PK/safety of glecaprevir/pibrentasvir initiated in pregnancy for HCV, with/without HIV co-infection; safety, not HIV efficacy |
| [NCT03823911](https://clinicaltrials.gov/study/NCT03823911) | Phase 4 | Completed | 87 | Cardiovascular risk after HCV eradication in HIV mono-infected vs. HCV/HIV co-infected patients — observational, not an HIV drug-efficacy trial |
| [NCT02738138](https://clinicaltrials.gov/study/NCT02738138) (EXPEDITION-2) | Phase 3 | Completed | 153 | Efficacy/safety of glecaprevir/pibrentasvir for HCV in HIV-1 co-infected adults; primary endpoint is HCV SVR12, not HIV viral load |
| [NCT02939989](https://clinicaltrials.gov/study/NCT02939989) (MAGELLAN-3) | Phase 3 | Completed | 33 | Glecaprevir/pibrentasvir + sofosbuvir/ribavirin in HCV virologic-failure patients; HCV endpoint only |
| [NCT03222583](https://clinicaltrials.gov/study/NCT03222583) | Phase 3 | Completed | 546 | Large Asian RCT of glecaprevir/pibrentasvir for HCV genotypes 1–6, with/without HIV co-infection; HIV is a baseline covariate, not the treated condition |
| [NCT04352309](https://clinicaltrials.gov/study/NCT04352309) (EASY) | N/A | Completed | 99 | Real-world 8-week glecaprevir/pibrentasvir effectiveness in HCV + cirrhosis (Russia); no HIV efficacy data |
| [NCT03868163](https://clinicaltrials.gov/study/NCT03868163) | N/A | Completed | 161 | Real-world glecaprevir/pibrentasvir effectiveness in chronic HCV genotypes 1–6 (Russia); no HIV efficacy data |

**None of the retrieved trials evaluate glecaprevir as a treatment for HIV itself.** All either treat the HCV component of HIV/HCV co-infection or are unrelated safety/logistics studies.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [31504702](https://pubmed.ncbi.nlm.nih.gov/31504702/) | 2020 | DDI study | J Infect Dis | Characterizes drug-drug interactions between glecaprevir/pibrentasvir and HIV antiretrovirals — relevant to **co-administration safety**, not anti-HIV efficacy |
| [37671831](https://pubmed.ncbi.nlm.nih.gov/37671831/) | 2023 | Cohort | J Antimicrob Chemother | Real-world SVR to glecaprevir/pibrentasvir in HIV/HCV-coinfected patients; HIV is lower with SVR to HCV, not treated by the drug |
| [34664197](https://pubmed.ncbi.nlm.nih.gov/34664197/) | 2021 | Case Report | Clin J Gastroenterol | Successful HCV genotype 4a clearance with glecaprevir/pibrentasvir in an HIV/HCV-coinfected hemophilia patient |
| [36415300](https://pubmed.ncbi.nlm.nih.gov/36415300/) | 2022 | Case Report | J Prev Med Hyg | Hyperbilirubinemia/jaundice during glecaprevir/pibrentasvir + ART in an HIV-infected patient — safety signal, not efficacy |
| [39697370](https://pubmed.ncbi.nlm.nih.gov/39697370/) | 2024 | N/A | Clin Exp Hepatol | Effectiveness of glecaprevir/pibrentasvir for HCV in HIV/HCV-coinfected patients on bictegravir/FTC/TAF |
| [29595065](https://pubmed.ncbi.nlm.nih.gov/29595065/) | 2018 | Review | Expert Opin Pharmacother | Overview of protease-inhibitor therapy for HCV, including HIV/HCV coinfection context |
| [30671330](https://pubmed.ncbi.nlm.nih.gov/30671330/) | 2017 | Review | GMS Infect Dis | Protease inhibitors for HCV treatment, including HIV-coinfected populations |
| [30499343](https://pubmed.ncbi.nlm.nih.gov/30499343/) | 2019 | Review | Future Microbiol | Glecaprevir/pibrentasvir for chronic HCV infection |
| [29845496](https://pubmed.ncbi.nlm.nih.gov/29845496/) | 2018 | Review | Hepatol Int | Glecaprevir/pibrentasvir expanding access to HCV therapy |
| [29369303](https://pubmed.ncbi.nlm.nih.gov/29369303/) | 2018 | Conference report | AIDS Reviews | Viral hepatitis conference report; HBV/HCV burden and DAA landscape |

**No publication reports direct antiretroviral (anti-HIV) activity for glecaprevir.** The strongest direct relevance is the DDI paper (PMID 31504702), which is a safety/co-administration reference for treating HCV alongside HIV therapy — not evidence of an HIV indication.

---

## Norway Market Information

Glecaprevir is currently **not marketed in Norway** — no marketing authorizations were found (`total_licenses: 0`, `licenses: []`).

---

## Safety Considerations

Please refer to the package insert for safety information. *(Key warnings, contraindications, and DDI data were all flagged as Data Gap / not found in this evidence pack. Note separately: the meta data-gap log lists the TFDA/label warnings gap (DG001) as **Blocking** for S1 safety review, and the MOA gap (DG002) as **High** impact.)*

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Despite a high TxGNN score, the mechanistic basis for glecaprevir treating HIV is absent (HCV NS3/4A vs. HIV protease share no target homology), and every retrieved trial/publication addresses HCV treatment in HIV-co-infected patients rather than anti-HIV activity. The internal repurposing rationale explicitly identifies this as a likely comorbidity-driven false positive, reinforced by the presence of biologically implausible co-ranked predictions (feline AIDS, SIV, rare hemorrhagic fevers) in the same top-10 list.

**To proceed, the following is needed:**
- Direct *in vitro* anti-HIV activity data for glecaprevir (currently absent) before this candidate can move past S0
- Resolution of Data Gap DG002 (MOA) via DrugBank API query
- Resolution of Data Gap DG001 (TFDA/label warnings and contraindications) — currently Blocking for any S1 safety evaluation
- If no direct antiviral evidence against HIV emerges, this candidate should be closed as a network-artifact false positive rather than advanced further
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

