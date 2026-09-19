---
layout: default
title: Leflunomide
parent: Kun modellprediksjon (L5)
nav_order: 203
evidence_level: L5
indication_count: 2
---

# Leflunomide
{: .fs-9 }

Evidensnivå: **L5** | Predikerte indikasjoner: **2** stk.
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

# Leflunomid: Fra DMARD/Immunmodulator til brachydactyly-syndactyly-syndrom

## Oppsummering i en setning

> Leflunomid er en kjent dihydroorotatdehydrogenase (DHODH)-hemmer som brukes klinisk som et sykdomsmodifiserende antirevmatisk legemiddel (DMARD) / immunmodulator; dens spesifikke opprinnelige indikasjonsetikett er ennå ikke tilgjengelig i dette datasettet.
> TxGNN-modellen forutsier at det kan være effektivt for **brachydactyly-syndactyly-syndrom**, en sjelden utviklingsbetonget lemmeforstyrrelse,
> men denne forutsigelsen er for tiden støttet av **0 kliniske forsøk** og **0 publikasjoner** — det er et signal kun fra modellens utdata uten uavhengig mekanistisk, forsøks- eller litteraturbekreftelse.

---

## Hurtigoversikt

| Element | Innhold |
|---------|---------|
| Opprinnelig indikasjon | Ikke tilgjengelig i gjeldende datasett (legemiddel er en kjent DHODH-hemmer / DMARD-immunmodulator per mekanistiske notater; formell indikasjonsetikett venter) |
| Forutsagt ny indikasjon | Brachydactyly-syndactyly-syndrom |
| TxGNN-forutsigelsesscore | 99.93% |
| Bevissnivå | L5 |
| Markedsstatus | Ikke markedsført |
| Antall godkjenninger | 0 |
| Anbefalt beslutning | Avvent |

---

## Hvorfor er denne forutsigelsen rimelig?

For tiden er detaljerte virkningsmekanisme-data for leflunomid merket som en datakløft i denne bevissamlingen. Basert på generelt kjent farmakologi som er referert i modellens egne begrunnede notater, hemmer leflunomid dihydroorotatdehydrogenase (DHODH), og undertrykker dermed pyrimidinsyntese og lymfocyttproliferasjon — dette er grunnlaget for dens etablerte bruk som en immunmodulatorisk DMARD.

Brachydactyly-syndactyly-syndrom er imidlertid en sjelden medfødt lemmeforstyrrelse, typisk forårsaket av mutasjoner i utviklings-mønstergivende gener som *HOXD* eller *GLI3*. Det er ingen kjent overlapping mellom DHODH/pyrimidinsyntese-hemmelse og de utviklings-genveiene som er implisert i dette syndromet.

Ombuksgrunnlaget for denne kandidaten uttaler eksplisitt at **ingen mekanistisk lenke kan etableres** — forutsigelsen reflekterer en høyt-scorende kunnskapsgraff-assosiasjon fra TxGNN-algoritmen alene, uten støtte fra biologisk plausibilitet. Dette bør behandles som et hypotesegenererende signal alene, ikke som bevis for terapeutisk relevans.

---

## Klinisk forsøksbevis

For tiden ingen relaterte kliniske forsøk registrert.

---

## Litteraturbevis

For tiden ingen relatert litteratur tilgjengelig.

---

## Markedsinformasjon for Norge

Leflunomid har for tiden ingen markedsføringsmyndighetsgjodkjenninger registrert (0 lisenser; markedsstatus: Ikke markedsført). Ingen produkttabell er tilgjengelig.

---

## Sikkerhetshensyn

Se pakningsvedlegget for sikkerhetsinformasjon.

---

## Konklusjon og neste trinn

**Beslutning: Avvent**

**Begrunnelse:**
Denne kandidaten er støttet kun av et L5 (modellforutsigelse-kun) bevissnivå, uten kliniske forsøk eller litteratur identifisert, og ombuksgrunnlaget selv uttaler at ingen mekanistisk plausibilitet kunne etableres mellom leflunomids kjente DHODH-hemming og patologien i brachydactyly-syndactyly-syndrom. Kombinert med en alvorlighetsgrad-blokkering datakløft på TFDA-etikettadvarsler/kontraindikasjoner, kan denne kandidaten ikke fortsette til sikkerhetsforscreening (S1).

**For å fortsette, trengs følgende:**
- TFDA-etikett (advarsler/kontraindikasjoner) — påkrevd før noen S1-sikkerhets-evaluering (DG001, Blokkering)
- Bekreftet virkningsmekanisme-data fra DrugBank (DG002, Høy)
- Uavhengig mekanistisk eller preklinisk grunnlag som forbinder DHODH/pyrimidinsyntese-hemmelse til lemmeuvtiklingsforstyrelser
- Eventuell ny klinisk forsøks- eller kasuistikk-litteratur for denne indikasjonen

---

*Merknad: En andre kandidat-indikasjon, colobomatous microphthalmia-rhizomelic dysplasia-syndrom (TxGNN-score 99.93%, rang 1084), bærer samme L5-bevissnivå, null forsøks-/litteratur-støtte og en tilsvarende «ingen mekanistisk lenke etablert»-konklusjon. Det anbefales på samme måte for Avvent inntil de samme datakløftene ovenfor er dekket.*

## Ansvarsfraskrivelse

Dette innholdet er kun til forskningsformål og utgjør ikke medisinsk rådgivning.
Klinisk validering kreves før enhver klinisk anvendelse.

---

