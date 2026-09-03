---
layout: default
title: Daptomycin
parent: 僅模型預測 (L5)
nav_order: 95
evidence_level: L5
indication_count: 10
---

# Daptomycin
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

# Daptomycin: From Gram-Positive Bacterial Infections to Osteoarthritis (Low-Confidence Signal)

## One-Sentence Summary

> Daptomycin is a cyclic lipopeptide antibiotic used to treat Gram-positive infections such as skin infections, bacteraemia, and right-sided endocarditis.
> The TxGNN model's top prediction is **Osteoarthritis**, but the supporting literature consists entirely of studies on *osteoarticular/prosthetic joint infection* treatment — not osteoarthritis itself —
> suggesting this signal is likely an entity-confusion artefact rather than genuine repurposing evidence. A biologically more plausible (but still preclinical) signal exists at rank 2 for **Rheumatoid Arthritis**.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not formally recorded (drug not marketed in Norway); per literature, daptomycin is approved for Gram-positive infections including skin infections, bacteraemia, and right-sided endocarditis |
| Predicted New Indication | Osteoarthritis |
| TxGNN Prediction Score | 99.86% (rank 1948) |
| Evidence Level | L4 |
| Norway Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available (blocked pending DrugBank query — see Data Gap DG002). Based on known information, daptomycin is a cyclic lipopeptide antibiotic that depolarizes the bacterial cell membrane, producing a bactericidal effect specific to Gram-positive organisms. This mechanism has no established biological link to the cartilage degradation and low-grade inflammatory processes that drive osteoarthritis (OA).

Critically, every piece of literature supporting the top-ranked "osteoarthritis" prediction is actually about *osteoarticular infection* or *prosthetic joint infection (PJI)* — i.e., antibiotic treatment and susceptibility of *S. aureus*/*S. epidermidis* in infected joints — not about osteoarthritis pathophysiology or treatment. This strongly suggests the knowledge graph has conflated the entities "osteoarticular infection" and "osteoarthritis," producing a high-confidence but likely spurious prediction. One outlier case report even involves *Corynebacterium* septic arthritis in a patient originally worked up for OA, further illustrating this confusion.

By contrast, the rank-2 prediction (**Rheumatoid Arthritis**) is supported by two 2025 preclinical studies showing daptomycin suppresses inflammatory cytokines and NF-κB signalling in a collagen-induced arthritis mouse model, and that structurally optimized daptomycin derivatives have enhanced anti-RA activity in vivo. This represents a genuine, if early-stage, mechanistic hypothesis (immunomodulation independent of antibacterial activity) and is arguably the more scientifically interesting signal in this evidence pack, despite its lower TxGNN score.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [23519823](https://pubmed.ncbi.nlm.nih.gov/23519823/) | 2013 | Cohort | Int Orthop | High-dose daptomycin + rifampicin for Gram-positive osteoarticular infections (not OA treatment) |
| [22511636](https://pubmed.ncbi.nlm.nih.gov/22511636/) | 2012 | Cohort | J Antimicrob Chemother | Daptomycin for knee/hip prosthetic joint infections |
| [26235888](https://pubmed.ncbi.nlm.nih.gov/26235888/) | 2015 | Cohort | Int J Antimicrob Agents | High-dose daptomycin (>6 mg/kg) for complicated bone/joint and implant infections |
| [17999973](https://pubmed.ncbi.nlm.nih.gov/17999973/) | 2008 | Cohort | J Antimicrob Chemother | Daptomycin vs standard therapy for osteoarticular infections with S. aureus bacteraemia |
| [22854340](https://pubmed.ncbi.nlm.nih.gov/22854340/) | 2012 | In vitro | J Antibiot | In vitro susceptibility of S. aureus/S. epidermidis from prosthetic joint infections |
| [21477701](https://pubmed.ncbi.nlm.nih.gov/21477701/) | 2010 | Registry/Cohort | Med Clin (Barc) | EU-CORE registry: Spanish real-world daptomycin use across Gram-positive infections |
| [32206362](https://pubmed.ncbi.nlm.nih.gov/32206362/) | 2020 | Case Report | Case Rep Orthop | Chronic *Corynebacterium striatum* septic arthritis initially referred for OA/TKA workup |
| [23312602](https://pubmed.ncbi.nlm.nih.gov/23312602/) | 2013 | Cohort | Int J Antimicrob Agents | Survey of prosthetic joint infection management practices (antibiotic choice) |
| [25650692](https://pubmed.ncbi.nlm.nih.gov/25650692/) | 2015 | Cohort | Surg Infect | 10-year microbiologic profile of Staphylococci in osteoarticular infections |
| [41853106](https://pubmed.ncbi.nlm.nih.gov/41853106/) | 2026 | Case Report | ASM Case Rep | First reported *Corynebacterium propinquum* septic arthritis in a native joint |

**Note:** None of the above literature addresses osteoarthritis pathophysiology or treatment efficacy; all relate to bacterial osteoarticular/prosthetic joint infections, reinforcing the assessment that this is an entity-confusion artefact.

---

## Norway Market Information

Daptomycin is currently **not marketed** in Norway (0 authorizations on file); no product license records are available.

---

## Safety Considerations

- **Data Gap (Blocking):** TFDA-equivalent package insert warnings and contraindications have not yet been retrieved (Data Gap DG001), so a formal S1 safety pre-assessment cannot proceed.
- **Literature Safety Signal:** One case report ([PMID 36693494](https://pubmed.ncbi.nlm.nih.gov/36693494/)) describes daptomycin-induced rhabdomyolysis complicated by acute gouty arthritis, consistent with daptomycin's known dose-related creatine kinase (CK) elevation toxicity. This appeared as a rank-4 TxGNN "gout" prediction but is properly interpreted as an adverse-event signal, not a therapeutic indication.
- **Drug Interaction Data:** Not found in the current evidence pack (query status: not_found).

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked prediction (osteoarthritis) is supported only by literature on unrelated osteoarticular *infections*, indicating a likely knowledge-graph entity-confusion artefact rather than genuine repurposing evidence. The one mechanistically credible signal (rheumatoid arthritis, rank 2) is still at the animal-model stage with no clinical trials. Combined with the absence of TFDA-equivalent safety data and the drug's unmarketed status in Norway, there is insufficient evidence to advance to formal evaluation.

**To proceed, the following is needed:**
- TFDA-equivalent warnings/contraindications data (blocking — DG001)
- Confirmed mechanism of action from DrugBank (DG002)
- Independent validation (in vivo/in vitro replication or early clinical data) of the daptomycin anti-inflammatory/NF-κB signal in rheumatoid arthritis before considering it a research priority over the osteoarthritis signal
- Drug-drug interaction data
- Clarification with the TxGNN knowledge graph team on possible entity overlap between "osteoarticular infection" and "osteoarthritis"
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

