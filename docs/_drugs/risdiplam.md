---
layout: default
title: Risdiplam
parent: Kun modellprediksjon (L5)
nav_order: 362
evidence_level: L5
indication_count: 1
last_modified_at: 2026-11-24
description: "Risdiplam: predikert ny indikasjon Akne (evidensnivå L5). Opprinnelig indikasjon: Spinal muskelatrofi"
monitor_inn: "RISDIPLAM"
predicted_indications: ["acne (disease)"]
---

# Risdiplam
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

## Risdiplam: Fra spinal muskelatrofi til akne
{: .text-alpha }

## Oppsummering i én setning

Risdiplam er et legemiddel som opprinnelig brukes til behandling av spinal muskelatrofi (SMA).
TxGNN-modellen forutsier at det kan ha effekt mot **akne**, men denne prediksjonen er ren modellberegning:
det finnes **0 kliniske studier** og **0 publikasjoner** i de innsamlede dataene som støtter retningen.

## Hurtigoversikt

| Punkt | Innhold |
|------|------|
| Opprinnelig indikasjon | Spinal muskelatrofi |
| Predikert ny indikasjon | Akne |
| TxGNN-prediksjonsscore | 0,9945 |
| Evidensnivå | L5 |
| Markedsstatus i Norge | Markedsført (gyldige tillatelser: 1 av 1) |
| Antall godkjenninger | 1 (gyldige: 1) |
| Antall tillatelser | 1 |
| Anbefalt beslutning | Hold |

## Hvorfor er denne prediksjonen (ikke) rimelig?

Ifølge avsnittet «Mechanism of Action» i preparatomtalen som er godkjent av amerikanske FDA (Prescribing Information), for Risdiplam (uoffisiell oversettelse): «Risdiplam er en spleisemodifikator for survival of motor neuron 2 (SMN2) utviklet for å behandle pasienter med spinal muskelatrofi (SMA) forårsaket av mutasjoner i kromosom 5q som fører til SMN-proteinmangel. Ved bruk av in vitro-analyser og studier i transgene dyremodeller av SMA ble det vist at risdiplam øker inklusjonen av ekson 7 i SMN2-budbringer-ribonukleinsyre (mRNA)-transkripter og produksjonen av fullengde SMN-protein i hjernen.» Engelsk originaltekst: "Risdiplam is a survival of motor neuron 2 (SMN2) splicing modifier designed to treat patients with spinal muscular atrophy (SMA) caused by mutations in chromosome 5q that lead to SMN protein deficiency. Using in vitro assays and studies in transgenic animal models of SMA, risdiplam was shown to increase exon 7 inclusion in SMN2 messenger ribonucleic acid (mRNA) transcripts and production of full-length SMN protein in the brain." ([DailyMed: Evrysdi (risdiplam) prescribing information, Genentech, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=eceb9a99-7191-4be5-87c3-0102707cf98e), versjon av 2026-11-02; hentet 2026-11-19). Risdiplam er kjent som en SMN2-spleisingsmodulator, godkjent for spinal muskelatrofi. Dette er imidlertid bakgrunnskunnskap og ikke en del av de innsamlede dataene, og bør verifiseres.

Den eneste støtten for akne er en høy score fra TxGNN-modellen (deep learning) (0,9945). Scoren kan gjenspeile likheter modellen har lært mellom beslektede sykdommer, og er ikke biologisk evidens. Dette er en beregnet prediksjon og ikke klinisk eller eksperimentell evidens. Det er ikke dokumentert noen plausibel mekanistisk sammenheng mellom risdiplam og akne (for eksempel talgproduksjon, kolonisering med *C. acnes*, follikulær hyperkeratinisering eller betennelse). En eventuell kobling, for eksempel via modulering av alternativ spleising som påvirker andre gener, er spekulativ.

Det bør også bemerkes at prekliniske sikkerhetsstudier av risdiplam har rapportert effekter på hud og epitelvev, og at hudrelaterte bivirkninger er beskrevet. Legemidlet kan derfor være assosiert med hudfunn snarere enn åpenbart terapeutiske effekter. Også dette er bakgrunnskunnskap utenfor datagrunnlaget og må verifiseres.

## Kliniske studier

Det er for tiden ingen relaterte kliniske studier registrert.

## Litteraturevidens

Det foreligger for tiden ingen relevant litteratur.

## Informasjon om det norske markedet

<!-- licenses:begin -->

| Godkjenningsnummer | Preparatnavn (EMA) | Virkestoff(er) (EMA, engelsk) | Terapeutisk område (EMA, engelsk) | Status |
|------|------|------|------|------|
| EMEA/H/C/005145 | Evrysdi | risdiplam | Muscular Atrophy, Spinal | Gyldig |

Kilde: EMA – Medicines output (sentralt godkjente legemidler til mennesker); preparatnavn, virkestoffer og terapeutisk område er gjengitt i engelsk original. Nasjonale markedsføringstillatelser (DMP) og veterinærpreparater er ikke med i disse dataene.

<!-- licenses:end -->

Merk: Legemidlet er markedsført, og den eneste registrerte tillatelsen (1 av 1) er gyldig.

## Sikkerhetsvurderinger

**Legemiddelinteraksjoner** (2 registrert, begge med moderat alvorlighetsgrad):
- Metformin
- Metformin og metylnaltrekson: se under
- Metylnaltrekson

Se pakningsvedlegget for øvrig sikkerhetsinformasjon, inkludert advarsler og kontraindikasjoner.

## Konklusjon og neste steg

**Beslutning: Hold**

**Begrunnelse:**
Prediksjonen bygger kun på en modellscore (evidensnivå L5) uten kliniske studier, litteratur eller dokumentert mekanistisk sammenheng. Det finnes dessuten indikasjoner på at legemidlet kan være assosiert med hudfunn.

<!-- review:begin no-lic-20261106-risdiplam-1 -->

> **Kontrollrettelse (2026-11-06)**: Opprinnelig sto det: «Det finnes dessuten indikasjoner på at legemidlet kan være assosiert med hudfunn. Dessuten er den eneste tillatelsen i Norge avregistrert.» Fjernet: opplysningen om at godkjenningene er avregistrert eller at ingen gyldig godkjenning finnes, stemte ikke med EMAs data om sentrale EU-godkjenninger (2026-11-06). Oppdaterte antall og statuser for godkjenningene står i hurtigoversikten og i lisenstabellen under markedsinformasjonen. Kilde: [EMA – Medicines output: medicines report](https://www.ema.europa.eu/en/documents/report/medicines-output-medicines-report_en.xlsx); [European Medicines Agency](https://www.ema.europa.eu/).

<!-- review:end no-lic-20261106-risdiplam-1 -->

**For å gå videre kreves følgende:**
- Data om virkningsmekanisme (MOA), f.eks. fra DrugBank
- Pakningsvedlegg med advarsler og kontraindikasjoner fra DMP (blokkerende for sikkerhetsscreening)
- Mekanistisk og preklinisk dokumentasjon som kobler risdiplam til akne
- Verifisering av rapporterte hud- og epitelrelaterte bivirkninger
- Vurdering av administrasjonsvei og forenlighet med en akneindikasjon

<!-- review:begin log -->

## Kontrollogg

Nedenfor er kontrolloggen for denne siden: opplysninger kontrollert mot EMAs data om sentrale EU-godkjenninger. Rettelser gjelder bare grunnleggende faktaopplysninger; modellens prediksjoner, evidensnivåer og konklusjoner er ikke skrevet om. Setningen om at data om virkningsmekanismen ikke var tilgjengelige, er erstattet med et utdrag fra den oppgitte offisielle preparatomtalen (med uoffisiell oversettelse).

| Kontrolldato | Punkt | Tiltak | Kilde |
|------|------|------|------|
| 2026-11-06 | Fjernet: «Dessuten er den eneste tillatelsen i Norge avregistrert» | Rettet (revidert 2026-11-24; tidligere versjon er lagret i posten) | [EMA – Medicines output: medicines report](https://www.ema.europa.eu/en/documents/report/medicines-output-medicines-report_en.xlsx); [European Medicines Agency](https://www.ema.europa.eu/) |
| 2026-11-19 | Setningen «data om virkningsmekanismen er ikke tilgjengelige» erstattet med utdrag fra amerikansk preparatomtale | Setning om manglende data om virkningsmekanismen erstattet med et utdrag med kilde | [DailyMed: Evrysdi (risdiplam) prescribing information, Genentech, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=eceb9a99-7191-4be5-87c3-0102707cf98e) |

<!-- review:end log -->

## Ansvarsfraskrivelse

Dette innholdet er kun til forskningsformål og utgjør ikke medisinsk rådgivning.
Klinisk validering kreves før enhver klinisk anvendelse.

---

