---
layout: default
title: Lumacaftor
parent: Kun modellprediksjon (L5)
nav_order: 218
evidence_level: L5
indication_count: 1
---

# Lumacaftor
{: .fs-9 }

Evidensnivå: **L5** | Predikerte indikasjoner: **1** stk.
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

# Lumacaftor: Fra cystisk fibrose til spedalskhet

## Sammenfatting i ett setning

Lumacaftor er en CFTR-proteinfoldingkorreksjonsmiddel, opprinnelig brukt til behandling av cystisk fibrose (brukt sammen med ivacaftor, slik som Orkambi, egnet for pasienter med F508del-CFTR-mutasjoner).
TxGNN-modellen forutsier at det kan være effektivt for **spedalskhet (Leprosy)**, men det finnes for tiden **ingen kliniske forsøk eller litteraturbeviser** for denne retningen, og bevisnivået er det laveste L5.

---

## Hurtigoversikt

| Element | Innhold |
|---------|---------|
| Opprinnelig indikasjon | Cystisk fibrose (kombinert bruk av ivacaftor, slik som Orkambi) |
| Forutsagt ny indikasjon | Spedalskhet (Leprosy) |
| TxGNN-prediksjonsresultat | 99.44% |
| Bevisnivå | L5 (kun modellprediksjon, ingen faktisk forskningsstøtte) |
| Taiwan-markedsstatus | Not marketed |
| Antall godkjenningsbevis | 0 |
| Anbefalt beslutning | Hold (utsett) |

---

## Hvorfor er rimeligheten til denne prediksjonen tvilsom?

Selv om Lumacaftor offisielt har MOA-feltet markert som datakløft ([Data Gap]), basert på kjent farmakologisk informasjon er Lumacaftor en CFTR-proteinfoldingkorreksjonsmiddel som forbedrer intracellulær transport og funksjon av F508del-CFTR-mutantproteinet gjennom molekylchaperon-lignende virkning, og er klinisk godkjent kun i kombinasjon med ivacaftor (slik som Orkambi) til behandling av cystisk fibrose.

Patogenesen av spedalskhet er kronisk granulomatøs inflammasjon og perifer nerveskade forårsaket av *Mycobacterium leprae*-infeksjon, og det finnes for tiden ingen kjent bevis som viser biologisk sammenheng mellom CFTR-proteinfoldning eller kloridjonionekanal-funksjon og denne patogenetiske prosessen.

Den høye poengsum gitt av TxGNN (0.994) reflekterer sannsynligvis indirekte koblinger i kunnskapsgrafen (for eksempel stoff–gen–sykdom-sameksistenssti), snarere enn en patogenetisk hypotese med biologisk rimelighet. I fravær av noen litteraturbeviser eller forsøk, bør mekanismenes rimelighet av denne prediksjonen anses som **tvilsom**, og det kreves manuell gjennomgang før man avgjør om man skal investere videre ressurser.

---

## Klinisk forsøksbeviser

For tiden ingen relevante kliniske forsøk registrert

---

## Litteraturbeviser

For tiden ingen relevant litteraturdata

---

## Taiwan-markedsinformasjon

Legemidlet er for tiden **ikke markedsført i Taiwan**, og det er ingen godkjenningsbeviser tilgjengelig for opplistning.

---

## Sikkerhetshensyn

Se produktinformasjonen for sikkerhetsinformasjon.

(Merknad: Produktinformasjonsadvarsel og kontraindikasjon er for tiden datakløfter på blokkernivå, og du må først oppnå offisiell TFDA-produktinformasjon før du kan utføre S1-sikkerhetsvurdering.)

---

## Konklusjon og neste trinn

**Beslutning: Hold (utsett)**

**Begrunnelse:**
Selv om TxGNN-prediksjonsscore er høyt, mangler det helt kliniske forsøk og litteraturbeviser (L5), og på mekanismenivå (CFTR-proteinfoldingkorreksjon vs. mykobakteriell infeksiøs granulomatøs sykdom) er det ingen kjent biologisk sammenheng, og mekanismenes rimelighet er tvilsom. Dessuten er produktinformasjonsadvarsel og kontraindikasjon fortsatt datakløfter på blokkernivå, og S1-sikkerhetsvurdering kan ikke utføres ennå.

**For å fortsette fremover, må følgende fylles ut:**
- Offisiell TFDA produktinformasjon advarsel/kontraindikasjon (DG001, Blocking, må lastes ned og analyseres)
- Fullstendig DrugBank MOA-data for å bekrefte mekanismekorrelasjoner (DG002, High)
- Preklinisk mekanismeforskning på om CFTR-modulatorer har antimykobakteriell eller immunmodulatorisk effekt
- Resultat av manuell gjennomgang av mekanismenes rimelighet, som grunnlag for vurdering av hvorvidt man skal gå til neste fase (S1)

## Ansvarsfraskrivelse

Dette innholdet er kun til forskningsformål og utgjør ikke medisinsk rådgivning.
Klinisk validering kreves før enhver klinisk anvendelse.

---

