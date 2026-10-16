---
layout: default
title: Regadenoson
parent: Kun modellprediksjon (L5)
nav_order: 351
evidence_level: L5
indication_count: 4
last_modified_at: 2026-10-15
description: "Regadenoson: predikert ny indikasjon Anafylaksi (evidensnivå L5). Opprinnelig indikasjon: Myokardperfusjonsavbildning"
monitor_inn: "REGADENOSON"
predicted_indications: ["anaphylaxis", "food-dependent exercise-induced anaphylaxis", "esotropia", "pseudoallergy"]
---

# Regadenoson
{: .fs-9 }

Evidensnivå: **L5** | Predikerte indikasjoner: **4** stk.
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

# Regadenoson: Fra myokardperfusjonsavbildning til anafylaksi

## Oppsummering i én setning

Regadenoson er en selektiv A2A-adenosinreseptoragonist som opprinnelig brukes som diagnostisk middel ved myokardperfusjonsavbildning (MPI).
TxGNN-modellen predikerer at legemidlet kan ha effekt ved **anafylaksi**,
men det finnes foreløpig **0 kliniske studier** og **0 publikasjoner** som støtter denne retningen. Prediksjonen er rent beregningsbasert.

---

## Hurtigoversikt

| Punkt | Innhold |
|------|------|
| Opprinnelig indikasjon | Myokardperfusjonsavbildning |
| Predikert ny indikasjon | Anafylaksi |
| TxGNN-prediksjonsscore | 99,85 % |
| Evidensnivå | L5 |
| Markedsstatus i Norge | Kun avregistrert (ingen gyldig markedsføringstillatelse) |
| Antall tillatelser | 1 (avregistrert) |
| Anbefalt beslutning | Hold |

---

## Hvorfor er denne prediksjonen rimelig?

Detaljerte data om virkningsmekanisme er foreløpig ikke tilgjengelige i datagrunnlaget. Regadenoson er kjent som en selektiv A2A-adenosinreseptoragonist, og dataene viser også binding til A1-, A2B- og A3-reseptorer. Effekten er godt dokumentert for koronar vasodilatasjon ved myokardperfusjonsavbildning.

Den teoretiske koblingen til anafylaksi er at A2A-signalering generelt har antiinflammatoriske effekter og kan dempe aktivering av mastceller og andre immunceller i prekliniske modeller. Samtidig kan adenosinreseptoraktivitet på mastceller (særlig A2B og A3) fremme degranulering, så effektretningen er usikker. Legemidlets vasodilaterende og blodtrykkssenkende virkning kan dessuten forverre hemodynamikken ved anafylaksi.

Prediksjonen hviler dermed kun på en høy TxGNN-score, uten støtte fra studier eller litteratur. De øvrige predikerte indikasjonene har enda svakere grunnlag:

| Predikert indikasjon | TxGNN-score | Vurdering |
|------|------|------|
| Næringsmiddelavhengig anstrengelsesutløst anafylaksi | 99,74 % | Samme resonnement som for anafylaksi; sjelden undertype uten data. Trolig drevet av likhet med overordnet term. |
| Esotropi | 99,12 % | Ingen plausibel mekanistisk sammenheng; sannsynlig artefakt i kunnskapsgrafen. |
| Pseudoallergi | 99,12 % | Overlapper med anafylaksi; kun teoretisk mastcellemodulering med blandede adenosineffekter. |

---

## Klinisk studieevidens

Foreløpig er ingen relaterte kliniske studier registrert.

---

## Litteraturevidens

Foreløpig er ingen relatert litteratur tilgjengelig.

---

## Markedsinformasjon for Norge

| Tillatelsesnummer | Produktnavn | Doseringsform | Godkjent indikasjon |
|---------|------|------|-----------|
| EMEA/H/C/001176 | Rapiscan (GE Healthcare AS) | Ikke oppgitt | Myokardperfusjonsavbildning |

Tillatelsen er avregistrert, og det finnes ingen gyldige tillatelser.

---

## Sikkerhetsvurderinger

- **Kontraindikasjoner fra kunnskapsgrafen (ikke fra preparatomtale):** Kunnskapsgrafen (PrimeKG) knytter legemidlet til blant annet hypertensjon, epilepsi, kronisk obstruktiv lungesykdom, astma, aortastenose, hypotensjon, atrioventrikulært blokk, sick sinus-syndrom, transitorisk iskemisk anfall, vertebrobasilær insuffisiens, perikarditt, mitralstenose, koronarsykdom, perikardeffusjon, karotisstenose og karotistrombose. Disse bør verifiseres mot preparatomtalen.
- **Legemiddelinteraksjoner (moderat alvorlighetsgrad):** Koffein, dipyridamol, dyfyllin, teofyllin, aminofyllin og oksytrifyllin. Metylxantiner er adenosinreseptorantagonister og kan dempe effekten av regadenoson, mens dipyridamol kan forsterke adenosinvirkninger.
- **Reseptorfarmakologi:** Regadenoson binder A1, A2A, A2B og A3. Ikke-selektiv aktivering kan forklare bivirkninger og gjør effekten på mastceller usikker.
- **Spesielt for anafylaksi:** Blodtrykksfall og vasodilatasjon kan være uheldig hos pasienter med anafylaktisk sirkulasjonssvikt.

---

## Konklusjon og neste steg

**Beslutning: Hold**

**Begrunnelse:**
Prediksjonen er kun beregningsbasert (evidensnivå L5) uten kliniske studier eller litteratur. Mekanismen er tvetydig, siden A2A kan dempe, mens A2B/A3 kan fremme mastcelleaktivering, og de hemodynamiske virkningene kan være skadelige ved anafylaksi. Legemidlet har dessuten ingen gyldig markedsføringstillatelse i Norge.

**For å gå videre kreves:**
- Preparatomtale med advarsler og kontraindikasjoner (kritisk mangel som blokkerer sikkerhetsscreening)
- Detaljerte data om virkningsmekanisme (f.eks. via DrugBank)
- Prekliniske data på regadenosons effekt på mastceller og i anafylaksemodeller
- Vurdering av administrasjonsvei og klinisk gjennomførbarhet, siden legemidlet gis intravenøst som diagnostisk middel
- Avklaring av regulatorisk status, siden den eneste tillatelsen er avregistrert
## Ansvarsfraskrivelse

Dette innholdet er kun til forskningsformål og utgjør ikke medisinsk rådgivning.
Klinisk validering kreves før enhver klinisk anvendelse.

---

