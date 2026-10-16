---
layout: default
title: Fosaprepitant
parent: Kun modellprediksjon (L5)
nav_order: 180
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-15
description: "Fosaprepitant: predikert ny indikasjon Nefrogent syndrom med uhensiktsmessig antidiurese (evidensnivå L5). Opprinnelig indikasjon: Oppkast"
---

# Fosaprepitant
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

# Fosaprepitant: Fra kvalme og oppkast ved kreft til nefrogent syndrom med uhensiktsmessig antidiurese

## Oppsummering i én setning

Fosaprepitant er en forløper (prodrug) til aprepitant og var opprinnelig godkjent mot oppkast og kvalme i forbindelse med kreftbehandling. TxGNN-modellen predikerer at legemidlet kan ha effekt ved **nefrogent syndrom med uhensiktsmessig antidiurese (NSIAD)**, men dette er en ren modellprediksjon: det finnes **ingen kliniske studier** og **ingen publikasjoner** som støtter denne retningen.

---

## Hurtigoversikt

| Punkt | Innhold |
|------|------|
| Opprinnelig indikasjon | Oppkast; kreft (kvalme og oppkast ved kreftbehandling) |
| Predikert ny indikasjon | Nefrogent syndrom med uhensiktsmessig antidiurese |
| TxGNN-prediksjonsscore | 99,92 % |
| Evidensnivå | L5 |
| Markedsstatus i Norge | Kun tilbakekalt/avregistrert (ingen gyldige markedsføringstillatelser) |
| Antall tillatelser | 1 (0 gyldige, 1 kansellert) |
| Anbefalt beslutning | Hold |

---

## Hvorfor er denne prediksjonen (ikke) rimelig?

Detaljerte data om virkningsmekanisme er foreløpig ikke tilgjengelige i det innsamlede datagrunnlaget. Basert på kjent informasjon er fosaprepitant en forløper til aprepitant, en antagonist mot NK1-reseptoren (substans P-reseptoren). Effekten ved kjemoterapiindusert kvalme og oppkast er godt etablert.

NSIAD skyldes derimot aktiverende (gain-of-function) mutasjoner i vasopressin V2-reseptoren (AVPR2). Dette er en annen reseptorvei enn NK1-antagonisme, og det er ikke påvist noen mekanistisk kobling mellom de to. Den høye scoren er en grafbasert prediksjon uten støtte i kliniske data eller litteratur, og må tolkes med stor forsiktighet.

Blant de ti høyest rangerte prediksjonene (blant annet pneumocystose, lepra, kryptokokkmeningitt, malaria, ekinokokkose og hyperargininemi) mangler de fleste både mekanistisk begrunnelse og studier. Det eneste unntaket er **retinitt** (rangert som nr. 7, score 99,68 %), der det finnes én prekliniske studie som gir en plausibel, men indirekte mekanisme (se under).

---

## Klinisk studieevidens

Det er for øyeblikket ingen relaterte kliniske studier registrert for den predikerte indikasjonen.

---

## Litteraturevidens

Det er for øyeblikket ingen relevant litteratur tilgjengelig for den predikerte indikasjonen (NSIAD).

For sammenligning er det for den alternative prediksjonen retinitt identifisert én preklinisk publikasjon:

| PMID | År | Type | Tidsskrift | Hovedfunn |
|------|-----|------|------|---------|
| [32058829](https://pubmed.ncbi.nlm.nih.gov/32058829/) | 2021 | Preklinisk (mus) | Ocular Immunology and Inflammation | Fosaprepitant blokkerte UVR-B-indusert NK1-reseptoruttrykk i øyevev, både i det eksponerte og det ueksponerte øyet |

Dette er indirekte, prekliniske data om øyeinflammasjon/-skade, ikke kliniske data hos pasienter med retinitt.

---

## Markedsinformasjon for Norge

| Tillatelsesnummer | Produktnavn | Doseringsform | Godkjent indikasjon |
|---------|------|------|-----------|
| EMEA/H/C/000743 | Ivemend | Ikke oppgitt | Oppkast; kreft (status: kansellert) |

Produsent: Merck Sharp & Dohme B.V. Det finnes ingen gyldige tillatelser for tiden.

---

## Cytotoksisitet

Fosaprepitant er et antiemetikum (NK1-antagonist) og ikke et cytostatikum. Legemidlet brukes imidlertid i støttebehandling ved kreftbehandling. Cytotoksisitetsvurdering er derfor ikke relevant, og seksjonen utelates.

---

## Sikkerhetsvurderinger

- **Kontraindikasjoner fra kunnskapsgrafen (ikke fra preparatomtale):** Leversvikt er registrert som kontraindikasjon i TxGNN-kunnskapsgrafen (PrimeKG).
- **Legemiddelinteraksjoner:** Totalt 100 interaksjoner er identifisert. Blant de første 20 som er oppført:
  - **Alvorlige (Major):** eliglustat, naloksegol
  - **Moderate:** blant andre deksametason, hydrokortison, betametason, budesonid, triamcinolon (kortikosteroider), klaritromycin, cimetidin, rabeprazol, lansoprazol, mikonazol, pioglitazon, saksagliptin, glimepirid, nateglinid, alosetron, dronabinol og naldemedin

For øvrig sikkerhetsinformasjon, se preparatomtalen.

---

## Konklusjon og neste steg

**Beslutning: Hold**

**Begrunnelse:**
Prediksjonen for NSIAD har evidensnivå L5: den bygger kun på modellscore, uten kliniske studier, litteratur eller en plausibel mekanisme. I tillegg har legemidlet ingen gyldig markedsføringstillatelse i Norge.

**For å gå videre kreves følgende:**
- Hentet og analysert preparatomtale (advarsler og kontraindikasjoner) fra legemiddelmyndighetene
- Fullstendige mekanismedata (MOA) fra DrugBank
- Mekanistisk og preklinisk validering av sammenhengen mellom NK1-antagonisme og AVPR2-drevet NSIAD
- Vurdering av om retinitt (preklinisk støtte, evidensnivå L4) bør prioriteres som en mer lovende forskningsretning
- Avklaring av administrasjonsvei og formuleringskompatibilitet for en eventuell ny indikasjon
## Ansvarsfraskrivelse

Dette innholdet er kun til forskningsformål og utgjør ikke medisinsk rådgivning.
Klinisk validering kreves før enhver klinisk anvendelse.

---

