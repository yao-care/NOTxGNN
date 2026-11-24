---
layout: default
title: Delamanid
parent: Kun modellprediksjon (L5)
nav_order: 122
evidence_level: L5
indication_count: 1
monitor_inn: "DELAMANID"
predicted_indications: ["allergic urticaria"]
last_modified_at: 2026-11-24
description: "Delamanid: predikert ny indikasjon Allergisk urticaria (allergic urticaria) (evidensnivå L5). Opprinnelig indikasjon: Tuberculosis, Multidrug-Resistant"
---

# Delamanid
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

## Delamanid: antimykobakterielt middel → allergisk urticaria (allergic urticaria)
{: .text-alpha }

## Oppsummering i én setning

Delamanid er et legemiddel mot tuberkulose som brukes ved multiresistent tuberkulose. TxGNN-modellen forutsier at det kan ha effekt ved **allergisk urticaria (allergic urticaria)**, men det finnes **ingen kliniske studier** og bare **én publikasjon** (en kasuistikk om et annet legemiddel som ikke handler om delamanid). Prediksjonen er derfor kun modellbasert.

## Hurtigoversikt

| Punkt | Innhold |
|------|------|
| Opprinnelig indikasjon | Tuberculosis, Multidrug-Resistant |
| Predikert ny indikasjon | Allergisk urticaria (allergic urticaria) |
| TxGNN-prediksjonsscore | 0,9956 |
| Evidensnivå | L5 |
| Markedsstatus i Norge | Markedsført (gyldige tillatelser: 1 av 1) |
| Antall godkjenninger | 1 (gyldige: 1) |
| Anbefalt beslutning | Hold |

## Hvorfor er denne prediksjonen rimelig?

Ifølge ChEMBL (EMBL-EBI) er den registrerte virkningsmekanismen for Delamanid (uoffisiell oversettelse): «Mycobacterium tuberculosis H37Rv-hemmer». Engelsk originaltekst: "Mycobacterium tuberculosis H37Rv inhibitor" ([ChEMBL CHEMBL218650 (delamanid): drug mechanism](https://www.ebi.ac.uk/chembl/explore/compound/CHEMBL218650), CC BY-SA 3.0; hentet 2026-11-19). Delamanid er et antimykobakterielt middel, og virkningen er knyttet til tuberkulosebehandling.

Det er ikke funnet noen plausibel mekanistisk sammenheng mellom delamanids antimykobakterielle virkning og allergisk urticaria. Den eneste identifiserte publikasjonen er en kasuistikk om urticaria og angioødem utløst av piperacillin-tazobaktam, som ikke gjelder delamanid. Prediksjonen er trolig et artefakt av modellen og bør tolkes med stor forsiktighet.

## Klinisk studieevidens

Foreløpig ingen relaterte kliniske studier registrert.

## Litteraturevidens

| PMID | År | Type | Tidsskrift | Hovedfunn |
|------|-----|------|------|---------|
| [38800261](https://pubmed.ncbi.nlm.nih.gov/38800261/) | 2024 | Kasuistikk med litteraturgjennomgang | Cureus | Piperacillin-tazobaktam-indusert urticaria og angioødem hos en 35 år gammel mann. Gjelder ikke delamanid, og viser dermed ingen støtte for prediksjonen. |

## Informasjon om markedet i Norge

<!-- licenses:begin -->

| Godkjenningsnummer | Preparatnavn (EMA) | Virkestoff(er) (EMA, engelsk) | Terapeutisk område (EMA, engelsk) | Status |
|------|------|------|------|------|
| EMEA/H/C/002552 | Deltyba | Delamanid | Tuberculosis, Multidrug-Resistant | Gyldig |

Kilde: EMA – Medicines output (sentralt godkjente legemidler til mennesker); preparatnavn, virkestoffer og terapeutisk område er gjengitt i engelsk original. Nasjonale markedsføringstillatelser (DMP) og veterinærpreparater er ikke med i disse dataene.

<!-- licenses:end -->

## Sikkerhetsvurderinger

Se pakningsvedlegget for sikkerhetsinformasjon.

## Konklusjon og neste steg

**Beslutning: Hold**

**Begrunnelse:**
Prediksjonen bygger kun på modellscore uten direkte kliniske studier eller litteratur om delamanid ved allergisk urticaria, og det finnes ingen plausibel mekanistisk forklaring. Evidensnivået er L5.

**For å gå videre kreves følgende:**
- Data om virkningsmekanisme (MOA) for delamanid
- Advarsler og kontraindikasjoner fra preparatomtalen
- Prekliniske eller kliniske data som direkte undersøker delamanid ved allergisk urticaria
- Vurdering av om prediksjonen er et modellartefakt

<!-- review:begin log -->

## Kontrollogg

Nedenfor er gjennomgangsloggen for denne siden. Setningen om at data om virkningsmekanismen ikke var tilgjengelige, er erstattet med et utdrag fra den oppgitte offisielle preparatomtalen (med uoffisiell oversettelse); modellprediksjoner, evidensnivåer og konklusjoner er ikke omskrevet.

| Kontrolldato | Punkt | Tiltak | Kilde |
|------|------|------|------|
| 2026-11-19 | Setningen «data om virkningsmekanismen er ikke tilgjengelige» erstattet med utdrag fra amerikansk preparatomtale | Setning om manglende data om virkningsmekanismen erstattet med et utdrag med kilde (revidert 2026-11-20; tidligere versjon er lagret i posten) | [ChEMBL CHEMBL218650 (delamanid): drug mechanism](https://www.ebi.ac.uk/chembl/explore/compound/CHEMBL218650) |

<!-- review:end log -->

## Ansvarsfraskrivelse

Dette innholdet er kun til forskningsformål og utgjør ikke medisinsk rådgivning.
Klinisk validering kreves før enhver klinisk anvendelse.

---

