---
layout: default
title: Lipegfilgrastim
parent: Kun modellprediksjon (L5)
nav_order: 211
evidence_level: L5
indication_count: 5
---

# Lipegfilgrastim
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

# Lipegfilgrastim: Fra kjemoterapiindusert neutropeni til primær utløsningsforstyrrelser av blodplater

## Sammendrag på én setning

Lipegfilgrastim er en pegylert rekombinant menneskelig G-CSF-analog som er kjent klinisk for behandling av kjemoterapiindusert neutropeni.
TxGNN-modellen forutsier at det kan være effektivt for **Primær utløsningsforstyrrelser av blodplater**,
men denne prediksjonen er for øyeblikket støttet av **0 kliniske studier** og **0 publikasjoner** — det er en hypotese basert utelukkende på modellen uten empirisk bevis.

## Raskt overblikk

| Punkt | Innhold |
|------|------|
| Opprinnelig indikasjon | Kjemoterapiindusert neutropeni (basert på kjent informasjon om legemiddelklasse; ikke bekreftet i kildebevisematerialet) |
| Forutsagt ny indikasjon | Primær utløsningsforstyrrelser av blodplater |
| TxGNN-prediksjonspoengsum | 99.93% |
| Bevisnivå | L5 |
| Markedsstatus i Norge | ✗ Ikke markedsført |
| Antall godkjennelser | 0 |
| Anbefalt beslutning | Avvent |

## Hvorfor er denne prediksjonen rimelig?

For øyeblikket er detaljerte data om virkningsmekanisme ikke tilgjengelige (flagget som et datahull med høy alvorlighetsgrad). Basert på kjent informasjon er lipegfilgrastim en pegylert rekombinant menneskelig G-CSF-analog som stimulerer proliferasjon og differensiering av granulocytt (nøytrofil) prekursorceller i benmargen, og dets effektivitet for kjemoterapiindusert neutropeni er godt etablert.

Imidlertid innebærer den forutsagte nye indikasjonen — primær utløsningsforstyrrelser av blodplater — en patologi med defekt frigjøring av innhold fra blodplategranuler, en mekanisme uten kjent overlapping med nøytrofil-stimulerende G-CSF-aktivitet. Bevisematerialets egen mekanistiske vurdering slår eksplisitt fast at det ikke finnes noen verifiserbar biologisk vei som forbinder de to, og denne rangeringen (poengsum 0.9993, grafrangering 1044) gjenspeiler TxGNN-kunnskapsgrafs assosiasjonspoengsum alene, ikke en validert farmakologisk hypotese.

De fire gjenværende forutsagte indikasjonene i dette bevisematerialet (alvorlig ikke-proliferativ diabetisk retinopati, pseudo-von Willebrand-sykdom, Glanzmann trombasteni, diabetisk retinopati) viser lignende svake eller spekulative mekanistiske forbindelser — alt fra en ubevist hypotese om mobilisering av endotel-stamceller til strukturelt/genetisk definerte blodplateavvik uten cytokinmodulert vei. Ingen stiger for øyeblikket over L5 (bare modellprediksjon).

## Bevis fra kliniske studier

Ingen relaterte kliniske studier registrert for øyeblikket

## Bevis fra litteratur

Ingen relatert litteratur tilgjengelig for øyeblikket

## Markedsinformasjon for Norge

Lipegfilgrastim er ikke for øyeblikket markedsført i Norge (0 godkjennelser på register). Ingen produktlisensdata er tilgjengelig.

## Sikkerhetshensyn

Vennligst se pakningsvedlegg for sikkerhetsinformasjon.

*Merk: Et blokerend datahull (DG001) finnes for TFDA advarsel- og kontraindikasjondata, som hindrer denne kandidaten fra å gå inn i S1-sikkerhetsforfasen.*

## Konklusjon og neste trinn

**Beslutning: Avvent**

**Begrunnelse:**
Alle fem forutsagte indikasjonene forblir på bevisstadium S0 (bare modellprediksjon) uten støttende kliniske studier eller litteratur, og et blokerend sikkerhetsdatahull hindrer fremgang til formell sikkerhetsvurdering på S1-stadiet. Den mekanistiske begrunnelsen for topprediksjonen er eksplisitt vurdert som biologisk usannsynlig.

**For å gå videre kreves følgende:**
- TFDA/regulatoriske advarsel- og kontraindikasjondata (Blokeringshull, DG001) — obligatorisk før eventuell S1-sikkerhetsvurdering
- Bekreftet opprinnelig virkningsmåte (MOA) data via DrugBank API (Høyt prioritert hull, DG002)
- Uavhengig litteratur eller prekliniske bevis som etablerer en biologisk vei mellom G-CSF-aktivitet og blodplatefrigi gjøring/funksjonsavvik
- Registrering av dedikerte kliniske studier, eller identifisering av eksisterende off-label casedata, for noen av de fem kandidatindikasjonene

## Ansvarsfraskrivelse

Dette innholdet er kun til forskningsformål og utgjør ikke medisinsk rådgivning.
Klinisk validering kreves før enhver klinisk anvendelse.

---

