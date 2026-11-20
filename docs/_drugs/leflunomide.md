---
layout: default
title: Leflunomide
parent: Kun modellprediksjon (L5)
nav_order: 238
evidence_level: L5
indication_count: 2
monitor_inn: "LEFLUNOMIDE"
predicted_indications: ["brachydactyly-syndactyly syndrome", "colobomatous microphthalmia-rhizomelic dysplasia syndrome"]
last_modified_at: 2026-10-28
description: "Leflunomide: predikert ny indikasjon Brakydaktyli-syndaktyli-syndrom (brachydactyly-syndactyly syndrome) (evidensnivå L5). Opprinnelig indikasjon: Arthritis, Rheumatoid"
---

# Leflunomide
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

## Leflunomide: DHODH-hemmer (pyrimidinsyntesehemmer) → brakydaktyli-syndaktyli-syndrom (brachydactyly-syndactyly syndrome)
{: .text-alpha }

## Oppsummering i én setning

Leflunomid er en immunmodulerende legemiddelsubstans som hemmer pyrimidinsyntesen. TxGNN-modellen forutsier at den kan være aktuell for **brakydaktyli-syndaktyli-syndrom (brachydactyly-syndactyly syndrome)**, men det finnes **ingen kliniske studier og ingen publikasjoner** i de samlede dataene som støtter denne retningen.

---

## Hurtigoversikt

| Punkt | Innhold |
|------|------|
| Opprinnelig indikasjon | Arthritis, Rheumatoid;Arthritis, Psoriatic; Arthritis, Rheumatoid |
| Predikert ny indikasjon | Brakydaktyli-syndaktyli-syndrom (brachydactyly-syndactyly syndrome) |
| TxGNN-prediksjonsscore | 0,9993 |
| Evidensnivå | L5 |
| Markedsstatus i Norge | Markedsført (gyldige tillatelser: 4 av 4) |
| Antall godkjenninger | 4 (gyldige: 4) |
| Anbefalt beslutning | Hold |

---

## Hvorfor er denne prediksjonen (ikke) rimelig?

Ifølge avsnittet «Mechanism of Action» i preparatomtalen som er godkjent av amerikanske FDA (Prescribing Information), for Leflunomide (uoffisiell oversettelse): «Leflunomid er et immunmodulerende isoksazolmiddel som hemmer dihydroorotatdehydrogenase (et mitokondrielt enzym involvert i de novo-pyrimidinsyntese) og har antiproliferativ aktivitet. Flere eksperimentelle in vivo- og in vitro-modeller har vist en antiinflammatorisk effekt.» Engelsk originaltekst: "Leflunomide is an isoxazole immunomodulatory agent that inhibits dihydroorotate dehydrogenase (a mitochondrial enzyme involved in de novo pyrimidine synthesis) and has antiproliferative activity. Several in vivo and in vitro experimental models have demonstrated an anti-inflammatory effect." ([DailyMed: Arava (leflunomide) prescribing information, sanofi-aventis U.S. LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=320f63f2-fac3-4aee-aff8-85724e00ef52), versjon av 2025-06-04; hentet 2026-11-19). Basert på allmenn farmakologisk kunnskap hemmer leflunomid, via den aktive metabolitten teriflunomid, enzymet dihydroorotatdehydrogenase (DHODH) og dermed pyrimidinsyntesen. Dette kan i teorien påvirke raskt prolifererende celler, særlig aktiverte lymfocytter.

Koblingen til brakydaktyli-syndaktyli-syndrom er spekulativ. Tilstanden er en medfødt utviklingsforstyrrelse i lemmene, og det finnes ingen kjent farmakologisk angrepsflate for en immunmodulator. Tvert imot er leflunomid teratogent, og DHODH-hemming er knyttet til lemmemisdannelser (for eksempel oppstår Miller-syndrom ved tap av DHODH-funksjon). En biologisk kobling peker dermed snarere mot skade enn mot terapeutisk nytte. Den høye modellscoren gjenspeiler trolig nærhet i modellens datagrunnlag, ikke en reell behandlingsmekanisme.

---

## Klinisk studiedokumentasjon

Det er for tiden ingen relaterte kliniske studier registrert.

---

## Litteraturdokumentasjon

Det er for tiden ingen relevant litteratur tilgjengelig.

---

## Markedsinformasjon for Norge

| Godkjenningsnummer | Produktnavn | Doseringsform | Godkjent indikasjon |
|---------|------|------|-----------|
| EMEA/H/C/001129 | Leflunomide Zentiva (previously Leflunomide Winthrop) | – | Ikke angitt her |
| EMEA/H/C/001227 | Leflunomide medac | – | Ikke angitt her |
| EMEA/H/C/000235 | Arava | – | Ikke angitt her |
| EMEA/H/C/002035 | Leflunomide ratiopharm | – | Ikke angitt her |

---

## Sikkerhetsvurderinger

- **Legemiddelinteraksjoner:** 100 interaksjoner er registrert. Blant de viktigste (alvorlighetsgrad «alvorlig») er acarbose, hydrokortison, pioglitazon, bupropion, triamcinolon, acetylsalisylsyre, deksametason, betametason, budesonid, klaritromycin, minocyklin og naltrekson. Flere kortikosteroider er blant disse.
- **Tilstander som er registrert som kontraindikasjoner i modelldataene:** leversvikt og leversykdom, nyresykdom, trombocytopeni, nøytropeni, agranulocytose, pancytopeni, anemi, kronisk hepatitt B- og C-infeksjon, perifer nevropati, interstitiell lungesykdom, pneumocystose og aspergillose. Dette er ikke hentet fra preparatomtalen.
- **Teratogenisitet:** Basert på allmenn farmakologisk kunnskap er leflunomid teratogent, noe som er særlig relevant for en medfødt utviklingsforstyrrelse.

Se preparatomtalen for fullstendig sikkerhetsinformasjon.

---

## Konklusjon og neste steg

**Beslutning: Hold**

**Begrunnelse:**
Prediksjonen bygger kun på en modellscore uten støtte fra kliniske studier eller litteratur (evidensnivå L5). Den kjente teratogene effekten og koblingen mellom DHODH-hemming og lemmemisdannelser taler mot terapeutisk nytte.

**For å gå videre kreves følgende:**
- Data om virkningsmekanisme (MOA) fra DrugBank
- Preparatomtale med advarsler og kontraindikasjoner
- Prekliniske eller kliniske data som direkte undersøker brakydaktyli-syndaktyli-syndrom
- En grundig vurdering av teratogenrisiko før eventuelle videre analyser

<!-- review:begin log -->

## Kontrollogg

Nedenfor er gjennomgangsloggen for denne siden. Setningen om at data om virkningsmekanismen ikke var tilgjengelige, er erstattet med et utdrag fra den oppgitte offisielle preparatomtalen (med uoffisiell oversettelse); modellprediksjoner, evidensnivåer og konklusjoner er ikke omskrevet.

| Kontrolldato | Punkt | Tiltak | Kilde |
|------|------|------|------|
| 2026-11-19 | Setningen «data om virkningsmekanismen er ikke tilgjengelige» erstattet med utdrag fra amerikansk preparatomtale | Setning om manglende data om virkningsmekanismen erstattet med et utdrag med kilde | [DailyMed: Arava (leflunomide) prescribing information, sanofi-aventis U.S. LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=320f63f2-fac3-4aee-aff8-85724e00ef52) |

<!-- review:end log -->

## Ansvarsfraskrivelse

Dette innholdet er kun til forskningsformål og utgjør ikke medisinsk rådgivning.
Klinisk validering kreves før enhver klinisk anvendelse.

---

