---
layout: default
title: Esketamine
parent: Kun modellprediksjon (L5)
nav_order: 162
evidence_level: L5
indication_count: 2
last_modified_at: 2026-11-20
description: "Esketamine: predikert ny indikasjon Agorafobi (evidensnivå L5). Opprinnelig indikasjon: Depressiv lidelse"
monitor_inn: "Esketamine"
predicted_indications: ["agoraphobia", "benign paroxysmal torticollis of infancy"]
---

# Esketamine
{: .fs-9 }

Evidensnivå: **L5** | Predikerte indikasjoner: **2** stk.
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

## Esketamin: Fra depressiv lidelse til agorafobi
{: .text-alpha }

## Oppsummering i én setning

Esketamin ble opprinnelig godkjent for behandling av depressiv lidelse.
TxGNN-modellen forutsier at det kan ha effekt på **agorafobi**, men
det finnes foreløpig **ingen kliniske studier** og **ingen publikasjoner** i dataene som er samlet inn for denne rapporten som støtter denne retningen.

---

## Hurtigoversikt

| Punkt | Innhold |
|------|------|
| Opprinnelig indikasjon | Depressiv lidelse |
| Predikert ny indikasjon | Agorafobi |
| TxGNN-prediksjonsscore | 0,9957 |
| Evidensnivå | L5 |
| Markedsstatus i Norge | Markedsført (gyldige tillatelser: 1 av 1) |
| Antall godkjenninger | 1 (gyldige: 1) |
| Anbefalt beslutning | Hold |

---

## Hvorfor er denne prediksjonen rimelig?

Ifølge avsnittet «Mechanism of Action» i preparatomtalen som er godkjent av amerikanske FDA (Prescribing Information), for Esketamine (uoffisiell oversettelse): «Esketamin, S-enantiomeren av racemisk ketamin, er en ikke-selektiv, ikke-kompetitiv antagonist av N-metyl-D-aspartat (NMDA)-reseptoren, en ionotrop glutamatreseptor. Mekanismen som esketamin utøver sin antidepressive effekt gjennom, er ukjent.» Engelsk originaltekst: "Esketamine, the S-enantiomer of racemic ketamine, is a non-selective, non-competitive antagonist of the N -methyl- D -aspartate (NMDA) receptor, an ionotropic glutamate receptor. The mechanism by which esketamine exerts its antidepressant effect is unknown." ([DailyMed: Spravato (esketamine hydrochloride) prescribing information, Janssen Pharmaceuticals, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=d81a6a79-a74a-44b7-822c-0dfa3036eaed), versjon av 2026-09-22; hentet 2026-11-19). Esketamin er kjent som en NMDA-reseptorantagonist, og er godkjent for depressiv lidelse. Mekanismen kan i teorien være relevant for agorafobi, men dette er ikke bekreftet i dataene.

Et mulig, men uverifisert resonnement er at esketamin øker glutamaterg signalering og synaptisk plastisitet. Dette kan påvirke nevrale kretser for angst og frykthåndtering som antas å spille en rolle ved agorafobi. Angst er dessuten ofte komorbid med depresjon. Koblingen er spekulativ, og det foreligger ingen støttende klinisk evidens eller litteratur i de innsamlede dataene.

Selv om modellscoren er svært høy (0,9957), er den kun en beregningsmessig prediksjon og må ikke tolkes som dokumentasjon på effekt.

---

## Evidens fra kliniske studier

Foreløpig ingen relaterte kliniske studier registrert.

---

## Litteraturevidens

Foreløpig ingen relatert litteratur tilgjengelig.

---

## Markedsinformasjon for Norge

| Godkjenningsnummer | Produktnavn | Doseringsform | Godkjent indikasjon |
|---------|------|------|-----------|
| EMEA/H/C/004535 | Spravato | Ikke oppgitt | Depressiv lidelse (status: godkjent) |

---

## Sikkerhetsvurderinger

- **Sykdommer med kontraindikasjon i kunnskapsgrafen (PrimeKG, ikke preparatomtale):** karsykdom, arteriovenøs hemangiom/misdannelse.
- **Legemiddelinteraksjoner:** Totalt 70 interaksjoner er funnet. Noen av de viktigste er:
  - **Alvorlige (Major):** dietylpropion, fentermin, fenfluramin, mazindol, koffein
  - **Moderate:** loperamid, morfin (inkl. liposomal), opium, difenoksin, difenoksylat, dronabinol, nabilon, metoklopramid, skopolamin, samt nasale kortikosteroider og efedrin (beklometason, budesonid, triamcinolon, deksametason)

Detaljert sikkerhetsinformasjon (advarsler og kontraindikasjoner) fra preparatomtalen mangler. Se preparatomtalen for fullstendig sikkerhetsinformasjon.

---

## Konklusjon og neste steg

**Beslutning: Hold**

**Begrunnelse:**
Prediksjonen bygger kun på modellscore (evidensnivå L5), uten kliniske studier eller litteratur. Sikkerhetsdata fra preparatomtalen mangler.

<!-- review:begin no-lic-20261106-esketamine-1 -->

> **Kontrollrettelse (2026-11-06)**: Opprinnelig sto det: «I tillegg er den eneste norske/europeiske godkjenningen avregistrert, og sikkerhetsdata fra preparatomtalen mangler.» Fjernet: opplysningen om at godkjenningene er avregistrert eller at ingen gyldig godkjenning finnes, stemte ikke med EMAs data om sentrale EU-godkjenninger (2026-11-06). Antall godkjenninger i dataene: 1, hvorav gyldige: 1; oppdaterte tall står i hurtigoversikten og i markedsinformasjonen. Kilde: [EMA – Medicines output: medicines report](https://www.ema.europa.eu/en/documents/report/medicines-output-medicines-report_en.xlsx); [European Medicines Agency](https://www.ema.europa.eu/).

<!-- review:end no-lic-20261106-esketamine-1 -->

**For å gå videre kreves følgende:**
- Innhenting og gjennomgang av preparatomtale (advarsler og kontraindikasjoner), som er en blokkerende datamangel
- Data om virkningsmekanisme (MOA) fra DrugBank
- Litteratursøk og søk etter kliniske studier på esketamin ved agorafobi og angstlidelser
- Avklaring av administrasjonsvei og forenlighet med den predikerte indikasjonen
- Vurdering av risiko ved interaksjoner, spesielt med sentralstimulerende og appetittdempende midler

---

## Merknad om rangering nr. 2: godartet paroksysmal torticollis hos spedbarn

TxGNN gir også en høy score (0,9949) for **godartet paroksysmal torticollis hos spedbarn**, men det foreligger ingen kliniske studier eller litteratur (evidensnivå L5, anbefaling: Hold). Tilstanden er en sjelden episodisk lidelse hos barn, knyttet til migrenespekteret og kanalopatier. Koblingen til NMDA-antagonisme er rent beregningsmessig og spekulativ. Esketamins sikkerhetsprofil (dissosiasjon, blodtrykksøkning, misbrukspotensial) og at det er godkjent kun for voksne, gjør bruk hos spedbarn til en stor bekymring. Ingenting i dataene støtter at dette bør forfølges.

<!-- review:begin log -->

## Kontrollogg

Nedenfor er kontrolloggen for denne siden: opplysninger kontrollert mot EMAs data om sentrale EU-godkjenninger. Rettelser gjelder bare grunnleggende faktaopplysninger; modellens prediksjoner, evidensnivåer og konklusjoner er ikke skrevet om. Setningen om at data om virkningsmekanismen ikke var tilgjengelige, er erstattet med et utdrag fra den oppgitte offisielle preparatomtalen (med uoffisiell oversettelse).

| Kontrolldato | Punkt | Tiltak | Kilde |
|------|------|------|------|
| 2026-11-06 | Fjernet: «I tillegg er den eneste norske/europeiske godkjenningen avregistrert, og s» | Rettet | [EMA – Medicines output: medicines report](https://www.ema.europa.eu/en/documents/report/medicines-output-medicines-report_en.xlsx); [European Medicines Agency](https://www.ema.europa.eu/) |
| 2026-11-19 | Setningen «data om virkningsmekanismen er ikke tilgjengelige» erstattet med utdrag fra amerikansk preparatomtale | Setning om manglende data om virkningsmekanismen erstattet med et utdrag med kilde | [DailyMed: Spravato (esketamine hydrochloride) prescribing information, Janssen Pharmaceuticals, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=d81a6a79-a74a-44b7-822c-0dfa3036eaed) |

<!-- review:end log -->

## Ansvarsfraskrivelse

Dette innholdet er kun til forskningsformål og utgjør ikke medisinsk rådgivning.
Klinisk validering kreves før enhver klinisk anvendelse.

---

