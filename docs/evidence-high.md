---
layout: default
title: Høy evidens (L1-L2)
nav_order: 21
permalink: /evidence-high/
description: "Kandidater for legemiddelreposisjonering på nivå L1-L2 i NOTxGNN, støttet av kliniske studier eller systematiske oversikter."
---

# Høy evidens (L1-L2)

<!-- page-data:start（母目錄 .claude/gen_page_data_20261116.py 產生，勿手改）-->
{% assign pd_m = site.data.drug_stats.level_counts.L1 | plus: site.data.drug_stats.level_counts.L2 %}
Siden viser **{{ pd_m }}** av de **{{ site.data.drug_stats.total_drugs }}** legemidlene med publisert rapport på dette nettstedet ({{ pd_m | times: 100.0 | divided_by: site.data.drug_stats.total_drugs | round: 1 }} %). Definisjon av nivåene: [Metodikk]({{ '/methodology/' | relative_url }}).
<!-- page-data:end -->

<p style="font-size: 1.25rem; color: #666; margin-bottom: 1.5rem;">
Kandidater som kan prioriteres for klinisk evaluering
</p>

Hvilke av disse legemidlene har studieevidens for den predikerte nye indikasjonen, og hvor mange registrerte studier siteres? Se [Legemidler i Norge med evidens fra kliniske studier for en ny indikasjon]({{ '/clinical-trial-evidence/' | relative_url }}).

---

## Kriterier

| Nivå | Definisjon | Klinisk betydning |
|-------|------------|------------------|
| **L1** | Flere fase 3-RCT-er / systematiske oversikter | Sterk støtte; klinisk bruk kan vurderes |
| **L2** | Én enkelt RCT eller flere fase 2-studier | Moderat støtte; valideringsstudier kan utformes |

---

{% assign l1_drugs = site.drugs | where: "evidence_level", "L1" | where_exp: "d", "d.noindex != true" | sort: "title" %}
{% assign l2_drugs = site.drugs | where: "evidence_level", "L2" | where_exp: "d", "d.noindex != true" | sort: "title" %}

### L1 ({{ l1_drugs.size }} legemidler)

| Legemiddel | Indikasjoner | Lenke |
|---------|---------|------|
{% for drug in l1_drugs %}| **{{ drug.title }}** | {{ drug.indication_count }} | [Se rapport]({{ drug.url | relative_url }}) |
{% endfor %}

### L2 ({{ l2_drugs.size }} legemidler)

| Legemiddel | Indikasjoner | Lenke |
|---------|---------|------|
{% for drug in l2_drugs %}| **{{ drug.title }}** | {{ drug.indication_count }} | [Se rapport]({{ drug.url | relative_url }}) |
{% endfor %}

---

<div class="disclaimer">
<strong>Ansvarsfraskrivelse</strong><br>
Denne rapporten er kun ment som referanse for akademisk forskning og <strong>utgjør ikke medisinske råd</strong>. Følg alltid legens anvisninger; juster aldri medisineringen på egen hånd. Enhver beslutning om legemiddelreposisjonering krever fullstendig klinisk validering og regulatorisk gjennomgang.
<br><br>
<small>Gjennomgått av: 藥提醒科技有限公司 (yao.care)</small>
</div>
