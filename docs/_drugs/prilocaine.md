---
layout: default
title: Prilocaine
parent: 僅模型預測 (L5)
nav_order: 291
evidence_level: L5
indication_count: 10
---

# Prilocaine
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

# Prilocaine: From Local Anesthesia to Neuralgia

## One-Sentence Summary

> Prilocaine is an amide-type local anesthetic, most widely used in combination with lidocaine as the eutectic mixture EMLA® cream for topical/regional anesthesia.
> Among 10 TxGNN-predicted indications, **Neuralgia** (particularly postherpetic neuralgia) stands out as the only candidate with substantive supporting evidence,
> with **12 clinical trials** and **20 publications** identified, including several completed RCTs on lidocaine-prilocaine cream in postherpetic neuralgia.

*Note: TxGNN generated 10 candidate indications for prilocaine in this evidence pack; the other 9 (e.g., papillary conjunctivitis, manic bipolar disorder, bronchitis, allergic asthma, rosacea conjunctivitis) had no clinical trial or literature support and were scored L4–L5/Hold. This report focuses on the one candidate (Neuralgia) that reached decision stage S3.*

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not formally registered in this dataset — clinically established as a local/regional anesthetic (typically combined with lidocaine as EMLA cream) |
| Predicted New Indication | Neuralgia (postherpetic neuralgia) |
| TxGNN Prediction Score | 99.34% |
| Evidence Level | L2 |
| Norway Market Status | ✗ Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this evidence pack (DG002). Based on established pharmacology, prilocaine is an amide-type local anesthetic that, after topical or subcutaneous administration, blocks voltage-gated sodium channels on peripheral neurons, inhibiting depolarization and action potential propagation. It is most commonly used clinically as part of EMLA (eutectic mixture of lidocaine 2.5% and prilocaine 2.5%) for procedural and dermatologic anesthesia.

Neuralgia — especially postherpetic neuralgia (PHN) — is characterized by aberrant peripheral sensory nerve firing and sensitization. Sodium-channel blockade by prilocaine (in combination with lidocaine) provides a mechanistically plausible route to reducing this abnormal signaling, and EMLA cream already has decades of clinical use for neuralgic pain relief, both as a standalone analgesic and as a pretreatment to reduce procedural pain (e.g., before capsaicin 8% patch application).

The key limitation is that essentially all supporting evidence involves prilocaine **in combination with lidocaine** (EMLA), not prilocaine as monotherapy. No identified trial isolates prilocaine's independent contribution to neuralgia relief.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00916942](https://clinicaltrials.gov/study/NCT00916942) | Phase 2 | Completed | 20 | Open-label study of topical lidocaine 2.5%/prilocaine 2.5% cream as pre-treatment for NGX-4010 (capsaicin patch) in postherpetic neuralgia |
| [NCT06247592](https://clinicaltrials.gov/study/NCT06247592) | N/A | Unknown | 70 | Greater occipital nerve block using 2% prilocaine vs pulsed radiofrequency in chronic migraine |
| [NCT06899438](https://clinicaltrials.gov/study/NCT06899438) | N/A | Completed | 38 | Prilocaine injection vs botulinum toxin A compared for myofascial pain syndrome trigger points |
| [NCT07021365](https://clinicaltrials.gov/study/NCT07021365) | N/A | Not yet recruiting | 30 | Ganglion impar radiofrequency ablation vs phenol neurolysis for chronic coccydynia (local-anesthetic-based nerve block techniques) |
| [NCT03587220](https://clinicaltrials.gov/study/NCT03587220) | N/A | Completed | 44 | Mechanistic study of capsaicin-induced desensitization combined with topical local anesthetic on cutaneous nociceptive C-fibers |
| [NCT03220113](https://clinicaltrials.gov/study/NCT03220113) | Phase 1/2 | Unknown | 100 | De-Novo algorithm (dexamethasone, lidocaine, thiamine) injected into trigeminal/occipital nerve branches for chronic craniofacial neuralgia/migraine |
| [NCT05411900](https://clinicaltrials.gov/study/NCT05411900) | Phase 2 | Unknown | 164 | RCT of repeated botulinum toxin A injections for peripheral neuropathic pain in carpal tunnel syndrome |
| [NCT02736890](https://clinicaltrials.gov/study/NCT02736890) | Phase 2 | Terminated | 8 | Subcutaneous botulinum toxin A for at-level back pain in spinal cord injury |
| [NCT01911377](https://clinicaltrials.gov/study/NCT01911377) | Phase 2 | Terminated | 12 | Botulinum toxin A for allodynic-type neuropathic pain in spinal cord injury/multiple sclerosis |
| [NCT04914637](https://clinicaltrials.gov/study/NCT04914637) | N/A | Completed | 66 | Dry needling combined with interlaminar epidural steroid injection for chronic neck pain from cervical disc herniation |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [2493878](https://pubmed.ncbi.nlm.nih.gov/2493878/) | 1989 | RCT | BMJ | Lignocaine-prilocaine cream significantly reduced pain in postherpetic neuralgia |
| [2616182](https://pubmed.ncbi.nlm.nih.gov/2616182/) | 1989 | RCT | Pain | EMLA cream (5–10g, 24h application) significantly improved pain intensity in refractory PHN, including facial PHN subgroup |
| [22182397](https://pubmed.ncbi.nlm.nih.gov/22182397/) | 2011 | RCT | BMC Anesthesiol | Lidocaine 2.5%/prilocaine 2.5% cream pretreatment improved tolerability of capsaicin 8% patch (NGX-4010) in PHN patients |
| [1430539](https://pubmed.ncbi.nlm.nih.gov/1430539/) | 1992 | Review | J Dermatol Surg Oncol | EMLA reviewed as an effective, safe topical anesthetic, including use in postherpetic neuralgia |
| [10353509](https://pubmed.ncbi.nlm.nih.gov/10353509/) | 1999 | Cohort | Pain | Single and repeated EMLA applications reduced spontaneous and evoked pain in PHN patients (n=11) |
| [12378018](https://pubmed.ncbi.nlm.nih.gov/12378018/) | 2002 | Cohort | J Korean Med Sci | Identified prognostic factors (age, affected area, pain duration) for progression to postherpetic neuralgia |
| [24310458](https://pubmed.ncbi.nlm.nih.gov/24310458/) | 2013 | Review | Turk Neurosurg | Evaluated invasive procedures for medically intractable genitofemoral/ilioinguinal neuralgia |
| [23314014](https://pubmed.ncbi.nlm.nih.gov/23314014/) | 2013 | Review | Curr Opin Support Palliat Care | Evidence-based approach to managing persistent wound-related pain, including topical anesthetics |
| [2046584](https://pubmed.ncbi.nlm.nih.gov/2046584/) | 1991 | Case report | Med J Aust | Early clinical report on EMLA cream use in herpetic neuralgia |
| [1875823](https://pubmed.ncbi.nlm.nih.gov/1875823/) | 1991 | Case report | Med J Aust | Companion report on EMLA cream in herpetic neuralgia |

---

## Norway Market Information

Prilocaine currently has **no marketing authorization on file in Norway** (market status: 未上市 / Not marketed; total licenses: 0). No product-level dosage form or approved-indication data is available.

---

## Safety Considerations

Please refer to the package insert for safety information. Formal key warnings, contraindications, and drug-drug interaction data (DG001) are not yet available for this drug in the current dataset and must be obtained from the TFDA/Norway product label before clinical use is expanded to a new indication.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Three completed RCTs (tier 1) and one completed Phase 2 trial support lidocaine-prilocaine cream (EMLA) for pain relief in postherpetic neuralgia, with a coherent sodium-channel-blockade mechanism. However, prilocaine has not been tested as monotherapy, and it currently has no Norway market authorization.

**To proceed, the following is needed:**
- Official TFDA/Norway package insert data — key warnings and contraindications (DG001, currently blocking)
- Verified mechanism-of-action documentation from DrugBank or equivalent source (DG002)
- Evidence isolating prilocaine's independent contribution versus the lidocaine-prilocaine combination
- Assessment of methemoglobinemia and systemic absorption risk — a known class effect of prilocaine, particularly relevant if topical use is expanded to patients with compromised skin barrier
- A regulatory pathway assessment, since prilocaine is not currently marketed in Norway (0 authorizations on file)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

