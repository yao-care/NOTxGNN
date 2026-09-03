---
layout: default
title: Tolvaptan
parent: 僅模型預測 (L5)
nav_order: 363
evidence_level: L5
indication_count: 10
---

# Tolvaptan
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

# Tolvaptan: From Hyponatremia (SIADH) to Autosomal Dominant Polycystic Kidney Disease (ADPKD)

## One-Sentence Summary

> Tolvaptan is a vasopressin V2-receptor antagonist historically used to treat hyponatremia related to SIADH, heart failure, and cirrhosis.
> The TxGNN model's top prediction points to **Polycystic Kidney Disease 3, with or without Polycystic Liver Disease** — a rare monogenic variant within the broader Autosomal Dominant Polycystic Kidney Disease (ADPKD) spectrum —
> and this direction is backed by **two landmark completed Phase 3 RCTs** (TEMPO 3:4, REPRISE) plus **20 supporting publications**, including consensus guidelines and a Cochrane systematic review. Notably, tolvaptan already holds approved ADPKD indications abroad (e.g., Jinarc/Jynarque in the EU/US/Japan), so this is best understood as the model correctly re-identifying an established, high-confidence indication rather than a purely novel signal.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Hyponatremia due to SIADH (Samsca) — established global label; **not confirmed in the Norway regulatory data pack**, which currently lists 0 authorizations |
| Predicted New Indication | Polycystic Kidney Disease 3, with/without Polycystic Liver Disease (ADPKD/PLD spectrum) |
| TxGNN Prediction Score | 99.99% (rank 319 overall) |
| Evidence Level | L1 (≥2 completed Phase 3 RCTs: TEMPO 3:4, REPRISE) |
| Norway Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

DrugBank-sourced mechanism-of-action data is currently unavailable (data gap DG002). However, the literature evidence collected in this pack consistently and independently identifies tolvaptan as a **selective vasopressin V2-receptor antagonist**. By blocking V2 receptor signaling in renal collecting duct cells, tolvaptan reduces intracellular cAMP, which is the principal driver of cyst-lining epithelial proliferation and fluid secretion in polycystic kidney disease. This mechanistic link — cAMP suppression halting cystogenesis — is the pharmacological basis repeatedly cited across the ADPKD literature in this pack (e.g., PMID 35328738, 40126492).

The relationship between tolvaptan's original use (aquaresis in hyponatremia/fluid-overload states) and the predicted indication is mechanistically coherent: both applications exploit V2-receptor blockade, just in different target tissues (systemic water handling vs. renal cyst epithelium). Critically, this is not a speculative extrapolation — tolvaptan **already carries approved ADPKD indications in the US, EU, and Japan** (branded Jynarque/Jinarc), built on the same TEMPO 3:4 and REPRISE trials surfaced by this evidence pack. The TxGNN model is therefore reproducing a well-validated, real-world indication rather than proposing something untested.

One caveat: the specific predicted disease term is "Polycystic Kidney Disease **3**" (a rarer PKD3 monogenic subtype, distinct from the far more common PKD1/PKD2-driven ADPKD). All clinical evidence in this pack (TEMPO 3:4, REPRISE, pediatric trials) was conducted in the broader ADPKD population, not PKD3 specifically. The ontology mapping likely captures the general ADPKD/PLD disease family, but this distinction should be verified before any indication-specific regulatory claim is made.

---

## Clinical Trial Evidence

Currently no related clinical trials registered in the structured `clinical_trials` field for this indication. (Note: the pivotal trials establishing this indication — TEMPO 3:4 and REPRISE — are captured as published literature below rather than as registry entries in this data pull.)

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [23121377](https://pubmed.ncbi.nlm.nih.gov/23121377/) | 2012 | RCT (Phase 3, TEMPO 3:4) | NEJM | Tolvaptan slowed growth in total kidney volume and decline in eGFR in early-stage ADPKD |
| [29105594](https://pubmed.ncbi.nlm.nih.gov/29105594/) | 2017 | RCT (Phase 3, REPRISE) | NEJM | Preserved kidney function in later-stage ADPKD; more frequent elevations in aminotransferase/bilirubin observed |
| [38091246](https://pubmed.ncbi.nlm.nih.gov/38091246/) | 2024 | RCT (Pediatric, NCT02964273) | Pediatr Nephrol | Evaluated tolvaptan safety/pharmacodynamics in children (5–17y) with ADPKD |
| [37150675](https://pubmed.ncbi.nlm.nih.gov/37150675/) | 2023 | Systematic Review/Meta-analysis | Nefrologia | Confirmed pooled efficacy and safety profile of tolvaptan in ADPKD |
| [39356039](https://pubmed.ncbi.nlm.nih.gov/39356039/) | 2024 | Systematic Review (Cochrane) | Cochrane Database Syst Rev | Reviewed disease-modifying agents, including tolvaptan, for ADPKD progression prevention |
| [35134221](https://pubmed.ncbi.nlm.nih.gov/35134221/) | 2022 | Consensus Statement | Nephrol Dial Transplant | ERA Working Group/PKD International consensus on evidence-based tolvaptan initiation in ADPKD |
| [40126492](https://pubmed.ncbi.nlm.nih.gov/40126492/) | 2025 | Review | JAMA | Comprehensive ADPKD review covering pathophysiology and management, including tolvaptan |
| [35487607](https://pubmed.ncbi.nlm.nih.gov/35487607/) | 2022 | Review | Clin Liver Dis | Confirms tolvaptan slows renal function decline and cyst growth in ADPKD/PCLD overlap |
| [35728731](https://pubmed.ncbi.nlm.nih.gov/35728731/) | 2022 | Guideline (EASL) | J Hepatol | Clinical practice guideline for cystic liver disease, including the polycystic liver disease component |
| [35328738](https://pubmed.ncbi.nlm.nih.gov/35328738/) | 2022 | Review | Int J Mol Sci | Reviews ADPKD cystogenesis pathophysiology and treatment advances |

---

## Norway Market Information

Tolvaptan currently has **no marketing authorizations on file in Norway** (0 licenses; market status "Not Marketed"). No product/dosage-form data is available to summarize.

---

## Safety Considerations

Please refer to the package insert for safety information — no structured warnings, contraindications, or DDI data are currently available in this evidence pack (flagged as **Blocking** data gap DG001).

That said, the pivotal REPRISE trial (PMID 29105594) explicitly reports **more frequent elevations in liver aminotransferases and bilirubin** with tolvaptan versus placebo — this hepatotoxicity signal is well documented in tolvaptan's approved labels elsewhere (boxed warning in the US) and should be treated as a known class-relevant risk pending confirmation of the local label.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Efficacy evidence for tolvaptan in ADPKD is exceptionally strong (L1 — two completed, published Phase 3 RCTs plus consensus guidelines), and the indication is already approved in major markets. However, Norway has zero existing authorizations and a Blocking data gap on local warnings/contraindications, so market entry cannot proceed without completing the safety dossier.

**To proceed, the following is needed:**
- Resolve DG001 (Blocking): obtain the approved EU/Norway-equivalent SmPC (e.g., Jinarc) for TFDA-equivalent warnings and contraindications
- Resolve DG002 (High): confirm DrugBank MOA record to formally support the mechanistic rationale
- Verify whether the target ontology term (PKD3-specific) should be reconciled to the broader ADPKD (PKD1/PKD2) population studied in TEMPO 3:4/REPRISE
- Establish a hepatic monitoring protocol (LFTs) given the documented hepatotoxicity signal, before any Norway MAA submission

**Note on lower-ranked predictions:** Ranks 2–10 (renal-hepatic-pancreatic dysplasia, karyomegalic interstitial nephritis, thoracic malformation, Joubert syndrome, hypertrichosis, periodontal-component syndromes, Dandy-Walker malformation syndrome, etc.) carry L4–L5 evidence at best, with most literature hits assessed as irrelevant or off-target (e.g., the periodontitis literature retrieved for rank 9 has no mechanistic connection to tolvaptan). These are held (Hold) and not pursued further in this report.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

