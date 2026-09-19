---
layout: default
title: Netarsudil
parent: Moderat evidens (L3-L4)
nav_order: 241
evidence_level: L4
indication_count: 2
---

# Netarsudil
{: .fs-9 }

Evidensnivå: **L4** | Predikerte indikasjoner: **2** stk.
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

# Netarsudil: Fra uspesifisert originalindikasjon til Primær Arvelig Glaukom

## Oppsummering i en setning

> Netarsudils opprinnelige godkjent indikasjon er ikke registrert i det gjeldende regulatoriske datasett (datakluft), selv om støttebeviser i denne Evidence Pack indikerer at det er en allerede markedsført Rho-kinase (ROCK)-hemmer brukt til kontroll av intraokulært trykk.
> TxGNN-modellen forutsier dessuten potensiell effektivitet for **Primær Arvelig Glaukom**,
> men denne spesifikke genetiske undertypen er for øyeblikket støttet av kun **1 indirekte relatert klinisk studie** og **0 dedikerte publikasjoner**.

---

## Rask oversikt

| Element | Innhold |
|--------|--------|
| Originalindikasjon | Ikke registrert i gjeldende datasett (datakluft — `original_indications` er tom og `original_moa` er merket som en datakluft; se notat nedenfor) |
| Forutsagt ny indikasjon | Primær Arvelig Glaukom |
| TxGNN-prediksjonspoengsum | 99.50% |
| Bevisnivå | L4 |
| Markedsstatus i Norge | ✗ Ikke markedsført |
| Antall autorisasjoner | 0 |
| Anbefalt beslutning | Avvent |

**Notat om originalindikasjon:** Evidence Packens egen analyse av en relatert, høyere rangert prediksjon ("glaukom", rangering 2 i denne pakken) slår fast at netarsudils mekanisme (ROCK-hemning som senker intraokulært trykk) tilsvarer dets allerede etablerte godkjent bruk for åpen-vinkel glaukom/okulær hypertensjon — det tomme `original_indications`-feltet er internt flagget som en datakluft snarere enn bevis på at ingen godkjent bruk eksisterer. Dette bør bekreftes mot en primær regulatorisk kilde før bruk i beslutningstagning.

---

## Hvorfor er denne prediksjonen rimelig?

Detaljert informasjon om virkningsmekanisme er ikke tilgjengelig i feltet `drug.original_moa` (merket som en datakluft). Imidlertid beskriver bevisepakken grunnlaget for repurposering netarsudil som en selektiv **Rho-kinase (ROCK)-hemmer** som også hemmer noradrenalin-transportøren (NET). ROCK-hemning avslapper cytoskelettet i trabekulær nettmaske og endotelceller i Schlemms kanal, og reduserer dermed motstanden mot utflyt av kammervæske og senker således det intraokulære trykket (IOP) — en mekanisme som allerede er godt validert for glaukom generelt.

Arvelige former for glaukom (f.eks. primært medfødt glaukom, juvenilt åpen-vinkel glaukom, vanligvis forbundet med *MYOC*/*CYP1B1*-mutasjoner) deler samme nedstrøms patologi: unormal trabekulær nettmaske struktur/funksjon som fører til økt utstrømningsresistans. Fordi ROCK-hemmere virker direkte på trabekulær nettmaske cytoskjelett og ekstracellulær matrise snarere enn på det spesifikke årsaksgivende genproduktet, er det en plausibel mekanistisk begrunnelse for genotype-uavhengig effektivitet ved arveformet glaukom.

Når det er sagt, gjør det eneste identifiserte forsøket (NCT06969586) **ikke** faktisk studie primær arveformet glaukom — det inkluderer pasienter med **Fuchs Endothelial Corneal Dystrophy (FECD)**, en distinkt korneal endotelial sykdom, og evaluerer beskyttelse av hornhinne-celler etter grå stær-operasjon snarere enn IOP-kontroll i genetisk definert glaukom. De to tilstandene deler bare den felles tråden av "ROCK-hemmer aktivitet i forstøtt vev." Direkte klinisk bevis for denne spesifikke forutsagte indikasjonen er derfor i hovedsak fraværende, og den mekanistiske broen forblir en hypotese snarere enn en påvist effekt.

---

## Bevis fra kliniske forsøk

| Forsøksnummer | Fase | Status | Inkludering | Viktige funn |
|---------|------|------|------|---------|
| [NCT06969586](https://clinicaltrials.gov/study/NCT06969586) | N/A | Rekrutterer ved invitasjon | 50 | Evaluerer hvorvidt topikale ROCK-hemmere reduserer tap av korneal endotelial celle etter grå stær-operasjon hos pasienter med glaukom og Fuchs Endothelial Corneal Dystrophy (FECD). Relevans gradert **C**: studiepopulasjonen er FECD-pasienter, ikke primære arvelige glaukom-pasienter — det er et indirekte, mekanisme-delt signal snarere enn direkte bevis for denne indikasjonen. |

---

## Litteraturbevis

For tiden ingen relatert litteratur tilgjengelig.

---

## Markedsinformasjon for Norge

Ingen markedsføringstillatelser er registrert for netarsudil i Norge (`total_licenses`: 0; markedsstatus: Ikke markedsført). Ingen produkt-/doserings-form-/indikasjondata kan hentes ut på dette tidspunktet.

---

## Sikkerhetshensyn

Vennligst se pakningsvedlegget for sikkerhetsinformasjon.

*(Notat: nøkkeladvarslinger, kontraindikasjoner og legemiddel-legemiddel interaksjonsdata er alle merket som dataklufter i denne Evidence Pack. Særlig bemerkes at TFDA-ekvivalente pakningsvedleggsadvarsler/kontraindikasjoner er internt flagget som en datakluft med **blokkerings-alvorlighetsgrad**, noe som betyr at en formell sikkerhetspre-screening (S1) for øyeblikket ikke kan fullføres for dette legemidlet.)*

---

## Konklusjon og neste trinn

**Beslutning: Avvent**

**Begrunnelse:**
Bevis spesifikt for primær arveformet glaukom er begrenset til en enkelt pågående studie som faktisk studerer en annen korneal tilstand (FECD), vurdert kun som indirekte relevant (Grad C), som plasserer denne indikasjonen på Bevisnivå L4 / Beslutningsstadium S1 ("Forskningsspørsmål"). Kombinert med en blokkerings-alvorlighetsgrad datakluft på sikkerhetadvarsler/kontraindikasjoner og legemidlets ubestemt regulatorisk status i Norge (0 autorisasjoner, ikke markedsført), er det for øyeblikket utilstrekkelig direkte bevis eller regulatorisk grunnlag for å fortsette videre.

**For å fortsette, kreves følgende:**
- Løsing av datakluften med blokkerings-alvorlighetsgrad (DG001): TFDA/regulatoriske pakningsvedleggsadvarsler og kontraindikasjoner, nødvendig før sikkerhetspre-screening (S1) kan fullføres
- Bekreftet dokumentasjon av virkningsmekanisme fra DrugBank (DG002), for å kunne vurdere mekanistisk plausibilitet for genetiske glaukom-undertyper
- Kliniske forsøk eller litteratur som studerer netarsudil spesifikt i primær arvelig/genetisk glaukom populasjoner (f.eks. *MYOC*/*CYP1B1*-assosiert sykdom), snarere enn å ekstrapolere fra Fuchs korneal dystrofi studier
- Avklaring av netarsudils sanne opprinnelige godkjent indikasjon og regulatorisk status, gitt at en relatert prediksjon i samme Evidence Pack (glaukom, bredt) indikerer at legemidlet allerede kan være et godkjent IOP-senkende middel andre steder — dette bør verifiseres mot primære regulatoriske kilder snarere enn å bli stående som et tomt felt

## Ansvarsfraskrivelse

Dette innholdet er kun til forskningsformål og utgjør ikke medisinsk rådgivning.
Klinisk validering kreves før enhver klinisk anvendelse.

---

