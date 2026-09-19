---
layout: default
title: Cetuximab
parent: Kun modellprediksjon (L5)
nav_order: 85
evidence_level: L5
indication_count: 10
---

# Cetuximab
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

# Cetuximab: Fra anti-EGFR onkologiterapi til bronkiale adenomer/karsinoider, barnealder

## Oppsummering i én setning

> Cetuximab er en anti-EGFR-kimerisk monoklonal antistoff; denne evidenspakken inneholder ikke en Taiwan-godkjent indikasjonsfremstilling eller formell MOA-journal (begge flagget som datakløfter), men den innebygde studie-/litteratursammenhengen identifiserer det konsistent som en etablert terapi for EGFR-overeksprimerende plateepitelkarsinom av hode og nakke (HNSCC) og metastatisk kolorektal kreft (mCRC).
> TxGNN-modellens topprangerte prediksjon er **Bronkiale adenomer/karsinoider, barnealder**, men denne kandidaten er for tiden støttet av **0 kliniske studier** og **0 publikasjoner** — det er en ren modellprediksjon (L5).
> To andre kandidater lenger ned på den rangerte listen (**Cystisk neoplasme** og **Premalignt neoplasme**) har meningsfullt sterkere evidens (L2, Research Question-fase) og er oppsummert separat nedenfor.

---

## Rask oversikt

| Punkt | Innhold |
|------|------|
| Opprinnelig indikasjon | Ikke spesifisert i Taiwan-regulatoriske data (ingen lokal markedslisens på fil). Internasjonalt er cetuximab en etablert anti-EGFR-terapi for HNSCC og RAS/BRAF villtype mCRC, som referanser gjennom hele den innebygde studie-/litteratursammenhengen i denne pakken. |
| Predikert ny indikasjon | Bronkiale adenomer/karsinoider, barnealder |
| TxGNN-prediksjonspoengsum | 99.95% |
| Evidensnivå | L5 (kun modellprediksjon, ingen støttestudier) |
| Taiwan markedsstatus | Ikke markedsført (Not marketed) |
| Antall godkjenninger | 0 |
| Anbefalt beslutning | Hold |

---

## Hvorfor er denne prediksjonen rimelig?

For tiden er detaljert virkningsmåtsinformasjon for cetuximab ikke tilgjengelig i denne evidenspakken (datakløft DG002). Basert på bakgrunnskonteksten som er innebygd på tvers av studie- og litteraturbevisene i denne pakken, er cetuximab kjent for å være en kimerisk IgG1-monoklonal antistoff som blokkerer epidermis vekstfaktorreceptor (EGFR), og effektiviteten er etablert i EGFR-overeksprimerende tumorer — først og fremst HNSCC og mCRC — gjennom tiår av studier referanset gjennom dette datasettet (f.eks. NCT00265941, NCT01302834, NCT00056030).

For den topprangerte kandidaten spesifikt er modellens egen begrunnelse eksplisitt at den mekanistiske forbindelsen er **svak**: bronkiale adenomer/karsinoider i barndommen er neuroendokrine tumorer, ikke en typisk EGFR-drevet ondartelse, og barnepopulasjonen mangler sikkerhetdata for cetuximab. Med andre ord er dette tilfellet der en høy TxGNN-likhetsscore ikke tilsvarer en plausibel biologisk mekanisme — prediksjonen bør behandles som kun hypotesegenerering, ikke som en kandidat for videre utvikling på dette tidspunktet.

Derimot viser to kandidater lenger ned på den rangerte listen en meget mer sammenhengende mekanistisk historie i samsvar med cetuximabs kjente EGFR-blokkadeaksjon: **adenoid cystisk karsinom** (innen kategorien «cystisk neoplasme») og **kjemoprevensjon av EGFR-overeksprimerende premalignte øvre aerodigestive lesjoner** (innen kategorien «premalignt neoplasme»). Disse diskuteres i oversiktsseksjonen nedenfor.

---

## Klinisk studie-evidens (topprangerte kandidat: Bronkiale adenomer/karsinoider, barnealder)

For tiden ingen relaterte kliniske studier registrert.

---

## Litteratur-evidens (topprangerte kandidat: Bronkiale adenomer/karsinoider, barnealder)

For tiden ingen relatert litteratur tilgjengelig.

---

## Taiwan markedsinformasjon

Ingen Taiwan-markedsgodkjenninger er på fil for cetuximab i denne evidenspakken (`total_licenses = 0`, `market_status = Not marketed`).

---

## Andre predikerte indikasjoneri denne evidenspakken

Denne evidenspakken inneholder 10 TxGNN-predikerte indikasjoneri for cetuximab, varierende fra L5 (ingen støtteevidenserer) til L2 (fase II-studie + gjennomgangs-nivå litteraturstøtte). For fullstendighet og for å unngå å begrave sterkere signaler, er alle 10 oppsummert nedenfor.

| Rangering | Sykdom | TxGNN poengsum | Evidensnivå | Beslutningsfase | Anbefaling | Studier | Litteratur |
|------|---------|------|------|------|------|------|------|
| 1 | Bronkiale adenomer/karsinoider, barnealder | 99.95% | L5 | S0 | Hold | 0 | 0 |
| 2 | Ikke-seminomatøs lesjon | 99.95% | L5 | S0 | Hold | 0 | 0 |
| 3 | Duktalt eller duktuløst proliferasjon | 99.95% | L4 | S0 | Hold | 0 | 20 |
| 4 | Kondroidt hamartom | 99.95% | L5 | S0 | Hold | 0 | 0 |
| 5 | Tumor av testis og paratestis | 99.95% | L5 | S0 | Hold | 0 | 0 |
| 6 | Odontogen cyste | 99.95% | L4 | S0 | Hold | 0 | 2 |
| 7 | Thyroglossal gangsyste | 99.95% | L5 | S0 | Hold | 0 | 0 |
| **8** | **Cystisk neoplasme** | 99.95% | **L2** | **S2** | **Forskningsspørsmål** | **5** | **20** |
| 9 | Epiglottis neoplasme | 99.95% | L5 | S1 | Forskningsspørsmål | 0 | 0 |
| **10** | **Premalignt neoplasme** | 99.95% | **L2** | **S2** | **Forskningsspørsmål** | **~50** | **2** |

### Bemerkelsesverdig kandidat — Cystisk neoplasme (rangering 8)

Det sterkeste enkeltbeviset i denne pakken er en direkte samsvarende fase I/II-studie for adenoid cystisk karsinom (en «cystisk neoplasme»-undertype):

| Studienummer | Fase | Status | Rekruttering | Viktige funn |
|---------|------|------|------|---------|
| [NCT01192087](https://clinicaltrials.gov/study/NCT01192087) | Fase 1/2 | Ukjent | 49 | ACCEPT-studie: cetuximab + IMRT + karbon-ion-boost for adenoid cystisk karsinom; gradert «A»-relevans i kildeevidensepakken |

Støttelitteratur (RCT/prospektiv evidens prioritert):

| PMID | År | Type | Journal | Viktige funn |
|------|-----|------|------|---------|
| [18804410](https://pubmed.ncbi.nlm.nih.gov/18804410/) | 2009 | Fase II prospektiv studie | Oral Oncology | Cetuximab-monoterapi ved gjentakende/metastatisk spyttkjertelkarsinom (23 adenoid cystisk karsinom-pasienter); klinisk responssats rapportert |
| [18366287](https://pubmed.ncbi.nlm.nih.gov/18366287/) | 2008 | Gjennomgang | Expert Rev Anticancer Ther | Systemisk terapialternativer, inkludert anti-EGFR-agenser, for gjentakende/metastatisk spyttkjertelkarsinom |
| [22144378](https://pubmed.ncbi.nlm.nih.gov/22144378/) | 2013 | Kasusrapport | Head & Neck | Metastatisk adenoid cystisk karsinom som responderer på cetuximab + ukentlig paclitaxel etter paclitaxel-monoterapisvikt |

### Bemerkelsesverdig kandidat — Premalignt neoplasme (rangering 10)

En dedikert enkeltagens fase II-studie eksisterer i høyrisikopremalignte øvre aerodigestive lesjoner, pluss en gjennomgang som direkte adresserer EGFR-målrettet kjemoprevensjon:

| Studienummer | Fase | Status | Rekruttering | Viktige funn |
|---------|------|------|------|---------|
| [NCT00524017](https://clinicaltrials.gov/study/NCT00524017) | Fase 2 | Fullført | 35 | Enkeltagens cetuximab i høyrisiko-premalignte øvre aerodigestive lesjoner |

| PMID | År | Type | Journal | Viktige funn |
|------|-----|------|------|---------|
| [24412287](https://pubmed.ncbi.nlm.nih.gov/24412287/) | 2014 | Gjennomgang | Oral Oncology | EGFR er overeksprimert i orale premalignte lesjoner; diskuterer EGFR-målrettet kjemoprevensjon-rasjonale for HNSCC |

**Viktig forbehold:** som kilderasjonaliseringen bemerker, er flertallet av de ~50 studiene merket til denne kandidaten (f.eks. NCT00956007, NCT05959356, NCT00056030) faktisk rekruttert pasienter med **allerede diagnostisert** HNSCC/CRC i stedet for ekte premalignte lesjoner. Bare NCT00524017 er en genuin kjemoprevensjon-studie. Denne distinksjonen er viktig fordi risiko/nytte-profilen i behandlingspopulasjonen overføres ikke direkte til en kjemoprevensjon-setting.

---

## Cytotoksisitet

Cetuximab er et antineoplastisk middel (anti-EGFR-monoklonal antistoff brukt i HNSCC/mCRC per den innebygde studie-bakgrunnen), så denne seksjonen gjelder.

| Punkt | Innhold |
|------|------|
| Cytotoksisitetsklassifisering | Målrettet terapi (anti-EGFR kimerisk IgG1-monoklonal antistoff) — ikke en konvensjonell cytotoksisk agens |
| Risiko for benmargdepreksjon | Ikke kvantifisert i denne evidenspakken; se vennligst pakningsinlegget for advarsler og forholdsregler |
| Emetogenitets klassifisering | Ikke kvantifisert i denne evidenspakken; se vennligst pakningsinlegget for advarsler og forholdsregler |
| Overvåkingselementer | Infusjonsrelaterte reaksjoner/overfølsomhet (referanset i NCT00896896 «Immunreaktivitet til cetuximab hos kreftpasienter», n=538, og PMID 39415301 alvorlig infusjonsreaksjons-kasusrapport); hudsykdom (referanset i PMID 30141310, hudsykdommer som prognostisk faktor i mCRC) |
| Håndteringsbeskyttelse | Ikke spesifisert i denne evidenspakken (TFDA-merkedata er en blokkerende datakløft, DG001); se vennligst pakningsinlegget |

---

## Sikkerhetshensyn

Se vennligst pakningsinlegget for sikkerhetsinformasjon. Viktige advarsler, kontraindikasjoner og legemiddelinteraksjondata er alle markert som datakløfter i denne evidenspakken (DG001, blokkerende alvorlighetsgrad), og ingen DDI-poster ble funnet (`query_status: not_found`).

---

## Konklusjon og neste trinn

**Beslutning: Hold**

**Begrunnelse:**
Den topprangerte TxGNN-prediksjonen (bronkiale adenomer/karsinoider, barnealder) har null støttekliniske studier eller litteratur og er eksplisitt flagget av modellens egen begrunnelse som mekanistisk implausibel (ikke-EGFR-drevet neuroendokrin tumor, ingen pediatrisk sikkerhetdata). Denne kandidaten oppfyller ikke terskelen for videre evaluering på dette tidspunktet.

**For å gå videre er det nødvendig med følgende:**
- Løs DG001 (blokkering): få TFDA-merkeadvarsler/kontraindikasjoner før S1-sikkerhetskjerning kan gjennomføres
- Løs DG002 (høy): få formell DrugBank MOA-journal for å ordentlig evaluere mekanistisk plausibilitet på tvers av alle 10 kandidater
- Hvis repurposing-arbeid forfølges for dette legemidlet, omdirigerer oppmerksomheten til de to evidensstøttede kandidatene identifisert i denne pakken — **Cystisk neoplasme** (adenoid cystisk karsinom, L2/Forskningsspørsmål, fase I/II-studie + fase II prospektiv litteratur) og **Premalignt neoplasme** (EGFR-kjemoprevensjon, L2/Forskningsspørsmål, dedikert fase II-studie) — i stedet for den topprangerte men evidensfrie kandidaten

## Ansvarsfraskrivelse

Dette innholdet er kun til forskningsformål og utgjør ikke medisinsk rådgivning.
Klinisk validering kreves før enhver klinisk anvendelse.

---

