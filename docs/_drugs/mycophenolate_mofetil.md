---
layout: default
title: Mycophenolate Mofetil
parent: 僅模型預測 (L5)
nav_order: 236
evidence_level: L5
indication_count: 10
---

# Mycophenolate Mofetil
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

# Mycophenolate Mofetil: From Transplant Rejection Prophylaxis to HIV Infectious Disease

## One-Sentence Summary

> Mycophenolate mofetil (MMF) is a well-established immunosuppressant primarily used to prevent rejection after solid organ transplantation.
> The TxGNN model predicts it may also be effective for **HIV Infectious Disease**,
> with **10 clinical trials** and **10 supporting publications** currently reviewed, though most trials are small, terminated, withdrawn, or of unknown status.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Prevention of organ transplant rejection (renal, cardiac, hepatic) — not captured in the evidence pack; based on established pharmacology of MMF |
| Predicted New Indication | HIV infectious disease |
| TxGNN Prediction Score | 99.86% |
| Evidence Level | L2 |
| Norway Market Status | ✗ Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the evidence pack. Based on established pharmacology, mycophenolate mofetil is a prodrug of mycophenolic acid (MPA), a selective, reversible inhibitor of inosine monophosphate dehydrogenase (IMPDH) type II. This enzyme is required for the *de novo* synthesis of guanine nucleotides — a pathway that activated T and B lymphocytes depend on heavily because they lack an efficient purine salvage route. This selective antiproliferative effect on lymphocytes is why MMF is used to suppress transplant rejection.

The hypothesized link to HIV infection rests on a different aspect of the same mechanism: chronic immune hyperactivation and clonal expansion of activated CD4+ T cells (the primary reservoir for HIV replication) drive disease progression. By depleting the guanine nucleotide pool in these activated cells, MMF could theoretically dampen immune-activation-driven viral replication and slow CD4+ T-cell depletion, independent of direct antiretroviral activity. Several groups also proposed a direct antiviral mechanism, since MPA-induced dGTP depletion can enhance the activity of guanosine-analogue reverse transcriptase inhibitors such as abacavir.

However, this rationale has been tested prospectively in several small Phase 1/2 studies over the past two decades, and the results are inconsistent: some trials show reduced HIV RNA or favorable immunological markers when MMF is added to abacavir-containing regimens, while the largest planned confirmatory studies (e.g., MAN2, NCT00120419) remain of unknown/unreported outcome, and a key adjunct trial (NCT00021489) was withdrawn before enrollment. The evidence therefore supports a plausible mechanism but not a demonstrated clinical benefit.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00120419](https://clinicaltrials.gov/study/NCT00120419) | Phase 4 | Unknown | 90 | MAN2 study — MMF for chronic immune hyperactivation in ART-naïve HIV-1 patients; assessed CD4+ decline, HIV-1 RNA, and disease progression; outcome not reported |
| [NCT00038272](https://clinicaltrials.gov/study/NCT00038272) | Phase 2 | Completed | 56 | Compared DAPD alone vs DAPD + MMF in treatment-experienced patients; MMF was an adjunct, not the primary study drug |
| [NCT01288131](https://clinicaltrials.gov/study/NCT01288131) | Phase 3 | Terminated | 8 | Cyclosporine + MMF vs cyclophosphamide + prednisolone for anti-r-HuEpo PRCA; not an HIV indication |
| [NCT06869265](https://clinicaltrials.gov/study/NCT06869265) | Phase 2 | Recruiting | 56 | Conditioning regimen for haplo-HSCT in AML; MMF incidental (GVHD prophylaxis), unrelated to HIV |
| [NCT00247494](https://clinicaltrials.gov/study/NCT00247494) | Phase 4 | Unknown | 90 | MAN2 substudy evaluating MMF's effect on cardiovascular surrogate markers in HIV-1 patients |
| [NCT00021489](https://clinicaltrials.gov/study/NCT00021489) | Phase 1/2 | Withdrawn | 0 | Planned to test MMF + abacavir safety and antiretroviral activity in treatment-failure patients; withdrawn before any data collected |
| [NCT02793544](https://clinicaltrials.gov/study/NCT02793544) | Phase 2 | Completed | 80 | MMF used for GVHD prophylaxis in HLA-mismatched unrelated donor BMT for hematologic malignancies; not HIV-related |
| [NCT00112593](https://clinicaltrials.gov/study/NCT00112593) | N/A | Completed | 5 | Allogeneic HSCT with post-transplant cyclosporine/MMF for mixed chimerism induction in HIV-1-positive patients |
| [NCT01453192](https://clinicaltrials.gov/study/NCT01453192) | Phase 3 | Completed | 27 | Renal transplant follow-up in HIV-1 patients with ESRD; MMF used as standard post-transplant immunosuppression, not tested for antiviral effect |
| [NCT00009009](https://clinicaltrials.gov/study/NCT00009009) | Phase 2 | Completed | 10 | Renal transplantation safety/efficacy in HIV-infected ESRD patients; MMF as standard immunosuppressant |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [15213566](https://pubmed.ncbi.nlm.nih.gov/15213566/) | 2004 | Randomized pilot study | J Acquir Immune Defic Syndr | MMF during structured HAART interruption; assessed immune response and plasma/lymphatic viral load in 17 chronic HIV patients |
| [15353978](https://pubmed.ncbi.nlm.nih.gov/15353978/) | 2004 | Clinical study | AIDS | HAART with or without MMF in treatment-naïve HIV-1 patients; examined effect on plasma HIV-1 RNA decay and latent reservoir |
| [12352149](https://pubmed.ncbi.nlm.nih.gov/12352149/) | 2002 | Cohort | J Acquir Immune Defic Syndr | Adding MMF to abacavir-based ART associated with intracellular dGTP depletion and decreased plasma HIV-1 RNA in 5 heavily treated patients |
| [16379601](https://pubmed.ncbi.nlm.nih.gov/16379601/) | 2005 | Cohort | AIDS Res Hum Retroviruses | No detrimental immunological effects observed with MMF + HAART in treatment-naïve acute/chronic HIV-1 patients |
| [15871638](https://pubmed.ncbi.nlm.nih.gov/15871638/) | 2005 | Cohort/PK-PD | Clin Pharmacokinet | PK/PD of low-dose MMF combined with abacavir, efavirenz, and nelfinavir in HIV-infected patients |
| [15355127](https://pubmed.ncbi.nlm.nih.gov/15355127/) | 2004 | Cohort/PK | Clin Pharmacokinet | Effect of MMF on antiretroviral drug pharmacokinetics and intracellular nucleoside triphosphate pools |
| [11391161](https://pubmed.ncbi.nlm.nih.gov/11391161/) | 2001 | Pilot study | J Acquir Immune Defic Syndr | MMF as a component of salvage therapy in 7 patients with multidrug-resistant HIV-1; well tolerated, no significant decline in viral suppression noted |
| [17885292](https://pubmed.ncbi.nlm.nih.gov/17885292/) | 2007 | Clinical study | AIDS | DAPD (amdoxovir) with or without MMF evaluated for safety, tolerability, and antiretroviral activity in drug-resistant HIV |
| [17017956](https://pubmed.ncbi.nlm.nih.gov/17017956/) | 2006 | Review | Curr Top Med Chem | Overview of immunosuppressive drugs, including MMF, as potential adjuncts targeting immune activation in HIV disease |
| [16515490](https://pubmed.ncbi.nlm.nih.gov/16515490/) | 2006 | Review | Curr Pharm Des | Review of "virostatic" agents, including MMF, as a strategy to target host factors sustaining HIV reservoirs |

---

## Norway Market Information

Currently not marketed in Norway — no authorization records are available in the evidence pack (`total_licenses: 0`).

---

## Safety Considerations

TFDA-equivalent label warnings, contraindications, and drug interaction data are not currently available (flagged as a **Blocking** data gap, DG001 — download/parse required from the regulatory label source). Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
While the immune-activation hypothesis linking MMF to HIV disease control is mechanistically plausible and has been tested in several small studies, the trial evidence is inconsistent (multiple studies withdrawn, terminated, or of unknown/unreported outcome), no confirmatory Phase 2/3 RCT has established clinical benefit, and MMF is not currently marketed in Norway. Core safety data needed for a preliminary safety assessment (S1) is also missing.

**To proceed, the following is needed:**
- TFDA/Norwegian label safety data — warnings, contraindications, DDI (DG001, currently Blocking)
- Formal mechanism-of-action documentation from DrugBank (DG002)
- Outcome data from the MAN2 study (NCT00120419/NCT00247494), currently listed as unknown status
- A dedicated risk assessment for immunosuppression in an HIV-positive population (balancing antiviral hypothesis vs. risk of further immune impairment)
- Norway/EU regulatory pathway assessment given the drug is not currently marketed in this indication or country
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

