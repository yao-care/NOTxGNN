---
layout: default
title: Alpelisib
parent: Kun modellprediksjon (L5)
nav_order: 27
evidence_level: L5
indication_count: 1
last_modified_at: 2026-11-12
description: "Alpelisib: predikert ny indikasjon Pulmonal hypertensjon (evidensnivå L5). Opprinnelig indikasjon: Brystkreft (Breast Neoplasms)"
monitor_inn: "ALPELISIB"
predicted_indications: ["pulmonary hypertension"]
---

# Alpelisib
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

## Alpelisib: Fra brystkreft til pulmonal hypertensjon
{: .text-alpha }

## Oppsummering

Alpelisib er en PI3Kα-selektiv hemmer som opprinnelig ble brukt til behandling av brystkreft.
TxGNN-modellen forutsier at legemidlet kan ha effekt ved **pulmonal hypertensjon**, men dette er foreløpig kun en beregningsmessig prediksjon: det finnes **0 kliniske studier** og **1 publikasjon** (en kasuistikk om en lungebivirkning, ikke en terapeutisk effekt).

---

## Hurtigoversikt

| Punkt | Innhold |
|------|------|
| Opprinnelig indikasjon | Brystkreft (Breast Neoplasms) |
| Predikert ny indikasjon | Pulmonal hypertensjon |
| TxGNN-prediksjonsscore | 0,9903 |
| Evidensnivå | L5 |
| Markedsstatus i Norge | Markedsført (gyldige tillatelser: 1 av 1) |
| Antall godkjenninger | 1 (gyldige: 1) |
| Antall autorisasjoner | 1 (0 gyldige, 1 opphevet) |
| Anbefalt beslutning | Hold |

---

## Hvorfor er denne prediksjonen rimelig?

Ifølge avsnittet «Mechanism of Action» i preparatomtalen som er godkjent av amerikanske FDA (Prescribing Information), for Alpelisib (uoffisiell oversettelse): «Alpelisib er en hemmer av fosfatidylinositol-3-kinase (PI3K) med hemmende aktivitet hovedsakelig mot PI3Kα. Funksjonsfremmende mutasjoner i genet som koder for den katalytiske α-subenheten av PI3K (PIK3CA), fører til aktivering av PI3Kα og Akt-signalering, cellulær transformasjon og tumordannelse i in vitro- og in vivo-modeller.» Engelsk originaltekst: "Alpelisib is an inhibitor of phosphatidylinositol-3-kinase (PI3K) with inhibitory activity predominantly against PI3Kα. Gain-of-function mutations in the gene encoding the catalytic α-subunit of PI3K (PIK3CA) lead to activation of PI3Kα and Akt-signaling, cellular transformation and the generation of tumors in in vitro and in vivo models." ([DailyMed: Piqray (alpelisib) prescribing information, Novartis Pharmaceuticals Corporation](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=b20b4e18-7a4b-4500-a08f-06c6dab0ee5b), versjon av 2026-10-28; hentet 2026-11-19). Alpelisib er kjent som en PI3Kα-selektiv hemmer, og effekten ved brystkreft er etablert.

Mekanistisk er det biologisk plausibelt at hemming av PI3K/AKT/mTOR-signalveien kan påvirke pulmonal vaskulær remodellering, blant annet proliferasjon av glatte muskelceller i lungearteriene og endotel-dysfunksjon. Dette er imidlertid en teoretisk kobling uten støtte fra kliniske data.

Den eneste tilgjengelige publikasjonen beskriver en alpelisib-indusert interstitiell lungesykdom hos en pasient med avansert brystkreft. Dette tyder på en mulig lungeskade, ikke en terapeutisk nytte, og omhandler ikke pulmonal hypertensjon. Den høye TxGNN-scoren bør derfor tolkes med stor forsiktighet.

---

## Litteraturevidens

| PMID | År | Type | Tidsskrift | Hovedfunn |
|------|-----|------|------|---------|
| [35730191](https://pubmed.ncbi.nlm.nih.gov/35730191/) | 2023 | Kasuistikk | J Oncol Pharm Pract | Alpelisib-indusert interstitiell lungesykdom hos en pasient med avansert brystkreft |

---

## Informasjon om det norske markedet

| Autorisasjonsnummer | Produktnavn | Legemiddelform | Godkjent indikasjon |
|---------|------|------|-----------|
| EMEA/H/C/004804 | Piqray | Ikke oppgitt | Brystkreft (status: opphevet) |

---

## Cytotoksisitet

| Punkt | Innhold |
|------|------|
| Klassifisering | Målrettet terapi (PI3Kα-hemmer) |
| Risiko for myelosuppresjon | Se pakningsvedlegget for advarsler og forsiktighetsregler |
| Emetogenisitet | Se pakningsvedlegget for advarsler og forsiktighetsregler |
| Overvåkingspunkter | Se pakningsvedlegget for advarsler og forsiktighetsregler |
| Håndtering og beskyttelse | Se pakningsvedlegget for advarsler og forsiktighetsregler |

---

## Sikkerhetsvurderinger

- **Legemiddelinteraksjoner:** Det er registrert 100 interaksjoner i de innsamlede dataene. De 20 som er vist er alle av moderat alvorlighetsgrad (kilde: DDInter). Hovedsakelig gjelder de antidiabetika, som kan påvirke blodsukkeret sammen med alpelisib:
  - Acarbose, metformin, pioglitazon, acetoheksamid, klorpropamid, glimepirid, glipizid
  - GLP-1-agonister: albiglutid, dulaglutid, eksenatid
  - DPP-4-hemmer: alogliptin
  - SGLT2-hemmere: kanagliflozin, dapagliflozin, empagliflozin, ertugliflozin
  - Andre: alosetron, bupropion, deksametason, dronabinol, fidaksomicin

- **Signal om lungeskade:** Den tilgjengelige litteraturen beskriver interstitiell lungesykdom som en bivirkning, noe som er særlig relevant ved vurdering av en lungeindikasjon.

Ytterligere informasjon om advarsler og kontraindikasjoner finnes i pakningsvedlegget.

---

## Konklusjon og neste steg

**Beslutning: Hold**

**Begrunnelse:**
Prediksjonen er kun modellbasert (evidensnivå L5) uten kliniske studier, og den eneste tilgjengelige litteraturen peker mot mulig lungeskade snarere enn nytte.

<!-- review:begin no-lic-20261106-alpelisib-1 -->

> **Kontrollrettelse (2026-11-06)**: Opprinnelig sto det: «Prediksjonen er kun modellbasert (evidensnivå L5) uten kliniske studier, og den eneste tilgjengelige litteraturen peker mot mulig lungeskade snarere enn nytte. I tillegg er den eneste norske autorisasjonen opphevet.» Fjernet: opplysningen om at godkjenningene er avregistrert eller at ingen gyldig godkjenning finnes, stemte ikke med EMAs data om sentrale EU-godkjenninger (2026-11-06). Antall godkjenninger i dataene: 1, hvorav gyldige: 1; oppdaterte tall står i hurtigoversikten og i markedsinformasjonen. Kilde: [EMA – Medicines output: medicines report](https://www.ema.europa.eu/en/documents/report/medicines-output-medicines-report_en.xlsx); [European Medicines Agency](https://www.ema.europa.eu/).

<!-- review:end no-lic-20261106-alpelisib-1 -->

**For å gå videre kreves følgende:**
- Prekliniske data (f.eks. dyremodeller for pulmonal hypertensjon) som viser nytte og sikkerhet av PI3Kα-hemming i lungekar
- Detaljerte data om virkningsmekanisme
- Gjennomgang av sikkerhetsinformasjon (advarsler og kontraindikasjoner) fra pakningsvedlegget, med særlig vekt på interstitiell lungesykdom og blodsukkerforstyrrelser
- Vurdering av formuleringsmuligheter og administrasjonsvei for den nye indikasjonen
- Avklaring av markedsstatus og tilgjengelighet i Norge

<!-- review:begin log -->

## Kontrollogg

Nedenfor er kontrolloggen for denne siden: opplysninger kontrollert mot EMAs data om sentrale EU-godkjenninger. Rettelser gjelder bare grunnleggende faktaopplysninger; modellens prediksjoner, evidensnivåer og konklusjoner er ikke skrevet om. Setningen om at data om virkningsmekanismen ikke var tilgjengelige, er erstattet med et utdrag fra den oppgitte offisielle preparatomtalen (med uoffisiell oversettelse).

| Kontrolldato | Punkt | Tiltak | Kilde |
|------|------|------|------|
| 2026-11-06 | Fjernet: «I tillegg er den eneste norske autorisasjonen opphevet» | Rettet | [EMA – Medicines output: medicines report](https://www.ema.europa.eu/en/documents/report/medicines-output-medicines-report_en.xlsx); [European Medicines Agency](https://www.ema.europa.eu/) |
| 2026-11-19 | Setningen «data om virkningsmekanismen er ikke tilgjengelige» erstattet med utdrag fra amerikansk preparatomtale | Setning om manglende data om virkningsmekanismen erstattet med et utdrag med kilde | [DailyMed: Piqray (alpelisib) prescribing information, Novartis Pharmaceuticals Corporation](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=b20b4e18-7a4b-4500-a08f-06c6dab0ee5b) |

<!-- review:end log -->

## Ansvarsfraskrivelse

Dette innholdet er kun til forskningsformål og utgjør ikke medisinsk rådgivning.
Klinisk validering kreves før enhver klinisk anvendelse.

---

