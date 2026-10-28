---
layout: default
title: Tezacaftor
parent: Kun modellprediksjon (L5)
nav_order: 414
evidence_level: L5
indication_count: 3
last_modified_at: 2026-10-15
description: "Tezacaftor: predikert ny indikasjon HIV-infeksjon (evidensnivå L5). Opprinnelig indikasjon: Cystisk fibrose"
monitor_inn: "TEZACAFTOR"
predicted_indications: ["HIV infectious disease", "leprosy", "multiple endocrine neoplasia"]
---

# Tezacaftor
{: .fs-9 }

Evidensnivå: **L5** | Predikerte indikasjoner: **3** stk.
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

## Tezacaftor: Fra cystisk fibrose til HIV-infeksjon
{: .text-alpha }

## Oppsummering i én setning

Tezacaftor er en CFTR-korrektor som opprinnelig brukes til behandling av cystisk fibrose, i kombinasjon med andre CFTR-modulatorer. TxGNN-modellen predikerer at legemidlet kan ha effekt mot **HIV-infeksjon**, men det finnes foreløpig **ingen kliniske studier** og **ingen publikasjoner** som støtter denne retningen. Prediksjonen er ren modellbasert (evidensnivå L5).

## Hurtigoversikt

| Punkt | Innhold |
|------|------|
| Opprinnelig indikasjon | Cystisk fibrose |
| Predikert ny indikasjon | HIV-infeksjon |
| TxGNN-prediksjonsscore | 0,9924 |
| Evidensnivå | L5 |
| Markedsstatus i Norge | Markedsført (gyldige tillatelser: 3 av 3) |
| Antall godkjenninger | 3 (gyldige: 3) |
| Anbefalt beslutning | Hold |

## Hvorfor er denne prediksjonen rimelig?

Detaljerte data om virkningsmekanismen (MOA) er for tiden ikke tilgjengelige i datagrunnlaget. Tezacaftor er kjent som en CFTR-korrektor som forbedrer foldingen og transporten av CFTR-proteinet til cellemembranen. Det er godkjent som del av kombinasjonsbehandlinger (Symkevi, Kaftrio, Alyftrek) ved cystisk fibrose.

Det er ikke påvist noen mekanistisk sammenheng mellom CFTR-korreksjon og HIV-patofysiologi (virusreplikasjon, tap av CD4-T-celler). Den høye scoren (0,9924) er en ren beregningsmessig prediksjon, og likheten med den opprinnelige indikasjonen er ikke vurdert. Prediksjonen bør derfor betraktes som en hypotese uten støtte i foreliggende data.

To andre prediksjoner er også generert av modellen, begge med evidensnivå L5 og anbefaling Hold, uten studier eller litteratur:

| Rangering | Predikert indikasjon | TxGNN-score | Kommentar |
|------|------|------|------|
| 2 | Lepra | 0,9914 | Eventuell kobling via vert-patogen-interaksjon eller membranproteintransport er spekulativ og utestet |
| 3 | Multippel endokrin neoplasi | 0,9906 | MEN-syndromer skyldes kimbaneмutasjoner (f.eks. MEN1, RET) som er urelatert til CFTR-korreksjon |

## Kliniske studier

Foreløpig er det ingen registrerte kliniske studier knyttet til denne indikasjonen.

## Litteraturevidens

Foreløpig finnes det ingen relatert litteratur.

## Informasjon om markedet i Norge

| Godkjenningsnummer | Produktnavn | Doseform | Godkjent indikasjon |
|---------|------|------|-----------|
| EMEA/H/C/004682 | Symkevi | – | Cystisk fibrose |
| EMEA/H/C/006382 | Alyftrek | – | Cystisk fibrose |
| EMEA/H/C/005269 | Kaftrio | – | Cystisk fibrose |

Alle tre godkjenningene er registrert som gyldige i datagrunnlaget, og legemidlet er markedsført.

## Sikkerhetsvurderinger

- **Legemiddelinteraksjoner**: Spørringen er gjennomført. Det er kun registrert én farmakologisk oppføring, nemlig målproteinet CFTR (tezacaftor virker på dette). Dette er ikke en klinisk legemiddelinteraksjon, og ingen alvorlighetsgrad er angitt.

Se preparatomtalen (SPC) for øvrig sikkerhetsinformasjon, inkludert advarsler og kontraindikasjoner.

## Konklusjon og neste steg

**Beslutning: Hold**

**Begrunnelse:**
Prediksjonen om HIV-infeksjon bygger kun på en modellscore, uten kliniske studier, litteratur eller en plausibel mekanistisk kobling. I tillegg er alle norske/europeiske godkjenninger i datagrunnlaget registrert som kansellert.

**For å gå videre kreves følgende:**
- Data om virkningsmekanisme (MOA) fra DrugBank for å kunne analysere mulige mekanistiske koblinger
- Advarsler og kontraindikasjoner fra preparatomtalen, slik at sikkerhetsscreening kan gjennomføres
- Prekliniske data (f.eks. in vitro-studier av tezacaftor i HIV-modeller) som kan gi grunnlag for en mekanistisk hypotese
- Avklaring av den nåværende markedsstatusen for tezacaftor-holdige preparater i Norge
- Vurdering av administrasjonsvei og forenlighet med den nye indikasjonen
## Ansvarsfraskrivelse

Dette innholdet er kun til forskningsformål og utgjør ikke medisinsk rådgivning.
Klinisk validering kreves før enhver klinisk anvendelse.

---

