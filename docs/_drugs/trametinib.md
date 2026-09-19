---
layout: default
title: Trametinib
parent: Kun modellprediksjon (L5)
nav_order: 367
evidence_level: L5
indication_count: 10
---

# Trametinib
{: .fs-9 }

Evidensnivå: **L5** | Predikerte indikasjoner: **10** stk.
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

# Trametinib: Fra malignt melanom til koreideremi

## Sammendrag i en setning

> Trametinib er en MEK1/2-hemmer utviklet og brukt (i kombinasjon med dabrafenib) for BRAF V600E/K-mutasjonspositiv malignt melanom.
> TxGNN-modellens topprangerte prediksjon er **koreideremi**, en sjelden arvelig netthinnedegenersjon,
> men denne prediksjonen er for øyeblikket støttet av **0 kliniske studier** og **0 publikasjoner**, og ingen kjent patofysiologisk sammenheng til legemidlets MAPK/MEK-mekanisme er identifisert.

---

## Rask oversikt

| Element | Innhold |
|------|------|
| Originalindikasjon | Malignt melanom, BRAF V600E/K-mutasjonspositiv (utledet fra internasjonale prøveregistreringer; ingen lokalt godkjent indiksjonstekst på fil) |
| Forutsagt ny indikasjon | Koreideremi |
| TxGNN prediksjonspoengsum | 99.31% |
| Bevisnivå | L5 |
| Status på Taiwan-markedet | Ikke markedsført (Ikke markedsført) |
| Antall godkjennelser | 0 |
| Anbefalt beslutning | Avvent |

---

## Hvorfor er denne prediksjonen fornuftig?

For øyeblikket er detaljerte virkningsmekanismedata ikke tilgjengelig i bevissamlingen (original_moa flagget som et datahull). Basert på informasjon innebygd i de støttende prøveregistreringene som følger med i denne pakken, beskrives trametinib (GSK1120212) som "en reversibel og svært selektiv allosterisk hemmer av MEK1 og MEK2," utviklet for behandling av malignt melanom, typisk i kombinasjon med BRAF-hemmeren dabrafenib.

Koreideremi er en sjelden X-koblet arvelig netthinnedegenersjon forårsaket av funksjonstap-mutasjoner i *CHM*-genet (som koder for Rab-eskorteprotein-1), som påvirker prenylasjonen av Rab GTPaser som kreves for fotoreseptor- og retinalt pigmentepitel-transport. Det finnes ingen etablert forbindelse mellom denne stien og MAPK/MEK-signaling, og bevissamlingens eget begrunnelse flagget dette eksplisitt: *"與 MAPK/MEK 通路無已知病理生理關聯"* — ingen kjent patofysiologisk sammenheng eksisterer.

Gitt fraværet av alle støttende kliniske prøver eller litteraturbeviser (bevisnivå L5, beslutningsstadium S0), gjenspeiler den høye TxGNN-poengsum for denne kandidaten mest sannsynlig en spuriøs korrelasjon i modellens innebyggingsrom snarere enn et genuint biologisk signal. Dette er en nyttig illustrasjon av en sak hvor råprediksjonsrangering ikke skal tolkes som klinisk prioritet uten uavhengig mekanistisk eller eksperimentell bekreftigelse.

---

## Klinisk bevismateriell fra prøver

Ingen relaterte kliniske prøver er for øyeblikket registrert.

---

## Litteraturbevis

Ingen relatert litteratur er for øyeblikket tilgjengelig.

---

## Informasjon om Taiwan-markedet

Trametinib er for øyeblikket **ikke markedsført** på Taiwan under denne bevissamlingen (0 godkjennelser på fil). Ingen produktlisensar eller godkjente indikasjonsposter er tilgjengelige for uttak.

---

## Cellegiftighet

Trametinib er et antineoplastisk middel (MEK1/2-hemmer brukt i BRAF-mutert melanom), så denne delen gjelder.

| Element | Innhold |
|------|------|
| Cellegiftklassifisering | Målrettet terapi (MEK1/2-hemmer) |
| Risiko for beinmargshemming | Vennligst se pakningsvedlegget for advarsler og forholdsregler |
| Emetogenisitetsklassifisering | Vennligst se pakningsvedlegget for advarsler og forholdsregler |
| Overvåkingselementer | Vennligst se pakningsvedlegget for advarsler og forholdsregler |
| Håndteringsbeskyttelse | Vennligst se pakningsvedlegget for advarsler og forholdsregler |

---

## Sikkerhetshensyn

Vennligst se pakningsvedlegget for sikkerhetsinformasjon.

---

## Konklusjon og neste steg

**Beslutning: Avvent**

**Begrunnelse:**
Koreideremiprediksjonen har ingen støttende kliniske prøver eller litteratur (L5/S0), og ingen kjent mekanistisk vei forbinder MEK-hemming til CHM-relatert netthinnedegenersjon. Den høye TxGNN-poengsum behandles best som en kandidat for modellartifaktgjennomgang snarere enn som en repurposingkandidat.

**For å gå videre, er følgende nødvendig:**
- Preklinisk/mekanistisk bevis som forbinder MAPK-MEK-signalering til CHM-defekt netthinnepatologi (hvis det finnes)
- Uavhengig verifisering av TxGNN-innebyggingspoengsum med modelleringsteamet for å utelukke spuriøs korrelasjon
- Trametinib virkningsmekanisme (MOA) og TFDA/lokale merkedata for å lukke gjeldende datahull (DG001, DG002)

---

## Merknad: Andre forutsagte indikasjoner i denne bevissamlingen

Denne bevissamlingen er en multi-kandidat ("TW-DB08911-multi") utdata, og rangeringer 2–9 viser merkbart bedre støttet (om enn fortsatt tidlig-stadium) signaler — verdt å flagge sammen med hovedprediksjonen ovenfor:

| Rangering | Sykdom | Bevisnivå | Beslutningsstadium | Anbefaling | Sentral støtte |
|------|---------|----------------|-----------------|-----------------|-----------|
| 2 | Ikke-kutant melanom | L2 | S2 | Forskningsspørsmål | Fase 3 DREAMseq + flere Fase 2-studier (BRAF-mutert populasjon, ikke subtypspesifikk) |
| 7 | Acralt lentigøst melanom | L2 | S2 | Forskningsspørsmål | [NCT02083354](https://clinicaltrials.gov/study/NCT02083354) — subtypspesifikk Fase 2 ORR-data, n=77 |
| 9 | Overflatisk spreiende melanom | L3 | S2 | Forskningsspørsmål | Molekylært matchet Fase 2-studie + saksrapporter (respons på hjerne-/korioidalmetastase) |
| 3, 4, 6, 8 | Epithelioid, øyelokk, amelanotisk, lentigo maligna melanom | L4 | S1 | Forskningsspørsmål | Kun saksrapporter/gjennomganger, ingen subtypspesifikke studier |
| 5, 10 | Skrotalt melanom, ballongcellemelanom | L5 | S0 | Avvent | Ingen bevis |

**Viktig forbehold:** alle rangeringer 2–10 er histologisk/anatomisk **undertyper av melanom** — sykdomsrommet trametinib allerede er brukt i (kombinert med dabrafenib) internasjonalt. Disse representerer ikke repurposering til nytt organ på samme måte som koreideremi ville gjøre; de gjenspeiler ekstrapolasjon av undertyper innen samme indikasjon, og deres kliniske verdi avhenger av subtypspesifikk BRAF-mutasjonsprevalens (f.eks. acralt og slimhinne-undertyper har markant lavere BRAF V600-mutasjonsrater enn klassisk kutant melanom).

## Ansvarsfraskrivelse

Dette innholdet er kun til forskningsformål og utgjør ikke medisinsk rådgivning.
Klinisk validering kreves før enhver klinisk anvendelse.

---

