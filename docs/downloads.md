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

<!-- site-data:start（母目錄 .claude/gen_page_data_20261116.py 產生，勿手改）-->
## Norge: data bak dette nettstedet

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

<!-- site-data:end -->

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
