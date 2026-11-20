---
layout: default
title: Etanercept
parent: Kun modellprediksjon (L5)
nav_order: 164
evidence_level: L5
indication_count: 3
monitor_inn: "ETANERCEPT"
predicted_indications: ["hypermobility of coccyx", "Kummell disease", "vertebral disease"]
last_modified_at: 2026-10-28
description: "Etanercept: predikert ny indikasjon Hypermobilitet i halebenet (hypermobility of coccyx) (evidensnivå L5). Opprinnelig indikasjon: Arthritis, Rheumatoid"
---

# Etanercept
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

## Etanercept: TNF-hemmer (løselig TNF-reseptor-fusjonsprotein) → Hypermobilitet i halebenet (hypermobility of coccyx)
{: .text-alpha }

## Oppsummering i en setning

Etanercept er et biologisk legemiddel som blokkerer tumornekrosefaktor (TNF) og brukes ved flere betennelsessykdommer. TxGNN-modellen forutsier at det kan ha effekt ved **hypermobilitet i halebenet (hypermobility of coccyx)**. Det finnes **ingen kliniske studier** og **ingen publikasjoner** som støtter denne prediksjonen i dataene som er samlet inn for rapporten.

---

## Hurtigoversikt

| Punkt | Innhold |
|------|------|
| Opprinnelig indikasjon | Arthritis, Rheumatoid;Arthritis, Juvenile Rheumatoid;Arthritis, Psoriatic;Spondylarthropathies;Spondylitis, Ankylosing;Psoriasis; Spondylitis, Ankylosing;Arthritis, Juvenile Rheumatoid;Arthritis, Psoriatic;Psoriasis;Arthritis, Rheumatoid; Arthritis, Psoriatic;Psoriasis;Arthritis, Juvenile Rheumatoid |
| Foreslått ny indikasjon | Hypermobilitet i halebenet (hypermobility of coccyx) |
| TxGNN-prediksjonsscore | 0,9963 |
| Evidensnivå | L5 |
| Markedsstatus i Norge | Markedsført (gyldige tillatelser: 4 av 4) |
| Antall godkjenninger | 4 (gyldige: 4) |
| Anbefalt beslutning | Avvent (Hold) |

---

## Hvorfor kan denne prediksjonen være rimelig?

Ifølge avsnittet «Mechanism of Action» i preparatomtalen som er godkjent av amerikanske FDA (Prescribing Information), for Etanercept (uoffisiell oversettelse): «TNF er et naturlig forekommende cytokin som er involvert i normale inflammatoriske responser og immunresponser. Det spiller en viktig rolle i de inflammatoriske prosessene ved RA, polyartikulær JIA, PsA og AS og den resulterende leddpatologien. […] Etanercept er en dimerisk løselig form av p75 TNF-reseptoren som kan binde TNF-molekyler.» Engelsk originaltekst: "TNF is a naturally occurring cytokine that is involved in normal inflammatory and immune responses. It plays an important role in the inflammatory processes of RA, polyarticular JIA, PsA, and AS and the resulting joint pathology. […] Etanercept is a dimeric soluble form of the p75 TNF receptor that can bind TNF molecules." ([DailyMed: Enbrel (etanercept) prescribing information, Immunex Corporation](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=a002b40c-097d-47a5-957f-7a7b1807af7f), versjon av 2026-05-11; hentet 2026-11-19). Etanercept er kjent som en TNF-hemmer, og effekten bygger på å dempe TNF-drevet betennelse.

Hypermobilitet i halebenet er først og fremst en mekanisk og strukturell tilstand. Det er ikke påvist noen TNF-drevet mekanisme som kan forklare en nytteeffekt her. Den høye modellscoren (0,9963) er en ren modellprediksjon uten støtte i biologiske eller kliniske data. Prediksjonen bør derfor tolkes med stor forsiktighet.

---

## Klinisk studiedokumentasjon

Foreløpig er det ikke registrert noen relevante kliniske studier.

---

## Litteraturdokumentasjon

Foreløpig er det ingen relevant litteratur som direkte undersøker denne tilstanden.

---

## Markedsinformasjon for Norge

Legemidlet har status «på markedet» i Norge ifølge de lokale godkjenningsdataene. Godkjenningsoversikten genereres av programmet og er ikke gjentatt her.

---

## Sikkerhetsvurderinger

**Legemiddelinteraksjoner** (100 interaksjoner er registrert; de viktigste er nevnt):

- **Alvorlige (Major):**
  - Kortikosteroider: hydrokortison, prednison, prednisolon, deksametason, betametason, triamcinolon (også til øyet) og budesonid.
  - Deferipron.
  - Radiofarmaka og radioimmunoterapi: jobenguan (I-131), ibritumomab tiuxetan, tositumomab og tositumomab (I-131).
- **Moderate:** metronidazol, tinidazol, rosuvastatin og simvastatin.
- **Mindre alvorlige (Minor):** sinksulfat, sinkacetat og sinkglukonat.

For øvrig sikkerhetsinformasjon henvises det til pakningsvedlegget.

---

## Konklusjon og neste steg

**Beslutning: Avvent (Hold)**

**Begrunnelse:**
Prediksjonen bygger kun på en modellscore. Det finnes ingen kliniske studier eller publikasjoner om denne tilstanden, og det er ingen plausibel TNF-drevet mekanisme for en primært mekanisk tilstand. Evidensnivået er derfor L5.

**For å gå videre trengs følgende:**
- Publiserte kasuistikker, observasjonsstudier eller prekliniske data som direkte omhandler hypermobilitet i halebenet.
- En begrunnet hypotese for hvordan TNF-hemming kan påvirke tilstanden.
- Data om virkningsmekanisme og sikkerhetsopplysninger fra preparatomtalen (advarsler og kontraindikasjoner).
- Vurdering av administrasjonsvei og dosering for den aktuelle tilstanden.

<!-- review:begin log -->

## Kontrollogg

Nedenfor er gjennomgangsloggen for denne siden. Setningen om at data om virkningsmekanismen ikke var tilgjengelige, er erstattet med et utdrag fra den oppgitte offisielle preparatomtalen (med uoffisiell oversettelse); modellprediksjoner, evidensnivåer og konklusjoner er ikke omskrevet.

| Kontrolldato | Punkt | Tiltak | Kilde |
|------|------|------|------|
| 2026-11-19 | Setningen «data om virkningsmekanismen er ikke tilgjengelige» erstattet med utdrag fra amerikansk preparatomtale | Setning om manglende data om virkningsmekanismen erstattet med et utdrag med kilde | [DailyMed: Enbrel (etanercept) prescribing information, Immunex Corporation](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=a002b40c-097d-47a5-957f-7a7b1807af7f) |

<!-- review:end log -->

## Ansvarsfraskrivelse

Dette innholdet er kun til forskningsformål og utgjør ikke medisinsk rådgivning.
Klinisk validering kreves før enhver klinisk anvendelse.

---

