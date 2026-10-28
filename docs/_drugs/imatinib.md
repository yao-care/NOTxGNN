---
layout: default
title: Imatinib
parent: Kun modellprediksjon (L5)
nav_order: 209
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-15
description: "Imatinib: predikert ny indikasjon Hjertefibrosarkom (heart fibrosarcoma) (evidensnivå L4). Opprinnelig indikasjon: Akutt lymfatisk leukemi (prekursor-B-celle), dermatofibrosarkom…"
monitor_inn: "IMATINIB"
predicted_indications: ["heart fibrosarcoma", "fibroblastic neoplasm", "conventional fibrosarcoma", "kidney fibrosarcoma", "low grade fibromyxoid sarcoma", "liposarcoma", "liver fibrosarcoma", "autosomal recessive familial Mediterranean fever", "ovarian myxoid liposarcoma", "familial rhabdoid tumor"]
---

# Imatinib
{: .fs-9 }

Evidensnivå: **L5** | Predikerte indikasjoner: **10** stk.
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

## Imatinib: Fra kronisk myelogen leukemi til hjertefibrosarkom (heart fibrosarcoma)
{: .text-alpha }

## Oppsummering

Imatinib er en tyrosinkinasehemmer som opprinnelig brukes mot kronisk myelogen leukemi (BCR-ABL-positiv), akutt lymfatisk leukemi, gastrointestinale stromale svulster (GIST), dermatofibrosarcoma protuberans og beslektede sykdommer.
TxGNN-modellen predikerer at imatinib kan ha effekt mot **hjertefibrosarkom**, men for denne indikasjonen finnes **ingen kliniske studier** og bare **1 publikasjon** (en oversiktsartikkel), så støtten er svak.

Merk: Blant de ti predikerte indikasjonene i datagrunnlaget har flere sterkere støtte enn rang 1. Disse omtales under «Øvrige predikerte indikasjoner».

---

## Hurtigoversikt

| Punkt | Innhold |
|------|------|
| Opprinnelig indikasjon | Akutt lymfatisk leukemi (prekursor-B-celle), dermatofibrosarkom, myelodysplastiske/myeloproliferative sykdommer, kronisk myelogen leukemi (BCR-ABL-positiv), hypereosinofilt syndrom (GIST for Glivec) |
| Predikert ny indikasjon | Hjertefibrosarkom (heart fibrosarcoma) |
| TxGNN-prediksjonsscore | 0.9994 |
| Evidensnivå | L5 |
| Markedsstatus i Norge | Markedsført (gyldige tillatelser: 3 av 3) |
| Antall godkjenninger | 3 (gyldige: 3) |
| Anbefalt beslutning | Hold |

---

## Hvorfor er denne prediksjonen rimelig?

Data om virkningsmekanisme (MOA) er ikke tilgjengelig i datagrunnlaget. Basert på kjent informasjon hemmer imatinib tyrosinkinasene BCR-ABL, KIT og PDGFR. Dens effekt ved flere sykdommer med disse kinasene som drivere er godt dokumentert.

Fibrosarkomlignende svulster, særlig dermatofibrosarcoma protuberans (DFSP) med COL1A1-PDGFB-fusjon, er avhengige av PDGFB/PDGFR-signalering. Det gir en plausibel mekanisme på klassenivå. Det finnes imidlertid ingen hjertespesifikke data, og prediksjonen for hjertefibrosarkom er derfor i hovedsak modellbasert.

---

## Dokumentasjon fra kliniske studier

Currently no related clinical trials registered for heart fibrosarcoma. Det finnes ingen registrerte kliniske studier knyttet til denne prediksjonen.

---

## Litteraturdokumentasjon

| PMID | År | Type | Tidsskrift | Hovedfunn |
|------|-----|------|------|---------|
| [18623899](https://pubmed.ncbi.nlm.nih.gov/18623899/) | 2008 | Oversikt | Prescrire international | Gjennomgang av nye imatinib-indikasjoner. Konkluderer med at bevisene for utvidede indikasjoner ikke er robuste. Ph+ ALL: høyere hematologisk respons enn kjemoterapi i en studie med 55 pasienter. |

---

## Øvrige predikerte indikasjoner

| Rang | Sykdom | Score | Evidensnivå | Anbefaling | Kommentar |
|------|------|------|------|------|------|
| 2 | Fibroblastisk neoplasme (inkl. DFSP) | 0,9994 | L5 | Proceed with Guardrails | DFSP er allerede en godkjent indikasjon. Støttes av europeisk retningslinje (2024) og flere oversikter. Ingen studier i datagrunnlaget, så reell evidens er trolig sterkere enn L4. |
| 3 | Konvensjonelt fibrosarkom | 0,9993 | L5 | Forskningsspørsmål | Litteraturen handler mest om DFSP. Konvensjonelt fibrosarkom mangler vanligvis fusjonen, så ekstrapolering er indirekte. |
| 4 | Nyrefibrosarkom | 0,9993 | L5 | Hold | Kun en basket-studie fase 2 (NCT00154388, n=185) uten nyrespesifikke data. |
| 5 | Lavgradig fibromyxoid sarkom | 0,9993 | L5 | Hold | Kun prediksjon. Drives av FUS-CREB3L2, ikke PDGFR/KIT. |
| 6 | Liposarkom | 0,9988 | L2 | Forskningsspørsmål | Tre fase 1/2-studier i bløtdelssarkom, men ingen subtypespesifikke resultater. |
| 7 | Leverfibrosarkom | 0,9986 | L5 | Hold | Kun indirekte litteratur (GIST, DRESS-tilfelle). |
| 8 | Autosomal recessiv familiær middelhavsfeber | 0,9986 | L5 | Hold | Kun prediksjon, ingen mekanistisk begrunnelse. |
| 9 | Ovarielt myxoid liposarkom | 0,9985 | L5 | Hold | Kun prediksjon. Drives av FUS-DDIT3. |
| 10 | Familiær rhabdoid tumor | 0,9983 | L5 | Hold | Kun prediksjon. SMARCB1-tap, ingen kjent kobling til imatinibs mål. |

### Kliniske studier for relaterte indikasjoner

| Studienummer | Fase | Status | Antall deltakere | Hovedfunn |
|---------|------|------|------|---------|
| [NCT00154388](https://clinicaltrials.gov/study/NCT00154388) | Fase 2 | Fullført | 185 | Utforskende basket-studie av imatinib ved livstruende sjeldne maligne sykdommer med imatinibfølsomme tyrosinkinaser. |
| [NCT00031915](https://clinicaltrials.gov/study/NCT00031915) | Fase 2 | Fullført | Ikke oppgitt | Imatinib ved metastatisk eller ikke-operabelt bløtdels- og beinsarkom. |
| [NCT00006357](https://clinicaltrials.gov/study/NCT00006357) | Fase 1/2 | Fullført | 91 | Doseringsstudie og fase 2 av imatinib (STI571) ved avansert bløtdelssarkom. |

### Utvalgt litteratur for relaterte indikasjoner

| PMID | År | Type | Tidsskrift | Hovedfunn |
|------|-----|------|------|---------|
| [19451433](https://pubmed.ncbi.nlm.nih.gov/19451433/) | 2009 | Fase 2-studie | J Clin Oncol | Multisenterstudie av imatinib i 10 histologiske sarkomsubtyper med bayesiansk hierarkisk modell. |
| [39904126](https://pubmed.ncbi.nlm.nih.gov/39904126/) | 2025 | Retningslinje | Eur J Cancer | Oppdatert europeisk tverrfaglig retningslinje for diagnostikk og behandling av DFSP. |
| [42062942](https://pubmed.ncbi.nlm.nih.gov/42062942/) | 2026 | Kohortstudie | BMC Cancer | 153 kinesiske DFSP-pasienter: Mohs-kirurgi med postoperativ imatinib. |
| [25852058](https://pubmed.ncbi.nlm.nih.gov/25852058/) | 2015 | Prekliniske data | Mol Cancer Ther | CDK4 som mål ved imatinibresistent DFSP. Imatinib gir klinisk nytte hos ca. 50 % med ikke-operabel/metastatisk DFSP. |
| [36999599](https://pubmed.ncbi.nlm.nih.gov/36999599/) | 2023 | Oversikt | J Surg Oncol | Kirurgi er førstevalg ved DFSP. Imatinib kan brukes ved avansert eller ikke-operabel sykdom. |
| [30096127](https://pubmed.ncbi.nlm.nih.gov/30096127/) | 2018 | Kasuistikk | Anti-Cancer Drugs | Imatinibindusert DRESS hos pasient med DFSP, håndtert med desensibilisering. |

---

## Informasjon om det norske markedet

| Godkjenningsnummer | Produktnavn | Doseringsform | Godkjent indikasjon |
|---------|------|------|-----------|
| EMEA/H/C/000406 | Glivec (Novartis Europharm) | Ikke oppgitt | Akutt lymfatisk leukemi, GIST, dermatofibrosarkom, myelodysplastiske/myeloproliferative sykdommer, kronisk myelogen leukemi, hypereosinofilt syndrom |
| EMEA/H/C/002681 | Imatinib Accord (Accord Healthcare) | Ikke oppgitt | Akutt lymfatisk leukemi, dermatofibrosarkom, myelodysplastiske/myeloproliferative sykdommer, kronisk myelogen leukemi, hypereosinofilt syndrom |
| EMEA/H/C/002585 | Imatinib Teva (Teva B.V.) | Ikke oppgitt | Kronisk myelogen leukemi, akutt lymfatisk leukemi, myelodysplastiske/myeloproliferative sykdommer, hypereosinofilt syndrom, dermatofibrosarkom |

Legemidlet er markedsført i Norge, og 3 av 3 godkjenninger (markedsføringstillatelser) er gyldige.

---

## Cytotoksisitet

| Punkt | Innhold |
|------|------|
| Cytotoksisitetsklassifisering | Målrettet terapi (tyrosinkinasehemmer) |
| Myelosuppresjonsrisiko | Se pakningsvedlegg for advarsler og forsiktighetsregler. Kontraindikasjonsdata fra kunnskapsgrafen nevner nøytropeni, trombocytopeni, anemi og agranulocytose, som indikerer behov for hematologisk overvåking. |
| Emetogenisitet | Se pakningsvedlegg for advarsler og forsiktighetsregler |
| Overvåkingspunkter | Blodstatus (CBC), lever- og nyrefunksjon, væskeretensjon/hjertefunksjon |
| Håndteringsbeskyttelse | Følg lokale retningslinjer for håndtering av cytostatika/antineoplastiske legemidler |

---

## Sikkerhetsbetraktninger

Pakningsvedleggets advarsler og kontraindikasjoner mangler i de data som er sammenstilt for denne rapporten. Se pakningsvedlegget for fullstendig sikkerhetsinformasjon.

**Sykdomstilstander knyttet til kontraindikasjon i kunnskapsgrafen (PrimeKG, ikke preparatomtale):** hypertensjon, leversvikt/leversykdom, nyresykdom, trombocytopeni, nøytropeni, agranulocytose, anemi, hjertesvikt, koronarsykdom, hjerteklaffsykdom, perikardeffusjon, medfødt hjertesykdom, hjerneødem, lungeødem, diabetes mellitus, diabetisk ketoacidose, fedme, hyperbilirubinemi (inkl. Gilberts syndrom), aktivt magesår, galleblæresykdom, hypofosfatemi og pyoureter. Dette er kunnskapsgrafsignaler og må verifiseres mot preparatomtalen.

**Legemiddelinteraksjoner (DDInter, 100 registrert totalt):** Utvalget viser hovedsakelig moderate interaksjoner, blant annet med kortikosteroider (hydrokortison, deksametason, betametason, triamcinolon, budesonid), pioglitazon, glimepiride, saksagliptin, aprepitant, morfin, cimetidin, klaritromycin, lansoprazol/deksansoprazol, naltrekson, naldemedin og metreleptin. **Alvorlige (Major)** interaksjoner er registrert med **eliglustat** og **naloxegol**.

**Annet sikkerhetssignal:** Ett kasus med imatinibindusert DRESS (legemiddelreaksjon med eosinofili og systemiske symptomer) er beskrevet.

---

## Konklusjon og neste steg

**Beslutning: Hold** (for hjertefibrosarkom). For fibroblastisk neoplasme/DFSP er anbefalingen i datagrunnlaget Proceed with Guardrails.

**Begrunnelse:**
- For hjertefibrosarkom finnes ingen kliniske studier og bare én generell oversiktsartikkel, så støtten er hovedsakelig modellbasert (L4). Den mest troverdige repurposingretningen er DFSP/fibroblastiske neoplasmer, der imatinib allerede har godkjent indikasjon og retningslinjestøtte.

**For å gå videre trengs følgende:**
- Pakningsvedleggets advarsler og kontraindikasjoner (kritisk datamangel som blokkerer sikkerhetsscreening)
- Data om virkningsmekanisme (MOA) fra DrugBank
- Avklaring av norsk markedsstatus: legemidlet er markedsført, og alle 3 godkjenninger er gyldige
- Kliniske data eller kasuistikker for hjerte- og fibrosarkomsubtyper, samt subtypespesifikke resultater fra basket- og bløtdelssarkomstudiene
- Sikkerhetsplan for pasienter med hjerte-, lever- og nyresykdom og for interaksjoner med eliglustat og naloxegol
## Ansvarsfraskrivelse

Dette innholdet er kun til forskningsformål og utgjør ikke medisinsk rådgivning.
Klinisk validering kreves før enhver klinisk anvendelse.

---

