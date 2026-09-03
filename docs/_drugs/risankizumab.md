---
layout: default
title: Risankizumab
parent: 僅模型預測 (L5)
nav_order: 307
evidence_level: L5
indication_count: 10
---

# Risankizumab
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

# Risankizumab: From Psoriasis to Dermatitis

## One-Sentence Summary

Risankizumab (Skyrizi) is an IL-23p19 inhibitor monoclonal antibody originally approved for psoriasis vulgaris, psoriatic arthritis, generalized pustular psoriasis, and erythrodermic psoriasis. The TxGNN model predicts it may be effective for **Dermatitis** (encompassing atopic dermatitis), with **7 clinical trials** and **16 publications** currently supporting this direction, including one completed Phase 2 RCT specifically in atopic dermatitis.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Psoriasis vulgaris, psoriatic arthritis, generalized pustular psoriasis, erythrodermic psoriasis (per global approval history documented in literature; no Norway license record available) |
| Predicted New Indication | Dermatitis |
| TxGNN Prediction Score | 99.98% |
| Evidence Level | L2 (1 completed Phase 2 RCT — NCT03706040) |
| Norway Market Status | ✗ Not Marketed (未上市) |
| Number of Authorizations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Structured mechanism-of-action data for risankizumab is not available in the current dataset (Data Gap DG002). Based on literature evidence collected for this candidate (PMID 31098898, *"Risankizumab: First Global Approval"*), risankizumab is a humanised IgG monoclonal antibody that selectively targets the p19 subunit of interleukin-23 (IL-23), blocking downstream Th17-mediated inflammatory signalling. It received its first global approval in Japan in 2019 for psoriasis vulgaris, psoriatic arthritis, generalized pustular psoriasis, and erythrodermic psoriasis, and has since been approved in the USA, Canada, and the EU.

Psoriasis and atopic/eczematous dermatitis are both chronic immune-mediated inflammatory skin diseases, but they historically involve different dominant T-helper pathways (psoriasis: Th17/IL-23; atopic dermatitis: Th2, with Th22 and Th17 contributions). A Phase 2 RCT (PMID 36588137) explicitly notes that atopic dermatitis involves the Th2, Th22, and *potentially* Th17 pathways, providing a rationale for testing IL-23/IL-22 blockade in this population — which supports the mechanistic plausibility of the TxGNN prediction rather than treating it as a purely coincidental association.

Clinically, this mechanistic overlap is further reflected in real-world reports of "paradoxical eczema" arising in psoriasis patients treated with IL-23 inhibitors including risankizumab, and conversely a case report of risankizumab used successfully in a patient with concomitant atopic dermatitis and psoriasis. These bidirectional clinical observations, together with a dedicated Phase 2 RCT in atopic dermatitis, indicate the prediction is grounded in genuine (if still evolving) pathophysiological overlap rather than model artifact.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT03706040](https://clinicaltrials.gov/study/NCT03706040) | Phase 2 | Completed | 172 | Randomized, placebo-controlled study of risankizumab in adults/adolescents with moderate-to-severe atopic dermatitis — the primary direct evidence for this indication |
| [NCT04908475](https://clinicaltrials.gov/study/NCT04908475) | Phase 4 | Completed | 352 | Risankizumab vs apremilast in moderate plaque psoriasis; safety/efficacy comparison in candidates for systemic therapy |
| [NCT05969223](https://clinicaltrials.gov/study/NCT05969223) | Phase 4 | Completed | 214 | Risankizumab in moderate-to-severe genital or scalp psoriasis |
| [NCT04818385](https://clinicaltrials.gov/study/NCT04818385) | N/A (Observational) | Completed | 240 | Taiwan real-world cohort comparing durability of risankizumab response (PASI 90) vs other biologics in chronic plaque psoriasis |
| [NCT07021495](https://clinicaltrials.gov/study/NCT07021495) | N/A (Observational) | Recruiting | 840 | Multi-centre biomarker profiling of six immune-mediated inflammatory skin diseases, including atopic dermatitis and plaque psoriasis |
| [NCT07041112](https://clinicaltrials.gov/study/NCT07041112) | N/A (Observational) | Completed | 1000 | Pharmacogenetic study of genetic/cardiometabolic factors on 10-year survival of biologic therapies in psoriasis/psoriatic arthritis |
| [NCT07352566](https://clinicaltrials.gov/study/NCT07352566) | Phase 4 | Not Yet Recruiting | 10 | Microdevice testing FDA-approved medications (including for atopic dermatitis and psoriasis) directly on skin |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [36588137](https://pubmed.ncbi.nlm.nih.gov/36588137/) | 2023 | RCT | Dermatology and Therapy | Phase 2, randomized, double-blind, placebo-controlled trial of risankizumab in moderate-to-severe atopic dermatitis; rationale based on IL-23/IL-22 pathway involvement |
| [31098898](https://pubmed.ncbi.nlm.nih.gov/31098898/) | 2019 | Review | Drugs | Drug profile: MOA (anti-IL-23p19), first global approval in Japan for psoriasis-spectrum indications |
| [33078990](https://pubmed.ncbi.nlm.nih.gov/33078990/) | 2020 | Review | Expert Opinion on Biological Therapy | Overview of current and emerging biologics, including risankizumab, for pediatric atopic dermatitis |
| [39201826](https://pubmed.ncbi.nlm.nih.gov/39201826/) | 2024 | Review | Children (Basel) | Narrative review of biologics/targeted therapies for pediatric alopecia areata, psoriasis, atopic dermatitis, and hidradenitis suppurativa |
| [39668419](https://pubmed.ncbi.nlm.nih.gov/39668419/) | 2025 | Case Report | International Journal of Dermatology | Effectiveness and safety of combined dupilumab and risankizumab in a patient with concomitant atopic dermatitis and psoriasis |
| [33185530](https://pubmed.ncbi.nlm.nih.gov/33185530/) | 2020 | Case Report | European Journal of Dermatology | Eczematous eruption occurring in psoriasis patients during risankizumab treatment |
| [36939506](https://pubmed.ncbi.nlm.nih.gov/36939506/) | 2023 | Case Report | Italian Journal of Dermatology and Venereology | Case of eczematous eruption occurring during risankizumab treatment |
| [41645692](https://pubmed.ncbi.nlm.nih.gov/41645692/) | 2026 | Case Report | Dermatology Reports | Upadacitinib as a management option for paradoxical eczema induced by IL-23 inhibitors including risankizumab |
| [37014149](https://pubmed.ncbi.nlm.nih.gov/37014149/) | 2023 | Case Series | Journal of Cutaneous Medicine and Surgery | Brodalumab-induced eczematous reactions managed by switching to risankizumab |
| [38607726](https://pubmed.ncbi.nlm.nih.gov/38607726/) | 2024 | Review | Military Medicine | Reappraisal of systemic immunomodulators, including risankizumab, for psoriasis and eczema in military populations |

---

## Norway Market Information

Risankizumab currently has **no marketing authorization on record in Norway** (`total_licenses: 0`, `market_status: 未上市 / Not Marketed`). No product license, dosage form, or approved indication text is available for this market.

---

## Safety Considerations

Please refer to the package insert for safety information. (Key warnings, contraindications, and drug-drug interaction data are all marked as Data Gaps in the current evidence pack — this is flagged as a **Blocking** gap, DG001, pending TFDA/regulatory label retrieval.)

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
A completed Phase 2 RCT (NCT03706040) directly evaluated risankizumab in moderate-to-severe atopic dermatitis, and this is reinforced by mechanistic literature on IL-22/Th17 pathway involvement plus multiple real-world case reports describing bidirectional clinical overlap between IL-23 inhibition and eczematous/dermatitis presentations. This supports genuine, non-coincidental biological plausibility (Evidence Level L2), but confirmatory Phase 3 data and full safety documentation are still missing.

**To proceed, the following is needed:**
- TFDA/regulatory package insert (warnings, contraindications, DDI) — currently Blocking (DG001)
- Structured MOA data from DrugBank to formally support the mechanistic rationale (DG002)
- Confirmatory Phase 3 RCT data specific to the dermatitis/atopic dermatitis indication
- Clarification of Norway market entry plans, since the drug currently holds no local authorization
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

