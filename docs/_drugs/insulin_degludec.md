---
layout: default
title: Insulin Degludec
parent: 僅模型預測 (L5)
nav_order: 183
evidence_level: L5
indication_count: 6
---

# Insulin Degludec
{: .fs-9 }

證據等級: **L5** | 預測適應症: **6** 個
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

# Insulin Degludec: A Self-Referential Prediction (Diabetes Mellitus → Type 1 Diabetes Mellitus)

## One-Sentence Summary

> Insulin degludec is a long-acting (ultra-long-acting) basal insulin analogue used for diabetes mellitus management. The TxGNN model's top-ranked prediction (**Type 1 Diabetes Mellitus**, score 99.44%) is not a genuine repurposing signal — it corresponds to the drug's own known clinical use — but the evidence pack is well supported by **58 clinical trials** and **20 publications**, including multiple completed Phase 3 RCTs. The remaining five ranked candidates in this pack are weaker, exploratory signals with little-to-no direct evidence.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Diabetes mellitus, basal insulin therapy (exact regulatory indication text not provided in evidence pack — data gap) |
| Predicted New Indication | Type 1 Diabetes Mellitus *(self-referential — see caveat below)* |
| TxGNN Prediction Score | 99.44% |
| Evidence Level | L1 (≥2 completed Phase 3 RCTs) |
| Taiwan Market Status | Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | **Hold** (for repurposing purposes — see rationale) |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism-of-action data for insulin degludec is not available in this evidence pack (data gap). Based on established pharmacological knowledge, insulin degludec is an ultra-long-acting basal insulin analogue that forms soluble multihexamers after subcutaneous injection, which are then slowly and continuously released into circulation — giving it a flat, stable, ~24+ hour action profile. It is used as exogenous replacement therapy for patients with absolute or relative insulin deficiency.

**Important caveat on Rank 1:** The repurposing rationale supplied with this evidence pack explicitly states that "type 1 diabetes mellitus" is insulin degludec's **original, already-approved indication** — not a novel repurposing candidate. TxGNN has effectively re-discovered the drug's own known use. This is a known limitation of graph-based drug–disease link prediction models: high-confidence edges can reflect existing knowledge already embedded in the training graph rather than a genuinely new therapeutic hypothesis. The extensive clinical trial and literature evidence below therefore should be read as **confirmatory evidence of established efficacy**, not as support for a new indication.

The genuinely exploratory candidates in this pack (ranks 2–6, summarized further below) are mechanistically much weaker: most reflect **disease comorbidity** (e.g., shared anti-GAD65 autoimmunity between Type 1 diabetes and stiff person syndrome) rather than a direct pharmacological effect of insulin on the predicted disease itself.

---

## Clinical Trial Evidence

*(for predicted_indications[0] — "type 1 diabetes mellitus," which is the drug's known/original indication)*

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT05463744](https://clinicaltrials.gov/study/NCT05463744) | Phase 3 | Completed | 692 | Once-weekly insulin efsitora alfa vs. insulin degludec in T1D patients on multiple daily injections |
| [NCT03214367](https://clinicaltrials.gov/study/NCT03214367) | Phase 3 | Completed | 1392 | PRONTO-T1D: LY900014 vs. insulin lispro, both combined with glargine or degludec, in T1D |
| [NCT02500706](https://clinicaltrials.gov/study/NCT02500706) | Phase 3 | Completed | 1108 | Faster-acting insulin aspart vs. NovoRapid, both combined with degludec, in adults with T1D |
| [NCT01835431](https://clinicaltrials.gov/study/NCT01835431) | Phase 3 | Completed | 362 | IDegAsp once daily + aspart vs. detemir once/twice daily + aspart in children/adolescents with T1D |
| [NCT04450407](https://clinicaltrials.gov/study/NCT04450407) | Phase 2 | Completed | 266 | LY3209590 vs. insulin degludec in T1D patients previously on multiple daily injections |
| [NCT05767255](https://clinicaltrials.gov/study/NCT05767255) | Phase 3 | Unknown | 66 | Basal-bolus insulin (incl. degludec) vs. basal insulin + GLP-1 analogue for hypoglycemia risk at hospital discharge |
| [NCT02536859](https://clinicaltrials.gov/study/NCT02536859) | Phase 1 | Completed | 60 | PK/PD comparison of degludec vs. glargine U300 at steady state in T1D |
| [NCT00841087](https://clinicaltrials.gov/study/NCT00841087) | Phase 2 | Completed | 65 | Safety of degludec + NovoRapid vs. detemir + NovoRapid, basal-bolus regimen, in Japanese T1D patients |
| [NCT03400501](https://clinicaltrials.gov/study/NCT03400501) | Early Phase 1 | Completed | 32 | School-supervised degludec vs. glargine to reduce ketosis risk in adolescents with poorly-controlled T1D |
| [NCT00992537](https://clinicaltrials.gov/study/NCT00992537) | Phase 1 | Completed | 27 | PK/PD comparison of IDegAsp, degludec, and insulin aspart in T1D |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [37863084](https://pubmed.ncbi.nlm.nih.gov/37863084/) | 2023 | RCT | Lancet | ONWARDS 6: once-weekly insulin icodec vs. once-daily degludec, basal-bolus regimen, in T1D |
| [39270686](https://pubmed.ncbi.nlm.nih.gov/39270686/) | 2024 | RCT | Lancet | QWINT-5: once-weekly efsitora alfa vs. once-daily degludec in adults with T1D |
| [36623517](https://pubmed.ncbi.nlm.nih.gov/36623517/) | 2023 | RCT | Lancet Diabetes Endocrinol | EXPECT: degludec vs. detemir (both + aspart) in pregnant women with T1D — non-inferiority trial |
| [34643020](https://pubmed.ncbi.nlm.nih.gov/34643020/) | 2022 | RCT | Diabetes Obes Metab | HypoDeg: degludec vs. glargine U100 in T1D patients prone to nocturnal severe hypoglycemia |
| [36610544](https://pubmed.ncbi.nlm.nih.gov/36610544/) | 2023 | RCT | Diabetes Res Clin Pract | INEOX: degludec 100 IU/mL vs. glargine 300 IU/mL efficacy/safety in T1D |
| [34763071](https://pubmed.ncbi.nlm.nih.gov/34763071/) | 2022 | RCT | Endocr Pract | BIGLEAP: degludec vs. aspart via insulin pump in well-controlled T1D, crossover design |
| [36516429](https://pubmed.ncbi.nlm.nih.gov/36516429/) | 2023 | RCT | Diabetes Technol Ther | ULTRAFLEXI-1: glargine U300 vs. degludec U100 around spontaneous exercise in T1D |
| [36763996](https://pubmed.ncbi.nlm.nih.gov/36763996/) | 2022 | Systematic Review / Meta-analysis | Clin Ther | Degludec vs. other long-acting basal insulins in T1D/T2D — efficacy and tolerability |
| [35476308](https://pubmed.ncbi.nlm.nih.gov/35476308/) | 2022 | Systematic Review | Int J Clin Pharm | Degludec U100 vs. glargine U300 in T1D — safety, efficacy, cost-effectiveness |
| [29477399](https://pubmed.ncbi.nlm.nih.gov/29477399/) | 2018 | Systematic Review / Network Meta-analysis | Value Health | Basal insulin regimens for adults with T1D — comparative efficacy and safety |

---

## Other Predicted Indications (Exploratory, Lower Evidence)

This evidence pack contains five additional TxGNN-ranked candidates. None currently have supporting clinical trials or literature. Summarized for completeness:

| Rank | Disease | Score | Evidence Level | Recommendation | Note |
|------|---------|-------|----------------|-----------------|------|
| 2 | Autoimmune oophoritis | 99.23% | L5 | Hold | No mechanistic link identified beyond possible co-occurrence in autoimmune polyglandular syndrome; pure model artifact |
| 3 | Opsismodysplasia | 99.12% | L5 | Hold | Rare skeletal dysplasia (INPPL1 mutation); no known interaction with insulin signaling |
| 4 | Thiamine-responsive dysfunction syndrome (TRMA) | 99.10% | L4 | Research Question | TRMA includes diabetes as part of its triad; insulin would only treat the diabetic component symptomatically, not the underlying B1-transporter defect |
| 5 | Classic stiff person syndrome | 99.08% | L4 | Research Question | Shares anti-GAD65 autoantibody pathophysiology with T1D (co-occurs in ~30–40% of SPS patients); insulin treats comorbid diabetes only, not SPS neurological symptoms |
| 6 | Focal stiff limb syndrome | 99.08% | L4 | Research Question | SPS-spectrum variant; same anti-GAD65/T1D comorbidity caveat as Rank 5 |

None of these warrant advancement without independent mechanistic or clinical evidence.

---

## Taiwan Market Information

Insulin degludec currently holds **no marketing authorizations in Taiwan** (market status: Not marketed; 0 licenses on file).

---

## Safety Considerations

Please refer to the package insert for safety information. No key warnings, contraindications, or drug interaction data were available in this evidence pack.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked candidate (Type 1 Diabetes Mellitus) is not a novel repurposing opportunity — it is insulin degludec's existing approved use, so it offers no new business or clinical value despite its strong L1 evidence base. The remaining five candidates all carry weak evidence (L4–L5), and several (autoimmune oophoritis, opsismodysplasia) lack any credible mechanistic rationale. The two most biologically plausible exploratory leads — stiff person syndrome and focal stiff limb syndrome — represent disease **comorbidity** via shared anti-GAD65 autoimmunity, not a direct pharmacological effect of insulin on the neurological disorder itself, and therefore do not currently support a repurposing claim.

**To proceed, the following is needed:**
- Resolve **DG001** (Blocking): obtain TFDA label/package insert (warnings, contraindications) before any S1 safety evaluation can begin
- Resolve **DG002** (High): retrieve formal mechanism-of-action data from DrugBank
- If pursuing the stiff person syndrome hypothesis, commission a targeted literature review of anti-GAD65 autoimmunity and insulin's potential immunomodulatory (not glycemic) role — current evidence pack contains zero supporting citations
- Deprioritize autoimmune oophoritis and opsismodysplasia unless new mechanistic evidence emerges
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

