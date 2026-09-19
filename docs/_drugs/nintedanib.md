---
layout: default
title: Nintedanib
parent: Moderat evidens (L3-L4)
nav_order: 244
evidence_level: L4
indication_count: 3
---

# Nintedanib
{: .fs-9 }

Evidensnivå: **L4** | Predikerte indikasjoner: **3** stk.
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

# Nintedanib: Fra idiopatisk lungefibrose til dermatofibrosarkom protuberans

## Sammendrag i én setning

> Nintedanib er en trippel angiokinasehemmer (som retter seg mot VEGFR/FGFR/PDGFR) med internasjonal godkjenning for idiopatisk lungefibrose (IPF) og, i kombinasjon med docetaxel, for ikke-småcellet lungekreft.
> TxGNN-modellen forutsier at det kan være effektivt for **Dermatofibrosarkom protuberans (DFSP)**,
> men for tiden **0 kliniske studier** og bare **1 ikke-spesifikk oversiktsartikkel** støtter denne retningen — saken hviler på mekanistisk plausibilitet snarere enn direkte klinisk bevis.

*Merk: denne bevissamlingen inneholder ingen norsk lisensdata for nintedanib (markedsstatus: ikke markedsført, 0 godkjenninger), så den opprinnelige indikasjonen ovenfor gjenspeiler legemidlets kjente internasjonale godkjenninger snarere enn en norskspesifikk merking.*

---

## Hurtig oversikt

| Element | Innhold |
|------|---------|
| Opprinnelig indikasjon | Idiopatisk lungefibrose (IPF); ikke-småcellet lungekreft (i kombinasjon med docetaxel) — generell internasjonal indikasjon; ingen norskspesifikk lisenstekst tilgjengelig |
| Forutsagt ny indikasjon | Dermatofibrosarkom protuberans |
| TxGNN-prediksjonspoengsum | 99.15% |
| Bevisnivå | L4 |
| Norsk markedsstatus | Ikke markedsført (Ikke markedsført) |
| Antall godkjenninger | 0 |
| Anbefalt beslutning | Hold |

---

## Hvorfor er denne prediksjonen rimelig?

Nintedanib beskrives i bevissamlingens ombruksrasjonale som en **trippel angiokinasehemmer**, med aktivitet mot PDGFRα/β i tillegg til VEGFR og FGFR (selve `original_moa`-feltet på legemiddelnivå er flagget som et datahull — DG002 — men denne mekanistiske detaljen er bevart i rasjonalteksten). Denne PDGFR-hemmende aktiviteten er det farmakologiske grunnlaget for DFSP-prediksjonen.

DFSP er en godt karakterisert bløtvevstumor drevet av **COL1A1-PDGFB fusjonsgenet**, som forårsaker konstant aktivering av PDGFRB-reseptoren — dette er en etablert, læreboksmessig onkogen mekanisme, og det er nettopp hvorfor det nåværende standardbehandlingsmidlet for DFSP (imatinib) virker ved å hemme PDGFR. Fordi nintedanib også hemmer PDGFR-signalering, er det en plausibel teoretisk overlapping mellom dets farmakologi og DFSPs drivervei, som er konsistent med modellens meget høye prediksjonspoengsum (0.9915).

Imidlertid er dette fortsatt en **mekanisme-nivå-hypotese, ikke en påvist klinisk effekt**. Det finnes ingen nintedanib-spesifikk klinisk studie eller kasusdata for DFSP; den eneste støttende litteraturen er en generell oversikt over PDGFR-hemmer-legemiddelklassens farmakologi, ikke en nintedanib-/DFSP-spesifikk studie.

To ytterligere kandidater ble flagget av modellen med lignende poengsum — **liposarkom** (0.9913, rang 8457) og **myksoid liposarkom i ovariene** (0.9911, rang 8580) — men begge er bevisnivå L5 (bare modellprediksjoner, ingen støttende studier eller litteratur) og har svakere eller ubekreftet mekanistisk rasjonale (liposarkomsubtyper viser bare inkonsistent PDGFR/FGFR-oppregulering; myksoid liposarkom er drevet av FUS-DDIT3/EWSR1-DDIT3, en vei uten etablert kobling til nintedanibs mål). Begge anbefales **Hold** og forfølges ikke videre i denne rapporten.

---

## Klinisk studiebevis

For tiden ingen relaterte kliniske studier registrert.

---

## Litteraturbevis

| PMID | År | Type | Tidsskrift | Viktige funn |
|------|-----|------|------|---------|
| [29408302](https://pubmed.ncbi.nlm.nih.gov/29408302/) | 2018 | Oversikt | Pharmacological Research | Gjennomgår rollen av småmolekyl-PDGFR-hemmere (som en legemiddelklasse) i behandlingen av neoplastiske lidelser; diskuterer PDGF/PDGFR-biologi relevant for tumorer som DFSP, men rapporterer ikke nintedanib-spesifikk eller DFSP-spesifikk klinisk data |

---

## Norsk markedsinformasjon

Nintedanib er for tiden **ikke markedsført i Norge** (0 markedsføringsgodkjenninger på register), så ingen lisens-/produkttabell er tilgjengelig.

---

## Sikkerhetshensyn

Vennligst se pakningsvedlegget for sikkerhetsinformasjon.

*(Ingen strukturerte viktige advarsler, kontraindikasjoner eller legemiddelinteraksjonsdata er for tiden tilgjengelige i denne bevissamlingen — TFDA/norsk pakningsvedleggsdata er flagget som et blokkerende datahull, DG001.)*

---

## Konklusjon og neste trinn

**Beslutning: Hold**

**Begrunnelse:**
- Den mekanistiske rasjonalen (PDGFR-hemming som overlapper med DFSPs COL1A1-PDGFB drivervei) er biologisk plausibel og gjenspeiler den etablerte mekanismen for den nåværende DFSP-standarden (imatinib), som er hvorfor TxGNN tildeler en meget høy poengsum. Imidlertid finnes det null kliniske studier og ingen legemiddelspesifikk litteratur som bekrefter dette i praksis — bevisnivå L4 betyr at dette for tiden er en forskningshypotese, ikke en validert ombrukskandidat.

**For å gå videre, er følgende nødvendig:**
- Norsk/TFDA-pakningsvedleggsdata — viktige advarsler og kontraindikasjoner (DG001, Blocking)
- Bekreftet strukturert dokumentasjon av virkningsmekanisme fra DrugBank (DG002, High)
- Preklinisk (in vitro/in vivo) eller kasusrapportbevis for nintedanib-aktivitet spesifikt i DFSP
- Avklaring av norsk regulatorisk/markedsvei, gitt at legemidlet for tiden ikke har noen lokal markedsføringsgodkjenning

## Ansvarsfraskrivelse

Dette innholdet er kun til forskningsformål og utgjør ikke medisinsk rådgivning.
Klinisk validering kreves før enhver klinisk anvendelse.

---

