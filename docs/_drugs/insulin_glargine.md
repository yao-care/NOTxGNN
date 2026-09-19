---
layout: default
title: Insulin Glargine
parent: Kun modellprediksjon (L5)
nav_order: 185
evidence_level: L5
indication_count: 10
---

# Insulin Glargine
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

# Insulin glargine: Fra Diabetes Mellitus til Autoimmun Ooforitt

## Oppsummering i en setning

> Insulin glargine er en langvirkende basalinsulinanalog opprinnelig brukt til behandling av Type 1 og Type 2 diabetes mellitus.
> TxGNN-modellen foreslår at det kan være relevant for **Autoimmun Ooforitt**,
> men denne assosiasjonen støttes for tiden av **0 kliniske studier** og **0 publikasjoner**, og ser ut til å reflektere et komorbiditetsmønster snarere enn et direkte behandlingssignal.

---

## Rask oversikt

| Punkt | Verdi |
|-------|-------|
| Originalindikasjon | Diabetes mellitus (Type 1 og Type 2) |
| Forutsagt ny indikasjon | Autoimmun Ooforitt |
| TxGNN-prediksjonspoeng | 99.88% |
| Evidensnivå | L5 |
| Markedsstatus i Norge | ✗ Ikke markedsført |
| Antall godkjennelser | 0 |
| Anbefalt beslutning | Avvent |

---

## Hvorfor er denne prediksjonen rimelig?

For tiden er det ikke tilgjengelig detaljerte data om virkningsmekanisme. Basert på kjent informasjon er insulin glargine en langvirkende rekombinant humaninsulinanalog brukt for å gi basalkontroll av blodsukkernivå ved diabetes; effektiviteten ved Type 1 og Type 2 diabetes er godt etablert, men det er ingen kjent farmakologisk vei som knytter det til ovarial autoimmun vevsødeleggelse.

Ombruksrasjonalen noterer eksplisitt at dette signalet sannsynligvis oppstår fra **samforekomst snarere enn årsakssammenheng**: autoimmun ooforitt forekommer hyppig samtidig med Type 1 diabetes mellitus som en del av Autoimmun polyglandulær syndrom type 2 (APS-2), hvor kunnskapsgrafen kan ha lært sykdom-sykdom-forholdet snarere enn et legemiddel-sykdom-behandlingsforhold.

Fordi insulin regulerer blodsukkernivå og ikke har noen kjent immunomodulatorisk effekt på ovarial autoimmunitet, er den mekanistiske plausibiliteten for denne prediksjonen som et *behandlings*signal lav. Dette bør tolkes som en komorbiditet-artefakt av modellen snarere enn en genuint ombruksmulighet.

---

## Bevis fra kliniske studier

For tiden ingen relaterte kliniske studier registrert

---

## Bevis fra litteratur

For tiden ingen relatert litteratur tilgjengelig

---

## Markedsinformasjon for Norge

Ingen markedsføringstillatelser er for tiden arkivert — markedsstatus i Norge er registrert som **Ikke markedsført**, med 0 totale lisenser.

---

## Sikkerhetshensyn

Venligst se pakningsvedlegget for sikkerhetsinformasjon.

---

## Konklusjon og neste trinn

**Beslutning: Avvent**

**Begrunnelse:**
Denne prediksjonen ligger på laveste bevisnivå (L5) — modellpoeng bare, uten noen støttende kliniske studier eller litteratur. Det underliggende rasjonalet selv flagger assosiasjonen som en sannsynlig komorbiditet-artefakt (via APS-2 samforekomst med T1DM) snarere enn en plausibel kausal behandlingsmekanisme, så det oppfyller ikke kriteriene for å gå videre enn S0.

**For å fortsette, er følgende nødvendig:**
- Uavhengig litteratur eller mekanistisk bevis som direkte knytter insulin (eller insulinsignalveier) til behandling av autoimmun ooforitt, ikke bare diabeteskomorbiditet
- TFDA/regulatorisk etikett data (advarsler, kontraindikasjoner) — for tiden et **blokkerende** datagap (DG001), påkrevd før noen S1-sikkerhetskontroll
- DrugBank-hentet virkningsmekanisme (DG002, Høy alvorlighetsgrad) for riktig å vurdere mekanistisk plausibilitet
- Ekspertvurdering innen endokrinologi/reproduktiv immunologi før ytterligere evaluering

**Merknad om andre kandidater i denne bevissammlingen:** Blant de 10 prediksjoner gitt for insulin glargine, har rangering #6 (**pancreasmangel**) et sterkere mekanistisk grunnlag — pancreasmangel (f.eks. PDX1/PTF1A-defekter) forårsaker absolutt insulinmangel, for hvilket insulinerstatning er standard behandling ved direkte kausal logikk (L4, beslutningsstadium S1, "Forskningsspørsmål"). Dette kan rettferdiggjøre separat evaluering, selv om dens støttende litteratur for tiden er indirekte (generelle T2DM-insulinterapiomtaler og dyrkasuistikker) snarere enn pancreasmangel-spesifikk. Flere andre rangerte elementer (medikament-indusert/sentrifugal/trykk-indusert/idiopatisk lipodystrofi) viser en **omvendt-kausalitetsadvarsel** — insulininjeksjon er en kjent *årsak* til lokalisert lipoatrofi/lipohypertrofi, ikke en behandling for det, og bør flagges som et sikkerhetssignal snarere enn screenet som en ombrukskandidat.

## Ansvarsfraskrivelse

Dette innholdet er kun til forskningsformål og utgjør ikke medisinsk rådgivning.
Klinisk validering kreves før enhver klinisk anvendelse.

---

