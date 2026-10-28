---
layout: default
title: "Kun kjente bruksområder (ingen nye prediksjoner)"
nav_order: 24
permalink: /known-uses/
description: "For disse legemidlene er alle kandidatene fra TxGNN-modellen allerede kjente bruksområder (registrert i kunnskapsgrafen eller i en markedsføringstillatelse…"
---

# Kun kjente bruksområder (ingen nye prediksjoner)

For disse legemidlene er alle kandidatene fra TxGNN-modellen allerede kjente bruksområder (registrert i kunnskapsgrafen eller i en markedsføringstillatelse), så det finnes ingen ny predikert indikasjon. Hver side viser de kjente bruksområdene og lokal markedsstatus.

{% assign known_drugs = site.drugs | where: "evidence_level", "N/A" | sort: "title" %}

**{{ known_drugs.size }} legemidler**

| Legemiddel | Rapport |
|------|------|
{% for drug in known_drugs %}| **{{ drug.title }}** | [Se siden]({{ drug.url | relative_url }}) |
{% endfor %}
