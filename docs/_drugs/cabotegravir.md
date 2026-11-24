---
layout: default
title: Cabotegravir
parent: Kun modellprediksjon (L5)
nav_order: 75
evidence_level: L5
indication_count: 5
last_modified_at: 2026-11-24
description: "Cabotegravir: predikert ny indikasjon Revmatoid artritt (evidensnivå L5). Opprinnelig indikasjon: HIV-infeksjon"
monitor_inn: "CABOTEGRAVIR"
predicted_indications: ["rheumatoid arthritis", "sclerosing cholangitis", "bronchitis", "colobomatous microphthalmia-rhizomelic dysplasia syndrome", "severe nonproliferative diabetic retinopathy"]
---

# Cabotegravir
{: .fs-9 }

Evidensnivå: **L5** | Predikerte indikasjoner: **5** stk.
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

## Kabotegravir: Fra HIV-infeksjon til revmatoid artritt
{: .text-alpha }

## Oppsummering i én setning

Kabotegravir er en integrasehemmer som opprinnelig brukes til behandling og forebygging av HIV-infeksjon. TxGNN-modellen forutsier at legemidlet kan ha effekt ved **revmatoid artritt**, men det finnes foreløpig **ingen kliniske studier** og **ingen publikasjoner** som støtter denne retningen. Prediksjonen er rent beregningsbasert.

---

## Hurtigoversikt

| Punkt | Innhold |
|------|------|
| Opprinnelig indikasjon | HIV-infeksjon |
| Predikert ny indikasjon | Revmatoid artritt |
| TxGNN-prediksjonsscore | 0,9945 |
| Evidensnivå | L5 |
| Markedsstatus i Norge | Markedsført (gyldige tillatelser: 2 av 2) |
| Antall godkjenninger | 2 (gyldige: 2) |
| Anbefalt beslutning | Hold |

---

## Hvorfor er denne prediksjonen (ikke) rimelig?

Ifølge avsnittene «Mechanism of Action» og «Microbiology» i preparatomtalen som er godkjent av amerikanske FDA (Prescribing Information), for Cabotegravir (uoffisiell oversettelse): «Kabotegravir er et antiretroviralt legemiddel mot HIV-1. […] Kabotegravir hemmer HIV-integrase ved å binde seg til integrasens aktive sete og blokkere trådoverføringstrinnet i integrasjonen av retroviral deoksyribonukleinsyre (DNA), som er avgjørende for HIVs replikasjonssyklus. Gjennomsnittlig 50 % hemmende konsentrasjon (IC 50 ) for kabotegravir i en trådoverføringsanalyse med renset rekombinant HIV-1-integrase var 3,0 nM.» Engelsk originaltekst: "Cabotegravir is an HIV-1 antiretroviral drug. […] Cabotegravir inhibits HIV integrase by binding to the integrase active site and blocking the strand transfer step of retroviral deoxyribonucleic acid (DNA) integration that is essential for the HIV replication cycle. The mean 50% inhibitory concentration (IC 50 ) value of cabotegravir in a strand transfer assay using purified recombinant HIV-1 integrase was 3.0 nM." ([DailyMed: Vocabria (cabotegravir sodium) prescribing information, ViiV Healthcare Company](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=66d450fb-cca4-476c-b0c7-c0730e3e4cf3), versjon av 2025-04-11; hentet 2026-11-19). Kabotegravir er kjent som en HIV-integrase-strengoverføringshemmer (INSTI), og effekten ved HIV er godt etablert.

Revmatoid artritt er en autoimmun sykdom drevet av cytokiner og betennelse i synovialvev. Det finnes ingen kjent mekanisme som kobler hemming av HIV-integrase til disse prosessene. Den høye TxGNN-scoren (0,9945) kommer fra TxGNN-modellen (dyp læring) og kan gjenspeile likheter modellen har lært mellom beslektede sykdommer, ikke biologisk evidens. Likheten mellom opprinnelig og ny indikasjon er ikke vurdert.

Andre prediksjoner fra modellen er like uten støtte i evidens:

| Rang | Predikert indikasjon | Score | Evidensnivå |
|------|------|------|------|
| 2 | Sklerote­rende kolangitt | 0,9922 | L5 |
| 3 | Bronkitt | 0,9919 | L5 |
| 4 | Kolobomatøs mikroftalmi-rhizomelisk dysplasi-syndrom | 0,9916 | L5 |
| 5 | Alvorlig ikke-proliferativ diabetisk retinopati | 0,9903 | L5 |

For disse er det heller ikke funnet kliniske studier eller litteratur. For skleroserende kolangitt må leversikkerhet og risiko for kolestase vurderes nøye før eventuell videre behandling. Den sjeldne utviklingsforstyrrelsen er sannsynligvis et artefakt av sparsomme nettverksdata.

---

## Klinisk studieevidens

Foreløpig er det ikke registrert noen relaterte kliniske studier.

---

## Litteraturevidens

Foreløpig finnes det ingen relatert litteratur.

---

## Informasjon om det norske markedet

<!-- licenses:begin -->

| Godkjenningsnummer | Preparatnavn (EMA) | Virkestoff(er) (EMA, engelsk) | Terapeutisk område (EMA, engelsk) | Status |
|------|------|------|------|------|
| EMEA/H/C/004976 | Vocabria | cabotegavir sodium; cabotegravir | HIV Infections | Gyldig |
| EMEA/H/C/005756 | Apretude | cabotegravir | HIV Infections | Gyldig |

Kilde: EMA – Medicines output (sentralt godkjente legemidler til mennesker); preparatnavn, virkestoffer og terapeutisk område er gjengitt i engelsk original. Nasjonale markedsføringstillatelser (DMP) og veterinærpreparater er ikke med i disse dataene.

<!-- licenses:end -->

Begge godkjenningene er gyldige, og legemidlet er markedsført i Norge.

---

## Sikkerhetsvurderinger

**Legemiddelinteraksjoner:** Det er funnet 7 interaksjoner med moderat alvorlighetsgrad. Alle gjelder antacida og mineralpreparater som inneholder flerverdige kationer:

- Kalsiumkarbonat
- Aluminiumhydroksid
- Magnesiumkarbonat
- Magnesiumhydroksid
- Magnesiumoksid
- Natriumbikarbonat
- Natriumcitrat

Se preparatomtalen for sikkerhetsinformasjon om advarsler og kontraindikasjoner, da disse ikke er tilgjengelige i dataene som er samlet inn for denne rapporten.

---

## Konklusjon og neste steg

**Beslutning: Hold**

**Begrunnelse:**
Prediksjonen for revmatoid artritt bygger utelukkende på en modellscore uten kliniske studier, litteratur eller kjent mekanistisk sammenheng (evidensnivå L5). Legemidlet er markedsført i Norge, med 2 gyldige markedsføringstillatelser av 2.

**For å gå videre kreves følgende:**
- Data om virkningsmekanisme (MOA) for å kunne vurdere en mulig mekanistisk kobling til autoimmun betennelse
- Preparatomtale med advarsler og kontraindikasjoner, som er nødvendig for sikkerhetsscreening
- Prekliniske data eller litteratursøk som kan gi et første evidensgrunnlag for revmatoid artritt
- Avklaring av administrasjonsvei og formulering (langtidsvirkende injeksjon vs. tabletter) i forhold til behovet ved revmatoid artritt
- Avklaring av regulatorisk status

<!-- review:begin no-lic-20261106-cabotegravir-1 -->

> **Kontrollrettelse (2026-11-06)**: Opprinnelig sto det: «Avklaring av regulatorisk status, siden begge godkjenningene er avregistrert» Fjernet: opplysningen om at godkjenningene er avregistrert eller at ingen gyldig godkjenning finnes, stemte ikke med EMAs data om sentrale EU-godkjenninger (2026-11-06). Oppdaterte antall og statuser for godkjenningene står i hurtigoversikten og i lisenstabellen under markedsinformasjonen. Kilde: [EMA – Medicines output: medicines report](https://www.ema.europa.eu/en/documents/report/medicines-output-medicines-report_en.xlsx); [European Medicines Agency](https://www.ema.europa.eu/).

<!-- review:end no-lic-20261106-cabotegravir-1 -->

<!-- review:begin log -->

## Kontrollogg

Nedenfor er kontrolloggen for denne siden: opplysninger kontrollert mot EMAs data om sentrale EU-godkjenninger. Rettelser gjelder bare grunnleggende faktaopplysninger; modellens prediksjoner, evidensnivåer og konklusjoner er ikke skrevet om. Setningen om at data om virkningsmekanismen ikke var tilgjengelige, er erstattet med et utdrag fra den oppgitte offisielle preparatomtalen (med uoffisiell oversettelse).

| Kontrolldato | Punkt | Tiltak | Kilde |
|------|------|------|------|
| 2026-11-06 | Fjernet: «siden begge godkjenningene er avregistrert» | Rettet (revidert 2026-11-24; tidligere versjon er lagret i posten) | [EMA – Medicines output: medicines report](https://www.ema.europa.eu/en/documents/report/medicines-output-medicines-report_en.xlsx); [European Medicines Agency](https://www.ema.europa.eu/) |
| 2026-11-19 | Setningen «data om virkningsmekanismen er ikke tilgjengelige» erstattet med utdrag fra amerikansk preparatomtale | Setning om manglende data om virkningsmekanismen erstattet med et utdrag med kilde | [DailyMed: Vocabria (cabotegravir sodium) prescribing information, ViiV Healthcare Company](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=66d450fb-cca4-476c-b0c7-c0730e3e4cf3) |

<!-- review:end log -->

## Ansvarsfraskrivelse

Dette innholdet er kun til forskningsformål og utgjør ikke medisinsk rådgivning.
Klinisk validering kreves før enhver klinisk anvendelse.

---

