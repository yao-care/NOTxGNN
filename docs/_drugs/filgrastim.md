---
layout: default
title: Filgrastim
parent: Kun modellprediksjon (L5)
nav_order: 152
evidence_level: L5
indication_count: 10
---

# Filgrastim
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

# Filgrastim: Fra neutropeni (G-CSF-støtteterapi) til primær sekresjonsforstyrrelse av platelett

## Oppsummering i en setning

> Filgrastim er et rekombinant humant G-CSF som klinisk brukes til å stimulere neutrofil-gjenoppretting og mobilisere hematopoietiske stamceller i støtteterapisammenheng (f.eks. rundt kjemoterapi og stamcelletransplantasjon).
> TxGNN-modellen forutsier at det kan være effektivt for **Primær sekresjonsforstyrrelse av platelett**,
> men bevisstøtten er svak — alle **13 kliniske forsøk** som er identifisert bruker Filgrastim bare som støtteagent for stamcelle-mobilisering/neutrofil-gjenoppretting i ikke-relaterte transplantprotokoller, og bare **1 publikasjon** berører emnet løst, uten direkte bevis som evaluerer Filgrastim for denne indikasjonen.

> ⚠️ **Merknad om original indikasjon**: Bevisepakken inneholder ikke en bekreftet regulatorisk godkjent indikasjonstekst for Filgrastim (`original_indications` er tom, `original_moa` er et datahull). Beskrivelsen av «Neutropeni» ovenfor er utledet fra gjentatt kontekst i merknadene om forsøksrelevans (G-CSF brukt for «stamcelle-mobilisering/neutrofil-gjenoppretting») og bør bekreftes mot en autoritativ etikett før bruk i dokument rettet til eksterne.

---

## Rask oversikt

| Element | Innhold |
|---------|---------|
| Original indikasjon | Ikke tilgjengelig i bevisepakken (regulatorisk datahull) — G-CSF er kontekstuelt referert som støtte for neutrofil-gjenoppretting/stamcelle-mobilisering |
| Forutsagt ny indikasjon | Primær sekresjonsforstyrrelse av platelett |
| TxGNN-prediktjonsscore | 99.99% (rangert 48 blant alle prediksjoner) |
| Bevisnivå | L5 |
| Norsk markedsstatus | ✗ Ikke markedsført |
| Antall autorisasjoner | 0 |
| Anbefalt beslutning | Avvent |

---

## Hvorfor er denne prediksjonen rimelig?

For tiden er detaljerte data om virkningsmekanisme ikke tilgjengelig (flagget som et **høy-alvorlighet datahull** i bevisepakken). Basert på tilgjengelig kontekstinformasjon, er Filgrastim et rekombinant granulocytt-kolonistimulerende faktor (G-CSF) hvis kjente farmakologi er å stimulere proliferasjon og differensiering av granulocytt-forløperceller og mobilisere hematopoietiske stamceller — en mekanisme som klinisk brukes til å støtte neutrofil-gjenoppretting etter myelosuppressiv terapi og mobilisere stamceller før transplantasjon.

Primær sekresjonsforstyrrelse av platelett er derimot en defekt i plateletgranul-sekresjonsmaskineri (veier som ADP/TXA2-signalering og granul-eksocytose). Bevisepakkens egen mekanistiske analyse uttaler eksplisitt at det er **ingen direkte biologisk sammenheng** mellom G-CSF-signalering og plateletgranul-frigjøringsvei. Den høye TxGNN-scoren reflekterer mest sannsynlig en indirekte assosiasjon som er lært fra kunnskapsgrafen — begge konsepter klynges under brede «hematologisk sykdom/hematopoese»-noder — snarere enn en genuin delt mekanisme.

I samsvar med dette er alle 13 kliniske forsøk som er hentet for denne indikasjonen studier av allogeneisk/autolog hematopoietisk stamcelletransplantasjon for ikke-relaterte tilstander (leukemi, lymfom, sarkom, MS, SLE, COVID-19), der Filgrastim/G-CSF vises bare som støtteagent for stamcelle-mobilisering eller post-transplant neutrofil-gjenoppretting — ikke som undersøkelsesbehandling for sekresjonforstyrrelser av platelett. Flere forsøk ble eksplisitt gradering «C» (lav relevans) under vurdering. Denne prediksjonen bør behandles som **hypotesegenerering bare**, ikke som bevis for terapeutisk plausibilitet.

---

## Klinisk forsøksbevis

| Forsøksnummer | Fase | Status | Innrullering | Viktige funn |
|---------|------|------|------|---------|
| [NCT00281879](https://clinicaltrials.gov/study/NCT00281879) | Fase 2 | Avbrutt | 200 | Ikke-relatert donor HSCT for hematologiske maligniteter; G-CSF brukt for stamcelle-mobilisering/neutrofil-gjenoppretting, ikke for plateletforstyrrelser (gradering lav relevans) |
| [NCT00043979](https://clinicaltrials.gov/study/NCT00043979) | Fase 2 | Fullført | 60 | Allogeneisk/syngeneisk HSCT for pediatriske sarkomer; G-CSF som støtteagent bare (gradering lav relevans) |
| [NCT00354172](https://clinicaltrials.gov/study/NCT00354172) | Fase 2 | Avbrutt | 16 | Navlestrengstransplantasjon + NK-celler for myeloid leukemi ikke i remisjon |
| [NCT00923364](https://clinicaltrials.gov/study/NCT00923364) | Fase 2 | Fullført | 19 | Redusert intensitet HSCT for pasienter med GATA2-mutasjoner |
| [NCT02646098](https://clinicaltrials.gov/study/NCT02646098) | Fase 2 | Fullført | 64 | CD34+ valgt vs. ikke-valgt autolog HSCT i MCL/DLBCL; G-CSF brukt for stamcelle-innsamling (gradering lav relevans) |
| [NCT05436418](https://clinicaltrials.gov/study/NCT05436418) | Fase 1/2 | Rekrutterer | 260 | Post-transplant cyclophosphamid + sirolimus/MMF for GVHD-profylakse etter PBSCT |
| [NCT05170828](https://clinicaltrials.gov/study/NCT05170828) | Fase 1 | Trukket | 0 | Kryokonservert HLA-mismatchet ikke-relatert donor benmargtransplantasjon med PTCy |
| [NCT00076752](https://clinicaltrials.gov/study/NCT00076752) | Fase 2 | Fullført | 9 | Autolog HSCT for alvorlig systemisk lupus erythematosus |
| [NCT04540120](https://clinicaltrials.gov/study/NCT04540120) | Fase 2 | Avbrutt | 49 | Dapansutrile (NLRP3-hemmer) for moderat COVID-19/cytokinfrislappelsessyndrom (ikke-relatert til Filgrastim-mekanisme) |
| [NCT06859424](https://clinicaltrials.gov/study/NCT06859424) | Fase 2 | Rekrutterer | 358 | Post-transplant cyclophosphamid-basert GVHD-profylakse i mismatchet ikke-relatert donor PBSCT |

**Ingen av ovennevnte forsøk evaluerer direkte Filgrastim som behandling for sekresjonforstyrrelser av platelett; alle identifiserte bruker er støtte/stamcelle-mobilisering i ikke-relaterte transplantsammenhenger.**

---

## Litteraturbevis

| PMID | År | Type | Journal | Viktige funn |
|------|-----|------|------|---------|
| [29770133](https://pubmed.ncbi.nlm.nih.gov/29770133/) | 2018 | Kohort-studie | Frontiers in Immunology | G-CSF-mobilisering i friske stamcelledonorer mobiliserer preferensielt lymfocytt-undergrupper; adresserer ikke plateletgranul-frigjørelsesnfunksjon |

---

## Norsk markedsinformasjon

Filgrastim er for tiden **ikke markedsført i Norge** (0 autorisasjoner på posten). Ingen produktlisens eller godkjent indikasjonstekst er tilgjengelig i bevisepakken.

---

## Sikkerhetshensyn

Vennligst se pakningsvedlegg for sikkerhetsinformasjon.

> **Viktig flagg**: Bevisepakken markerer TFDA/pakningsvedlegg-advarsler og kontraindikasjoner som et **kritisk datahull** — dette må løses (via TFDA-etikett-henting og parsing) før noen sikkerhetsvurdering (S1) kan fortsette. Legemiddelinteraksjons-data ble også spurt med ingen resultater funnet.

---

## Konklusjon og neste steg

**Beslutning: Avvent**

**Begrunnelse:**
TxGNN-scoren er høy, men bevisepakkens egen mekanistiske og klinisk-forsøksvurdering finner ingen direkte biologisk eller klinisk sammenheng mellom Filgrastims kjente G-CSF-aktivitet og sekresjonforstyrrelser av platelett — alle hentede forsøk bruker Filgrastim bare som støtteagent i ikke-relaterte transplantprotokoller, og bare en løst relatert observasjonsstudie finnes. Kombinert med et kritisk datahull i sikkerhet/etikett-data, oppfyller denne kandidaten ikke terskelen for å gå videre utover signaldeteksjon (S0).

**For å fortsette, er følgende nødvendig:**
- Hent og parse den offisielle TFDA-etiketten for advarsler, kontraindikasjoner, og DDI (kritisk datahull, DG001)
- Innhent bekreftet virkningsmekanisme og godkjent indikasjons-data fra DrugBank (høy-alvorlighet datahull, DG002)
- Søk preklinisk eller mekanistisk bevis direkte som kobler G-CSF/granulocytt-signalering til plateletgranul-sekresjons-veier, hvis en slik hypotese skal forfølges videre
- Revurderes de «ventende» relevans-graderte forsøkene for å bekrefte ingen gir direkte bevis før noen re-evaluering

## Ansvarsfraskrivelse

Dette innholdet er kun til forskningsformål og utgjør ikke medisinsk rådgivning.
Klinisk validering kreves før enhver klinisk anvendelse.

---

