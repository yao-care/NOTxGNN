---
layout: default
title: "Prediksjoner for Legemiddelreposisjonering \u2014 Norge"
nav_order: 1
description: "KI-baserte prediksjoner for ny bruk av legemidler i Norge. Evidensbasert analyse av godkjente legemidler for mulige nye bruksområder."
permalink: /
---

# Prediksjoner for ny bruk av legemidler — Norge

This project uses the TxGNN graph neural network to predict potential new therapeutic uses for medicines approved in Norway.

**Disclaimer**: This content is for research purposes only and does not constitute medical advice. All drug repurposing predictions require clinical validation before application.

---

<!-- local-home:start（母目錄 .claude/gen_local_home_20261029.py 產生，勿手改）-->
## Norge: hva dette nettstedet dekker

Dette nettstedet publiserer rapporter om **{{ site.data.drug_stats.total_drugs }}** legemidler fra registreringsdataene til [DMP](https://www.dmp.no/) (Norge).

Rapporter etter evidensnivå: L1 {{ site.data.drug_stats.level_counts.L1 }} · L2 {{ site.data.drug_stats.level_counts.L2 }} · L3 {{ site.data.drug_stats.level_counts.L3 }} · L4 {{ site.data.drug_stats.level_counts.L4 }} · L5 {{ site.data.drug_stats.level_counts.L5 }}

### Legemidler med høyest evidensnivå på dette nettstedet

| Legemiddel | Evidensnivå |
|---|---|
| [Bupropion](/drugs/bupropion/) | L1 |
| [Lanadelumab](/drugs/lanadelumab/) | L1 |
| [Nepafenac](/drugs/nepafenac/) | L1 |
| [Oteracil](/drugs/oteracil/) | L1 |
| [Solriamfetol](/drugs/solriamfetol/) | L1 |
| [Tegafur](/drugs/tegafur/) | L1 |
| [Hydrocortisone](/drugs/hydrocortisone/) | L1 |
| [Peginterferon Alfa-2A](/drugs/peginterferon-alfa-2a/) | L1 |
| [Clofarabine](/drugs/clofarabine/) | L1 |
| [Doxorubicin](/drugs/doxorubicin/) | L1 |

<!-- local-home:end -->

## Om utvikleren

Denne plattformen er utviklet og drives av **藥提醒科技有限公司** (yao.care, organisasjonsnummer
83620786, 12F, No. 220, Sec. 2, Taiwan Blvd., West Dist., Taichung City, Taiwan).

NOTxGNN er Norge-nettstedet i selskapets produktlinje «TxGNN Drug Repurposing».
Det samme systemet er satt i drift i 30 land og regioner, hvert med navnet `{CC}TxGNN`
(JpTxGNN, UsTxGNN, DETxGNN og så videre) på `{cc}txgnn.yao.care`.
Produktoversikt: <https://www.yao.care/medical/txgnn/>.

Selve TxGNN-modellen ble utviklet av Zitnik Lab ved Harvard Medical School og publisert
i *Nature Medicine*. Denne plattformen er produksjonssystemet som 藥提醒科技有限公司 har bygget oppå
den modellen, og omfatter integrasjon av nasjonale legemiddelregistreringsdata, prediksjon med dyp læring der bruk som allerede er registrert i kunnskapsgrafen, er utelatt, evidensgradering fra PubMed / ClinicalTrials samt integrasjon mot
elektronisk pasientjournal via SMART on FHIR.
