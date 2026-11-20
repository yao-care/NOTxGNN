---
layout: default
title: Caspofungin
parent: Kun modellprediksjon (L5)
nav_order: 86
evidence_level: L5
indication_count: 1
last_modified_at: 2026-11-20
description: "Caspofungin: predikert ny indikasjon Abnormal gastrinsekresjon (gastrin secretion abnormality) (evidensnivå L5). Opprinnelig indikasjon: Candidiasis og aspergillose"
monitor_inn: "CASPOFUNGIN"
predicted_indications: ["gastrin secretion abnormality"]
---

# Caspofungin
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

## Kaspofungin: Fra candidiasis og aspergillose til abnormal gastrinsekresjon
{: .text-alpha }

## Oppsummering i én setning

Kaspofungin er et soppdrepende legemiddel (echinocandin) som opprinnelig brukes til behandling av candidiasis og aspergillose. TxGNN-modellen forutsier at det kan ha effekt ved **abnormal gastrinsekresjon**, men det finnes foreløpig **ingen kliniske studier** og **ingen publikasjoner** som støtter denne retningen. Prediksjonen bygger kun på modellen.

---

## Hurtigoversikt

| Punkt | Innhold |
|------|------|
| Opprinnelig indikasjon | Candidiasis og aspergillose |
| Predikert ny indikasjon | Abnormal gastrinsekresjon (gastrin secretion abnormality) |
| TxGNN-prediksjonsscore | 0,9944 |
| Evidensnivå | L5 |
| Markedsstatus i Norge | Markedsført (gyldige tillatelser: 1 av 1) |
| Antall godkjenninger | 1 (gyldige: 1) |
| Anbefalt beslutning | Hold |

---

## Hvorfor er denne prediksjonen (ikke) rimelig?

Ifølge avsnittene «Mechanism of Action» og «Microbiology» i preparatomtalen som er godkjent av amerikanske FDA (Prescribing Information), for Caspofungin (uoffisiell oversettelse): «Kaspofungin er et antimykotisk legemiddel av typen ekinokandin. […] Kaspofungin, et ekinokandin, hemmer syntesen av beta (1,3)-D-glukan, en essensiell komponent i celleveggen hos følsomme Aspergillus-arter og Candida-arter. Beta (1,3)-D-glukan finnes ikke i pattedyrceller.» Engelsk originaltekst: "Caspofungin is an echinocandin antifungal drug. […] Caspofungin, an echinocandin, inhibits the synthesis of beta (1,3)-D-glucan, an essential component of the cell wall of susceptible Aspergillus species and Candida species. Beta (1,3)-D-glucan is not present in mammalian cells." ([DailyMed: Cancidas (caspofungin acetate) prescribing information, Merck Sharp & Dohme LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=3bad23a6-09a6-4194-9182-093ed61bc71c), versjon av 2024-10-11; hentet 2026-11-19). Kaspofungin er likevel kjent som et echinocandin som hemmer beta-(1,3)-D-glukansyntase og dermed forstyrrer oppbyggingen av soppens cellevegg.

Pattedyrceller har ingen cellevegg av beta-glukan. Det er heller ingen kjent mekanisme som knytter denne virkningen til regulering av gastrin, funksjonen til G-celler eller utskillelse av magesyre. Det er derfor ikke etablert noen mekanistisk sammenheng mellom den opprinnelige indikasjonen (soppinfeksjoner) og den predikerte indikasjonen (forstyrrelse av gastrinsekresjon).

Den høye scoren (0,9944) er en ren prediksjon fra TxGNN-modellen (dyp læring). Den kan skyldes nærhet i nettverket eller delte assosiasjoner med andre legemidler eller gener, og har ingen støtte i kliniske eller farmakologiske data. Ifølge avsnittene «Mechanism of Action» og «Microbiology» i preparatomtalen som er godkjent av amerikanske FDA (Prescribing Information), for Caspofungin (uoffisiell oversettelse): «Kaspofungin er et antimykotisk legemiddel av typen ekinokandin. […] Kaspofungin, et ekinokandin, hemmer syntesen av beta (1,3)-D-glukan, en essensiell komponent i celleveggen hos følsomme Aspergillus-arter og Candida-arter. Beta (1,3)-D-glukan finnes ikke i pattedyrceller.» Engelsk originaltekst: "Caspofungin is an echinocandin antifungal drug. […] Caspofungin, an echinocandin, inhibits the synthesis of beta (1,3)-D-glucan, an essential component of the cell wall of susceptible Aspergillus species and Candida species. Beta (1,3)-D-glucan is not present in mammalian cells." ([DailyMed: Cancidas (caspofungin acetate) prescribing information, Merck Sharp & Dohme LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=3bad23a6-09a6-4194-9182-093ed61bc71c), versjon av 2024-10-11; hentet 2026-11-20). Likhet med den opprinnelige indikasjonen og forenlighet med administrasjonsvei er ikke vurdert.

---

## Klinisk evidens

Foreløpig er det ingen relaterte kliniske studier registrert.

---

## Litteraturevidens

Foreløpig finnes det ingen relatert litteratur.

---

## Markedsinformasjon for Norge

| Godkjenningsnummer | Produktnavn | Doseringsform | Godkjent indikasjon |
|---------|------|------|-----------|
| EMEA/H/C/000379 | Cancidas (tidligere Caspofungin MSD), Merck Sharp & Dohme B.V. | – | Candidiasis; aspergillose |

Legemidlet er markedsført, og 1 av 1 godkjenning er gyldig.

---

## Cytotoksisitet

Kaspofungin er ikke et antineoplastisk legemiddel. Denne delen er derfor ikke relevant.

---

## Sikkerhetsvurderinger

- **Kontraindikasjoner fra kunnskapsgrafen** (kontraindikasjonskoblinger i TxGNN-kunnskapsgrafen, ikke tekst fra preparatomtale): leversykdom, gallblæresykdom og kaliummangel.
- **Legemiddelinteraksjoner:** 81 interaksjoner er identifisert. De viktigste:
  - **Alvorlig (Major):** deksametason
  - **Moderat:** naltrekson
  - Øvrige interaksjoner har ukjent alvorlighetsgrad, blant annet kalsitriol, pantoprazol, omeprazol, lansoprazol, doksycyklin, morfin, vankomycin, sukralfat, laktulose, prednison, prednisolon, hydrokortison, simvastatin, nystatin, epinefrin, amfotericin B, mannitol og kaliumklorid.

For øvrig sikkerhetsinformasjon (advarsler og kontraindikasjoner fra preparatomtalen), se preparatomtalen.

---

## Konklusjon og neste steg

**Beslutning: Hold**

**Begrunnelse:**
Prediksjonen er kun modellbasert (L5) uten kliniske studier eller litteratur. Det finnes heller ingen kjent mekanistisk kobling mellom hemming av soppens glukansyntase og gastrinregulering. I tillegg er den norske godkjenningen kansellert.

**For å gå videre kreves følgende:**
- Hente og analysere preparatomtalen for advarsler og kontraindikasjoner (nødvendig før sikkerhetsscreening)
- Dokumentere virkningsmekanismen (MOA) fra DrugBank
- Prekliniske eller mekanistiske data som kan underbygge en kobling til gastrinsekresjon
- Gjennomgang av litteratur og studieregistre for evidens ved gastrinrelaterte tilstander
- Vurdere administrasjonsvei og forenlighet med den nye indikasjonen

<!-- review:begin log -->

## Kontrollogg

Nedenfor er gjennomgangsloggen for denne siden. Setningen om at data om virkningsmekanismen ikke var tilgjengelige, er erstattet med et utdrag fra den oppgitte offisielle preparatomtalen (med uoffisiell oversettelse); modellprediksjoner, evidensnivåer og konklusjoner er ikke omskrevet.

| Kontrolldato | Punkt | Tiltak | Kilde |
|------|------|------|------|
| 2026-11-19 | Setningen «data om virkningsmekanismen er ikke tilgjengelige» erstattet med utdrag fra amerikansk preparatomtale | Setning om manglende data om virkningsmekanismen erstattet med et utdrag med kilde | [DailyMed: Cancidas (caspofungin acetate) prescribing information, Merck Sharp & Dohme LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=3bad23a6-09a6-4194-9182-093ed61bc71c) |
| 2026-11-20 | Setningen «data om virkningsmekanismen er ikke tilgjengelige» erstattet med utdrag fra amerikansk preparatomtale | Setning om manglende data om virkningsmekanismen erstattet med et utdrag med kilde | [DailyMed: Cancidas (caspofungin acetate) prescribing information, Merck Sharp & Dohme LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=3bad23a6-09a6-4194-9182-093ed61bc71c) |

<!-- review:end log -->

## Ansvarsfraskrivelse

Dette innholdet er kun til forskningsformål og utgjør ikke medisinsk rådgivning.
Klinisk validering kreves før enhver klinisk anvendelse.

---

