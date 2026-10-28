---
layout: default
title: Alanine
parent: Kun modellprediksjon (L5)
nav_order: 21
evidence_level: L5
indication_count: 1
last_modified_at: 2026-10-15
description: "Alanine: predikert ny indikasjon Gastroparese (evidensnivå L5). Opprinnelig indikasjon: Lønnesirupsykdom (Maple Syrup Urine Disease)"
monitor_inn: "alanine"
predicted_indications: ["gastroparesis (disease)"]
---

# Alanine
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

## Alanin: Fra lønnesirupsykdom (MSUD) til gastroparese
{: .text-alpha }

## Oppsummering i én setning

Alanin er en aminosyre som i produktet Maapliv er godkjent for behandling av lønnesirupsykdom (Maple Syrup Urine Disease). TxGNN-modellen forutsier at den kan være aktuell for **gastroparese**, men det finnes **ingen registrerte kliniske studier** og bare **3 publikasjoner** med svak tilknytning til denne retningen. Forutsigelsen bygger i praksis kun på en datamodell.

---

## Hurtigoversikt

| Punkt | Innhold |
|------|------|
| Opprinnelig indikasjon | Lønnesirupsykdom (Maple Syrup Urine Disease) |
| Foreslått ny indikasjon | Gastroparese |
| TxGNN-prediksjonsscore | 0,9937 |
| Evidensnivå | L5 |
| Markedsstatus i Norge | Markedsført (gyldige tillatelser: 1 av 1) |
| Antall godkjenninger | 1 (gyldige: 1) |
| Antall tillatelser | 1 (avregistrert) |
| Anbefalt beslutning | Hold |

---

## Hvorfor er denne prediksjonen (ikke) rimelig?

Det foreligger for øyeblikket ingen detaljerte data om virkningsmekanisme for alanin. Alanin er en naturlig forekommende aminosyre, og den er godkjent for lønnesirupsykdom, en stoffskjellsykdom. Det er ikke påvist noen troverdig mekanistisk kobling mellom alanin og gastroparese.

Den høye prediksjonsscoren (0,9937) er et rent beregningsmessig resultat fra TxGNN-modellen (deep learning), og kan gjenspeile likheter modellen har lært mellom beslektede sykdommer, ikke biologisk evidens. De tre hentede publikasjonene omhandler mage-tarm- og leverlidelser ved nyresvikt i sluttstadiet, diabetisk hepatosklerose og glykogenhepatopati ved type 1-diabetes. Ingen av dem undersøker alanin som behandling av gastroparese. Sammenhengen skyldes trolig den felles diabetiske konteksten, siden gastroparese er en vanlig diabeteskomplikasjon, og ikke en faktisk samhandling mellom legemiddel og sykdom.

Likheten mellom den opprinnelige og den nye indikasjonen er ikke vurdert.

---

## Evidens fra kliniske studier

Det er for øyeblikket ingen relaterte kliniske studier registrert.

---

## Litteraturevidens

| PMID | År | Type | Tidsskrift | Hovedfunn |
|------|-----|------|------|---------|
| [10926110](https://pubmed.ncbi.nlm.nih.gov/10926110/) | 2000 | Oversikt | Advances in Renal Replacement Therapy | Mage-tarm- og leverlidelser ved nyresvikt i sluttstadiet og etter nyretransplantasjon; gastroparese er vanligere ved kronisk nyresvikt. Omtaler ikke alanin. |
| [26315331](https://pubmed.ncbi.nlm.nih.gov/26315331/) | 2016 | Oversikt | Diabetic Medicine | Diabetisk hepatosklerose som mulig mikrovaskulær diabeteskomplikasjon. Omtaler ikke alanin. |
| [33763324](https://pubmed.ncbi.nlm.nih.gov/33763324/) | 2021 | Oversikt (kasuistikk) | Cureus | Glykogenhepatopati ved type 1-diabetes, hos en pasient som også hadde gastroparese. Omtaler ikke alanin. |

---

## Markedsinformasjon for Norge

| Tillatelsesnummer | Produktnavn | Doseringsform | Godkjent indikasjon |
|---------|------|------|-----------|
| EMEA/H/C/005557 | Maapliv | Ikke oppgitt | Maple Syrup Urine Disease (status: godkjent) |

---

## Sikkerhetsvurderinger

Se pakningsvedlegget for sikkerhetsinformasjon.

Kunnskapsgrafen (PrimeKG) viser følgende sykdommer knyttet til kontraindikasjoner. Dette er modellrelasjoner og ikke tekst fra godkjent preparatomtale, så de må verifiseres mot offisiell produktinformasjon:

- **Nyre:** nyresykdom, kronisk nyresykdom, kronisk nyresvikt, nyresvikt i sluttstadiet, nefrolitiasis (inkludert SLC26A1-relatert disposisjon), nefrokalsinose, akutt uratnefropati
- **Kalsium og fosfor:** hyperkalsemi, humoral hyperkalsemi ved malignitet, sarkoidose, forstyrrelser i fosformetabolismen
- **Hjerte og kar:** hjertesykdom, kardiovaskulær sykdom, ventrikkelflimmer, digitalisforgiftning
- **Stoffskifte:** fenylketonuri, forstyrrelser i fenylalaninmetabolismen
- **Annet:** pyoureter

Det er ikke funnet registrerte legemiddelinteraksjoner i de innsamlede dataene.

---

## Konklusjon og neste steg

**Beslutning: Hold**

**Begrunnelse:**
Prediksjonen støttes bare av en beregningsmodell (evidensnivå L5), uten kliniske studier og uten litteratur som undersøker alanin ved gastroparese. I tillegg er produktet avregistrert i Norge, og sikkerhetsdata fra preparatomtale mangler.

**For å gå videre kreves følgende:**
- Data om virkningsmekanisme (MOA) fra DrugBank for å kunne vurdere en mekanistisk kobling
- Advarsler og kontraindikasjoner fra pakningsvedlegget (DMP), som er nødvendig før sikkerhetsscreening
- Målrettet litteratursøk og prekliniske data om alanin og mage-tarmmotilitet
- Vurdering av de kunnskapsgrafbaserte kontraindikasjonene, særlig nyre- og hjertesykdom
- Avklaring av doseringsform og administrasjonsvei for en eventuell ny indikasjon
## Ansvarsfraskrivelse

Dette innholdet er kun til forskningsformål og utgjør ikke medisinsk rådgivning.
Klinisk validering kreves før enhver klinisk anvendelse.

---

