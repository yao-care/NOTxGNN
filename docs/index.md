---
layout: default
title: "Prediksjoner for Legemiddelreposisjonering \u2014 Norge"
nav_order: 1
description: "KI-baserte prediksjoner for ny bruk av legemidler i Norge. Evidensbasert analyse av godkjente legemidler for mulige nye bruksområder."
permalink: /
---

# Prediksjoner for ny bruk av legemidler — Norge

Dette prosjektet bruker TxGNN, et grafnevralt nettverk, til å predikere mulige nye terapeutiske bruksområder for legemidler som er godkjent i Norge.

**Ansvarsfraskrivelse**: Dette innholdet er kun ment for forskningsformål og utgjør ikke medisinske råd. Alle prediksjoner om legemiddelreposisjonering krever klinisk validering før bruk.

---

<!-- local-home:start（母目錄 .claude/gen_local_home_20261029.py 產生，勿手改）-->
## Norge: hva dette nettstedet dekker

Dette nettstedet publiserer rapporter om **{{ site.data.drug_stats.total_drugs }}** legemidler med sentral markedsføringstillatelse i EU fra [EMA Medicines report](https://www.ema.europa.eu/en/documents/report/medicines-output-medicines-report_en.xlsx) (gjelder også i Norge).

Datasett: [EMA Medicines report](https://www.ema.europa.eu/en/documents/report/medicines-output-medicines-report_en.xlsx); lastes ned og sammenlignes automatisk hver uke (mandager). Detaljer: [Datakilder]({{ '/sources/' | relative_url }}).

Rapporter etter evidensnivå:

| Evidensnivå | Rapporter | Andel |
|---|---|---|
| L1 | {{ site.data.drug_stats.level_counts.L1 }} | {{ site.data.drug_stats.level_counts.L1 | times: 100.0 | divided_by: site.data.drug_stats.total_drugs | round: 1 }}% |
| L2 | {{ site.data.drug_stats.level_counts.L2 }} | {{ site.data.drug_stats.level_counts.L2 | times: 100.0 | divided_by: site.data.drug_stats.total_drugs | round: 1 }}% |
| L3 | {{ site.data.drug_stats.level_counts.L3 }} | {{ site.data.drug_stats.level_counts.L3 | times: 100.0 | divided_by: site.data.drug_stats.total_drugs | round: 1 }}% |
| L4 | {{ site.data.drug_stats.level_counts.L4 }} | {{ site.data.drug_stats.level_counts.L4 | times: 100.0 | divided_by: site.data.drug_stats.total_drugs | round: 1 }}% |
| L5 | {{ site.data.drug_stats.level_counts.L5 }} | {{ site.data.drug_stats.level_counts.L5 | times: 100.0 | divided_by: site.data.drug_stats.total_drugs | round: 1 }}% |
{% assign na = site.data.drug_stats.total_drugs | minus: site.data.drug_stats.level_counts.L1 | minus: site.data.drug_stats.level_counts.L2 | minus: site.data.drug_stats.level_counts.L3 | minus: site.data.drug_stats.level_counts.L4 | minus: site.data.drug_stats.level_counts.L5 %}{% if na > 0 %}| N/A | {{ na }} | {{ na | times: 100.0 | divided_by: site.data.drug_stats.total_drugs | round: 1 }}% |{% endif %}

### Legemidler med høyest evidensnivå på dette nettstedet

| Legemiddel | Evidensnivå |
|---|---|
| [Bupropion](/drugs/bupropion/) | L1 |
| [Nepafenac](/drugs/nepafenac/) | L1 |
| [Peginterferon Alfa-2A](/drugs/peginterferon-alfa-2a/) | L1 |
| [Clofarabine](/drugs/clofarabine/) | L1 |
| [Doxorubicin](/drugs/doxorubicin/) | L1 |
| [Ketorolac](/drugs/ketorolac/) | L1 |
| [Tacrolimus](/drugs/tacrolimus/) | L1 |
| [Busulfan](/drugs/busulfan/) | L2 |
| [Ledipasvir](/drugs/ledipasvir/) | L2 |
| [Mycophenolate Mofetil](/drugs/mycophenolate-mofetil/) | L2 |

<!-- local-home:end -->

## Om utvikleren

Denne plattformen er utviklet og drives av **藥提醒科技有限公司** (yao.care). Opplysninger om selskapet,
bakgrunnen for TxGNN-modellen og alle nettstedene i produktlinjen finner du på siden <a href="{{ '/about/' | relative_url }}">Om</a>.
