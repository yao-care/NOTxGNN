---
layout: default
title: Om
nav_order: 90
permalink: /about/
description: "NOTxGNN er en plattform for prediksjon av legemiddelreposisjonering utviklet av 藥提醒科技有限公司 (yao.care), bygget på TxGNN-modellen fra Harvard og med dekning av legemidler godkjent av DMP i Norge."
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
Den predikerer utvidelse av indikasjoner for legemidler godkjent av DMP i Norge. I tillegg til
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
den modellen, og omfatter integrasjon av nasjonale legemiddelregistreringsdata, dobbel prediksjon
med kunnskapsgraf og dyp læring, evidensgradering fra PubMed / ClinicalTrials samt integrasjon mot
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
<a href="https://www.nature.com/articles/s41591-023-02233-x">TxGNN</a> er en modell for dyp læring
utviklet av Zitnik Lab ved Harvard Medical School og publisert i <em>Nature Medicine</em>.
Den predikerer nye sammenhenger mellom legemiddel og sykdom og er den første grunnmodellen for
legemiddelreposisjonering som er utformet spesielt for klinikere.
</p>

<blockquote class="expert-quote">
"TxGNN integrerer en kunnskapsgraf med 17 080 biomedisinske entiteter og bruker grafnevrale nettverk
til å lære komplekse relasjoner mellom noder, og predikerer dermed legemidlers potensielle effekt mot
sjeldne sykdommer."
<cite>&mdash; Huang et al., Nature Medicine (2023)</cite>
</blockquote>

---

## Datakilder

<table class="comparison-table">
<thead>
<tr><th>Type</th><th>Kilde</th><th>Beskrivelse</th></tr>
</thead>
<tbody>
<tr><td>KI-prediksjon</td><td><a href="https://zitniklab.hms.harvard.edu/projects/TxGNN/">TxGNN</a></td><td>Harvards prediksjonsmodell basert på kunnskapsgraf</td></tr>
<tr><td>Kliniske studier</td><td><a href="https://clinicaltrials.gov/">ClinicalTrials.gov</a></td><td>Globalt register over kliniske studier</td></tr>
<tr><td>Litteratur</td><td><a href="https://pubmed.ncbi.nlm.nih.gov/">PubMed</a></td><td>Database over biomedisinsk litteratur</td></tr>
<tr><td>Legemiddelinformasjon</td><td><a href="https://go.drugbank.com/">DrugBank</a></td><td>Database over legemidler og målmolekyler</td></tr>
<tr><td>Registreringsdata</td><td><a href="https://www.dmp.no/">DMP</a></td><td>Data om legemiddelgodkjenning i Norge</td></tr>
</tbody>
</table>

---

## Faglig grunnlag

> Huang, K., et al. (2023). A foundation model for clinician-centered drug repurposing. *Nature Medicine*.
> [DOI: 10.1038/s41591-023-02233-x](https://doi.org/10.1038/s41591-023-02233-x)

---

## Omfang

| Element | Verdi |
|------|-------|
| Legemiddelrapporter | {{ site.drugs.size }} |
| Legemiddelmyndighet | DMP |
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
