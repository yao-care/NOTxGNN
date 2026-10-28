---
layout: default
title: Formoterol
parent: Kun modellprediksjon (L5)
nav_order: 179
evidence_level: L5
indication_count: 3
monitor_inn: "formoterol"
predicted_indications: ["respiratory malformation", "bronchitis", "Rienhoff syndrome"]
last_modified_at: 2026-10-27
description: "Formoterol: predikert ny indikasjon Luftveismisdannelse (respiratory malformation) (evidensnivå L5). Opprinnelig indikasjon: Pulmonary Disease, Chronic Obstructive"
---

# Formoterol
{: .fs-9 }

Evidensnivå: **L5** | Predikerte indikasjoner: **3** stk.
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

## Formoterol: langtidsvirkende beta2-agonist → Luftveismisdannelse (respiratory malformation)
{: .text-alpha }

## Oppsummering i én setning

Formoterol er en langtidsvirkende beta2-agonist som utvider luftveiene. Modellen TxGNN spår at legemidlet kan ha effekt ved **luftveismisdannelse (respiratory malformation)**, men for denne sykdommen er det **ingen kliniske studier** og **ingen publikasjoner som direkte omhandler tilstanden**, så støtten er svært svak.

---

## Hurtigoversikt

| Punkt | Innhold |
|------|------|
| Opprinnelig indikasjon | Pulmonary Disease, Chronic Obstructive; Pulmonary Disease, Chronic Obstructive;Asthma; Asthma;Pulmonary Disease, Chronic Obstructive |
| Foreslått ny indikasjon | Luftveismisdannelse (respiratory malformation) |
| TxGNN-prediksjonsscore | 0,9992 |
| Evidensnivå | L5 |
| Markedsstatus i Norge | Markedsført (gyldige tillatelser: 10 av 10) |
| Antall godkjenninger | 10 (gyldige: 10) |
| Anbefalt beslutning | Hold |

---

## Hvorfor er denne prediksjonen rimelig?

Detaljerte data om virkningsmekanisme er ikke tilgjengelige i de innsamlede dataene. Formoterol tilhører klassen langtidsvirkende beta2-adrenerge agonister, som slapper av glatt muskulatur i luftveiene og bedrer luftstrømmen.

Det er imidlertid ingen troverdig mekanistisk kobling til strukturelle, medfødte misdannelser i luftveiene. Bronkodilatasjon kan ikke korrigere utviklingsmessige anatomiske avvik. Den høye scoren gjenspeiler trolig nærhet i grafmodellen til obstruktive luftveissykdommer som astma og KOLS, snarere enn et reelt terapeutisk forhold. Prediksjonen bør derfor tolkes med stor forsiktighet.

---

## Kliniske studier

Det er for øyeblikket ingen registrerte kliniske studier knyttet til luftveismisdannelse.

---

## Litteraturevidens

De identifiserte publikasjonene omhandler i hovedsak KOLS, astma og andre tilstander, ikke luftveismisdannelse som sådan. Kun de mest relevante er oppsummert.

| PMID | År | Type | Tidsskrift | Hovedfunn |
|------|-----|------|------|---------|
| [40840693](https://pubmed.ncbi.nlm.nih.gov/40840693/) | 2026 | RCT (metaanalyse) | J Am Pharm Assoc | Sikkerhet og effekt av budesonid/glykopyrrolat/formoterol versus glykopyrrolat/formoterol ved KOLS |
| [35115339](https://pubmed.ncbi.nlm.nih.gov/35115339/) | 2022 | RCT | Eur Respir J | Budesonid/formoterol sammenlignet med salbutamol ved stabil astma |
| [22541245](https://pubmed.ncbi.nlm.nih.gov/22541245/) | 2012 | RCT | J Allergy Clin Immunol | Langtidssikkerhet av budesonid/formoterol hos afroamerikanske astmapasienter |
| [20528601](https://pubmed.ncbi.nlm.nih.gov/20528601/) | 2010 | Oversikt | J Asthma | Gjennomgang av budesonid/formoterol ved vedvarende astma |
| [35034195](https://pubmed.ncbi.nlm.nih.gov/35034195/) | 2022 | Kohort | Eur J Appl Physiol | Kompensatoriske responser på økt mekanisk belastning ved KOLS under søvn |
| [14738234](https://pubmed.ncbi.nlm.nih.gov/14738234/) | 2004 | RCT | Eur Respir J | Formoterol beskytter mot PAF-induserte effekter ved astma |

Ingen av disse studerer luftveismisdannelse direkte.

---

## Markedsinformasjon for Norge

| Godkjenningsnummer | Produktnavn | Legemiddelform | Godkjent indikasjon |
|---------|------|------|-----------|
| EMEA/H/C/003745 | Duaklir Genuair | – | Kronisk obstruktiv lungesykdom |
| EMEA/H/C/003890 | BiResp Spiromax | – | Kronisk obstruktiv lungesykdom, astma |
| EMEA/H/C/003969 | Brimica Genuair | – | Kronisk obstruktiv lungesykdom |
| EMEA/H/C/004245 | Bevespi Aerosphere | – | Kronisk obstruktiv lungesykdom |
| EMEA/H/C/002348 | DuoResp Spiromax | – | Kronisk obstruktiv lungesykdom, astma |

Merk: Listen er et utvalg av de registrerte godkjenningene, og flere av dem gjelder kombinasjonsprodukter.

---

## Sikkerhetsvurderinger

**Legemiddelinteraksjoner:** Det er registrert 463 mulige interaksjoner. Blant de som er nevnt er:
- Moderate: akarbose, famotidin, klaritromycin, cisaprid, dolasetron, efedrin, samt flere diabetesmidler (f.eks. dapagliflozin, empagliflozin, canagliflozin, alogliptin)
- Mindre: beklometason, betametason, budesonid, deksametason

For øvrig sikkerhetsinformasjon, se preparatomtalen.

---

## Konklusjon og neste steg

**Beslutning: Hold**

**Begrunnelse:**
Det finnes ingen kliniske studier og ingen publikasjoner som direkte studerer luftveismisdannelse, og det mangler en troverdig mekanistisk kobling. Den høye TxGNN-scoren alene er ikke tilstrekkelig grunnlag for å gå videre.

**For å gå videre kreves følgende:**
- Dokumentasjon av en biologisk eller klinisk begrunnelse for at en beta2-agonist kan påvirke tilstanden
- Data om virkningsmekanisme
- Preparatomtale med advarsler og kontraindikasjoner for sikkerhetsvurdering
- Eventuelt prekliniske eller eksplorative kliniske data som direkte omhandler sykdommen
## Ansvarsfraskrivelse

Dette innholdet er kun til forskningsformål og utgjør ikke medisinsk rådgivning.
Klinisk validering kreves før enhver klinisk anvendelse.

---

