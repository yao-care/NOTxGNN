---
layout: default
title: Aztreonam
parent: 僅模型預測 (L5)
nav_order: 45
evidence_level: L5
indication_count: 10
---

# Aztreonam
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

# Aztreonam: From Gram-Negative Infections to Gonococcal Urethritis

## One-Sentence Summary

> Aztreonam is a monobactam antibiotic used against aerobic gram-negative bacterial infections.
> Among 10 TxGNN-predicted indications, **Gonococcal Urethritis** is the only candidate with meaningful evidence,
> supported by **1 completed clinical trial** and **8 publications** (including 1 RCT).
> The remaining 9 candidates — including the model's top-scored prediction, hyperamylasemia — lack any mechanistic or empirical support and are flagged **Hold**.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not confirmed via local licensing data; per general pharmacology, aztreonam is indicated for infections caused by aerobic gram-negative bacteria |
| Predicted New Indication | Gonococcal Urethritis |
| TxGNN Prediction Score | 99.59% |
| Evidence Level | L2 |
| Norway Market Status | Not marketed (未上市) |
| Number of Authorizations | 0 |
| Recommended Decision | Proceed with Guardrails |

**Note on ranking:** The evidence pack's top-ranked prediction (hyperamylasemia, score 99.73%) and ranks 2–3, 5–7, 9–10 are all annotated by the repurposing rationale as having **no mechanistic link** and **no clinical/literature support** (Hold, L5). This report focuses on **Gonococcal Urethritis (rank 4)**, the only candidate with real-world evidence, and briefly notes **Epiglottitis (rank 8, L4, Research Question)** as a secondary signal worth monitoring.

---

## Why is This Prediction Reasonable?

Currently, no formal MOA record is available in the evidence pack (DrugBank MOA field: Data Gap). Based on known pharmacology, aztreonam is a **monobactam antibiotic** that selectively binds to Penicillin-Binding Protein 3 (PBP3) of gram-negative bacteria, inhibiting bacterial cell wall synthesis. Its spectrum of activity is limited to aerobic gram-negative organisms, with negligible activity against gram-positive bacteria or anaerobes.

*Neisseria gonorrhoeae* is a gram-negative diplococcus, placing gonococcal urethritis squarely within aztreonam's known antibacterial spectrum. This is therefore **not a novel mechanistic inference by TxGNN, but a direct extension of an established antibacterial spectrum** — the model has essentially rediscovered a pharmacologically expected relationship. This is further reinforced by clinical context: the CDC has identified antimicrobial-resistant *N. gonorrhoeae* as a top public health threat, since ceftriaxone (a third-generation cephalosporin) is now nearly the only reliably effective first-line agent. Repurposing older, underused antibiotics like aztreonam has been explicitly proposed in the literature as a strategy to expand treatment options against resistant gonorrhea, including for pharyngeal infection sites that are harder to eradicate.

By contrast, several other TxGNN-flagged candidates are mechanistically implausible — for example, Ureaplasma urethritis is caused by cell-wall-deficient organisms (Mycoplasmataceae), against which a cell-wall synthesis inhibitor like aztreonam should theoretically have no effect. This illustrates the importance of evidence-level triage rather than acting on TxGNN scores alone.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT03867734](https://clinicaltrials.gov/study/NCT03867734) | Phase 2/3 | Completed | 32 | Single-arm, open-label demonstration study of aztreonam for pharyngeal gonorrhea, conducted in response to CDC's identification of antimicrobial-resistant *N. gonorrhoeae* as an urgent threat; evaluated an older, underused antibiotic as a potential new option given increasing resistance to first-line cephalosporins |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [3095216](https://pubmed.ncbi.nlm.nih.gov/3095216/) | 1986 | RCT (single-dose) | Genitourinary Medicine | Single 1g IM dose of aztreonam cleared infection in 61 men and 26 women at nearly all sites; well tolerated, effective against both penicillin-sensitive and penicillinase-producing strains |
| [11406757](https://pubmed.ncbi.nlm.nih.gov/11406757/) | 2001 | Review/Surveillance | J Infect Chemother | Reviews emergence of cephem/aztreonam-resistant *N. gonorrhoeae* not mediated by beta-lactamase; notes no clinical treatment failures with third-generation cephems and aztreonam had been reported to date |
| [33077658](https://pubmed.ncbi.nlm.nih.gov/33077658/) | 2020 | Cohort (single-arm, open-label) | Antimicrob Agents Chemother | Single-dose IM aztreonam (2g) trial in men, conducted to identify new gonorrhea treatment options amid ceftriaxone-resistance concerns; emphasizes need for regimens effective at the pharynx |
| [3937450](https://pubmed.ncbi.nlm.nih.gov/3937450/) | 1985 | Cohort | Hinyokika Kiyo | Japanese epidemiologic and one-shot therapy study of aztreonam for gonorrheal infections; reports resistance rates among clinical isolates |
| [6225808](https://pubmed.ncbi.nlm.nih.gov/6225808/) | 1983 | Cohort | J Infect Dis | Demonstrates aztreonam effectiveness against penicillinase-producing, penicillin-resistant gonococci amid rising global PPNG prevalence |
| [6438364](https://pubmed.ncbi.nlm.nih.gov/6438364/) | 1984 | Cohort | Jpn J Antibiot | Bacteriological and clinical evaluation of aztreonam in 30 men with gonorrheal urethritis, including PPNG and non-PPNG strains |
| [3157346](https://pubmed.ncbi.nlm.nih.gov/3157346/) | 1985 | Cohort | Antimicrob Agents Chemother | 1g IM aztreonam compared with spectinomycin for uncomplicated gonorrhea; no treatment failures with either drug across urethral, rectal, and endocervical sites |
| [6226596](https://pubmed.ncbi.nlm.nih.gov/6226596/) | 1983 | Cohort | G Ital Dermatol Venereol | Italian study of aztreonam in patients with acute gonococcal urethritis (abstract not available) |

---

## Norway Market Information

Aztreonam is currently **not marketed** in Norway, and no authorization records are available in this evidence pack.

---

## Safety Considerations

Please refer to the package insert for safety information. No structured warnings, contraindications, or drug-drug interaction data are currently available in the evidence pack (DDI query status: not found).

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Gonococcal urethritis is the only TxGNN-predicted indication in this evidence pack supported by direct mechanistic rationale (gram-negative spectrum match), a completed Phase 2/3 clinical trial, and an RCT alongside multiple decades-old cohort studies. This is a plausible, evidence-backed repurposing candidate — but the supporting trial (n=32) is small and single-arm, and most supporting literature predates modern resistance patterns, so guardrails are warranted before advancing further.

**To proceed, the following is needed:**
- Resolve **DG001 (Blocking)**: obtain TFDA/local regulatory label warnings and contraindications — required before any S1 safety pre-assessment can proceed
- Resolve **DG002 (High)**: obtain formal DrugBank MOA record to confirm mechanistic analysis
- Since the drug is not currently marketed in Norway, assess import/registration pathway feasibility
- Given the small, single-arm nature of the primary trial, consider whether additional confirmatory data (e.g., larger RCTs, current resistance surveillance) exists before clinical use is considered
- **Secondary signal for monitoring**: Epiglottitis (rank 8, L4, Research Question) — mechanistically plausible (H. influenzae, gram-negative) but only supported by non-specific gram-negative infection case series; not yet actionable
- **Deprioritize**: Ranks 1–3, 5–7, 9–10 (including the top TxGNN score, hyperamylasemia) — explicitly flagged as lacking mechanistic or empirical support; no further action recommended at this time
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

