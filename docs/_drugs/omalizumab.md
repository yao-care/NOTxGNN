---
layout: default
title: Omalizumab
parent: 僅模型預測 (L5)
nav_order: 254
evidence_level: L5
indication_count: 10
---

# Omalizumab
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

# Omalizumab: From Allergic Asthma to Bronchitis

## One-Sentence Summary

> Omalizumab is a humanized anti-IgE monoclonal antibody with internationally established efficacy in severe allergic asthma; it is not currently marketed in Norway.
> The TxGNN model predicts it may be effective for **Bronchitis**,
> with **2 clinical trials** and **8 publications** currently identified, though most of this evidence comes from asthma populations rather than a confirmed bronchitis diagnosis.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not licensed in Norway; internationally recognized for severe allergic asthma (per literature evidence in this pack) |
| Predicted New Indication | Bronchitis |
| TxGNN Prediction Score | 99.9992% |
| Evidence Level | L3 |
| Norway Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this evidence pack. Based on known information drawn from the attached literature, omalizumab is a humanized anti-IgE monoclonal antibody that binds free IgE and reduces FcεRI expression on mast cells and basophils, which decreases IgE-mediated airway inflammation. Its efficacy in severe allergic asthma has been well documented, and mechanistically this same pathway may be relevant to bronchitis when the underlying inflammation is allergic or eosinophilic in nature.

Bronchitis and asthma frequently overlap clinically — eosinophilic bronchitis and asthma share airway inflammatory features, and smoking-induced chronic bronchitis is often discussed alongside asthma-COPD overlap. This overlap is the basis for the TxGNN prediction.

However, it is important to note that the two clinical trials retrieved for this indication (NCT02477332 and NCT02049294) were not designed with bronchitis as the primary diagnosis — the enrolled populations were asthma patients (one for chronic spontaneous urticaria dose-finding, one for asthma with eosinophilic bronchitis as a steroid-sparing sub-study of only 11 patients). The mechanistic link is therefore indirect, inferred through the asthma–bronchitis overlap rather than direct clinical evidence in a bronchitis-diagnosed population.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT02477332](https://clinicaltrials.gov/study/NCT02477332) | Phase 2b | Completed | 382 | Dose-finding study of QGE031 (ligelizumab, an anti-IgE agent) as add-on therapy in chronic spontaneous urticaria — not a bronchitis-specific trial; included for mechanistic relevance only |
| [NCT02049294](https://clinicaltrials.gov/study/NCT02049294) | Phase 2/3 | Completed | 11 | Randomized, placebo-controlled trial evaluating whether omalizumab allows steroid dose reduction in patients with asthma and persistent eosinophilic bronchitis; very small sample size limits conclusiveness |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [35369622](https://pubmed.ncbi.nlm.nih.gov/35369622/) | 2022 | Cohort | Postepy Dermatologii i Alergologii | Biologic therapy (including omalizumab) may benefit older patients with severe allergic asthma-COPD overlap phenotype |
| [16222080](https://pubmed.ncbi.nlm.nih.gov/16222080/) | 2005 | Review | Clin Rev Allergy Immunol | Overview of omalizumab approval and post-approval experience in moderate-to-severe persistent asthma |
| [30196731](https://pubmed.ncbi.nlm.nih.gov/30196731/) | 2018 | Review | Expert Opin Pharmacother | Discusses treatment challenges in smoking-induced airway disease, including chronic bronchitis, in asthma and asthma-COPD overlap patients |
| [21163396](https://pubmed.ncbi.nlm.nih.gov/21163396/) | 2010 | Review | Rev Mal Respir | French expert review on definitions and treatment of adult asthma exacerbations |
| [26466493](https://pubmed.ncbi.nlm.nih.gov/26466493/) | 2015 | Review | Masui | Japanese perioperative management review noting omalizumab's role in severe allergic asthma alongside bronchitis-related airway inflammation |
| [21121874](https://pubmed.ncbi.nlm.nih.gov/21121874/) | 2011 | Pooled Analysis | Curr Med Res Opin | Pooled safety analysis of omalizumab in children with allergic (IgE-mediated) asthma |
| [17663923](https://pubmed.ncbi.nlm.nih.gov/17663923/) | 2007 | Review | Allergol Immunopathol | General review of monoclonal antibody use in pediatric allergic and respiratory disease |
| [31478531](https://pubmed.ncbi.nlm.nih.gov/31478531/) | 2019 | Case Report | J Investig Allergol Clin Immunol | Rare case of plastic bronchitis following bronchial thermoplasty; not related to omalizumab treatment |

---

## Norway Market Information

Omalizumab currently has **no market authorization records in Norway** (0 licenses, market status: Not Marketed). No product, dosage form, or approved indication text is available for this jurisdiction.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The clinical trial and literature evidence for bronchitis is indirect — the two supporting trials primarily enrolled asthma patients rather than subjects with a confirmed bronchitis diagnosis, and no direct RCT targets bronchitis as the primary endpoint. Combined with the drug's current lack of market authorization in Norway and outstanding blocking safety data gaps, the evidence does not yet support advancing this indication.

**To proceed, the following is needed:**
- TFDA/Norway product labeling with warnings and contraindications (currently a Blocking data gap)
- Detailed mechanism of action (MOA) documentation from DrugBank (currently a High-severity data gap)
- Dedicated clinical trials enrolling patients with a confirmed (eosinophilic) bronchitis diagnosis, rather than asthma-overlap populations
- Clarification of the regulatory pathway, given zero existing Norway market authorizations

**Note:** Within this same evidence pack, the predicted indication "obstructive lung disease" (rank 3) has substantially stronger, more direct evidence (Evidence Level L1, multiple completed Phase 3 RCTs directly evaluating omalizumab in allergic asthma) and may warrant a separate, higher-priority evaluation.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

