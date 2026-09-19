---
layout: default
title: Prasterone
parent: Kun modellprediksjon (L5)
nav_order: 286
evidence_level: L5
indication_count: 10
---

# Prasterone
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

# Prasterone: Fra uspesifisert original indikasjon til Heparin Cofactor 2-mangel

## Oppsummering i en setning

> Prasterone (DHEA, DB01708) er en adrenalt steroidhormonforløper; ingen godkjent indikasjondata er tilgjengelige i denne bevissamlingen, og legemidlet markedsføres ikke for tiden i Norge.
> TxGNN-modellens topprediksjon er **Heparin Cofactor 2-mangel**, men denne kandidaten har **ingen støttende kliniske forsøk eller litteratur**, og den foreslåtte mekanismen strider mot kjent androgenfarmakologi.

---

## Hurtigoversikt

| Objekt | Innhold |
|--------|---------|
| Original indikasjon | Ikke dokumentert i bevissamlingen (ingen lisens-/indikasjonsposter tilgjengelig) |
| Forutsagt ny indikasjon | Heparin Cofactor 2-mangel |
| TxGNN-prediksjonspoengsum | 99.99% (rangering 223 av fullstendig sykdomsliste) |
| Bevisnivå | L5 (modellprediksjon kun, ingen klinisk eller litteraturstøtte) |
| Norges markedsstatus | ✗ Ikke markedsført |
| Antall godkjenninger | 0 |
| Anbefalt beslutning | Pausert |

---

## Hvorfor er denne prediksjonen rimelig?

For tiden er detaljerte virkningsmekanismedata ikke tilgjengelige for prasterone. Basert på kjent farmakologisk klassifisering er prasterone (DHEA) en adrenal steroidhormonforløper som konverteres perifert til androgener og østrogener; dette klassifiseringsnivåfaktet er ikke spesifikt nok til å etablere en mekanistisk sammenheng til heparin cofactor II-mangel.

Heparin cofactor II-mangel er en arvelig tilstand der det terapeutiske målet er å **gjenopprette antikoagulantaktivitet**. Androgener er imidlertid generelt forbundet med **pro-koagulanteffekter** — økt syntese av koagulasjonsfaktorer og redusert naturlig antikoagulantaktivitet (et mønster som også gjenspeiles i denne samme bevissamlingens andre topprediksjoner, som antithrombin-mangel og protein S-mangel, alle flagget med samme retningspregte bekymring). Dette plasserer den forutsagte indikasjonen i mekanistisk konflikt med legemidlets kjente farmakologi snarere enn som støtte for den.

Gitt fraværet av noen kliniske forsøk, publisert litteratur, eller dokumentert MOA som forbinder prasterone til denne sykdommen, rangeres dette som en ren nettverkstopologi-prediksjon (L5) med et plausibelt biologisk argument *mot* effektivitet snarere enn for den.

---

## Klinisk forsøksbeviser

For tiden ingen beslektede kliniske forsøk registrert.

---

## Litteraturbeviser

For tiden ingen beslektet litteratur tilgjengelig.

---

## Norges markedsinformasjon

Prasterone har for tiden **ingen markedsføringsgodkjenninger i Norge** (markedsstatus: Ikke markedsført; totale godkjenninger: 0). Ingen lisensdata er tilgjengelig for oppsummering.

---

## Sikkerhetshensyn

Vennligst se pakningsvedlegget for sikkerhetsinformasjon. (Merk: TFDA/etikett-advarsler og kontraindikasjonsdata er for tiden utilgjengelige — se datahull nedenfor.)

---

## Konklusjon og neste trinn

**Beslutning: Pausert**

**Begrunnelse:**
Topprangerte prediksjon (heparin cofactor 2-mangel) har null klinisk eller litteraturbevis, og dens foreslåtte farmakologi er i konflikt med androgeners kjente pro-koagulantegenskaper, noe som gjør det biologisk usannsynlig i sin nåværende form. Kombinert med manglende MOA- og sikkerhetsetikett-data, oppfyller denne kandidaten ikke kravet for å gå videre forbi S0.

**For å gå videre er følgende nødvendig:**
- TFDA/etikett-advarsler og kontraindikasjoner (blokkerende hull — kreves før S1-sikkerhetsvurdering)
- Bekreftet virkningsmekanismedata fra DrugBank eller primærlitteratur
- Eksperimentell eller klinisk evidens for DHEA-effekt på heparin cofactor II / antithrombin / protein S-aktivitet, gitt sikkerhetskonsernet som er reist ovenfor
- Vurder å nedprioritere denne høyest rangerte kandidaten: innenfor samme prediksjonsgruppe har **skleroderm (rangering 7)** sterkere biologisk begrunnelse (L4-bevis, 6 observasjonsstudier som konsekvent viser DHEA-S-mangel korrelert med sykdomsalvorsgrad, beslutningsstadium S1 "Research Question") og kan være en mer produktiv kandidat å forfølge videre.

## Ansvarsfraskrivelse

Dette innholdet er kun til forskningsformål og utgjør ikke medisinsk rådgivning.
Klinisk validering kreves før enhver klinisk anvendelse.

---

