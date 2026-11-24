---
layout: default
title: Lapatinib
parent: Kun modellprediksjon (L5)
nav_order: 232
evidence_level: L5
indication_count: 1
monitor_inn: "LAPATINIB"
predicted_indications: ["dermatofibrosarcoma protuberans"]
last_modified_at: 2026-11-24
description: "Lapatinib: predikert ny indikasjon Dermatofibrosarcoma protuberans (evidensnivå L5). Opprinnelig indikasjon: Breast Neoplasms"
---

# Lapatinib
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

## Lapatinib: tyrosinkinasehemmer (EGFR/HER2) → Dermatofibrosarcoma protuberans (dermatofibrosarcoma protuberans)
{: .text-alpha }

## Oppsummering i én setning

Lapatinib er en tyrosinkinasehemmer som hemmer EGFR og HER2. TxGNN-modellen predikerer at legemidlet kan ha effekt ved **dermatofibrosarcoma protuberans (dermatofibrosarcoma protuberans)**, men i dataene som er samlet inn for denne rapporten finnes **ingen kliniske studier og ingen publikasjoner** som støtter denne retningen.

---

## Hurtigoversikt

| Punkt | Innhold |
|------|------|
| Opprinnelig indikasjon | Breast Neoplasms |
| Predikert ny indikasjon | Dermatofibrosarcoma protuberans (dermatofibrosarcoma protuberans) |
| TxGNN-prediksjonsscore | 0,9930 |
| Evidensnivå | L5 |
| Markedsstatus i Norge | Markedsført (gyldige tillatelser: 1 av 1) |
| Antall godkjenninger | 1 (gyldige: 1) |
| Anbefalt beslutning | Hold |

---

## Hvorfor er denne prediksjonen rimelig?

Ifølge avsnittet «Mechanism of Action» i preparatomtalen som er godkjent av amerikanske FDA (Prescribing Information), for Lapatinib (uoffisiell oversettelse): «Lapatinib er en 4-anilinokinazolin-kinasehemmer av de intracellulære tyrosinkinasedomenene til både epidermal vekstfaktorreseptor (EGFR [ErbB1]) og human epidermal reseptor type 2 (HER2 [ErbB2]) (estimerte K i app-verdier på henholdsvis 3nM og 13nM), med en dissosiasjonshalveringstid på 300 minutter eller mer. Lapatinib hemmer ErbB-drevet tumorcellevekst in vitro og i ulike dyremodeller.» Engelsk originaltekst: "Lapatinib is a 4-anilinoquinazoline kinase inhibitor of the intracellular tyrosine kinase domains of both Epidermal Growth Factor Receptor (EGFR [ErbB1]) and of Human Epidermal Receptor Type 2 (HER2 [ErbB2]) receptors (estimated K i app values of 3nM and 13nM, respectively) with a dissociation half-life of greater than or equal to 300 minutes. Lapatinib inhibits ErbB-driven tumor cell growth in vitro and in various animal models." ([DailyMed: Tykerb (lapatinib) prescribing information, Novartis Pharmaceuticals Corporation](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=eee37f88-ec6a-4c30-b8aa-e2c71f93088c), versjon av 2026-01-27; hentet 2026-11-19). Lapatinib er kjent som en dobbel hemmer av tyrosinkinasene EGFR og HER2.

Dermatofibrosarcoma protuberans (DFSP) drives hovedsakelig av en COL1A1-PDGFB-fusjon som gir vedvarende aktivering av PDGFR-beta, og behandles med imatinib, en PDGFR-hemmer. En direkte mekanistisk kobling mellom EGFR/HER2-hemming og DFSP er derfor ikke etablert ut fra de tilgjengelige dataene.

Eventuelle koblinger er spekulative, for eksempel via felles nedstrøms signalveier (PI3K/AKT eller MAPK) eller mulig off-target kinaseaktivitet, og må kontrolleres mot primærkilder. Den høye scoren gjenspeiler trolig nærhet i modellens nettverk (felles kinasemål eller relaterte tumorassosiasjoner) snarere enn validert biologi.

---

## Evidens fra kliniske studier

Foreløpig er ingen relevante kliniske studier registrert.

---

## Litteraturevidens

Foreløpig er ingen relevant litteratur tilgjengelig.

---

## Markedsinformasjon for Norge

<!-- licenses:begin -->

| Godkjenningsnummer | Preparatnavn (EMA) | Virkestoff(er) (EMA, engelsk) | Terapeutisk område (EMA, engelsk) | Status |
|------|------|------|------|------|
| EMEA/H/C/000795 | Tyverb | lapatinib | Breast Neoplasms | Gyldig |

Kilde: EMA – Medicines output (sentralt godkjente legemidler til mennesker); preparatnavn, virkestoffer og terapeutisk område er gjengitt i engelsk original. Nasjonale markedsføringstillatelser (DMP) og veterinærpreparater er ikke med i disse dataene.

<!-- licenses:end -->

---

## Cytotoksisitet

| Punkt | Innhold |
|------|------|
| Cytotoksisitetsklassifisering | Målrettet behandling (tyrosinkinasehemmer) |
| Risiko for myelosuppresjon | Se preparatomtalen for advarsler og forholdsregler |
| Emetogenisitet | Se preparatomtalen for advarsler og forholdsregler |
| Overvåkingspunkter | Se preparatomtalen; leverfunksjon, hjertefunksjon (QT/ejeksjonsfraksjon) og elektrolytter er relevante ut fra de registrerte kontraindikasjonsrelasjonene |
| Håndteringsbeskyttelse | Se preparatomtalen for gjeldende retningslinjer for håndtering av kreftlegemidler |

---

## Sikkerhetsvurderinger

- **Sykdommer med registrert kontraindikasjonsrelasjon (ikke fra preparatomtale):** langt QT-syndrom, familiært langt QT-syndrom, torsades de pointes, leversvikt, kaliummangel, interstitiell lungesykdom, legemiddelindusert leverskade, hjertesvikt.
- **Legemiddelinteraksjoner:** 100 interaksjoner er registrert. Alvorlige (Major) interaksjoner omfatter blant annet:
  - Loperamid
  - Klaritromycin

  Moderate interaksjoner omfatter blant annet syrehemmere (famotidin, ranitidin, omeprazol, rabeprazol, cimetidin, dekslansoprazol), kortikosteroider (hydrokortison, deksametason, betametason, budesonid, triamcinolon), pioglitazon, aprepitant, saksagliptin og avføringsmidler (bisakodyl, pikosulfat, polyetylenglykol).

Opplysninger om advarsler og kontraindikasjoner fra preparatomtalen mangler; se preparatomtalen for fullstendig sikkerhetsinformasjon.

---

## Konklusjon og neste steg

**Beslutning: Hold**

**Begrunnelse:**
Prediksjonen bygger kun på en høy modellscore (0,9930). Det finnes ingen kliniske studier eller publikasjoner for dette legemiddel-sykdomsparet, og det er ingen etablert mekanistisk kobling mellom EGFR/HER2-hemming og DFSP, som er PDGFR-drevet.

**For å gå videre kreves følgende:**
- Systematisk litteratursøk og gjennomgang av primærkilder for lapatinib ved DFSP, inkludert prekliniske data
- Mekanistisk vurdering av om EGFR/HER2-signalering har noen rolle i DFSP
- Data om virkningsmekanisme (MOA) for lapatinib
- Preparatomtale med advarsler og kontraindikasjoner for sikkerhetsscreening, særlig mht. QT-forlengelse, lever- og hjertetoksisitet
- Vurdering av ruteforenlighet og likhet med opprinnelig bruk

<!-- review:begin log -->

## Kontrollogg

Nedenfor er gjennomgangsloggen for denne siden. Setningen om at data om virkningsmekanismen ikke var tilgjengelige, er erstattet med et utdrag fra den oppgitte offisielle preparatomtalen (med uoffisiell oversettelse); modellprediksjoner, evidensnivåer og konklusjoner er ikke omskrevet.

| Kontrolldato | Punkt | Tiltak | Kilde |
|------|------|------|------|
| 2026-11-19 | Setningen «data om virkningsmekanismen er ikke tilgjengelige» erstattet med utdrag fra amerikansk preparatomtale | Setning om manglende data om virkningsmekanismen erstattet med et utdrag med kilde | [DailyMed: Tykerb (lapatinib) prescribing information, Novartis Pharmaceuticals Corporation](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=eee37f88-ec6a-4c30-b8aa-e2c71f93088c) |

<!-- review:end log -->

## Ansvarsfraskrivelse

Dette innholdet er kun til forskningsformål og utgjør ikke medisinsk rådgivning.
Klinisk validering kreves før enhver klinisk anvendelse.

---

