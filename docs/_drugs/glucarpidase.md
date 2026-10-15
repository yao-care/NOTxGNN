---
layout: default
title: Glucarpidase
parent: Kun modellprediksjon (L5)
nav_order: 193
evidence_level: L5
indication_count: 10
---

# Glucarpidase
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

# Glukarpidase: Fra metotreksat-toksisitet til diabetisk katarakt

## Oppsummering

Glukarpidase er et enzym som opprinnelig brukes for å behandle metabolske bivirkninger av legemidler og stoffer, i praksis toksiske metotreksatnivåer. TxGNN-modellen forutsier at det kan ha effekt mot **diabetisk katarakt**, men det finnes **ingen kliniske studier** og **ingen publikasjoner** som støtter denne retningen. Den høye prediksjonsscoren skyldes trolig en artefakt i kunnskapsgrafen, ikke biologisk sannsynlighet.

---

## Hurtigoversikt

| Punkt | Innhold |
|------|------|
| Opprinnelig indikasjon | Metabolske bivirkninger av legemidler og stoffer |
| Predikert ny indikasjon | Diabetisk katarakt |
| TxGNN-prediksjonsscore | 99,85 % |
| Evidensnivå | L5 |
| Markedsstatus i Norge | Kun opphevede godkjenninger |
| Antall godkjenninger | 1 (opphevet) |
| Anbefalt beslutning | Hold |

---

## Hvorfor er (eller er ikke) denne prediksjonen rimelig?

Detaljerte data om virkningsmekanisme er ikke tilgjengelige i datagrunnlaget. Ut fra kjent farmakologi er glukarpidase et rekombinant karboksypeptidase G2-enzym som bryter ned metotreksat utenfor cellene til inaktive metabolitter (DAMPA og glutamat). Det gis intravenøst ved toksiske metotreksatnivåer.

Det er ikke funnet noen troverdig mekanistisk kobling til diabetisk katarakt. Glukarpidase påvirker ikke polyolveien, aldosereduktase eller glykering av linseproteiner. Som et stort protein (ca. 83 kDa dimer) gitt intravenøst er det lite praktisk å nå linsen. Den høye scoren skyldes trolig grafnærhet til den opprinnelige betegnelsen «metabolske bivirkninger», ikke biologisk plausibilitet.

Andre topprangerte prediksjoner (alle med score 99,8 % og evidensnivå L5) gjelder i hovedsak ulike katarakttyper og diabetisk retinopati:

| Rang | Predikert indikasjon | Score |
|------|------|------|
| 2 | Diabetisk retinopati | 99,84 % |
| 3 | Kraniostenose-katarakt | 99,83 % |
| 4 | Tetanisk katarakt | 99,83 % |
| 5 | Katarakt ved diabetes mellitus type 2 | 99,83 % |
| 6 | Umoden katarakt | 99,83 % |
| 7 | Moden katarakt | 99,83 % |
| 8 | Nukleær senil katarakt | 99,83 % |
| 9 | Kortikal katarakt | 99,83 % |
| 10 | Senil katarakt | 99,82 % |

For ingen av disse er det identifisert en mekanistisk begrunnelse. Mønsteret tyder på at prediksjonene stammer fra delte «katarakt»-noder i kunnskapsgrafen.

---

## Klinisk studieevidens

Det er for øyeblikket ingen relaterte kliniske studier registrert.

---

## Litteraturevidens

Det er for øyeblikket ingen relatert litteratur tilgjengelig.

---

## Markedsinformasjon for Norge

| Godkjenningsnummer | Produktnavn | Doseringsform | Godkjent indikasjon |
|---------|------|------|-----------|
| EMEA/H/C/005467 | Voraxaze | – | Metabolske bivirkninger av legemidler og stoffer |

Denne godkjenningen er opphevet, og det finnes ingen gyldige godkjenninger i Norge.

---

## Sikkerhetsmomenter

**Legemiddelinteraksjoner** (8 registrerte, alle av moderat alvorlighetsgrad):

- Proguanil
- Trimetoprim
- Levoleukovorin
- Pemetreksed
- Pralatreksat
- Pyrimetamin
- Leukovorin
- Trimetreksat

Det er ikke tilgjengelig data om advarsler og kontraindikasjoner. Se preparatomtalen for øvrig sikkerhetsinformasjon.

---

## Konklusjon og neste steg

**Beslutning: Hold**

**Begrunnelse:**
Prediksjonen bygger kun på modellscore (evidensnivå L5), uten kliniske studier, litteratur eller troverdig mekanistisk kobling. Systemisk enzymbehandling gitt intravenøst er dessuten dårlig egnet for å nå linsen eller netthinnen. Legemidlet har i tillegg ingen gyldig godkjenning i Norge.

**For å gå videre kreves følgende:**
- Data om virkningsmekanisme (MOA) fra DrugBank
- Advarsler og kontraindikasjoner fra preparatomtalen, som er en forutsetning for sikkerhetsscreening
- Prekliniske data som viser en biologisk sammenheng med linse- eller netthinnepatologi ved diabetes
- Vurdering av administrasjonsvei og tilgang til øyevev
- Avklaring av godkjenningsstatus i Norge
## Ansvarsfraskrivelse

Dette innholdet er kun til forskningsformål og utgjør ikke medisinsk rådgivning.
Klinisk validering kreves før enhver klinisk anvendelse.

---

