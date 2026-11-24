---
layout: default
title: Lumacaftor
parent: Kun modellprediksjon (L5)
nav_order: 254
evidence_level: L5
indication_count: 1
last_modified_at: 2026-11-24
description: "Lumacaftor: predikert ny indikasjon Lepra (evidensnivå L5). Opprinnelig indikasjon: Cystisk fibrose"
monitor_inn: "LUMACAFTOR"
predicted_indications: ["leprosy"]
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

<div id="pharmacist" markdown="1">

## Farmasøytens vurderingsrapport

</div>

## Lumacaftor: Fra cystisk fibrose til lepra
{: .text-alpha }

## Oppsummering i én setning

Lumacaftor er en CFTR-korrektor som opprinnelig brukes til behandling av cystisk fibrose. TxGNN-modellen forutsier at legemidlet kan ha effekt mot **lepra**, men det finnes foreløpig **ingen registrerte kliniske studier** og **ingen publikasjoner** som støtter denne retningen. Prediksjonen er derfor kun modellbasert.

---

## Hurtigoversikt

| Punkt | Innhold |
|------|------|
| Opprinnelig indikasjon | Cystisk fibrose |
| Predikert ny indikasjon | Lepra |
| TxGNN-prediksjonsscore | 0,9944 |
| Evidensnivå | L5 |
| Markedsstatus i Norge | Markedsført (gyldige tillatelser: 1 av 1) |
| Antall godkjenninger | 1 (gyldige: 1) |
| Anbefalt beslutning | Hold |

---

## Hvorfor er denne prediksjonen (ikke) rimelig?

Ifølge avsnittet «Mechanism of Action» i preparatomtalen som er godkjent av amerikanske FDA (Prescribing Information), for lumacaftor and ivacaftor (kombinasjonspreparat med Lumacaftor) (uoffisiell oversettelse): «Lumakaftor forbedrer den konformasjonelle stabiliteten til F508del-CFTR, noe som fører til økt prosessering og transport av modent protein til celleoverflaten. Studier in vitro har vist at både lumakaftor og ivakaftor virker direkte på CFTR-proteinet i primære humane bronkiale epitelkulturer og andre cellelinjer som bærer F508del-CFTR-mutasjonen, og øker mengden, stabiliteten og funksjonen av F508del-CFTR på celleoverflaten, noe som fører til økt transport av kloridioner.» Engelsk originaltekst: "Lumacaftor improves the conformational stability of F508del-CFTR, resulting in increased processing and trafficking of mature protein to the cell surface. In vitro studies have demonstrated that both lumacaftor and ivacaftor act directly on the CFTR protein in primary human bronchial epithelial cultures and other cell lines harboring the F508del-CFTR mutation to increase the quantity, stability, and function of F508del-CFTR at the cell surface, resulting in increased chloride ion transport." ([DailyMed: Orkambi (lumacaftor and ivacaftor) prescribing information, Vertex Pharmaceuticals Incorporated](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=3fc1c40e-cfac-47a1-9e1a-61ead3570600), versjon av 2026-03-24; hentet 2026-11-19). Basert på kjent informasjon er lumacaftor en CFTR-korrektor som bedrer foldingen og transporten av F508del-CFTR-proteinet til cellemembranen. Effekten er dokumentert ved cystisk fibrose.

Det finnes ingen etablert mekanistisk kobling mellom CFTR-korreksjon og lepra. Lepra skyldes infeksjon med *Mycobacterium leprae*, og har ingen kjent CFTR-avhengig patofysiologi. Den høye scoren (0,9944) er en prediksjon fra TxGNN-modellen (dyp læring) og kan skyldes nettverksnærhet via felles biologiske traséer, for eksempel proteinfolding i verten, kloridtransport eller betennelsesrelaterte og mykobakterie-relaterte koblinger til cystisk fibrose. Dette er spekulativt og ikke støttet av direkte data.

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
| EMEA/H/C/003954 | Orkambi | Lumacaftor; ivacaftor | Cystic Fibrosis | Gyldig |

Kilde: EMA – Medicines output (sentralt godkjente legemidler til mennesker); preparatnavn, virkestoffer og terapeutisk område er gjengitt i engelsk original. Nasjonale markedsføringstillatelser (DMP) og veterinærpreparater er ikke med i disse dataene.

<!-- licenses:end -->

Merk: Legemidlet er markedsført, og 1 av 1 godkjenning er gyldig.

---

## Sikkerhetsvurderinger

**Legemiddelinteraksjoner:** Den innsamlede interaksjonssøkingen er fullført og viser 100 registrerte interaksjoner. De 20 som er listet i dataene, fordeler seg slik:

- **Alvorlige (Major):** eliglustat, naldemedin, naloxegol, rolapitant
- **Moderate:** blant annet protonpumpehemmere (omeprazol, esomeprazol, lansoprazol, deksla­nsoprazol, pantoprazol, rabeprazol), ranitidin, prednison, betametason, bupropion, antidiabetika (acetoheksamid, glimepirid, linagliptin, pioglitazon, repaglinid) og nitisinon

Informasjon om advarsler og kontraindikasjoner fra preparatomtalen er ikke tilgjengelig. Se preparatomtalen for fullstendig sikkerhetsinformasjon.

---

## Konklusjon og neste steg

**Beslutning: Hold**

**Begrunnelse:**
Prediksjonen bygger kun på en modellscore uten støtte fra kliniske studier, litteratur eller en kjent virkningsmekanisme. Sikkerhetsdata fra preparatomtalen mangler.

<!-- review:begin no-lic-20261106-lumacaftor-1 -->

> **Kontrollrettelse (2026-11-06)**: Opprinnelig sto det: «Legemidlet er dessuten ikke lenger markedsført i Norge, og sikkerhetsdata fra preparatomtalen mangler.» Fjernet: opplysningen om at godkjenningene er avregistrert eller at ingen gyldig godkjenning finnes, stemte ikke med EMAs data om sentrale EU-godkjenninger (2026-11-06). Oppdaterte antall og statuser for godkjenningene står i hurtigoversikten og i lisenstabellen under markedsinformasjonen. Kilde: [EMA – Medicines output: medicines report](https://www.ema.europa.eu/en/documents/report/medicines-output-medicines-report_en.xlsx); [European Medicines Agency](https://www.ema.europa.eu/).

<!-- review:end no-lic-20261106-lumacaftor-1 -->

**For å gå videre kreves følgende:**
- Data om virkningsmekanisme (MOA) fra DrugBank
- Sikkerhetsinformasjon (advarsler og kontraindikasjoner) fra preparatomtalen, som er en forutsetning for videre sikkerhetsvurdering
- Prekliniske studier som undersøker en mulig kobling mellom CFTR-korreksjon og *M. leprae*-infeksjon
- Vurdering av administrasjonsvei og formulering for den nye indikasjonen
- Avklaring av den regulatoriske statusen

<!-- review:begin no-lic-20261106-lumacaftor-2 -->

> **Kontrollrettelse (2026-11-06)**: Opprinnelig sto det: «Avklaring av den regulatoriske statusen, siden eneste godkjenning er avregistrert» Fjernet: opplysningen om at godkjenningene er avregistrert eller at ingen gyldig godkjenning finnes, stemte ikke med EMAs data om sentrale EU-godkjenninger (2026-11-06). Oppdaterte antall og statuser for godkjenningene står i hurtigoversikten og i lisenstabellen under markedsinformasjonen. Kilde: [EMA – Medicines output: medicines report](https://www.ema.europa.eu/en/documents/report/medicines-output-medicines-report_en.xlsx); [European Medicines Agency](https://www.ema.europa.eu/).

<!-- review:end no-lic-20261106-lumacaftor-2 -->

<!-- review:begin log -->

## Kontrollogg

Nedenfor er kontrolloggen for denne siden: opplysninger kontrollert mot EMAs data om sentrale EU-godkjenninger. Rettelser gjelder bare grunnleggende faktaopplysninger; modellens prediksjoner, evidensnivåer og konklusjoner er ikke skrevet om. Setningen om at data om virkningsmekanismen ikke var tilgjengelige, er erstattet med et utdrag fra den oppgitte offisielle preparatomtalen (med uoffisiell oversettelse).

| Kontrolldato | Punkt | Tiltak | Kilde |
|------|------|------|------|
| 2026-11-06 | Fjernet: «Legemidlet er dessuten ikke lenger markedsført i Norge, og s» | Rettet (revidert 2026-11-24; tidligere versjon er lagret i posten) | [EMA – Medicines output: medicines report](https://www.ema.europa.eu/en/documents/report/medicines-output-medicines-report_en.xlsx); [European Medicines Agency](https://www.ema.europa.eu/) |
| 2026-11-06 | Fjernet: «siden eneste godkjenning er avregistrert» | Rettet (revidert 2026-11-24; tidligere versjon er lagret i posten) | [EMA – Medicines output: medicines report](https://www.ema.europa.eu/en/documents/report/medicines-output-medicines-report_en.xlsx); [European Medicines Agency](https://www.ema.europa.eu/) |
| 2026-11-19 | Setningen «data om virkningsmekanismen er ikke tilgjengelige» erstattet med utdrag fra amerikansk preparatomtale | Setning om manglende data om virkningsmekanismen erstattet med et utdrag med kilde | [DailyMed: Orkambi (lumacaftor and ivacaftor) prescribing information, Vertex Pharmaceuticals Incorporated](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=3fc1c40e-cfac-47a1-9e1a-61ead3570600) |

<!-- review:end log -->

## Ansvarsfraskrivelse

Dette innholdet er kun til forskningsformål og utgjør ikke medisinsk rådgivning.
Klinisk validering kreves før enhver klinisk anvendelse.

---

