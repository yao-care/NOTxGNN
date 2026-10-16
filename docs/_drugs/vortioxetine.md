---
layout: default
title: Vortioxetine
parent: Kun modellprediksjon (L5)
nav_order: 455
evidence_level: L5
indication_count: 5
last_modified_at: 2026-10-15
description: "Vortioxetine: predikert ny indikasjon Nevrotisk lidelse (neurotic disorder) (evidensnivå L5). Opprinnelig indikasjon: Alvorlig depressiv lidelse (Depressive Disorder, Major)"
monitor_inn: "VORTIOXETINE"
predicted_indications: ["neurotic disorder", "neurotic depression", "melancholia", "benign paroxysmal torticollis of infancy", "dysthymic disorder"]
---

# Vortioxetine
{: .fs-9 }

Evidensnivå: **L5** | Predikerte indikasjoner: **5** stk.
{: .fs-6 .fw-300 }

---

## Innholdsfortegnelse
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## Farmasøytens vurderingsrapport

</div>

# Vortioksetin: Fra alvorlig depressiv lidelse til nevrotisk lidelse

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
| TxGNN-prediksjonsscore | 99,24 % |
| Evidensnivå | L5 |
| Markedsstatus i Norge | Kun tilbakekalt/avregistrert (Cancelled only) |
| Antall markedsføringstillatelser | 1 (0 gyldige, 1 avregistrert) |
| Anbefalt beslutning | Hold |

---

## Hvorfor er denne prediksjonen rimelig?

Data om virkningsmekanisme (MOA) er for tiden ikke tilgjengelige i de innsamlede dataene. Ut fra kjent informasjon er vortioksetin et antidepressivum med dokumentert effekt ved alvorlig depressiv lidelse, og det kan mekanistisk tenkes å være relevant for nevrotisk lidelse. Litteraturen som er innhentet beskriver vortioksetin som en serotoninreopptakshemmer med modulerende effekt på flere 5-HT-reseptorer, men dette er ikke verifisert mot MOA-feltet i datasettet.

«Nevrotisk lidelse» er en bred, historisk diagnosekategori som i stor grad overlapper med depressive lidelser og angstlidelser. Den høye TxGNN-scoren speiler derfor trolig ontologisk nærhet til MDD snarere enn selvstendig evidens. Den eneste litteraturen er en russiskspråklig narrativ artikkel om behandling av nevrotisk depresjon (kasuistikk med antidepressiva og kognitiv atferdsterapi), som ikke vurderer vortioksetin.

Av den grunn kan ikke det mekanistiske grunnlaget bekreftes ut fra dataene som foreligger.

**Andre predikerte indikasjoner (til orientering):**

| Predikert indikasjon | Score | Evidensnivå | Kommentar |
|------|------|------|------|
| Nevrotisk depresjon | 99,09 % | L4 | Praktisk talt den opprinnelige indikasjonen under en eldre betegnelse; ingen studier knyttet til begrepet |
| Melankoli | 99,09 % | L1 | 4 fase 3-RCT-er og 1 fase 2/3-studie i MDD; evidensen er direkte for MDD, men indirekte for melankolisk subtype |
| Benign paroksysmal torticollis hos spedbarn | 99,07 % | L5 | Ingen mekanistisk begrunnelse; trolig grafartefakt |
| Dystymi | 99,02 % | L4 | Kun én åpen MDD-forlengelsesstudie, indirekte kobling |

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

| Tillatelsesnummer | Produktnavn | Doseringsform | Godkjent indikasjon |
|---------|------|------|-----------|
| EMEA/H/C/002717 | Brintellix | Ikke oppgitt | Alvorlig depressiv lidelse (status: avregistrert) |

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
Det finnes ingen kliniske studier og kun én litteraturreferanse uten direkte kobling til vortioksetin for nevrotisk lidelse. Den høye TxGNN-scoren skyldes trolig ontologisk nærhet til MDD. I tillegg er produktet kun registrert som avregistrert i Norge.

**For å gå videre kreves følgende:**
- Innhenting av preparatomtale med advarsler og kontraindikasjoner (kritisk datamangel som blokkerer sikkerhetsscreening)
- Data om virkningsmekanisme (f.eks. via DrugBank)
- Avklaring av hvordan «nevrotisk lidelse» skal defineres i moderne diagnostikk (f.eks. mot angst- og depressive lidelser)
- Kontrollerte kliniske studier i en tydelig definert populasjon
- Avklaring av markedsstatus i Norge, siden den eneste tillatelsen er avregistrert

**Merknad om andre kandidater:** Melankoli er den predikerte indikasjonen med sterkest evidens (L1, men indirekte via MDD-studier). En subgruppe- eller post hoc-analyse av melankolisk subtype ville være nødvendig for å bekrefte subtypespesifikk nytte.
## Ansvarsfraskrivelse

Dette innholdet er kun til forskningsformål og utgjør ikke medisinsk rådgivning.
Klinisk validering kreves før enhver klinisk anvendelse.

---

