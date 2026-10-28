---
layout: default
title: Darolutamide
parent: Kun modellprediksjon (L5)
nav_order: 113
evidence_level: L5
indication_count: 3
last_modified_at: 2026-10-28
description: "Darolutamide: predikert ny indikasjon Homozygot familiær hypercholesterolemi (evidensnivå L5). Opprinnelig indikasjon: Kastrasjonsresistent prostatakreft"
monitor_inn: "DAROLUTAMIDE"
predicted_indications: ["homozygous familial hypercholesterolemia", "multiple endocrine neoplasia", "HIV infectious disease"]
---

# Darolutamide
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

## Darolutamid: Fra kastrasjonsresistent prostatakreft til homozygot familiær hyperkolesterolemi
{: .text-alpha }

## Oppsummering i én setning

Darolutamid er en androgenreseptorantagonist som opprinnelig brukes til behandling av **kastrasjonsresistent prostatakreft**.
TxGNN-modellen forutsier at legemidlet kan ha effekt ved **homozygot familiær hypercholesterolemi**, men dette er en ren modellprediksjon: det finnes **ingen kliniske studier** og **ingen publikasjoner** som støtter den.

---

## Hurtigoversikt

| Punkt | Innhold |
|------|------|
| Opprinnelig indikasjon | Kastrasjonsresistent prostatakreft |
| Predikert ny indikasjon | Homozygot familiær hypercholesterolemi |
| TxGNN-prediksjonsscore | 0,9911 |
| Evidensnivå | L5 |
| Markedsstatus i Norge | Markedsført (gyldige tillatelser: 1 av 1) |
| Antall godkjenninger | 1 (gyldige: 1) |
| Anbefalt beslutning | Hold |

---

## Hvorfor er denne prediksjonen rimelig?

Darolutamid er en androgenreseptorantagonist. Detaljerte data om virkningsmekanisme er ikke tilgjengelige i datagrunnlaget som er samlet for denne rapporten, så mekanismeanalysen er begrenset.

Homozygot familiær hyperkolesterolemi skyldes defekter i LDL-reseptorveien. Det finnes ingen opplagt kobling til androgenreseptorsignalering i de tilgjengelige dataene. Den høye scoren (0,9911) kommer fra TxGNN-modellen (deep learning) og kan gjenspeile likheter modellen har lært mellom beslektede sykdommer, ikke biologisk eller klinisk dokumentasjon.

Prediksjonen bør derfor regnes som en hypotese uten støtte. Den bør ikke tolkes som et signal om at legemidlet virker ved sykdommen.

---

## Kliniske studier

Foreløpig ingen relaterte kliniske studier registrert for denne indikasjonen.

---

## Litteraturevidens

Foreløpig ingen relatert litteratur tilgjengelig.

---

## Markedsinformasjon for Norge

| Godkjenningsnummer | Produktnavn | Doseringsform | Godkjent indikasjon |
|---------|------|------|-----------|
| EMEA/H/C/004790 | Nubeqa | – | Kastrasjonsresistent prostatakreft |

Denne godkjenningen er gyldig (1 av 1 gyldige godkjenninger), og legemidlet er markedsført.

---

## Cytotoksisitet

Darolutamid er et legemiddel mot kreft, men det er en hormonell/målrettet behandling (androgenreseptorhemmer) og ikke en konvensjonell cytostatika. Datagrunnlaget inneholder ingen toksisitetsdata.

| Punkt | Innhold |
|------|------|
| Klassifisering | Målrettet hormonbehandling (androgenreseptorantagonist), ikke konvensjonelt cytotoksisk |
| Risiko for myelosuppresjon | Se pakningsvedlegget for advarsler og forsiktighetsregler |
| Emetogenisitet | Se pakningsvedlegget for advarsler og forsiktighetsregler |
| Overvåkingspunkter | Se pakningsvedlegget for advarsler og forsiktighetsregler |
| Håndteringsbeskyttelse | Se pakningsvedlegget for advarsler og forsiktighetsregler |

---

## Sikkerhetsvurderinger

- **Legemiddelinteraksjoner**: Det er registrert 100 interaksjoner. Blant de første 20 som ble gjennomgått, er følgende klassifisert som **alvorlige (Major)**:
  - Deksametason
  - Eluksadolin
  - Rosuvastatin

  Flere moderate interaksjoner er også registrert, blant annet med klaritromycin, empagliflozin, glyburid, repaglinid, simvastatin, sulfasalazin, kobicistat, deferasirox og eltrombopag. Interaksjonene med rosuvastatin og simvastatin er særlig relevante hvis legemidlet skulle vurderes ved hyperkolesterolemi, siden pasientene som regel bruker statiner.

For øvrig sikkerhetsinformasjon (advarsler og kontraindikasjoner), se pakningsvedlegget.

---

## Konklusjon og neste steg

**Beslutning: Hold**

**Begrunnelse:**
Prediksjonen bygger kun på modellscore uten kliniske studier, litteratur eller en plausibel mekanistisk kobling. I tillegg er den norske godkjenningen ikke lenger gyldig, og viktig sikkerhetsinformasjon mangler.

**For å gå videre kreves følgende:**
- Hente og analysere pakningsvedlegget (advarsler og kontraindikasjoner), som i dag er en blokkerende datamangel
- Innhente detaljerte data om virkningsmekanisme (f.eks. fra DrugBank)
- Prekliniske data eller en mekanistisk hypotese som knytter androgenreseptorhemming til LDL-metabolisme
- Gjennomgang av interaksjoner med statiner og andre lipidsenkende midler
- Avklaring av markedsstatus og regulatorisk situasjon i Norge

---

## Andre predikerte indikasjoner (til orientering)

| Predikert indikasjon | TxGNN-score | Evidensnivå | Anbefaling |
|------|------|------|------|
| Multippel endokrin neoplasi | 0,9906 | L5 | Hold |
| HIV-infeksjon | 0,9904 | L5 | Hold |

For multippel endokrin neoplasi er to studier registrert (NCT07795177 og NCT03878524), men begge gjelder prostatakreft eller presisjonsonkologi, har lav relevans og gir ingen tolkbar evidens for denne indikasjonen. For HIV-infeksjon finnes ingen studier eller litteratur, og de mange registrerte legemiddelinteraksjonene måtte vurderes nøye før videre utforskning.
## Ansvarsfraskrivelse

Dette innholdet er kun til forskningsformål og utgjør ikke medisinsk rådgivning.
Klinisk validering kreves før enhver klinisk anvendelse.

---

