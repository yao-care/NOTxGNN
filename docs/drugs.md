---
layout: default
title: Alle legemidler
nav_order: 20
permalink: /drugs/
description: "Alle valideringsrapporter for legemidler og statistikk over evidensnivåer i NOTxGNN."
---
{% assign l1_count = site.drugs | where: "evidence_level", "L1" | size %}
{% assign l2_count = site.drugs | where: "evidence_level", "L2" | size %}
{% assign l3_count = site.drugs | where: "evidence_level", "L3" | size %}
{% assign l4_count = site.drugs | where: "evidence_level", "L4" | size %}
{% assign l5_count = site.drugs | where: "evidence_level", "L5" | size %}

# Alle legemidler

{{ site.drugs.size }} valideringsrapporter for legemidler

---

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

{% assign all_drugs = site.drugs | sort: 'title' %}

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
