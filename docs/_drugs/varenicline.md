---
layout: default
title: Varenicline
parent: Kun modellprediksjon (L5)
nav_order: 445
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-28
description: "Varenicline: predikert ny indikasjon Migrene (migraine disorder) (evidensnivå L5). Opprinnelig indikasjon: Tobakksavvenning"
monitor_inn: "VARENICLINE"
predicted_indications: ["migraine disorder", "migraine with brainstem aura", "congenital hypotrichosis milia", "hypotrichosis simplex of the scalp", "diffuse alopecia areata", "alopecia", "open-angle glaucoma", "primary hereditary glaucoma", "headache disorder", "pulmonary hypertension"]
---

# Varenicline
{: .fs-9 }

Evidensnivå: **L5** | Predikerte indikasjoner: **10** stk.
{: .fs-6 .fw-300 }

---

## Innholdsfortegnelse
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist" markdown="1">

## Farmasøytens vurderingsrapport

</div>

## Vareniklin: Fra tobakksavvenning til migrene
{: .text-alpha }

## Oppsummering i én setning

Vareniklin er et legemiddel som opprinnelig brukes til **røykeslutt (tobakksavvenning)**. TxGNN-modellen forutsier at det kan ha effekt ved **migrene (migraine disorder)**, men det finnes foreløpig **ingen kliniske studier** og **ingen litteratur som støtter en terapeutisk effekt** i denne retningen. Prediksjonen er rent beregningsbasert.

---

## Hurtigoversikt

| Punkt | Innhold |
|------|------|
| Opprinnelig indikasjon | Tobakksavvenning |
| Predikert ny indikasjon | Migrene (migraine disorder) |
| TxGNN-prediksjonsscore | 0,9992 |
| Evidensnivå | L5 |
| Markedsstatus i Norge | Markedsført (gyldige tillatelser: 1 av 1) |
| Antall godkjenninger | 1 (gyldige: 1) |
| Antall tillatelser | 1 |
| Anbefalt beslutning | Hold (avvent) |

---

## Hvorfor er denne prediksjonen rimelig?

Data om virkningsmekanisme er ikke tilgjengelig i de innsamlede dataene. Ut fra kjent farmakologi er vareniklin en partiell agonist på nikotinske acetylkolinreseptorer av typen α4β2 og en full agonist på α7-reseptorer. Effekten ved røykeslutt skyldes at det reduserer sug og abstinenssymptomer og samtidig reduserer den belønnende effekten av røyking.

Nikotinerg kolinerg signalering kan i teorien knyttes til trigeminovaskulære mekanismer og «cortical spreading depression», som begge er sentrale i migrenepatofysiologien. Det finnes imidlertid ingen direkte evidens for at vareniklin har terapeutisk effekt ved migrene. Den høye TxGNN-scoren er en ren beregningsbasert prediksjon.

Det er også verdt å merke seg at hodepine er en kjent og hyppig rapportert bivirkning av vareniklin. Signalet i litteraturen peker dermed mer mot en bivirkning enn mot en behandlingseffekt.

Andre predikerte indikasjoner i datagrunnlaget (alle med evidensnivå L5 og anbefaling Hold) omfatter migrene med hjernestammeaura, kongenital hypotrikose med milia, hypotrikose simplex i hodebunnen, diffus alopecia areata, alopeci, åpenvinklet glaukom, primær hereditær glaukom, hodepineforstyrrelse og pulmonal hypertensjon. For disse finnes det ingen kliniske studier, og mekanistisk støtte er enten spekulativ eller fraværende.

---

## Evidens fra kliniske studier

Foreløpig er det ingen relaterte kliniske studier registrert.

---

## Litteraturevidens

For migrene (rangert som nr. 1) er det kun én publikasjon, og den dreier seg om en bivirkning, ikke behandling:

| PMID | År | Type | Tidsskrift | Hovedfunn |
|------|-----|------|------|---------|
| [19585710](https://pubmed.ncbi.nlm.nih.gov/19585710/) | 2009 | Kasuistikk | Therapie | Rapport om hjertestans hos en pasient som brukte vareniklin. Gir ingen støtte for effekt ved migrene. |

Det finnes ingen litteratur som viser at vareniklin behandler migrene. Relatert litteratur for «hodepineforstyrrelse» (rangert som nr. 9) handler hovedsakelig om røykeslutt og sikkerhet, blant annet:

- [27116918](https://pubmed.ncbi.nlm.nih.gov/27116918/) (2016, RCT, sekundæranalyse, Lancet): EAGLES-studien om nevropsykiatrisk sikkerhet og effekt av vareniklin, bupropion og nikotinplaster hos røykere med og uten psykiske lidelser.
- [23175211](https://pubmed.ncbi.nlm.nih.gov/23175211/) (2012, Arq Neuropsiquiatr): Rapport om badrelatert hodepine utløst av vareniklin, altså hodepine som bivirkning.
- [41991082](https://pubmed.ncbi.nlm.nih.gov/41991082/) (2026, systematisk oversikt/metaanalyse): Vareniklin ved avvenning fra e-sigaretter.

---

## Informasjon om det norske markedet

| Tillatelsesnummer | Produktnavn | Doseringsform | Godkjent indikasjon |
|---------|------|------|-----------|
| EMEA/H/C/000699 | Champix (Pfizer Europe MA EEIG) | Ikke oppgitt | Tobakksavvenning |

Tillatelsen har status **gyldig**. Det finnes 1 gyldig tillatelse av 1, og legemidlet er markedsført.

---

## Sikkerhetsvurderinger

- **Kontraindikasjoner fra kunnskapsgrafen (TxGNN/PrimeKG, ikke preparatomtale):** Angstlidelse, nevrotisk lidelse, dystymi, bipolar lidelse, alvorlig affektiv lidelse, rusmiddelmisbruk/avhengighet, akutt koronarsyndrom, perifer karsykdom, claudicatio intermittens, perifer arteriell sykdom og schizofreni. Disse er grafbaserte signaler og må verifiseres mot preparatomtalen.
- **Legemiddelinteraksjoner:** Totalt 100 interaksjoner ble funnet (kilde: DDInter). Av de 20 som er vist i datagrunnlaget, er cimetidin klassifisert som **mindre alvorlig (Minor)**. De øvrige har ukjent alvorlighetsgrad, blant annet fentermin, pantoprazol, glimepirid, mesalazin, doksysyklin, morfin, metformin, omeprazol, palonosetron, rosiglitazon, lansoprazol, vankomycin, laktulose, nizatidin, triamcinolon, prednison, simvastatin, epinefrin og vitamin A.
- **Relevante signaler fra litteraturen:** Hodepine og hjertestans er rapportert som bivirkninger i kasuistikker. Hudutslett (diffust eksantem) er også beskrevet.

Utfyllende advarsler og kontraindikasjoner i preparatomtalen må gjennomgås før en eventuell videre vurdering.

---

## Konklusjon og neste steg

**Beslutning: Hold (avvent)**

**Begrunnelse:**
Prediksjonen for migrene bygger utelukkende på en beregningsbasert modell (evidensnivå L5), uten kliniske studier og uten litteratur som støtter terapeutisk effekt. Hodepine er dessuten en kjent bivirkning av vareniklin, og markedsføringstillatelsen i Norge er kansellert. Kunnskapsgrafen peker i tillegg på flere psykiatriske og kardiovaskulære kontraindikasjoner.

**For å gå videre kreves følgende:**
- Sikkerhetsinformasjon fra preparatomtalen (advarsler og kontraindikasjoner) må innhentes. Dette er en blokkerende datamangel for sikkerhetsscreening.
- Data om virkningsmekanisme (MOA) må hentes fra DrugBank.
- Prekliniske studier som undersøker nikotinerg modulering i migrenemodeller (trigeminovaskulære veier, «cortical spreading depression»).
- En vurdering av om hodepine som bivirkning er forenlig med en migrenebehandling.
- En avklaring av regulatorisk status og tilgjengelige administrasjonsveier, siden tillatelsen i Norge er kansellert.
## Ansvarsfraskrivelse

Dette innholdet er kun til forskningsformål og utgjør ikke medisinsk rådgivning.
Klinisk validering kreves før enhver klinisk anvendelse.

---

