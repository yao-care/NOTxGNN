---
layout: default
title: Alle legemidler
nav_order: 20
permalink: /drugs/
description: "Alle valideringsrapporter for legemidler og statistikk over evidensnivåer i NOTxGNN."
---
{%- comment -%}2026-10-27 build gate：站上各頁的藥物數讀 site.data.drug_stats；它和實際公開藥物頁數／等級分布不一致時，
故意 include 不存在的檔讓 Jekyll 建置失敗，錯誤訊息即修法。{%- endcomment -%}
{%- assign gate_listed = site.drugs | where_exp: "d", "d.layout != 'id_redirect'" | where_exp: "d", "d.noindex != true" -%}
{%- assign gate_ds = site.data.drug_stats -%}
{%- assign gate_l1 = gate_listed | where: "evidence_level", "L1" | size -%}
{%- assign gate_l2 = gate_listed | where: "evidence_level", "L2" | size -%}
{%- assign gate_l3 = gate_listed | where: "evidence_level", "L3" | size -%}
{%- assign gate_l4 = gate_listed | where: "evidence_level", "L4" | size -%}
{%- assign gate_l5 = gate_listed | where: "evidence_level", "L5" | size -%}
{%- if gate_listed.size != gate_ds.total_drugs or gate_l1 != gate_ds.level_counts.L1 or gate_l2 != gate_ds.level_counts.L2 or gate_l3 != gate_ds.level_counts.L3 or gate_l4 != gate_ds.level_counts.L4 or gate_l5 != gate_ds.level_counts.L5 -%}
{% include ERROR-docs-data-drug_stats-json-out-of-sync--run-python3-scripts-generate_drug_stats-py.html %}
{%- endif %}
{%- comment -%}2026-10-16：列表不含舊 ID 轉址頁與 noindex 頁{%- endcomment -%}
{% assign listed_drugs = site.drugs | where_exp: "d", "d.layout != 'id_redirect'" | where_exp: "d", "d.noindex != true" %}
{% assign l1_count = listed_drugs | where: "evidence_level", "L1" | size %}
{% assign l2_count = listed_drugs | where: "evidence_level", "L2" | size %}
{% assign l3_count = listed_drugs | where: "evidence_level", "L3" | size %}
{% assign l4_count = listed_drugs | where: "evidence_level", "L4" | size %}
{% assign l5_count = listed_drugs | where: "evidence_level", "L5" | size %}

# Alle legemidler

{{ listed_drugs.size }} valideringsrapporter for legemidler

---

<!-- local-home:start（母目錄 .claude/gen_local_home_20261029.py 產生，勿手改）-->
Listen bygger på registreringsdataene til [DMP](https://www.dmp.no/) (Norge).

<!-- local-home:end -->

## Fordeling etter evidensnivå

| Evidensnivå | Legemidler | Beskrivelse |
|---------|--------|------|
| **L1** | {{ l1_count }} | Flere RCT-er / systematiske oversikter |
| **L2** | {{ l2_count }} | Én enkelt RCT / fase 2-studier |
| **L3** | {{ l3_count }} | Observasjonsstudier / store kasusserier |
| **L4** | {{ l4_count }} | Prekliniske / mekanistiske studier |
| **L5** | {{ l5_count }} | Kun modellprediksjon |

---

## Fullstendig legemiddelliste

{% assign all_drugs = listed_drugs | sort: 'title' %}

| Legemiddel | Evidensnivå | Indikasjoner |
|---------|---------|---------|
{% for drug in all_drugs %}| [{{ drug.title }}]({{ drug.url | relative_url }}) | {{ drug.evidence_level }} | {{ drug.indication_count }} |
{% endfor %}

---

<div class="disclaimer">
<strong>Ansvarsfraskrivelse</strong><br>
Denne rapporten er kun ment som referanse for akademisk forskning og <strong>utgjør ikke medisinske råd</strong>. Følg alltid legens anvisninger; juster aldri medisineringen på egen hånd. Enhver beslutning om legemiddelreposisjonering krever fullstendig klinisk validering og regulatorisk gjennomgang.
<br><br>
<small>Gjennomgått av: 藥提醒科技有限公司 (yao.care)</small>
</div>
