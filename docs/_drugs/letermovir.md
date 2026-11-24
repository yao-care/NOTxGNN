---
layout: default
title: Letermovir
parent: Kun modellprediksjon (L5)
nav_order: 241
evidence_level: L5
indication_count: 1
last_modified_at: 2026-11-24
description: "Letermovir: predikert ny indikasjon Vulvovaginal candidiasis (evidensnivå L5). Opprinnelig indikasjon: Cytomegalovirusinfeksjon"
monitor_inn: "LETERMOVIR"
predicted_indications: ["vulvovaginal candidiasis"]
---

# Letermovir
{: .fs-9 }

Evidensnivå: **L5** | Predikerte indikasjoner: **1** stk.
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

## Letermovir: Fra cytomegalovirusinfeksjon til vulvovaginal candidiasis
{: .text-alpha }

## Oppsummering i en setning

Letermovir er et antiviralt middel som opprinnelig brukes mot **cytomegalovirusinfeksjon (CMV)**. TxGNN-modellen forutsier at legemidlet kan ha effekt mot **vulvovaginal candidiasis**, men det finnes foreløpig **ingen kliniske studier og ingen publikasjoner** som støtter denne retningen. Prediksjonen er rent beregningsbasert.

---

## Hurtigoversikt

| Punkt | Innhold |
|------|------|
| Opprinnelig indikasjon | Cytomegalovirusinfeksjon |
| Foreslått ny indikasjon | Vulvovaginal candidiasis |
| TxGNN-prediksjonsscore | 0,9988 |
| Evidensnivå | L5 |
| Markedsstatus i Norge | Markedsført (gyldige tillatelser: 1 av 1) |
| Antall godkjenninger | 1 (gyldige: 1) |
| Anbefalt beslutning | Hold |

---

## Hvorfor er denne prediksjonen (ikke) rimelig?

Ifølge avsnittene «Mechanism of Action» og «Microbiology» i preparatomtalen som er godkjent av amerikanske FDA (Prescribing Information), for Letermovir (uoffisiell oversettelse): «PREVYMIS er et antiviralt legemiddel mot CMV. […] Letermovir hemmer CMV-DNA-terminasekomplekset (pUL51, pUL56 og pUL89), som er nødvendig for prosessering og pakking av viralt DNA. Biokjemisk karakterisering og elektronmikroskopi viste at letermovir påvirker produksjonen av genomer med korrekt enhetslengde og forstyrrer virionmodningen.» Engelsk originaltekst: "PREVYMIS is an antiviral drug against CMV. […] Letermovir inhibits the CMV DNA terminase complex (pUL51, pUL56, and pUL89) which is required for viral DNA processing and packaging. Biochemical characterization and electron microscopy demonstrated that letermovir affects the production of proper unit length genomes and interferes with virion maturation." ([DailyMed: Prevymis (letermovir) prescribing information, Merck Sharp & Dohme LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=1b49df80-be4f-47e0-a0b7-123f3e69395b), versjon av 2026-01-14; hentet 2026-11-19). Basert på kjent kunnskap hemmer letermovir det virale terminasekomplekset (pUL56/UL89/UL51) hos CMV. Dette er en mekanisme som er spesifikk for viruset.

Det er ingen kjent fungal homolog til dette målet. Aktivitet mot *Candida*-arter er derfor ikke biologisk sannsynlig ut fra dagens kunnskap. Det foreligger heller ingen in vitro-, in vivo- eller kliniske data om antifungal effekt.

Den høye TxGNN-scoren (0,9988) bør tolkes med forsiktighet. Scoren kommer fra TxGNN-modellen (deep learning) og kan gjenspeile likheter modellen har lært mellom beslektede sykdommer, ikke biologisk evidens. Likhet mellom opprinnelig og ny indikasjon er ikke vurdert.

---

## Klinisk studieevidens

Foreløpig er det ingen relaterte kliniske studier registrert.

---

## Litteraturevidens

Foreløpig finnes det ingen relatert litteratur.

---

## Markedsinformasjon for Norge

<!-- licenses:begin -->

| Godkjenningsnummer | Preparatnavn (EMA) | Virkestoff(er) (EMA, engelsk) | Terapeutisk område (EMA, engelsk) | Status |
|------|------|------|------|------|
| EMEA/H/C/004536 | Prevymis | Letermovir | Cytomegalovirus Infections | Gyldig |

Kilde: EMA – Medicines output (sentralt godkjente legemidler til mennesker); preparatnavn, virkestoffer og terapeutisk område er gjengitt i engelsk original. Nasjonale markedsføringstillatelser (DMP) og veterinærpreparater er ikke med i disse dataene.

<!-- licenses:end -->

Legemidlet er markedsført i Norge, og 1 av 1 godkjenning er gyldig.

---

## Sikkerhetsvurderinger

**Legemiddelinteraksjoner**: Det er funnet 100 registrerte interaksjoner. Blant de viste er følgende klassifisert som **alvorlige (Major)**:

- Eliglustat
- Naloksegol
- Cisaprid

Flere interaksjoner med **moderat** alvorlighetsgrad er også registrert, blant annet:

- Kortikosteroider: hydrokortison, deksametason, betametason, triamsinolon, budesonid (inkl. nasal)
- Protonpumpehemmere: omeprazol, lansoprazol
- Antidiabetika: pioglitazon, saksagliptin, glimepirid, klorpropamid, acetoheksamid
- Andre: aprepitant, klaritromycin, naldemedin, nitisinon

For øvrige sikkerhetsopplysninger, som advarsler og kontraindikasjoner, henvises det til preparatomtalen.

---

## Konklusjon og neste steg

**Beslutning: Hold**

**Begrunnelse:**
Prediksjonen bygger kun på en modellscore uten støtte fra kliniske studier, litteratur eller en plausibel virkningsmekanisme. Letermovirs mål er virusspesifikt, og det er ikke noe kjent tilsvarende mål hos sopp.

<!-- review:begin no-lic-20261106-letermovir-1 -->

> **Kontrollrettelse (2026-11-06)**: Opprinnelig sto det: «Letermovirs mål er virusspesifikt, og det er ikke noe kjent tilsvarende mål hos sopp. I tillegg er den eneste godkjenningen i Norge opphevet.» Fjernet: opplysningen om at godkjenningene er avregistrert eller at ingen gyldig godkjenning finnes, stemte ikke med EMAs data om sentrale EU-godkjenninger (2026-11-06). Oppdaterte antall og statuser for godkjenningene står i hurtigoversikten og i lisenstabellen under markedsinformasjonen. Kilde: [EMA – Medicines output: medicines report](https://www.ema.europa.eu/en/documents/report/medicines-output-medicines-report_en.xlsx); [European Medicines Agency](https://www.ema.europa.eu/).

<!-- review:end no-lic-20261106-letermovir-1 -->

**For å gå videre kreves følgende:**
- Data om virkningsmekanisme (MOA) fra DrugBank
- Advarsler og kontraindikasjoner fra preparatomtalen (blokkerende mangel for sikkerhetsscreening)
- In vitro-data som viser eventuell aktivitet mot *Candida*-arter
- Vurdering av administrasjonsveier som er relevante for vulvovaginal candidiasis (f.eks. lokal behandling), siden dette ikke er avklart
- Gjennomgang av det store antallet legemiddelinteraksjoner dersom prosjektet fortsetter

<!-- review:begin log -->

## Kontrollogg

Nedenfor er kontrolloggen for denne siden: opplysninger kontrollert mot EMAs data om sentrale EU-godkjenninger. Rettelser gjelder bare grunnleggende faktaopplysninger; modellens prediksjoner, evidensnivåer og konklusjoner er ikke skrevet om. Setningen om at data om virkningsmekanismen ikke var tilgjengelige, er erstattet med et utdrag fra den oppgitte offisielle preparatomtalen (med uoffisiell oversettelse).

| Kontrolldato | Punkt | Tiltak | Kilde |
|------|------|------|------|
| 2026-11-06 | Fjernet: «I tillegg er den eneste godkjenningen i Norge opphevet» | Rettet (revidert 2026-11-24; tidligere versjon er lagret i posten) | [EMA – Medicines output: medicines report](https://www.ema.europa.eu/en/documents/report/medicines-output-medicines-report_en.xlsx); [European Medicines Agency](https://www.ema.europa.eu/) |
| 2026-11-19 | Setningen «data om virkningsmekanismen er ikke tilgjengelige» erstattet med utdrag fra amerikansk preparatomtale | Setning om manglende data om virkningsmekanismen erstattet med et utdrag med kilde | [DailyMed: Prevymis (letermovir) prescribing information, Merck Sharp & Dohme LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=1b49df80-be4f-47e0-a0b7-123f3e69395b) |

<!-- review:end log -->

## Ansvarsfraskrivelse

Dette innholdet er kun til forskningsformål og utgjør ikke medisinsk rådgivning.
Klinisk validering kreves før enhver klinisk anvendelse.

---

