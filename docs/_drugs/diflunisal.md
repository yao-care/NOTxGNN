---
layout: default
title: Diflunisal
parent: Kun modellprediksjon (L5)
nav_order: 109
evidence_level: L5
indication_count: 10
---

# Diflunisal
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

# Diflunisal: Fra NSAID-antiinflammatorisk smertestillende middel til ankylosing spondylitt (Ankylosing Spondylitis)

> **Utvalgsforklaring**: De høyeste TxGNN-scoringene i Evidence Pack, kandidatene rangert 1–4 og 6–9 (som acromesomelic dysplasia, brachyolmia osv.), er alle ekstremt sjeldne genetiske bein-/strukturelle sykdommer, og hver enkelt `repurposing_rationale` angir allerede tydelig at mekanismen ikke holder stikk, det finnes ingen klinisk evidens, dette er støy i kunnskapsgrafen (L5/S0/Hold). Denne rapporten fokuserer på den eneste kandidaten med vesentlig litteraturbevis — **ankylosing spondylitt** — som hovedevalueringsobjekt (rangering 10, inflammatory spondylopathy, tilhører samme sykdomsspektrum, beviser overlapper, forklares sammen).

## Én-setnings sammendrag

Diflunisal sin opprinnelig godkjent indikasjon mangler taiwansk regulatorisk dokumentasjon i denne Evidence Pack (ingen tillatelser registrert i `taiwan_regulatory.licenses`). TxGNN-modellen forutsier at det kan være effektivt for **ankylosing spondylitt**, men litteraturgjennomgangen viser at denne sammenhengen **ikke er nytt legemiddelrepurposing**, men heller eksisterende klinisk bruk innenfor NSAID-medikasjonsklassen; for tiden finnes det **0 kliniske forsøk**, **7 relaterte litteraturkilder** (hvorav kun 3 er direkte studier av diflunisal, 1 er RCT) som støtter denne retningen.

## Rask oversikt

| Emne | Innhold |
|------|---------|
| Original indikasjon | Datakluft (`taiwan_regulatory.licenses` er tom, ingen godkjent indikasjon kan fastslås) |
| Forutsagt ny indikasjon | Ankylosing Spondylitis (ankylosing spondylitt) |
| TxGNN forutsigelsesscore | 99.98% (rangering 373) |
| Evidensnivå | L2 (1 fullført RCT av fase 2/3 nivå, 1986) |
| Taiwansk markedsstatus | Ikke markedsført |
| Antall lisenser | 0 |
| Anbefalt beslutning | **Hold** |

## Hvorfor denne forutsigelsen er rimelig

Det finnes for tiden ingen detaljerte mekanisme-data fra DrugBank (`original_moa` er datakluft). Basert på eksisterende litteratur og `repurposing_rationale`-beskrivelser av samme kandidater, tilhører diflunisal NSAID-familien (ikke-steroide antiinflammatoriske legemidler), et salicylsyrederivat, antatt mekanisme konsistent med samme klasse NSAID: hemmer syklooksygenase (COX-1/COX-2), reduserer prostaglandinsyntese, oppnår antiinflammatorisk og smertestillende effekt.

Ankylosing spondylitt er en inflammatorisk sykdom som påvirker wirvelsøylen og andre ledd. NSAID er en av **standardbehandlingsmedikamentklassene** for denne tilstanden. Med andre ord er forholdet funnet av TxGNN i hovedsak en gjenbekreftelse av allerede etablert NSAID-farmakologi og eksisterende klinisk bruk, **ikke en oppdagelse av helt nye repurposing-muligheter** — dette punktum er allerede tydelig merket i Evidence Pack `repurposing_rationale` ("tilhører eksisterende klinisk bruk av legemiddel (ikke nytt repurposing)").

Det er verdt å merke seg at den støttende litteraturen kun inneholder 3 artikler (PMID 3524970, 4062389, 3546687) som er direkte studier av diflunisal selv hos AS-pasienter (alle fra 1985–1986 fra samme forskergruppe, prøvestørrelse ca. 33–38 personer), de øvrige 4 litteraturkildene (diclofenac, naproxen, pirprofen review) diskuterer **andre NSAID-legemidler** effektivitet ved AS, som tilhører legemiddelklasse-nivå-bevis, ikke bevis spesielt for diflunisal, tolkning bør skille disse.

## Klinisk forsøksbevis

Det finnes for tiden ingen relaterte kliniske forsøksregistreringer (`clinical_trials` er en tom matrise).

## Litteraturbevis

| PMID | År | Type | Journal | Viktig funn |
|------|-----|------|---------|---------|
| [3524970](https://pubmed.ncbi.nlm.nih.gov/3524970/) | 1986 | RCT | Clinical Rheumatology | 38 mannlige AS-pasienter, 12 ukers dobbeltblindet randomisert forsøk som sammenlignet diflunisal (500mg bid) med fenylbutazon (200mg bid), begge kunne forbedre alvorlighetsgraden av AS-symptomer, diflunisal viste raskere initial smertelindring og mer fremtredende effekt, med opprettholdelse av virkning over 36 uker i åpen periode |
| [4062389](https://pubmed.ncbi.nlm.nih.gov/4062389/) | 1985 | Kohorte | Annals of the Rheumatic Diseases | Samme kohorte av 38 AS-pasienter (behandlet med diflunisal eller fenylbutazon) fulgt i 48 uker; serum IgA-konsentrasjon var korrelert med thorakale ekspansjonsgrad og lumbal fleksjon indeks, pasienter med mer alvorlige røntgenforandringer hadde høyere IgA |
| [3546687](https://pubmed.ncbi.nlm.nih.gov/3546687/) | 1986 | Kohorte | The Journal of Rheumatology | 33 AS-pasienter som blindet randomisert mottok diflunisal eller fenylbutazon behandling i 12 uker (utvidet til 48 uker), vurderte forholdet mellom lungefunksjon (VC), sykdomsaktivitet og NSAID-behandling |
| [2670397](https://pubmed.ncbi.nlm.nih.gov/2670397/) | 1989 | Gjennomgang | Clinical Pharmacy | Diclofenac (ikke diflunisal) farmakologisk gjennomgang, klassifiserer som samme NSAID-klasse bevis for revmatologiske sykdommer |
| [6772422](https://pubmed.ncbi.nlm.nih.gov/6772422/) | 1980 | Gjennomgang | Drugs | Diclofenac ved revmatologiske sykdommer (inkludert AS) farmakologi og terapeutisk bruk gjennomgang, ikke direkte bevis for diflunisal |
| [387372](https://pubmed.ncbi.nlm.nih.gov/387372/) | 1979 | Gjennomgang | Drugs | Naproxen ved revmatologisk behandling gjennomgang, ikke direkte bevis for diflunisal |
| [3539573](https://pubmed.ncbi.nlm.nih.gov/3539573/) | 1986 | Gjennomgang | Drugs | Pirprofen farmakodynamikk/farmakokinetikk gjennomgang, nevner som mulig alternativ behandling for AS og andre revmatologiske sykdommer, ikke direkte bevis for diflunisal |

## Taiwansk markedsinformasjon

Diflunisal er for tiden **ikke markedsført på Taiwan** (`market_status: Not marketed`), ingen lisensregistreringer finnes (`total_licenses: 0`), og derfor kan merkenavn, doseringsform og godkjent indikasjon ikke oppgis.

## Sikkerhetshensyn

Nøkkeladvarslene og kontraindikasjoner i Evidence Pack er alle merket som datakluft, medikasjonsinteraksjonsspørring gir ingen resultater (`query_status: not_found`).

Vennligst se forskriving/pakningsvedlegg for sikkerhetsinformasjon.

> ⚠️ Spesiell merknad: `DG001` (DMP pakningsvedlegg advarsler/kontraindikasjoner) i metadataene er merket som **Blocking**-nivå datakluft, tydelig angir «Cannot proceed to S1 safety screening», dette er hovedgrunnen til at denne saken ikke kan påbegynnes direkte.

## Konklusjon og påfølgende anbefalinger

**Beslutning: Hold**

**Grunn:**
- Selv om ankylosing spondylitt har 1 liten (n=38) RCT fra 1986 som støtter diflunisal effektivitet (L2 evidensnivå), er denne sammenhengen i hovedsak en gjenbekreftelse av allerede kjent NSAID-klassebruk, ikke en virkelig ny repurposing-oppdagelse, tilleggsverdi er begrenset.
- Mer kritisk er at DMP pakningsvedlegg advarsler/kontraindikasjoner data er **Blocking**-nivå datakluft, i henhold til reglen «Cannot proceed to S1 safety screening», denne datakluft bør utfylles før noen beslutning skal tas.
- Legemiddel er ikke markedsført på Taiwan (0 lisenser), ingen DDI-spørringsresultater foreligger heller, sikkerhetsinformasjon er alvorlig mangelfull totalt sett.

**For å kunne gå videre, må man utfylle:**
- TFDA forskriving PDF-nedlasting og analyse (DG001, Blocking, kilde: DMP website)
- DrugBank handlingsmekanisme (MOA) data-spørring (DG002, High, kilde: DrugBank API)
- Hvis påfølgende evaluering av ankylosing spondylitt retning, må man bekrefte om det allerede er dekket i diflunisal andre lands eksisterende indikasjon, for å avklare om denne saken virkelig utgjør «legemiddelrepurposing» eller heller eksisterende bruk utvidelse

## Ansvarsfraskrivelse

Dette innholdet er kun til forskningsformål og utgjør ikke medisinsk rådgivning.
Klinisk validering kreves før enhver klinisk anvendelse.

---

