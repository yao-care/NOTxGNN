---
layout: default
title: Ledipasvir
parent: 僅模型預測 (L5)
nav_order: 202
evidence_level: L5
indication_count: 10
---

# Ledipasvir
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

# Ledipasvir: From Chronic Hepatitis C to Hepatitis B Virus Infection

## One-Sentence Summary

> Ledipasvir is an NS5A inhibitor best known as a component of the ledipasvir/sofosbuvir (Harvoni) fixed-dose combination for chronic hepatitis C virus (HCV) infection.
> The TxGNN model predicts it may also be effective for **Hepatitis B Virus (HBV) Infection**,
> with **21 clinical trials** and **20 publications** identified in the evidence pack — but the strongest direct evidence (a dedicated Phase 2 HBV trial) reported a **negative efficacy signal**, and much of the remaining literature concerns HBV *reactivation risk* during HCV treatment rather than antiviral benefit against HBV itself.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not documented in Norway regulatory data (drug unmarketed); per known clinical use, ledipasvir is used as part of the ledipasvir/sofosbuvir combination for chronic hepatitis C |
| Predicted New Indication | Hepatitis B Virus Infection |
| TxGNN Prediction Score | 99.91% |
| Evidence Level | L3 |
| Norway Market Status | ✗ Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available from DrugBank in this evidence pack. Based on known information, ledipasvir is an HCV NS5A protein inhibitor, marketed exclusively as part of the ledipasvir/sofosbuvir fixed-dose combination for chronic genotype 1/4/5/6 HCV infection. HCV (Flaviviridae, positive-sense RNA virus) and HBV (Hepadnaviridae, a DNA virus replicating via reverse transcription) are virologically distinct families with no known overlapping molecular target — NS5A has no HBV homolog.

Despite this mechanistic gap, the prediction is not entirely without a rationale to test: patients coinfected with HCV and HBV are common, and retrospective data suggested modest reductions in HBsAg during HCV treatment with ledipasvir/sofosbuvir, motivating a dedicated Phase 2 trial (NCT03312023) in HBV-monoinfected subjects. However, the published results of that trial (PMID 36045503) showed **no clinically meaningful suppression of HBV DNA**, indicating the earlier HBsAg-decline signal did not translate into antiviral efficacy. In parallel, a substantial portion of the literature base actually documents the *opposite* clinical concern — HBV reactivation during ledipasvir/sofosbuvir treatment of HCV/HBV-coinfected patients — which is a safety signal, not a therapeutic rationale.

**In summary: the high TxGNN score for this indication appears to reflect literature co-occurrence (both diseases are frequently studied together in coinfected populations) rather than a validated pharmacological effect.** The evidence pack's own rationale and "Hold" recommendation align with this interpretation.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT03312023](https://clinicaltrials.gov/study/NCT03312023) | Phase 2 | Completed | 21 | Open-label study directly testing ledipasvir/sofosbuvir for 12 weeks in HBV-monoinfected subjects; hypothesis-generating, but published results showed no significant HBV DNA decline |
| [NCT02555943](https://clinicaltrials.gov/study/NCT02555943) | Phase 2/3 | Completed | 23 | Studied incidence and risk factors for HBV reactivation during direct-acting antiviral treatment of HCV/HBV coinfection — a safety, not efficacy, endpoint |
| [NCT02613871](https://clinicaltrials.gov/study/NCT02613871) | Phase 3 | Completed | 111 | LDV/SOF for HCV genotype 1/2 in HCV/HBV-coinfected patients (Taiwan); treatment target was HCV clearance, not HBV |
| [NCT01938430](https://clinicaltrials.gov/study/NCT01938430) | Phase 2 | Completed | 339 | LDV/SOF + ribavirin in advanced liver disease/post-transplant HCV patients (genotype 1/4, some HBV-exposed); HCV-focused endpoints |
| [NCT02010255](https://clinicaltrials.gov/study/NCT02010255) | Phase 2 | Completed | 334 | Companion cohort study to NCT01938430, same protocol; HCV efficacy endpoint |

*Note: 16 additional trials in the evidence pack are standard HCV genotype 1/2/4 treatment studies with only incidental HBV coinfection status and were excluded here as not directly relevant to HBV efficacy.*

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [36045503](https://pubmed.ncbi.nlm.nih.gov/36045503/) | 2023 | Phase 2 open-label trial | J Med Virol | Direct test of LDV/SOF in HBV-monoinfected subjects; no significant decline in HBV DNA at Week 12 despite hypothesis based on retrospective HBsAg signal |
| [34864948](https://pubmed.ncbi.nlm.nih.gov/34864948/) | 2022 | Cohort (108-week follow-up) | Clin Infect Dis | Taiwan cohort of HCV/HBV-coinfected patients treated with LDV/SOF; evaluated HBV reactivation, not HBV cure |
| [29174546](https://pubmed.ncbi.nlm.nih.gov/29174546/) | 2018 | Prospective cohort | Gastroenterology | Risks and outcomes of HCV treatment with LDV/SOF in HBV-coinfected patients; reactivation-focused |
| [29334502](https://pubmed.ncbi.nlm.nih.gov/29334502/) | 2018 | Cohort (reactivation risk) | J Clin Gastroenterol | Examined HBV reactivation risk in actively/previously infected patients during DAA therapy |
| [27486112](https://pubmed.ncbi.nlm.nih.gov/27486112/) | 2016 | Cohort (no reactivation) | Clin Infect Dis | Taiwan/Korea cohort of 173 patients (103 with prior HBV exposure); no HBV reactivation observed during LDV/SOF |
| [27367295](https://pubmed.ncbi.nlm.nih.gov/27367295/) | 2016 | Pilot study | Antivir Ther | Gane et al.; evaluated whether LDV/SOF can suppress HCV in HBV-coinfected patients — HCV-focused |
| [33523503](https://pubmed.ncbi.nlm.nih.gov/33523503/) | 2021 | Prospective observational | J Viral Hepat | HBV reactivation risk during DAA treatment for HCV in cancer patients with HBV/HCV coinfection |
| [37254310](https://pubmed.ncbi.nlm.nih.gov/37254310/) | 2024 | In silico / molecular docking | J Biomol Struct Dyn | Computational screening of antiviral compounds against HBx protein; not specific to ledipasvir mechanism |

---

## Norway Market Information

Ledipasvir is currently **not marketed in Norway** (market status: 未上市). No authorization records are available in the evidence pack.

---

## Safety Considerations

Please refer to the package insert for safety information. (TFDA/DMP label warnings and contraindications were not available in this evidence pack — flagged as a **Blocking** data gap, see Next Steps.)

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Although the TxGNN score is very high (99.91%), the strongest and most direct clinical evidence — a Phase 2 trial specifically testing ledipasvir/sofosbuvir in HBV-monoinfected patients (NCT03312023 / PMID 36045503) — reported no meaningful antiviral effect on HBV DNA. Most of the remaining trial and literature base concerns HBV *reactivation risk* during HCV treatment, which is a safety consideration working against this indication rather than supporting evidence for it. The mechanistic basis (HCV NS5A inhibition) also has no established relevance to HBV replication (reverse transcriptase-dependent, cccDNA-based). This candidate should not advance without new positive efficacy data.

**To proceed, the following is needed:**
- Resolution of the **Blocking** data gap: TFDA/DMP label warnings and contraindications (DG001)
- Resolution of the **High** priority data gap: confirmed mechanism of action from DrugBank (DG002)
- If pursued further, an updated systematic review or a properly powered, randomized trial with a confirmed antiviral (HBV DNA/HBsAg) endpoint would be required to override the current negative Phase 2 signal
- Given the negative primary trial result, further investment in this specific indication is not currently recommended; lower-ranked candidates in this evidence pack (e.g., hepatitis E virus infection, rank 2) may warrant separate evaluation given their distinct mechanistic rationale
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

