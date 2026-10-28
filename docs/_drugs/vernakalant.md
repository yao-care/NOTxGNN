---
layout: default
title: Vernakalant
parent: Kun modellprediksjon (L5)
nav_order: 448
evidence_level: L5
indication_count: 5
last_modified_at: 2026-10-28
description: "Vernakalant: predikert ny indikasjon Hjerneslag (stroke disorder) (evidensnivå L4). Opprinnelig indikasjon: Atrieflimmer"
monitor_inn: "Vernakalant"
predicted_indications: ["stroke disorder", "sick sinus syndrome 2, autosomal dominant", "sarcoglycanopathy", "Wildervanck syndrome", "ABri amyloidosis"]
---

# Vernakalant
{: .fs-9 }

Evidensnivå: **L5** | Predikerte indikasjoner: **5** stk.
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

## Vernakalant: Fra atrieflimmer til hjerneslag (stroke disorder)
{: .text-alpha }

## Oppsummering i én setning

Vernakalant er et atrieselektivt antiarytmisk legemiddel som opprinnelig ble godkjent for behandling av **atrieflimmer**.
TxGNN-modellen forutsier at det kan ha effekt ved **hjerneslag (stroke disorder)**, men ingen kliniske studier og ingen litteratur som direkte viser redusert slagrisiko er funnet. Kun **7 publikasjoner** om atrieflimmer er tilgjengelige, og de gir bare indirekte støtte.

---

## Hurtigoversikt

| Punkt | Innhold |
|------|------|
| Opprinnelig indikasjon | Atrieflimmer |
| Predikert ny indikasjon | Hjerneslag (stroke disorder) |
| TxGNN-prediksjonsscore | 0,9983 |
| Evidensnivå | L5 |
| Markedsstatus i Norge | Markedsført (gyldige tillatelser: 1 av 1) |
| Antall godkjenninger | 1 (gyldige: 1) |
| Anbefalt beslutning | Hold |

---

## Hvorfor er denne prediksjonen rimelig?

Detaljerte data om virkningsmekanisme (MOA) er for tiden ikke tilgjengelige i de innsamlede dataene. Ut fra kjent informasjon er vernakalant et atrieselektivt antiarytmikum som blokkerer flere ionekanaler: tidlig aktiverte kaliumstrømmer (som IKur og IKACh) og natriumkanaler på en frekvensavhengig måte. Det brukes til farmakologisk konvertering av nyoppstått atrieflimmer til sinusrytme.

Koblingen til hjerneslag er indirekte. Atrieflimmer er en viktig risikofaktor for kardioemboliske slag, så gjenoppretting av sinusrytme kan teoretisk redusere emboliskrisikoen. Samtidig medfører selve kardioversjonen en tromboembolisk risiko, og ingen av publikasjonene i datagrunnlaget viser at vernakalant reduserer forekomsten av hjerneslag.

Den svært høye TxGNN-scoren kommer fra TxGNN-modellen (deep learning) og kan gjenspeile likheter modellen har lært mellom beslektede sykdommer, som atrieflimmer og hjerneslag, ikke biologisk evidens eller en direkte terapeutisk effekt.

---

## Litteraturevidens

| PMID | År | Type | Tidsskrift | Hovedfunn |
|------|-----|------|------|---------|
| [22166900](https://pubmed.ncbi.nlm.nih.gov/22166900/) | 2012 | Oversikt | Lancet | Oversikt over behandling av atrieflimmer, inkludert slagrisikostratifisering og orale antikoagulantia |
| [17371199](https://pubmed.ncbi.nlm.nih.gov/17371199/) | 2007 | Oversikt | Expert Opin Investig Drugs | Mekanisme og utvikling av vernakalant (RSD1235) for akutt konvertering av atrieflimmer |
| [19678722](https://pubmed.ncbi.nlm.nih.gov/19678722/) | 2009 | Oversikt | J Manag Care Pharm | Etablerte og nye farmakologiske alternativer ved atrieflimmer |
| [22576674](https://pubmed.ncbi.nlm.nih.gov/22576674/) | 2012 | Oversikt | Curr Hypertens Rep | Nyere studier av atrieflimmer hos hypertensive, inkludert vernakalant og dronedaron |
| [23553811](https://pubmed.ncbi.nlm.nih.gov/23553811/) | 2013 | Oversikt | Pharmacotherapy | Klinisk oppdatering om behandling av atrieflimmer |
| [27292602](https://pubmed.ncbi.nlm.nih.gov/27292602/) | 2016 | Kohort | Am J Emerg Med | Sikkerhet og effekt av farmakologisk kardioversjon ved nyoppstått atrieflimmer, med oppfølging av tromboembolisme og død etter 30 dager |
| [25024989](https://pubmed.ncbi.nlm.nih.gov/25024989/) | 2014 | Oversikt | Heart Lung Vessels | Hovedtemaer innen kardiotorakal anestesi og intensivmedisin, inkludert nytt antiarytmikum og okklusjon av venstre aurikkel for slagreduksjon |

Merk: Ingen av publikasjonene viser at vernakalant reduserer hjerneslag direkte.

---

## Markedsinformasjon for Norge

| Godkjenningsnummer | Produktnavn | Doseringsform | Godkjent indikasjon |
|---------|------|------|-----------|
| EMEA/H/C/001215 | Brinavess | Ikke oppgitt | Atrieflimmer |

Legemidlet er markedsført, og den ene markedsføringstillatelsen (1 av 1) er gyldig.

---

## Sikkerhetsmomenter

Se pakningsvedlegget for sikkerhetsinformasjon.

Det finnes ingen registrerte legemiddelinteraksjoner i de innsamlede dataene. Dette er ikke det samme som at interaksjoner er utelukket.

---

## Andre predikerte indikasjoner (for oversikt)

| Rangering | Sykdom | Score | Evidensnivå | Vurdering |
|------|------|------|------|------|
| 2 | Sick sinus syndrome 2, autosomalt dominant | 0,9955 | L5 | Mekanistisk tvilsom. Natriumkanalblokade kan forverre sinusknutedysfunksjon, bradykardi eller ledningsforstyrrelser, så dette kan være et sikkerhetsproblem snarere enn en fordel. |
| 4 | Sarkoglykanopati | 0,9932 | L5 | Ingen mekanistisk kobling identifisert, trolig nettverksartefakt. |
| 5 | Wildervanck syndrom | 0,9929 | L5 | Strukturell utviklingsforstyrrelse, uten plausibel relevans. |
| 6 | ABri-amyloidose | 0,9926 | L5 | Ingen kjent anti-amyloid-mekanisme. |

Ingen av disse har kliniske studier eller litteratur.

---

## Konklusjon og neste steg

**Beslutning: Hold**

**Begrunnelse:**
Prediksjonen for hjerneslag kommer fra TxGNN-modellen (deep learning) og kan gjenspeile likheter modellen har lært mellom beslektede sykdommer, ikke biologisk evidens. Det finnes ingen kliniske studier og ingen data som viser at vernakalant reduserer slagrisiko, og selve kardioversjonen medfører tromboembolisk risiko.

**For å gå videre kreves følgende:**
- Sikkerhetsinformasjon fra pakningsvedlegget (advarsler og kontraindikasjoner), som er et blokkerende datagap
- Detaljerte data om virkningsmekanisme (MOA) fra DrugBank
- Studier eller registerdata som undersøker slagforekomst etter vernakalant-kardioversjon
- Avklaring av hvorfor godkjenningen ble kansellert, og om legemidlet i praksis er tilgjengelig i Norge
## Ansvarsfraskrivelse

Dette innholdet er kun til forskningsformål og utgjør ikke medisinsk rådgivning.
Klinisk validering kreves før enhver klinisk anvendelse.

---

