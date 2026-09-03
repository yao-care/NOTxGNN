---
layout: default
title: Pegaspargase
parent: 僅模型預測 (L5)
nav_order: 268
evidence_level: L5
indication_count: 10
---

# Pegaspargase
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

# Pegaspargase: From Acute Lymphoblastic Leukemia to Precursor Lymphoblastic Lymphoma/Leukemia

## One-Sentence Summary

Pegaspargase is a PEGylated form of *E. coli* L-asparaginase used as a cornerstone agent in the treatment of acute lymphoblastic leukemia (ALL). The TxGNN model's top prediction, **precursor lymphoblastic lymphoma/leukemia**, sits within the same disease spectrum the drug already treats — this is not a novel repurposing hypothesis but a confirmation of established standard-of-care, backed by **50 clinical trials** and **20 publications** in the evidence pack.

> ⚠️ **Important caveat**: Unlike a typical repurposing candidate, this predicted indication overlaps substantially with pegaspargase's known/approved use. The evidence pack's own rationale explicitly flags this as "an extension of an already-established treatment, not a novel repurposing hypothesis." The report below is presented for completeness and regulatory-status tracking, not as a discovery signal.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Acute lymphoblastic leukemia (ALL) — pegaspargase's established indication, per mechanistic/rationale data in the evidence pack (no Norway license record exists, as the drug is not locally marketed) |
| Predicted New Indication | Precursor Lymphoblastic Lymphoma/Leukemia |
| TxGNN Prediction Score | 99.96% |
| Evidence Level | L1 |
| Norway Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Pegaspargase depletes serum asparagine by hydrolyzing it into aspartic acid and ammonia. Lymphoblasts characteristically lack (or have very low) asparagine synthetase, meaning they cannot synthesize their own asparagine and depend entirely on the extracellular pool — depletion by pegaspargase is therefore selectively lethal to these cells while sparing most normal tissues, which retain synthetase activity. This is a well-established, decades-old mechanism, not a newly inferred one.

"Precursor lymphoblastic lymphoma/leukemia" and "acute lymphoblastic leukemia" describe overlapping points on the same disease continuum (WHO classification treats ALL and lymphoblastic lymphoma as the same neoplasm presenting either in blood/marrow or as a nodal/extranodal mass). Because pegaspargase's antineoplastic mechanism targets the shared metabolic vulnerability of lymphoblasts regardless of presentation (leukemic vs. lymphomatous), the TxGNN prediction is mechanistically sound — but it largely reflects confirmation of existing practice rather than a new therapeutic hypothesis.

Detailed formal MOA documentation (DrugBank `original_moa` field) was not available in this evidence pack; the mechanistic description above is derived from the model's own repurposing rationale rather than a structured DrugBank entry, and should be independently verified before use in regulatory submissions.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT02013167](https://clinicaltrials.gov/study/NCT02013167) | Phase 3 | Terminated | 405 | Blinatumomab vs. standard-of-care chemotherapy (pegaspargase-containing backbone) in relapsed/refractory B-precursor ALL (TOWER study) |
| [NCT00103285](https://clinicaltrials.gov/study/NCT00103285) | Phase 3 | Completed | 5,377 | Large randomized comparison of combination chemotherapy regimens in newly diagnosed standard-risk B-precursor ALL |
| [NCT00022737](https://clinicaltrials.gov/study/NCT00022737) | Phase 3 | Completed | 220 | COG pilot study of combination chemotherapy ± donor stem cell transplant in very high-risk pediatric ALL |
| [NCT03643276](https://clinicaltrials.gov/study/NCT03643276) | Phase 3 | Recruiting | 5,000 | AIEOP-BFM ALL 2017 international collaborative protocol for children/adolescents with ALL |
| [NCT00005945](https://clinicaltrials.gov/study/NCT00005945) | Phase 3 | Completed | 3,054 | Escalating-dose IV methotrexate vs. oral methotrexate and intensification strategies in standard-risk pediatric ALL |
| [NCT03959085](https://clinicaltrials.gov/study/NCT03959085) | Phase 3 | Recruiting | 5,951 | Inotuzumab ozogamicin added to post-induction chemo-immunotherapy for high-risk B-ALL |
| [NCT02881086](https://clinicaltrials.gov/study/NCT02881086) | Phase 3 | Completed | 1,023 | Pediatric-inspired, MRD-directed therapy incl. nelarabine consolidation in adult ALL/lymphoblastic lymphoma |
| [NCT05602194](https://clinicaltrials.gov/study/NCT05602194) | Phase 3 | Recruiting | 440 | Levocarnitine prophylaxis against asparaginase-associated hepatotoxicity in AYA ALL/LL patients |
| [NCT06195735](https://clinicaltrials.gov/study/NCT06195735) | N/A | Completed | 649 | Forecasting hypersensitivity to PEG-asparaginase to optimize ALL treatment outcomes |
| [NCT00671034](https://clinicaltrials.gov/study/NCT00671034) | Phase 3 | Completed | 166 | Calaspargase pegol vs. pegaspargase pilot RCT in newly diagnosed high-risk ALL |

*40 additional trials were identified in the evidence pack but are omitted here for brevity (full list available in the raw Evidence Pack).*

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [37276451](https://pubmed.ncbi.nlm.nih.gov/37276451/) | 2023 | Cohort | Blood Advances | GIMEMA LAL1913: pegaspargase-modified, risk-oriented program improves outcomes in adult Ph-negative ALL/LL |
| [34228505](https://pubmed.ncbi.nlm.nih.gov/34228505/) | 2021 | Cohort | J Clin Oncol | DFCI 11-001: efficacy/toxicity comparison of pegaspargase vs. calaspargase pegol in childhood ALL |
| [35271306](https://pubmed.ncbi.nlm.nih.gov/35271306/) | 2022 | Phase 3 RCT | J Clin Oncol | COG AALL1231: bortezomib added to therapy in newly diagnosed T-ALL/T-LL |
| [39322712](https://pubmed.ncbi.nlm.nih.gov/39322712/) | 2024 | Phase 2 | Leukemia | Long-term follow-up: venetoclax + hyper-CVAD/nelarabine/pegylated asparaginase in T-ALL/LBL |
| [40109190](https://pubmed.ncbi.nlm.nih.gov/40109190/) | 2025 | Review | Haematologica | Expert panel consensus on recognition/prevention/management of asparaginase-related adverse events in adults |
| [27114587](https://pubmed.ncbi.nlm.nih.gov/27114587/) | 2016 | Phase 3 RCT | J Clin Oncol | COG AALL0232: dexamethasone + high-dose methotrexate improve outcomes in high-risk B-ALL |
| [32813610](https://pubmed.ncbi.nlm.nih.gov/32813610/) | 2020 | Phase 3 RCT | J Clin Oncol | COG AALL0434: nelarabine tested in newly diagnosed T-cell ALL |
| [17696798](https://pubmed.ncbi.nlm.nih.gov/17696798/) | 2007 | Review | Expert Opin Pharmacother | Foundational review of PEG-asparaginase pharmacology and clinical role |
| [40163215](https://pubmed.ncbi.nlm.nih.gov/40163215/) | 2025 | Phase 2 | Int J Hematol | Multicenter study of lyophilized pegaspargase efficacy/safety/PK in Japanese ALL patients |
| [35987855](https://pubmed.ncbi.nlm.nih.gov/35987855/) | 2022 | Review | Bulletin du Cancer | French Society of Children/Adolescent Cancers recommendations on managing pegaspargase-associated toxicities |

*10 additional publications were identified in the evidence pack but are omitted here for brevity.*

---

## Norway Market Information

No authorizations are currently registered for pegaspargase in Norway (market status: **Not Marketed**, total licenses: 0). If clinical use is pursued, access would require a named-patient/exemption import route or a new marketing authorization application, rather than reliance on an existing local license.

---

## Cytotoxicity

Pegaspargase is an antineoplastic biologic enzyme (L-asparaginase class) used exclusively in cytotoxic chemotherapy regimens for lymphoid malignancies; its original indication (ALL) and mechanism (selective cytotoxicity via asparagine depletion) both meet the criteria for this section.

| Item | Content |
|------|------|
| Cytotoxicity Classification | Conventional cytotoxic — enzyme-based antimetabolic agent (asparaginase class), distinct in mechanism from DNA-damaging cytotoxics |
| Myelosuppression Risk | Not directly characterized in the available evidence; pegaspargase is generally considered less myelosuppressive on its own than classic cytotoxics, but it is invariably administered within multi-agent regimens where overall myelosuppression is driven by co-administered drugs (per trial NCT01193933, dosing is modified based on combined regimen myelosuppression severity) |
| Emetogenicity Classification | Low to moderate (consistent with the asparaginase drug class) |
| Monitoring Items | Liver function (hepatotoxicity — PMID 34528411, 40109190), pancreatic enzymes/pancreatitis (PMID 10696127), coagulation parameters (thrombosis/hemostasis — NCT01094392), triglycerides and glucose (PMID 30823860, 34931744), and hypersensitivity monitoring (PMID 31571395, NCT06195735) |
| Handling Protection | Must be handled under standard cytotoxic/antineoplastic drug handling precautions |

---

## Safety Considerations

Please refer to the package insert for safety information. No structured key warnings, contraindications, or drug–drug interaction data were available in this evidence pack (DDI query returned no results).

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The mechanistic and clinical trial evidence (L1, 50 trials including large Phase 3 RCTs) is strong, but this is fundamentally confirmatory evidence for pegaspargase's already-established role in ALL/lymphoblastic lymphoma rather than a genuine repurposing discovery. Combined with the drug's current unmarketed status in Norway and a blocking data gap on local product labeling, this candidate should proceed only under guardrails — not as a novel indication launch.

**To proceed, the following is needed:**
- TFDA/Norway-equivalent package insert warnings and contraindications (currently a **Blocking** data gap — DG001)
- Formal DrugBank-sourced mechanism of action documentation (currently a **High**-severity data gap — DG002)
- Confirmation of regulatory pathway for Norway market access (named-patient import vs. new MA application), given zero current authorizations
- Clarification with clinical/regulatory stakeholders that this candidate represents confirmation of existing use, not a new repurposing opportunity, before including it in any repurposing-focused decision packet
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

