---
layout: default
title: Kun modellprediksjon (L5)
nav_order: 23
permalink: /evidence-low/
description: "L5-kandidater i NOTxGNN: kun modellprediksjon, uten klinisk evidens eller litteraturevidens så langt."
---

# Kun modellprediksjon (L5)

<p style="font-size: 1.25rem; color: #666; margin-bottom: 1.5rem;">
Kandidater med kun modellprediksjon og uten evidens fra mennesker så langt
</p>

---

## Kriterier

| Nivå | Definisjon | Klinisk betydning |
|-------|------------|------------------|
| **L5** | Kun modellprediksjon | Hypotesestadiet; ingen human evidens ennå |

---

{% assign l5_drugs = site.drugs | where: "evidence_level", "L5" | sort: "title" %}

### L5 ({{ l5_drugs.size }} legemidler)

| Legemiddel | Indikasjoner | Lenke |
|---------|---------|------|
{% for drug in l5_drugs %}| **{{ drug.title }}** | {{ drug.indication_count }} | [Se rapport]({{ drug.url | relative_url }}) |
{% endfor %}

---

<div class="disclaimer">
<strong>Ansvarsfraskrivelse</strong><br>
Denne rapporten er kun ment som referanse for akademisk forskning og <strong>utgjør ikke medisinske råd</strong>. Følg alltid legens anvisninger; juster aldri medisineringen på egen hånd. Enhver beslutning om legemiddelreposisjonering krever fullstendig klinisk validering og regulatorisk gjennomgang.
<br><br>
<small>Gjennomgått av: 藥提醒科技有限公司 (yao.care)</small>
</div>
