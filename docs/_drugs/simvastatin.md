---
layout: default
title: Simvastatin
parent: 僅模型預測 (L5)
nav_order: 326
evidence_level: L5
indication_count: 8
---

# Simvastatin
{: .fs-9 }

證據等級: **L5** | 預測適應症: **8** 個
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

# Simvastatin: From Hypercholesterolemia to Familial Hypercholesterolemia

## One-Sentence Summary

Simvastatin is an HMG-CoA reductase inhibitor originally used to lower LDL-cholesterol in general hypercholesterolemia and mixed dyslipidemia.
The TxGNN model predicts it may also be effective for **Familial Hypercholesterolemia (FH)**,
with **19 clinical trials** and **18 publications** currently supporting this direction — though, as noted below, this largely confirms an *already-approved* statin-class indication rather than a novel repurposing signal.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not specified in the evidence pack's Norway license data (0 licenses on file); simvastatin is internationally indicated for hypercholesterolemia and mixed dyslipidemia |
| Predicted New Indication | Familial Hypercholesterolemia |
| TxGNN Prediction Score | 99.63% |
| Evidence Level | L1 |
| Norway Market Status | Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Formal mechanism-of-action documentation (the DrugBank MOA field) is currently a data gap for this candidate. However, the evidence pack's own repurposing rationale supplies the mechanism: simvastatin is an HMG-CoA reductase inhibitor that blocks the rate-limiting step of hepatic cholesterol biosynthesis, thereby lowering LDL-C synthesis and up-regulating LDL receptor expression.

Familial hypercholesterolemia is caused by defective LDL receptor function, producing markedly elevated LDL-C from birth. Because statins directly counteract this pathway, the mechanistic fit is strong and well established — this is reflected in the large volume of Phase 3 evidence below, much of it using simvastatin as either the primary study drug or the standard background therapy.

Importantly, the evidence pack's rationale explicitly flags that this is **not a novel repurposing discovery**: statins, including simvastatin, are already an approved treatment class for FH. TxGNN's high score here reflects recovery of known, guideline-endorsed pharmacology rather than an unexpected new therapeutic area. This should be factored into how much additional strategic value this candidate carries versus the lower-ranked, evidence-free predictions (e.g., brain stem infarction, CETP deficiency) also present in this pack.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT02107898](https://clinicaltrials.gov/study/NCT02107898) | Phase 3 | Completed | 216 | Alirocumab add-on to stable statin therapy (incl. simvastatin) vs placebo; LDL-C reduction in heterozygous FH |
| [NCT03885921](https://clinicaltrials.gov/study/NCT03885921) | Phase 3 | Completed | 44 | 24-month open-label extension: long-term safety of ezetimibe + atorvastatin/simvastatin in homozygous FH |
| [NCT00654446](https://clinicaltrials.gov/study/NCT00654446) | Phase 3b | Completed | 442 | Renal effects of rosuvastatin vs simvastatin in Fredrickson type IIa/IIb dyslipidemia incl. heterozygous FH |
| [NCT01507831](https://clinicaltrials.gov/study/NCT01507831) | Phase 3 | Completed | 2341 | Long-term safety/tolerability of alirocumab vs placebo in high-CV-risk hypercholesterolemia on background statin therapy |
| [NCT00552097](https://clinicaltrials.gov/study/NCT00552097) | Phase 3 | Completed | 720 | ENHANCE trial: ezetimibe + high-dose simvastatin vs simvastatin alone; carotid atherosclerosis progression in heterozygous FH |
| [NCT03884452](https://clinicaltrials.gov/study/NCT03884452) | Phase 3 | Completed | 50 | Ezetimibe co-administered with atorvastatin or simvastatin in homozygous FH; efficacy and safety |
| [NCT00129402](https://clinicaltrials.gov/study/NCT00129402) | Phase 3 | Completed | 248 | Ezetimibe + simvastatin vs simvastatin alone in adolescents (10–17y) with heterozygous FH |
| [NCT01070966](https://clinicaltrials.gov/study/NCT01070966) | N/A (post-marketing) | Completed | 2089 | Re-examination/surveillance study of VYTORIN (ezetimibe/simvastatin) safety and efficacy in routine practice |
| [NCT01890967](https://clinicaltrials.gov/study/NCT01890967) | Phase 2 | Completed | 527 | Dose-ranging study of LY3015014 (PCSK9 antibody) added to background statin (incl. simvastatin) ± ezetimibe |
| [NCT01623115](https://clinicaltrials.gov/study/NCT01623115) | Phase 3 | Completed | 486 | Alirocumab vs placebo in heterozygous FH inadequately controlled on lipid-modifying therapy (statin background) |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [41824552](https://pubmed.ncbi.nlm.nih.gov/41824552/) | 2026 | Guideline | Circulation | New ACC/AHA dyslipidemia guideline replacing the 2018 cholesterol guideline; reaffirms statin-based lipid management framework relevant to FH |
| [18376000](https://pubmed.ncbi.nlm.nih.gov/18376000/) | 2008 | RCT | New England Journal of Medicine | ENHANCE trial: ezetimibe + simvastatin vs simvastatin alone in heterozygous FH; greater LDL-C lowering without additional carotid IMT benefit |
| [31696945](https://pubmed.ncbi.nlm.nih.gov/31696945/) | 2019 | Systematic Review (Cochrane) | Cochrane Database of Systematic Reviews | Statins, including simvastatin, safely and effectively reduce LDL-C in pediatric FH patients |
| [15794711](https://pubmed.ncbi.nlm.nih.gov/15794711/) | 2005 | Review | Expert Opinion on Drug Safety | Benefit-risk assessment of simvastatin specifically in familial hypercholesterolemia; supports long-term use |
| [27417002](https://pubmed.ncbi.nlm.nih.gov/27417002/) | 2016 | Cohort | Journal of the American College of Cardiology | Statin therapy associated with reduced coronary artery disease events and all-cause mortality in FH |
| [12908847](https://pubmed.ncbi.nlm.nih.gov/12908847/) | 2003 | Review | Drug Safety | Long-term benefits and risks of simvastatin in familial hypercholesterolemia patients |
| [21173733](https://pubmed.ncbi.nlm.nih.gov/21173733/) | 2010 | Cohort | International Angiology | Long-term ezetimibe/simvastatin treatment reduces CV risk markers in FH |
| [28437620](https://pubmed.ncbi.nlm.nih.gov/28437620/) | 2017 | Guideline | Endocrine Practice (AACE/ACE) | Dyslipidemia management guideline recommending statin-based therapy including for FH |
| [11383320](https://pubmed.ncbi.nlm.nih.gov/11383320/) | 2001 | RCT | Nutrition, Metabolism & Cardiovascular Diseases | Atorvastatin vs simvastatin comparison for LDL-C goal attainment in heterozygous FH |
| [35629051](https://pubmed.ncbi.nlm.nih.gov/35629051/) | 2022 | Cross-sectional | Journal of Clinical Medicine | Immune parameters in pediatric FH patients on simvastatin show no adverse immunological effects |

---

## Norway Market Information

Simvastatin currently has **0 registered authorizations** in the Norway regulatory data provided (`market_status: 未上市`, not marketed). No product/authorization records are available to list.

---

## Safety Considerations

Please refer to the package insert for safety information. Key warnings, contraindications, and drug-drug interaction data are not yet available in this evidence pack (see Data Gaps below).

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Evidence strength is high (L1: multiple completed Phase 3 RCTs directly involving simvastatin in FH populations), but the pack's own rationale confirms this is essentially validation of an already-approved statin-class indication rather than a novel repurposing opportunity. Combined with the drug's current unmarketed status in Norway and missing label-level safety data, guardrails are warranted before any regulatory or commercial action.

**To proceed, the following is needed:**
- TFDA/Norway product label warnings and contraindications (Blocking gap — required before safety pre-assessment, per data_gaps DG001)
- Formal DrugBank mechanism-of-action record (High priority gap DG002, to replace the inferred MOA used in this report)
- Clarification of Norway market-entry pathway, since simvastatin currently has zero registered authorizations
- Strategic reassessment of whether this candidate merits prioritization given it largely reconfirms known statin pharmacology, versus the lower-ranked, evidence-free predictions in this pack (e.g., brain stem infarction, CETP deficiency) that would represent genuinely novel signals if evidence emerges
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

