---
layout: default
title: Zanamivir
parent: Kun modellprediksjon (L5)
nav_order: 457
evidence_level: L5
indication_count: 2
last_modified_at: 2026-10-15
description: "Zanamivir: predikert ny indikasjon Pyelonefritt (evidensnivå L5). Opprinnelig indikasjon: Influenza (Influenza, Human)"
monitor_inn: "ZANAMIVIR"
predicted_indications: ["pyelonephritis", "disorder of tyrosine metabolism"]
---

# Zanamivir
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

# Zanamivir: Fra influensa til pyelonefritt

## Oppsummering i én setning

Zanamivir er en nevraminidasehemmer som opprinnelig brukes til behandling av influensa (Influenza, Human).
TxGNN-modellen predikerer at legemidlet kan ha effekt mot **pyelonefritt**, men det finnes **ingen kliniske studier** og **ingen publikasjoner** som støtter denne retningen.
Den høye modellscoren ser ut til å være et beregningsmessig artefakt og ikke et resultat av biologisk evidens.

---

## Hurtigoversikt

| Punkt | Innhold |
|------|------|
| Opprinnelig indikasjon | Influenza (Influenza, Human) |
| Predikert ny indikasjon | Pyelonefritt |
| TxGNN-prediksjonsscore | 99,84 % |
| Evidensnivå | L5 |
| Markedsstatus i Norge | Kun avregistrert/kansellert |
| Antall godkjenninger | 1 |
| Anbefalt beslutning | Hold |

---

## Hvorfor er (eller er ikke) denne prediksjonen rimelig?

Data om virkningsmekanisme er ikke tilgjengelig i datagrunnlaget for denne rapporten. Basert på kjent informasjon er zanamivir en hemmer av det virale enzymet nevraminidase, med aktivitet mot influensa A og B.

Pyelonefritt er vanligvis en bakteriell nyreinfeksjon, oftest forårsaket av *E. coli*. Det finnes bakterielle nevraminidaser (sialidaser), men zanamivir er ikke kjent for å ha klinisk meningsfull antibakteriell aktivitet, og det foreligger ingen støttende data. Det er dermed ingen etablert mekanistisk kobling mellom den opprinnelige og den predikerte indikasjonen.

Den svært høye TxGNN-scoren (0,998) skyldes trolig felles «infeksjons»-assosiasjoner i kunnskapsgrafen og ikke faktisk evidens. Prediksjonen bør derfor betraktes som en hypotese uten støtte.

Merk også at den nest rangerte prediksjonen, **forstyrrelse i tyrosinmetabolismen** (score 99,02 %), heller ikke har noen plausibel mekanistisk kobling. Nevraminidase har ingen kjent rolle i tyrosinkatabolismen. De tre publikasjonene som ble hentet frem, handler om resistens mot nevraminidasehemmere (oseltamivir-resistens, en SPR-analyse og en N294S-mutasjon i nevraminidase) og er urelaterte til tyrosinmetabolisme. Treffet skyldes trolig et nøkkelordartefakt («tyrosin» mot aminosyremutasjoner).

---

## Klinisk studieevidens

Foreløpig er ingen relaterte kliniske studier registrert.

---

## Litteraturevidens

Foreløpig finnes ingen relatert litteratur for pyelonefritt.

---

## Markedsinformasjon for Norge

| Godkjenningsnummer | Produktnavn | Doseringsform | Godkjent indikasjon |
|---------|------|------|-----------|
| EMEA/H/C/004102 | Dectova | Ikke oppgitt | Influenza, Human |

Godkjenningen er kansellert, og det finnes ingen gyldige markedsføringstillatelser for zanamivir i dataene.

---

## Sikkerhetsvurderinger

- **Kontraindikasjoner fra kunnskapsgrafen (PrimeKG, ikke preparatomtale):** epilepsi, kronisk obstruktiv lungesykdom (KOLS), tidligdebuterende alvorlig KOLS, bronkiale sykdommer og delirium. Disse er relasjoner fra en kunnskapsgraf og må verifiseres mot preparatomtalen.
- **Legemiddelinteraksjoner (8 funnet):**
  - Insulin human (inhalasjon, hurtigvirkende): **moderat**
  - Klaritromycin, loratadin, montelukast, ketotifen, feksofenadin, ibuprofen og diklofenak: alvorlighetsgrad ukjent

Informasjon om advarsler og kontraindikasjoner fra preparatomtalen er ikke tilgjengelig. Se preparatomtalen for fullstendig sikkerhetsinformasjon.

---

## Konklusjon og neste steg

**Beslutning: Hold**

**Begrunnelse:**
Prediksjonen for pyelonefritt har kun modellstøtte (L5), uten kliniske studier, uten litteratur og uten plausibel mekanistisk kobling. I tillegg er den eneste norske/europeiske godkjenningen kansellert.

**For å gå videre kreves følgende:**
- Preparatomtale med advarsler og kontraindikasjoner (blokkerende datamangel)
- Data om virkningsmekanisme (MOA), f.eks. fra DrugBank
- Prekliniske data (in vitro) som viser eventuell antibakteriell aktivitet mot uropatogener som *E. coli*
- Vurdering av administrasjonsvei og farmakokinetikk (nyre-/urinkonsentrasjoner) for den predikerte indikasjonen
- Systematisk litteratursøk målrettet mot pyelonefritt
## Ansvarsfraskrivelse

Dette innholdet er kun til forskningsformål og utgjør ikke medisinsk rådgivning.
Klinisk validering kreves før enhver klinisk anvendelse.

---

