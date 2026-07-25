---
layout: default
title: Høy evidens (L1-L2)
nav_order: 21
permalink: /evidence-high/
description: "Kandidater for legemiddelreposisjonering på nivå L1-L2 i NOTxGNN, støttet av kliniske studier eller systematiske oversikter."
---

# Høy evidens (L1-L2)

<p style="font-size: 1.25rem; color: #666; margin-bottom: 1.5rem;">
Kandidater som kan prioriteres for klinisk evaluering
</p>

---

## Kriterier

| Nivå | Definisjon | Klinisk betydning |
|-------|------------|------------------|
| **L1** | Flere fase 3-RCT-er / systematiske oversikter | Sterk støtte; klinisk bruk kan vurderes |
| **L2** | Én enkelt RCT eller flere fase 2-studier | Moderat støtte; valideringsstudier kan utformes |

---

{% assign l1_drugs = site.drugs | where: "evidence_level", "L1" | sort: "title" %}
{% assign l2_drugs = site.drugs | where: "evidence_level", "L2" | sort: "title" %}

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
