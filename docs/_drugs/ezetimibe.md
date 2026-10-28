---
layout: default
title: Ezetimibe
parent: Kun modellprediksjon (L5)
nav_order: 170
evidence_level: L5
indication_count: 1
monitor_inn: "EZETIMIBE"
predicted_indications: ["cholesterol-ester transfer protein deficiency"]
last_modified_at: 2026-10-28
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

Detaljerte data om virkningsmekanisme er ikke tilgjengelige i datagrunnlaget for denne rapporten. Ezetimib er kjent for å hemme NPC1L1-mediert opptak av kolesterol i tarmen og dermed senke LDL-kolesterol. Denne mekanismen er ikke bekreftet av de innsamlede dataene.

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
## Ansvarsfraskrivelse

Dette innholdet er kun til forskningsformål og utgjør ikke medisinsk rådgivning.
Klinisk validering kreves før enhver klinisk anvendelse.

---

