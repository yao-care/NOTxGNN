---
layout: default
title: Pioglitazone
parent: Kun modellprediksjon (L5)
nav_order: 327
evidence_level: L5
indication_count: 9
last_modified_at: 2026-10-15
description: "Pioglitazone: predikert ny indikasjon Opsismodysplasi (evidensnivå L5). Opprinnelig indikasjon: Diabetes mellitus type 2"
monitor_inn: "PIOGLITAZONE"
predicted_indications: ["opsismodysplasia", "focal stiff limb syndrome", "classic stiff person syndrome", "thiamine-responsive dysfunction syndrome", "drug-induced localized lipodystrophy", "centrifugal lipodystrophy", "pressure-induced localized lipoatrophy", "idiopathic localized lipodystrophy", "pancreatic agenesis"]
---

# Pioglitazone
{: .fs-9 }

Evidensnivå: **L5** | Predikerte indikasjoner: **9** stk.
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

# Pioglitazon: Fra diabetes mellitus type 2 til opsismodysplasi

## Oppsummering i én setning

Pioglitazon er en insulinsensitiserende PPAR-gamma-agonist som opprinnelig brukes til behandling av diabetes mellitus type 2.
TxGNN-modellen predikerer at legemidlet kan være effektivt mot **opsismodysplasi** (en sjelden skjelettdysplasi),
men det finnes **ingen kliniske studier** og **ingen publikasjoner** som støtter denne spesifikke prediksjonen. Prediksjonen er kun modellbasert.

---

## Hurtigoversikt

| Punkt | Innhold |
|------|------|
| Opprinnelig indikasjon | Diabetes mellitus type 2 |
| Predikert ny indikasjon | Opsismodysplasi |
| TxGNN-prediksjonsscore | 99,59 % |
| Evidensnivå | L5 |
| Markedsstatus i Norge | Kun opphevede/utgåtte godkjenninger |
| Antall godkjenninger | 6 (alle opphevet) |
| Anbefalt beslutning | Hold |

---

## Hvorfor er denne prediksjonen rimelig?

Detaljerte data om virkningsmekanisme er foreløpig ikke tilgjengelige i datagrunnlaget. Pioglitazon er kjent som en PPAR-gamma-agonist og insulinsensitiserer, og effekten ved diabetes mellitus type 2 er godt dokumentert.

Opsismodysplasi er en sjelden skjelettdysplasi forårsaket av mutasjoner i INPPL1 (SHIP2), som påvirker PI3K-/insulinsignalering og utvikling av vekstplaten. En spekulativ kobling via insulin-/PI3K-signalering er tenkelig, men den støttes ikke av noen studie eller litteratur. Den høye scoren (0,996) er utelukkende en modellprediksjon, og prediksjonen kan like gjerne gjenspeile nærhet i kunnskapsgrafen som et reelt terapeutisk grunnlag.

Andre høyt rangerte prediksjoner (alle på evidensnivå L5 og med anbefalingen «Hold») er stiv-person-spekteret (fokalt stivt lem-syndrom og klassisk stiv person-syndrom), tiaminresponsivt dysfunksjonssyndrom, flere lokaliserte lipodystrofier og pankreasagenesi. Av disse er lipodystrofiene biologisk mest plausible på grunn av PPAR-gammas rolle i adipogenese, men også her mangler data.

---

## Evidens fra kliniske studier

Foreløpig finnes ingen registrerte kliniske studier knyttet til denne indikasjonen.

---

## Litteraturevidens

Foreløpig finnes ingen relevant litteratur for opsismodysplasi.

*Merknad:* For den niende prediksjonen (pankreasagenesi) ble det hentet sju publikasjoner. De er generelle oversikter om diabetes type 2 og tiazolidindioner og omhandler ikke pankreasagenesi. De er trolig funnet gjennom treff på legemiddelnavn og regnes som indirekte og lite relevante.

---

## Markedsinformasjon for Norge

Alle seks godkjenningene er oppført som opphevet (ingen gyldige godkjenninger).

| Godkjenningsnummer | Produktnavn | Doseringsform | Godkjent indikasjon |
|---------|------|------|-----------|
| EMEA/H/C/000285 | Actos | – | Diabetes mellitus type 2 |
| EMEA/H/C/002277 | Pioglitazone Accord | – | Diabetes mellitus type 2 |
| EMEA/H/C/002324 | Pioglitazone Actavis | – | Diabetes mellitus type 2 |
| EMEA/H/C/000655 | Competact | – | Diabetes mellitus type 2 |
| EMEA/H/C/000680 | Tandemact | – | Diabetes mellitus type 2 |

---

## Sikkerhetsvurderinger

Pakningsvedlegg med advarsler og kontraindikasjoner er ikke tilgjengelig i datagrunnlaget. Les preparatomtalen for fullstendig sikkerhetsinformasjon.

- **Kontraindikasjoner fra kunnskapsgraf (ikke fra preparatomtale):** Kunnskapsgrafen (PrimeKG) knytter pioglitazon til blant annet kongestiv hjertesvikt, nyresykdom, leversykdom, gallblæresykdom, hypofysesvikt (hypopituitarisme og relaterte tilstander, inkl. Sheehan syndrom og Kallmann syndrom), binyrebarksvikt/Addisons sykdom, sykdom i thymus og infeksjonssykdom. Dette er grafbaserte assosiasjoner og må verifiseres mot offisiell preparatomtale.
- **Legemiddelinteraksjoner:** Totalt 100 interaksjoner er registrert. Eksempler på moderate interaksjoner: abirateron, fenylefrin, acetazolamid, formoterol, pseudoefedrin, epinefrin, hydrokortison, salbutamol, etanol, hydroklortiazid, aloe vera-blad og alpelisib. Eksempler på mindre alvorlige: nifedipin, etinylestradiol og liponsyre.

---

## Konklusjon og neste steg

**Beslutning: Hold**

**Begrunnelse:**
Prediksjonen er kun modellbasert (L5) uten kliniske studier eller relevant litteratur. Pioglitazon har dessuten ingen gyldige godkjenninger i Norge i dag, og sikkerhetsdata fra preparatomtalen mangler.

**For å gå videre kreves følgende:**
- Data om virkningsmekanisme (MOA) fra DrugBank
- Preparatomtale med advarsler og kontraindikasjoner (blokkerende datamangel for sikkerhetsscreening)
- Prekliniske eller mekanistiske studier som knytter PPAR-gamma-/insulin-/PI3K-signalering til INPPL1-relatert skjelettdysplasi
- Systematisk litteratursøk for opsismodysplasi og vurdering av de mer plausible alternativene (lokaliserte lipodystrofier)
- Avklaring av regulatorisk status i Norge siden alle godkjenninger er opphevet
## Ansvarsfraskrivelse

Dette innholdet er kun til forskningsformål og utgjør ikke medisinsk rådgivning.
Klinisk validering kreves før enhver klinisk anvendelse.

---

