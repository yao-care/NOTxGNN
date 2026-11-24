---
layout: default
title: Sacituzumab Govitecan
parent: Kun modellprediksjon (L5)
nav_order: 373
evidence_level: L5
indication_count: 4
last_modified_at: 2026-11-24
description: "Sacituzumab Govitecan: predikert ny indikasjon Legemiddelindusert osteoporose (evidensnivå L5). Opprinnelig indikasjon: Brystkreft"
monitor_inn: "SACITUZUMAB GOVITECAN"
predicted_indications: ["drug-induced osteoporosis", "severe nonproliferative diabetic retinopathy", "diabetic retinopathy", "diabetic cataract"]
---

# Sacituzumab Govitecan
{: .fs-9 }

Evidensnivå: **L5** | Predikerte indikasjoner: **4** stk.
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

## Sacituzumab govitecan: Fra brystkreft til legemiddelindusert osteoporose
{: .text-alpha }

## Oppsummering

Sacituzumab govitecan er et antistoff-legemiddelkonjugat (Trop-2-rettet antistoff koblet til topoisomerase I-hemmeren SN-38), opprinnelig brukt til behandling av brystkreft, inkludert trippelnegativ brystkreft.
TxGNN-modellen predikerer at det kan være effektivt mot **legemiddelindusert osteoporose**, men det finnes **0 kliniske studier** og **0 publikasjoner** som støtter denne retningen. Prediksjonen er kun modellbasert.

---

## Hurtigoversikt

| Punkt | Innhold |
|------|------|
| Opprinnelig indikasjon | Brystkreft; trippelnegativ brystkreft |
| Predikert ny indikasjon | Legemiddelindusert osteoporose |
| TxGNN-prediksjonsscore | 0,9978 |
| Evidensnivå | L5 |
| Markedsstatus i Norge | Markedsført (gyldige tillatelser: 1 av 1) |
| Antall godkjenninger | 1 (gyldige: 1) |
| Anbefalt beslutning | Hold (avvent) |

---

## Hvorfor er denne prediksjonen (ikke) rimelig?

Ifølge avsnittet «Mechanism of Action» i preparatomtalen som er godkjent av amerikanske FDA (Prescribing Information), for Sacituzumab Govitecan (uoffisiell oversettelse): «Sacituzumab govitekan-hziy er et Trop-2-rettet antistoff-legemiddelkonjugat. Sacituzumab er et humanisert antistoff som gjenkjenner Trop-2. Småmolekylet SN-38 er en topoisomerase I-hemmer, som er kovalent bundet til antistoffet via en linker.» Engelsk originaltekst: "Sacituzumab govitecan-hziy is a Trop-2-directed antibody-drug conjugate. Sacituzumab is a humanized antibody that recognizes Trop-2. The small molecule, SN-38, is a topoisomerase I inhibitor, which is covalently attached to the antibody by a linker." ([DailyMed: Trodelvy (sacituzumab govitecan) prescribing information, Gilead Sciences, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=57a597d2-03f0-472e-b148-016d7169169d), versjon av 2026-06-24; hentet 2026-11-19). Det er kjent at sacituzumab govitecan er et Trop-2-rettet antistoff-legemiddelkonjugat med SN-38 som cytotoksisk last, og at effekten ved trippelnegativ brystkreft er etablert.

Datagrunnlaget gir ingen støtte for en mekanistisk kobling til benmetabolisme. Den høye TxGNN-scoren (0,9978) er en ren grafbasert prediksjon. Cytotoksiske legemidler er generelt oftere forbundet med benmargstoksisitet enn med beskyttende effekt på skjelettet. Det er heller ingen likhet mellom den opprinnelige indikasjonen (kreft) og den predikerte indikasjonen (osteoporose) som kan forklare prediksjonen.

### Andre predikerte indikasjoner (alle uten støtte)

| Rangering | Predikert indikasjon | TxGNN-score | Evidensnivå | Anbefaling |
|------|------|------|------|------|
| 2 | Alvorlig ikke-proliferativ diabetisk retinopati | 0,9969 | L5 | Hold |
| 3 | Diabetisk retinopati | 0,9960 | L5 | Hold |
| 4 | Diabetisk katarakt | 0,9912 | L5 | Hold |

Disse prediksjonene mangler både kliniske studier og litteratur. Scorene kommer fra TxGNN-modellen (deep learning) og kan gjenspeile likheter modellen har lært mellom beslektede sykdommer, ikke biologisk evidens. Systemisk cytotoksisk behandling er ikke en rimelig kandidat for disse tilstandene uten en tydelig mekanistisk begrunnelse, og tryggere godkjente alternativer finnes (f.eks. anti-VEGF, laser, fenofibrat for retinopati; kirurgi for katarakt).

---

## Klinisk studieevidens

Foreløpig ingen relaterte kliniske studier registrert.

---

## Litteraturevidens

Foreløpig ingen relatert litteratur tilgjengelig.

---

## Informasjon om det norske markedet

<!-- licenses:begin -->

| Godkjenningsnummer | Preparatnavn (EMA) | Virkestoff(er) (EMA, engelsk) | Terapeutisk område (EMA, engelsk) | Status |
|------|------|------|------|------|
| EMEA/H/C/005182 | Trodelvy | sacituzumab govitecan | Breast Neoplasms; Triple Negative Breast Neoplasms | Gyldig |

Kilde: EMA – Medicines output (sentralt godkjente legemidler til mennesker); preparatnavn, virkestoffer og terapeutisk område er gjengitt i engelsk original. Nasjonale markedsføringstillatelser (DMP) og veterinærpreparater er ikke med i disse dataene.

<!-- licenses:end -->

Legemidlet er markedsført, og 1 av 1 godkjenning er gyldig.

---

## Cytotoksisitet

| Punkt | Innhold |
|------|------|
| Cytotoksisitetsklassifisering | Antistoff-legemiddelkonjugat med topoisomerase I-hemmer (SN-38) som cytotoksisk last |
| Risiko for myelosuppresjon | Høy (nøytropeni er et kjent og betydelig problem) |
| Emetogenisitet | Se preparatomtalen |
| Overvåkingspunkter | Fullstendig blodtelling med differensialtelling, lever- og nyrefunksjon; observasjon for diaré og overfølsomhetsreaksjoner |
| Håndteringsvern | Følg gjeldende regelverk for håndtering av cytotoksiske legemidler |

---

## Sikkerhetsvurderinger

**Legemiddelinteraksjoner:** Totalt 40 interaksjoner er identifisert. Eksempler på de viktigste (alvorlighetsgrad «Major»):
- Deferipron
- Fostamatinib
- Adalimumab
- Apalutamid
- Certolizumab pegol
- Kladribin
- Dakomitinib
- Irinotekan
- Leflunomid
- Natalizumab
- Nilotinib
- Ozanimod

Moderate interaksjoner omfatter blant annet alefacept, alemtuzumab, anakinra, kanakinumab, dimetylfumarat, lorlatinib, okrelizumab og omacetaksinmepesuccinat.

Mange av disse er immunsuppressive eller myelosuppressive midler, noe som gir risiko for additiv toksisitet.

For advarsler og kontraindikasjoner, se preparatomtalen.

---

## Konklusjon og neste steg

**Beslutning: Hold (avvent)**

**Begrunnelse:**
Prediksjonen er rent modellbasert (L5) uten kliniske studier eller publikasjoner, og det finnes ingen plausibel mekanistisk kobling til legemiddelindusert osteoporose. Legemidlets toksisitetsprofil er dessuten ugunstig for en kronisk, ikke-onkologisk tilstand.

<!-- review:begin no-lic-20261124b-sacituzumab_govitecan-1 -->

> **Kontrollrettelse (2026-11-24)**: Opprinnelig sto det: «Legemidlets toksisitetsprofil er dessuten ugunstig for en kronisk, ikke-onkologisk tilstand, og den norske godkjenningen er kansellert.» Rettet: opplysningen om at godkjenningen(e) er kansellert, er tatt ut fordi den ikke stemte med EMAs data om sentrale EU-godkjenninger (2026-11-12), der godkjenningene står som gyldige (Authorised); resten av setningen er uendret. Oppdaterte antall og statuser for godkjenningene står i hurtigoversikten og i lisenstabellen under markedsinformasjonen. Kilde: [EMA – Medicines output: medicines report](https://www.ema.europa.eu/en/documents/report/medicines-output-medicines-report_en.xlsx); [European Medicines Agency](https://www.ema.europa.eu/).

<!-- review:end no-lic-20261124b-sacituzumab_govitecan-1 -->

**For å gå videre kreves følgende:**
- Data om virkningsmekanisme (MOA), f.eks. fra DrugBank
- Advarsler og kontraindikasjoner fra preparatomtalen (blokkerende datamangel)
- Prekliniske eller mekanistiske studier som kan underbygge en kobling til benmetabolisme
- Avklaring av markedsstatus og tilgjengelighet i Norge

<!-- review:begin log -->

## Kontrollogg

Nedenfor er kontrolloggen for denne siden: opplysninger kontrollert mot EMAs data om sentrale EU-godkjenninger. Rettelser gjelder bare grunnleggende faktaopplysninger; modellens prediksjoner, evidensnivåer og konklusjoner er ikke skrevet om. Setningen om at data om virkningsmekanismen ikke var tilgjengelige, er erstattet med et utdrag fra den oppgitte offisielle preparatomtalen (med uoffisiell oversettelse).

| Kontrolldato | Punkt | Tiltak | Kilde |
|------|------|------|------|
| 2026-11-19 | Setningen «data om virkningsmekanismen er ikke tilgjengelige» erstattet med utdrag fra amerikansk preparatomtale | Setning om manglende data om virkningsmekanismen erstattet med et utdrag med kilde | [DailyMed: Trodelvy (sacituzumab govitecan) prescribing information, Gilead Sciences, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=57a597d2-03f0-472e-b148-016d7169169d) |
| 2026-11-24 | Rettet: «Legemidlets toksisitetsprofil er dessuten ugunstig for en kronisk, ikke-onkologisk tilstand, og den norske godkjenningen er kansellert.» → «Legemidlets toksisitetsprofil er dessuten ugunstig for en kronisk, ikke-onkologisk tilstand.» | Rettet | [EMA – Medicines output: medicines report](https://www.ema.europa.eu/en/documents/report/medicines-output-medicines-report_en.xlsx); [European Medicines Agency](https://www.ema.europa.eu/) |

<!-- review:end log -->

## Ansvarsfraskrivelse

Dette innholdet er kun til forskningsformål og utgjør ikke medisinsk rådgivning.
Klinisk validering kreves før enhver klinisk anvendelse.

---

