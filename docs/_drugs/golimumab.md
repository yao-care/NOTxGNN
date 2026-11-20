---
layout: default
title: Golimumab
parent: Kun modellprediksjon (L5)
nav_order: 196
evidence_level: L5
indication_count: 2
monitor_inn: "GOLIMUMAB"
predicted_indications: ["hypermobility of coccyx", "Kummell disease"]
last_modified_at: 2026-11-20
description: "Golimumab: predikert ny indikasjon Hypermobilitet i halebenet (hypermobility of coccyx) (evidensnivå L5). Opprinnelig indikasjon: Arthritis, Rheumatoid"
---

# Golimumab
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

## Golimumab: TNF-hemmer → Hypermobilitet i halebenet (hypermobility of coccyx)
{: .text-alpha }

## Oppsummering i én setning

Golimumab er et biologisk legemiddel som hemmer TNF (tumornekrosefaktor). Modellen TxGNN forutsier at det kan ha effekt ved **hypermobilitet i halebenet (hypermobility of coccyx)**, men i dataene som er samlet inn for denne rapporten finnes det **ingen kliniske studier og ingen publikasjoner** som støtter denne retningen.

---

## Hurtigoversikt

| Punkt | Innhold |
|------|------|
| Opprinnelig indikasjon | Arthritis, Rheumatoid;Arthritis, Juvenile;Arthritis, Psoriatic;Axial Spondyloarthritis;Non-Radiographic Axial Spondyloarthritis;Colitis, Ulcerative; Arthritis, Psoriatic;Spondylitis, Ankylosing;Colitis, Ulcerative;Arthritis, Rheumatoid; Arthritis, Rheumatoid;Arthritis, Juvenile;Arthritis, Psoriatic; |
| Predikert ny indikasjon | Hypermobilitet i halebenet (hypermobility of coccyx) |
| TxGNN-prediksjonsscore | 0,9967 |
| Evidensnivå | L5 |
| Markedsstatus i Norge | Markedsført (gyldige tillatelser: 3 av 3) |
| Antall godkjenninger | 3 (gyldige: 3) |
| Anbefalt beslutning | Hold |

---

## Hvorfor er denne prediksjonen rimelig?

Ifølge avsnittet «Mechanism of Action» i preparatomtalen som er godkjent av amerikanske FDA (Prescribing Information), for Golimumab (uoffisiell oversettelse): «Golimumab er et humant monoklonalt antistoff som bindes til både de løselige og de transmembrane bioaktive formene av humant TNFα. Denne interaksjonen hindrer binding av TNFα til reseptorene, og hemmer dermed den biologiske aktiviteten til TNFα (et cytokinprotein).» Engelsk originaltekst: "Golimumab is a human monoclonal antibody that binds to both the soluble and transmembrane bioactive forms of human TNFα. This interaction prevents the binding of TNFα to its receptors, thereby inhibiting the biological activity of TNFα (a cytokine protein)." ([DailyMed: Simponi (golimumab) prescribing information, Janssen Biotech, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=f86cb4a7-c358-4136-ae57-b32bda9bba00), versjon av 2026-11-02; hentet 2026-11-19). Golimumab er et monoklonalt antistoff som er kjent for å hemme TNF, og tilhører klassen TNF-hemmere som brukes ved immunmedierte inflammatoriske sykdommer.

Hypermobilitet i halebenet er derimot vanligvis en mekanisk eller traumatisk tilstand, ikke en TNF-drevet inflammatorisk sykdom. Koblingen til golimumab er dermed ikke støttet av mekanistiske eller kliniske data. Den høye scoren (0,9967) er en ren modellprediksjon, trolig drevet av nærhet til noder knyttet til spondyloartropati-lignende tilstander.

Prediksjonen må derfor betraktes som en hypotese som ikke er underbygget.

---

## Klinisk studieevidens

Foreløpig er ingen relaterte kliniske studier registrert.

---

## Litteraturevidens

Foreløpig finnes ingen relatert litteratur.

---

## Informasjon om det norske markedet

| Godkjenningsnummer | Produktnavn | Doseringsform | Godkjent indikasjon |
|---------|------|------|-----------|
| EMEA/H/C/006621 | Gotenfia | – | Ikke angitt i lokale data |
| EMEA/H/C/000992 | Simponi | – | Ikke angitt i lokale data |
| EMEA/H/C/006560 | Gobivaz | – | Ikke angitt i lokale data |

---

## Sikkerhetsvurderinger

**Legemiddelinteraksjoner** (100 registrerte; de viktigste er nevnt):

- **Alvorlige (Major):** hydrokortison, triamcinolon, deksametason, betametason, budesonid, prednison, prednisolon, deferipron, jobenguan (I-131), ibritumomab tiuxetan, tositumomab
- **Moderate:** metronidazol, rosuvastatin, simvastatin, tinidazol
- **Mindre (Minor):** sinksulfat, sinkacetat, sinkglukonat

For øvrig sikkerhetsinformasjon, se preparatomtalen.

---

## Konklusjon og neste steg

**Beslutning: Hold**

**Begrunnelse:**
Prediksjonen bygger kun på en modellscore, uten kliniske studier eller publikasjoner, og det er ingen plausibel TNF-mediert mekanisme for en i hovedsak mekanisk tilstand. Evidensnivået er L5.

**For å gå videre trengs følgende:**
- Data om virkningsmekanisme (MOA)
- Preparatomtale med advarsler og kontraindikasjoner
- Mekanistisk begrunnelse og prekliniske eller kliniske data som direkte omhandler hypermobilitet i halebenet
- Vurdering av administrasjonsvei og aktuell pasientgruppe

<!-- review:begin log -->

## Kontrollogg

Nedenfor er gjennomgangsloggen for denne siden. Setningen om at data om virkningsmekanismen ikke var tilgjengelige, er erstattet med et utdrag fra den oppgitte offisielle preparatomtalen (med uoffisiell oversettelse); modellprediksjoner, evidensnivåer og konklusjoner er ikke omskrevet.

| Kontrolldato | Punkt | Tiltak | Kilde |
|------|------|------|------|
| 2026-11-19 | Setningen «data om virkningsmekanismen er ikke tilgjengelige» erstattet med utdrag fra amerikansk preparatomtale | Setning om manglende data om virkningsmekanismen erstattet med et utdrag med kilde | [DailyMed: Simponi (golimumab) prescribing information, Janssen Biotech, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=f86cb4a7-c358-4136-ae57-b32bda9bba00) |

<!-- review:end log -->

## Ansvarsfraskrivelse

Dette innholdet er kun til forskningsformål og utgjør ikke medisinsk rådgivning.
Klinisk validering kreves før enhver klinisk anvendelse.

---

