---
layout: default
title: Mecasermin
parent: Kun modellprediksjon (L5)
nav_order: 259
evidence_level: L5
indication_count: 4
last_modified_at: 2026-10-15
description: "Mecasermin: predikert ny indikasjon Monosomi X (evidensnivå L5). Opprinnelig indikasjon: Laron syndrom"
monitor_inn: "MECASERMIN"
predicted_indications: ["monosomy X", "Wolman disease with hypolipoproteinemia and acanthocytosis", "esophageal varices with bleeding", "esophageal varices without bleeding"]
---

# Mecasermin
{: .fs-9 }

Evidensnivå: **L5** | Predikerte indikasjoner: **4** stk.
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

## Mecasermin: Fra Laron syndrom til monosomi X
{: .text-alpha }

## Sammendrag i én setning

Mecasermin er rekombinant IGF-1 (insulinlignende vekstfaktor 1), opprinnelig godkjent for behandling av Laron syndrom (vekstveksthormon-insensitivitet).
TxGNN-modellen predikerer at legemidlet kan ha effekt ved **monosomi X** (Turner syndrom), men dette er **kun en modellprediksjon**: de innsamlede dataene inneholder **ingen kliniske studier** og **ingen publikasjoner** som støtter indikasjonen.

---

## Hurtigoversikt

| Punkt | Innhold |
|------|------|
| Opprinnelig indikasjon | Laron syndrom |
| Predikert ny indikasjon | Monosomi X |
| TxGNN-prediksjonsscore | 0,9959 |
| Evidensnivå | L5 |
| Markedsstatus i Norge | Markedsført (gyldige tillatelser: 1 av 1) |
| Antall godkjenninger | 1 (gyldige: 1) |
| Anbefalt beslutning | Hold |

---

## Hvorfor er denne prediksjonen rimelig?

Det finnes for tiden ingen detaljerte data om virkningsmekanisme i de innsamlede dataene. Mecasermin er imidlertid rekombinant IGF-1, som virker nedstrøms for veksthormon (GH). Effekten ved Laron syndrom, der kroppen ikke responderer på veksthormon, er etablert.

Monosomi X (Turner syndrom) kjennetegnes blant annet av kortvoksthet, og standardbehandlingen er veksthormon. En IGF-1-begrunnelse er derfor biologisk plausibel. Pasienter med Turner syndrom har imidlertid vanligvis intakt GH–IGF-1-signalering, så det er uklart om erstatning med IGF-1 gir noen fordel fremfor veksthormon. Den høye scoren (0,9959) er ikke støttet av kliniske data.

### Øvrige predikerte indikasjoner (alle L5, Hold)

| Rang | Sykdom | Score | Vurdering |
|------|------|------|------|
| 2 | Wolmans sykdom med hypolipoproteinemi og akantocytose | 0,9909 | Ingen klar mekanistisk kobling; scoren gjenspeiler trolig nettverksassosiasjoner |
| 4 | Øsofagusvaricer med blødning | 0,9903 | Ingen etablert kobling; IGF-1s mitogene og væskeretinerende effekter gir ekstra sikkerhetsbekymring ved portal hypertensjon |
| 5 | Øsofagusvaricer uten blødning | 0,9903 | Identisk score som rang 4, noe som tyder på duplikat i prediksjonsgrafen |

---

## Klinisk studiedokumentasjon

Det er for tiden ingen relaterte kliniske studier registrert.

---

## Litteraturdokumentasjon

Det er for tiden ingen relatert litteratur tilgjengelig.

---

## Informasjon om det norske markedet

| Godkjenningsnummer | Produktnavn | Doseform | Godkjent indikasjon |
|---------|------|------|-----------|
| EMEA/H/C/000704 | Increlex | – | Laron syndrom (status: kansellert) |

---

## Sikkerhetshensyn

**Legemiddelinteraksjoner:** Det er funnet 24 interaksjoner, alle klassifisert som **moderate**. De omfatter hovedsakelig blodsukkersenkende legemidler, der risikoen er additiv hypoglykemi (IGF-1 har insulinlignende effekt):

- **Sulfonylurea:** klorpropamid, acetoheksamid, glimepirid, glipizid, glyburid
- **Glinider:** nateglinid
- **Insuliner:** humant insulin (vanlig, isofan, sink, forlenget sink, inhalasjon), insulin aspart (inkl. protamin), degludec, detemir, glargin, glulisin, lispro (inkl. protamin)

Pakningsvedlegget bør konsulteres for øvrig sikkerhetsinformasjon, inkludert advarsler og kontraindikasjoner.

---

## Konklusjon og neste steg

**Beslutning: Hold**

**Begrunnelse:**
Prediksjonen er kun modellbasert (evidensnivå L5) uten kliniske studier eller publikasjoner. Mekanismen ved Turner syndrom er plausibel, men fordelen sammenlignet med standard veksthormonbehandling er uklar. I tillegg er den eneste norske godkjenningen kansellert.

**For å gå videre kreves følgende:**
- Systematisk litteratur- og kasuistikksøk, særlig for veksthormoninsensitivitet med immundysregulering (rang 3) og for Turner syndrom
- Data om virkningsmekanisme (MOA) fra DrugBank
- Pakningsvedlegg med advarsler og kontraindikasjoner for sikkerhetsscreening
- Avklaring av hvorfor godkjenningen i Norge er kansellert, og av tilgjengelige administrasjonsveier
- Vurdering av nytte kontra veksthormon ved Turner syndrom, samt overvåkingsplan for hypoglykemi
## Ansvarsfraskrivelse

Dette innholdet er kun til forskningsformål og utgjør ikke medisinsk rådgivning.
Klinisk validering kreves før enhver klinisk anvendelse.

---

