---
layout: default
title: Lapatinib
parent: Kun modellprediksjon (L5)
nav_order: 199
evidence_level: L5
indication_count: 1
---

# Lapatinib
{: .fs-9 }

Evidensnivå: **L5** | Predikerte indikasjoner: **1** stk.
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

# Lapatinib: Fra en uregistrert originalindikasjon til dermatofibrosarcoma protuberans

## Oppsummering på én setning

Bevissamlingen for Lapatinib (DrugBank DB01259) inneholder ikke den opprinnelige godkjente indikasjonen eller virkningsmekanisme — begge er registrert som datamangler. TxGNN-modellen forutsier en mulig ny indikasjon for **Dermatofibrosarcoma Protuberans (DFSP)**, men denne prediksjonen er for øyeblikket støttet av **ingen kliniske forsøk og ingen publisert litteratur**, og legemidlet er ikke markedsført i Norge.

---

## Hurtig oversikt

| Element | Innhold |
|---------|---------|
| Originalindikasjon | Ikke tilgjengelig — ingen norske lisensoppføringer og `original_indications` er tom i bevissamlingen |
| Forutsagt ny indikasjon | Dermatofibrosarcoma Protuberans |
| TxGNN Prediction Score | 99.30% |
| Evidence Level | L5 |
| Markedsstatus Norge | ✗ Ikke markedsført |
| Antall godkjenninger | 0 |
| Anbefalt beslutning | Hold |

---

## Hvorfor er denne prediksjonen fornuftig?

Detaljerte data om virkningsmekanisme for Lapatinib er ikke tilgjengelig i denne bevissamlingen, og ingen originalindikasjon er registrert heller, så en direkte mekanistisk forbindelse mellom den opprinnelige bruken og DFSP kan ikke etableres fra dataene som er gitt.

Basert på generell kunnskap kodet i modellens begrunnelse, er DFSP primært drevet av en **COL1A1-PDGFB-fusjon** som forårsaker konstant PDGFRB-aktivering, og dens standard målrettet terapi er imatinib (en PDGFR-hemmer). Lapatinibs kjente mål — EGFR og HER2 — overlapper ikke direkte med PDGFRB. Den foreslåtte forbindelsen hviler kun på en teoretisk, ubekreftet mulighet for off-target PDGFR-kryssinhibisjon, uten eksperimentelle eller kliniske data som støtter det.

Gitt de manglende MOA-dataene og fraværet av en validert originalindikasjon, er den mekanistiske plausibiliteten til denne prediksjonen svak og bør behandles som hypotesegenererende kun, ikke som bevis på terapeutisk relevans.

---

## Bevis fra kliniske forsøk

For øyeblikket ingen relaterte kliniske forsøk registrert.

---

## Bevis fra litteratur

For øyeblikket ingen relatert litteratur tilgjengelig.

---

## Norsk markedsinformasjon

Lapatinib har for øyeblikket ingen markedsgodkjenning i Norge (0 lisenser på fil; markedsstatus: ikke markedsført).

---

## Sikkerhetshensyn

Vennligst se pakningsvedlegget for sikkerhetsinformasjon.

---

## Konklusjon og neste steg

**Beslutning: Hold**

**Begrunnelse:**
TxGNN-skåren er høy, men det er null klinisk forsøk eller litteraturstøtte, den mekanistiske begrunnelsen som forbinder Lapatinib (EGFR/HER2-hemmer) til DFSP (PDGFRB-drevet) er svak og spekulativ, og kritiske legemiddeldata (MOA, TFDA/etikett advarsler og kontraindikasjoner) mangler — en av disse (etikett advarsler/kontraindikasjoner) er flagget som en **Blokkering**-datamangel som forhindrer selv en innledende S1-sikkerhetsvurdering.

**For å fortsette, kreves følgende:**
- Originalindikasjon og etikett-data for Lapatinib (for øyeblikket helt fraværende fra bevissamlingen)
- Virkningsmekanisme-data (DG002) for å kunne vurdere EGFR/HER2–PDGFRB-forbindelsen på riktig måte
- TFDA/Norge etikett advarsler og kontraindikasjoner (DG001, Blokkering) før noen sikkerhetsvurdering kan begynne
- Som minimum preklinisk eller bevis på saksnivå som forbinder HER2/EGFR-inhibisjon til DFSP-biologi før avansering utover S0

## Ansvarsfraskrivelse

Dette innholdet er kun til forskningsformål og utgjør ikke medisinsk rådgivning.
Klinisk validering kreves før enhver klinisk anvendelse.

---

