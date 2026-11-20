---
layout: default
title: Fosaprepitant
parent: Kun modellprediksjon (L5)
nav_order: 180
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-28
description: "Fosaprepitant: predikert ny indikasjon Nefrogent syndrom med uhensiktsmessig antidiurese (evidensnivå L5). Opprinnelig indikasjon: Oppkast"
monitor_inn: "FOSAPREPITANT"
predicted_indications: ["nephrogenic syndrome of inappropriate antidiuresis", "pneumocystosis", "leprosy", "Cryptococcal meningitis", "multiple endocrine neoplasia", "intracranial abscess", "retinitis", "Plasmodium falciparum malaria", "echinococcus granulosus infectious disease", "hyperargininemia"]
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

<div id="pharmacist" markdown="1">

## Farmasøytens vurderingsrapport

</div>

## Fosaprepitant: Fra kvalme og oppkast ved kreft til nefrogent syndrom med uhensiktsmessig antidiurese
{: .text-alpha }

## Oppsummering i én setning

Fosaprepitant er en forløper (prodrug) til aprepitant og var opprinnelig godkjent mot oppkast og kvalme i forbindelse med kreftbehandling. TxGNN-modellen predikerer at legemidlet kan ha effekt ved **nefrogent syndrom med uhensiktsmessig antidiurese (NSIAD)**, men dette er en ren modellprediksjon: det finnes **ingen kliniske studier** og **ingen publikasjoner** som støtter denne retningen.

---

## Hurtigoversikt

| Punkt | Innhold |
|------|------|
| Opprinnelig indikasjon | Oppkast; kreft (kvalme og oppkast ved kreftbehandling) |
| Predikert ny indikasjon | Nefrogent syndrom med uhensiktsmessig antidiurese |
| TxGNN-prediksjonsscore | 0,9992 |
| Evidensnivå | L5 |
| Markedsstatus i Norge | Markedsført (gyldige tillatelser: 1 av 1) |
| Antall godkjenninger | 1 (gyldige: 1) |
| Antall tillatelser | 1 (0 gyldige, 1 kansellert) |
| Anbefalt beslutning | Hold |

---

## Hvorfor er denne prediksjonen (ikke) rimelig?

Ifølge avsnittet «Mechanism of Action» i preparatomtalen som er godkjent av amerikanske FDA (Prescribing Information), for Fosaprepitant (uoffisiell oversettelse): «Fosaprepitant er et prodrug av aprepitant, og de antiemetiske effektene kan følgelig tilskrives aprepitant. Aprepitant er en selektiv høyaffinitetsantagonist av humane substans P/nevrokinin 1 (NK-1)-reseptorer. Aprepitant har liten eller ingen affinitet for serotonin- (5-HT 3 ), dopamin- og kortikosteroidreseptorer, som er målene for eksisterende behandlinger av kjemoterapiindusert kvalme og oppkast (CINV).» Engelsk originaltekst: "Fosaprepitant is a prodrug of aprepitant and accordingly, its antiemetic effects are attributable to aprepitant. Aprepitant is a selective high-affinity antagonist of human substance P/neurokinin 1 (NK-1) receptors. Aprepitant has little or no affinity for serotonin (5-HT 3 ), dopamine, and corticosteroid receptors, the targets of existing therapies for chemotherapy-induced nausea and vomiting (CINV)." ([DailyMed: Navitrux (fosaprepitant) prescribing information, AVYXA Pharma, LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=a41b7c3a-1376-43a7-b5b9-6ba2eba1e169), versjon av 2026-07-29; hentet 2026-11-19). Basert på kjent informasjon er fosaprepitant en forløper til aprepitant, en antagonist mot NK1-reseptoren (substans P-reseptoren). Effekten ved kjemoterapiindusert kvalme og oppkast er godt etablert.

NSIAD skyldes derimot aktiverende (gain-of-function) mutasjoner i vasopressin V2-reseptoren (AVPR2). Dette er en annen reseptorvei enn NK1-antagonisme, og det er ikke påvist noen mekanistisk kobling mellom de to. Den høye scoren er en grafbasert prediksjon uten støtte i kliniske data eller litteratur, og må tolkes med stor forsiktighet.

Blant de ti høyest rangerte prediksjonene (blant annet pneumocystose, lepra, kryptokokkmeningitt, malaria, ekinokokkose og hyperargininemi) mangler de fleste både mekanistisk begrunnelse og studier. Det eneste unntaket er **retinitt** (rangert som nr. 7, score 0,9968), der det finnes én prekliniske studie som gir en plausibel, men indirekte mekanisme (se under).

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

Produsent: Merck Sharp & Dohme B.V. Legemidlet er markedsført i Norge, og 1 av 1 markedsføringstillatelser er gyldig.

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
Prediksjonen for nefrogent syndrom med uhensiktsmessig antidiurese har evidensnivå L5: den bygger kun på modellscore, uten kliniske studier, litteratur eller en plausibel mekanisme. Legemidlet er markedsført i Norge, og 1 av 1 markedsføringstillatelser er gyldig.

**For å gå videre kreves følgende:**
- Hentet og analysert preparatomtale (advarsler og kontraindikasjoner) fra legemiddelmyndighetene
- Fullstendige mekanismedata (MOA) fra DrugBank
- Mekanistisk og preklinisk validering av sammenhengen mellom NK1-antagonisme og AVPR2-drevet NSIAD
- Vurdering av om retinitt (preklinisk støtte, evidensnivå L4) bør prioriteres som en mer lovende forskningsretning
- Avklaring av administrasjonsvei og formuleringskompatibilitet for en eventuell ny indikasjon

<!-- review:begin log -->

## Kontrollogg

Nedenfor er gjennomgangsloggen for denne siden. Setningen om at data om virkningsmekanismen ikke var tilgjengelige, er erstattet med et utdrag fra den oppgitte offisielle preparatomtalen (med uoffisiell oversettelse); modellprediksjoner, evidensnivåer og konklusjoner er ikke omskrevet.

| Kontrolldato | Punkt | Tiltak | Kilde |
|------|------|------|------|
| 2026-11-19 | Setningen «data om virkningsmekanismen er ikke tilgjengelige» erstattet med utdrag fra amerikansk preparatomtale | Setning om manglende data om virkningsmekanismen erstattet med et utdrag med kilde | [DailyMed: Navitrux (fosaprepitant) prescribing information, AVYXA Pharma, LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=a41b7c3a-1376-43a7-b5b9-6ba2eba1e169) |

<!-- review:end log -->

## Ansvarsfraskrivelse

Dette innholdet er kun til forskningsformål og utgjør ikke medisinsk rådgivning.
Klinisk validering kreves før enhver klinisk anvendelse.

---

