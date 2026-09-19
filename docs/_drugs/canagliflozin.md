---
layout: default
title: Canagliflozin
parent: Kun modellprediksjon (L5)
nav_order: 70
evidence_level: L5
indication_count: 0
---

# Canagliflozin
{: .fs-9 }

Evidensnivå: **L5** | Predikerte indikasjoner: **0** stk.
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

# Canagliflozin: Evaluering av legemiddelombruk — Prediksjonsdata utilgjengelig

## Sammendrag i én setning

Canagliflozin (DrugBank DB08907) er et legemiddel som evalueres for ombrukspotensialet via TxGNN-modellen. Imidlertid **inneholder denne Evidence Pack ingen TxGNN-prediksjonsresultater**, og både de opprinnelige indikasjonsdata og virkningsmekanismen er for tiden fraværende. Denne rapporten fungerer som en **oppsummering av datamangeler** og handlingsplan for utbedring i stedet for en fullstendig ombruksevaluering.

---

## Kort oversikt

| Element | Innhold |
|---------|---------|
| Opprinnelig indikasjon | Ingen data tilgjengelig i denne Evidence Pack |
| Forutsagt ny indikasjon | Ingen TxGNN-prediksjonsresultater tilgjengelige |
| TxGNN-prediksjonspoeng | — |
| Bevisnivå | L5 (modellprediksjon ikke ennå tilgjengelig) |
| Status i norsk marked | Ikke markedsført |
| Antall autoriseringer | 0 |
| Anbefalt beslutning | **Behold** |

---

## Hvorfor er denne prediksjonen rimelig?

For tiden er detaljerte data om virkningsmekanisme ikke tilgjengelig i denne Evidence Pack (datamangel DG002). Feltet `original_moa` mangler, og ingen opprinnelige indikasjoner er registrert i regelverksdata.

Basert på offentlig tilgjengelig farmakologisk kunnskap tilhører Canagliflozin klassen av natriumglukose-kotransporter-2 (SGLT2)-hemmere. Denne klassen virker ved å blokkere glukosereabsorpsjon i den proksimale tubelen i nyrene, noe som fører til glukosuri og reduksjon av blodsukker. Utover glykemisk kontroll har SGLT2-hemmere demonstrert kardiovaskulære og renale beskyttende effekter som er delvis uavhengige av deres blodsukkerreduserende mekanisme — noe som gjør dem av interesse i metabolske, kardiale og renale ombukskontekster.

Imidlertid, fordi `predicted_indications`-matrisen i denne Evidence Pack er tom, **er ingen formell TxGNN-ombruksprediksjon lastet inn**. En mekanistisk begrunnelse for enhver spesifikk ny indikasjon kan ikke bekreftes fra disse data alene. Det er nødvendig å kjøre TxGNN-pipelinen på nytt med komplette legemiddel-sykdoms-graf-innleiringer før man fortsetter med ombruksevaluering.

---

## Bevis fra kliniske studier

For tiden er ingen relaterte kliniske studier registrert i denne Evidence Pack.

---

## Litteraturbevis

For tiden er ingen relatert litteratur tilgjengelig i denne Evidence Pack.

---

## Informasjon om norsk marked

Canagliflozin har **ingen registrerte autoriseringer** i Norge basert på gjeldende Evidence Pack. Ingen lisensposter er tilgjengelige.

---

## Sikkerhetshensyn

Vennligst se pakningsvedlegget for sikkerhetsinformasjon.

> **Merk:** Viktige advarsler, kontraindikasjoner og legemiddel-legemiddel-interaksjonsdata mangler alle fra denne Evidence Pack. Datamangelen DG001 (TFDA-pakningsvedlegg-advarsler) er klassifisert som **blokkerings-alvorlighetsgrad**, noe som betyr at sikkerhetsvurderingen ikke kan fortsette før denne mangelen er løst.

---

## Konklusjon og neste trinn

**Beslutning: Behold**

**Begrunnelse:**
Denne Evidence Pack er kritisk ufullstendig — `predicted_indications`-matrisen er tom, MOA-data mangler, sikkerhetdata er utilgjengelig, og det er ingen norske regelverksregistreringer. Det er et utilstrekkelig grunnlag for å evaluere noen ombukshypotese på dette stadiet.

**For å fortsette, trengs følgende:**

- **[Blokkering — DG001]** Innhent og parse TFDA-pakningsvedlegg-PDF for å trekke ut viktige advarsler og kontraindikasjoner
- **[Høy — DG002]** Spør DrugBank API for Canagliflozin MOA, farmakodynamikk og legemiddelkategorier
- **[Kritisk]** Kjør TxGNN-prediksjons-pipelinen på nytt for å populere `predicted_indications` — dette er leveransen som er kritisk; uten den kan ingen ombruksevaluering gjennomføres
- Verifiser norsk/EMA-regelverksstatus via Norges legemiddelverket (NoMA / Legemiddelverket) for å bekrefte om noen autoriseringer finnes under merkenavn (f.eks. Invokana, Vokanamet)
- Etter å ha innhentet DDI-data, foreta screening for legemiddelinteraksjoner mot vanlige samlegemidler som er relevante for kandidatindikasjonen

## Ansvarsfraskrivelse

Dette innholdet er kun til forskningsformål og utgjør ikke medisinsk rådgivning.
Klinisk validering kreves før enhver klinisk anvendelse.

---

