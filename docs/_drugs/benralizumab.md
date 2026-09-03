---
layout: default
title: Benralizumab
parent: 僅模型預測 (L5)
nav_order: 49
evidence_level: L5
indication_count: 5
---

# Benralizumab
{: .fs-9 }

證據等級: **L5** | 預測適應症: **5** 個
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

# Benralizumab: From Severe Eosinophilic Asthma to Atopic Dermatitis

## One-Sentence Summary

> Benralizumab is an anti-IL-5Rα monoclonal antibody that depletes eosinophils, with established clinical use in severe eosinophilic asthma (per trial/literature context in this evidence pack — the drug is not marketed in Norway and no regulatory indication text is on file).
> TxGNN's top-ranked prediction (immune thrombocytopenia) has no supporting trials or literature, so this report focuses on **Atopic Dermatitis**, the only candidate with substantial real-world clinical evidence — **6 clinical trials** and **20 publications**.
> However, the key confirmatory Phase 2 RCT (HILLIER) was **terminated early and published as a negative result**, so the evidence currently argues against, not for, this repurposing direction.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not specified in Norway regulatory data (drug not marketed); evidence context indicates severe eosinophilic asthma |
| Predicted New Indication | Atopic Dermatitis (TxGNN label: "dermatitis") |
| TxGNN Prediction Score | 99.16% (rank 8215) |
| Evidence Level | L2 (1 completed Phase 2 trial exists), but the larger confirmatory Phase 2 RCT was terminated with a **negative** efficacy outcome |
| Norway Market Status | ✗ Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | **Hold** |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data for benralizumab is not available in this evidence pack (Data Gap DG002). Based on the literature retrieved, benralizumab binds IL-5Rα and depletes eosinophils via antibody-dependent cell-mediated cytotoxicity — this is the mechanism underlying its use in severe eosinophilic asthma. Atopic dermatitis lesions also show tissue eosinophilia, which is the mechanistic rationale TxGNN's knowledge graph likely leveraged to link the two conditions.

Clinically, however, this hypothesis has already been tested: a dedicated Phase 2 RCT (NCT04605094, "HILLIER," N=194) was designed specifically to test benralizumab in moderate-to-severe atopic dermatitis. The trial was **terminated early**, and the published result (PMID 37178404) is titled *"Lack of effect of benralizumab on signs and symptoms of moderate-to-severe atopic dermatitis."* The literature consistently frames dupilumab (anti-IL-4/13) — not anti-IL-5 agents — as the effective biologic class for AD, suggesting eosinophils are not the primary pathogenic driver in this disease, unlike in eosinophilic asthma. This is a case where TxGNN's mechanistic plausibility did not translate into clinical benefit.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT03563066](https://clinicaltrials.gov/study/NCT03563066) | Phase 2 | Completed | 20 | Small mechanistic study on eosinophil/basophil/ILC2 effects of benralizumab in AD skin. |
| [NCT04605094](https://clinicaltrials.gov/study/NCT04605094) | Phase 2 | **Terminated** | 194 | Pivotal placebo-controlled AD trial ("HILLIER"); published result shows **no significant clinical benefit** — key negative finding for this repurposing candidate. |
| [NCT04126499](https://clinicaltrials.gov/study/NCT04126499) | N/A | Completed | 28 | Observational cohort of severe eosinophilic **asthma** patients receiving benralizumab; not AD-specific. |
| [NCT04763447](https://clinicaltrials.gov/study/NCT04763447) | Phase 4 | Recruiting | 234 | Omalizumab (not benralizumab) withdrawal trial in severe asthma; of limited direct relevance. |
| [NCT06734884](https://clinicaltrials.gov/study/NCT06734884) | Phase 2 | Not yet recruiting | 96 | Anti-IL-5Rα therapy in DRESS syndrome — a different eosinophil-driven skin/systemic reaction, not AD. |
| [NCT06477653](https://clinicaltrials.gov/study/NCT06477653) | Phase 2 | Recruiting | 30 | Dupilumab add-on for hypereosinophilic syndrome in patients with partial response to eosinophil-depleting biologics (incl. benralizumab); background use only. |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [37178404](https://pubmed.ncbi.nlm.nih.gov/37178404/) | 2023 | RCT | J Eur Acad Dermatol Venereol | Full HILLIER trial results: benralizumab showed **no effect** on AD signs/symptoms vs placebo. |
| [38695680](https://pubmed.ncbi.nlm.nih.gov/38695680/) | 2024 | Plain-language summary | Immunotherapy | Patient-friendly summary of the same negative HILLIER trial. |
| [36270814](https://pubmed.ncbi.nlm.nih.gov/36270814/) | 2023 | Case report | Therapie | Reports **benralizumab-induced interstitial granulomatous dermatitis** — an adverse skin reaction, not a therapeutic benefit. |
| [38074921](https://pubmed.ncbi.nlm.nih.gov/38074921/) | 2024 | Case series | Respirology Case Reports | Dual-biologic (dupilumab + mepolizumab/benralizumab/tezepelumab) use in severe asthma with AD comorbidity; benralizumab used as asthma add-on, not primary AD treatment. |
| [31690400](https://pubmed.ncbi.nlm.nih.gov/31690400/) | 2019 | Review | Allergy Asthma Proc | Reviews immunobiologics (anti-IgE, anti-IL-5, anti-IL-4/13) across asthma, AD, urticaria; positions benralizumab primarily as an anti-IL-5 asthma agent. |
| [33717370](https://pubmed.ncbi.nlm.nih.gov/33717370/) | 2020 | Real-world experience | Open Respir Med J | Real-life biologic use across urticaria, asthma, and AD in UAE cohort. |
| [39600395](https://pubmed.ncbi.nlm.nih.gov/39600395/) | 2024 | Review | Allergologie Select | Update on biologics for atopic disease/urticaria/angioedema, contextualizing anti-IL-5 vs anti-IL-4/13 classes. |
| [36355314](https://pubmed.ncbi.nlm.nih.gov/36355314/) | 2023 | Review | Dermatol Ther | Discusses combining dupilumab with other monoclonal antibodies (incl. anti-IL-5 agents) for comorbid conditions. |
| [33138725](https://pubmed.ncbi.nlm.nih.gov/33138725/) | 2021 | Review | Otolaryngol Head Neck Surg | Reviews targeted biologics across Type 2 inflammatory conditions including AD. |
| [38878020](https://pubmed.ncbi.nlm.nih.gov/38878020/) | 2024 | Cohort study | J Allergy Clin Immunol | Patients on benralizumab/dupilumab/mepolizumab show **lower post-vaccination SARS-CoV-2 immunity** — relevant safety signal, not AD-specific. |

---

## Norway Market Information

Benralizumab has **no marketing authorizations on file for Norway** (`market_status`: 未上市 / Not marketed; `total_licenses`: 0). No licence-level indication text is available to summarize.

---

## Safety Considerations

Please refer to the package insert for safety information. Formal warnings, contraindications, and DDI data are not available in the current dataset (Data Gap DG001, marked **Blocking**).

**Additional signals identified from the literature evidence (not part of the structured safety dataset):**
- A case report of benralizumab-induced interstitial granulomatous dermatitis (PMID 36270814) — paradoxically, a skin adverse reaction rather than benefit.
- Reduced post-vaccination SARS-CoV-2 antibody response in patients on benralizumab (PMID 38878020), relevant to vaccination timing counseling.

---

## Other Candidate Indications for This Drug (Portfolio Overview)

For context, this evidence pack included four other TxGNN-predicted indications for benralizumab, none of which currently have supporting evidence:

| Rank | Disease | TxGNN Score | Evidence | Recommendation |
|------|---------|-------------|----------|-----------------|
| 1 | Thrombocytopenia due to immune destruction | 99.34% | None (no trials/literature) | Hold (L5, model-only) |
| 3 | Acne keloid | 99.13% | None (no trials/literature) | Hold (L5, model-only) |
| 4 | Neonatal dermatomyositis | 99.05% | None; mechanism mismatch (maternal antibody/IFN-I driven, not eosinophilic) | Hold (L5/S0) |
| 5 | Amyopathic dermatomyositis | 99.03% | None; mechanism mismatch (IFN-I/complement driven, not eosinophilic) | Hold (L5/S0) |

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The mechanistically plausible candidate (atopic dermatitis) has already been tested in an adequately sized Phase 2 RCT (HILLIER, N=194), which was terminated early and published as a **negative result**. TxGNN's other top-ranked candidates for this drug have no supporting clinical or literature evidence at all (L5). Combined with the drug's lack of Norway market presence and unavailable formal safety/label data, there is currently no viable repurposing pathway to advance.

**To proceed, the following is needed:**
- TFDA/manufacturer package insert (warnings, contraindications) — currently Blocking gap (DG001)
- DrugBank-sourced MOA confirmation (DG002)
- Monitor the emerging DRESS (NCT06734884) and hypereosinophilic syndrome (NCT06477653) trials — these represent mechanistically better-aligned eosinophil-driven conditions than AD, and may surface as stronger candidates once results mature
- No further investment recommended in atopic dermatitis given the existing negative RCT
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

