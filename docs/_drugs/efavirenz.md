---
layout: default
title: Efavirenz
parent: Kun modellprediksjon (L5)
nav_order: 120
evidence_level: L5
indication_count: 3
---

# Efavirenz
{: .fs-9 }

Evidensnivå: **L5** | Predikerte indikasjoner: **3** stk.
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

# Efavirenz: Fra HIV-1-infeksjon til Simian Immunodeficiency Virus-infeksjon

## Sammenfatting i én setning

Efavirenz er en ikke-nukleosid revers transkriptase-inhibitor (NNRTI) etablert for behandling av HIV-1-infeksjon (reflektert konsekvent gjennom den støttende litteraturen, selv om det ikke er eksplisitt oppført i denne bevissamlingen).
TxGNN-modellen predikerer at det kan være relevant for **Simian Immunodeficiency Virus (SIV)-infeksjon**,
men bevisgrunnlaget består nesten utelukkende av **prekliniske makakmodellstudier (16 publikasjoner)** og en eneste **trukket tilbake, null påmelding prøve**, uten bekreftet menneskelig klinisk utvikling for denne spesifikke indikasjonen.

## Rask oversikt

| Element | Innhold |
|---------|---------|
| Original indikasjon | HIV-1-infeksjon (utledet fra konsekvent litteraturkontekst; ikke eksplisitt fanget i `taiwan_regulatory` data) |
| Predikert ny indikasjon | Simian immunodeficiency virus-infeksjon |
| TxGNN-prediksjonspoengsum | 99.80% |
| Bevisnivå | L4 (kun prekliniske/mekanistiske studier) |
| Markedsstatus i Norge | Ikke markedsført |
| Antall autorisasjoner | 0 |
| Anbefalt beslutning | Hold |

## Hvorfor er denne prediksjonen rimelig?

Detaljerte data om virkningsmekanisme er ikke tilgjengelig i denne bevissamlingen (`original_moa: [Data Gap]`). Basert på den støttende litteraturen er efavirenz en velkarakterisert NNRTI som hemmer HIV-1-revers transkriptase, og dens kliniske bruk for HIV-1-infeksjon er veletablert i den bredere litteraturkonteksten som følger med denne bevissamlingen.

Den predikerte indikasjonen, "simian immunodeficiency virus-infeksjon," er ikke en menneskesykdom — SIV er primatanalogen av HIV som brukes for å konstruere den RT-SHIV-kimeriske virusmodellen (SIV-rygg med HIV-1-revers transkriptase innsatt) spesielt slik at HIV-målrettede NNRTIer som efavirenz kan testes i ikke-menneskelige primater. Mekanistisk sett er dette koherent: fordi efavirenz sitt mål (HIV-1 RT) bevisst er konstruert inn i RT-SHIV-viruset, er efavirenz farmakologisk aktivt mot det. Dette representerer imidlertid en **forskning/dyremodell-bruksfall snarere enn en ny menneskelig terapeutisk indikasjon**, og bør ikke tolkes som en ny klinisk omposisjonering-mulighet i konvensjonell forstand.

Det er verdt å merke seg at den andre-rangerte prediksjonen ("felin ervervede immunmangelssyndrom," dvs. FIV i katter) viser samme mønster — reelle efavirenz-inneholdende HIV-prøver (f.eks. ATRIPLA i NCT01263015) vises i bevissettet, men bare fordi ATRIPLA er det menneskelige sammenligningslegemiddelet i prøver av *urelaterte* eksperimentelle forbindelser (dolutegravir/GSK1349572), ikke på grunn av en FIV-spesifikk menneskelig studie.

## Klinisk prøvebevis

| Prøvenummer | Fase | Status | Påmelding | Viktige funn |
|---------|------|------|------|---------|
| [NCT00863668](https://clinicaltrials.gov/study/NCT00863668) | NA | Trukket tilbake | 0 | Studie av HIV/SIV virusnedbrytin gskinetikk med integrase-inhibitor raltegravir i ikke-menneskelige primater; trukket tilbake med null påmelding, hvilket ikke gir brukbare effektivitetsdata for efavirenz spesielt |

## Litteraturbevis

| PMID | År | Type | Journal | Viktige funn |
|------|-----|------|------|---------|
| [35856680](https://pubmed.ncbi.nlm.nih.gov/35856680/) | 2022 | Preklinisk (NHP-modell) | Antimicrob Agents Chemother | Massespectrometrisk avbildning av antiretroviral (inkl. efavirenz) vevsdistribusjon kontra viral RNA og fibrose i RT-SHIV-infiserte primat-milter |
| [24777106](https://pubmed.ncbi.nlm.nih.gov/24777106/) | 2014 | Preklinisk (NHP-modell) | Antimicrob Agents Chemother | Forbedret HAART-regimer med 4-5 legemidler forbedrer RT-SHIV-virusnedbrytin gskinetikk hos rhesus-makaker |
| [24505452](https://pubmed.ncbi.nlm.nih.gov/24505452/) | 2014 | Preklinisk (NHP-modell) | PLoS One | Karakteriserer residuell viremi og mangel på virusevolusjon i RT-SHIV-makak HAART-modell |
| [26559632](https://pubmed.ncbi.nlm.nih.gov/26559632/) | 2015 | Preklinisk (NHP-modell) | Retrovirology | Velblandede plasma/vevs virale populasjoner i RT-SHIV-makaker antyder ingen pågående vevreplikasjon under ART |
| [22933296](https://pubmed.ncbi.nlm.nih.gov/22933296/) | 2012 | Preklinisk (NHP-modell) | J Virol | Ultrafølsom PCR detekterer pre-eksisterende legemiddelresistente RT-SHIV-varianter i makaker før ART |
| [21084490](https://pubmed.ncbi.nlm.nih.gov/21084490/) | 2011 | Preklinisk (NHP-modell) | J Virol | Genetisk mangfold av RT-SHIV vedvarer i makaker til tross for efavirenz-inneholdende ART |
| [21289110](https://pubmed.ncbi.nlm.nih.gov/21289110/) | 2011 | Preklinisk (mekanistisk) | J Virol | Gag-Pol/klathrin-interaksjonsstudie i HIV-1 og relaterte primat-lentiviruser |
| [20032180](https://pubmed.ncbi.nlm.nih.gov/20032180/) | 2010 | Preklinisk (NHP-modell) | J Virol | Identifiserer virale fristed som vedvarer under HAART i RT-SHIV-makak AIDS-modellen |
| [20668516](https://pubmed.ncbi.nlm.nih.gov/20668516/) | 2010 | Preklinisk (NHP-modell) | PLoS One | Virusnedbrytin gskinetikk karakterisert i HAART-behandlet RT-SHIV-makak-modell |
| [19889213](https://pubmed.ncbi.nlm.nih.gov/19889213/) | 2009 | Preklinisk (NHP-modell) | Retrovirology | RT-SHIV-subpopulasjons dynamikk i makaker under kortkurs efavirenz-monoterapi etterfulgt av kombinasjons-ART |

*Ytterligere publikasjoner (f.eks. PMID 15328115, 15564466, 15919889, 19195672, 15040537, 17045247) gir videre støtte til RT-SHIV/efavirenz-makakmodellen men er utelatt her av korthetshensyn.*

## Informasjon om det norske markedet

Ingen autorisasjonsdata for markedsføring er tilgjengelig — efavirenz er for øyeblikket **ikke markedsført** i denne rettsordenen (`total_licenses: 0`).

## Sikkerhetshensyn

Vennligst se pakningsvedlegget for sikkerhetsinformasjon. (Alle sikkerhetsfelt i denne bevissamlingen — viktige advarsler, kontraindikasjoner og legemiddelinteraksjoner — er for øyeblikket datalakuner.)

## Konklusjon og neste trinn

**Beslutning: Hold**

**Begrunnelse:**
Den høyest-rangerte predikerte indikasjonen ("simian immunodeficiency virus-infeksjon") er en dyremodell-sykdom snarere enn en menneskelig klinisk indikasjon, og den eneste tilknyttede kliniske prøven ble trukket tilbake med null påmelding. Bevisnivå L4 (kun preklinisk), kombinert med en **Blokkering**-datalakune på TFDA/merketikett-sikkerhetsinformasjon og manglende MOA-data, betyr at denne kandidaten ikke er klar for videre evaluering.

**For å fortsette kreves følgende:**
- Løs DG001 (Blokkering): få offisielle merketikett-advarsler/kontraindikasjoner før S1 sikkerhetskontroll
- Løs DG002: få formelle MOA-data fra DrugBank for å støtte mekanistisk begrunnelse
- Klargjør den faktiske menneske-relevante indikasjonen som blir målrettet — de nåværende "SIV-infeksjon" og "felin AIDS"-prediksjoner reflekterer ikke-menneskelige forskningsmodeller, ikke omposisjonerbare menneskesykdommer; kjør eller kartlegg TxGNN-utgang på nytt mot et menneskesykdom-ontologi-filter
- Bekreft reell-verdens markedsføring/regulatorisk status, siden 0 autorisasjoner for øyeblikket er på fil

## Ansvarsfraskrivelse

Dette innholdet er kun til forskningsformål og utgjør ikke medisinsk rådgivning.
Klinisk validering kreves før enhver klinisk anvendelse.

---

