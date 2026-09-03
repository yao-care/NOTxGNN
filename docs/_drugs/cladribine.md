---
layout: default
title: Cladribine
parent: 僅模型預測 (L5)
nav_order: 88
evidence_level: L5
indication_count: 7
---

# Cladribine
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

Using no specific skill (straightforward report-writing task from evidence pack; no coding/debugging/brainstorming trigger). Producing report per template, with one correction: source data is `taiwan_regulatory`, not Norway, so I've labeled the market section "Taiwan" accordingly rather than guessing/copying the template's Norway wording.

---

# Cladribine: From Hairy Cell Leukemia to Parameningeal Embryonal Rhabdomyosarcoma

## One-Sentence Summary

Cladribine is a purine nucleoside (deoxyadenosine) analog originally established for **hairy cell leukemia** and **multiple sclerosis**. The TxGNN model predicts it may be effective for **parameningeal embryonal rhabdomyosarcoma**, but this is currently supported by **zero clinical trials** and **zero publications** — the prediction rests entirely on the model's graph-based score.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Hairy Cell Leukemia; Multiple Sclerosis (per known drug class profile — not derived from Taiwan license data, as the drug is not marketed there) |
| Predicted New Indication | Parameningeal Embryonal Rhabdomyosarcoma |
| TxGNN Prediction Score | 99.77% |
| Evidence Level | L5 (model prediction only, no supporting studies) |
| Taiwan Market Status | 未上市 (Not marketed) |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, an official mechanism-of-action record from DrugBank is not available (data gap DG002). Based on the drug profile embedded in the evidence pack, cladribine is a deoxyadenosine analog that, after intracellular phosphorylation, resists adenosine deaminase degradation, incorporates into DNA, and causes strand breaks that inhibit DNA synthesis and repair. This broad cytotoxic mechanism underlies its approved use in hairy cell leukemia and its immunomodulatory use in multiple sclerosis.

Hairy cell leukemia and rhabdomyosarcoma are both malignancies of rapidly dividing cells, so a generic "cytotoxic drugs can suppress proliferating tumor cells" argument is mechanistically plausible. However, there is **no rhabdomyosarcoma-specific mechanistic link** — no connection to the pathways that actually drive this pediatric solid tumor (e.g., PAX3/PAX7–FOXO1 fusion in alveolar subtypes, RAS pathway alterations in embryonal subtypes). The rationale is a class-level extrapolation, not a target-informed hypothesis.

Notably, this candidate's predicted-indication list (ranks 1–6) consists almost entirely of rhabdomyosarcoma anatomic/histologic subtypes with near-identical scores (99.69%–99.77%), suggesting TxGNN has identified a broad "rhabdomyosarcoma" cluster in the knowledge graph rather than a subtype-specific signal. The one literature citation retrieved for rank 7 (liver sarcoma) is a case report on cladribine for smoldering systemic mastocytosis — unrelated to liver sarcoma — and is best treated as a **false-positive retrieval**, not supporting evidence.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

*(Note: one literature record was retrieved elsewhere in this candidate's evidence set — PMID [15241520](https://pubmed.ncbi.nlm.nih.gov/15241520/), a 2004 case report on cladribine for systemic mastocytosis, attached to the *liver sarcoma* prediction, rank 7. It does not address rhabdomyosarcoma and is not counted as supporting evidence for the top-ranked indication.)*

---

## Taiwan Market Information

Cladribine is currently not marketed in Taiwan (0 authorizations); no product license records are available to display.

---

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Conventional cytotoxic (purine nucleoside/antimetabolite analog) |
| Myelosuppression Risk | High — purine analogs, and cladribine in particular, are associated with significant and often prolonged myelosuppression (notably profound lymphopenia); this reflects the established class profile, as quantitative TFDA/DrugBank toxicity data is not available in this evidence pack (see DG001) |
| Emetogenicity Classification | Low to Moderate (consistent with the purine analog class; specific TFDA emetogenicity data not available — see DG001) |
| Monitoring Items | CBC with differential (especially lymphocyte counts), infection surveillance, renal and hepatic function |
| Handling Protection | Yes — cytotoxic drug handling precautions apply |

---

## Safety Considerations

Please refer to the package insert for safety information. Key warnings, contraindications, and drug-interaction data are not currently available in this evidence pack (data gap DG001, Blocking severity).

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top prediction has zero clinical trial or literature support and sits at evidence level L5 (model score only), with no rhabdomyosarcoma-specific mechanistic rationale. TFDA safety data required for even a preliminary S1 safety review is missing (DG001, Blocking), and the drug is not currently marketed in Taiwan.

**To proceed, the following is needed:**
- TFDA package insert (warnings/contraindications) — required to clear the Blocking gap DG001 before any safety review
- Confirmed DrugBank MOA record (DG002)
- Preclinical (cell-line/animal model) or clinical evidence specific to rhabdomyosarcoma, ideally addressing embryonal-subtype biology
- Re-verification of the rank 7 literature match (PMID 15241520), which appears to be an irrelevant retrieval and should be excluded or corrected
- Route-of-administration and formulation compatibility assessment (currently marked "pending" for all ranked indications)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

