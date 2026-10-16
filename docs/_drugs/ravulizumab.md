---
layout: default
title: Ravulizumab
parent: Kun modellprediksjon (L5)
nav_order: 350
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-15
description: "Ravulizumab: predikert ny indikasjon Autosomal recessiv alvorlig medfødt nøytropeni på grunn av G6PC3-mang… (evidensnivå L5). Opprinnelig indikasjon: Paroksysmal nattlig hemoglobinuri"
---

# Ravulizumab
{: .fs-9 }

Evidensnivå: **L5** | Predikerte indikasjoner: **10** stk.
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

# Ravulizumab: Fra paroksysmal nattlig hemoglobinuri til autosomal recessiv alvorlig medfødt nøytropeni (G6PC3-mangel)

## Oppsummering

Ravulizumab er en komplementhemmer (C5-hemmer) som opprinnelig brukes mot **paroksysmal nattlig hemoglobinuri**.
TxGNN-modellen forutsier at legemidlet kan ha effekt ved **autosomal recessiv alvorlig medfødt nøytropeni på grunn av G6PC3-mangel**, men det finnes foreløpig **ingen kliniske studier og ingen publikasjoner** som støtter denne retningen. Prediksjonen er kun modellbasert.

---

## Hurtigoversikt

| Punkt | Innhold |
|------|------|
| Opprinnelig indikasjon | Paroksysmal nattlig hemoglobinuri |
| Predikert ny indikasjon | Autosomal recessiv alvorlig medfødt nøytropeni på grunn av G6PC3-mangel |
| TxGNN-prediksjonsscore | 99,96 % |
| Evidensnivå | L5 |
| Markedsstatus i Norge | Kun kansellerte godkjenninger |
| Antall godkjenninger | 1 (kansellert) |
| Anbefalt beslutning | Hold |

---

## Hvorfor er denne prediksjonen (ikke) rimelig?

Detaljerte data om virkningsmekanisme er foreløpig ikke tilgjengelige i datagrunnlaget. Ravulizumab er likevel kjent som en hemmer av komplementfaktor C5, og effekten ved paroksysmal nattlig hemoglobinuri, en komplementmediert hemolytisk sykdom, er etablert.

Datagrunnlaget som er samlet for rapporten, støtter **ikke** en mekanistisk kobling til den predikerte indikasjonen. G6PC3-mangel er en metabolsk defekt i modning av myeloide celler, med økt nøytrofil apoptose og stress i endoplasmatisk retikulum. Den er ikke primært komplementdrevet. TxGNN-scoren er derfor å regne som en ren modellprediksjon.

Det samme gjelder de øvrige ni predikerte indikasjonene (rangert 2–10), som alle har evidensnivå L5 og anbefalingen «Hold»:

| Rang | Predikert indikasjon | Score | Vurdering av mekanistisk kobling |
|------|------|------|------|
| 2 | Syklisk hematopoese | 99,94 % | Skyldes hovedsakelig ELANE-mutasjoner; ingen kjent rolle for terminal komplement |
| 3 | Primær hyperoksaluri | 99,90 % | Hepatisk enzymdefekt; komplementlink kun spekulativ |
| 4 | Alvorlig medfødt nøytropeni | 99,87 % | Defekter i myeloid differensiering; ingen plausibel C5-rolle |
| 5 | Alvorlig medfødt nøytropeni (CXCR2-mangel) | 99,86 % | Kjemokinreseptordefekt uten tydelig komplementkobling |
| 6 | Primær immunsvikt (p14-mangel) | 99,83 % | Ingen C5-kobling; økt infeksjonsrisiko hos immunsvekkede |
| 7 | Pseudo-von Willebrands sykdom | 99,82 % | Trombocyttdefekt (GP1BA); ingen komplementavhengighet |
| 8 | X-bundet alvorlig medfødt nøytropeni | 99,82 % | WAS-mutasjon; ingen støttet C5-rasjonale |
| 9 | Primær frigjøringsforstyrrelse i blodplater | 99,81 % | Intrinsisk trombocyttdefekt; ingen dokumentert komplementmekanisme |
| 10 | Megaloblastær anemi | 99,80 % | Vitaminmangel; svak og spekulativ assosiasjon |

---

## Klinisk studieevidens

Det er foreløpig ingen relaterte kliniske studier registrert.

---

## Litteraturevidens

Det er foreløpig ingen relatert litteratur tilgjengelig.

---

## Markedsinformasjon for Norge

| Godkjenningsnummer | Produktnavn | Doseringsform | Godkjent indikasjon |
|---------|------|------|-----------|
| EMEA/H/C/004954 | Ultomiris | – | Paroksysmal nattlig hemoglobinuri (status: kansellert) |

---

## Sikkerhetsvurderinger

- **Kontraindikasjoner fra kunnskapsgraf:** TxGNN-kunnskapsgrafen (PrimeKG) angir en kontraindikasjon-relasjon til **meningokokkinfeksjon**. Dette er hentet fra grafen og ikke fra preparatomtalen. Hemming av terminal komplement er generelt forbundet med økt risiko for alvorlige meningokokkinfeksjoner.
- **Legemiddelinteraksjoner:** Fire interaksjoner er funnet, alle av nivå **Minor**, med humant immunglobulin G (intravenøst, subkutant, intramuskulært, og intravenøst/subkutant kombinert).
- **Merknad ved aktuelle pasientgrupper:** Flere av de predikerte tilstandene innebærer nøytropeni eller immunsvikt. Komplementhemming kan der gi ytterligere økt infeksjonsrisiko.

Se preparatomtalen for fullstendig sikkerhetsinformasjon.

---

## Konklusjon og neste steg

**Beslutning: Hold**

**Begrunnelse:**
Prediksjonen bygger kun på modellscore (evidensnivå L5), uten kliniske studier, uten litteratur og uten støttet mekanistisk kobling. Markedsføringstillatelsen i Norge er kansellert, og sikkerhetsdata fra preparatomtalen mangler.

**For å gå videre kreves følgende:**
- Innhenting og gjennomgang av preparatomtalen (advarsler og kontraindikasjoner), som er en blokkerende datamangel
- Data om virkningsmekanisme (MOA), for eksempel fra DrugBank
- Prekliniske eller mekanistiske studier som viser en rolle for komplement (C5) ved den predikerte sykdommen
- Avklaring av administrasjonsvei og markedsstatus i Norge
- Vurdering av infeksjonsrisiko (særlig meningokokker) hos nøytropene og immunsvekkede pasienter
## Ansvarsfraskrivelse

Dette innholdet er kun til forskningsformål og utgjør ikke medisinsk rådgivning.
Klinisk validering kreves før enhver klinisk anvendelse.

---

