---
layout: default
title: Durvalumab
parent: 僅模型預測 (L5)
nav_order: 117
evidence_level: L5
indication_count: 10
---

# Durvalumab
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

Using the evidence pack as given (no skill applies here — this is a direct report-writing task following the provided prompt template), here is the report.

Note on structure: this evidence pack is a **multi-indication candidate** (`TW-DB11714-multi`) — TxGNN returned 10 predicted indications for durvalumab, not one. I followed the template's extraction rule (use `predicted_indications[0]` for the headline Title/Quick Overview) but added a Portfolio table and supplementary evidence tables so the other 9 candidates — some with materially stronger evidence than the #1-ranked candidate — aren't lost.

---

# Durvalumab: From Anti-PD-L1 Immuno-Oncology to Prostatic Urethra Urothelial Carcinoma

## One-Sentence Summary

Durvalumab is an anti-PD-L1 immune checkpoint inhibitor monoclonal antibody; no approved indication is currently on file for this market and the product is **not marketed** here. The TxGNN model's top-ranked prediction is **Prostatic Urethra Urothelial Carcinoma** (score 99.98%), but this specific indication currently has **0 clinical trials** and **0 publications** directly supporting it — the rationale rests entirely on drug-class analogy to PD-L1-responsive urothelial cancers. Across the full 10-indication portfolio generated for durvalumab, **4 unique trials** and **1 publication** provide indirect support, with the strongest evidence (L2) actually found for a lower-ranked candidate, endocervical carcinoma.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not on file — drug is not marketed in this jurisdiction and DrugBank `original_indications` is empty |
| Predicted New Indication | Prostatic Urethra Urothelial Carcinoma |
| TxGNN Prediction Score | 99.98% |
| Evidence Level | L4 (mechanistic/class-analogy only; no direct trials or literature) |
| Norway Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Portfolio of Predicted Indications (Top 10)

The model returned 9 additional candidates in the same run. Two — the sarcomatoid urothelial variants — already have early-phase trial support, and one (endocervical carcinoma) has the strongest evidence level in the entire set despite ranking 6th by raw score.

| Rank | Predicted Indication | TxGNN Score | Evidence Level | Decision Stage | Recommendation |
|------|----------------------|-------------|-----------------|-----------------|-----------------|
| 1 | Prostatic urethra urothelial carcinoma | 99.98% | L4 | S0 | Hold |
| 2 | Kidney pelvis sarcomatoid transitional cell carcinoma | 99.98% | L3 | S1 | Research Question |
| 3 | Infiltrating bladder urothelial carcinoma, sarcomatoid variant | 99.98% | L3 | S1 | Research Question |
| 4 | Renal pelvis papillary urothelial carcinoma | 99.98% | L4 | S0 | Hold |
| 5 | Uterine ligament adenocarcinoma | 99.92% | L5 | S0 | Hold |
| 6 | **Endocervical carcinoma** | 99.91% | **L2** | **S2** | Research Question |
| 7 | Adenoid cystic carcinoma of the cervix uteri | 99.91% | L5 | S0 | Hold |
| 8 | Uterine ligament serous adenocarcinoma | 99.91% | L5 | S0 | Hold |
| 9 | Signet ring cell variant cervical mucinous adenocarcinoma | 99.90% | L5 | S0 | Hold |
| 10 | Intestinal variant cervical mucinous adenocarcinoma | 99.90% | L5 | S0 | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the DrugBank record (DB11714) for this evidence pack — this is flagged as data gap **DG002 (High severity)**. Based on the repurposing rationale evidence collected across all 10 predictions, durvalumab is consistently described as an **anti-PD-L1 (programmed death-ligand 1) immune checkpoint inhibitor**, a drug class with established activity in PD-L1-expressing, immunologically active tumors.

The 10 predicted indications cluster into two biological groups. The **urothelial group** (ranks 1–4: prostatic urethra, kidney pelvis, bladder sarcomatoid variant, renal pelvis papillary) shares tissue origin with bladder urothelial carcinoma — a tumor type where anti-PD-L1 agents already have broad pharmacological-class precedent — and shares PD-L1 expression and tumor mutational burden (TMB) characteristics with that established indication. This is a coherent mechanistic extension even where direct trial data is absent (ranks 1 and 4). The **gynecologic group** (ranks 5–10) is more heterogeneous: endocervical carcinoma (rank 6) has plausible mechanistic support via HPV-related tumor immunogenicity and an active trial combining durvalumab with ATR/PARP inhibition to amplify immunogenic cell death. By contrast, the rationale text for several ultra-rare variants (adenoid cystic carcinoma of the cervix, signet-ring and intestinal-variant mucinous adenocarcinoma) explicitly notes these histologies are typically associated with **low PD-L1 expression and low TMB** based on analogous tumors elsewhere in the body — meaning the mechanistic case for those specific candidates is weak even though the model score is high. These should be treated with more skepticism than the score alone suggests.

For the headline indication (prostatic urethra urothelial carcinoma), no direct clinical or literature evidence exists in this pack; the case rests solely on tissue-of-origin analogy to bladder urothelial carcinoma, which is why it is scored L4/Hold despite the highest raw TxGNN score in the set.

---

## Clinical Trial Evidence

**Prostatic urethra urothelial carcinoma (headline indication):** Currently no related clinical trials registered.

The following trials were identified for other candidates in the same portfolio and are included for context, since they inform the mechanistic case for the urothelial and gynecologic clusters above:

| Trial Number | Phase | Status | Enrollment | Relevant Indication | Key Findings |
|---------|------|------|------|------|---------|
| [NCT02812420](https://clinicaltrials.gov/study/NCT02812420) | Early Phase 1 | Active, not recruiting | 54 | Kidney pelvis sarcomatoid TCC (rank 2) / Bladder sarcomatoid variant (rank 3) | Pilot pre-surgical study of durvalumab + tremelimumab in cisplatin-ineligible, high-risk muscle-invasive urothelial carcinoma; no results reported yet |
| [NCT03912818](https://clinicaltrials.gov/study/NCT03912818) | Phase 2 | Terminated | 7 | Infiltrating bladder urothelial carcinoma, sarcomatoid variant (rank 3) | Neoadjuvant durvalumab + chemotherapy in variant histology bladder cancer; terminated with only 7 patients enrolled, reason not stated — treat as inconclusive, not a negative result |
| [NCT04065269](https://clinicaltrials.gov/study/NCT04065269) | Phase 2 | Active, not recruiting | 174 | Endocervical carcinoma (rank 6) | ATARI trial: ATR inhibitor ceralasertib ± olaparib or durvalumab in relapsed gynecological cancers stratified by ARID1A status; ongoing, no results yet |
| [NCT03452332](https://clinicaltrials.gov/study/NCT03452332) | Phase 1 | Completed | 20 | Endocervical carcinoma (rank 6) | Hypofractionated stereotactic radiotherapy + durvalumab/tremelimumab in recurrent/metastatic cervical, vaginal, or vulvar cancer; small early-phase safety/feasibility study |

---

## Literature Evidence

**Prostatic urethra urothelial carcinoma (headline indication):** Currently no related literature available.

| PMID | Year | Type | Journal | Relevant Indication | Key Findings |
|------|-----|------|------|------|---------|
| [37467967](https://pubmed.ncbi.nlm.nih.gov/37467967/) | 2023 | Review | Biomedical Journal | Endocervical carcinoma (rank 6) | Reviews small cell neuroendocrine carcinoma of the cervix — a rare, aggressive, HPV-associated cervical malignancy with no established evidence-based treatment guidelines; management currently extrapolated from small-cell lung cancer protocols |

---

## Norway Market Information

Durvalumab is **not currently marketed** in this jurisdiction. There are no marketing authorizations, product names, dosage forms, or approved indication text on file (`total_licenses: 0`).

---

## Cytotoxicity

Durvalumab is an oncology agent (anti-PD-L1 immune checkpoint inhibitor, per the repurposing rationale evidence above), so this section applies.

| Item | Content |
|------|------|
| Cytotoxicity Classification | Immunotherapy (anti-PD-L1 checkpoint inhibitor) |
| Myelosuppression Risk | Please refer to the package insert warnings and precautions |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | Please refer to the package insert warnings and precautions |
| Handling Protection | Please refer to the package insert warnings and precautions |

No DrugBank toxicity data or TFDA package insert content was available in this evidence pack to substantiate specific myelosuppression, emetogenicity, or monitoring detail — checkpoint inhibitors as a class are typically associated with immune-related adverse events (e.g., colitis, pneumonitis, hepatitis, endocrinopathies) rather than classical myelosuppression, but this should be confirmed against the actual package insert rather than assumed.

---

## Safety Considerations

Package insert warnings, contraindications, and drug-drug interaction data are not currently available for durvalumab in this evidence pack. This gap is flagged as **DG001 (Blocking severity)** — its stated impact is that the candidate **cannot proceed to the S1 safety pre-assessment gate** until TFDA package insert content is obtained and parsed. Please refer to the package insert for safety information once available.

---

## Conclusion and Next Steps

**Decision: Hold** (headline indication — prostatic urethra urothelial carcinoma)

**Rationale:**
Despite having the highest TxGNN score in the portfolio (99.98%), the headline indication has zero direct clinical trial or literature support and rests on class-level mechanistic analogy alone (L4). Separately, a **Blocking** data gap (DG001 — missing TFDA package insert) prevents this candidate from clearing the S1 safety pre-assessment gate regardless of indication-level evidence, and the drug is not currently marketed in this jurisdiction (0 authorizations).

**To proceed, the following is needed:**
- TFDA package insert (warnings, contraindications) — required to clear the S1 safety gate (DG001, Blocking)
- Detailed mechanism of action data via DrugBank API (DG002, High)
- Continued monitoring of NCT02812420 (est. completion 2027-12) and NCT04065269 (est. completion 2026-08) for interim or final results
- Given the evidence asymmetry within this portfolio, prioritize **endocervical carcinoma** (rank 6, L2, S2 — Research Question) and the **sarcomatoid urothelial variants** (ranks 2–3, L3, S1 — Research Question) for active tracking, since they currently carry more mature evidence than the top-ranked headline indication
- Periodic re-query of ClinicalTrials.gov/PubMed specifically for "prostatic urethra urothelial carcinoma" + durvalumab, as no direct evidence currently exists for this exact indication
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

