---
layout: default
title: Vilanterol
parent: Kun modellprediksjon (L5)
nav_order: 451
evidence_level: L5
indication_count: 6
monitor_inn: "VILANTEROL"
predicted_indications: ["hyperlucent lung", "tracheal stenosis", "bronchial neoplasm (disease)", "respiratory malformation", "tracheal calcification", "laryngotracheitis"]
last_modified_at: 2026-11-24
description: "Vilanterol: predikert ny indikasjon Hyperlusent lunge (hyperlucent lung) (evidensnivå L5). Opprinnelig indikasjon: Pulmonary Disease, Chronic Obstructive"
---

# Vilanterol
{: .fs-9 }

Evidensnivå: **L5** | Predikerte indikasjoner: **6** stk.
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

## Vilanterol: langtidsvirkende beta2-agonist → hyperlusent lunge (hyperlucent lung)
{: .text-alpha }

## Oppsummering i én setning

Vilanterol er en inhalert langtidsvirkende beta2-agonist som brukes i kombinasjonspreparater mot kronisk obstruktiv lungesykdom.
TxGNN-modellen predikerer at legemidlet kan være aktuelt for **hyperlusent lunge (hyperlucent lung)**, men det finnes **ingen kliniske studier og ingen publikasjoner** som støtter denne retningen. Prediksjonen bygger kun på modellen.

## Hurtigoversikt

| Punkt | Innhold |
|------|------|
| Opprinnelig indikasjon | Pulmonary Disease, Chronic Obstructive |
| Predikert ny indikasjon | Hyperlusent lunge (hyperlucent lung) |
| TxGNN-prediksjonsscore | 0,9972 |
| Evidensnivå | L5 |
| Markedsstatus i Norge | Markedsført (gyldige tillatelser: 2 av 2) |
| Antall godkjenninger | 2 (gyldige: 2) |
| Anbefalt beslutning | Hold |

## Hvorfor kan denne prediksjonen være rimelig?

Ifølge avsnittet «Mechanism of Action» i preparatomtalen som er godkjent av amerikanske FDA (Prescribing Information), for fluticasone furoate and vilanterol (kombinasjonspreparat med Vilanterol) (uoffisiell oversettelse): «De farmakologiske effektene av beta 2-adrenerge agonister, inkludert vilanterol, kan i det minste delvis tilskrives stimulering av intracellulær adenylatsyklase, enzymet som katalyserer omdannelsen av adenosintrifosfat (ATP) til syklisk 3′,5′-adenosinmonofosfat (syklisk AMP).» Engelsk originaltekst: "The pharmacologic effects of beta 2 -adrenergic agonist drugs, including vilanterol, are at least in part attributable to stimulation of intracellular adenyl cyclase, the enzyme that catalyzes the conversion of adenosine triphosphate (ATP) to cyclic-3′,5′-adenosine monophosphate (cyclic AMP)." ([DailyMed: fluticasone furoate and vilanterol prescribing information, Prasco Laboratories](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=3a761487-c300-451a-8537-3196c00c11b5), versjon av 2024-11-21; hentet 2026-11-19). Vilanterol tilhører klassen inhalerte langtidsvirkende beta2-agonister, som gir bronkodilatasjon ved å slappe av glatt muskulatur i luftveiene. Dette er en klassebasert antakelse, ikke noe som er dokumentert i dataene som er samlet for denne rapporten.

Hyperlusent lunge er et radiologisk funn som kan henge sammen med obstruktiv lungesykdom. En eventuell kobling til vilanterol vil være indirekte, via den underliggende luftveisobstruksjonen. Det er ikke påvist noen direkte mekanistisk eller klinisk sammenheng, og prediksjonen må betraktes som en hypotese.

## Kliniske studier

Foreløpig er det ikke registrert noen relaterte kliniske studier.

## Litteraturevidens

Foreløpig finnes det ingen relevant litteratur.

## Markedsinformasjon for Norge

<!-- licenses:begin -->

| Godkjenningsnummer | Preparatnavn (EMA) | Virkestoff(er) (EMA, engelsk) | Terapeutisk område (EMA, engelsk) | Status |
|------|------|------|------|------|
| EMEA/H/C/002673 | Relvar Ellipta | fluticasone furoate; vilanterol | Pulmonary Disease, Chronic Obstructive | Gyldig |
| EMEA/H/C/003754 | Laventair Ellipta (previously Laventair) | umeclidinium bromide; vilanterol | Pulmonary Disease, Chronic Obstructive | Gyldig |

Kilde: EMA – Medicines output (sentralt godkjente legemidler til mennesker); preparatnavn, virkestoffer og terapeutisk område er gjengitt i engelsk original. Nasjonale markedsføringstillatelser (DMP) og veterinærpreparater er ikke med i disse dataene.

<!-- licenses:end -->

## Sikkerhetsmomenter

Det finnes ikke tilgjengelige data om advarsler eller kontraindikasjoner. Se preparatomtalen (pakningsvedlegget) for sikkerhetsinformasjon.

**Legemiddelinteraksjoner** (100 interaksjoner registrert; et utvalg vises):
- **Moderat:** akarbose, albiglutid, alogliptin, kanagliflozin, klorpropamid, cisaprid, klaritromycin, dapagliflozin, dietylpropion, dolasetron, dulaglutid, empagliflozin, efedrin, adrenalin (epinefrin)
- **Mindre:** beklometasondipropionat, betametason, budesonid, deksametason

## Konklusjon og neste steg

**Beslutning: Hold**

**Begrunnelse:**
Prediksjonen har høy modellscore, men ingen kliniske studier eller litteratur som direkte undersøker hyperlusent lunge, og evidensnivået er derfor L5. Den mulige koblingen til vilanterol er indirekte og mekanistisk svak.

**For å gå videre kreves følgende:**
- Data om virkningsmekanisme (MOA)
- Gjennomgang av preparatomtalens advarsler og kontraindikasjoner
- Klinisk eller epidemiologisk evidens som direkte kobler bronkodilatasjon med vilanterol til hyperlusent lunge
- Avklaring av om en klinisk relevant endepunktdefinisjon finnes for et radiologisk funn som dette

<!-- review:begin log -->

## Kontrollogg

Nedenfor er gjennomgangsloggen for denne siden. Setningen om at data om virkningsmekanismen ikke var tilgjengelige, er erstattet med et utdrag fra den oppgitte offisielle preparatomtalen (med uoffisiell oversettelse); modellprediksjoner, evidensnivåer og konklusjoner er ikke omskrevet.

| Kontrolldato | Punkt | Tiltak | Kilde |
|------|------|------|------|
| 2026-11-19 | Setningen «data om virkningsmekanismen er ikke tilgjengelige» erstattet med utdrag fra amerikansk preparatomtale | Setning om manglende data om virkningsmekanismen erstattet med et utdrag med kilde | [DailyMed: fluticasone furoate and vilanterol prescribing information, Prasco Laboratories](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=3a761487-c300-451a-8537-3196c00c11b5) |

<!-- review:end log -->

## Ansvarsfraskrivelse

Dette innholdet er kun til forskningsformål og utgjør ikke medisinsk rådgivning.
Klinisk validering kreves før enhver klinisk anvendelse.

---

