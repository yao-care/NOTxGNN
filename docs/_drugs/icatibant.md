---
layout: default
title: Icatibant
parent: 僅模型預測 (L5)
nav_order: 172
evidence_level: L5
indication_count: 7
---

# Icatibant
{: .fs-9 }

證據等級: **L5** | 預測適應症: **7** 個
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

# Icatibant: From Undocumented Original Indication to C1 Inhibitor Deficiency

## One-Sentence Summary

> Icatibant's original approved indication was not specified in this evidence pack (the drug is not currently marketed in Norway).
> The TxGNN model predicts it may be effective for **C1 Inhibitor Deficiency**,
> with **0 registered clinical trials** and **20 publications** currently supporting this direction.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not specified in regulatory data (drug not marketed in Norway) |
| Predicted New Indication | C1 inhibitor deficiency |
| TxGNN Prediction Score | 99.99% |
| Evidence Level | L3 |
| Norway Market Status | ✗ Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the structured evidence pack (`original_moa: [Data Gap]`). However, the supporting literature consistently and independently describes icatibant as a selective **bradykinin B2 receptor antagonist**, used to block bradykinin-mediated vascular permeability in patients with C1 inhibitor deficiency (e.g., PMID 22686628: "Icatibant, a bradykinin B2 receptor antagonist, is an established treatment for acute attacks of hereditary angioedema (HAE) with C1-inhibitor (C1-INH) deficiency"; PMID 34965883 describes it as "indicated for the acute treatment of hereditary angioedema (HAE) attacks").

No formal "original indication" field was provided for the Norway market, but the literature body — spanning national registries and cohorts from Spain, Czech Republic, UK, Italy, Croatia, and the Asia-Pacific region across 2010–2024 — consistently and specifically links icatibant to the treatment of angioedema attacks caused by C1-INH deficiency (both hereditary and acquired forms). This suggests the TxGNN-predicted association reflects an already well-established pharmacological use rather than a novel, speculative repurposing hypothesis.

Mechanistically, C1-INH deficiency leads to unchecked activation of the kallikrein-kinin cascade and excess bradykinin generation, which drives the vascular permeability and tissue swelling characteristic of angioedema attacks. Direct antagonism of the bradykinin B2 receptor addresses this core pathophysiology, which explains why the evidence base — though largely observational/registry-based rather than randomized — is broad and consistent across multiple independent populations.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [37898409](https://pubmed.ncbi.nlm.nih.gov/37898409/) | 2024 | Review | J Allergy Clin Immunol | Reviews disease burden of C1-INH-deficient HAE with focus on Asia-Pacific access gaps |
| [37716525](https://pubmed.ncbi.nlm.nih.gov/37716525/) | 2023 | Retrospective (bicenter) | JACI In Practice | Diagnosis, course, and therapy of acquired C1-INH deficiency; notes no licensed therapy exists for the acquired form |
| [37146882](https://pubmed.ncbi.nlm.nih.gov/37146882/) | 2023 | National survey | JACI In Practice | UK-wide demographic survey of HAE and acquired C1-INH deficiency patients |
| [35871284](https://pubmed.ncbi.nlm.nih.gov/35871284/) | 2023 | Retrospective chart review | J Clin Pharmacol | Documents extensive off-label use of icatibant/C1-INH concentrates in non-HAE bradykinin-mediated angioedema (2016–2020) |
| [35662289](https://pubmed.ncbi.nlm.nih.gov/35662289/) | 2022 | Registry-based analysis | Clin Exp Allergy | Icatibant and C1-inhibitor use in treating laryngeal HAE attacks |
| [34965883](https://pubmed.ncbi.nlm.nih.gov/34965883/) | 2021 | Real-world registry (Icatibant Outcome Survey) | Allergy Asthma Clin Immunol | Spain-specific outcomes for icatibant in C1-INH-deficient HAE (type 1/2) |
| [33472202](https://pubmed.ncbi.nlm.nih.gov/33472202/) | 2021 | Nationwide retrospective study | Int Arch Allergy Immunol | Czech Republic occurrence, clinical features, and management of acquired C1-INH deficiency |
| [33602658](https://pubmed.ncbi.nlm.nih.gov/33602658/) | 2021 | Review | J Investig Allergol Clin Immunol | Overview of HAE treatment landscape including kallikrein-kinin pathway inhibitors |
| [32753245](https://pubmed.ncbi.nlm.nih.gov/32753245/) | 2020 | Clinical recommendations (CREAK) | Rev Med Interne | French expert recommendations for diagnosis and treatment of acquired C1-INH-deficient angioedema |
| [30280305](https://pubmed.ncbi.nlm.nih.gov/30280305/) | 2018 | Case series | J Clin Immunol | Icatibant and recombinant C1-INH use for HAE attacks during pregnancy |

---

## Norway Market Information

Currently not marketed in Norway; no authorization records are available (`total_licenses: 0`).

---

## Safety Considerations

Please refer to the package insert for safety information. A Blocking data gap (missing TFDA-equivalent label warnings/contraindications) currently prevents a full safety review of this candidate.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The predicted indication is supported by a strong TxGNN score and a consistent, multi-national body of observational/registry literature, but no randomized clinical trial data is present in this evidence pack, and a Blocking safety data gap (DG001) explicitly prevents entry into the S1 safety review stage.

**To proceed, the following is needed:**
- TFDA-equivalent package insert (warnings, contraindications) — resolves DG001
- Confirmed mechanism of action documentation from DrugBank — resolves DG002
- Formal original indication/regulatory history for this candidate (currently absent)
- Registered clinical trial evidence, if any exists, to upgrade evidence level beyond L3
- Norway market entry/registration pathway assessment, given current "not marketed" status
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

