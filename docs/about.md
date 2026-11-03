---
layout: default
title: Om
nav_order: 90
permalink: /about/
description: "NOTxGNN er en plattform for prediksjon av legemiddelreposisjonering utviklet av 藥提醒科技有限公司 (yao.care), bygget på TxGNN-modellen fra Harvard og med dekning av legemidler med sentral markedsføringstillatelse i EU (EMA), som også gjelder i Norge."
---

# Om

<div class="key-takeaway">
Raskere evidensvalidering av legemiddelreposisjonering med KI — fra prediksjon til evidens med ett blikk.
</div>

---

## Bakgrunn

<p class="key-answer" data-question="Hva er NOTxGNN?">
<strong>NOTxGNN</strong> er en forskningsstøtteplattform for legemiddelreposisjonering, bygget på
TxGNN-modellen som ble publisert i <em>Nature Medicine</em> av Zitnik Lab ved Harvard University.
Den predikerer utvidelse av indikasjoner for legemidler med sentral markedsføringstillatelse i EU (EMA), som også gjelder i Norge. I tillegg til
KI-baserte prediksjonsskår integrerer plattformen klinisk evidens fra ClinicalTrials.gov og PubMed,
slik at forskere raskt kan vurdere hvor troverdig hver enkelt prediksjon er.
</p>

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
den modellen, og omfatter integrasjon av EMAs data om markedsføringstillatelser, prediksjon med dyp læring der bruk som allerede er registrert i kunnskapsgrafen, er utelatt, evidensgradering fra PubMed / ClinicalTrials samt integrasjon mot
elektronisk pasientjournal via SMART on FHIR.

---

## Hva er legemiddelreposisjonering?

<p class="key-answer" data-question="Hva er legemiddelreposisjonering?">
<strong>Legemiddelreposisjonering</strong> betyr å finne nye terapeutiske bruksområder for
eksisterende legemidler. Sammenlignet med å utvikle et nytt legemiddel fra bunnen av — 10 til
15 år og USD 1&ndash;2 milliarder — tar reposisjonering 3 til 5 år og USD 100&ndash;300 millioner,
og sikkerhetsdata fra mennesker finnes allerede, slik at risikoen for å mislykkes er lavere.
</p>

<table class="comparison-table">
<thead>
<tr><th>Aspekt</th><th>Utvikling av nytt legemiddel</th><th>Legemiddelreposisjonering</th></tr>
</thead>
<tbody>
<tr><td>Tid</td><td>10&ndash;15 år</td><td>3&ndash;5 år</td></tr>
<tr><td>Kostnad</td><td>USD 1&ndash;2 milliarder</td><td>USD 100&ndash;300 millioner</td></tr>
<tr><td>Sikkerhetsdata</td><td>Må etableres</td><td>Humane data finnes allerede</td></tr>
<tr><td>Risiko for å mislykkes</td><td>Svært høy (&gt;90 %)</td><td>Lavere</td></tr>
</tbody>
</table>

---

## Hva er TxGNN?

<p class="key-answer" data-question="Hva er TxGNN?">
<a href="https://www.nature.com/articles/s41591-024-03233-x">TxGNN</a> er en modell for dyp læring
utviklet av Zitnik Lab ved Harvard Medical School og publisert i <em>Nature Medicine</em>.
Den predikerer nye sammenhenger mellom legemiddel og sykdom og er den første grunnmodellen for
legemiddelreposisjonering som er utformet spesielt for klinikere.
</p>

<blockquote class="expert-quote">
"TxGNN integrerer en kunnskapsgraf med 17 080 sykdommer og bruker grafnevrale nettverk
til å lære komplekse relasjoner mellom noder, og predikerer dermed legemidlers potensielle effekt mot
sjeldne sykdommer."
<cite>&mdash; Huang et al., Nature Medicine (2024)</cite>
</blockquote>

---

## Datakilder

Kildene til prediksjoner, evidens og legemiddeldata, med lisenser og oppdateringsfrekvens,
er samlet på siden <a href="{{ '/sources/' | relative_url }}">Datakilder</a>.

---

## Faglig grunnlag

> Huang, K., et al. (2024). A foundation model for clinician-centered drug repurposing. *Nature Medicine*.
> [DOI: 10.1038/s41591-024-03233-x](https://doi.org/10.1038/s41591-024-03233-x)

---

## Omfang

| Element | Verdi |
|------|-------|
| Legemiddelrapporter | {{ site.data.drug_stats.total_drugs }} |
| Registreringsdata | EMA (sentrale markedsføringstillatelser i EU) |
| Nettsteder i drift | 30 land / regioner |

---

## Kontakt

- **GitHub Issues**: <https://github.com/yao-care/NOTxGNN/issues>
- **Utvikler**: 藥提醒科技有限公司 (<https://www.yao.care>, service@yao.care)
- **Produktoversikt**: <https://www.yao.care/medical/txgnn/>

---

<div class="disclaimer">
<strong>Ansvarsfraskrivelse</strong><br>
Denne rapporten er kun ment som referanse for akademisk forskning og <strong>utgjør ikke medisinske råd</strong>. Følg alltid legens anvisninger; juster aldri medisineringen på egen hånd. Enhver beslutning om legemiddelreposisjonering krever fullstendig klinisk validering og regulatorisk gjennomgang.
<br><br>
<small>Gjennomgått av: 藥提醒科技有限公司 (yao.care)</small>
</div>
