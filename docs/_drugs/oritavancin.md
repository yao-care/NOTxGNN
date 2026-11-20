---
layout: default
title: Oritavancin
parent: Kun modellprediksjon (L5)
nav_order: 299
evidence_level: L5
indication_count: 3
last_modified_at: 2026-11-20
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

<div id="pharmacist" markdown="1">

## Farmasøytens vurderingsrapport

</div>

## Oritavancin: Fra bakterielle hud- og bløtdelsinfeksjoner til Bacteroidaceae-infeksjon
{: .text-alpha }

## Sammendrag i én setning

Oritavancin er et lipoglykopeptid-antibiotikum som opprinnelig brukes mot bakterielle hud- og bløtdelsinfeksjoner.
TxGNN-modellen predikerer at det kan være effektivt mot **Bacteroidaceae-infeksjon**, men det finnes foreløpig **ingen kliniske studier** og **ingen publikasjoner** i de innsamlede dataene som støtter denne retningen. Prediksjonen er mekanistisk lite plausibel og bør betraktes som et rent modellresultat.

---

## Hurtigoversikt

| Punkt | Innhold |
|------|------|
| Opprinnelig indikasjon | Bløtvevsinfeksjoner; bakterielle hudsykdommer |
| Predikert ny indikasjon | Bacteroidaceae-infeksjon |
| TxGNN-prediksjonsscore | 0,9948 |
| Evidensnivå | L5 |
| Markedsstatus i Norge | Markedsført (gyldige tillatelser: 1 av 1) |
| Antall godkjenninger | 1 (gyldige: 1) |
| Antall tillatelser | 1 |
| Anbefalt beslutning | Hold |

---

## Hvorfor er denne prediksjonen (ikke) rimelig?

Ifølge avsnittene «Mechanism of Action» og «Microbiology» i preparatomtalen som er godkjent av amerikanske FDA (Prescribing Information), for Oritavancin (uoffisiell oversettelse): «Oritavancin er et antibakterielt legemiddel. […] Oritavancin har tre virkningsmekanismer: (i) hemming av transglykosyleringstrinnet (polymeriseringstrinnet) i cellevegg-biosyntesen ved binding til stammepeptidet i peptidoglykanforløpere; (ii) hemming av transpeptideringstrinnet (kryssbindingstrinnet) i cellevegg-biosyntesen ved binding til de peptidbroende segmentene i celleveggen; og (iii) forstyrrelse av integriteten til bakteriemembranen, noe som fører til depolarisering, permeabilisering og celledød. Disse ulike mekanismene bidrar til den konsentrasjonsavhengige baktericide aktiviteten til oritavancin.» Engelsk originaltekst: "Oritavancin is an antibacterial drug. […] Oritavancin has three mechanisms of action: (i) inhibition of the transglycosylation (polymerization) step of cell wall biosynthesis by binding to the stem peptide of peptidoglycan precursors; (ii) inhibition of the transpeptidation (crosslinking) step of cell wall biosynthesis by binding to the peptide bridging segments of the cell wall; and (iii) disruption of bacterial membrane integrity, leading to depolarization, permeabilization, and cell death. These multiple mechanisms contribute to the concentration-dependent bactericidal activity of oritavancin." ([DailyMed: Orbactiv (oritavancin) prescribing information, Melinta Therapeutics, LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=ff09a726-9f9b-4e30-b509-396781293220), versjon av 2026-09-15; hentet 2026-11-19). Basert på kjent farmakologi er oritavancin et lipoglykopeptid som hemmer celleveggsyntesen hos grampositive bakterier ved å binde D-Ala-D-Ala (og D-Ala-D-Lac) i peptidoglykanforløpere, og i tillegg forstyrrer membranintegriteten.

Bacteroidaceae (for eksempel *Bacteroides*-arter) er gramnegative anaerobe bakterier med en ytre membran som glykopeptider vanligvis ikke trenger gjennom. Den høye TxGNN-scoren (0,9948) har derfor ikke noen plausibel mekanistisk støtte. Scoren kommer fra TxGNN-modellen (deep learning) og kan gjenspeile likheter modellen har lært mellom beslektede sykdommer, ikke biologisk evidens.

Til sammenligning er også de to neste predikerte indikasjonene mekanistisk problematiske:
- **Oftalmisk herpes zoster** (score 0,9903): Forårsakes av et DNA-virus, og oritavancin har ingen kjent antiviral virkning.
- **Mycoplasma pneumoniae-pneumoni** (score 0,9901): *Mycoplasma* mangler cellevegg, så celleveggshemmere som oritavancin er iboende uvirksomme.

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

Legemidlet er markedsført i Norge, og 1 av 1 markedsføringstillatelser er gyldig.

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
Prediksjonen har kun modellstøtte (L5) uten kliniske studier eller litteratur, og virkningsmekanismen taler imot aktivitet mot gramnegative anaerober som Bacteroidaceae. Produktet er markedsført i Norge med 1 gyldig markedsføringstillatelse av 1.

**For å gå videre kreves følgende:**
- Preparatomtale med advarsler og kontraindikasjoner fra DMP for sikkerhetsscreening
- Detaljerte data om virkningsmekanisme (MOA)
- *In vitro*-data på følsomhet hos *Bacteroides*-arter (MIC-verdier) for å vurdere om det finnes noen reell aktivitet
- Avklaring av markedsstatus og tilgjengelige administrasjonsveier i Norge

<!-- review:begin log -->

## Kontrollogg

Nedenfor er gjennomgangsloggen for denne siden. Setningen om at data om virkningsmekanismen ikke var tilgjengelige, er erstattet med et utdrag fra den oppgitte offisielle preparatomtalen (med uoffisiell oversettelse); modellprediksjoner, evidensnivåer og konklusjoner er ikke omskrevet.

| Kontrolldato | Punkt | Tiltak | Kilde |
|------|------|------|------|
| 2026-11-19 | Setningen «data om virkningsmekanismen er ikke tilgjengelige» erstattet med utdrag fra amerikansk preparatomtale | Setning om manglende data om virkningsmekanismen erstattet med et utdrag med kilde | [DailyMed: Orbactiv (oritavancin) prescribing information, Melinta Therapeutics, LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=ff09a726-9f9b-4e30-b509-396781293220) |

<!-- review:end log -->

## Ansvarsfraskrivelse

Dette innholdet er kun til forskningsformål og utgjør ikke medisinsk rådgivning.
Klinisk validering kreves før enhver klinisk anvendelse.

---

