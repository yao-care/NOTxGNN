---
layout: default
title: Ezetimibe
parent: Kun modellprediksjon (L5)
nav_order: 170
evidence_level: L5
indication_count: 1
monitor_inn: "EZETIMIBE"
predicted_indications: ["cholesterol-ester transfer protein deficiency"]
last_modified_at: 2026-11-20
description: "Ezetimibe: predikert ny indikasjon kolesterolester-transferproteinmangel (cholesterol-ester transfer protein deficiency) (evidensnivå L5)"
---

# Ezetimibe
{: .fs-9 }

Evidensnivå: **L5** | Predikerte indikasjoner: **1** stk.
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

## Ezetimib: kolesterolester-transferproteinmangel (cholesterol-ester transfer protein deficiency)
{: .text-alpha }

## Oppsummering i én setning

Ezetimib er et kolesterolsenkende legemiddel som opprinnelig brukes ved hyperkolesterolemi og dyslipidemi. TxGNN-modellen forutsier at det kan være nyttig ved **kolesterolester-transferproteinmangel (CETP-mangel)**, men det finnes **ingen kliniske studier** og **ingen publikasjoner som direkte studerer denne sykdommen**. Prediksjonen bygger derfor kun på modellen.

## Hurtigoversikt

| Punkt | Innhold |
|------|------|
| Opprinnelig indikasjon | Hyperkolesterolemi og dyslipidemi |
| Predikert ny indikasjon | Kolesterolester-transferproteinmangel |
| TxGNN-prediksjonsscore | 0,9909 |
| Evidensnivå | L5 |
| Markedsstatus i Norge | Markedsført (gyldige tillatelser: 1 av 1) |
| Antall godkjenninger | 1 (gyldige: 1) |
| Anbefalt beslutning | Hold |

## Hvorfor er denne prediksjonen rimelig?

Ifølge avsnittet «Mechanism of Action» i preparatomtalen som er godkjent av amerikanske FDA (Prescribing Information), for Ezetimibe (uoffisiell oversettelse): «Ezetimib reduserer kolesterol i blodet ved å hemme absorpsjonen av kolesterol i tynntarmen. Det molekylære målet for ezetimib har vist seg å være steroltransportøren Niemann-Pick C1-Like 1 (NPC1L1), som er involvert i intestinalt opptak av kolesterol og fytosteroler.» Engelsk originaltekst: "Ezetimibe reduces blood cholesterol by inhibiting the absorption of cholesterol by the small intestine. The molecular target of ezetimibe has been shown to be the sterol transporter, Niemann-Pick C1-Like 1 (NPC1L1), which is involved in the intestinal uptake of cholesterol and phytosterols." ([DailyMed: ezetimibe prescribing information, A-S Medication Solutions](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=c37c695b-fb40-423c-9b73-d1aa58a34db9), versjon av 2026-10-08; hentet 2026-11-19). Ezetimib er kjent for å hemme NPC1L1-mediert opptak av kolesterol i tarmen og dermed senke LDL-kolesterol. Denne mekanismen er ikke bekreftet av de innsamlede dataene.

CETP-mangel er en genetisk tilstand som gir forhøyet HDL-kolesterol og redusert LDL-kolesterol gjennom svekket overføring av kolesterolestere. De to tilstandene ligger langs samme akse i lipidmetabolismen, men koblingen er indirekte. CETP-mangel er stort sett godartet og er ikke en anerkjent sykdom som krever behandling. Den høye scoren (0,9909) kommer fra TxGNN-modellen (dyp læring) og kan gjenspeile likheter modellen har lært mellom beslektede sykdommer, ikke biologisk evidens.

## Klinisk studiedokumentasjon

Foreløpig er det ingen relaterte kliniske studier registrert.

## Litteraturevidens

| PMID | År | Type | Tidsskrift | Hovedfunn |
|------|-----|------|------|---------|
| [40911366](https://pubmed.ncbi.nlm.nih.gov/40911366/) | 2025 | Oversiktsartikkel | European Heart Journal | Gjennomgang av mål for lipidsenkende behandling, fra molekylære mekanismer til klinisk bruk. Omhandler ikke CETP-mangel spesifikt. |
| [31779098](https://pubmed.ncbi.nlm.nih.gov/31779098/) | 2019 | Dyrestudie | International Journal of Molecular Sciences | Hamstermodell med Ldlr-mangel for å evaluere PCSK9-antistoff ved hyperlipidemi og aterosklerose. Ikke studert med ezetimib ved CETP-mangel. |

Ingen av publikasjonene studerer ezetimib ved CETP-mangel direkte.

## Informasjon om det norske markedet

| Godkjenningsnummer | Produktnavn | Doseringsform | Godkjent indikasjon |
|---------|------|------|-----------|
| EMEA/H/C/004959 | Nustendi | – | Hyperkolesterolemi, dyslipidemi |

Merk: Nustendi er godkjent som sentral europeisk godkjenning, og denne oppføringen er den eneste i datagrunnlaget.

## Sikkerhetsvurderinger

- **Kontraindikasjoner registrert i kunnskapsgrafen (ikke fra preparatomtale):** pankreatitt, leversykdom, galleblæresykdom, myopati, muskelsykdom, skjelettmuskelsykdom, familiær periodisk paralyse, rusmiddelmisbruk/avhengighet, rabdomyolyse og nodulær fasciitt.
- **Legemiddelinteraksjoner:** 100 interaksjoner er registrert totalt. De som er klassifisert som moderate:
  - Chenodeoksykolsyre
  - Eluxadolin
  - Rosuvastatin
  - Simvastatin

  Flere andre (bl.a. kalsitriol, pantoprazol, glimepirid, metformin, omeprazol og morfin) har ukjent alvorlighetsgrad.

Se preparatomtalen for fullstendig sikkerhetsinformasjon.

## Konklusjon og neste steg

**Beslutning: Hold**

**Begrunnelse:**
Prediksjonen bygger kun på TxGNN-modellen (dyp læring) (evidensnivå L5). Det finnes ingen kliniske studier eller litteratur som direkte studerer ezetimib ved CETP-mangel, og tilstanden er i hovedsak godartet og trenger vanligvis ikke behandling. Den høye scoren kan gjenspeile likheter modellen har lært mellom beslektede sykdommer, ikke biologisk evidens.

**For å gå videre kreves følgende:**
- Preparatomtale med advarsler og kontraindikasjoner (mangler i dag og er et blokkerende datagap)
- Data om virkningsmekanisme (MOA) fra DrugBank
- Klinisk og biologisk begrunnelse for at CETP-mangel er en tilstand som bør behandles
- Direkte studier eller mekanistiske data som knytter ezetimib til denne tilstanden

<!-- review:begin log -->

## Kontrollogg

Nedenfor er gjennomgangsloggen for denne siden. Setningen om at data om virkningsmekanismen ikke var tilgjengelige, er erstattet med et utdrag fra den oppgitte offisielle preparatomtalen (med uoffisiell oversettelse); modellprediksjoner, evidensnivåer og konklusjoner er ikke omskrevet.

| Kontrolldato | Punkt | Tiltak | Kilde |
|------|------|------|------|
| 2026-11-19 | Setningen «data om virkningsmekanismen er ikke tilgjengelige» erstattet med utdrag fra amerikansk preparatomtale | Setning om manglende data om virkningsmekanismen erstattet med et utdrag med kilde | [DailyMed: ezetimibe prescribing information, A-S Medication Solutions](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=c37c695b-fb40-423c-9b73-d1aa58a34db9) |

<!-- review:end log -->

## Ansvarsfraskrivelse

Dette innholdet er kun til forskningsformål og utgjør ikke medisinsk rådgivning.
Klinisk validering kreves før enhver klinisk anvendelse.

---

