---
layout: default
title: Prasugrel
parent: Kun modellprediksjon (L5)
nav_order: 287
evidence_level: L5
indication_count: 10
---

# Prasugrel
{: .fs-9 }

Evidensnivå: **L5** | Predikerte indikasjoner: **10** stk.
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

# Prasugrel: Fra antitrombosytt-terapi til pulmonær hypertensjon

## Oppsummering i én setning

> Prasugrel er en thienopyridin-P2Y12-reseptorblokkator (antitrombosytt-middel); detaljerte opplysninger om originale indikasjoner og virkningsmekanisme er ikke tilgjengelige i denne bevisspakken.
> TxGNN-modellen forutsier at det kan være effektivt for **pulmonær hypertensjon**, men den støttende bevis er begrenset til **2 kliniske forsøk og 2 publikasjoner**, hvorav ingen direkte omhandler prasugrel eller pulmonær hypertensjon — dette er et høyt-poeng-signal med lav bevis.

---

## Rask oversikt

| Element | Innhold |
|------|------|
| Opprinnelig indikasjon | Ikke tilgjengelig i bevisspakken (legemiddel ikke markedsført i Norge; klassifisert som thienopyridin-P2Y12-blokkator / antitrombosytt-middel basert på litteraturbeviser) |
| Forutsagt ny indikasjon | Pulmonær hypertensjon |
| TxGNN-prediksjonspoeng | 99.88% |
| Bevisnivå | L5 (kun modellpreduksjon) |
| Markedsstatus i Norge | ✗ Ikke markedsført |
| Antall autorisasjoner | 0 |
| Anbefalt beslutning | Hold |

---

## Hvorfor er denne prediksjonen rimelig?

For tiden er detaljert virkningsmekanisme-data ikke tilgjengelig (`original_moa: [Data Gap]`). Basert på informasjon som er innebygd i litteraturnotatene i bevisspakken, er prasugrel en thienopyridin-klasse P2Y12-reseptorblokkator, i samme farmakologiske familie som klopidogrel og tiklopydin, og dens etablerte rolle er som antitrombosytt-middel (f.eks. for preventering av stenttrombase).

For den høyest rangerte forutsagte indikasjonen, **pulmonær hypertensjon**, er modellens egen omformål-logikk eksplisitt om svakheten i forbindelsen: *"Ingen direkte mekanistisk forbindelse. Antitrombosytt-midler kan teoretisk spille en tilleggsrolle i noe tromboembolisme-/KTPH (kronisk tromboembolis pulmonær hypertensjon) patofysiologi, men forsøkene og litteraturen som er oppgitt er ikke fokusert på pulmonær hypertensjon — dette er et typisk TxGNN høyt-poeng-signal uten tilsvarende beviser (en sannsynlig falsk positiv)."*

Både de hentede kliniske forsøkene (NOAC-bruk ved atrieflimmer; kreftassosiert tromboembolisme-screening) og begge hentede publikasjoner (COVID-19 komorbiditet-terapi; klopidogrel-etterlevelse etter PCI) er kun tangensielt relatert til antitrombosytt-terapi generelt og studerer ikke prasugrel i pulmonær hypertensjon. Den mekanistiske hypotesen (antitrombosytt-effekt i KTPH) er biologisk plausibel i teorien, men er for tiden ikke støttet av direkte data.

**Merknad om alternative kandidater:** Blant de andre 9 forutsagte indikasjonene i denne bevisspakken, **migrene** (rangering 2, poeng 99.88%) har relativt sterkere støttende beviser — en åpen pilot-studie og en retrospektiv kohortstudie som spesifikt beskriver thienopyridin (klopidogrel/prasugrel-klasse) bruk som reduserer migrene-symptomer hos pasienter med patentforamen ovale (PFO), og når bevisnivå **L3 / beslutningsstadium S1 (Forskningsspørsmål)**. Dette kan garantere separat evaluering, selv om det er beviser på legemiddelklasse-nivå snarere enn prasugrel-spesifikk.

---

## Kliniske forsøksbeviser

| Forsøksnummer | Fase | Status | Deltakere | Viktige funn |
|---------|------|------|------|---------|
| [NCT03993119](https://clinicaltrials.gov/study/NCT03993119) | N/A | Avsluttet | 500 | Observasjonell tverrsnittsstudie av NOAC-håndtering hos eldre spanske pasienter med ikke-ventilklaffbetinget atrieflimmer; ingen direkte relevans til prasugrel eller pulmonær hypertensjon (relevansnivå C). |
| [NCT04846556](https://clinicaltrials.gov/study/NCT04846556) | N/A | Avsluttet | 300 | Retrospektiv studie av forsøkskvalifikasjon for kreftassosiert tromboembolisme (CARAVAGGIO-type populasjon); involverer ikke prasugrel eller pulmonær hypertensjon (relevansnivå C). |

---

## Litteraturbeviser

| PMID | År | Type | Tidsskrift | Viktige funn |
|------|-----|------|------|---------|
| [21241206](https://pubmed.ncbi.nlm.nih.gov/21241206/) | 2011 | Kohortstudie | Curr Med Res Opin | Faktorer knyttet til klopidogrel-etterlevelse hos AKS-pasienter etter PCI; prasugrel nevnt kun som et alternativt regime, ikke studert i pulmonær hypertensjon. |
| [34713782](https://pubmed.ncbi.nlm.nih.gov/34713782/) | 2021 | Observasjonell/retrospektiv | Kardiologiia | ACTIV-register-analyse av bakgrunnskardiologisk terapi og COVID-19-utfall; ingen spesifikk data på prasugrel eller pulmonær hypertensjon. |

---

## Markedsinformasjon for Norge

Prasugrel har for tiden **ingen markedsføringstillatelse** i Norge (`market_status: Not marketed / Not Marketed`, `total_licenses: 0`). Ingen produktoppføringer er tilgjengelige for gjennomgang.

---

## Sikkerhetshensyn

Se pakningsvedlegget for sikkerhetsinformasjon. Ingen viktige advarsler, kontraindikasjoner eller legemiddelinteraksjon-data var hentbar for denne evalueringen (`DDI query_status: not_found`).

---

## Konklusjon og neste trinn

**Beslutning: Hold**

**Begrunnelse:**
Den høyest rangerte forutsagte indikasjonen (pulmonær hypertensjon) har bevisnivå **L5** — et TxGNN-modellpoeng uten tilsvarende sykdomsspesifikke kliniske forsøk eller litteratur. Kombinert med legemidlets ikke-markedsførte status i Norge og en **blokkerende datakløft** på det offisielle pakningsvedlegget (advarsler/kontraindikasjoner), oppfyller kandidaten for tiden ikke terskelen til å gå videre forbi innledende screening (S0).

**For å komme videre kreves følgende:**
- TFDA/produsent-pakningsvedlegg (advarsler og kontraindikasjoner) — for tiden en **blokkerende** datakløft (DG001)
- Bekreftet virkningsmekanisme-data fra DrugBank eller tilsvarende kilde (DG002)
- Sykdomsspesifikke (pulmonær hypertensjon, ideelt KTPH) prekliniske eller kliniske beviser for prasugrel, snarere enn generell antitrombosytt-klasse litteratur
- Dersom man forfølger migrenésignalet/PFO (rangering 2) i stedet, en prasugrel-spesifikk forsøk eller kasuistikk, da gjeldende beviser er kun på thienopyridin-legemiddelklasse-nivå

## Ansvarsfraskrivelse

Dette innholdet er kun til forskningsformål og utgjør ikke medisinsk rådgivning.
Klinisk validering kreves før enhver klinisk anvendelse.

---

