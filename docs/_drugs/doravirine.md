---
layout: default
title: Doravirine
parent: Kun modellprediksjon (L5)
nav_order: 131
evidence_level: L5
indication_count: 3
last_modified_at: 2026-10-15
description: "Doravirine: predikert ny indikasjon Felint ervervet immunsviktsyndrom (evidensnivå L5). Opprinnelig indikasjon: Hiv-infeksjon"
---

# Doravirine
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

# Doravirin: Fra hiv-infeksjon til felint ervervet immunsviktsyndrom

## Oppsummering i én setning

Doravirin er en ikke-nukleosid revers transkriptasehemmer (NNRTI) som opprinnelig brukes til behandling av **hiv-infeksjon**. TxGNN-modellen forutsier at legemidlet kan ha effekt mot **felint ervervet immunsviktsyndrom** (katte-immunsvikt), men det finnes foreløpig **ingen kliniske studier** og **ingen publikasjoner** som direkte støtter denne prediksjonen. Prediksjonen er kun modellbasert.

---

## Hurtigoversikt

| Punkt | Innhold |
|------|------|
| Opprinnelig indikasjon | Hiv-infeksjon |
| Predikert ny indikasjon | Felint ervervet immunsviktsyndrom |
| TxGNN-prediksjonsscore | 99,93 % |
| Evidensnivå | L5 |
| Markedsstatus i Norge | Kun opphevede/trukne godkjenninger |
| Antall godkjenninger | 2 (begge opphevet) |
| Anbefalt beslutning | Hold |

---

## Hvorfor er denne prediksjonen rimelig?

Detaljerte data om virkningsmekanisme er foreløpig ikke tilgjengelige i datagrunnlaget. Basert på kjent informasjon er doravirin en NNRTI som hemmer revers transkriptase hos hiv-1, og effekten ved hiv-infeksjon er dokumentert. Mekanistisk kan den i prinsippet være aktuell for beslektede lentivirus.

Felint immunsviktvirus (FIV) er et lentivirus i slekt med hiv, og dette gir et teoretisk grunnlag for prediksjonen. Det er imidlertid en viktig svakhet: NNRTI-er har generelt dårlig aktivitet mot FIV, fordi revers transkriptase hos FIV har en annen struktur i NNRTI-bindingslommen. Den høye TxGNN-scoren ser ut til å gjenspeile at sykdommen ligger nær hiv i kunnskapsgrafen, snarere enn dokumentert aktivitet. Det foreligger ingen doravirinspesifikke FIV-data.

Det bør også nevnes at to andre prediksjoner i datagrunnlaget er enda svakere:
- **Simian immunsviktvirus-infeksjon (SIV):** Moderat mekanistisk plausibilitet, men SIV (i likhet med HIV-2) er naturlig resistent mot mange NNRTI-er. Den ene tilknyttede publikasjonen gjelder islatravir, ikke doravirin. Dette er i tillegg en indikasjon knyttet til dyremodeller uten klinisk relevans for mennesker.
- **Nevroutviklingsforstyrrelse med ataktisk gange, fraværende tale og redusert kortikal hvit substans:** Ingen plausibel mekanistisk kobling. Prediksjonen er sannsynligvis en grafbasert artefakt.

---

## Klinisk studieevidens

Foreløpig er det ingen relaterte kliniske studier registrert.

---

## Litteraturevidens

For den primære prediksjonen (felint ervervet immunsviktsyndrom) finnes foreløpig ingen relatert litteratur.

For SIV-prediksjonen (rangert som nr. 2) er følgende publikasjon knyttet, men den er bare indirekte relevant:

| PMID | År | Type | Tidsskrift | Hovedfunn |
|------|-----|------|------|---------|
| [31658118](https://pubmed.ncbi.nlm.nih.gov/31658118/) | 2020 | Oversiktsartikkel | Current Opinion in HIV and AIDS | Drøfter islatravirs potensielle rolle (en revers transkriptase-translokasjonshemmer) i behandling og forebygging av hiv-1. Gjelder ikke doravirin. |

---

## Informasjon om det norske markedet

| Godkjenningsnummer | Produktnavn | Doseringsform | Godkjent indikasjon |
|---------|------|------|-----------|
| EMEA/H/C/004747 | Pifeltro | Ikke oppgitt | Hiv-infeksjon (opphevet) |
| EMEA/H/C/004746 | Delstrigo | Ikke oppgitt | Hiv-infeksjon (opphevet) |

Begge godkjenningene er registrert som opphevet, og det finnes ingen gyldige godkjenninger.

---

## Sikkerhetsvurderinger

**Legemiddelinteraksjoner:** Det er registrert 59 interaksjoner. Blant de som er oppgitt i datagrunnlaget er de viktigste:

- **Alvorlig (Major):** deksametason, lumakaftor
- **Moderat:** glyserolfenylbutyrat, metreleptin, troglitazon, deferasirox, prazikvantel, griseofulvin
- **Mindre (Minor):** blant annet aprepitant, cimetidin, klaritromycin, klotrimazol, mikonazol, kobicistat, tikagrelor, ivakaftor, zafirlukast, kloramfenikol, erytromycin og flukonazol

For øvrig henvises det til preparatomtalen for sikkerhetsinformasjon.

---

## Konklusjon og neste steg

**Beslutning: Hold**

**Begrunnelse:**
Prediksjonen er kun modellbasert (evidensnivå L5) uten kliniske studier eller direkte litteratur. Den høye scoren synes å skyldes nærhet til hiv i kunnskapsgrafen, og NNRTI-er har kjent svak aktivitet mot FIV. I tillegg har legemidlet ingen gyldige godkjenninger i Norge i dag.

**For å gå videre kreves følgende:**
- Data om virkningsmekanisme (MOA) fra DrugBank
- Sikkerhetsopplysninger fra preparatomtalen (advarsler og kontraindikasjoner), som i dag mangler og blokkerer sikkerhetsvurderingen
- Doravirinspesifikke prekliniske data (in vitro-aktivitet mot FIV-revers transkriptase)
- Avklaring av om en veterinær indikasjon er relevant for porteføljen, og en vurdering av administrasjonsveier og formuleringer for dyr
- Avklaring av markedsstatus, siden begge norske godkjenninger er opphevet
## Ansvarsfraskrivelse

Dette innholdet er kun til forskningsformål og utgjør ikke medisinsk rådgivning.
Klinisk validering kreves før enhver klinisk anvendelse.

---

