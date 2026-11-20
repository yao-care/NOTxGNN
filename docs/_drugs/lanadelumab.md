---
layout: default
title: Lanadelumab
parent: Kun modellprediksjon (L5)
nav_order: 231
evidence_level: L5
indication_count: 9
last_modified_at: 2026-11-03
monitor_inn: "LANADELUMAB"
predicted_indications: ["serpinopathy with toxic serpin polymerization", "pancreatitis", "pseudo-von Willebrand disease", "primary release disorder of platelets", "immune-mediated necrotizing myopathy", "Glanzmann thrombasthenia", "antisynthetase syndrome", "focal myositis", "Scott syndrome"]
description: "Lanadelumab: predikert ny indikasjon Serpinopati med toksisk serpinpolymerisering (serpinopathy with toxic serpin polymerization) (evidensnivå L5). Opprinnelig indikasjon: Angioedemas, Hereditary"
---

# Lanadelumab
{: .fs-9 }

Evidensnivå: **L5** | Predikerte indikasjoner: **9** stk.
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

## Lanadelumab: Serpinopati med toksisk serpinpolymerisering (serpinopathy with toxic serpin polymerization)
{: .text-alpha }

## Oppsummering i én setning

Lanadelumab er et monoklonalt antistoff som hemmer plasma-kallikrein. TxGNN-modellen forutsier at det kan ha effekt ved **serpinopati med toksisk serpinpolymerisering (serpinopathy with toxic serpin polymerization)**, men det finnes **ingen kliniske studier og ingen publikasjoner** som støtter denne retningen i dataene som er sammenstilt for denne rapporten. Prediksjonen er derfor kun modellbasert.

## Hurtigoversikt

| Punkt | Innhold |
|------|------|
| Opprinnelig indikasjon | Angioedemas, Hereditary |
| Predikert ny indikasjon | Serpinopati med toksisk serpinpolymerisering (serpinopathy with toxic serpin polymerization) |
| TxGNN-prediksjonsscore | 0.9999 |
| Evidensnivå | L5 |
| Markedsstatus i Norge | Markedsført (gyldige tillatelser: 1 av 1) |
| Antall godkjenninger | 1 (gyldige: 1) |
| Anbefalt beslutning | Hold |

## Hvorfor er denne prediksjonen rimelig?

Ifølge avsnittet «Mechanism of Action» i preparatomtalen som er godkjent av amerikanske FDA (Prescribing Information), for Lanadelumab (uoffisiell oversettelse): «Lanadelumab-flyo er et fullt humant monoklonalt antistoff (IgG1/κ-lettkjede) som binder plasmakallikrein og hemmer dets proteolytiske aktivitet. Plasmakallikrein er en protease som spalter høymolekylært kininogen (HMWK) og danner spaltet HMWK (cHMWK) og bradykinin, en potent vasodilatator som øker vaskulær permeabilitet, noe som resulterer i hevelse og smerte forbundet med HAE.» Engelsk originaltekst: "Lanadelumab-flyo is a fully human monoclonal antibody (IgG1/κ-light chain) that binds plasma kallikrein and inhibits its proteolytic activity. Plasma kallikrein is a protease that cleaves high-molecular-weight-kininogen (HMWK) to generate cleaved HMWK (cHMWK) and bradykinin, a potent vasodilator that increases vascular permeability resulting in swelling and pain associated with HAE." ([DailyMed: Takhzyro (lanadelumab-flyo) prescribing information, Takeda Pharmaceuticals America, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=15f99d8c-efe7-4f7d-aa20-0d0f1e30c6e8), versjon av 2026-09-18; hentet 2026-11-19). Basert på kjent informasjon binder lanadelumab seg til plasma-kallikrein (KLKB1) og hemmer dermed kallikrein-bradykinin-aksen. Det er et antistoff som er godkjent som forebyggende behandling mot anfall av arvelig angioødem hos pasienter fra 12 år.

Koblingen til den predikerte sykdommen er svak. Serpinfamilien omfatter proteaseinhibitorer som er relevante for kallikrein-systemet, men toksisk serpinpolymerisering er en egen mekanisme (gain-of-function) som ikke åpenbart påvirkes av kallikreinhemming. Den høye scoren gjenspeiler trolig nærhet i nettverket til beslektede serpinrelaterte tilstander, ikke en dokumentert terapeutisk sammenheng. Enhver kobling må derfor regnes som spekulativ.

## Kliniske studier

Foreløpig er ingen relaterte kliniske studier registrert.

## Litteraturevidens

Foreløpig finnes ingen relatert litteratur.

## Informasjon om det norske markedet

| Godkjenningsnummer | Produktnavn | Doseringsform | Godkjent indikasjon |
|---------|------|------|-----------|
| EMEA/H/C/004806 | Takhzyro | Ikke angitt | Arvelig angioødem (status: godkjent) |

## Sikkerhetsvurderinger

- **Legemiddelinteraksjoner:** Én farmakologisk relasjon er registrert, med målproteinet kallikrein B1 (KLKB1), som er lanadelumabs terapeutiske mål. Det er ikke angitt noe alvorlighetsnivå.
- **Koagulasjonsanalyser:** Lanadelumab kan påvirke koagulasjonsrelaterte analyser (forlenget aPTT). Dette bør vurderes dersom bruk i tilstander med blødningstendens overveies.

For øvrig sikkerhetsinformasjon, se preparatomtalen.

## Konklusjon og neste steg

**Beslutning: Hold**

**Begrunnelse:**
Prediksjonen bygger kun på en modellscore (0,9999) uten kliniske studier eller publikasjoner som direkte omhandler sykdommen. Den mekanistiske koblingen er spekulativ, og evidensnivået er L5.

**For å gå videre kreves følgende:**
- Detaljerte data om virkningsmekanismen (MOA) og en begrunnet hypotese for hvordan kallikreinhemming kan påvirke toksisk serpinpolymerisering
- Prekliniske data i relevante modeller som kan understøtte hypotesen
- Informasjon fra preparatomtalen om advarsler og kontraindikasjoner
- Vurdering av om det finnes en definert pasientpopulasjon og målbare endepunkter for denne sjeldne tilstanden

<!-- review:begin log -->

## Kontrollogg

Nedenfor er gjennomgangsloggen for denne siden. Setningen om at data om virkningsmekanismen ikke var tilgjengelige, er erstattet med et utdrag fra den oppgitte offisielle preparatomtalen (med uoffisiell oversettelse); modellprediksjoner, evidensnivåer og konklusjoner er ikke omskrevet.

| Kontrolldato | Punkt | Tiltak | Kilde |
|------|------|------|------|
| 2026-11-19 | Setningen «data om virkningsmekanismen er ikke tilgjengelige» erstattet med utdrag fra amerikansk preparatomtale | Setning om manglende data om virkningsmekanismen erstattet med et utdrag med kilde | [DailyMed: Takhzyro (lanadelumab-flyo) prescribing information, Takeda Pharmaceuticals America, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=15f99d8c-efe7-4f7d-aa20-0d0f1e30c6e8) |

<!-- review:end log -->

## Ansvarsfraskrivelse

Dette innholdet er kun til forskningsformål og utgjør ikke medisinsk rådgivning.
Klinisk validering kreves før enhver klinisk anvendelse.

---

