---
layout: default
title: Pregabalin
parent: 僅模型預測 (L5)
nav_order: 289
evidence_level: L5
indication_count: 6
---

# Pregabalin
{: .fs-9 }

證據等級: **L5** | 預測適應症: **6** 個
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

# Pregabalin: From Neuropathic Pain to Tendinitis

## One-Sentence Summary

Pregabalin is an α2δ (alpha-2-delta) voltage-gated calcium channel ligand historically used for neuropathic pain and as adjunctive therapy for partial epilepsy, with additional off-label use in generalized anxiety disorder and fibromyalgia.
The TxGNN model predicts it may be effective for **Tendinitis**, but this direction is currently supported by **0 clinical trials** and only **6 tangentially related publications** — mostly on post-surgical opioid-sparing analgesia rather than tendinitis treatment itself.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not documented in the evidence pack (no TFDA/DrugBank license text available); literature (PMID 30001248) indicates established use for neuropathic pain and adjunctive partial-epilepsy treatment |
| Predicted New Indication | Tendinitis |
| TxGNN Prediction Score | 99.71% |
| Evidence Level | L4 |
| Taiwan Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data from DrugBank is not available (flagged as a High-severity data gap). Based on what is documented in the supporting literature and the model's own rationale, pregabalin acts as a ligand of the α2δ subunit of voltage-gated calcium channels, producing central antinociceptive and anti-hyperalgesic effects. Clinically, this mechanism has been used to reduce opioid consumption after arthroscopic shoulder (rotator cuff/tendon) surgery.

However, the mechanistic link to tendinitis itself is weak. Tendinitis is fundamentally an inflammatory/degenerative condition of tendon tissue, whereas pregabalin's action is centered on central pain sensitization rather than local inflammation, collagen repair, or tendon healing. The supporting literature largely describes pregabalin as a perioperative analgesic adjunct *after* tendon surgery (e.g., rotator cuff repair) — not as a treatment for tendinitis pathology or its resolution. As the evidence pack's own rationale states, there is "no direct correspondence" between pregabalin's mechanism and the inflammatory pathology of tendinitis; the prediction appears to arise from co-occurrence in the literature (pain management around tendon procedures) rather than a disease-modifying rationale.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [32839073](https://pubmed.ncbi.nlm.nih.gov/32839073/) | 2021 | RCT | J Orthop Sci | Retrospective cohort evaluating analgesic efficacy and opioid-sparing effect of pregabalin after arthroscopic rotator cuff (tendon) repair surgery |
| [34052386](https://pubmed.ncbi.nlm.nih.gov/34052386/) | 2022 | RCT | Arthroscopy | Perioperative oral pregabalin produced pain scores comparable to interscalene brachial plexus block after arthroscopic rotator cuff repair |
| [40818536](https://pubmed.ncbi.nlm.nih.gov/40818536/) | 2025 | Review/Editorial | Arthroscopy | Editorial on piriformis syndrome diagnosis and surgical release of the piriformis tendon; not focused on pregabalin efficacy |
| [41017607](https://pubmed.ncbi.nlm.nih.gov/41017607/) | 2025 | Case Report | Praxis | Case of fluoroquinolone-associated disability including tendinopathy after ciprofloxacin; pregabalin not the subject drug |
| [37051935](https://pubmed.ncbi.nlm.nih.gov/37051935/) | 2023 | Case Report | Pain Practice | Case of posterior femoral cutaneous nerve impingement from hamstring tendonitis after marathon running |
| [39703364](https://pubmed.ncbi.nlm.nih.gov/39703364/) | 2024 | Preclinical | Adv Pharmacol Pharm Sci | Rat study of a plant extract (not pregabalin) attenuating vincristine-induced peripheral neuropathy; only tangential relevance |

Note: none of the above studies directly evaluate pregabalin as a treatment for tendinitis; relevance is indirect (perioperative pain control around tendon surgery or unrelated tendon case reports).

## Taiwan Market Information

Pregabalin is currently **not marketed** in Taiwan under this evidence pack (0 authorizations, no license records available).

## Safety Considerations

Please refer to the package insert for safety information. (Key warnings, contraindications, and DDI data are not yet available in this evidence pack; TFDA label retrieval is flagged as a Blocking data gap — DG001.)

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
No clinical trials directly test pregabalin for tendinitis, and the supporting literature addresses perioperative opioid-sparing analgesia after tendon surgery rather than tendinitis treatment or resolution. The proposed mechanism (central calcium-channel modulation of pain sensitization) does not clearly address the underlying inflammatory/degenerative pathology of tendinitis, so the evidence level remains L4 (mechanistic/indirect only).

**To proceed, the following is needed:**
- TFDA label data (warnings/contraindications) — currently Blocking (DG001)
- Confirmed mechanism of action from DrugBank (DG002)
- A prospective study designed to evaluate pregabalin's effect on tendinitis pain/healing specifically, rather than post-surgical analgesia as a surrogate
- Reassessment of the TxGNN prediction rationale to rule out confounding from co-occurrence in perioperative pain literature
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

