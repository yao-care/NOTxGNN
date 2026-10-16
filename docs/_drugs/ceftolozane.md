---
layout: default
title: Ceftolozane
parent: Kun modellprediksjon (L5)
nav_order: 89
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-15
description: "Ceftolozane: predikert ny indikasjon Gonokokk-uretritt (evidensnivå L5). Opprinnelig indikasjon: Bakterielle infeksjoner"
monitor_inn: "Ceftolozane"
predicted_indications: ["gonococcal urethritis", "Ureaplasma urethritis", "uterine inflammatory disease", "xanthogranulomatous pyelonephritis", "polyclonal hyperviscosity syndrome", "hyperamylasemia", "urogenital tuberculosis", "congenital analbuminemia", "blood group incompatibility", "premalignant hematological system disease"]
---

# Ceftolozane
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

# Ceftolozan: Fra bakterielle infeksjoner til gonokokk-uretritt

## Oppsummering i én setning

Ceftolozan er et cefalosporin-antibiotikum som opprinnelig er brukt mot bakterielle infeksjoner (i Europa markedsført som Zerbaxa).
TxGNN-modellen forutsier at det kan ha effekt mot **gonokokk-uretritt**, med en prediksjonsscore på **99,89 %**.
Det finnes foreløpig **ingen kliniske studier** og **ingen publikasjoner** som direkte støtter denne retningen, så prediksjonen er kun modellbasert.

---

## Hurtigoversikt

| Punkt | Innhold |
|------|------|
| Opprinnelig indikasjon | Bakterielle infeksjoner |
| Predikert ny indikasjon | Gonokokk-uretritt |
| TxGNN-prediksjonsscore | 99,89 % |
| Evidensnivå | L5 |
| Markedsstatus i Norge | Kun kansellerte godkjenninger |
| Antall godkjenninger | 1 (kansellert) |
| Anbefalt beslutning | Hold (avvent) |

---

## Hvorfor er denne prediksjonen rimelig?

Detaljerte data om virkningsmekanisme er foreløpig ikke tilgjengelige. Ut fra kjent informasjon er ceftolozan et cefalosporin med aktivitet mot Pseudomonas og andre gramnegative bakterier. Som andre betalaktamer hemmer det sannsynligvis bakteriens celleveggsyntese via penicillinbindende proteiner. Effekten ved bakterielle infeksjoner er dokumentert, og på klassenivå finnes det derfor en antibakteriell begrunnelse for bruk ved gonokokk-uretritt, som også er en bakteriell infeksjon.

Begrunnelsen er imidlertid svak. Ceftolozan er ikke et etablert middel mot *Neisseria gonorrhoeae*, der andre cefalosporiner (for eksempel ceftriaxon) er standardbehandling. Den høye scoren (0,999) er en ren modellprediksjon. Samme score er gitt til flere andre diagnoser, blant annet ureaplasma-uretritt, der betalaktamer er mekanistisk lite sannsynlige fordi *Ureaplasma* mangler cellevegg. Det tyder på at prediksjonene i stor grad gjenspeiler en generell assosiasjon til «bakteriell infeksjon».

Blant de ti øverste prediksjonene er den mest troverdige koblingen faktisk **xantogranulomatøs pyelonefritt**, siden ceftolozan/tazobaktam er godkjent mot kompliserte urinveisinfeksjoner, inkludert pyelonefritt. Tilstanden behandles som regel kirurgisk (nefrektomi), så antibiotika er bare et supplement. Flere av de øvrige prediksjonene (for eksempel polyklonalt hyperviskositetssyndrom, hyperamylasemi, medfødt analbuminemi og blodgruppeinkompatibilitet) er ikke infeksjonssykdommer og mangler troverdig mekanistisk sammenheng.

---

## Evidens fra kliniske studier

Foreløpig er det ingen relaterte kliniske studier registrert for gonokokk-uretritt.

---

## Evidens fra litteratur

Foreløpig er det ingen relatert litteratur for gonokokk-uretritt.

For den nest mest relevante prediksjonen, xantogranulomatøs pyelonefritt, ble én artikkel funnet:

| PMID | År | Type | Tidsskrift | Hovedfunn |
|------|-----|------|------|---------|
| [26658652](https://pubmed.ncbi.nlm.nih.gov/26658652/) | 2016 | Oversiktsartikkel | Current Opinion in Infectious Diseases | Generell oversikt over febrile urinveisinfeksjoner, pyelonefritt og urosepsis. Omtaler verken ceftolozan eller xantogranulomatøs pyelonefritt spesifikt. |

---

## Markedsinformasjon for Norge

| Godkjenningsnummer | Produktnavn | Doseringsform | Godkjent indikasjon |
|---------|------|------|-----------|
| EMEA/H/C/003772 | Zerbaxa (Merck Sharp & Dohme B.V.) | Ikke oppgitt | Bakterielle infeksjoner (status: kansellert) |

---

## Sikkerhetsvurderinger

**Legemiddelinteraksjoner:** Det er funnet 11 interaksjoner av moderat alvorlighetsgrad:

- **Aminoglykosider:** kanamycin, neomycin, streptomycin, amikacin (inkludert liposomal formulering) og gentamicin
- **Antikoagulantia:** warfarin og dikumarol
- **Andre:** kloramfenikol, etinylestradiol og mykofenolsyre

Informasjon om advarsler og kontraindikasjoner foreligger ikke i de innsamlede dataene. Se preparatomtalen (SPC) for fullstendig sikkerhetsinformasjon.

---

## Konklusjon og neste steg

**Beslutning: Hold (avvent)**

**Begrunnelse:**
Prediksjonen for gonokokk-uretritt bygger kun på en modellscore uten kliniske studier eller litteratur. Ceftolozan er ikke et etablert middel mot *N. gonorrhoeae*, der effektive standardbehandlinger allerede finnes. Den eneste norske/europeiske godkjenningen er kansellert, og sikkerhetsdata fra preparatomtalen mangler.

**For å gå videre kreves følgende:**
- Preparatomtale med advarsler og kontraindikasjoner (blokkerende datagap)
- Data om virkningsmekanisme (MOA) fra DrugBank
- In vitro-data på følsomhet hos *N. gonorrhoeae* (MIC-verdier) og sammenligning med ceftriaxon
- Dersom en alternativ indikasjon skal vurderes, bør xantogranulomatøs pyelonefritt prioriteres som forskningsspørsmål (evidensnivå L4), basert på den godkjente indikasjonen for kompliserte urinveisinfeksjoner
- Avklaring av administrasjonsvei og tilgjengelige formuleringer, siden markedsstatus i Norge er kansellert
## Ansvarsfraskrivelse

Dette innholdet er kun til forskningsformål og utgjør ikke medisinsk rådgivning.
Klinisk validering kreves før enhver klinisk anvendelse.

---

