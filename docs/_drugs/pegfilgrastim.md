---
layout: default
title: Pegfilgrastim
parent: Kun modellprediksjon (L5)
nav_order: 315
evidence_level: L5
indication_count: 2
last_modified_at: 2026-10-15
description: "Pegfilgrastim: predikert ny indikasjon Alvorlig ikke-proliferativ diabetisk retinopati (evidensnivå L5). Opprinnelig indikasjon: Nøytropeni"
---

# Pegfilgrastim
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

# Pegfilgrastim: Fra nøytropeni hos kreftpasienter til alvorlig ikke-proliferativ diabetisk retinopati

## Oppsummering i én setning

Pegfilgrastim er en langtidsvirkende vekstfaktor (G-CSF) som opprinnelig brukes mot nøytropeni og febril nøytropeni forårsaket av kjemoterapi hos kreftpasienter.
TxGNN-modellen predikerer at legemidlet kan ha effekt ved **alvorlig ikke-proliferativ diabetisk retinopati**,
men det finnes **ingen kliniske studier** og **ingen publikasjoner** i dataene som er samlet inn for denne rapporten. Prediksjonen bygger kun på modellens score.

---

## Hurtigoversikt

| Punkt | Innhold |
|------|------|
| Opprinnelig indikasjon | Nøytropeni; kreft (kjemoterapiindusert febril nøytropeni) |
| Predikert ny indikasjon | Alvorlig ikke-proliferativ diabetisk retinopati |
| TxGNN-prediksjonsscore | 99,89 % |
| Evidensnivå | L5 |
| Markedsstatus i Norge | Kun kansellerte godkjenninger |
| Antall godkjenninger | 11 (alle kansellert) |
| Anbefalt beslutning | Hold |

Merk: Godkjenningene i dataene er europeiske sentrale godkjenninger (EMEA/H/C), og alle har status kansellert. Ingen gyldige godkjenninger er registrert.

---

## Hvorfor er denne prediksjonen rimelig?

Data om virkningsmekanisme (MOA) for pegfilgrastim er ikke tilgjengelig i dataene som er samlet inn for denne rapporten. Pegfilgrastim er en pegylert form av filgrastim (G-CSF). Effekten ved nøytropeni hos kreftpasienter er veldokumentert, og legemidlet stimulerer produksjon og modning av nøytrofile granulocytter i benmargen.

En mulig, men spekulativ, kobling til diabetisk retinopati er at G-CSF mobiliserer benmargsavledede progenitorceller, som kan påvirke reparasjon av retinale kar. Retningen på effekten er imidlertid usikker: G-CSF kan også fremme betennelse og nydannelse av kar (neovaskularisering), noe som kan være skadelig, særlig ved proliferativ sykdom. Koblingen støttes ikke av noen studie eller publikasjon i dataene.

Den nest høyest rangerte prediksjonen, **diabetisk retinopati** (score 99,73 %), er en overordnet kategori til den første. De to prediksjonene er derfor ikke uavhengig evidens.

---

## Evidens fra kliniske studier

Foreløpig er det ingen relaterte kliniske studier registrert.

---

## Litteraturevidens

Foreløpig er det ingen relatert litteratur tilgjengelig.

---

## Markedsinformasjon for Norge

Alle 11 godkjenninger er kansellert. De fem første er vist under; doseringsform er ikke oppgitt i dataene.

| Godkjenningsnummer | Produktnavn | Doseringsform | Godkjent indikasjon |
|---------|------|------|-----------|
| EMEA/H/C/005312 | Cegfila (tidligere Pegfilgrastim Mundipharma) | – | – |
| EMEA/H/C/006407 | Dyrupeg | – | Nøytropeni; kreft |
| EMEA/H/C/000420 | Neulasta | – | Kreft; nøytropeni; febril nøytropeni; kjemoterapiindusert febril nøytropeni |
| EMEA/H/C/004780 | Stimufend | – | – |
| EMEA/H/C/004556 | Grasustek | – | – |

---

## Cytotoksisitet

Pegfilgrastim er ikke et antineoplastisk legemiddel, men en støttebehandling gitt til kreftpasienter. Dette avsnittet er derfor utelatt.

---

## Sikkerhetsvurderinger

Data om advarsler og kontraindikasjoner fra preparatomtalen er ikke tilgjengelig. Se preparatomtalen for sikkerhetsinformasjon.

- **Legemiddelinteraksjoner**: Interaksjonssøket ga 100 treff. Dataene som er samlet inn viser 20 av dem, alle klassifisert som **moderate** (kilde: DDInter). Eksempler:
  - Cellegift og antineoplastiske midler: paklitaksel, merkaptopurin, azacitidin, arsentrioksid, altretamin, trimetreksat, asparaginase
  - Målrettede legemidler og antistoffer: abemaciklib, akalabrutinib, avapritinib, alemtuzumab, belantamab mafodotin, aldesleukin
  - Radiofarmaka og radioimmunterapi: jobenguan (I-131), fludeoksyglukose (18F), ibritumomab tiuxetan, tositumomab (med og uten I-131)
  - Andre: levamisol, pegvaliase

  Interaksjonene er i hovedsak relevante for kreftbehandling, ikke for diabetisk retinopati. Ved bruk i en ny pasientgruppe må interaksjonsprofilen vurderes på nytt.

- **Teoretisk sikkerhetsbekymring ved ny indikasjon**: G-CSF kan potensielt fremme betennelse og nydannelse av kar. Dette er en hypotese uten støtte i data, men må vurderes nøye hos pasienter med diabetisk retinopati.

---

## Konklusjon og neste steg

**Beslutning: Hold**

**Begrunnelse:**
Prediksjonen støttes kun av en høy TxGNN-score (evidensnivå L5). Det finnes ingen kliniske studier, ingen litteratur og ingen MOA-data. Retningen på en eventuell effekt er usikker og kan være skadelig. Dessuten er alle europeiske godkjenninger i dataene kansellert.

**For å gå videre kreves følgende:**
- Hente inn data om virkningsmekanisme (MOA), f.eks. fra DrugBank
- Hente og analysere preparatomtalen (advarsler og kontraindikasjoner), noe som er en blokkerende datamangel for sikkerhetsscreening
- Systematisk litteratur- og studiesøk om G-CSF og diabetisk retinopati, inkludert prekliniske data
- Vurdere risikoen for pro-angiogene og pro-inflammatoriske effekter i øyet
- Avklare faktisk markedsstatus og tilgjengelige administrasjonsveier i Norge
## Ansvarsfraskrivelse

Dette innholdet er kun til forskningsformål og utgjør ikke medisinsk rådgivning.
Klinisk validering kreves før enhver klinisk anvendelse.

---

