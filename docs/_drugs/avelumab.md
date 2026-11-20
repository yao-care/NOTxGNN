---
layout: default
title: Avelumab
parent: Kun modellprediksjon (L5)
nav_order: 47
evidence_level: L5
indication_count: 9
monitor_inn: "AVELUMAB"
predicted_indications: ["human herpesvirus 8-related tumor", "middle ear neuroendocrine tumor", "malignant cutaneous granular cell skin tumor", "ectomesenchymoma", "adenosine deaminase deficiency", "reticular dysgenesis", "Immunoerythromyeloid hypoplasia", "non-severe combined immunodeficiency", "kidney pelvis sarcomatoid transitional cell carcinoma"]
last_modified_at: 2026-10-28
description: "Avelumab: predikert ny indikasjon Humant herpesvirus 8-relatert svulst (human herpesvirus 8-related tumor) (evidensnivå L5). Opprinnelig indikasjon: Neuroendocrine Tumors"
---

# Avelumab
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

## Avelumab: PD-L1-hemmer (immunsjekkpunkthemmer) → humant herpesvirus 8-relatert svulst (human herpesvirus 8-related tumor)
{: .text-alpha }

## Oppsummering i én setning

Avelumab er et monoklonalt antistoff mot PD-L1. Modellen TxGNN predikerer at legemidlet kan være aktuelt for **humant herpesvirus 8-relatert svulst (human herpesvirus 8-related tumor)**. Per i dag finnes **ingen kliniske studier og ingen publikasjoner** i de samlede dataene som støtter denne prediksjonen direkte.

## Hurtigoversikt

| Punkt | Innhold |
|------|------|
| Opprinnelig indikasjon | Neuroendocrine Tumors |
| Predikert ny indikasjon | Humant herpesvirus 8-relatert svulst (human herpesvirus 8-related tumor) |
| TxGNN-prediksjonsscore | 0,9997 |
| Evidensnivå | L5 |
| Markedsstatus i Norge | Markedsført (gyldige tillatelser: 1 av 1) |
| Antall godkjenninger | 1 (gyldige: 1) |
| Anbefalt beslutning | Hold (avvent) |

## Hvorfor er prediksjonen rimelig?

Avelumab er et anti-PD-L1-antistoff som blokkerer samspillet mellom PD-L1 og PD-1 og dermed kan gjenopprette T-cellenes immunrespons mot svulstceller. Ifølge avsnittet «Mechanism of Action» i preparatomtalen som er godkjent av amerikanske FDA (Prescribing Information), for Avelumab (uoffisiell oversettelse): «PD-L1 kan uttrykkes på tumorceller og tumorinfiltrerende immunceller og kan bidra til hemming av den antitumorale immunresponsen i tumormikromiljøet. Binding av PD-L1 til PD-1- og B7.1-reseptorene på T-celler og antigenpresenterende celler hemmer cytotoksisk T-celleaktivitet, T-celleproliferasjon og cytokinproduksjon. […] Avelumab binder PD-L1 og blokkerer interaksjonen mellom PD-L1 og reseptorene PD-1 og B7.1.» Engelsk originaltekst: "PD-L1 may be expressed on tumor cells and tumor-infiltrating immune cells and can contribute to the inhibition of the anti-tumor immune response in the tumor microenvironment. Binding of PD-L1 to the PD-1 and B7.1 receptors found on T cells and antigen presenting cells suppresses cytotoxic T-cell activity, T-cell proliferation, and cytokine production. […] Avelumab binds PD-L1 and blocks the interaction between PD-L1 and its receptors PD-1 and B7.1." ([DailyMed: Bavencio (avelumab) prescribing information, EMD Serono, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=5cd725a1-2fa4-408a-a651-57a7b84b2118), versjon av 2026-09-22; hentet 2026-11-19).

HHV-8-relaterte svulster, for eksempel Kaposis sarkom, kjennetegnes av immununnvikelse og uttrykk av PD-L1. Blokkade av immunsjekkpunkter er derfor biologisk plausibelt. Dette er imidlertid en mekanistisk hypotese, ikke et klinisk bevist funn. Scoren er en ren modellprediksjon uten støtte fra studier.

## Klinisk studiedokumentasjon

Foreløpig er det ingen relaterte kliniske studier registrert.

## Litteraturdokumentasjon

Foreløpig finnes ingen relatert litteratur.

## Informasjon om det norske markedet

| Godkjenningsnummer | Produktnavn | Doseringsform | Godkjent indikasjon |
|---------|------|------|-----------|
| EMEA/H/C/004338 | Bavencio | Ikke oppgitt | Se lokale lisensdata |

## Sikkerhetsvurderinger

**Legemiddelinteraksjoner** (alle klassifisert som «Major»):
- Lenalidomid
- Pomalidomid
- Talidomid

For øvrig sikkerhetsinformasjon, se preparatomtalen (SPC/pakningsvedlegg).

## Konklusjon og neste steg

**Beslutning: Hold (avvent)**

**Begrunnelse:**
Prediksjonen bygger kun på en modellscore (evidensnivå L5) uten kliniske studier eller publikasjoner for denne sykdommen. Den biologiske begrunnelsen via PD-L1 er plausibel, men ubekreftet.

**For å gå videre kreves følgende:**
- Systematisk litteratursøk og søk i studieregistre etter avelumab ved HHV-8-relaterte svulster (f.eks. Kaposis sarkom)
- Data om virkningsmekanisme (MOA) og PD-L1-uttrykk i aktuelle svulster
- Gjennomgang av preparatomtalens advarsler og kontraindikasjoner
- Vurdering av sikkerhet hos pasienter med HIV-assosiert immunsvikt, som er relevant for denne svulsttypen

<!-- review:begin log -->

## Kontrollogg

Nedenfor er gjennomgangsloggen for denne siden. Setningen om at data om virkningsmekanismen ikke var tilgjengelige, er erstattet med et utdrag fra den oppgitte offisielle preparatomtalen (med uoffisiell oversettelse); modellprediksjoner, evidensnivåer og konklusjoner er ikke omskrevet.

| Kontrolldato | Punkt | Tiltak | Kilde |
|------|------|------|------|
| 2026-11-19 | Setningen «data om virkningsmekanismen er ikke tilgjengelige» erstattet med utdrag fra amerikansk preparatomtale | Setning om manglende data om virkningsmekanismen erstattet med et utdrag med kilde | [DailyMed: Bavencio (avelumab) prescribing information, EMD Serono, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=5cd725a1-2fa4-408a-a651-57a7b84b2118) |

<!-- review:end log -->

## Ansvarsfraskrivelse

Dette innholdet er kun til forskningsformål og utgjør ikke medisinsk rådgivning.
Klinisk validering kreves før enhver klinisk anvendelse.

---

