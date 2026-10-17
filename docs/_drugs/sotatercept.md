---
layout: default
title: Sotatercept
parent: Kun modellprediksjon (L5)
nav_order: 391
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-15
description: "Sotatercept: predikert ny indikasjon Akutt lymfatisk leukemi (evidensnivå L5). Opprinnelig indikasjon: Pulmonal hypertensjon"
monitor_inn: "SOTATERCEPT"
predicted_indications: ["acute lymphoblastic leukemia (disease)", "severe nonproliferative diabetic retinopathy", "diabetic retinopathy", "drug-induced osteoporosis", "diabetic cataract", "HER2 positive breast carcinoma", "transitional cell carcinoma", "prostatic urethra urothelial carcinoma", "kidney pelvis sarcomatoid transitional cell carcinoma", "infiltrating bladder urothelial carcinoma sarcomatoid variant"]
---

# Sotatercept
{: .fs-9 }

Evidensnivå: **L5** | Predikerte indikasjoner: **10** stk.
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

# Sotatercept: Fra pulmonal hypertensjon til akutt lymfatisk leukemi

## Oppsummering

Sotatercept er et aktivin-reseptor type IIA-Fc-fusjonsprotein som opprinnelig brukes til behandling av **pulmonal hypertensjon**.
TxGNN-modellen predikerer at legemidlet kan være effektivt ved **akutt lymfatisk leukemi**, men for øyeblikket finnes **ingen kliniske studier og ingen publikasjoner** i de samlede dataene som støtter denne retningen. Prediksjonen er rent beregningsbasert.

---

## Hurtigoversikt

| Punkt | Innhold |
|------|------|
| Opprinnelig indikasjon | Pulmonal hypertensjon |
| Predikert ny indikasjon | Akutt lymfatisk leukemi |
| TxGNN-prediksjonsscore | 99,78 % |
| Evidensnivå | L5 |
| Markedsstatus i Norge | Kun kansellerte registreringer |
| Antall godkjenninger | 1 (kansellert) |
| Anbefalt beslutning | Hold |

---

## Hvorfor er denne prediksjonen rimelig?

Detaljerte data om virkningsmekanisme (MOA) er for øyeblikket ikke tilgjengelige fra de innhentede kildene. Ut fra generell kunnskap om legemiddelklassen fungerer sotatercept som en ligandfelle for aktivin og vekstdifferensieringsfaktorer (GDF-er). Dermed gjenoppretter det balansen mellom proliferative og antiproliferative signaler i BMPR-II/aktivin-banen, noe som er grunnlaget for effekten ved pulmonal hypertensjon.

Koblingen til akutt lymfatisk leukemi er foreløpig bare spekulativ. Signalveiene i aktivin/TGF-beta-familien bidrar til reguleringen av bloddannelsen, men det foreligger verken direkte mekanistiske data eller kliniske data som viser en sammenheng. Den høye TxGNN-scoren (0,998) er utelukkende en beregningsbasert prediksjon og bør ikke tolkes som klinisk støtte.

### Andre predikerte indikasjoner (alle L5, Hold)

Modellen predikerer også følgende indikasjoner, alle uten kliniske studier eller litteratur i de samlede dataene:

| Rangering | Predikert indikasjon | Score | Kort vurdering |
|------|------|------|------|
| 2 | Alvorlig ikke-proliferativ diabetisk retinopati | 99,77 % | Aktivin/TGF-beta kan påvirke retinal kar-remodellering. Sotatercept har blødnings- og telangiektasi-signaler som er bekymringsfulle i øyet. |
| 3 | Diabetisk retinopati | 99,72 % | Samme begrunnelse som over. |
| 4 | Legemiddelindusert osteoporose | 99,65 % | Aktivin A hemmer beindannelse, og hemmere i samme klasse har vist benoppbyggende effekt i dyremodeller. Biologisk plausibelt, men ikke verifisert. |
| 5 | Diabetisk katarakt | 99,49 % | Svak, indirekte kobling via TGF-beta i linseepitel. |
| 6 | HER2-positivt brystkarsinom | 99,43 % | Effekten av aktivin/TGF-beta er kontekstavhengig og kan være både gunstig og skadelig. |
| 7 | Overgangsepitelkarsinom | 99,39 % | Spekulativ kobling via tumormikromiljø og epitelial-mesenkymal transisjon (EMT). |
| 8 | Urotelialt karsinom i prostatisk uretra | 99,36 % | Samme rasjonale. Scoren gjenspeiler trolig likhet med andre uroteliale oppføringer. |
| 9 | Sarkomatoid overgangsepitelkarsinom i nyrebekkenet | 99,36 % | Sjelden subtype med EMT-rasjonale. Evidensgenerering vil være vanskelig. |
| 10 | Infiltrerende sarkomatoid variant av urotelialt blærekarsinom | 99,34 % | Scoren skyldes trolig klynging blant beslektede uroteliale termer. |

---

## Klinisk studieevidens

Det finnes for øyeblikket ingen relaterte kliniske studier registrert.

---

## Litteraturevidens

Det finnes for øyeblikket ingen relatert litteratur tilgjengelig.

---

## Informasjon om det norske markedet

| Godkjenningsnummer | Produktnavn | Doseringsform | Godkjent indikasjon |
|---------|------|------|-----------|
| EMEA/H/C/005647 | Winrevair | – | Pulmonal hypertensjon |

Merk: Denne registreringen har status **kansellert**. Innehaver er Merck Sharp & Dohme B.V.

---

## Sikkerhetsvurderinger

Ingen data om advarsler, kontraindikasjoner eller legemiddelinteraksjoner er tilgjengelige i de samlede dataene. Se preparatomtalen (pakningsvedlegget) for sikkerhetsinformasjon.

Det kan likevel nevnes at sotatercept i den mekanistiske vurderingen er knyttet til vaskulære sikkerhetssignaler (telangiektasi og blødningshendelser). Dette er særlig relevant om legemidlet skulle vurderes ved øyesykdommer med karpatologi, som diabetisk retinopati.

---

## Konklusjon og neste steg

**Beslutning: Hold**

**Begrunnelse:**
Alle predikerte indikasjoner har evidensnivå L5, det vil si kun modellprediksjon uten kliniske studier eller publikasjoner. I tillegg er den norske registreringen kansellert, og sikkerhetsdata fra preparatomtalen mangler, noe som blokkerer videre sikkerhetsscreening.

**For å gå videre kreves følgende:**
- Hente og analysere preparatomtalen (advarsler og kontraindikasjoner) fra legemiddelmyndighetenes kilde
- Detaljerte data om virkningsmekanisme (MOA), for eksempel via DrugBank
- Systematisk litteratur- og studiesøk for de høyest rangerte indikasjonene
- Prekliniske data som kan underbygge koblingen mellom aktivin/GDF-fangst og den aktuelle sykdommen
- Avklaring av administrasjonsvei og forenlighet for hver ny indikasjon
- Avklaring av årsaken til og konsekvensene av den kansellerte registreringen i Norge
## Ansvarsfraskrivelse

Dette innholdet er kun til forskningsformål og utgjør ikke medisinsk rådgivning.
Klinisk validering kreves før enhver klinisk anvendelse.

---

