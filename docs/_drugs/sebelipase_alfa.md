---
layout: default
title: Sebelipase Alfa
parent: 僅模型預測 (L5)
nav_order: 320
evidence_level: L5
indication_count: 10
---

# Sebelipase Alfa
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

# Sebelipase Alfa: From Unmarketed Status in Norway to Lysosomal Acid Lipase Deficiency (Wolman Disease / Cholesteryl Ester Storage Disease)

## One-Sentence Summary

Sebelipase alfa is not currently on the Norwegian market and has no locally recorded approved indication.
The TxGNN model — after filtering out several mechanistically implausible top hits — correctly converges on **Lysosomal Acid Lipase Deficiency (LAL-D)**, spanning the infantile-onset form (**Wolman disease**) and the later-onset form (**Cholesteryl Ester Storage Disease, CESD**), supported by **9 clinical trials (including 1 completed Phase 3 RCT)** and **~19 publications**.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | None on file — not marketed in Norway (data gap). Globally approved as Kanuma® for LAL-D since 2015 (PMID 26452566). |
| Predicted New Indication | Lysosomal Acid Lipase Deficiency (Wolman disease / Cholesteryl Ester Storage Disease) |
| TxGNN Prediction Score | ~99.7% (Wolman disease 99.72% / CESD 99.72%) |
| Evidence Level | L2 (1 completed pivotal Phase 3 RCT — ARISE, NCT01757184 — plus multiple long-term cohort/extension studies) |
| Norway Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

The DrugBank-sourced mechanism-of-action field in this evidence pack is a confirmed data gap. However, the literature evidence retrieved for this candidate independently establishes the mechanism: sebelipase alfa is a **recombinant human lysosomal acid lipase (rhLAL)** enzyme-replacement therapy (Shirley, *Drugs* 2015, PMID 26452566). It directly supplies the enzyme that is absent or deficient in LAL-D — a 1:1 enzyme-substrate correction, not an indirect similarity heuristic.

This matters because the raw TxGNN ranking (predicted_indications ranks 1–10) is dominated by other lysosomal storage diseases that share phenotypic embedding space but have **unrelated deficient enzymes**: Scheie/Hurler syndrome (α-L-iduronidase), Gaucher disease (glucocerebrosidase), Tay-Sachs disease (hexosaminidase A). None of these would be corrected by rhLAL, and the evidence pack's own rationale annotations explicitly flag them as mechanistically unsupported (Hold, L5, no clinical evidence). By contrast, Wolman disease and CESD are simply the two ends of the **same LAL-D disease spectrum** that sebelipase alfa was originally developed for — the trial program listed under "cholesteryl ester storage disease" (rank 4) in fact enrolled both infantile Wolman-disease patients and late-onset CESD patients, which explains why the Wolman-disease entry (rank 5) shows 0 trials in its own record despite having a completed L2/S3 evidence assessment — a database classification artifact rather than an evidence gap.

In practical terms, this "prediction" is not a novel repurposing hypothesis but a **re-identification of the drug's own established global indication** in a market (Norway) where it currently has no authorization. The clinical utility of this report is therefore less about new pharmacology and more about flagging a market-entry / registration gap.

---

## Clinical Trial Evidence

*(Pooled from the CESD/LAL-D trial program, which encompasses both Wolman disease and CESD patients)*

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT01757184](https://clinicaltrials.gov/study/NCT01757184) | Phase 3 | Completed | 66 | Pivotal randomized placebo-controlled trial (ARISE) of sebelipase alfa 1 mg/kg IV every other week in late-onset LAL-D (CESD) |
| [NCT02112994](https://clinicaltrials.gov/study/NCT02112994) | Phase 2 | Completed | 31 | Multicenter open-label safety/efficacy study across a broad LAL-D population |
| [NCT02193867](https://clinicaltrials.gov/study/NCT02193867) | Phase 2 | Terminated | 10 | Weekly infusions up to 3 years in infants with rapidly progressive LAL-D (Wolman disease) |
| [NCT01371825](https://clinicaltrials.gov/study/NCT01371825) | Phase 2/3 | Completed | 9 | Dose-escalation study in children with growth failure due to LAL-D, weekly dosing up to 5 years |
| [NCT01488097](https://clinicaltrials.gov/study/NCT01488097) | Phase 2 | Completed | 8 | Extension study evaluating long-term safety/tolerability in adults with LAL-D-related liver dysfunction |
| [NCT01307098](https://clinicaltrials.gov/study/NCT01307098) | Phase 1/2 | Completed | 9 | First-in-human dose-escalation study in adults with LAL-D-related liver dysfunction |
| [NCT02376751](https://clinicaltrials.gov/study/NCT02376751) | N/A | No longer available | N/A | Expanded access protocol for LAL-D patients pending commercial availability |
| [NCT02926872](https://clinicaltrials.gov/study/NCT02926872) | N/A | Terminated | 22 | DETECT: screening for LAL-D as underlying cause of pediatric liver injury |
| [NCT04532047](https://clinicaltrials.gov/study/NCT04532047) | Phase 1 | Recruiting | 10 | PEARL basket trial: in-utero enzyme replacement feasibility across multiple LSDs (not LAL-D specific; low direct relevance) |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [34774639](https://pubmed.ncbi.nlm.nih.gov/34774639/) | 2022 | RCT (extension) | Journal of Hepatology | Final results of Phase 3 ARISE study; sebelipase alfa efficacy/safety in children and adults with LAL-D |
| [35442238](https://pubmed.ncbi.nlm.nih.gov/35442238/) | 2022 | Cohort | J Pediatr Gastroenterol Nutr | Long-term treatment outcomes from single-arm open-label study (NCT02112994) |
| [34906190](https://pubmed.ncbi.nlm.nih.gov/34906190/) | 2021 | Cohort (10-yr) | Orphanet J Rare Dis | Nationwide cohort of ERT in Wolman disease with up to 10 years of follow-up |
| [29628368](https://pubmed.ncbi.nlm.nih.gov/29628368/) | 2018 | Cohort | J Clin Lipidol | Sebelipase alfa improves atherogenic biomarkers (Phase 3 ARISE data) |
| [38918870](https://pubmed.ncbi.nlm.nih.gov/38918870/) | 2024 | Case series | Orphanet J Rare Dis | Twice-weekly dosing rescues severely ill infants with Wolman disease |
| [28179030](https://pubmed.ncbi.nlm.nih.gov/28179030/) | 2017 | Open-label dose-escalation | Orphanet J Rare Dis | Survival outcomes in infants treated with sebelipase alfa |
| [33407676](https://pubmed.ncbi.nlm.nih.gov/33407676/) | 2021 | Long-term follow-up | Orphanet J Rare Dis | Long-term survival with sebelipase alfa in rapidly progressive LAL-D (final results, 2 open-label studies) |
| [40781810](https://pubmed.ncbi.nlm.nih.gov/40781810/) | 2025 | Registry | Liver International | International registry data: sebelipase alfa improves aminotransferase levels |
| [39770929](https://pubmed.ncbi.nlm.nih.gov/39770929/) | 2024 | Review | Nutrients | Practical diagnosis/management recommendations for LAL-D, focus on Wolman disease |
| [26452566](https://pubmed.ncbi.nlm.nih.gov/26452566/) | 2015 | Review | Drugs | Sebelipase alfa: first global approval |

---

## Norway Market Information

Sebelipase alfa currently holds no marketing authorization in Norway and no license records are available in the evidence pack (`total_licenses: 0`).

---

## Safety Considerations

Please refer to the package insert for safety information.

> Note: The evidence base independently indicates infusion-associated hypersensitivity is a known clinical concern with sebelipase alfa (e.g., PMID 38572778 describes a 14-step desensitization protocol for a Wolman-disease patient), but no structured warnings, contraindications, or DDI data are present in the DrugBank-sourced safety fields of this evidence pack (DG001, blocking severity).

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The core drug-disease pairing (sebelipase alfa → LAL-D/Wolman disease/CESD) is mechanistically direct and backed by a completed pivotal Phase 3 RCT (ARISE) plus multiple long-term cohort and registry studies — this is in fact the drug's own globally approved indication (Kanuma®, approved since 2015), not a speculative repurposing hypothesis. However, the drug is entirely unmarketed in Norway and this specific evidence pack is missing safety/label data, so the appropriate next step is a guarded regulatory-entry pathway rather than an unconditional "Go."

**To proceed, the following is needed:**
- TFDA/Norwegian-equivalent label data — key warnings, contraindications (DG001, blocking; requires PDF label retrieval)
- Structured DrugBank MOA record (DG002)
- Formal Norway market authorization / import license assessment, since the drug has no local regulatory footprint
- Explicit exclusion of the other TxGNN top-10 candidates (Scheie syndrome, Hurler syndrome, growth hormone insensitivity syndrome, Gaucher disease, lysosomal storage disease with skeletal involvement, autosomal ichthyosis syndrome, Tay-Sachs disease, benign adrenal neoplasm) from further review — all lack mechanistic plausibility and supporting evidence per the rationale annotations in this pack
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

