---
layout: default
title: Nedlastinger
nav_order: 94
permalink: /downloads/
description: "Åpne data til nedlasting fra NOTxGNN: FHIR-ressurser, prediksjonsresultater og søkeindeks."
---

# Nedlastinger

<div class="key-takeaway">
Prediksjonene publiseres i FHIR R4-format, klare til å integreres med journalsystemer.
</div>

---

<!-- local-facts:start（母目錄 .claude/gen_local_pages_20261119.py 產生，勿手改）-->
## Norge: hva filene inneholder nå

| Fil | Innhold nå |
|---|---|
| `/data/search-index.json` | {{ site.data.local_facts.files.search_index }} legemidler med predikerte indikasjoner |
| `/data/drugs.json` | {{ site.data.local_facts.files.drugs_json }} legemidler med evidensnivå og opprinnelig indikasjon |
| `/fhir/MedicationKnowledge/` | {{ site.data.local_facts.fhir.medication_knowledge }} MedicationKnowledge-ressurser (én per legemiddel) |
| `/fhir/ClinicalUseDefinition/` | {{ site.data.local_facts.fhir.clinical_use_definition }} ClinicalUseDefinition-ressurser (én per predikert indikasjon) |

Gjenbruk av det lokale datasettet: [EMA Medicines report](https://www.ema.europa.eu/en/documents/report/medicines-output-medicines-report_en.xlsx), publisert av Det europeiske legemiddelkontoret (EMA); gjenbruk følger utgiverens vilkår, og dette nettstedet gir ingen ytterligere rettigheter.

{% if site.data.local_facts.top_licensed.size > 0 %}Legemidler med flest gyldige sentrale EU-godkjenninger (EMA): {% for r in site.data.local_facts.top_licensed limit: 5 offset: 3 %}[{{ r.t }}]({{ r.u | relative_url }}) ({{ r.lv }}){% unless forloop.last %}, {% endunless %}{% endfor %}{% endif %}

{% if site.data.local_facts.recent_reviews.size > 0 %}Siste rettelser i kontrolloggen: {% for r in site.data.local_facts.recent_reviews limit: 8 offset: 16 %}[{{ r.t }}]({{ r.u | relative_url }}) ({{ r.d }}): {{ r.s }}{% unless forloop.last %}; {% endunless %}{% endfor %}{% endif %}

<!-- local-facts:end -->

## FHIR-ressurser

Dette nettstedet publiserer prediksjoner som FHIR R4-ressurser, som kan brukes direkte av SMART on FHIR-apper:

| Ressurs | Sti | Beskrivelse |
|----------|------|-------------|
| CapabilityStatement | `/fhir/metadata` | Kapabilitetserklæring for FHIR-serveren |
| MedicationKnowledge | `/fhir/MedicationKnowledge/` | Legemiddelressurser |
| ClinicalUseDefinition | `/fhir/ClinicalUseDefinition/` | Predikerte indikasjoner |
| Bundle | `/fhir/Bundle/all-predictions.json` | Alle prediksjoner samlet |

---

## Søkeindeks

`/data/search-index.json` gir en søkeindeks over legemidler og indikasjoner, slik at du kan bygge
ditt eget grensesnitt for oppslag.

---

## Bruksvilkår

<ol class="actionable-steps">
<li>Dataene på dette nettstedet er <strong>kun ment som referanse for forskning</strong> og skal ikke brukes som grunnlag for medisinske beslutninger.</li>
<li>Ved sitering skal du kreditere NOTxGNN (藥提醒科技有限公司) og sitere den opprinnelige TxGNN-artikkelen.</li>
<li>Videre bruk av dataene er fortsatt underlagt lisensvilkårene til hver enkelt opprinnelige kilde (se <a href="{{ '/sources/' | relative_url }}">Datakilder</a>).</li>
</ol>

---

## Om utvikleren

Denne plattformen er utviklet og drives av **藥提醒科技有限公司** (yao.care). Opplysninger om selskapet,
bakgrunnen for TxGNN-modellen og alle nettstedene i produktlinjen finner du på siden <a href="{{ '/about/' | relative_url }}">Om</a>.

---

<div class="disclaimer">
<strong>Ansvarsfraskrivelse</strong><br>
Denne rapporten er kun ment som referanse for akademisk forskning og <strong>utgjør ikke medisinske råd</strong>. Følg alltid legens anvisninger; juster aldri medisineringen på egen hånd. Enhver beslutning om legemiddelreposisjonering krever fullstendig klinisk validering og regulatorisk gjennomgang.
<br><br>
<small>Gjennomgått av: 藥提醒科技有限公司 (yao.care)</small>
</div>
