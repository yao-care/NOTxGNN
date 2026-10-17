---
layout: default
title: Ipilimumab
parent: Kun modellprediksjon (L5)
nav_order: 223
evidence_level: L5
indication_count: 2
last_modified_at: 2026-10-15
description: "Ipilimumab: predikert ny indikasjon Choroideremi (evidensnivå L5). Opprinnelig indikasjon: Melanom, nyrecellekarsinom, ikke-småcellet lungekreft…"
monitor_inn: "IPILIMUMAB"
predicted_indications: ["choroideremia"]
---

# Ipilimumab
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

# Ipilimumab: Fra melanom til choroideremi

## Oppsummering

Ipilimumab er et antistoff mot CTLA-4 som brukes i kreftbehandling, blant annet ved melanom, nyrecellekarsinom, ikke-småcellet lungekreft, malignt mesoteliom og kolorektal kreft. TxGNN-modellen forutsier at det kan ha effekt ved **choroideremi**, en arvelig netthinnesykdom, med en svært høy modellscore. Det finnes imidlertid **ingen kliniske studier og ingen publikasjoner** som støtter denne prediksjonen, så den er foreløpig rent modellbasert.

---

## Hurtigoversikt

| Punkt | Innhold |
|------|------|
| Opprinnelig indikasjon | Melanom, nyrecellekarsinom, ikke-småcellet lungekreft, malignt mesoteliom, kolorektal kreft |
| Predikert ny indikasjon | Choroideremi |
| TxGNN-prediksjonsscore | 99,06 % |
| Evidensnivå | L5 |
| Markedsstatus i Norge | Kun avregistrerte (trukket) tillatelser |
| Antall tillatelser | 1 (0 gyldige, 1 avregistrert) |
| Anbefalt beslutning | Hold (avvent) |

---

## Hvorfor er denne prediksjonen (ikke) rimelig?

Ipilimumab er et antistoff som blokkerer CTLA-4. Dermed fjernes bremsen på T-cellene, og kroppens immunforsvar kan angripe kreftceller kraftigere. Mekanismen er godt etablert ved melanom.

Choroideremi er en X-bundet arvelig netthinnedegenerasjon som skyldes tap av funksjon i genet *CHM* (REP1). Sykdommen drives verken av immunsystemet eller av tumorbiologi. Vi ser derfor ingen plausibel mekanistisk forbindelse mellom ipilimumabs virkning og sykdomsårsaken. Den høye TxGNN-scoren (0,99) ser ut til å være en artefakt i modellen uten biologisk støtte.

Ipilimumab kan dessuten gi immunrelaterte bivirkninger, blant annet uveitt (øyebetennelse). Hos pasienter med en netthinne som allerede degenererer, kan dette forverre tilstanden.

---

## Evidens fra kliniske studier

Foreløpig er det ikke registrert noen relaterte kliniske studier av ipilimumab ved choroideremi.

---

## Litteraturevidens

Foreløpig finnes det ingen relatert litteratur om ipilimumab ved choroideremi.

---

## Markedsinformasjon for Norge

| Tillatelsesnummer | Produktnavn | Legemiddelform | Godkjent indikasjon |
|---------|------|------|-----------|
| EMEA/H/C/002213 (avregistrert) | Yervoy (Bristol-Myers Squibb Pharma EEIG) | – | Melanom, nyrecellekarsinom, ikke-småcellet lungekreft, malignt mesoteliom, kolorektal kreft |

---

## Cytotoksisitet

| Punkt | Innhold |
|------|------|
| Cytotoksisitetsklassifisering | Immunterapi (immunsjekkpunkthemmer, anti-CTLA-4), ikke et klassisk cytotoksisk middel |
| Risiko for myelosuppresjon | Lav som direkte effekt. Immunrelaterte blodforandringer kan forekomme |
| Emetogenisitet | Lav |
| Overvåkingspunkter | Blodstatus, lever- og nyrefunksjon, skjoldbruskkjertel- og binyrefunksjon, samt tegn på immunrelaterte bivirkninger (hud, tarm, lever, øyne) |
| Håndteringsbeskyttelse | Se preparatomtalen og lokale retningslinjer for håndtering av kreftlegemidler |

---

## Sikkerhetsmomenter

- **Immunrelaterte bivirkninger:** Ipilimumab kan gi immunrelaterte bivirkninger, blant annet uveitt. Dette er særlig bekymringsfullt ved en netthinnesykdom som choroideremi.
- **Legemiddelinteraksjoner:** Det er registrert 100 interaksjoner. Et utvalg:
  - **Alvorlig (Major):** Antikoagulantia og trombinhemmere, blant annet apiksaban, betriksaban, bivalirudin, dalteparin, desirudin, edoksaban, argatroban og danaparoid.
  - **Moderat:** Kortikosteroider (hydrokortison, triamcinolon, deksametason, betametason, budesonid, prednisolon, prednison), metronidazol, tinidazol, naltrekson, rosuvastatin og simvastatin.

---

## Konklusjon og neste steg

**Beslutning: Hold (avvent)**

**Begrunnelse:**
Prediksjonen bygger kun på modellscore, uten kliniske studier, litteratur eller biologisk forklaring. Sykdommen er ikke immun- eller tumordrevet, og de immunrelaterte bivirkningene (som uveitt) kan skade netthinnen ytterligere. Ipilimumabs tillatelse i Norge er dessuten avregistrert.

**For å gå videre kreves følgende:**
- Prekliniske data eller mekanistiske studier som kan vise en biologisk kobling mellom CTLA-4-blokkade og choroideremi
- Vurdering av netthinnesikkerhet, særlig risiko for uveitt
- Detaljerte data om virkningsmekanisme og preparatomtale (advarsler og kontraindikasjoner)

**Merknad:** For en annen prediksjon i samme analyse, **ikke-kutant melanom** (som uveale og mukosale melanomer), er evidensen bedre. Der finnes fase 2-studier av nivolumab pluss ipilimumab ved uvealt melanom (NCT02626962, n=52). Det er imidlertid en subtypeutvidelse av en eksisterende indikasjon og ikke en reell repurposing. Den kan vurderes separat, med forbehold om subtypespesifikk effekt og overvåking av immunrelaterte bivirkninger.
## Ansvarsfraskrivelse

Dette innholdet er kun til forskningsformål og utgjør ikke medisinsk rådgivning.
Klinisk validering kreves før enhver klinisk anvendelse.

---

