---
layout: default
title: Verteporfin
parent: Kun modellprediksjon (L5)
nav_order: 449
evidence_level: L5
indication_count: 1
last_modified_at: 2026-10-28
description: "Verteporfin: predikert ny indikasjon Mitokondriell oksidativ fosforyleringssykdom på grunn av kjerne-DNA-avvik (evidensnivå L5). Opprinnelig indikasjon: Degenerativ myopi"
monitor_inn: "VERTEPORFIN"
predicted_indications: ["mitochondrial oxidative phosphorylation disorder due to nuclear DNA anomalies"]
---

# Verteporfin
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

## Verteporfin: Fra degenerativ myopi og makuladegenerasjon til mitokondriell oksidativ fosforyleringssykdom som skyldes kjerne-DNA-avvik
{: .text-alpha }

## Oppsummering i én setning

Verteporfin er et lysaktivert legemiddel (fotosensibilisator) som opprinnelig brukes ved degenerativ myopi og makuladegenerasjon. TxGNN-modellen forutsier at det kan ha effekt på **mitokondriell oksidativ fosforyleringssykdom som skyldes kjerne-DNA-avvik**, men det finnes **0 kliniske studier** og **0 publikasjoner** i dataene som støtter denne retningen. Prediksjonen er derfor kun en hypotese.

---

## Hurtigoversikt

| Punkt | Innhold |
|------|------|
| Opprinnelig indikasjon | Degenerativ myopi; makuladegenerasjon |
| Predikert ny indikasjon | Mitokondriell oksidativ fosforyleringssykdom som skyldes kjerne-DNA-avvik |
| TxGNN-prediksjonsscore | 0,9949 |
| Evidensnivå | L5 |
| Markedsstatus i Norge | Markedsført (gyldige tillatelser: 1 av 1) |
| Antall godkjenninger | 1 (gyldige: 1) |
| Anbefalt beslutning | Hold |

---

## Hvorfor er denne prediksjonen rimelig?

Data om virkningsmekanisme er ikke tilgjengelige for denne rapporten. Verteporfin er kjent som en fotosensibilisator som brukes sammen med lysaktivering (fotodynamisk terapi) ved neovaskulær makuladegenerasjon og beslektede øyetilstander.

I prekliniske arbeider hemmer verteporfin også samspillet mellom YAP og TEAD, og det kan danne reaktive oksygenforbindelser (ROS) og påvirke autofagi. Disse egenskapene kan i teorien berøre mitokondriebiologi.

Det finnes imidlertid ingen evidens som kobler dem til oksidative fosforyleringssykdommer drevet av kjerne-DNA. ROS fra fotosensibilisatorer kan i tillegg forverre mitokondriell dysfunksjon, så retningen på en eventuell effekt er uklar. Den eneste støtten er den høye modellscoren, og koblingen kan ikke verifiseres.

---

## Klinisk evidens

Det er for øyeblikket ingen registrerte kliniske studier knyttet til denne prediksjonen.

---

## Litteraturevidens

Det er for øyeblikket ingen relevant litteratur tilgjengelig.

---

## Markedsinformasjon for Norge

| Godkjenningsnummer | Produktnavn | Doseringsform | Godkjent indikasjon |
|---------|------|------|-----------|
| EMEA/H/C/000305 | Visudyne | Ikke oppgitt | Degenerativ myopi; makuladegenerasjon |

Legemidlet er markedsført. Det finnes 1 gyldig godkjenning av 1 (innehaver: CHEPLAPHARM Arzneimittel GmbH).

---

## Sikkerhetsvurderinger

- **Kontraindikasjoner fra kunnskapsgraf (ikke preparatomtale):** TxGNN-kunnskapsgrafen (PrimeKG) angir kontraindikasjonskoblinger til arvelig porfyri, forstyrrelser i porfyrinmetabolismen, porfyri, leversykdom og galleblæresykdom.
- **Legemiddelinteraksjoner:** Totalt 100 interaksjoner er funnet. De fleste i utvalget er av moderat alvorlighetsgrad, og én er mindre alvorlig (minor). Eksempler:
  - Tetracykliner: doksysyklin, tetracyklin, minocyklin (også topikale former)
  - Sulfonylurea-antidiabetika: klorpropamid, glimepirid, glipizid, glyburid, tolbutamid, tolazamid, acetoheksamid
  - Andre: acetylsalisylsyre, levofloksacin, mannitol, sulfasalazin, betakaroten, papaverin
  - Mindre alvorlig: polymyksin B

Fotosensibiliserende og andre legemidler bør vurderes samlet. For øvrig sikkerhetsinformasjon, se preparatomtalen.

---

## Konklusjon og neste steg

**Beslutning: Hold**

**Begrunnelse:**
Prediksjonen bygger kun på en høy modellscore (evidensnivå L5), uten kliniske studier eller litteratur. Virkningsmekanismen er ikke tilgjengelig, og det er uklart om ROS-dannelse vil hjelpe eller forverre mitokondriell dysfunksjon.

<!-- review:begin no-lic-20261112-verteporfin-1 -->

> **Kontrollrettelse (2026-11-12)**: Opprinnelig sto det: «forverre mitokondriell dysfunksjon. Den eneste norske godkjenningen er dessuten opphørt.» Fjernet: opplysningen om at godkjenningene er avregistrert eller at ingen gyldig godkjenning finnes, stemte ikke med EMAs data om sentrale EU-godkjenninger (2026-11-09). Antall godkjenninger i dataene: 1, hvorav gyldige: 1; oppdaterte tall står i hurtigoversikten og i markedsinformasjonen. Kilde: [EMA – Medicines output: medicines report](https://www.ema.europa.eu/en/documents/report/medicines-output-medicines-report_en.xlsx); [European Medicines Agency](https://www.ema.europa.eu/).

<!-- review:end no-lic-20261112-verteporfin-1 -->

**For å gå videre kreves følgende:**
- Detaljerte data om virkningsmekanisme (MOA), for eksempel fra DrugBank
- Preparatomtale med advarsler og kontraindikasjoner, som er nødvendig før en sikkerhetsvurdering
- Prekliniske studier (celle- eller dyremodeller) som tester effekt av verteporfin ved oksidative fosforyleringssykdommer, med særlig vekt på ROS-risiko
- Avklaring av egnet administrasjonsvei og lysaktiveringsstrategi for en ikke-okulær indikasjon

<!-- review:begin no-lic-20261112-verteporfin-2 -->

> **Kontrollrettelse (2026-11-12)**: Opprinnelig sto det: «Avklaring av egnet administrasjonsvei og lysaktiveringsstrategi for en ikke-okulær indikasjon / Avklaring av regulatorisk status, siden Visudyne-godkjenningen er opphørt» Fjernet: opplysningen om at godkjenningene er avregistrert eller at ingen gyldig godkjenning finnes, stemte ikke med EMAs data om sentrale EU-godkjenninger (2026-11-09). Antall godkjenninger i dataene: 1, hvorav gyldige: 1; oppdaterte tall står i hurtigoversikten og i markedsinformasjonen. Kilde: [EMA – Medicines output: medicines report](https://www.ema.europa.eu/en/documents/report/medicines-output-medicines-report_en.xlsx); [European Medicines Agency](https://www.ema.europa.eu/).

<!-- review:end no-lic-20261112-verteporfin-2 -->

<!-- review:begin log -->

## Kontrollogg

Nedenfor er kontrolloggen for denne siden: opplysninger kontrollert mot EMAs data om sentrale EU-godkjenninger. Rettelser gjelder bare grunnleggende faktaopplysninger; modellens prediksjoner, evidensnivåer og konklusjoner er ikke skrevet om.

| Kontrolldato | Punkt | Tiltak | Kilde |
|------|------|------|------|
| 2026-11-12 | Fjernet: «Den eneste norske godkjenningen er dessuten opphørt» | Rettet | [EMA – Medicines output: medicines report](https://www.ema.europa.eu/en/documents/report/medicines-output-medicines-report_en.xlsx); [European Medicines Agency](https://www.ema.europa.eu/) |
| 2026-11-12 | Fjernet: «Avklaring av regulatorisk status, siden Visudyne-godkjenningen er opphørt» | Rettet | [EMA – Medicines output: medicines report](https://www.ema.europa.eu/en/documents/report/medicines-output-medicines-report_en.xlsx); [European Medicines Agency](https://www.ema.europa.eu/) |

<!-- review:end log -->

## Ansvarsfraskrivelse

Dette innholdet er kun til forskningsformål og utgjør ikke medisinsk rådgivning.
Klinisk validering kreves før enhver klinisk anvendelse.

---

