---
layout: default
title: Sotatercept
parent: Kun modellprediksjon (L5)
nav_order: 391
evidence_level: L5
indication_count: 10
last_modified_at: 2026-11-24
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

## Sotatercept: Fra pulmonal hypertensjon til akutt lymfatisk leukemi
{: .text-alpha }

## Oppsummering

Sotatercept er et aktivin-reseptor type IIA-Fc-fusjonsprotein som opprinnelig brukes til behandling av **pulmonal hypertensjon**.
TxGNN-modellen predikerer at legemidlet kan være effektivt ved **akutt lymfatisk leukemi**, men for øyeblikket finnes **ingen kliniske studier og ingen publikasjoner** i de samlede dataene som støtter denne retningen. Prediksjonen er rent beregningsbasert.

---

## Hurtigoversikt

| Punkt | Innhold |
|------|------|
| Opprinnelig indikasjon | Pulmonal hypertensjon |
| Predikert ny indikasjon | Akutt lymfatisk leukemi |
| TxGNN-prediksjonsscore | 0,9978 |
| Evidensnivå | L5 |
| Markedsstatus i Norge | Markedsført (gyldige tillatelser: 1 av 1) |
| Antall godkjenninger | 1 (gyldige: 1) |
| Anbefalt beslutning | Hold |

---

## Hvorfor er denne prediksjonen rimelig?

Ifølge avsnittet «Mechanism of Action» i preparatomtalen som er godkjent av amerikanske FDA (Prescribing Information), for Sotatercept (uoffisiell oversettelse): «Sotatercept-csrk, et rekombinant aktivinreseptor type IIA-Fc (ActRIIA-Fc)-fusjonsprotein, er en hemmer av aktivinsignalering som binder seg til aktivin A og andre ligander i TGF- β-superfamilien. Som et resultat forbedrer sotatercept-csrk balansen mellom proproliferativ (ActRIIA/Smad2/3-mediert) og antiproliferativ (BMPRII/Smad1/5/8-mediert) signalering for å modulere vaskulær proliferasjon.» Engelsk originaltekst: "Sotatercept-csrk, a recombinant activin receptor type IIA-Fc (ActRIIA-Fc) fusion protein, is an activin signaling inhibitor that binds to activin A and other TGF- β superfamily ligands. As a result, sotatercept-csrk improves the balance between the pro-proliferative (ActRIIA/Smad2/3-mediated) and anti-proliferative (BMPRII/Smad1/5/8-mediated) signaling to modulate vascular proliferation." ([DailyMed: Winrevair (sotatercept-csrk) prescribing information, Merck Sharp & Dohme LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=21693ee2-cd23-4137-ac67-066bb3a4a9b7), versjon av 2026-09-21; hentet 2026-11-19). Ut fra generell kunnskap om legemiddelklassen fungerer sotatercept som en ligandfelle for aktivin og vekstdifferensieringsfaktorer (GDF-er). Dermed gjenoppretter det balansen mellom proliferative og antiproliferative signaler i BMPR-II/aktivin-banen, noe som er grunnlaget for effekten ved pulmonal hypertensjon.

Koblingen til akutt lymfatisk leukemi er foreløpig bare spekulativ. Signalveiene i aktivin/TGF-beta-familien bidrar til reguleringen av bloddannelsen, men det foreligger verken direkte mekanistiske data eller kliniske data som viser en sammenheng. Den høye TxGNN-scoren (0,9978) er utelukkende en beregningsbasert prediksjon og bør ikke tolkes som klinisk støtte.

### Andre predikerte indikasjoner (alle L5, Hold)

Modellen predikerer også følgende indikasjoner, alle uten kliniske studier eller litteratur i de samlede dataene:

| Rangering | Predikert indikasjon | Score | Kort vurdering |
|------|------|------|------|
| 2 | Alvorlig ikke-proliferativ diabetisk retinopati | 0,9977 | Aktivin/TGF-beta kan påvirke retinal kar-remodellering. Sotatercept har blødnings- og telangiektasi-signaler som er bekymringsfulle i øyet. |
| 3 | Diabetisk retinopati | 0,9972 | Samme begrunnelse som over. |
| 4 | Legemiddelindusert osteoporose | 0,9965 | Aktivin A hemmer beindannelse, og hemmere i samme klasse har vist benoppbyggende effekt i dyremodeller. Biologisk plausibelt, men ikke verifisert. |
| 5 | Diabetisk katarakt | 0,9949 | Svak, indirekte kobling via TGF-beta i linseepitel. |
| 6 | HER2-positivt brystkarsinom | 0,9943 | Effekten av aktivin/TGF-beta er kontekstavhengig og kan være både gunstig og skadelig. |
| 7 | Overgangsepitelkarsinom | 0,9939 | Spekulativ kobling via tumormikromiljø og epitelial-mesenkymal transisjon (EMT). |
| 8 | Urotelialt karsinom i prostatisk uretra | 0,9936 | Samme rasjonale. Scoren gjenspeiler trolig likhet med andre uroteliale oppføringer. |
| 9 | Sarkomatoid overgangsepitelkarsinom i nyrebekkenet | 0,9936 | Sjelden subtype med EMT-rasjonale. Evidensgenerering vil være vanskelig. |
| 10 | Infiltrerende sarkomatoid variant av urotelialt blærekarsinom | 0,9934 | Scoren skyldes trolig klynging blant beslektede uroteliale termer. |

---

## Klinisk studieevidens

Det finnes for øyeblikket ingen relaterte kliniske studier registrert.

---

## Litteraturevidens

Det finnes for øyeblikket ingen relatert litteratur tilgjengelig.

---

## Informasjon om det norske markedet

<!-- licenses:begin -->

| Godkjenningsnummer | Preparatnavn (EMA) | Virkestoff(er) (EMA, engelsk) | Terapeutisk område (EMA, engelsk) | Status |
|------|------|------|------|------|
| EMEA/H/C/005647 | Winrevair | sotatercept | Hypertension, Pulmonary | Gyldig |

Kilde: EMA – Medicines output (sentralt godkjente legemidler til mennesker); preparatnavn, virkestoffer og terapeutisk område er gjengitt i engelsk original. Nasjonale markedsføringstillatelser (DMP) og veterinærpreparater er ikke med i disse dataene.

<!-- licenses:end -->

Innehaver er Merck Sharp & Dohme B.V.

<!-- review:begin no-lic-20261124b-sotatercept-1 -->

> **Kontrollrettelse (2026-11-24)**: Opprinnelig sto det: «Merk: Denne registreringen har status **kansellert**.» Fjernet: opplysningen om at godkjenningen(e) er kansellert, stemte ikke med EMAs data om sentrale EU-godkjenninger (2026-11-12), der godkjenningene står som gyldige (Authorised). Oppdaterte antall og statuser for godkjenningene står i hurtigoversikten og i lisenstabellen under markedsinformasjonen. Kilde: [EMA – Medicines output: medicines report](https://www.ema.europa.eu/en/documents/report/medicines-output-medicines-report_en.xlsx); [European Medicines Agency](https://www.ema.europa.eu/).

<!-- review:end no-lic-20261124b-sotatercept-1 -->

---

## Sikkerhetsvurderinger

Ingen data om advarsler, kontraindikasjoner eller legemiddelinteraksjoner er tilgjengelige i de samlede dataene. Se preparatomtalen (pakningsvedlegget) for sikkerhetsinformasjon.

Det kan likevel nevnes at sotatercept i den mekanistiske vurderingen er knyttet til vaskulære sikkerhetssignaler (telangiektasi og blødningshendelser). Dette er særlig relevant om legemidlet skulle vurderes ved øyesykdommer med karpatologi, som diabetisk retinopati.

---

## Konklusjon og neste steg

**Beslutning: Hold**

**Begrunnelse:**
Alle predikerte indikasjoner har evidensnivå L5, det vil si kun modellprediksjon uten kliniske studier eller publikasjoner. I tillegg mangler sikkerhetsdata fra preparatomtalen, noe som blokkerer videre sikkerhetsscreening.

<!-- review:begin no-lic-20261124b-sotatercept-2 -->

> **Kontrollrettelse (2026-11-24)**: Opprinnelig sto det: «I tillegg er den norske registreringen kansellert, og sikkerhetsdata fra preparatomtalen mangler, noe som blokkerer videre sikkerhetsscreening.» Rettet: opplysningen om at godkjenningen(e) er kansellert, er tatt ut fordi den ikke stemte med EMAs data om sentrale EU-godkjenninger (2026-11-12), der godkjenningene står som gyldige (Authorised); resten av setningen er uendret. Oppdaterte antall og statuser for godkjenningene står i hurtigoversikten og i lisenstabellen under markedsinformasjonen. Kilde: [EMA – Medicines output: medicines report](https://www.ema.europa.eu/en/documents/report/medicines-output-medicines-report_en.xlsx); [European Medicines Agency](https://www.ema.europa.eu/).

<!-- review:end no-lic-20261124b-sotatercept-2 -->

**For å gå videre kreves følgende:**
- Hente og analysere preparatomtalen (advarsler og kontraindikasjoner) fra legemiddelmyndighetenes kilde
- Detaljerte data om virkningsmekanisme (MOA), for eksempel via DrugBank
- Systematisk litteratur- og studiesøk for de høyest rangerte indikasjonene
- Prekliniske data som kan underbygge koblingen mellom aktivin/GDF-fangst og den aktuelle sykdommen
- Avklaring av administrasjonsvei og forenlighet for hver ny indikasjon

<!-- review:begin no-lic-20261124b-sotatercept-3 -->

> **Kontrollrettelse (2026-11-24)**: Opprinnelig sto det: «Avklaring av årsaken til og konsekvensene av den kansellerte registreringen i Norge» Fjernet: oppfølgingspunktet bygde på at godkjenningen(e) er kansellert, noe som ikke stemte med EMAs data om sentrale EU-godkjenninger (2026-11-12), der godkjenningene står som gyldige (Authorised). Oppdaterte antall og statuser for godkjenningene står i hurtigoversikten og i lisenstabellen under markedsinformasjonen. Kilde: [EMA – Medicines output: medicines report](https://www.ema.europa.eu/en/documents/report/medicines-output-medicines-report_en.xlsx); [European Medicines Agency](https://www.ema.europa.eu/).

<!-- review:end no-lic-20261124b-sotatercept-3 -->

<!-- review:begin log -->

## Kontrollogg

Nedenfor er kontrolloggen for denne siden: opplysninger kontrollert mot EMAs data om sentrale EU-godkjenninger. Rettelser gjelder bare grunnleggende faktaopplysninger; modellens prediksjoner, evidensnivåer og konklusjoner er ikke skrevet om. Setningen om at data om virkningsmekanismen ikke var tilgjengelige, er erstattet med et utdrag fra den oppgitte offisielle preparatomtalen (med uoffisiell oversettelse).

| Kontrolldato | Punkt | Tiltak | Kilde |
|------|------|------|------|
| 2026-11-19 | Setningen «data om virkningsmekanismen er ikke tilgjengelige» erstattet med utdrag fra amerikansk preparatomtale | Setning om manglende data om virkningsmekanismen erstattet med et utdrag med kilde | [DailyMed: Winrevair (sotatercept-csrk) prescribing information, Merck Sharp & Dohme LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=21693ee2-cd23-4137-ac67-066bb3a4a9b7) |
| 2026-11-24 | Fjernet: «Merk: Denne registreringen har status **kansellert**.» | Rettet | [EMA – Medicines output: medicines report](https://www.ema.europa.eu/en/documents/report/medicines-output-medicines-report_en.xlsx); [European Medicines Agency](https://www.ema.europa.eu/) |
| 2026-11-24 | Rettet: «I tillegg er den norske registreringen kansellert, og sikkerhetsdata fra preparatomtalen mangler, noe som blokkerer videre sikkerhetsscreening.» → «I tillegg mangler sikkerhetsdata fra preparatomtalen, noe som blokkerer videre sikkerhetsscreening.» | Rettet | [EMA – Medicines output: medicines report](https://www.ema.europa.eu/en/documents/report/medicines-output-medicines-report_en.xlsx); [European Medicines Agency](https://www.ema.europa.eu/) |
| 2026-11-24 | Fjernet: «Avklaring av årsaken til og konsekvensene av den kansellerte registreringen i Norge» | Rettet | [EMA – Medicines output: medicines report](https://www.ema.europa.eu/en/documents/report/medicines-output-medicines-report_en.xlsx); [European Medicines Agency](https://www.ema.europa.eu/) |

<!-- review:end log -->

## Ansvarsfraskrivelse

Dette innholdet er kun til forskningsformål og utgjør ikke medisinsk rådgivning.
Klinisk validering kreves før enhver klinisk anvendelse.

---

