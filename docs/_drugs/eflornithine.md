---
layout: default
title: Eflornithine
parent: Kun modellprediksjon (L5)
nav_order: 140
evidence_level: L5
indication_count: 2
last_modified_at: 2026-10-28
description: "Eflornithine: predikert ny indikasjon Esotropi (evidensnivå L5). Opprinnelig indikasjon: Hirsutisme"
monitor_inn: "EFLORNITHINE"
predicted_indications: ["esotropia", "neurotrophic keratopathy"]
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

<div id="pharmacist" markdown="1">

## Farmasøytens vurderingsrapport

</div>

## Eflornitin: Fra hirsutisme til esotropi
{: .text-alpha }

## Oppsummering i én setning

Eflornitin er en hemmer av enzymet ornitindekarboksylase, opprinnelig godkjent for behandling av **hirsutisme** (uønsket hårvekst i ansiktet).
TxGNN-modellen predikerer at legemidlet kan ha effekt ved **esotropi**, men det finnes **ingen kliniske studier** og **ingen publikasjoner** som støtter denne prediksjonen i de data som er sammenstilt for rapporten.

## Hurtigoversikt

| Punkt | Innhold |
|------|------|
| Opprinnelig indikasjon | Hirsutisme |
| Predikert ny indikasjon | Esotropi |
| TxGNN-prediksjonsscore | 0,9985 |
| Evidensnivå | L5 |
| Markedsstatus i Norge | Markedsført (gyldige tillatelser: 1 av 1) |
| Antall godkjenninger | 1 (gyldige: 1) |
| Anbefalt beslutning | Hold |

## Hvorfor er denne prediksjonen rimelig?

Ifølge avsnittet «Mechanism of Action» i preparatomtalen som er godkjent av amerikanske FDA (Prescribing Information), for Eflornithine (uoffisiell oversettelse): «Eflornitin er en irreversibel hemmer av enzymet ornitindekarboksylase (ODC), det første og hastighetsbegrensende enzymet i biosyntesen av polyaminer og et transkripsjonelt mål for MYCN. Polyaminer er involvert i differensiering og proliferasjon av pattedyrceller og er viktige for neoplastisk transformasjon.» Engelsk originaltekst: "Eflornithine is an irreversible inhibitor of the enzyme ornithine decarboxylase (ODC), the first and rate-limiting enzyme in the biosynthesis of polyamines and a transcriptional target of MYCN. Polyamines are involved in differentiation and proliferation of mammalian cells and are important for neoplastic transformation." ([DailyMed: Iwilfin (eflornithine hydrochloride) prescribing information, USWM, LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=6716d8cc-66e6-4cee-935c-ccb85ed984f5), versjon av 2026-03-26; hentet 2026-11-19). Ut fra generell farmakologi er eflornitin en irreversibel hemmer av ornitindekarboksylase (ODC, kodet av *ODC1*), det hastighetsbegrensende enzymet i polyaminsyntesen. Mekanismen forklarer effekten ved hirsutisme, der hemming av polyaminer bremser celledeling i hårfollikler. Legemidlet brukes også ved afrikansk søvnsyke og er nylig godkjent i USA som vedlikeholdsbehandling ved høyrisiko nevroblastom.

Det er vanskelig å se en plausibel mekanistisk sammenheng mellom ODC-hemming og esotropi. Esotropi er en forstyrrelse i øyets innstilling som skyldes nevromuskulære, refraktive eller binokulære faktorer. Den svært høye TxGNN-scoren (0,9985) kommer fra TxGNN-modellen (dyp læring) og er en ren modellprediksjon uten støtte i studier eller litteratur. Scoren kan gjenspeile likheter modellen har lært mellom beslektede sykdommer, ikke biologisk evidens. Prediksjonen bør derfor tolkes med stor forsiktighet.

Som sekundær prediksjon fremhever modellen også **nevrotrofisk keratopati** (score 0,9938). Her finnes en teoretisk kobling via polyaminenes rolle i celleproliferasjon og nerveregenerering, men polyaminmangel vil sannsynligvis svekke fremfor å fremme sårheling i hornhinnen. Effektretningen er uklar og muligens ugunstig, og koblingen er spekulativ.

## Klinisk studiedokumentasjon

Foreløpig er ingen relaterte kliniske studier registrert.

## Litteraturdokumentasjon

Foreløpig er ingen relatert litteratur tilgjengelig.

## Markedsinformasjon for Norge

| Godkjenningsnummer | Produktnavn | Doseform | Godkjent indikasjon |
|---------|------|------|-----------|
| EMEA/H/C/000325 | Vaniqa (Almirall, S.A.) | Ikke oppgitt | Hirsutisme (status: godkjent) |

## Sikkerhetsvurderinger

- **Kontraindikasjoner fra kunnskapsgraf (ikke preparatomtale):** Kunnskapsgrafen (PrimeKG) knytter eflornitin til eksantem og dermatitt. Dette er ikke hentet fra preparatomtalen og må verifiseres.
- **Legemiddelinteraksjoner:** Én farmakologisk registrering, med målproteinet ornitindekarboksylase (ODC1, human). Det er ikke angitt noen interaksjon med andre legemidler eller alvorlighetsgrad.

For fullstendig sikkerhetsinformasjon (advarsler og kontraindikasjoner) må preparatomtalen konsulteres.

## Konklusjon og neste steg

**Beslutning: Hold**

**Begrunnelse:**
Prediksjonene for esotropi og nevrotrofisk keratopati bygger kun på modellscore (evidensnivå L5), uten kliniske studier, litteratur eller en plausibel mekanistisk kobling. Legemidlet er markedsført i Norge, med 1 gyldig markedsføringstillatelse av 1.

**For å gå videre kreves følgende:**
- Hente og analysere preparatomtalens advarsler og kontraindikasjoner (blokkerende datamangel for sikkerhetsscreening)
- Innhente detaljerte MOA-data fra DrugBank
- Systematisk litteratur- og studiesøk for esotropi og nevrotrofisk keratopati
- Prekliniske data eller en mekanistisk hypotese som forklarer sammenhengen mellom ODC-hemming og de predikerte tilstandene
- Vurdering av administrasjonsvei og formulering, siden eksisterende produkt er topisk (krem) og øyeindikasjoner kan kreve en annen formulering

<!-- review:begin log -->

## Kontrollogg

Nedenfor er gjennomgangsloggen for denne siden. Setningen om at data om virkningsmekanismen ikke var tilgjengelige, er erstattet med et utdrag fra den oppgitte offisielle preparatomtalen (med uoffisiell oversettelse); modellprediksjoner, evidensnivåer og konklusjoner er ikke omskrevet.

| Kontrolldato | Punkt | Tiltak | Kilde |
|------|------|------|------|
| 2026-11-19 | Setningen «data om virkningsmekanismen er ikke tilgjengelige» erstattet med utdrag fra amerikansk preparatomtale | Setning om manglende data om virkningsmekanismen erstattet med et utdrag med kilde | [DailyMed: Iwilfin (eflornithine hydrochloride) prescribing information, USWM, LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=6716d8cc-66e6-4cee-935c-ccb85ed984f5) |

<!-- review:end log -->

## Ansvarsfraskrivelse

Dette innholdet er kun til forskningsformål og utgjør ikke medisinsk rådgivning.
Klinisk validering kreves før enhver klinisk anvendelse.

---

