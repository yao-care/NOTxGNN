---
layout: default
title: Talimogene Laherparepvec
parent: Kun modellprediksjon (L5)
nav_order: 338
evidence_level: L5
indication_count: 7
---

# Talimogene Laherparepvec
{: .fs-9 }

Evidensnivå: **L5** | Predikerte indikasjoner: **7** stk.
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

# Talimogene laherparepvec: Fra kutant melanom til investigative onkolytiske viralterapiindikasjoner

## Sammenfattelse i én setning

> Talimogene laherparepvec (T-VEC) er en onkolytisk HSV-1-basert viralterapeutikum hvis godkjent indikasjon i praksis er kutant malign melanom (CMM7) — men dette datasettets `drug.original_indications`-felt er tomt, så modellen fremhevet denne kjente indikasjonen som sin beste «prediksjon» i stedet for en ekte legemiddel-repurposering-kandidat.
> De gjenstående kandidatene (leptomeningeal melanom, uveal melanom, glottis plataskjørcellekarsinom, okkulpt lungekarsinom, kloakogent karsinom, galleblæreadenoskvamøst karsinom) er ekte nye signaler, men **ingen av dem har noe klinisk forsøks- eller litteraturbevis som er fanget opp i denne pakken**, og flere er anatomisk inkompatible med T-VECs intratumorale injeksjonsrute.
> En datakløft **med blokeringsalvorlighetsgrad** (manglende TFDA-etikettadvarsler/kontraindikasjoner) betyr også at denne kandidaten ennå ikke kan gå inn i S1-sikkerhetspre-vurdering.

---

## Rask oversikt

| Element | Innhold |
|---------|---------|
| Originalindikasjon | Ikke tilgjengelig i dette datasettet (datakløft); ifølge modellens egen rasjonale tekst er T-VECs godkjente indikasjon i praksis kutant malign melanom (markedsført som Imlygic) |
| Predikert ny indikasjon | CMM7 (Kutant malign melanom) — **se forbehold nedenfor: dette er ikke et genuint nytt signal** |
| TxGNN-prediksjonsscore | 99.20% |
| Bevisnivå | L1 (per datasett; basert på ekstern/praktisk bevis, ikke på de tomme forsøks-/litteraturmatrisene i denne pakken) |
| Norges markedsstatus | ✗ Ikke markedsført |
| Antall godkjenninger | 0 |
| Anbefalt beslutning | **Avvent** (overstyrt fra postens «Fortsett med sikkerhetstiltak» — se rasjonale nedenfor) |

---

## Hvorfor er denne prediksjonen rimelig?

Detaljerte data om virkningsmekanisme er ikke tilgjengelig fra DrugBank for denne kandidaten (`original_moa: [Datakløft]`, DG002). Basert på den mekanistiske beskrivelsen som er innebygd i bevisavsnittet for repurposering, er T-VEC en onkolytisk herpes simplex virus type-1 (HSV-1) vektor som, etter intratumoralt injeksjon, selektivt replikeres og lyserer melanomceller mens den uttrykker GM-CSF for å stimulere en systemisk antitumorrespons. Denne mekanismen er klinisk validert og er grunnlaget for T-VECs godkjenning som Imlygic for melanom.

**Viktig datakalitetsforbehold:** Indikasjon på rangering 1, CMM7, er eksplisitt identifisert i postens egen rasjonale tekst som T-VECs kjernefunksjon, allerede godkjent indikasjon — ikke en ny repurposering-mulighet. Dette skjedde fordi `drug.original_indications` ble etterlatt tomt i dette datasettet, så pipelinen kunne ikke skille «kjent indikasjon» fra «ny kandidat». Dens L1-bevisnivå og tomme forsøks-/litteraturantall bør derfor leses som **bevis-innsamlingskløfter for en allerede etablert indikasjon**, ikke som en nylig oppdaget bruk.

Ser man forbi rangering 1, grupperes de genuint nye kandidatene i to grupper etter anatomisk/mekanistisk sannsynlighet:
- **Anatomisk inkompatibel** (Avvent, L5): pediatrisk leptomeningeal melanom, okkulpt lungekarsinom, rektal kloakogent karsinom, galleblæreadenoskvamøst karsinom — disse omfatter sentralnervesystemet, uoppdagbare eller dypt liggende innevoldslesioner som ikke kan nås av T-VECs godkjente intratumorale injeksjonsrute.
- **Mekanistisk sannsynlig men bevis-tynn** (Forskningsspørsmål, L3–L4): epitelloidt uveal melanom (deler melanocyttlinjal og HSV-1-reseptorexpresjon, men har ulik molekylær drivere og ingen injiserbar primærsted) og glottis plataskjørcellekarsinom (hode- og halskarsinom, indirekte støttet av T-VEC + pembrolizumab-kombinasjonsforsøk som MASTERKEY-232, selv om det ikke finnes glottis-spesifikke data i denne pakken).

---

## Bevis fra kliniske forsøk

For tiden ingen relaterte kliniske forsøk registrert (alle `evidence.clinical_trials`-matriser er tomme på alle predikerte indikasjoner i denne pakken, inkludert oppføringen CMM7 på topp).

---

## Litteraturbevis

For tiden ingen relatert litteratur tilgjengelig (alle `evidence.literature`-matriser er tomme på alle predikerte indikasjoner i denne pakken).

---

## Norges markedsinformasjon

For tiden ingen markedsføringsautoriseringsoppføringer (`total_licenses: 0`; markedsstatus: Ikke markedsført).

---

## Cytotoksisitet

T-VEC er et antineoplastisk middel (godkjent onkolytisk viralterapeutikum for kutant melanom), så denne delen gjelder.

| Element | Innhold |
|---------|---------|
| Cytotoksisitetsklassifisering | Immunterapi — Onkolytisk viral terapi (HSV-1-vektor konstruert for å uttrykke GM-CSF), ikke et konvensjonelt cytotoksisk kjemoterapilege |
| Risiko for beinnmargsundertrykkelse | Se pakningsvedlegget for advarsler og forholdsregler |
| Emetogenisitetsklassifisering | Se pakningsvedlegget for advarsler og forholdsregler |
| Overvåkingspunkter | Se pakningsvedlegget for advarsler og forholdsregler |
| Håndteringsbeskyttelse | Som et levende, replikasjonskompetent onkolytisk virusprodukt krever håndtering biosikkerhetstiltak som er forskjellige fra standard cytotoksisk legemiddelhåndteringsforskrifter (f.eks. beskyttelse mot virusspredning, dedikert avfallshåndtering). Spesifikke TFDA-etikett-krav er utilgjengelig i påvente av løsning av DG001 |

---

## Sikkerhetshensyn

Se pakningsvedlegget for sikkerhetsinformasjon. Merk: TFDA-etikettadvarsler, kontraindikasjoner og legemiddelinteraksjonsdata er for tiden en datakløft **med blokeringsalvorlighetsgrad (DG001)** — denne kandidaten kan ikke gå videre til S1-sikkerhetspre-vurdering før dette er løst.

---

## Konklusjon og neste trinn

**Beslutning: Avvent**

**Rasjonale:**
Den mekanistiske saken for den best rangerte indikasjonen (CMM7/kutant melanom) er sterk, men den gjenspeiler T-VECs eksisterende godkjente bruk i stedet for en ekte repurposering-mulighet — en registreringskløft, ikke en oppdagelse. Alle ekte nye kandidater (ranger 2–7) bærer svakt bevis (L3–L5) og flere er utelukket av administrasjonsvei-inkompatibilitet. Kombinert med en datakløft med blokeringsalvorlighetsgrad, kan ingen kandidat i denne pakken for tiden rettferdiggjøre en «Gå» eller «Fortsett med sikkerhetstiltak»-beslutning.

**For å gå videre trengs følgende:**
- Løs DG001 (Blokeringsalvorlighetsgrad): skaff og parser TFDA-etikettens PDF for advarsler/kontraindikasjoner før noen S1-sikkerhetssvurdering
- Løs DG002 (Høy): hent fullstendige MOA-data via DrugBank-API
- Rett `drug.original_indications` for å reflektere T-VECs faktiske godkjente indikasjon (kutant melanom) slik at fremtidlige TxGNN-kjøringer ikke gjenopptrer den som en «ny» prediksjon
- For genuint nye kandidater — særlig glottis plataskjørcellekarsinom — skaff dedikert forsøks-/litteraturbevis (f.eks. MASTERKEY-232 data) før du går videre forbi Forskningsspørsmål-fase
- Klargjør lokal markedsstatus/regulatorisk vei, siden en markedsføringsautoriseringsapplikasjon i seg selv kan være en forutsetning før noen repurposering-indikasjon kan forfølges

## Ansvarsfraskrivelse

Dette innholdet er kun til forskningsformål og utgjør ikke medisinsk rådgivning.
Klinisk validering kreves før enhver klinisk anvendelse.

---

