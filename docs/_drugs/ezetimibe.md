---
layout: default
title: Ezetimibe
parent: 僅模型預測 (L5)
nav_order: 146
evidence_level: L5
indication_count: 4
---

# Ezetimibe
{: .fs-9 }

證據等級: **L5** | 預測適應症: **4** 個
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

# Ezetimibe: From Hypercholesterolemia to Hyperlipoproteinemia

## One-Sentence Summary

> Ezetimibe is an NPC1L1 inhibitor that blocks intestinal cholesterol absorption, established as add-on therapy for hypercholesterolemia and dyslipidemia.
> The TxGNN model's top signal, **Hyperlipoproteinemia**, is supported by **80+ clinical trials** and **20+ publications** — but this evidence pack's own mechanistic rationale flags it as the drug's *existing* approved use rather than a genuinely new indication.
> A more novel, but much weaker, signal appears further down the ranked list (see caveat below).

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not documented in Norway regulatory filings (drug not marketed locally, 0 authorizations); literature in this pack confirms ezetimibe's established use is LDL-C-lowering / hypercholesterolemia therapy |
| Predicted New Indication | Hyperlipoproteinemia |
| TxGNN Prediction Score | 99.63% |
| Evidence Level | L1 |
| Norway Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Currently, no structured MOA field is available (`original_moa: [Data Gap]`), but the evidence pack's mechanistic rationale supplies the underlying pharmacology: **ezetimibe selectively inhibits the NPC1L1 (Niemann-Pick C1-Like 1) transporter on the intestinal brush border**, blocking absorption of dietary and biliary cholesterol. This lowers LDL-C and produces a synergistic lipid-lowering effect when combined with statins.

**Important caveat:** the model's rank-1 prediction, *hyperlipoproteinemia*, is explicitly annotated in this evidence pack's own `repurposing_rationale` as *"the drug's existing approved indication, not a new-use signal"* (原文: 此為藥物之既有核准適應症，非新用途訊號). The rank-2 prediction, *familial hypercholesterolemia*, is similarly described as a *"standard adjunct therapy"* already in clinical use — not a repurposing candidate. Both are therefore best read as **model validation** (TxGNN correctly recovering known indications) rather than novel repurposing opportunities.

The genuinely exploratory signal in this candidate set is rank 3, *hypercholesterolemia due to CYP7A1 (cholesterol 7α-hydroxylase) deficiency* — a rare monogenic bile-acid synthesis disorder where NPC1L1 blockade could theoretically reduce cholesterol/bile-acid recycling. However, this carries only **L4 evidence** (mechanistic extrapolation, no clinical trials) and is staged as a **Research Question**, not ready for further action. Rank 4 (CETP deficiency) is unsupported (L5, Hold) since that condition typically presents with elevated, not deficient, HDL-C — mechanistically disconnected from ezetimibe's action.

---

## Clinical Trial Evidence

*(Evidence for rank-1 prediction: Hyperlipoproteinemia)*

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00093899](https://clinicaltrials.gov/study/NCT00093899) | Phase 3 | Completed | 611 | Ezetimibe/simvastatin + fenofibrate coadministration lowers cholesterol and triglycerides in mixed hyperlipidemia |
| [NCT06005597](https://clinicaltrials.gov/study/NCT06005597) | Phase 3 | Completed | 407 | Obicetrapib + ezetimibe fixed-dose combination on top of maximal lipid-lowering therapy in HeFH/ASCVD |
| [NCT01763827](https://clinicaltrials.gov/study/NCT01763827) | Phase 3 | Completed | 615 | Ezetimibe as active comparator vs evolocumab for LDL-C lowering |
| [NCT01043380](https://clinicaltrials.gov/study/NCT01043380) | Phase 4 | Completed | 245 | PRECISE-IVUS: ezetimibe+statin vs statin alone on coronary plaque regression by intravascular ultrasound |
| [NCT00092833](https://clinicaltrials.gov/study/NCT00092833) | Phase 3 | Terminated | 49 | Ezetimibe 10 mg/day open-label treatment-use study in homozygous FH / homozygous sitosterolemia |
| [NCT00092560](https://clinicaltrials.gov/study/NCT00092560) | Phase 3 | Completed | 587 | Fenofibrate + ezetimibe coadministration efficacy/safety in mixed hyperlipidemia |
| [NCT00349284](https://clinicaltrials.gov/study/NCT00349284) | Phase 3 | Completed | 181 | Fenofibrate vs ezetimibe vs combination in Type IIb dyslipidemia with metabolic syndrome features |
| [NCT00843661](https://clinicaltrials.gov/study/NCT00843661) | Phase 4 | Unknown | 60 | Ezetimibe+fenofibrate vs pravastatin monotherapy in HIV patients on protease inhibitors |
| [NCT03434613](https://clinicaltrials.gov/study/NCT03434613) | Phase 4 | Completed | 64 | Statin monotherapy vs statin/ezetimibe combination effect on hepatic steatosis in NAFLD |
| [NCT04862260](https://clinicaltrials.gov/study/NCT04862260) | Early Phase 1 | Active, not recruiting | 3 | Exploratory cholesterol-metabolism reprogramming (ezetimibe+atorvastatin+evolocumab) in pancreatic adenocarcinoma |

---

## Literature Evidence

*(Evidence for rank-1 prediction: Hyperlipoproteinemia)*

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [40347969](https://pubmed.ncbi.nlm.nih.gov/40347969/) | 2025 | RCT | Lancet | TANDEM trial: obicetrapib+ezetimibe fixed-dose combination significantly reduces LDL-C |
| [41206969](https://pubmed.ncbi.nlm.nih.gov/41206969/) | 2026 | RCT | JAMA | Oral PCSK9 inhibitor enlicitide evaluated in HeFH patients not at goal on standard lipid-lowering therapy (incl. ezetimibe) |
| [25939291](https://pubmed.ncbi.nlm.nih.gov/25939291/) | 2015 | Review | Cardiology Clinics | Ezetimibe among established add-on therapies for familial hypercholesterolemia |
| [38599725](https://pubmed.ncbi.nlm.nih.gov/38599725/) | 2024 | Review | Indian Heart Journal | FH underdiagnosis/undertreatment; ezetimibe's role in standard management |
| [35593194](https://pubmed.ncbi.nlm.nih.gov/35593194/) | 2022 | Review | J Cardiovasc Pharmacol Ther | PCSK9 inhibitors reviewed against background statin/ezetimibe therapy in statin-intolerant and FH patients |
| [40682836](https://pubmed.ncbi.nlm.nih.gov/40682836/) | 2025 | — | Molecular Medicine Reports | Review of current hyperlipidemia drug classes, including cholesterol absorption inhibitors |
| [33766264](https://pubmed.ncbi.nlm.nih.gov/33766264/) | 2021 | — | J American College of Cardiology | New/emerging LDL-C and ApoB-lowering therapies positioned alongside ezetimibe/PCSK9i |
| [30702994](https://pubmed.ncbi.nlm.nih.gov/30702994/) | 2019 | — | Circulation Research | Overview of cholesterol-lowering agent classes, including ezetimibe's NPC1L1 mechanism |
| [19654419](https://pubmed.ncbi.nlm.nih.gov/19654419/) | 2009 | — | Drug and Therapeutics Bulletin | Direct review/update on ezetimibe efficacy and safety evidence at the time |
| [34480646](https://pubmed.ncbi.nlm.nih.gov/34480646/) | 2021 | — | Current Cardiology Reports | Global burden and treatment approaches for FH, including ezetimibe |

---

## Norway Market Information

No authorization records are present in the evidence pack — `market_status = 未上市 (Not Marketed)` with `total_licenses = 0`. Ezetimibe currently has no registered product license in Norway per available data.

---

## Safety Considerations

Please refer to the package insert for safety information. (`key_warnings`, `contraindications`, and DDI records are all flagged as data gaps in this evidence pack, and DDI query status is `not_found`.)

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The rank-1 signal (hyperlipoproteinemia, L1 evidence) is backed by extensive Phase 3 RCT data, but this evidence pack itself identifies it as the drug's *existing* indication rather than a novel repurposing opportunity — so the "Proceed with Guardrails" call should be understood as validating ezetimibe's established use, not greenlighting a new indication. The one candidate that would represent genuine repurposing (CYP7A1-deficiency hypercholesterolemia, rank 3) remains at L4/Research Question stage and is not yet actionable.

**To proceed, the following is needed:**
- TFDA/Norwegian regulatory label data (DG001, Blocking) — required before any S1 safety pre-assessment
- Formal DrugBank MOA confirmation (DG002, High) to replace the rationale-derived mechanistic summary used here
- If pursuing the CYP7A1-deficiency signal: dedicated preclinical/mechanistic studies, since no clinical trials currently exist for this ultra-rare indication
- Re-scope the "new indication" framing for this candidate, since ranks 1–2 substantially overlap with ezetimibe's known label
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

