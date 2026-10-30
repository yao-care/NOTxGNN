---
layout: default
title: Temsirolimus
parent: Kun modellprediksjon (L5)
nav_order: 407
evidence_level: L5
indication_count: 3
last_modified_at: 2026-10-30
description: "Temsirolimus: predikert ny indikasjon Liposarkom (evidensnivå L5). Opprinnelig indikasjon: Nyrecellekarsinom"
monitor_inn: "TEMSIROLIMUS"
predicted_indications: ["liposarcoma", "ovarian myxoid liposarcoma", "vulva sarcoma"]
---

# Temsirolimus
{: .fs-9 }

Evidensnivå: **L5** | Predikerte indikasjoner: **3** stk.
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

## Temsirolimus: Fra nyrecellekarsinom og mantelcellelymfom til liposarkom
{: .text-alpha }

## Oppsummering i én setning

Temsirolimus er en mTOR-hemmer som opprinnelig er godkjent for behandling av nyrecellekarsinom og mantelcellelymfom.
TxGNN-modellen forutsier at legemidlet kan ha effekt på **liposarkom**,
og foreløpig finnes det **2 kliniske studier** (begge ikke spesifikke for liposarkom) og **1 publikasjon** (en oversiktsartikkel) som peker i denne retningen.

---

## Hurtigoversikt

| Punkt | Innhold |
|------|------|
| Opprinnelig indikasjon | Nyrecellekarsinom; mantelcellelymfom |
| Predikert ny indikasjon | Liposarkom |
| TxGNN-prediksjonsscore | 0,9954 |
| Evidensnivå | L5 (etter tildelt nivå i de kompilerte dataene; se merknad under kliniske studier) |
| Markedsstatus i Norge | Markedsført (gyldige tillatelser: 1 av 1) |
| Antall godkjenninger | 1 (gyldige: 1) |
| Antall tillatelser | 1 (avregistrert) |
| Anbefalt beslutning | Hold |

---

## Hvorfor er denne prediksjonen rimelig?

Detaljerte data om virkningsmekanisme (MOA) er ikke tilgjengelige i de kompilerte dataene. Temsirolimus er imidlertid et velkjent rapamycin-analog og en mTOR-hemmer, og effekten er dokumentert ved nyrecellekarsinom og mantelcellelymfom.

PI3K/AKT/mTOR-signalveien er ofte aktivert i bløtvevssarkomer, inkludert liposarkom. Ved velddifferensierte og dedifferensierte liposarkomer er dessuten MDM2/CDK4-amplifikasjon knyttet til krysskommunikasjon med PI3K/mTOR-signalering. Dette gir et plausibelt biologisk grunnlag for mTOR-hemming.

Den høye TxGNN-scoren (0,9954) er i samsvar med dette resonnementet, men er utelukkende en beregningsmessig prediksjon og ikke bevis for klinisk effekt.

Prediksjonene for to ytterligere, svært sjeldne sarkomtyper (ovarielt myksoid liposarkom, score 0,9947, og vulvasarkom, score 0,9909) har ingen støtte i studier eller litteratur og er vurdert som «Hold».

---

## Klinisk evidens

| Studienummer | Fase | Status | Antall deltakere | Hovedfunn |
|---------|------|------|------|---------|
| [NCT00949325](https://clinicaltrials.gov/study/NCT00949325) | Fase 1/2 | Fullført | 24 | Temsirolimus + liposomal doksorubicin ved avanserte bløtvevs- og beinsarkomer; undersøker sikker dosering og foreløpig effekt. Ikke spesifikk for liposarkom (relevans B). |
| [NCT01614795](https://clinicaltrials.gov/study/NCT01614795) | Fase 2 | Fullført | 46 | Cixutumumab (IGF-1R-antistoff) + temsirolimus hos barn med tilbakevendende/refraktære solide svulster og sarkomer. Indirekte relevans for voksne med liposarkom (relevans C). |

**Merknad:** Ingen av studiene er liposarkom-spesifikke, og ingen resultater er oppgitt. Evidensnivået L2 bør derfor tolkes med forsiktighet; i praksis er støtten svakere enn nivået tilsier.

---

## Litteraturevidens

| PMID | År | Type | Tidsskrift | Hovedfunn |
|------|-----|------|------|---------|
| [20497911](https://pubmed.ncbi.nlm.nih.gov/20497911/) | 2010 | Oversiktsartikkel | Bulletin du cancer | Gjennomgang av målrettet behandling av sjeldne bindevevssvulster og sarkomer, basert på molekylære undergrupper av sarkomer. |

---

## Informasjon om det norske markedet

| Tillatelsesnummer | Produktnavn | Legemiddelform | Godkjent indikasjon |
|---------|------|------|-----------|
| EMEA/H/C/000799 | Torisel | Ikke oppgitt | Nyrecellekarsinom; mantelcellelymfom (status: godkjent) |

---

## Cytotoksisitet

| Punkt | Innhold |
|------|------|
| Klassifisering | Målrettet behandling (mTOR-hemmer) |
| Risiko for myelosuppresjon | Se pakningsvedlegg for advarsler og forsiktighetsregler |
| Emetogenisitet | Se pakningsvedlegg for advarsler og forsiktighetsregler |
| Overvåkingspunkter | Blodstatus (CBC), lever- og nyrefunksjon, blodsukker og lipider (jf. de registrerte kontraindikasjonskoblingene under) |
| Håndteringsbeskyttelse | Følg gjeldende retningslinjer for håndtering av cytostatika/antineoplastiske legemidler |

---

## Sikkerhetsvurderinger

Offisielle advarsler og kontraindikasjoner fra preparatomtalen mangler i de kompilerte dataene. Følgende er hentet fra kunnskapsgrafen (PrimeKG) og er ikke teksten fra preparatomtalen:

- **Kontraindikasjoner i kunnskapsgrafen**: nyresykdom, leversykdom, galleblæresykdom, hyperglykemi, diabetes mellitus, diabetisk ketoacidose, hyperlipidemi (inkl. familiær), hjerneslag/cerebrovaskulær sykdom, hjerneinfarkt, hyperbilirubinemi (inkl. Gilberts syndrom), interstitiell lungesykdom, samt flere hjernesvulster (blant annet astrocytomer, glioblastom og oligodendrogliale svulster).
- **Legemiddelinteraksjoner** (100 registrert; utvalg av de viktigste):
  - **Alvorlige (Major)**: amfotericin B (inkl. lipidkompleks), deksametason, klaritromycin.
  - **Moderate**: blant annet kortikosteroider (hydrokortison, triamcinolon, betametason, budesonid), antidiabetika (acarbose, metformin, pioglitazon, alogliptin, albiglutid, kanagliflozin, dapagliflozin, klorpropamid), aprepitant, cimetidin, mesalazin og balsalazid.

---

## Konklusjon og neste steg

**Beslutning: Hold**

**Begrunnelse:**
Det biologiske grunnlaget (mTOR-signalering i sarkomer) er plausibelt og TxGNN-scoren er høy, men det finnes ingen liposarkom-spesifikke studier eller resultater. I tillegg er den eneste norske/europeiske tillatelsen avregistrert, og sikkerhetsdata fra preparatomtalen mangler.

**For å gå videre kreves følgende:**
- Hente og analysere preparatomtalen (advarsler og kontraindikasjoner), som er en blokkerende datamangel for sikkerhetsvurdering.
- Supplere data om virkningsmekanisme (MOA), for eksempel fra DrugBank.
- Undersøke om det finnes en liposarkom-undergruppe i resultatene fra NCT00949325.
- Vurdere den kliniske relevansen av de to studiene og innhente flere publikasjoner som er spesifikke for liposarkom.
- Avklare markedsstatus og tilgjengelighet i Norge, siden tillatelsen er avregistrert.
- Vurdere interaksjonsrisiko (spesielt CYP3A4-relaterte, f.eks. klaritromycin og deksametason) og metabolske risikoer i aktuell pasientgruppe.
## Ansvarsfraskrivelse

Dette innholdet er kun til forskningsformål og utgjør ikke medisinsk rådgivning.
Klinisk validering kreves før enhver klinisk anvendelse.

---

