---
layout: default
title: Empagliflozin
parent: Kun modellprediksjon (L5)
nav_order: 148
evidence_level: L5
indication_count: 3
last_modified_at: 2026-11-24
description: "Empagliflozin: predikert ny indikasjon Fokalt stiff-limb-syndrom (focal stiff limb syndrome) (evidensnivå L5). Opprinnelig indikasjon: Diabetes mellitus type 2"
monitor_inn: "EMPAGLIFLOZIN"
predicted_indications: ["focal stiff limb syndrome", "classic stiff person syndrome", "opsismodysplasia"]
---

# Empagliflozin
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

## Empagliflozin: Fra type 2-diabetes til fokalt stiff-limb-syndrom
{: .text-alpha }

## Oppsummering i én setning

Empagliflozin er en SGLT2-hemmer som opprinnelig brukes til behandling av type 2-diabetes, hjertesvikt og kronisk nyresvikt.
TxGNN-modellen forutsier at legemidlet kan ha effekt ved **fokalt stiff-limb-syndrom** (score 0,9906), men det finnes for tiden **0 kliniske studier** og **0 publikasjoner** som støtter denne retningen. Prediksjonen er kun modellbasert.

---

## Hurtigoversikt

| Punkt | Innhold |
|------|------|
| Opprinnelig indikasjon | Diabetes mellitus type 2; hjertesvikt; kronisk nyresvikt |
| Predikert ny indikasjon | Fokalt stiff-limb-syndrom (focal stiff limb syndrome) |
| TxGNN-prediksjonsscore | 0,9906 |
| Evidensnivå | L5 |
| Markedsstatus i Norge | Markedsført (gyldige tillatelser: 3 av 3) |
| Antall godkjenninger | 3 (gyldige: 3) |
| Antall tillatelser | 3 (alle avregistrert/trukket) |
| Anbefalt beslutning | Hold |

---

## Hvorfor er denne prediksjonen rimelig?

Ifølge avsnittet «Mechanism of Action» i preparatomtalen som er godkjent av amerikanske FDA (Prescribing Information), for Empagliflozin (uoffisiell oversettelse): «Empagliflozin er en hemmer av SGLT2, den dominerende transportøren som er ansvarlig for reabsorpsjon av glukose fra glomerulusfiltratet tilbake til sirkulasjonen. Ved å hemme SGLT2 reduserer empagliflozin renal reabsorpsjon av filtrert glukose og senker nyreterskelen for glukose, og øker dermed glukoseutskillelsen i urinen.» Engelsk originaltekst: "Empagliflozin is an inhibitor of SGLT2, the predominant transporter responsible for reabsorption of glucose from the glomerular filtrate back into the circulation. By inhibiting SGLT2, empagliflozin reduces renal reabsorption of filtered glucose and lowers the renal threshold for glucose, and thereby increases urinary glucose excretion." ([DailyMed: Jardiance (empagliflozin) prescribing information, Boehringer Ingelheim Pharmaceuticals, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=faf3dd6a-9cd0-39c2-0d2e-232cb3f67565), versjon av 2026-11-10; hentet 2026-11-19). Basert på kjent informasjon er empagliflozin en SGLT2-hemmer (natrium-glukose-kotransportør 2) med dokumentert effekt ved type 2-diabetes, hjertesvikt og kronisk nyresvikt.

Fokalt stiff-limb-syndrom tilhører spekteret av «stiff-person»-lidelser, som er autoimmune eller nevrologiske tilstander. Ut fra dataene som er samlet inn for denne rapporten, finnes det ingen etablert mekanistisk kobling mellom SGLT2-hemming og denne sykdommen. Eventuelle hypoteser, for eksempel immunmetabolske eller antiinflammatoriske effekter, er spekulative.

Den høye modellscoren er en beregnet prediksjon uten klinisk støtte. Samme score (0,9906) er gitt til klassisk stiff-person-syndrom, og i tillegg er opsismodysplasi (0,9903) predikert. Heller ikke for disse finnes det kliniske studier eller litteratur:

- **Klassisk stiff-person-syndrom:** SGLT2-hemming har ingen kjent direkte kobling til den GABAerge eller anti-GAD-autoimmune patofysiologien.
- **Opsismodysplasi:** En sjelden genetisk skjelettdysplasi (INPPL1-relatert, påvirker SHIP2 og insulin/PI3K-signalering). En teoretisk kobling via insulinsignalering er tenkelig, men ikke validert.

---

## Klinisk studieevidens

For tiden er det ingen relaterte kliniske studier registrert.

---

## Litteraturevidens

For tiden er det ingen relatert litteratur tilgjengelig.

---

## Markedsinformasjon for Norge

Alle tre tillatelser er gyldige i dag, og legemidlet er markedsført i Norge.

<!-- licenses:begin -->

| Godkjenningsnummer | Preparatnavn (EMA) | Virkestoff(er) (EMA, engelsk) | Terapeutisk område (EMA, engelsk) | Status |
|------|------|------|------|------|
| EMEA/H/C/002677 | Jardiance | empagliflozin | Diabetes Mellitus, Type 2; Heart Failure; Renal Insufficiency, Chronic | Gyldig |
| EMEA/H/C/003770 | Synjardy | empagliflozin; metformin | Diabetes Mellitus, Type 2 | Gyldig |
| EMEA/H/C/003833 | Glyxambi | empagliflozin; linagliptin | Diabetes Mellitus, Type 2 | Gyldig |

Kilde: EMA – Medicines output (sentralt godkjente legemidler til mennesker); preparatnavn, virkestoffer og terapeutisk område er gjengitt i engelsk original. Nasjonale markedsføringstillatelser (DMP) og veterinærpreparater er ikke med i disse dataene.

<!-- licenses:end -->

---

## Sikkerhetsvurderinger

Det foreligger ikke data om advarsler eller kontraindikasjoner fra preparatomtalen. Se preparatomtalen for sikkerhetsinformasjon.

**Legemiddelinteraksjoner:** Interaksjonssøket er gjennomført og fant 100 registrerte interaksjoner (kilde: DDInter). De 20 som er tilgjengelige i dataene, er hovedsakelig av moderat alvorlighetsgrad, og to er svake:

- **Moderat:** fenylefrin, acebutolol, acetazolamid, formoterol, pseudoefedrin, nifedipin, adrenalin, etinylestradiol, hydrokortison, salbutamol, etanol, fosamprenavir, fosinopril, fosfenytoin, fostamatinib, fostemsavir, furosemid, gemifloksacin
- **Svak:** hydrokortison (topikal), alklometason (topikal)

---

## Konklusjon og neste steg

**Beslutning: Hold**

**Begrunnelse:**
Prediksjonen bygger kun på modellscore (evidensnivå L5), uten kliniske studier, litteratur eller en identifiserbar mekanistisk kobling. I tillegg mangler sikkerhetsdata fra preparatomtalen.

**For å gå videre kreves følgende:**
- Data om virkningsmekanisme (MOA) for å kunne vurdere en mulig mekanistisk kobling
- Advarsler og kontraindikasjoner fra preparatomtalen (blokkerende datamangel for sikkerhetsscreening)
- Prekliniske eller mekanistiske studier som støtter en kobling til stiff-person-spekteret
- Avklaring av formuleringer og administrasjonsveier (ikke vurdert ennå)

<!-- review:begin log -->

## Kontrollogg

Nedenfor er gjennomgangsloggen for denne siden. Setningen om at data om virkningsmekanismen ikke var tilgjengelige, er erstattet med et utdrag fra den oppgitte offisielle preparatomtalen (med uoffisiell oversettelse); modellprediksjoner, evidensnivåer og konklusjoner er ikke omskrevet.

| Kontrolldato | Punkt | Tiltak | Kilde |
|------|------|------|------|
| 2026-11-19 | Setningen «data om virkningsmekanismen er ikke tilgjengelige» erstattet med utdrag fra amerikansk preparatomtale | Setning om manglende data om virkningsmekanismen erstattet med et utdrag med kilde | [DailyMed: Jardiance (empagliflozin) prescribing information, Boehringer Ingelheim Pharmaceuticals, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=faf3dd6a-9cd0-39c2-0d2e-232cb3f67565) |

<!-- review:end log -->

## Ansvarsfraskrivelse

Dette innholdet er kun til forskningsformål og utgjør ikke medisinsk rådgivning.
Klinisk validering kreves før enhver klinisk anvendelse.

---

