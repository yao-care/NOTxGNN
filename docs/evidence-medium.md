---
layout: default
title: Moderat evidens (L3-L4)
nav_order: 22
permalink: /evidence-medium/
description: "Kandidater for legemiddelreposisjonering på nivå L3-L4 i NOTxGNN, understøttet av observasjonelle eller prekliniske data."
---

# Moderat evidens (L3-L4)

<p style="font-size: 1.25rem; color: #666; margin-bottom: 1.5rem;">
Kandidater med foreløpig evidens som krever ytterligere validering
</p>

---

## Kriterier

| Nivå | Definisjon | Klinisk betydning |
|-------|------------|------------------|
| **L3** | Observasjonsstudier / store kasusserier | Foreløpig støtte; krever ytterligere validering |
| **L4** | Prekliniske / mekanistiske studier | Teoretisk støtte; langt fra klinisk bruk |

---

{% assign l3_drugs = site.drugs | where: "evidence_level", "L3" | sort: "title" %}
{% assign l4_drugs = site.drugs | where: "evidence_level", "L4" | sort: "title" %}

### L3 ({{ l3_drugs.size }} legemidler)

| Legemiddel | Indikasjoner | Lenke |
|---------|---------|------|
{% for drug in l3_drugs %}| **{{ drug.title }}** | {{ drug.indication_count }} | [Se rapport]({{ drug.url | relative_url }}) |
{% endfor %}

### L4 ({{ l4_drugs.size }} legemidler)

| Legemiddel | Indikasjoner | Lenke |
|---------|---------|------|
{% for drug in l4_drugs %}| **{{ drug.title }}** | {{ drug.indication_count }} | [Se rapport]({{ drug.url | relative_url }}) |
{% endfor %}

---

<div class="disclaimer">
<strong>Ansvarsfraskrivelse</strong><br>
Denne rapporten er kun ment som referanse for akademisk forskning og <strong>utgjør ikke medisinske råd</strong>. Følg alltid legens anvisninger; juster aldri medisineringen på egen hånd. Enhver beslutning om legemiddelreposisjonering krever fullstendig klinisk validering og regulatorisk gjennomgang.
<br><br>
<small>Gjennomgått av: 藥提醒科技有限公司 (yao.care)</small>
</div>
