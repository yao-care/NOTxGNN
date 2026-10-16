---
layout: default
title: Oritavancin
parent: Kun modellprediksjon (L5)
nav_order: 299
evidence_level: L5
indication_count: 3
last_modified_at: 2026-10-15
description: "Oritavancin: predikert ny indikasjon Bacteroidaceae-infeksjon (evidensnivå L5). Opprinnelig indikasjon: Bløtvevsinfeksjoner"
monitor_inn: "ORITAVANCIN"
predicted_indications: ["Bacteroidaceae infectious disease", "ophthalmic herpes zoster", "Mycoplasma pneumoniae pneumonia"]
---

# Oritavancin
{: .fs-9 }

Evidensnivå: **L5** | Predikerte indikasjoner: **3** stk.
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

# Oritavancin: Fra bakterielle hud- og bløtdelsinfeksjoner til Bacteroidaceae-infeksjon

## Sammendrag i én setning

Oritavancin er et lipoglykopeptid-antibiotikum som opprinnelig brukes mot bakterielle hud- og bløtdelsinfeksjoner.
TxGNN-modellen predikerer at det kan være effektivt mot **Bacteroidaceae-infeksjon**, men det finnes foreløpig **ingen kliniske studier** og **ingen publikasjoner** i de innsamlede dataene som støtter denne retningen. Prediksjonen er mekanistisk lite plausibel og bør betraktes som et rent modellresultat.

---

## Hurtigoversikt

| Punkt | Innhold |
|------|------|
| Opprinnelig indikasjon | Bløtvevsinfeksjoner; bakterielle hudsykdommer |
| Predikert ny indikasjon | Bacteroidaceae-infeksjon |
| TxGNN-prediksjonsscore | 99,48 % |
| Evidensnivå | L5 |
| Markedsstatus i Norge | Kun tilbakekalt/avregistrert (ingen gyldig markedsføringstillatelse) |
| Antall tillatelser | 1 |
| Anbefalt beslutning | Hold |

---

## Hvorfor er denne prediksjonen (ikke) rimelig?

Detaljerte data om virkningsmekanisme er ikke tilgjengelige i de innsamlede dataene. Basert på kjent farmakologi er oritavancin et lipoglykopeptid som hemmer celleveggsyntesen hos grampositive bakterier ved å binde D-Ala-D-Ala (og D-Ala-D-Lac) i peptidoglykanforløpere, og i tillegg forstyrrer membranintegriteten.

Bacteroidaceae (for eksempel *Bacteroides*-arter) er gramnegative anaerobe bakterier med en ytre membran som glykopeptider vanligvis ikke trenger gjennom. Den høye TxGNN-scoren (0,995) har derfor ikke noen plausibel mekanistisk støtte. Prediksjonen gjenspeiler trolig nærhet til andre antibakterielle midler i kunnskapsgrafen snarere enn reell aktivitet.

Til sammenligning er også de to neste predikerte indikasjonene mekanistisk problematiske:
- **Oftalmisk herpes zoster** (score 99,03 %): Forårsakes av et DNA-virus, og oritavancin har ingen kjent antiviral virkning.
- **Mycoplasma pneumoniae-pneumoni** (score 99,01 %): *Mycoplasma* mangler cellevegg, så celleveggshemmere som oritavancin er iboende uvirksomme.

---

## Evidens fra kliniske studier

Foreløpig er ingen relaterte kliniske studier registrert.

---

## Litteraturevidens

Foreløpig er ingen relatert litteratur tilgjengelig.

---

## Informasjon om det norske markedet

| Tillatelsesnummer | Produktnavn | Doseringsform | Godkjent indikasjon |
|---------|------|------|-----------|
| EMEA/H/C/003785 | Tenkasi (tidligere Orbactiv) | Ikke oppgitt | Bløtvevsinfeksjoner; bakterielle hudsykdommer |

Tillatelsen har status «kansellert», og det finnes ingen gyldige tillatelser for enkeltstoffpreparater eller kombinasjoner.

---

## Sikkerhetsvurderinger

- **Legemiddelinteraksjoner**: Det er funnet 38 registrerte interaksjoner. Blant de viktigste:
  - **Alvorlig (Major)**: Heparin
  - **Moderat**: warfarin, tikagrelor, fostamatinib, kobicistat, etinylestradiol, hydrokodon, abemasiklib, acalabrutinib, alpelisib, brigatinib, kabozantinib, krizotinib, pikosulfat, nitisinon, makimorelin, prazikvantel, elagoliks, osilodrostat
  - **Mindre (Minor)**: bortezomib

  Interaksjonene med heparin, warfarin og tikagrelor er særlig relevante fordi de gjelder blødnings- og koagulasjonsforhold.

Se preparatomtalen for øvrig sikkerhetsinformasjon, som advarsler og kontraindikasjoner.

---

## Konklusjon og neste steg

**Beslutning: Hold**

**Begrunnelse:**
Prediksjonen har kun modellstøtte (L5) uten kliniske studier eller litteratur, og virkningsmekanismen taler imot aktivitet mot gramnegative anaerober som Bacteroidaceae. I tillegg har produktet ingen gyldig markedsføringstillatelse i Norge.

**For å gå videre kreves følgende:**
- Preparatomtale med advarsler og kontraindikasjoner fra DMP for sikkerhetsscreening
- Detaljerte data om virkningsmekanisme (MOA)
- *In vitro*-data på følsomhet hos *Bacteroides*-arter (MIC-verdier) for å vurdere om det finnes noen reell aktivitet
- Avklaring av markedsstatus og tilgjengelige administrasjonsveier i Norge
## Ansvarsfraskrivelse

Dette innholdet er kun til forskningsformål og utgjør ikke medisinsk rådgivning.
Klinisk validering kreves før enhver klinisk anvendelse.

---

