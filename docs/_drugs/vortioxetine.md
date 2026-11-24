---
layout: default
title: Vortioxetine
parent: Kun modellprediksjon (L5)
nav_order: 455
evidence_level: L5
indication_count: 2
last_modified_at: 2026-11-24
description: "Vortioxetine: predikert ny indikasjon Nevrotisk lidelse (neurotic disorder) (evidensnivå L5). Opprinnelig indikasjon: Alvorlig depressiv lidelse (Depressive Disorder, Major)"
monitor_inn: "VORTIOXETINE"
predicted_indications: ["neurotic disorder", "benign paroxysmal torticollis of infancy"]
---

# Vortioxetine
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

## Vortioksetin: Fra alvorlig depressiv lidelse til nevrotisk lidelse
{: .text-alpha }

## Oppsummering i én setning

Vortioksetin er et antidepressivt middel med multimodal serotonerg virkning, opprinnelig godkjent for behandling av alvorlig depressiv lidelse (MDD).
TxGNN-modellen predikerer at det kan være effektivt ved **nevrotisk lidelse**, men det finnes **ingen kliniske studier** og bare **1 publikasjon** (en russisk narrativ artikkel som ikke undersøker vortioksetin spesifikt) som støtter denne indikasjonen.
Den høye prediksjonsscoren gjenspeiler trolig nærheten til MDD i ontologien, ikke uavhengig evidens.

---

## Hurtigoversikt

| Punkt | Innhold |
|------|------|
| Opprinnelig indikasjon | Alvorlig depressiv lidelse (Depressive Disorder, Major) |
| Predikert ny indikasjon | Nevrotisk lidelse (neurotic disorder) |
| TxGNN-prediksjonsscore | 0,9924 |
| Evidensnivå | L5 |
| Markedsstatus i Norge | Markedsført (gyldige tillatelser: 1 av 1) |
| Antall godkjenninger | 1 (gyldige: 1) |
| Antall markedsføringstillatelser | 1 (0 gyldige, 1 avregistrert) |
| Anbefalt beslutning | Hold |

---

## Hvorfor er denne prediksjonen rimelig?

Ifølge avsnittet «Mechanism of Action» i preparatomtalen som er godkjent av amerikanske FDA (Prescribing Information), for Vortioxetine (uoffisiell oversettelse): «Mekanismen bak den antidepressive effekten av vortioksetin er ikke fullstendig klarlagt, men antas å være relatert til forsterkning av serotonerg aktivitet i CNS gjennom hemming av gjenopptaket av serotonin (5-HT). Vortioksetin har også flere andre virkninger, inkludert antagonisme ved 5-HT3-reseptoren og agonisme ved 5-HT1A-reseptoren.» Engelsk originaltekst: "The mechanism of the antidepressant effect of vortioxetine is not fully understood, but is thought to be related to its enhancement of serotonergic activity in the CNS through inhibition of the reuptake of serotonin (5-HT). It also has several other activities including 5-HT3 receptor antagonism and 5-HT1A receptor agonism." ([DailyMed: Trintellix (vortioxetine) prescribing information, REMEDYREPACK INC.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=bd0107e5-1cb9-4b40-a6af-fa65fcbe6b4e), versjon av 2026-04-23; hentet 2026-11-19). Ut fra kjent informasjon er vortioksetin et antidepressivum med dokumentert effekt ved alvorlig depressiv lidelse, og det kan mekanistisk tenkes å være relevant for nevrotisk lidelse. Litteraturen som er innhentet beskriver vortioksetin som en serotoninreopptakshemmer med modulerende effekt på flere 5-HT-reseptorer, men dette er ikke verifisert mot MOA-feltet i datasettet.

«Nevrotisk lidelse» er en bred, historisk diagnosekategori som i stor grad overlapper med depressive lidelser og angstlidelser. Den høye TxGNN-scoren speiler derfor trolig ontologisk nærhet til MDD snarere enn selvstendig evidens. Den eneste litteraturen er en russiskspråklig narrativ artikkel om behandling av nevrotisk depresjon (kasuistikk med antidepressiva og kognitiv atferdsterapi), som ikke vurderer vortioksetin.

Av den grunn kan ikke det mekanistiske grunnlaget bekreftes ut fra dataene som foreligger.

**Andre predikerte indikasjoner (til orientering):**

| Predikert indikasjon | Score | Evidensnivå | Kommentar |
|------|------|------|------|
| Benign paroksysmal torticollis hos spedbarn | 0,9907 | L5 | Ingen mekanistisk begrunnelse; trolig grafartefakt |

---

## Klinisk studieevidens

Ingen kliniske studier er registrert for nevrotisk lidelse. Det finnes for tiden ingen relaterte kliniske studier.

---

## Litteraturevidens

| PMID | År | Type | Tidsskrift | Hovedfunn |
|------|-----|------|------|---------|
| [31006795](https://pubmed.ncbi.nlm.nih.gov/31006795/) | 2019 | Oversikt/kasuistikk | Zhurnal nevrologii i psikhiatrii imeni S.S. Korsakova | Kasuistikk om nevrotisk depresjon; fremhever en integrert tilnærming med antidepressiva og kognitiv atferdsterapi. Omtaler ikke vortioksetin spesifikt. |

---

## Informasjon om det norske markedet

<!-- licenses:begin -->

| Godkjenningsnummer | Preparatnavn (EMA) | Virkestoff(er) (EMA, engelsk) | Terapeutisk område (EMA, engelsk) | Status |
|------|------|------|------|------|
| EMEA/H/C/002717 | Brintellix | vortioxetine | Depressive Disorder, Major | Gyldig |

Kilde: EMA – Medicines output (sentralt godkjente legemidler til mennesker); preparatnavn, virkestoffer og terapeutisk område er gjengitt i engelsk original. Nasjonale markedsføringstillatelser (DMP) og veterinærpreparater er ikke med i disse dataene.

<!-- licenses:end -->

---

## Sikkerhetsvurderinger

**Legemiddelinteraksjoner** (100 interaksjoner registrert; de viktigste er vist):

- **Alvorlig (Major):** bupropion, lorkaserin, dietylpropion, dolasetron, palonosetron, fentermin
- **Moderat (Moderate):** morfin, acetylsalisylsyre, deksametason, klorpropamid, glimepirid, insuliner (aspart, degludek, detemir, glargin, glulisin), pikosulfat, polyetylenglykol (3350 med elektrolytter), natriumsulfat, eliglustat

Informasjon om advarsler og kontraindikasjoner fra preparatomtalen er ikke tilgjengelig; se preparatomtalen for fullstendig sikkerhetsinformasjon.

---

## Konklusjon og neste steg

**Beslutning: Hold**

**Begrunnelse:**
Det finnes ingen kliniske studier og kun én litteraturreferanse uten direkte kobling til vortioksetin for nevrotisk lidelse. Den høye TxGNN-scoren skyldes trolig ontologisk nærhet til MDD.

<!-- review:begin no-lic-20261031-vortioxetine-1 -->

> **Kontrollrettelse (2026-10-31)**: Opprinnelig sto det: «Den høye TxGNN-scoren skyldes trolig ontologisk nærhet til MDD. I tillegg er produktet kun registrert som avregistrert i Norge.» Fjernet: opplysningen om at godkjenningene er avregistrert eller at ingen gyldig godkjenning finnes, stemte ikke med EMAs data om sentrale EU-godkjenninger (2026-10-31). Oppdaterte antall og statuser for godkjenningene står i hurtigoversikten og i lisenstabellen under markedsinformasjonen. Kilde: [EMA – Medicines output: medicines report](https://www.ema.europa.eu/en/documents/report/medicines-output-medicines-report_en.xlsx); [European Medicines Agency](https://www.ema.europa.eu/).

<!-- review:end no-lic-20261031-vortioxetine-1 -->

**For å gå videre kreves følgende:**
- Innhenting av preparatomtale med advarsler og kontraindikasjoner (kritisk datamangel som blokkerer sikkerhetsscreening)
- Data om virkningsmekanisme (f.eks. via DrugBank)
- Avklaring av hvordan «nevrotisk lidelse» skal defineres i moderne diagnostikk (f.eks. mot angst- og depressive lidelser)
- Kontrollerte kliniske studier i en tydelig definert populasjon
- Avklaring av markedsstatus i Norge

<!-- review:begin no-lic-20261106-vortioxetine-2 -->

> **Kontrollrettelse (2026-11-06)**: Opprinnelig sto det: «Avklaring av markedsstatus i Norge, siden den eneste tillatelsen er avregistrert» Fjernet: opplysningen om at godkjenningene er avregistrert eller at ingen gyldig godkjenning finnes, stemte ikke med EMAs data om sentrale EU-godkjenninger (2026-11-06). Oppdaterte antall og statuser for godkjenningene står i hurtigoversikten og i lisenstabellen under markedsinformasjonen. Kilde: [EMA – Medicines output: medicines report](https://www.ema.europa.eu/en/documents/report/medicines-output-medicines-report_en.xlsx); [European Medicines Agency](https://www.ema.europa.eu/).

<!-- review:end no-lic-20261106-vortioxetine-2 -->

**Merknad om andre kandidater:** Melankoli er den predikerte indikasjonen med sterkest evidens (L1, men indirekte via MDD-studier). En subgruppe- eller post hoc-analyse av melankolisk subtype ville være nødvendig for å bekrefte subtypespesifikk nytte.

<!-- review:begin log -->

## Kontrollogg

Nedenfor er kontrolloggen for denne siden: opplysninger kontrollert mot EMAs data om sentrale EU-godkjenninger. Rettelser gjelder bare grunnleggende faktaopplysninger; modellens prediksjoner, evidensnivåer og konklusjoner er ikke skrevet om. Setningen om at data om virkningsmekanismen ikke var tilgjengelige, er erstattet med et utdrag fra den oppgitte offisielle preparatomtalen (med uoffisiell oversettelse).

| Kontrolldato | Punkt | Tiltak | Kilde |
|------|------|------|------|
| 2026-10-31 | Fjernet: «I tillegg er produktet kun registrert som avregistrert i Norge» | Rettet (revidert 2026-11-24; tidligere versjon er lagret i posten) | [EMA – Medicines output: medicines report](https://www.ema.europa.eu/en/documents/report/medicines-output-medicines-report_en.xlsx); [European Medicines Agency](https://www.ema.europa.eu/) |
| 2026-11-06 | Fjernet: «siden den eneste tillatelsen er avregistrert» | Rettet (revidert 2026-11-24; tidligere versjon er lagret i posten) | [EMA – Medicines output: medicines report](https://www.ema.europa.eu/en/documents/report/medicines-output-medicines-report_en.xlsx); [European Medicines Agency](https://www.ema.europa.eu/) |
| 2026-11-19 | Setningen «data om virkningsmekanismen er ikke tilgjengelige» erstattet med utdrag fra amerikansk preparatomtale | Setning om manglende data om virkningsmekanismen erstattet med et utdrag med kilde | [DailyMed: Trintellix (vortioxetine) prescribing information, REMEDYREPACK INC.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=bd0107e5-1cb9-4b40-a6af-fa65fcbe6b4e) |

<!-- review:end log -->

## Ansvarsfraskrivelse

Dette innholdet er kun til forskningsformål og utgjør ikke medisinsk rådgivning.
Klinisk validering kreves før enhver klinisk anvendelse.

---

