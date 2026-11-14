---
layout: default
title: Brukerveiledning
nav_order: 92
permalink: /guide/
description: "Brukerveiledning for NOTxGNN: hvordan du slår opp legemidler, leser evidensnivåer og tolker anbefalinger."
---

# Brukerveiledning

<div class="key-takeaway">
Sjekk evidensnivået først, deretter anbefalingen, og les så kildelitteraturen.
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

## Slå opp et legemiddel

<ol class="actionable-steps">
<li>Bruk søkefeltet øverst på siden (generiske navn på virkestoff gir bedre treff enn merkenavn).</li>
<li>Eller bla gjennom hele listen på <a href="{{ '/drugs/' | relative_url }}">Alle legemidler</a>.</li>
<li>Du kan også bla etter evidensnivå: <a href="{{ '/evidence-high/' | relative_url }}">høy</a>, <a href="{{ '/evidence-medium/' | relative_url }}">moderat</a>, <a href="{{ '/evidence-low/' | relative_url }}">kun modellprediksjon</a>.</li>
</ol>

---

## Lese en rapport

<p class="key-answer" data-question="Hva betyr evidensnivåene L1 til L5?">
Hver legemiddelrapport lister opp predikerte nye indikasjoner, og hver indikasjon har et
evidensnivå fra L1 til L5. <strong>L1 betyr at flere randomiserte kontrollerte studier i fase 3
allerede støtter den; L5 betyr kun modellprediksjon, uten evidens fra mennesker.</strong>
Fullstendige kriterier finner du på siden
<a href="{{ '/methodology/' | relative_url }}">Metodikk</a>.
</p>

| Hvis du ser | Det betyr | Foreslått handling |
|-----------|----------|------------------|
| L1 / L2 | Det finnes evidens fra kliniske studier | Gjennomgå kilde-oppføringene NCT og PMID |
| L3 / L4 | Observasjonell eller preklinisk evidens | Behandle som et forskningsspor |
| L5 | Kun modellprediksjon | Kun for å generere hypoteser; ikke til klinisk referanse |

---

## Sitering og sporbarhet

Hvert enkelt evidenselement i en rapport har en sporbar identifikator:

- **NCT-nummer**: lenker til registreringen på ClinicalTrials.gov
- **PMID**: lenker til oppføringen i PubMed
- **DrugBank-ID**: lenker til data om legemiddel og målmolekyl

Les kildelitteraturen for å bekrefte konteksten før du siterer noen konklusjon fra denne plattformen.

---

## Ofte stilte spørsmål

<p class="key-answer" data-question="Kan prediksjonene brukes klinisk?">
<strong>Nei.</strong> Prediksjonene på denne plattformen er forskningsspor, ikke kliniske råd.
Enhver klinisk anvendelse av legemiddelreposisjonering må gjennom fullstendig validering i
kliniske studier og regulatorisk gjennomgang.
</p>

<p class="key-answer" data-question="Hvorfor finner jeg ikke et bestemt legemiddel?">
Et virkestoff må kunne kobles mot DrugBank-vokabularet for å bli inkludert i prediksjonen.
Plantebaserte ekstrakter, vaksiner, hjelpestoffer og andre oppføringer som ikke er katalogisert av
DrugBank, vises ikke på denne plattformen.
</p>

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
