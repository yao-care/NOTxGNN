---
layout: default
title: Tezacaftor
parent: Kun modellprediksjon (L5)
nav_order: 414
evidence_level: L5
indication_count: 3
last_modified_at: 2026-11-20
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

Ifølge avsnittet «Mechanism of Action» i preparatomtalen som er godkjent av amerikanske FDA (Prescribing Information), for vanzacaftor, tezacaftor, and deutivacaftor (kombinasjonspreparat med Tezacaftor) (uoffisiell oversettelse): «Vanzakaftor og tezakaftor bindes til ulike seter på CFTR-proteinet og har en additiv effekt når det gjelder å fremme cellulær prosessering og transport av utvalgte mutante former av CFTR (inkludert F508del-CFTR), slik at mengden CFTR-protein som leveres til celleoverflaten øker sammenlignet med hvert av molekylene alene. Den kombinerte effekten av vanzakaftor, tezakaftor og deutivakaftor er økt mengde og funksjon av CFTR på celleoverflaten, noe som gir økt CFTR-aktivitet målt både ved CFTR-mediert kloridtransport in vitro og ved svettekloridkonsentrasjon hos pasienter med CF.» Engelsk originaltekst: "Vanzacaftor and tezacaftor bind to different sites on the CFTR protein and have an additive effect in facilitating the cellular processing and trafficking of select mutant forms of CFTR (including F508del- CFTR) to increase the amount of CFTR protein delivered to the cell surface compared to either molecule alone. The combined effect of vanzacaftor, tezacaftor and deutivacaftor is increased quantity and function of CFTR at the cell surface, resulting in increased CFTR activity as measured both by CFTR-mediated chloride transport in vitro and by sweat chloride in patients with CF." ([DailyMed: Alyftrek (vanzacaftor, tezacaftor, and deutivacaftor) prescribing information, Vertex Pharmaceuticals Incorporated](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=7e635909-c6fd-4f0d-ae77-cdff03653a20), versjon av 2026-08-26; hentet 2026-11-19). Tezacaftor er kjent som en CFTR-korrektor som forbedrer foldingen og transporten av CFTR-proteinet til cellemembranen. Det er godkjent som del av kombinasjonsbehandlinger (Symkevi, Kaftrio, Alyftrek) ved cystisk fibrose.

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

<!-- review:begin log -->

## Kontrollogg

Nedenfor er gjennomgangsloggen for denne siden. Setningen om at data om virkningsmekanismen ikke var tilgjengelige, er erstattet med et utdrag fra den oppgitte offisielle preparatomtalen (med uoffisiell oversettelse); modellprediksjoner, evidensnivåer og konklusjoner er ikke omskrevet.

| Kontrolldato | Punkt | Tiltak | Kilde |
|------|------|------|------|
| 2026-11-19 | Setningen «data om virkningsmekanismen er ikke tilgjengelige» erstattet med utdrag fra amerikansk preparatomtale | Setning om manglende data om virkningsmekanismen erstattet med et utdrag med kilde | [DailyMed: Alyftrek (vanzacaftor, tezacaftor, and deutivacaftor) prescribing information, Vertex Pharmaceuticals Incorporated](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=7e635909-c6fd-4f0d-ae77-cdff03653a20) |

<!-- review:end log -->

## Ansvarsfraskrivelse

Dette innholdet er kun til forskningsformål og utgjør ikke medisinsk rådgivning.
Klinisk validering kreves før enhver klinisk anvendelse.

---

