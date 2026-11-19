---
layout: default
title: Metodikk
nav_order: 91
permalink: /methodology/
description: "Slik utarbeider og validerer NOTxGNN sine prediksjoner: prediksjon med TxGNN-modellen (dyp læring), evidensinnsamling, gradering L1-L5 og beslutningsanbefalinger."
---

# Metodikk

<div class="key-takeaway">
Fra KI-prediksjon til evidensgradering — hver kandidat har et sporbart grunnlag for vurderingen sin.
</div>

---

<!-- local-facts:start（母目錄 .claude/gen_local_pages_20261119.py 產生，勿手改）-->
## Norge: slik brukes metoden på dette nettstedet

Lokale data: [EMA Medicines report](https://www.ema.europa.eu/en/documents/report/medicines-output-medicines-report_en.xlsx). De lokale dataene er sentrale markedsføringstillatelser i EU fra EMA Medicines report, som også gjelder i Norge. Nasjonale markedsføringstillatelser (DMP) finnes ikke i disse dataene.

| Nivå | Rapporter | …med gyldige lokal oppføring |
|---|---|---|
| L1 | {{ site.data.local_facts.by_level.L1.n }} | {{ site.data.local_facts.by_level.L1.current }} |
| L2 | {{ site.data.local_facts.by_level.L2.n }} | {{ site.data.local_facts.by_level.L2.current }} |
| L3 | {{ site.data.local_facts.by_level.L3.n }} | {{ site.data.local_facts.by_level.L3.current }} |
| L4 | {{ site.data.local_facts.by_level.L4.n }} | {{ site.data.local_facts.by_level.L4.current }} |
| L5 | {{ site.data.local_facts.by_level.L5.n }} | {{ site.data.local_facts.by_level.L5.current }} |

Kontrolloggen har **{{ site.data.local_facts.reviews.records }}** oppføringer på **{{ site.data.local_facts.reviews.public_pages_with_records }}** legemiddelsider; rettelser endrer bare godkjenningsopplysninger, aldri modellens prediksjoner.

<!-- local-facts:end -->

## Samlet arbeidsflyt

<p class="key-answer" data-question="Hvordan utarbeider NOTxGNN sine prediksjoner?">
Plattformen bruker en arbeidsflyt i fire trinn: TxGNN-modellen (dyp læring) predikerer potensielle
sammenhenger mellom legemiddel og sykdom, deretter samles det automatisk inn evidens for hvert
predikerte par, evidensen graderes fra L1 til L5, og til slutt gis en beslutningsanbefaling.
</p>

<ol class="actionable-steps">
<li><strong>TxGNN-prediksjon</strong>: relasjoner mellom legemiddel og sykdom predikeres av TxGNN-modellen (dyp læring: et grafnevralt nettverk trent på en biomedisinsk kunnskapsgraf).</li>
<li><strong>Evidensinnsamling</strong>: for hvert predikerte par hentes evidens fra ClinicalTrials.gov, PubMed, DrugBank og EMAs Medicines report.</li>
<li><strong>Evidensgradering</strong>: gradert fra L1 til L5, der L1 er sterkest (flere fase 3-RCT-er) og L5 kun er en modellprediksjon.</li>
<li><strong>Beslutningsanbefaling</strong>: Go, Proceed, Consider, Explore eller Hold, basert på evidensnivået.</li>
</ol>

---

## Kriterier for evidensgradering

<table class="comparison-table">
<thead>
<tr><th>Nivå</th><th>Definisjon</th><th>Klinisk betydning</th></tr>
</thead>
<tbody>
<tr><td><strong>L1</strong></td><td>Flere fase 3-RCT-er / systematiske oversikter</td><td>Sterk støtte; klinisk bruk kan vurderes</td></tr>
<tr><td><strong>L2</strong></td><td>Én enkelt RCT eller flere fase 2-studier</td><td>Moderat støtte; valideringsstudier kan utformes</td></tr>
<tr><td><strong>L3</strong></td><td>Observasjonsstudier / store kasusserier</td><td>Foreløpig støtte; krever ytterligere validering</td></tr>
<tr><td><strong>L4</strong></td><td>Prekliniske / mekanistiske studier</td><td>Teoretisk støtte; langt fra klinisk bruk</td></tr>
<tr><td><strong>L5</strong></td><td>Kun modellprediksjon</td><td>Hypotesestadiet; ingen human evidens ennå</td></tr>
</tbody>
</table>

---

## Slik lages prediksjonene

TxGNNs dyplæringsmodell (DL) gir hvert legemiddel–sykdom-par en score. Deretter fjernes indikasjoner og kontraindikasjoner som allerede er registrert for legemidlet i TxGNNs kunnskapsgraf (KG), slik at legemiddelsidene bare viser nye predikerte indikasjoner med en score på minst 0,99 (opptil 10 per legemiddel).

| Trinn | Rolle |
|-------|-------|
| Dyplæring (DL) | TxGNNs grafbaserte nevrale nettverk gir hvert legemiddel–sykdom-par en score |
| Kontroll av kjent bruk (KG) | Fjerner indikasjoner og kontraindikasjoner som allerede er registrert i kunnskapsgrafen; de telles ikke som nye prediksjoner |
| Innsamling av evidens | Søker i ClinicalTrials.gov og PubMed for hver gjenværende prediksjon og gir et evidensnivå (L1–L5) |

---

## Integrasjon av regulatoriske data

Data om legemiddelgodkjenning kommer fra EMAs Medicines report (sentralt godkjente legemidler i EU, gyldig også i Norge). Navn på virkestoffer kobles mot
DrugBank-vokabularet; virkestoffer som ikke lar seg koble — plantebaserte ekstrakter, vaksiner,
hjelpestoffer og annet som ikke er katalogisert av DrugBank — utelates fra prediksjonen.

---

## Begrensninger

<ol class="actionable-steps">
<li>Prediksjoner er statistiske sammenhenger og <strong>innebærer ikke årsakssammenheng eller klinisk effekt</strong>.</li>
<li>Vurderingen L5 betyr kun modellprediksjon, uten støttende evidens fra mennesker.</li>
<li>Evidensinnsamlingen er avhengig av offentlige databaser; upubliserte eller uindekserte studier fanges ikke opp.</li>
<li>Kobling av virkestoffer kan gå glipp av oppføringer på grunn av forskjeller i navngivning.</li>
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
