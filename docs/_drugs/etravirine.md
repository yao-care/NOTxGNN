---
layout: default
title: Etravirine
parent: Kun modellprediksjon (L5)
nav_order: 167
evidence_level: L5
indication_count: 8
monitor_inn: "ETRAVIRINE"
predicted_indications: ["simian immunodeficiency virus infection", "feline acquired immunodeficiency syndrome", "neurodevelopmental disorder with ataxic gait, absent speech, and decreased cortical white matter", "fibroma of prostate", "Brenner tumor", "benign reproductive system neoplasm", "benign prostate phyllodes tumor", "obsolete familial combined hyperlipidemia"]
last_modified_at: 2026-11-24
description: "Etravirine: predikert ny indikasjon Simian immunsviktvirusinfeksjon (simian immunodeficiency virus infection) (evidensnivå L5). Opprinnelig indikasjon: HIV Infections"
---

# Etravirine
{: .fs-9 }

Evidensnivå: **L5** | Predikerte indikasjoner: **8** stk.
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

## Etravirin: ikke-nukleosid revers transkriptasehemmer (NNRTI) → simian immunsviktvirusinfeksjon (simian immunodeficiency virus infection)
{: .text-alpha }

## Oppsummering

Etravirin er en ikke-nukleosid revers transkriptasehemmer (NNRTI) som brukes mot HIV-infeksjon. TxGNN-modellen forutsier at legemidlet kan ha effekt mot **simian immunsviktvirusinfeksjon (simian immunodeficiency virus infection)**. Det er **ingen kliniske studier** og bare **én publikasjon** (en preklinisk in vitro-studie av HIV) i de data som er sammenstilt for denne rapporten, så støtten er svært svak.

## Hurtigoversikt

| Punkt | Innhold |
|------|------|
| Opprinnelig indikasjon | HIV Infections |
| Foreslått ny indikasjon | Simian immunsviktvirusinfeksjon (simian immunodeficiency virus infection) |
| TxGNN-prediksjonsscore | 0,9998 |
| Evidensnivå | L5 |
| Markedsstatus i Norge | Markedsført (gyldige tillatelser: 1 av 1) |
| Antall godkjenninger | 1 (gyldige: 1) |
| Anbefalt beslutning | Hold |

## Hvorfor er denne prediksjonen rimelig?

Ifølge avsnittene «Mechanism of Action» og «Microbiology» i preparatomtalen som er godkjent av amerikanske FDA (Prescribing Information), for Etravirine (uoffisiell oversettelse): «Etravirin er et antiretroviralt legemiddel. […] Etravirin er en NNRTI for HIV-1. Etravirin bindes direkte til revers transkriptase (RT) og blokkerer de RNA-avhengige og DNA-avhengige DNA-polymeraseaktivitetene ved å forårsake en forstyrrelse av enzymets katalytiske sete. Etravirin hemmer ikke de humane DNA-polymerasene α, β og γ.» Engelsk originaltekst: "Etravirine is an antiretroviral drug. […] Etravirine is an NNRTI of HIV-1. Etravirine binds directly to reverse transcriptase (RT) and blocks the RNA-dependent and DNA-dependent DNA polymerase activities by causing a disruption of the enzyme's catalytic site. Etravirine does not inhibit the human DNA polymerases α, β, and γ." ([DailyMed: Intelence (etravirine) prescribing information, Janssen Products LP](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=6a9cbc29-9f15-4b24-8d86-206b82887f3d), versjon av 2023-08-15; hentet 2026-11-19). Etravirin er kjent som en NNRTI som hemmer revers transkriptase hos HIV-1. SIV er en nær lentiviral slektning av HIV, og et felles revers transkriptase-mål er derfor konseptuelt mulig.

Den mekanistiske koblingen er likevel svak. SIV er, i likhet med HIV-2, i hovedsak naturlig resistent mot de fleste NNRTI-er. Den høye prediksjonsscoren gjenspeiler trolig likhet med HIV i modellens data, ikke dokumentert aktivitet mot SIV. Indikasjonen gjelder dessuten en dyremodell/veterinærmedisinsk sammenheng med liten klinisk relevans for mennesker.

## Kliniske studier

Foreløpig er ingen relaterte kliniske studier registrert.

## Litteraturevidens

| PMID | År | Type | Tidsskrift | Hovedfunn |
|------|-----|------|------|---------|
| [26529558](https://pubmed.ncbi.nlm.nih.gov/26529558/) | 2015 | Preklinisk (in vitro) | Molecular Pharmaceutics | Nanopartikkelbaserte kombinasjoner av antiretrovirale legemidler ga synergistisk hemming av HIV-overføring. Studien omhandler HIV, ikke SIV, og er derfor kun indirekte evidens. |

Ingen publikasjon i dataene studerer SIV-infeksjon direkte.

## Markedsinformasjon for Norge

<!-- licenses:begin -->

| Godkjenningsnummer | Preparatnavn (EMA) | Virkestoff(er) (EMA, engelsk) | Terapeutisk område (EMA, engelsk) | Status |
|------|------|------|------|------|
| EMEA/H/C/000900 | Intelence | Etravirine | HIV Infections | Gyldig |

Kilde: EMA – Medicines output (sentralt godkjente legemidler til mennesker); preparatnavn, virkestoffer og terapeutisk område er gjengitt i engelsk original. Nasjonale markedsføringstillatelser (DMP) og veterinærpreparater er ikke med i disse dataene.

<!-- licenses:end -->

## Sikkerhetsvurderinger

**Legemiddelinteraksjoner:** Interaksjonsdata er hentet (100 registrerte interaksjoner). Blant de oppførte er de fleste av moderat alvorlighetsgrad, blant annet:
- Protonpumpehemmere og H2-blokkere: omeprazol, rabeprazol, cimetidin (moderat), ranitidin (mindre)
- Kortikosteroider: hydrokortison, deksametason, betametason, triamcinolon
- Antidiabetika: pioglitazon, glimepirid, klorpropamid, saksagliptin, linagliptin
- Andre: klaritromycin, metronidazol, aprepitant, dronabinol, eliglustat, naloksegol, naldemedin

Merk: Ettersom listen er avgrenset, bør fullstendig interaksjonsinformasjon sjekkes i preparatomtalen.

Preparatomtalen bør konsulteres for advarsler og kontraindikasjoner.

## Konklusjon og neste steg

**Beslutning: Hold**

**Begrunnelse:**
Prediksjonen bygger kun på modellscore uten kliniske studier og uten litteratur som direkte undersøker SIV-infeksjon. Den mekanistiske koblingen er svak på grunn av SIVs iboende NNRTI-resistens, og indikasjonen har liten relevans for mennesker.

**For å gå videre kreves:**
- In vitro-data på etravirins aktivitet mot SIV-stammer, inkludert resistensprofil
- Data om virkningsmekanisme (MOA)
- Informasjon fra preparatomtalen om advarsler og kontraindikasjoner
- En klar begrunnelse for relevans i dyremodell eller veterinærbruk før videre prioritering

<!-- review:begin log -->

## Kontrollogg

Nedenfor er gjennomgangsloggen for denne siden. Setningen om at data om virkningsmekanismen ikke var tilgjengelige, er erstattet med et utdrag fra den oppgitte offisielle preparatomtalen (med uoffisiell oversettelse); modellprediksjoner, evidensnivåer og konklusjoner er ikke omskrevet.

| Kontrolldato | Punkt | Tiltak | Kilde |
|------|------|------|------|
| 2026-11-19 | Setningen «data om virkningsmekanismen er ikke tilgjengelige» erstattet med utdrag fra amerikansk preparatomtale | Setning om manglende data om virkningsmekanismen erstattet med et utdrag med kilde | [DailyMed: Intelence (etravirine) prescribing information, Janssen Products LP](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=6a9cbc29-9f15-4b24-8d86-206b82887f3d) |

<!-- review:end log -->

## Ansvarsfraskrivelse

Dette innholdet er kun til forskningsformål og utgjør ikke medisinsk rådgivning.
Klinisk validering kreves før enhver klinisk anvendelse.

---

