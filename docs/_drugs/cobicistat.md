---
layout: default
title: Cobicistat
parent: Kun modellprediksjon (L5)
nav_order: 103
evidence_level: L5
indication_count: 3
last_modified_at: 2026-10-15
description: "Cobicistat: predikert ny indikasjon Simian immunsviktvirus-infeksjon (evidensnivå L5). Opprinnelig indikasjon: Hiv-infeksjon"
monitor_inn: "COBICISTAT"
predicted_indications: ["simian immunodeficiency virus infection", "feline acquired immunodeficiency syndrome", "neurodevelopmental disorder with ataxic gait, absent speech, and decreased cortical white matter"]
---

# Cobicistat
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

# Kobicistat: Fra hiv-infeksjon til simian immunsviktvirus-infeksjon

## Oppsummering i én setning

Kobicistat er en farmakokinetisk forsterker (booster) som opprinnelig brukes i behandling av hiv-infeksjon, og som i seg selv ikke har antiviral effekt. TxGNN-modellen forutsier at legemidlet kan være effektivt mot **simian immunsviktvirus-infeksjon**, men det finnes **ingen kliniske studier** og **ingen publikasjoner** i de sammenstilte dataene som støtter denne prediksjonen.

---

## Hurtigoversikt

| Punkt | Innhold |
|------|------|
| Opprinnelig indikasjon | Hiv-infeksjon |
| Predikert ny indikasjon | Simian immunsviktvirus-infeksjon |
| TxGNN-prediksjonsscore | 99,92 % |
| Evidensnivå | L5 |
| Markedsstatus i Norge | Kun opphevede (kansellerte) godkjenninger |
| Antall godkjenninger | 6 (alle kansellerte) |
| Anbefalt beslutning | Hold |

---

## Hvorfor er denne prediksjonen rimelig?

Detaljerte data om virkningsmekanisme er ikke tilgjengelige i datagrunnlaget. Basert på kjent informasjon er kobicistat en mekanismebasert hemmer av CYP3A og brukes til å øke blodnivået av andre antiretrovirale legemidler. Legemidlet har ingen egen antiviral aktivitet.

Simian immunsviktvirus (SIV) hos ikke-menneskelige primater er en veterinærmedisinsk og prekliniske modell for hiv, som er legemidlets opprinnelige indikasjon. Den høye TxGNN-scoren gjenspeiler trolig nærhet til hiv i kunnskapsgrafen (begge er lentivirus) snarere enn en ny terapeutisk mekanisme.

Enhver bruk ville måtte skje som booster for et antiretroviralt partnerlegemiddel. Dette er en sykdom i en modellorganisme og ikke et reelt repurposing-mål hos mennesker.

### Andre prediksjoner i datagrunnlaget

| Rang | Predikert sykdom | TxGNN-score | Evidensnivå | Vurdering |
|------|------|------|------|------|
| 2 | Felint ervervet immunsviktsyndrom (FIV, veterinær) | 99,92 % | L5 | Hold. Samme resonnement som over: ingen direkte antiviral effekt, kun mulig boosterrolle. |
| 3 | Nevroutviklingsforstyrrelse med ataktisk gange, fravær av tale og redusert kortikal hvit substans | 99,91 % | L5 | Hold. Ingen mekanistisk sammenheng identifisert; scoren kan være et grafartefakt. |

---

## Klinisk studieevidens

Foreløpig finnes det ingen relaterte kliniske studier registrert.

---

## Litteraturevidens

Foreløpig finnes det ingen relatert litteratur.

---

## Informasjon om det norske markedet

Alle godkjenninger er kansellerte. Oppføringene under er de som er kompilert for denne rapporten.

| Godkjenningsnummer | Produktnavn | Doseringsform | Godkjent indikasjon |
|---------|------|------|-----------|
| EMEA/H/C/002572 | Tybost | – | Hiv-infeksjon |
| EMEA/H/C/003904 | Evotaz | – | Hiv-infeksjon |
| EMEA/H/C/002819 | Rezolsta | – | Hiv-infeksjon |
| EMEA/H/C/004042 | Genvoya | – | Hiv-infeksjon |
| EMEA/H/C/002574 | Stribild | – | Hiv-infeksjon |

*Ytterligere én kansellert godkjenning (Symtuza, EMEA/H/C/004391) er ikke vist i tabellen.*

---

## Sikkerhetsvurderinger

- **Legemiddelinteraksjoner**: Det er registrert 100 interaksjoner i datagrunnlaget. Et utvalg av de mest alvorlige (nivå «Major»):
  - Loperamid
  - Triamcinolon
  - Cisaprid
  - Budesonid

  Mange interaksjoner på nivå «Moderate» gjelder blant annet kortikosteroider (hydrokortison, deksametason, betametason), aprepitant, klotrimazol, klaritromycin, metoklopramid og repaglinid. Interaksjonene skyldes i hovedsak kobicistats hemming av CYP3A.

For øvrig sikkerhetsinformasjon, se preparatomtalen (pakningsvedlegget).

---

## Konklusjon og neste steg

**Beslutning: Hold**

**Begrunnelse:**
Prediksjonen er kun modellbasert (L5) uten støtte fra kliniske studier eller litteratur. Kobicistat har ingen egen antiviral effekt, og de predikerte indikasjonene er enten veterinære/modellorganismer eller uten identifisert mekanistisk sammenheng. I tillegg er alle norske godkjenninger kansellert, og legemidlet har et stort interaksjonsbyrde.

**For å gå videre trengs følgende:**
- Informasjon om advarsler og kontraindikasjoner fra preparatomtalen (blokkerende datagap for sikkerhetsscreening)
- Detaljerte data om virkningsmekanisme (MOA)
- Prekliniske eller kliniske data som viser en reell terapeutisk verdi utover boosting av partnerlegemidler
- Avklaring av om en veterinær- eller modellorganisme-indikasjon er relevant for repurposing-formålet
- Avklaring av markedsstatus og tilgjengelighet i Norge, siden alle godkjenninger er kansellert
## Ansvarsfraskrivelse

Dette innholdet er kun til forskningsformål og utgjør ikke medisinsk rådgivning.
Klinisk validering kreves før enhver klinisk anvendelse.

---

