---
layout: default
title: Metodikk
nav_order: 91
permalink: /methodology/
description: "Slik utarbeider og validerer NOTxGNN sine prediksjoner: prediksjon med TxGNN-kunnskapsgraf, evidensinnsamling, gradering L1-L5 og beslutningsanbefalinger."
---

# Metodikk

<div class="key-takeaway">
Fra KI-prediksjon til evidensgradering — hver kandidat har et sporbart grunnlag for vurderingen sin.
</div>

---

## Samlet arbeidsflyt

<p class="key-answer" data-question="Hvordan utarbeider NOTxGNN sine prediksjoner?">
Plattformen bruker en arbeidsflyt i fire trinn: TxGNN-kunnskapsgrafmodellen predikerer potensielle
sammenhenger mellom legemiddel og sykdom, deretter samles det automatisk inn evidens for hvert
predikerte par, evidensen graderes fra L1 til L5, og til slutt gis en beslutningsanbefaling.
</p>

<ol class="actionable-steps">
<li><strong>TxGNN-prediksjon</strong>: relasjoner mellom legemiddel og sykdom predikeres med en kunnskapsgraf kombinert med grafnevrale nettverk.</li>
<li><strong>Evidensinnsamling</strong>: for hvert predikerte par hentes evidens fra ClinicalTrials.gov, PubMed, DrugBank og DMP.</li>
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

## Prediksjon med dobbel motor

To metoder kjører parallelt, og en konfidensmerkelapp registrerer om de er enige:

| Metode | Hastighet | Presisjon | Beskrivelse |
|--------|-------|-----------|-------------|
| Kunnskapsgraf (KG) | Rask | Lavere | Slutninger basert på DrugBank-relasjoner og grafstruktur |
| Dyp læring (DL) | Langsom | Høyere | TxGNN grafnevralt nettverk |

| Konfidens | Kilde | Betydning |
|------------|--------|---------|
| very_high | KG + DL | Begge metodene er enige |
| high | Kun DL | Støtte fra dyp læring med høy skår |
| medium | Kun KG | Støtte fra kunnskapsgraf |

---

## Integrasjon av regulatoriske data

Data om legemiddelgodkjenning i Norge kommer fra DMP. Navn på virkestoffer kobles mot
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

Denne plattformen er utviklet og drives av **藥提醒科技有限公司** (yao.care, organisasjonsnummer
83620786, 12F, No. 220, Sec. 2, Taiwan Blvd., West Dist., Taichung City, Taiwan).

NOTxGNN er Norge-nettstedet i selskapets produktlinje «TxGNN Drug Repurposing».
Det samme systemet er satt i drift i 30 land og regioner, hvert med navnet `{CC}TxGNN`
(JpTxGNN, UsTxGNN, DETxGNN og så videre) på `{cc}txgnn.yao.care`.
Produktoversikt: <https://www.yao.care/medical/txgnn/>.

Selve TxGNN-modellen ble utviklet av Zitnik Lab ved Harvard Medical School og publisert
i *Nature Medicine*. Denne plattformen er produksjonssystemet som 藥提醒科技有限公司 har bygget oppå
den modellen, og omfatter integrasjon av nasjonale legemiddelregistreringsdata, dobbel prediksjon
med kunnskapsgraf og dyp læring, evidensgradering fra PubMed / ClinicalTrials samt integrasjon mot
elektronisk pasientjournal via SMART on FHIR.

---

<div class="disclaimer">
<strong>Ansvarsfraskrivelse</strong><br>
Denne rapporten er kun ment som referanse for akademisk forskning og <strong>utgjør ikke medisinske råd</strong>. Følg alltid legens anvisninger; juster aldri medisineringen på egen hånd. Enhver beslutning om legemiddelreposisjonering krever fullstendig klinisk validering og regulatorisk gjennomgang.
<br><br>
<small>Gjennomgått av: 藥提醒科技有限公司 (yao.care)</small>
</div>
