---
layout: default
title: Panitumumab
parent: Kun modellprediksjon (L5)
nav_order: 309
evidence_level: L5
indication_count: 2
last_modified_at: 2026-10-15
description: "Panitumumab: predikert ny indikasjon Legemiddelindusert osteoporose (evidensnivå L5). Opprinnelig indikasjon: Kolorektal kreft (Colorectal Neoplasms)"
monitor_inn: "PANITUMUMAB"
predicted_indications: ["drug-induced osteoporosis", "severe nonproliferative diabetic retinopathy"]
---

# Panitumumab
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

## Panitumumab: Fra kolorektal kreft til legemiddelindusert osteoporose
{: .text-alpha }

## Oppsummering i én setning

Panitumumab er et monoklonalt antistoff mot EGFR som opprinnelig brukes mot kolorektal kreft.
TxGNN-modellen forutsier at det kan være effektivt mot **legemiddelindusert osteoporose**, men det finnes foreløpig **ingen kliniske studier** og **ingen publikasjoner** som støtter denne retningen. Prediksjonen er ren modellberegning.

---

## Hurtigoversikt

| Punkt | Innhold |
|------|------|
| Opprinnelig indikasjon | Kolorektal kreft (Colorectal Neoplasms) |
| Foreslått ny indikasjon | Legemiddelindusert osteoporose |
| TxGNN-prediksjonsscore | 99,13 % |
| Evidensnivå | L5 |
| Markedsstatus i Norge | Kun trukket tilbake (ingen gyldige markedsføringstillatelser) |
| Antall tillatelser | 1 |
| Anbefalt beslutning | Hold |

---

## Hvorfor er denne prediksjonen rimelig?

Data om virkningsmekanisme er ikke tilgjengelig i dataene som er sammenstilt for denne rapporten. Basert på kjent informasjon er panitumumab et anti-EGFR-antistoff, og effekten ved kolorektal kreft er dokumentert. Mekanistisk er koblingen til legemiddelindusert osteoporose usikker.

EGFR-signalering kan ha en rolle i osteoblastdifferensiering og benombygging, men effektretningen er uklar. EGFR-hemming kan tvert imot svekke beindannelse i stedet for å beskytte mot tap av benmasse. Anti-EGFR-behandling er også forbundet med hypomagnesemi og hypokalsemi, som kan påvirke benhelsen negativt. Den mekanistiske koblingen er derfor spekulativ og muligens motstridende.

Den høye TxGNN-scoren (0,991) er kun en beregnet prediksjon og er ikke bekreftet av kliniske eller litteraturbaserte data.

### Alternativ prediksjon (rangert nr. 2)

Modellen foreslår også **alvorlig ikke-proliferativ diabetisk retinopati** (score 99,05 %, evidensnivå L5, beslutning: Hold). EGFR-signalering kan bidra til karskade i netthinnen, betennelse og patologisk angiogenese. Panitumumab er imidlertid et stort IgG2-antistoff gitt systemisk med begrenset penetrasjon til øyet, og anti-EGFR-midler gir øyetoksisitet (f.eks. keratitt, overflateproblemer på øyet, trikomegali). Det foreligger ingen intravitreale eller prekliniske data. At produktet kun har trukket tilbake tillatelse, kan også svekke gjennomførbarheten.

---

## Dokumentasjon fra kliniske studier

Det er for tiden ingen relaterte kliniske studier registrert.

---

## Litteraturevidens

Det er for tiden ingen relevant litteratur tilgjengelig.

---

## Markedsinformasjon for Norge

| Tillatelsesnummer | Produktnavn | Doseringsform | Godkjent indikasjon |
|---------|------|------|-----------|
| EMEA/H/C/000741 (trukket tilbake) | Vectibix | – | Kolorektal kreft |

---

## Cytotoksisitet

| Punkt | Innhold |
|------|------|
| Klassifisering | Målrettet terapi (monoklonalt anti-EGFR-antistoff), ikke konvensjonelt cytotoksisk middel |
| Risiko for myelosuppresjon | Se pakningsvedlegget for advarsler og forholdsregler |
| Klassifisering av emetogenisitet | Se pakningsvedlegget for advarsler og forholdsregler |
| Overvåkingspunkter | Se pakningsvedlegget; relevante hensyn er elektrolytter (magnesium, kalsium) samt hud og øyne |
| Håndtering og beskyttelse | Se pakningsvedlegget for advarsler og forholdsregler |

---

## Sikkerhetsvurderinger

**Legemiddelinteraksjoner** (27 registrerte interaksjoner; utvalg av de viktigste):

- **Alvorlig (Major):** bevacizumab, irinotekan (inkl. liposomal), amiodaron, arsentrioksid, dofetilid, dronedaron, droperidol, aminolevulinsyre, levacetylmetadol
- **Moderat:** protonpumpehemmere (omeprazol, esomeprazol, lansoprazol, dexlansoprazol, pantoprazol, rabeprazol), metoksalen, aminolevulinsyre (topisk), disopyramid, idelalisib

For øvrig sikkerhetsinformasjon (advarsler og kontraindikasjoner) vises det til pakningsvedlegget.

---

## Konklusjon og neste steg

**Beslutning: Hold**

**Begrunnelse:**
Begge prediksjonene bygger kun på modellberegning (L5) uten kliniske studier eller publikasjoner. Den mekanistiske koblingen er spekulativ og for osteoporose muligens motstridende. Produktet har dessuten kun en trukket tilbake tillatelse, og sikkerhetsdata fra pakningsvedlegget mangler.

**For å gå videre kreves følgende:**
- Pakningsvedlegg med advarsler og kontraindikasjoner (blokkerende datamangel, må løses før sikkerhetsscreening)
- Data om virkningsmekanisme (MOA) fra DrugBank for å vurdere den mekanistiske koblingen
- Prekliniske eller mekanistiske studier på EGFR-hemming og benombygging (osteoporose) og på netthinnekar (retinopati)
- Avklaring av markedsstatus og tilgjengelighet i Norge, siden tillatelsen er trukket tilbake
- Vurdering av administrasjonsvei og passform (spesielt ved okulær bruk) samt sikkerhetsprofil ved hypomagnesemi, hypokalsemi og øyetoksisitet
## Ansvarsfraskrivelse

Dette innholdet er kun til forskningsformål og utgjør ikke medisinsk rådgivning.
Klinisk validering kreves før enhver klinisk anvendelse.

---

