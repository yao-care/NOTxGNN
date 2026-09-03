---
layout: default
title: Ipilimumab
parent: 僅模型預測 (L5)
nav_order: 190
evidence_level: L5
indication_count: 2
---

# Ipilimumab
{: .fs-9 }

證據等級: **L5** | 預測適應症: **2** 個
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

# Ipilimumab: From Cutaneous Melanoma to Non-Cutaneous Melanoma

## One-Sentence Summary

> Ipilimumab is an anti-CTLA-4 immune checkpoint inhibitor originally established for (cutaneous) metastatic melanoma.
> The TxGNN model additionally predicts activity in **Non-Cutaneous Melanoma** (uveal, mucosal, acral, and CNS-metastatic subtypes),
> with **80 clinical trials** and **5 publications** identified in the evidence pack, including several completed Phase 2/3 studies specific to non-cutaneous subtypes.

*Note: The evidence pack also contained a second TxGNN prediction — **choroideremia** (score 99.06%, rank 9029) — but this candidate has zero supporting trials or literature, and the pack itself states there is no known mechanistic link between anti-CTLA-4 immune activation and this monogenic retinal degeneration. It has been screened out (evidence level L5, decision stage S0, recommendation **Hold**) and is not discussed further below.*

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Metastatic (cutaneous) melanoma — no local license on file (see note below) |
| Predicted New Indication | Non-Cutaneous Melanoma (uveal, mucosal, acral, leptomeningeal-metastatic) |
| TxGNN Prediction Score | 99.02% |
| Evidence Level | L2 |
| Norway Market Status | Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Ipilimumab is an anti-CTLA-4 monoclonal antibody. It blocks the inhibitory CTLA-4 signal on T cells, thereby restoring and amplifying tumor-specific T-cell activation and proliferation. Critically, this is a **host immune-modulation mechanism**, not one that targets a specific tumor genotype (e.g., BRAF mutation status). Because the drug acts on the patient's immune system rather than on melanoma-specific molecular drivers, there is a plausible mechanistic rationale for activity across melanoma subtypes beyond the cutaneous form — including uveal, mucosal, acral, and CNS-metastatic (leptomeningeal) disease.

Ipilimumab is already established for metastatic cutaneous melanoma. The predicted new indication, non-cutaneous melanoma, represents a **label-adjacent extension** within the same disease family rather than a novel therapeutic area — a pattern generally associated with lower repurposing risk. That said, the rationale in the evidence pack flags an important caveat: uveal melanoma occurs in an immune-privileged ocular environment and typically carries a lower tumor mutational burden, and mucosal melanoma shows a similar, though less pronounced, pattern. Both subtypes have historically shown **lower response rates to checkpoint inhibition** than cutaneous disease, which tempers — but does not eliminate — the mechanistic plausibility.

Detailed drug-level mechanism-of-action documentation (DrugBank MOA field) was not available in this evidence pack; the mechanistic description above is derived from the repurposing rationale rather than a structured MOA record.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT01654692](https://clinicaltrials.gov/study/NCT01654692) | Phase 2 | Completed | 86 | Ipilimumab + fotemustine in unresectable/locally advanced or metastatic melanoma, including uveal melanoma population — direct, completed evidence (Grade A) |
| [NCT02626962](https://clinicaltrials.gov/study/NCT02626962) | Phase 2 | Completed | 52 | Nivolumab + ipilimumab in previously untreated metastatic **uveal** melanoma — directly relevant non-cutaneous subtype |
| [NCT01730157](https://clinicaltrials.gov/study/NCT01730157) | Early Phase 1 | Terminated | 6 | Sequential hepatic radioembolization + ipilimumab in **uveal** melanoma with liver metastases |
| [NCT02939300](https://clinicaltrials.gov/study/NCT02939300) | Phase 2 | Completed | 18 | Ipilimumab + nivolumab in melanoma **leptomeningeal metastases** (Grade B) |
| [NCT03220009](https://clinicaltrials.gov/study/NCT03220009) | Phase 2 | Withdrawn | 0 | Adjuvant nivolumab vs. observation after neoadjuvant ipilimumab+nivolumab in **mucosal** melanoma — directly relevant subtype but trial withdrawn |
| [NCT02224781](https://clinicaltrials.gov/study/NCT02224781) | Phase 3 | Active, not recruiting | 267 | DREAMseq: sequencing of ipilimumab+nivolumab vs. targeted therapy in advanced melanoma (Grade B, indirect support) |
| [NCT01927419](https://clinicaltrials.gov/study/NCT01927419) | Phase 2 | Completed | 142 | Randomized double-blind nivolumab+ipilimumab vs. ipilimumab alone in untreated advanced melanoma (Grade B, indirect support) |
| [NCT01810016](https://clinicaltrials.gov/study/NCT01810016) | Phase 1 | Terminated | 8 | NY-ESO-1 vaccine + ipilimumab in unresectable/metastatic melanoma (Grade C, weak evidence) |
| [NCT02388906](https://clinicaltrials.gov/study/NCT02388906) | Phase 3 | Completed | 906 | CheckMate 238: adjuvant nivolumab vs. ipilimumab after resection of high-risk melanoma — large completed RCT, general population |
| [NCT01515189](https://clinicaltrials.gov/study/NCT01515189) | Phase 3 | Completed | 831 | Ipilimumab 3 mg/kg vs. 10 mg/kg in previously treated/untreated melanoma — large completed dose-finding RCT, general population |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [24999899](https://pubmed.ncbi.nlm.nih.gov/24999899/) | 2014 | Cohort | The Medical Journal of Australia | Real-world efficacy/tolerability of ipilimumab across **cutaneous, uveal, and mucosal** melanoma; assessed response by subtype, BRAF status, and irAE incidence |
| [28183255](https://pubmed.ncbi.nlm.nih.gov/28183255/) | 2018 | Review | Current Cancer Drug Targets | Systematic review of melanoma adjuvant treatment (2000–2015); explicitly notes non-cutaneous melanoma comprises ~5% of cases |
| [37887546](https://pubmed.ncbi.nlm.nih.gov/37887546/) | 2023 | Cohort | Current Oncology | Retrospective multicenter cohort comparing anti-PD-1 monotherapy vs. combination with ipilimumab by age group in advanced melanoma |
| [29466692](https://pubmed.ncbi.nlm.nih.gov/29466692/) | 2018 | Review | Discovery Medicine | Clinical update on anti-PD-1 antibodies as monotherapy or combined with ipilimumab in advanced melanoma |
| [40236344](https://pubmed.ncbi.nlm.nih.gov/40236344/) | 2025 | Case Report | Cureus | Case of metastatic melanoma with colonic involvement, treated with immunotherapy; highlights GI immune-related adverse event risk |

---

## Norway Market Information

Ipilimumab is **not currently marketed** in this jurisdiction (0 authorizations on file). No local license records or approved indication text are available for extraction.

---

## Cytotoxicity

Melanoma is a malignant neoplasm, and ipilimumab is an anticancer immune checkpoint inhibitor; this section is included per the antineoplastic-drug criteria.

| Item | Content |
|------|------|
| Cytotoxicity Classification | Immunotherapy (anti-CTLA-4 immune checkpoint inhibitor) |
| Myelosuppression Risk | Please refer to the package insert warnings and precautions |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | Please refer to the package insert warnings and precautions |
| Handling Protection | Please refer to the package insert warnings and precautions |

*Note: Unlike conventional cytotoxic chemotherapy, checkpoint inhibitors are primarily associated with immune-related adverse events (e.g., colitis, hepatitis, dermatitis, endocrinopathies) rather than myelosuppression — but no drug-specific toxicity data were present in this evidence pack, so specific claims are deferred to the package insert.*

---

## Safety Considerations

Please refer to the package insert for safety information. No warnings, contraindications, or drug-interaction data were available in this evidence pack — this is flagged as a **Blocking** data gap (DG001: TFDA/local label warnings and contraindications) that must be resolved before this candidate can proceed to safety evaluation (S1).

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Multiple completed Phase 2 trials provide direct evidence for ipilimumab activity in non-cutaneous melanoma subtypes (uveal, mucosal, leptomeningeal-metastatic), and the mechanism — non-genotype-specific immune activation — is plausibly generalizable across melanoma subtypes. However, response rates in uveal and mucosal disease are historically lower than in cutaneous melanoma, and the drug is not currently marketed in this jurisdiction, so evidence is sufficient to advance cautiously but not for an unconditional Go.

**To proceed, the following is needed:**
- Local label safety data (TFDA/regulatory warnings, contraindications) — currently a **Blocking** gap (DG001)
- Structured mechanism-of-action documentation from DrugBank (DG002)
- Subtype-stratified efficacy data (uveal vs. mucosal vs. acral response rates) to size expected benefit
- Route/formulation compatibility assessment (currently pending in evidence pack)
- Market entry/registration pathway assessment, since the drug currently holds zero local authorizations
- Exclude choroideremia from further development given absence of mechanistic plausibility and supporting evidence
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

