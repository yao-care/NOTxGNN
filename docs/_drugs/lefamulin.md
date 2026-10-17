---
layout: default
title: Lefamulin
parent: Kun modellprediksjon (L5)
nav_order: 237
evidence_level: L5
indication_count: 3
last_modified_at: 2026-10-15
description: "Lefamulin: predikert ny indikasjon Diffus kutan leishmaniasis (evidensnivå L5). Opprinnelig indikasjon: Bakteriell lungebetennelse"
monitor_inn: "Lefamulin"
predicted_indications: ["leishmaniasis, diffuse cutaneous", "polyclonal hyperviscosity syndrome", "hyperamylasemia"]
---

# Lefamulin
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

# Lefamulin: Fra bakteriell lungebetennelse til diffus kutan leishmaniasis

## Oppsummering

Lefamulin er et pleuromutilin-antibiotikum som opprinnelig brukes til behandling av bakteriell samfunnervervet lungebetennelse.
TxGNN-modellen forutsier at det kan ha effekt mot **diffus kutan leishmaniasis**, men det finnes **ingen kliniske studier** og **ingen publikasjoner** som støtter denne prediksjonen. Prediksjonen er kun beregningsbasert.

---

## Hurtigoversikt

| Punkt | Innhold |
|------|------|
| Opprinnelig indikasjon | Bakteriell lungebetennelse; samfunnservervede infeksjoner |
| Predikert ny indikasjon | Diffus kutan leishmaniasis |
| TxGNN-prediksjonsscore | 99,24 % |
| Evidensnivå | L5 |
| Markedsstatus i Norge | Kun avregistrert/trukket tilbake |
| Antall godkjenninger | 1 |
| Anbefalt beslutning | Hold |

---

## Hvorfor er denne prediksjonen (ikke) rimelig?

Detaljerte data om virkningsmekanisme er foreløpig ikke tilgjengelige i de innsamlede dataene. Det som er kjent, er at lefamulin er et pleuromutilin-antibiotikum som hemmer bakteriell proteinsyntese ved å binde seg til peptidyltransferasesenteret i den bakterielle 50S-ribosomale underenheten.

Leishmania er en eukaryot protozo, og den bakterielle ribosommekanismen har ingen etablert kobling til parasitten. En mulig effekt på parasittens mitokondrielle ribosomer er spekulativ og støttes ikke av data. Standardbehandlingene for sykdommen (f.eks. antimonpreparater, amfotericin B og miltefosin) virker via andre mekanismer.

Den høye TxGNN-scoren (0,992) er derfor å regne som en ren modellprediksjon uten biologisk eller klinisk støtte. Den kan gjenspeile artefakter i kunnskapsgrafen.

### Andre predikerte indikasjoner

| Rang | Sykdom | TxGNN-score | Evidensnivå | Vurdering |
|------|------|------|------|------|
| 2 | Polyklonalt hyperviskositetssyndrom | 99,10 % | L5 | Ingen plausibel mekanistisk kobling; sannsynlig grafartefakt |
| 3 | Hyperamylasemi | 99,10 % | L5 | Laboratoriefunn, ikke en sykdom et antibiotikum forventes å behandle; relevans gjelder snarere overvåking av bivirkninger |

Ingen av disse har kliniske studier eller litteratur.

---

## Klinisk studieevidens

Foreløpig er det ingen registrerte kliniske studier knyttet til denne indikasjonen.

---

## Litteraturevidens

Foreløpig finnes det ingen relevant litteratur.

---

## Informasjon om det norske markedet

| Godkjenningsnummer | Produktnavn | Doseringsform | Godkjent indikasjon |
|---------|------|------|-----------|
| EMEA/H/C/005048 | Xenleta | Ikke oppgitt | Bakteriell lungebetennelse; samfunnservervede infeksjoner |

Denne godkjenningen har status avregistrert/trukket tilbake. Det finnes ingen gyldige godkjenninger for tiden.

---

## Sikkerhetsvurderinger

- **Legemiddelinteraksjoner**: Det er registrert 100 interaksjoner i den interaksjonsdatabasen som er brukt. Blant de som er vist, er følgende klassifisert som **alvorlige (Major)**:
  - Deksametason
  - Klaritromycin
  - Dolasetron

  Mange andre er klassifisert som moderate, blant annet famotidin, rabeprazol, omeprazol, dekslansoprazol, cimetidin, hydrokortison, triamcinolon, betametason, budesonid, pioglitazon, saksagliptin, loperamid, aprepitant, bisakodyl, pikosulfat, polyetylenglykol og dronabinol.

Advarsler og kontraindikasjoner fra preparatomtalen mangler i de innsamlede dataene. Se preparatomtalen for fullstendig sikkerhetsinformasjon.

---

## Konklusjon og neste steg

**Beslutning: Hold**

**Begrunnelse:**
Prediksjonen bygger kun på en modellscore (L5) uten kliniske studier, litteratur eller plausibel mekanistisk kobling mellom en bakteriell ribosomhemmer og en eukaryot parasitt. I tillegg er produktet avregistrert i det norske markedet.

**For å gå videre kreves følgende:**
- Data om virkningsmekanisme (MOA) og en vurdering av mulig effekt på Leishmania
- Prekliniske data (in vitro-aktivitet mot Leishmania og dyremodeller)
- Preparatomtale med advarsler og kontraindikasjoner for å gjennomføre sikkerhetsscreening
- Avklaring av markedsstatus og tilgjengelige administrasjonsveier
- Vurdering av om prediksjonen er en artefakt i kunnskapsgrafen
## Ansvarsfraskrivelse

Dette innholdet er kun til forskningsformål og utgjør ikke medisinsk rådgivning.
Klinisk validering kreves før enhver klinisk anvendelse.

---

