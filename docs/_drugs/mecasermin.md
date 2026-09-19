---
layout: default
title: Mecasermin
parent: Kun modellprediksjon (L5)
nav_order: 223
evidence_level: L5
indication_count: 5
---

# Mecasermin
{: .fs-9 }

Evidensnivå: **L5** | Predikerte indikasjoner: **5** stk.
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

# Mecasermin: Fra uspesifisert original indikasjon til Monisomi X

## Sammendrag på én setning

> Den opprinnelige godkjente indikasjonen for Mecasermin er ikke dokumentert i den tilgjengelige regulatoriske datakilde, og virkningsmekanisme-data mangler for øyeblikket.
> TxGNN-modellens høyest rangerte prediksjon er **Monisomi X**, men dette signalet støttes av **0 kliniske forsøk** og **0 publikasjoner**, og det underliggende rasjonalet er en indirekte analogi i stedet for en validert mekanistisk kobling.

## Rask oversikt

| Element | Innhold |
|---------|---------|
| Original indikasjon | Ikke dokumentert i gjeldende datakilde |
| Forutsagt ny indikasjon | Monisomi X |
| TxGNN prediktjonsscore | 99.59% |
| Evidensnivå | L5 |
| Markedsstatus i Norge | Ikke markedsført |
| Antall autorisasjoner | 0 |
| Anbefalt beslutning | Avvente |

## Hvorfor er denne prediksjonen rimelig?

For øyeblikket er detaljerte virkningsmekanisme-data for Mecasermin ikke tilgjengelige, og ingen original indikasjon er registrert i den gjeldende datakilde. Dette er flagget som et **blokkerende datahull** (manglende TFDA/pakningsvedleggsadvarsler og kontraindikasjoner) og et **kritisk datahull** (manglende virkningsmekanisme), som begge begrenser enhver sikker mekanistisk vurdering.

For den høyest rangerte prediksjonen, Monisomi X (vanligvis assosiert med Turners syndrom), sier modellens eget rasjonale at denne tilstanden ofte ledsages av delvis GH/IGF-1-akseinsufficiens og vekstforsinkelse, så IGF-1-tilskudd kan teoretisk tilby vekstfordel. Imidlertid er dette eksplisitt notert som en **indirekte analogi** — Turners syndrom håndteres konvensjonelt med veksthormon (GH), ikke mecasermin (rekombinant IGF-1), og det er ingen direkte mekanistisk bevisrekke som kobler mecasermin spesifikt til denne tilstanden. Prediksjonen bør behandles som et graf-avledet signal i stedet for en understøttet hypotese.

Bemerkelsesverdig er en lavere-rangert kandidat i denne evidenspakken — **veksthormoninsensitivitetssyndrom med immunologisk dysfunksjon 2, autosomalt dominant** (rang 3, score 99.06%) — som har et betydelig sterkere mekanistisk grunnlag: det faller innenfor familien av GH-insensitivitetssyndrom/Laron-type-syndrom, som er det farmakologiske området mecasermin (rhIGF-1) er designet for å adressere ved å omgå en defekt GH-reseptor-vei. Denne kandidaten har allerede avansert til beslutningsstadium **S1 (Forskningsspørsmål)**, versus S0 (Avvente) for Monisomi X, og kan være verdt nærmere gjennomgang til tross for dens lavere TxGNN-score.

## Evidens fra kliniske forsøk

For øyeblikket ingen relaterte kliniske forsøk registrert

## Litteraturbevis

For øyeblikket ingen relatert litteratur tilgjengelig

## Markedsinformasjon for Norge

Mecasermin har for øyeblikket **ingen markedsføringstillatelser i Norge** (totalt antall lisenser: 0; markedsstatus: Ikke markedsført). Ingen produkt-, doseringsformal- eller godkjent indikasjonsinformasjon er tilgjengelig i den gjeldende datakilde.

## Sikkerhetshensyn

Vær vennlig og se pakningsvedlegget for sikkerhetsinformasjon. (Pakningsvedleggsadvarsler, kontraindikasjoner og stoff-stoff-interaksjondata er for øyeblikket utilgjengelige og er flagget som et blokkerende datahull som krever henting av TFDA-etikett før noen sikkerhetsstadium-evaluering kan fortsette.)

## Konklusjon og neste trinn

**Beslutning: Avvente**

**Begrunnelse:**
Den høyest rangerte forutsatte indikasjonen (Monisomi X) har kun evidensnivå L5 (kun modellprediksjon, ingen kliniske forsøk eller litteratur) og er basert på en indirekte mekanistisk analogi i stedet for en validert vei. Kombinert med fraværet av markedsføringstillatelse i Norge og et blokkerende hull i pakningsvedleggssikkerhetsdata, er det for øyeblikket utilstrekkelig grunnlag for å avansere ut over foreløpig forskning.

**For å fortsette, er følgende nødvendig:**
- TFDA/pakningsvedleggsadvarsler og kontraindikasjoner (blokkerende hull, DG001)
- Bekreftet virkningsmekanisme-dokumentasjon fra DrugBank eller tilsvarende kilde (DG002)
- Dokumentasjon av Mecasermin's opprinnelige godkjente indikasjon(er)
- Målrettet litteratur-/klinisk forsøkssøk for den mekanistisk sterkere kandidaten (veksthormoninsensitivitetssyndrom med immunologisk dysfunksjon 2, autosomalt dominant), gitt dens tettere sammenheng med Mecasermin's kjente farmakologi

## Ansvarsfraskrivelse

Dette innholdet er kun til forskningsformål og utgjør ikke medisinsk rådgivning.
Klinisk validering kreves før enhver klinisk anvendelse.

---

