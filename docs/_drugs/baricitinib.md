---
layout: default
title: Baricitinib
parent: Kun modellprediksjon (L5)
nav_order: 52
evidence_level: L5
indication_count: 2
last_modified_at: 2026-11-24
description: "Baricitinib: predikert ny indikasjon Kolobomatøs mikroftalmi-rhizomelisk dysplasi-syndrom (evidensnivå L5). Opprinnelig indikasjon: Revmatoid artritt"
monitor_inn: "BARICITINIB"
predicted_indications: ["colobomatous microphthalmia-rhizomelic dysplasia syndrome", "brachydactyly-syndactyly syndrome"]
---

# Baricitinib
{: .fs-9 }

Evidensnivå: **L5** | Predikerte indikasjoner: **2** stk.
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

## Baricitinib: Fra revmatoid artritt til kolobomatøs mikroftalmi-rhizomelisk dysplasi-syndrom
{: .text-alpha }

## Oppsummering i én setning

Baricitinib er et legemiddel som opprinnelig brukes til behandling av revmatoid artritt.
TxGNN-modellen forutsier at det kan være effektivt mot **kolobomatøs mikroftalmi-rhizomelisk dysplasi-syndrom**, men det finnes foreløpig **0 kliniske studier** og **0 publikasjoner** som støtter denne retningen. Prediksjonen bygger kun på modellens skår.

---

## Hurtigoversikt

| Punkt | Innhold |
|------|------|
| Opprinnelig indikasjon | Revmatoid artritt |
| Predikert ny indikasjon | Kolobomatøs mikroftalmi-rhizomelisk dysplasi-syndrom |
| TxGNN-prediksjonsskår | 0,9994 |
| Evidensnivå | L5 |
| Markedsstatus i Norge | Markedsført (gyldige tillatelser: 1 av 1) |
| Antall godkjenninger | 1 (gyldige: 1) |
| Anbefalt beslutning | Hold |

---

## Hvorfor er denne prediksjonen rimelig (eller ikke)?

Ifølge avsnittet «Mechanism of Action» i preparatomtalen som er godkjent av amerikanske FDA (Prescribing Information), for Baricitinib (uoffisiell oversettelse): «Baricitinib er en Janus-kinase (JAK)-hemmer. JAK er intracellulære enzymer som overfører signaler fra cytokin- eller vekstfaktor-reseptorinteraksjoner på cellemembranen for å påvirke cellulære prosesser i hematopoesen og immuncellefunksjonen.» Engelsk originaltekst: "Baricitinib is a Janus kinase (JAK) inhibitor. JAKs are intracellular enzymes which transmit signals arising from cytokine or growth factor-receptor interactions on the cellular membrane to influence cellular processes of hematopoiesis and immune cell function." ([DailyMed: Olumiant (baricitinib) prescribing information, Eli Lilly and Company](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=866e9f35-9035-4581-a4b1-75a621ab55cf), versjon av 2026-10-09; hentet 2026-11-19). Baricitinib er generelt kjent som en JAK1/JAK2-hemmer, og effekten ved revmatoid artritt skyldes dempet immunsignalering via JAK-STAT-banen.

Den predikerte sykdommen er et ekstremt sjeldent utviklingssyndrom. Det foreligger ingen opplysninger i dataene som tilsier at JAK-STAT-signalering spiller en rolle i sykdommens patogenese. Det kan derfor ikke etableres noen mekanistisk kobling mellom den opprinnelige og den nye indikasjonen.

Den svært høye skåren (0,9994) er en ren modellbasert prediksjon uten støtte i kliniske studier eller litteratur. Den bør betraktes som et hypotesegenererende signal, ikke som bevis for effekt.

---

## Klinisk studieevidens

Det er for øyeblikket ingen relaterte kliniske studier registrert.

---

## Litteraturevidens

Det er for øyeblikket ingen relatert litteratur tilgjengelig.

---

## Informasjon om det norske markedet

<!-- licenses:begin -->

| Godkjenningsnummer | Preparatnavn (EMA) | Virkestoff(er) (EMA, engelsk) | Terapeutisk område (EMA, engelsk) | Status |
|------|------|------|------|------|
| EMEA/H/C/004085 | Olumiant | Baricitinib | Arthritis, Rheumatoid | Gyldig |

Kilde: EMA – Medicines output (sentralt godkjente legemidler til mennesker); preparatnavn, virkestoffer og terapeutisk område er gjengitt i engelsk original. Nasjonale markedsføringstillatelser (DMP) og veterinærpreparater er ikke med i disse dataene.

<!-- licenses:end -->

Merk: Denne godkjenningen har status gyldig, og legemidlet er markedsført. 1 av 1 godkjenninger er gyldig i dataene.

---

## Sikkerhetsvurderinger

**Legemiddelinteraksjoner**: Det er funnet 100 registrerte interaksjoner (20 vist i de innsamlede dataene). Viktigste funn:

- **Alvorlig (Major)**: kortikosteroider (hydrokortison, triamcinolon, betametason, budesonid, deksametason, prednisolon, prednison, oftalmisk triamcinolon), samt deferipron, ibritumomab tiuxetan, jobenguan (I-131) og tositumomab (I-131).
- **Moderat**: morfin (inkl. liposomal), acetylsalisylsyre, nitisinon og opium.
- **Mild (Minor)**: sinkacetat, sinkglukonat og sinksulfat.

For øvrig sikkerhetsinformasjon, se preparatomtalen.

---

## Konklusjon og neste steg

**Beslutning: Hold**

**Begrunnelse:**
Prediksjonen støttes kun av modellskår (evidensnivå L5), uten kliniske studier, litteratur eller kjent mekanistisk kobling til en utviklingsforstyrrelse. Den norske godkjenningen er i tillegg kansellert, og sikkerhetsdata fra preparatomtalen mangler.

**For å gå videre kreves følgende:**
- Data om virkningsmekanisme (MOA) fra DrugBank
- Advarsler og kontraindikasjoner fra preparatomtalen
- Biologisk belegg for at JAK-STAT-signalering er involvert i sykdommen
- Prekliniske studier eller litteraturgjennomgang som kan støtte hypotesen
- Avklaring av administrasjonsvei og markedstilgjengelighet

<!-- review:begin log -->

## Kontrollogg

Nedenfor er gjennomgangsloggen for denne siden. Setningen om at data om virkningsmekanismen ikke var tilgjengelige, er erstattet med et utdrag fra den oppgitte offisielle preparatomtalen (med uoffisiell oversettelse); modellprediksjoner, evidensnivåer og konklusjoner er ikke omskrevet.

| Kontrolldato | Punkt | Tiltak | Kilde |
|------|------|------|------|
| 2026-11-19 | Setningen «data om virkningsmekanismen er ikke tilgjengelige» erstattet med utdrag fra amerikansk preparatomtale | Setning om manglende data om virkningsmekanismen erstattet med et utdrag med kilde | [DailyMed: Olumiant (baricitinib) prescribing information, Eli Lilly and Company](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=866e9f35-9035-4581-a4b1-75a621ab55cf) |

<!-- review:end log -->

## Ansvarsfraskrivelse

Dette innholdet er kun til forskningsformål og utgjør ikke medisinsk rådgivning.
Klinisk validering kreves før enhver klinisk anvendelse.

---

