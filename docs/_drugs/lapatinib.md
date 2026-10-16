---
layout: default
title: Lapatinib
parent: Kun modellprediksjon (L5)
nav_order: 232
evidence_level: L5
indication_count: 1
last_modified_at: 2026-10-15
description: "Lapatinib: predikert ny indikasjon Dermatofibrosarcoma protuberans (evidensnivå L5). Opprinnelig indikasjon: Brystneoplasmer (brystkreft)"
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

# Lapatinib: Fra brystkreft til dermatofibrosarcoma protuberans

## Oppsummering i én setning

Lapatinib er en tyrosinkinasehemmer som opprinnelig ble godkjent for behandling av brystkreft (brystneoplasmer). TxGNN-modellen forutsier at legemidlet kan ha effekt mot **dermatofibrosarcoma protuberans (DFSP)**, men det finnes foreløpig **ingen registrerte kliniske studier** og **ingen publikasjoner** som støtter denne retningen i de innsamlede dataene. Prediksjonen bygger kun på modellens score.

---

## Hurtigoversikt

| Punkt | Innhold |
|------|------|
| Opprinnelig indikasjon | Brystneoplasmer (brystkreft) |
| Predikert ny indikasjon | Dermatofibrosarcoma protuberans |
| TxGNN-prediksjonsscore | 99,30 % |
| Evidensnivå | L5 |
| Markedsstatus i Norge | Kun avregistrert (ingen gyldig markedsføringstillatelse) |
| Antall tillatelser | 1 (0 gyldige, 1 avregistrert) |
| Anbefalt beslutning | Hold |

---

## Hvorfor er denne prediksjonen rimelig?

Data om virkningsmekanisme (MOA) er ikke tilgjengelig i de innsamlede dataene. Ut fra allment kjent informasjon er lapatinib en dobbel hemmer av EGFR og HER2 (tyrosinkinasereseptorer), og effekten er dokumentert ved HER2-positiv brystkreft.

Koblingen til DFSP er svak. DFSP drives hovedsakelig av COL1A1-PDGFB-fusjonen, som gir konstitutiv aktivering av PDGFR-beta, og behandles med imatinib, en PDGFR-hemmer. En direkte mekanistisk sammenheng mellom EGFR/HER2-hemming og DFSP er derfor ikke påvist i de foreliggende dataene. Mulige forklaringer, som delte nedstrøms signalveier (PI3K/AKT, MAPK) eller off-target kinaseaktivitet, er spekulative og må verifiseres mot primærkilder.

Den høye scoren gjenspeiler trolig nærhet i kunnskapsgrafen (felles kinasemål eller assosiasjoner til beslektede sarkomer/svulster) snarere enn validert biologi.

---

## Kliniske studier

Foreløpig er ingen relaterte kliniske studier registrert.

---

## Litteraturevidens

Foreløpig er ingen relatert litteratur tilgjengelig.

---

## Markedsinformasjon for Norge

| Tillatelsesnummer | Produktnavn | Doseringsform | Godkjent indikasjon |
|---------|------|------|-----------|
| EMEA/H/C/000795 | Tyverb | – | Brystneoplasmer |

Merk: Tillatelsen er avregistrert. Det finnes ingen gyldig tillatelse i datagrunnlaget.

---

## Cytotoksisitet

| Punkt | Innhold |
|------|------|
| Cytotoksisitetsklassifisering | Målrettet terapi (tyrosinkinasehemmer mot EGFR/HER2) |
| Myelosuppresjonsrisiko | Se pakningsvedlegg for advarsler og forsiktighetsregler |
| Emetogenisitetsklassifisering | Se pakningsvedlegg for advarsler og forsiktighetsregler |
| Overvåkingspunkter | Se pakningsvedlegg. Kunnskapsgrafen peker på lever, hjerte (QT, hjertesvikt) og lunger (se under) |
| Håndteringsbeskyttelse | Se pakningsvedlegg for advarsler og forsiktighetsregler |

---

## Sikkerhetsvurderinger

Data fra pakningsvedlegg (advarsler og kontraindikasjoner) mangler. Følgende er hentet fra andre kilder.

**Sykdomsassosiasjoner fra kunnskapsgrafen (TxGNN/PrimeKG, ikke preparatomtale):** Grafen knytter lapatinib til kontraindikasjon ved følgende tilstander:
- Langt QT-syndrom (inkludert familiær form) og torsades de pointes
- Leversvikt og legemiddelindusert leverskade
- Kaliummangel
- Interstitiell lungesykdom
- Hjertesvikt

Disse er kun signaler fra en kunnskapsgraf og må bekreftes mot offisiell preparatomtale.

**Legemiddelinteraksjoner:** Totalt 100 interaksjoner er registrert (DDInter). Et utvalg:
- **Alvorlige (Major):** loperamid, klaritromycin
- **Moderate:** famotidin, ranitidin, cimetidin, omeprazol, rabeprazol, deksлансоprazol, hydrokortison, deksametason, betametason, triamcinolon, budesonid, pioglitazon, saksagliptin, aprepitant, bisakodyl, pikosulfat og polyetylenglykol

---

## Konklusjon og neste steg

**Beslutning: Hold**

**Begrunnelse:**
Prediksjonen støttes kun av en høy TxGNN-score (evidensnivå L5), uten kliniske studier eller publikasjoner. Den kjente mekanismen (EGFR/HER2-hemming) passer dårlig med DFSPs PDGFR-drevne biologi, og standardbehandlingen er imatinib. I tillegg er lapatinibs eneste norske tillatelse avregistrert.

**For å gå videre kreves følgende:**
- Gjennomgang av primærlitteratur og prekliniske data om EGFR/HER2-signalering i DFSP
- Mekanismedata (MOA) fra DrugBank
- Pakningsvedlegg fra DMP (advarsler og kontraindikasjoner) for sikkerhetsscreening
- Avklaring av markedsstatus og tilgjengelighet i Norge
- Vurdering av ruteforenlighet og likhet med opprinnelig indikasjon (fortsatt uavklart)
## Ansvarsfraskrivelse

Dette innholdet er kun til forskningsformål og utgjør ikke medisinsk rådgivning.
Klinisk validering kreves før enhver klinisk anvendelse.

---

