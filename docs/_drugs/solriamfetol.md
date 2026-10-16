---
layout: default
title: Solriamfetol
parent: Kun modellprediksjon (L5)
nav_order: 389
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-15
description: "Solriamfetol: predikert ny indikasjon Attention deficit-hyperactivity disorder (ADHD) (evidensnivå L5). Opprinnelig indikasjon: Narkolepsi"
---

# Solriamfetol
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

# Solriamfetol: Fra narkolepsi og obstruktiv søvnapné til ADHD

## Oppsummering

Solriamfetol er et vekkende legemiddel (dopamin- og noradrenalinreopptakshemmer) som opprinnelig brukes mot overdreven søvnighet på dagtid ved **narkolepsi** og **obstruktiv søvnapné**.
TxGNN-modellen predikerer at det kan være effektivt ved **ADHD (attention deficit-hyperactivity disorder)**.
Foreløpig støttes dette av **5 kliniske studier** (blant annet en fullført fase 3-studie hos voksne) og **6 publikasjoner**, der én er en randomisert, placebokontrollert pilotstudie.

---

## Hurtigoversikt

| Punkt | Innhold |
|------|------|
| Opprinnelig indikasjon | Narkolepsi; obstruktiv søvnapné |
| Predikert ny indikasjon | Attention deficit-hyperactivity disorder (ADHD) |
| TxGNN-prediksjonsscore | 99,99 % |
| Evidensnivå | L1 (se merknad under) |
| Markedsstatus i Norge | Kun opphevede (kansellerte) godkjenninger |
| Antall godkjenninger | 1 (opphevet) |
| Anbefalt beslutning | Proceed with Guardrails (fortsette med forbehold) |

*Merknad om evidensnivå:* Datagrunnlaget klassifiserer ADHD som L1. Kun én fullført fase 3-studie (NCT05972044) er imidlertid registrert for voksne, og resultatene er ikke tilgjengelige i de innsamlede dataene. Nivået bør derfor verifiseres mot studieregisteret eller publikasjoner.

---

## Hvorfor er denne prediksjonen rimelig?

Data om virkningsmekanisme (MOA) fra DrugBank er ikke tilgjengelig i de innsamlede dataene. Basert på kjent farmakologi er solriamfetol en hemmer av noradrenalintransportøren (NET, SLC6A2) og dopamintransportøren (DAT, SLC6A3). Disse målene er også oppført i farmakologidataene som ble samlet inn for denne rapporten.

Økt katekolaminerg signalering i prefrontale kretser er den etablerte mekanismen bak godkjente ADHD-legemidler som metylfenidat og atomoksetin. Solriamfetol har dermed en biologisk sammenhengende mekanisme med ADHD-patofysiologi, selv om den opprinnelige indikasjonen (søvnighet) og ADHD er ulike tilstander. Begge involverer oppmerksomhet og våkenhet, som reguleres av de samme transmittersystemene.

Det finnes også en forskningsmessig begrunnelse: Solriamfetol har sympatomimetiske egenskaper som ligner på ADHD-legemidler, og er undersøkt som et alternativ til tradisjonelle sentralstimulerende midler. Koblingen bygger på legemidlets kjente farmakologi og ikke på selve DrugBank-registreringen.

---

## Klinisk evidens

| Studienummer | Fase | Status | Antall deltakere | Hovedfunn |
|---------|------|------|------|---------|
| [NCT05972044](https://clinicaltrials.gov/study/NCT05972044) | Fase 3 | Fullført | 516 | FOCUS: randomisert, dobbeltblind, placebokontrollert studie hos voksne med ADHD. Resultater ikke tilgjengelige i dataene. |
| [NCT04839562](https://clinicaltrials.gov/study/NCT04839562) | Fase 2/3 | Fullført | 66 | Dobbeltblind, placebokontrollert pilotstudie hos voksne (18–65 år) med ADHD. |
| [NCT07717892](https://clinicaltrials.gov/study/NCT07717892) | Fase 3 | Rekrutterer | 468 | 6-ukers placebokontrollert studie hos ungdom (12 til <18 år). Ingen resultater ennå. |
| [NCT07717879](https://clinicaltrials.gov/study/NCT07717879) | Fase 3 | Rekrutterer | 468 | 6-ukers placebokontrollert studie hos barn (6 til <12 år). Ingen resultater ennå. |
| [NCT07773883](https://clinicaltrials.gov/study/NCT07773883) | Fase 3 | Inviterte deltakere | 300 | Åpen langtidsstudie av sikkerhet hos barn og ungdom med ADHD. |

---

## Litteraturevidens

| PMID | År | Type | Tidsskrift | Hovedfunn |
|------|-----|------|------|---------|
| [37819836](https://pubmed.ncbi.nlm.nih.gov/37819836/) | 2023 | RCT | J Clin Psychiatry | Dobbeltblind, placebokontrollert 6-ukers pilotstudie hos 60 voksne med ADHD (75 mg eller 150 mg). Undersøkte effekt og toleranse hos personer som ikke tåler eller responderer tilstrekkelig på eksisterende behandling. |
| [38771653](https://pubmed.ncbi.nlm.nih.gov/38771653/) | 2024 | Oversikt | Expert Opin Pharmacother | Gjennomgang av nyere ADHD-behandling utover sentralstimulerende midler, som har lignende bivirkninger og risiko for misbruk og avhengighet. |
| [40986064](https://pubmed.ncbi.nlm.nih.gov/40986064/) | 2025 | Oversikt | Expert Opin Pharmacother | Oversikt over potensielle ADHD-behandlinger med fokus på fase III-studier og nye nevrobiologiske mekanismer. |
| [41621729](https://pubmed.ncbi.nlm.nih.gov/41621729/) | 2026 | Oversikt | Pharmacol Ther | Samlet gjennomgang av farmakologiske, nevromodulerende og psykoterapeutiske tiltak ved ADHD hos voksne. |
| [33870884](https://pubmed.ncbi.nlm.nih.gov/33870884/) | 2022 | Oversikt/kommentar | CNS Spectrums | Kommentar om solriamfetol ved ADHD. |
| [34534876](https://pubmed.ncbi.nlm.nih.gov/34534876/) | 2021 | Oversikt | Epilepsy Behav | Legemidler ved epilepsi og overdreven søvnighet; nevner ADHD som mulig medvirkende tilstand. |

---

## Markedsinformasjon for Norge

| Godkjenningsnummer | Produktnavn | Doseringsform | Godkjent indikasjon |
|---------|------|------|-----------|
| EMEA/H/C/004893 | Sunosi | Ikke oppgitt | Narkolepsi; obstruktiv søvnapné (status: opphevet) |

---

## Sikkerhetsvurderinger

- **Legemiddelinteraksjoner:** Interaksjonsspørringen ga to farmakologiske mål, ikke interagerende legemidler med klinisk gradering: noradrenalintransportøren (NET) og dopamintransportøren (DAT). Dette er legemidlets virkningsmål og bekrefter mekanismen, men sier lite om konkrete legemiddelkombinasjoner.
- **Kardiovaskulære hensyn:** Fra generell farmakologi kan katekolaminerg stimulering øke puls og blodtrykk. Dette bør følges opp i ADHD-studiene og hos pasienter med hjerte- og karsykdom.

Se preparatomtalen for fullstendig informasjon om advarsler og kontraindikasjoner.

---

## Konklusjon og neste steg

**Beslutning: Proceed with Guardrails (fortsette med forbehold)**

**Begrunnelse:**
Mekanismen er biologisk sammenhengende med ADHD, og det finnes en fullført fase 3-studie og en fullført fase 2/3-studie hos voksne, samt flere pågående fase 3-studier hos barn og ungdom. Resultatene fra de store studiene er imidlertid ikke bekreftet i datagrunnlaget, og produktet har ingen gyldig godkjenning i Norge.

**For å gå videre kreves følgende:**
- Verifisere resultater fra NCT05972044 (FOCUS) i studieregisteret eller publikasjoner
- Innhente preparatomtale med advarsler og kontraindikasjoner (dette er en blokkerende datamangel for sikkerhetsvurdering)
- Hente detaljerte data om virkningsmekanisme fra DrugBank
- Avklare regulatorisk status i Norge, siden eneste godkjenning er opphevet
- Utarbeide en plan for kardiovaskulær overvåking og for barn og ungdom når resultater fra de pågående studiene foreligger
## Ansvarsfraskrivelse

Dette innholdet er kun til forskningsformål og utgjør ikke medisinsk rådgivning.
Klinisk validering kreves før enhver klinisk anvendelse.

---

