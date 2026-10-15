---
layout: default
title: Eflornithine
parent: Kun modellprediksjon (L5)
nav_order: 140
evidence_level: L5
indication_count: 2
---

# Eflornithine
{: .fs-9 }

Evidensnivå: **L5** | Predikerte indikasjoner: **2** stk.
{: .fs-6 .fw-300 }

---

## Innholdsfortegnelse
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## Farmasøytens vurderingsrapport

</div>

# Eflornitin: Fra hirsutisme til esotropi

## Oppsummering i én setning

Eflornitin er en hemmer av enzymet ornitindekarboksylase, opprinnelig godkjent for behandling av **hirsutisme** (uønsket hårvekst i ansiktet).
TxGNN-modellen predikerer at legemidlet kan ha effekt ved **esotropi**, men det finnes **ingen kliniske studier** og **ingen publikasjoner** som støtter denne prediksjonen i de data som er sammenstilt for rapporten.

## Hurtigoversikt

| Punkt | Innhold |
|------|------|
| Opprinnelig indikasjon | Hirsutisme |
| Predikert ny indikasjon | Esotropi |
| TxGNN-prediksjonsscore | 99,85 % |
| Evidensnivå | L5 |
| Markedsstatus i Norge | Kun trukket tilbake (ingen gyldige markedsføringstillatelser) |
| Antall godkjenninger | 1 (trukket tilbake) |
| Anbefalt beslutning | Hold |

## Hvorfor er denne prediksjonen rimelig?

Detaljerte data om virkningsmekanisme (MOA) er ikke tilgjengelige i den sammenstilte posten. Ut fra generell farmakologi er eflornitin en irreversibel hemmer av ornitindekarboksylase (ODC, kodet av *ODC1*), det hastighetsbegrensende enzymet i polyaminsyntesen. Mekanismen forklarer effekten ved hirsutisme, der hemming av polyaminer bremser celledeling i hårfollikler. Legemidlet brukes også ved afrikansk søvnsyke og er nylig godkjent i USA som vedlikeholdsbehandling ved høyrisiko nevroblastom.

Det er vanskelig å se en plausibel mekanistisk sammenheng mellom ODC-hemming og esotropi. Esotropi er en forstyrrelse i øyets innstilling som skyldes nevromuskulære, refraktive eller binokulære faktorer. Den svært høye TxGNN-scoren (0,9985) er en ren modellprediksjon uten støtte i studier eller litteratur, og den kan gjenspeile artefakter i kunnskapsgrafen. Prediksjonen bør derfor tolkes med stor forsiktighet.

Som sekundær prediksjon fremhever modellen også **nevrotrofisk keratopati** (score 99,38 %). Her finnes en teoretisk kobling via polyaminenes rolle i celleproliferasjon og nerveregenerering, men polyaminmangel vil sannsynligvis svekke fremfor å fremme sårheling i hornhinnen. Effektretningen er uklar og muligens ugunstig, og koblingen er spekulativ.

## Klinisk studiedokumentasjon

Foreløpig er ingen relaterte kliniske studier registrert.

## Litteraturdokumentasjon

Foreløpig er ingen relatert litteratur tilgjengelig.

## Markedsinformasjon for Norge

| Godkjenningsnummer | Produktnavn | Doseform | Godkjent indikasjon |
|---------|------|------|-----------|
| EMEA/H/C/000325 | Vaniqa (Almirall, S.A.) | Ikke oppgitt | Hirsutisme (status: trukket tilbake) |

## Sikkerhetsvurderinger

- **Kontraindikasjoner fra kunnskapsgraf (ikke preparatomtale):** Kunnskapsgrafen (PrimeKG) knytter eflornitin til eksantem og dermatitt. Dette er ikke hentet fra preparatomtalen og må verifiseres.
- **Legemiddelinteraksjoner:** Én farmakologisk registrering, med målproteinet ornitindekarboksylase (ODC1, human). Det er ikke angitt noen interaksjon med andre legemidler eller alvorlighetsgrad.

For fullstendig sikkerhetsinformasjon (advarsler og kontraindikasjoner) må preparatomtalen konsulteres.

## Konklusjon og neste steg

**Beslutning: Hold**

**Begrunnelse:**
Prediksjonene for esotropi og nevrotrofisk keratopati bygger kun på modellscore (evidensnivå L5), uten kliniske studier, litteratur eller en plausibel mekanistisk kobling. Legemidlet har dessuten ingen gyldig markedsføringstillatelse i Norge.

**For å gå videre kreves følgende:**
- Hente og analysere preparatomtalens advarsler og kontraindikasjoner (blokkerende datamangel for sikkerhetsscreening)
- Innhente detaljerte MOA-data fra DrugBank
- Systematisk litteratur- og studiesøk for esotropi og nevrotrofisk keratopati
- Prekliniske data eller en mekanistisk hypotese som forklarer sammenhengen mellom ODC-hemming og de predikerte tilstandene
- Vurdering av administrasjonsvei og formulering, siden eksisterende produkt er topisk (krem) og øyeindikasjoner kan kreve en annen formulering
## Ansvarsfraskrivelse

Dette innholdet er kun til forskningsformål og utgjør ikke medisinsk rådgivning.
Klinisk validering kreves før enhver klinisk anvendelse.

---

