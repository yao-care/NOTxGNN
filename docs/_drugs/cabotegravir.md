---
layout: default
title: Cabotegravir
parent: Kun modellprediksjon (L5)
nav_order: 75
evidence_level: L5
indication_count: 5
last_modified_at: 2026-10-15
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

Data om virkningsmekanisme er ikke tilgjengelig i dataene som er samlet inn for denne rapporten. Kabotegravir er kjent som en HIV-integrase-strengoverføringshemmer (INSTI), og effekten ved HIV er godt etablert.

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

| Godkjenningsnummer | Produktnavn | Doseringsform | Godkjent indikasjon |
|---------|------|------|-----------|
| EMEA/H/C/005756 | Apretude (godkjent) | – | HIV-infeksjon |
| EMEA/H/C/004976 | Vocabria (godkjent) | – | HIV-infeksjon |

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
- Avklaring av regulatorisk status, siden begge godkjenningene er avregistrert
## Ansvarsfraskrivelse

Dette innholdet er kun til forskningsformål og utgjør ikke medisinsk rådgivning.
Klinisk validering kreves før enhver klinisk anvendelse.

---

