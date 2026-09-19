---
layout: default
title: Galcanezumab
parent: Kun modellprediksjon (L5)
nav_order: 157
evidence_level: L5
indication_count: 3
---

# Galcanezumab
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

# Galcanezumab: Fra migreneforebygging til heparinkofaktor 2-mangel

## Sammendrag på en setning

Galcanezumab er et anti-CGRP (calcitonin gene-related peptide) monoklonal antistoff, kjent klinisk for migrenforebygging (originale indikasjonsdata er ikke registrert i denne bevissakken).
TxGNN-modellen forutsier at det kan være effektivt for **heparinkofaktor 2-mangel**,
men for tiden finnes det **ingen kliniske studier** og **ingen publikasjoner** som støtter denne retningen — prediksjonen er basert på modellpoengstanden alene.

---

## Rask oversikt

| Element | Innhold |
|------|--------|
| Original indikasjon | Ikke registrert i denne bevissakken (original_indications er tom); kjent farmakologi indikerer bruk som anti-CGRP-antistoff for migrenforebygging |
| Forutsagt ny indikasjon | Heparinkofaktor 2-mangel |
| TxGNN-prediksjonspoengstand | 99.50% |
| Bevisnivå | L5 |
| Markedsstatus Norge | Ikke markedsført |
| Antall autorisasjoner | 0 |
| Anbefalt beslutning | Avvent |

---

## Hvorfor er denne prediksjonen rimelig?

For tiden er detaljerte virkningsmekanisme-data ikke tilgjengelige (MOA-feltet er en datamangler). Basert på kjent farmakologi er galcanezumab et anti-CGRP monoklonal antistoff, og dets effektivitet i migrenforebygging er godt etablert gjennom trigeminovaskular smertevei.

Imidlertid er bevissakken sitt eget mekanistiske vurdering eksplisitt at **ingen kjent biologisk forbindelse finnes** mellom CGRP-signalering og heparinkofaktor II (en serinproteasehemmer som hemmer trombin). CGRP virker på neurovaskular smertesignalering og vasodilatasjon, mens heparinkofaktor II-mangel er en blødningsrelatert genetisk tilstand — disse to systemene har ingen etablert farmakologisk sammenfall.

Dette ser ut til å være et tilfelle der TxGNN-modellen tildelte en numerisk høy poengstand uten et underliggende biologisk grunnlag (også reflektert i den lave prediksjonsrangeringen på 5461 av den fulle kandidatlisten). Modellpoengstanden alene er utilstrekkelig grunnlag for å prioritere denne kandidaten; uavhengig mekanistisk eller preklinisk validering ville være nødvendig før denne prediksjonen kan anses som troverdig.

**Merknad:** To andre kandidater ble også forutsagt for dette legemidlet med tilsvarende høye poengstander, men like svak mekanistisk støtte — *antitrombin-mangel type 2* (poengstand 99.41%, rangering 6213) og *faktor 5-overskudd med spontan trombose* (poengstand 99.41%, rangering 6221). Alle tre faller inn i blødnings-/hemostase-sykdomsklyngen, noe som antyder at modellen kanskje plukker opp et falskt mønster snarere enn et ekte CGRP–blødningsforhold.

---

## Bevis fra kliniske studier

For tiden ingen relaterte kliniske studier registrert

---

## Bevis fra litteratur

For tiden ingen relatert litteratur tilgjengelig

---

## Markedsinformasjon Norge

Galcanezumab er ikke markedsført i Norge etter denne bevissakken (0 autorisasjoner registrert); ingen lisensdatakort er tilgjengelig for gjennomgang.

---

## Sikkerhetshensyn

Vennligst se pakningsvedlegget for sikkerhetsinformasjon.

---

## Konklusjon og neste trinn

**Beslutning: Avvent**

**Begrunnelse:**
Til tross for en høy TxGNN-prediksjonspoengstand, finnes det ingen klinisk studie eller litteraturbevis, og den mekanistiske begrunnelsen identifiserer eksplisitt ingen kjent biologisk forbindelse mellom CGRP-signalering og heparinkofaktor II-funksjon. Bevisnivået (L5) gjenspeiler modellprediksjon kun, som er utilstrekkelig til å rettferdiggjøre ytterligere utviklingsinnsats på dette stadiet.

**For å fortsette trengs følgende:**
- Bekreftet original indikasjon og MOA-data for galcanezumab (for tiden datamangler)
- TFDA/regulatoriske etikettadvarsler og kontraindikasjoner (for tiden datamangler, merket med blokkerende alvorlighetsgrad)
- Uavhengig mekanistisk eller preklinisk bevis som knytter CGRP-veier til blødnings-/hemostase-forstyrrelser
- Revurdering hvis noen kliniske studier eller kasuistikker dukker opp som forbinder anti-CGRP-terapi til blødningsfaktorforstyrrelser

## Ansvarsfraskrivelse

Dette innholdet er kun til forskningsformål og utgjør ikke medisinsk rådgivning.
Klinisk validering kreves før enhver klinisk anvendelse.

---

