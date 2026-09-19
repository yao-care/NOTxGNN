---
layout: default
title: Aliskiren
parent: Kun modellprediksjon (L5)
nav_order: 24
evidence_level: L5
indication_count: 7
---

# Aliskiren
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

# Aliskiren: Fra hypertensjon til pulmonær hypertensjon på grunn av lungesykdom og/eller hypoksemi

*Merk: evidenspakken inneholder ingen `original_indications`-tekst og ingen norske lisenspostinger for aliskiren, så "original indikasjon" nedenfor er angitt fra legemidlets kjente farmakologiske klasse (direkte renin-hemmer, indisert for essensiell hypertensjon), ikke fra pakkdata.*

## En-setnings sammendrag

Aliskiren er en direkte renin-hemmer opprinnelig utviklet for essensiell hypertensjon. TxGNN-modellen forutsier at det kan være effektivt for **pulmonær hypertensjon på grunn av lungesykdom og/eller hypoksemi**, men denne retningen støttes for øyeblikket kun av modellens score — **0 kliniske forsøk** og ingen av de **20 hentede publikasjonene** studerer faktisk aliskiren, RAAS-hemming eller pulmonær hypertensjon. Dette er et rent algoritmisk signal, ikke et legemiddel-spesifikt funn.

## Raskt overblikk

| Element | Innhold |
|------|------|
| Original indikasjon | Essensiell hypertensjon (fra kjent legemiddelklasse; ikke til stede i evidenspakken — ingen `original_indications` eller norsk lisensstekst oppgitt) |
| Forutsagt ny indikasjon | Pulmonær hypertensjon på grunn av lungesykdom og/eller hypoksemi |
| TxGNN prognose-score | 99.98% |
| Evidensnivå | L5 (kun modellprognose) |
| Markedsstatus i Norge | ✗ Ikke markedsført |
| Antall godkjenninger | 0 |
| Anbefalt avgjørelse | Avvent |

## Hvorfor er denne prognosen rimelig?

For øyeblikket er detaljerte virkningsmekanisme-data ikke tilgjengelig (merket som alvorlig datakløft, DG002). Basert på kjent farmakologi er aliskiren en direkte renin-hemmer (DRI) som blokkerer det hastighetsbestemmende trinnet i renin-angiotensin-aldosteron-systemet (RAAS), og dens effektivitet ved essensiell hypertensjon er vel etablert.

Den teoretiske koblingen til pulmonær hypertensjon er at kronisk hypoksemi kan lokalt aktivere RAAS og fremme pulmonær vaskulær remodellering, som i prinsippet kunne gjøre renin-hemming til et plausibelt intervensjonssted. Dette er en biologisk sammenhengende hypotese, ikke en som er bekreftet.

Kritisk sett nevner ingen av de 20 litteraturpostene som ble returnert for denne paringen aliskiren, RAAS-hemmere eller behandling av pulmonær hypertensjon — de er generell hypoksemi-biologi og neurodegenersjon-litteratur (f.eks. høyfjells-fysiologi, kognitiv svikt under hypoksemi, tumor hypoksemi-signalering). Heller ingen kliniske forsøk ble identifisert. TxGNN-scoren gjenspeiler derfor en rent graf-basert assosiasjon, uten legemiddel-spesifikk mekanistisk eller klinisk bekrefting i den nåværende evidenspakken.

## Klinisk forsøk-evidens

For øyeblikket ingen relaterte kliniske forsøk registrert.

## Litteratur-evidens

Alle 20 hentede publikasjoner handler om hypoksemi-biologi generelt og **adresserer ikke spesifikt aliskiren, RAAS-hemming eller pulmonær hypertensjon**. De er oppført nedenfor for åpenhet, prioritert etter gjennomgangs-type klassifisering (ingen RCT-er ble returnert):

| PMID | År | Type | Journal | Hovedfunn |
|------|-----|------|------|---------|
| [33862277](https://pubmed.ncbi.nlm.nih.gov/33862277/) | 2021 | Gjennomgang | Ageing Research Reviews | Hypoksemis doble rolle i neurodegenersjon vs. potensiell neuroproteksjon ved høyfjell/i sykdom; ingen legemiddel-spesifikt innhold |
| [34618295](https://pubmed.ncbi.nlm.nih.gov/34618295/) | 2022 | Gjennomgang | Metabolic Brain Disease | Mekanismer for kognitiv svikt under akutt vs. kronisk hypoksemi |
| [21328446](https://pubmed.ncbi.nlm.nih.gov/21328446/) | 2011 | Gjennomgang | Journal of Cellular Biochemistry | Generell hypoksemi-mediiert biologisk kontroll (metabolisme, angiogenese, sykdom) |
| [11172576](https://pubmed.ncbi.nlm.nih.gov/11172576/) | 2000 | Gjennomgang | Respiratory Care Clinics of North America | Mekanismer for hypoksemi (V/Q misforhold, shunt, hypoventilasjon) — generell respiratorisk fysiologi |
| [34535359](https://pubmed.ncbi.nlm.nih.gov/34535359/) | 2021 | Gjennomgang | Clinical Oncology | Terapeutisk modifisering av tumor-hypoksemi (radioterap-resistans-sammenheng) |
| [31961750](https://pubmed.ncbi.nlm.nih.gov/31961750/) | 2020 | Gjennomgang | Annual Review of Immunology | HIF-veiens rolle i medfødt immunitet/inflammasjon |
| [28219680](https://pubmed.ncbi.nlm.nih.gov/28219680/) | 2017 | Gjennomgang | Experimental Cell Research | Transkripsjons-undertrykkings-mekanismer under hypoksemi (HIF-regulering) |
| [40347693](https://pubmed.ncbi.nlm.nih.gov/40347693/) | 2025 | Gjennomgang | Redox Biology | Hypoksemis rolle i multippel sklerose-patologi |
| [27146279](https://pubmed.ncbi.nlm.nih.gov/27146279/) | 2017 | Gjennomgang | Cephalalgia | Hypoksemi-mekanismer i primære hodepine-lidelser |
| [36100192](https://pubmed.ncbi.nlm.nih.gov/36100192/) | 2022 | Gjennomgang | Journal of Controlled Release | Tumor hypoksemi-assosiert nanomedisinn-strategier |

*10 av 20 postinger vist (prioritert etter Gjennomgang-klassifisering); de gjenstående 10 er lavere-kategori/ukategorisert ("ventende") postinger om urelatert hypoksemi-tematikk (f.eks. kreft HIF-signalering, cerebral anoksi-caseberetninger) og legger til ingen ytterligere relevans.*

## Markedsinformasjon Norge

Aliskiren har for øyeblikket **ingen markedsføringstillatelse i Norge** (status: Ikke markedsført; 0 lisenser på fil). Ingen produkt, doseringsform eller godkjent-indikasjon-data er tilgjengelig fra norske regulatoriske poster.

## Sikkerhetshensyn

Se pakningsvedlegget for sikkerhetsinformasjon. Merk at evidenspakken flagger TFDA/merkat-ekvivalente advarsler og kontraindikasjoner som en **blokkerings**-datakløft (DG001) — dette forhindrer kandidaten fra å gå inn i S1 sikkerhetsvurderingsstadiet, uavhengig av effektivitets-evidensen diskutert ovenfor.

## Konklusjon og neste trinn

**Avgjørelse: Avvent**

**Begrunnelse:**
TxGNN-scoren er høy, men støtte-evidensen er L5 (kun modellprognose) — det er ingen kliniske forsøk og ingen litteratur som faktisk studerer aliskiren, RAAS-hemming eller pulmonær hypertensjon. Kombinert med en blokkerings-datakløft på sikkerhet/merkat-data og fravær av markedstilstedeværelse i Norge, er det ingen grunnlag for å fremme denne indikasjon-paringen utover hypotetisk fase.

**For å gå videre, er følgende nødvendig:**
- TFDA-ekvivalent pakningsvedlegg-data (advarsler, kontraindikasjoner) for å rydde blokkerings-datakløften (DG001) og tillate inngang til S1 sikkerhetsvurderingsstadiet
- Detaljert virkningsmekanisme-dokumentasjon (DG002) for å substansiere RAAS–hypoksemi–pulmonær vaskulær remodellering-rasjonalet
- Aliskiren- eller RAAS-hemmer-spesifikke pre-kliniske eller kliniske studier i pulmonær hypertensjon (ingen eksisterer for øyeblikket i den hentede litteraturen)
- Til kontekst: evidenspakken lister også 6 andre forutsatt indikasjon for aliskiren med vesentlig ulik evidens-profiler — spesielt "cerebrovaskulær lidelse" (L2, inkluderer ALTITUDE-forsøk post-hoc data), selv om denne evidensen viser en *økt* risiko for slag/hypotensjon med aliskiren + ACEI/ARB kombinasjons-terapi snarere enn fordel, og bør gjennomgås som et sikkerhet-signal, ikke en ombruk-mulighet, før noen videre handling på dette legemidlet

## Ansvarsfraskrivelse

Dette innholdet er kun til forskningsformål og utgjør ikke medisinsk rådgivning.
Klinisk validering kreves før enhver klinisk anvendelse.

---

