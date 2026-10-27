---
layout: default
title: Oxybutynin
parent: Kun modellprediksjon (L5)
nav_order: 302
evidence_level: L5
indication_count: 3
last_modified_at: 2026-10-15
description: "Oxybutynin: predikert ny indikasjon Restless legs-syndrom (evidensnivå L5). Opprinnelig indikasjon: Urge-inkontinens (Urinary Incontinence, Urge)"
monitor_inn: "OXYBUTYNIN"
predicted_indications: ["restless legs syndrome", "gastroduodenitis", "peptic ulcer disease"]
---

# Oxybutynin
{: .fs-9 }

Evidensnivå: **L5** | Predikerte indikasjoner: **3** stk.
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

## Oksybutynin: Fra urge-inkontinens til restless legs-syndrom
{: .text-alpha }

## Oppsummering i én setning

Oksybutynin er et antimuskarint legemiddel som opprinnelig brukes mot urge-inkontinens (overaktiv blære).
TxGNN-modellen predikerer at det kan ha effekt på **restless legs-syndrom** (høyest rangert), men det finnes **ingen kliniske studier og ingen publikasjoner** som støtter denne retningen.
Prediksjonen er kun modellbasert (evidensnivå L5).

---

## Hurtigoversikt

| Punkt | Innhold |
|------|------|
| Opprinnelig indikasjon | Urge-inkontinens (Urinary Incontinence, Urge) |
| Predikert ny indikasjon | Restless legs-syndrom |
| TxGNN-prediksjonsscore | 99,74 % |
| Evidensnivå | L5 |
| Markedsstatus i Norge | Kun trukket tilbake (ingen gyldig tillatelse) |
| Antall tillatelser | 1 (trukket tilbake) |
| Anbefalt beslutning | Hold |

---

## Hvorfor er denne prediksjonen (ikke) rimelig?

Data om detaljert virkningsmekanisme er foreløpig ikke tilgjengelig i de innsamlede dataene. Oksybutynin er kjent som en muskarin antagonist med antikolinerg og direkte glattmuskelavslappende (antispasmodisk) effekt, og effekten ved urge-inkontinens er etablert.

Restless legs-syndrom (RLS) er hovedsakelig knyttet til jernmangel i hjernen og dysfunksjon i dopaminsystemet. Antikolinerg aktivitet er ikke en etablert behandlingsvei, og antikolinergika kan tvert imot forverre RLS-symptomer eller søvnkvalitet. Det finnes derfor ingen mekanistisk kobling mellom oksybutynin og RLS som støttes av dataene.

Den høye TxGNN-scoren (0,997) er en ren modellprediksjon og bør tolkes med forsiktighet.

**Andre predikerte indikasjoner i dataene:**

| Rang | Sykdom | TxGNN-score | Evidensnivå | Vurdering |
|------|------|------|------|------|
| 2 | Gastroduodenitt | 99,62 % | L5 | Antispasmodisk lindring er mulig, men adresserer ikke underliggende årsaker (H. pylori, NSAID, syre). Ingen studier eller litteratur. |
| 3 | Magesår (peptisk ulkussykdom) | 99,31 % | L4 | Antikolinergika har historisk vært brukt, men er i stor grad erstattet av protonpumpehemmere, H2-blokkere og H. pylori-eradikering. |

---

## Klinisk studiedata

Foreløpig er ingen relevante kliniske studier registrert for restless legs-syndrom (og heller ikke for de to andre predikerte indikasjonene).

---

## Litteraturevidens

For den høyest rangerte indikasjonen (restless legs-syndrom) finnes foreløpig ingen relevant litteratur.

Følgende litteratur er knyttet til rang 3 (magesår), og er gjengitt for fullstendighetens skyld:

| PMID | År | Type | Tidsskrift | Hovedfunn |
|------|-----|------|------|---------|
| [2360335](https://pubmed.ncbi.nlm.nih.gov/2360335/) | 1990 | Kasuistikk | DICP: The Annals of Pharmacotherapy | Beskriver oksybutynin-indusert refluksøsofagitt, trolig på grunn av redusert tonus i nedre øsofagussfinkter. Et sikkerhetssignal mot bruk i øvre mage-tarmkanal. |
| [4380481](https://pubmed.ncbi.nlm.nih.gov/4380481/) | 1965 | Oversikt/farmakologi | Archives Internationales de Pharmacodynamie et de Thérapie | Beskriver oksybutynin som et muskulotropt antispasmodisk middel med moderat antikolinerg virkning. |
| [14173506](https://pubmed.ncbi.nlm.nih.gov/14173506/) | 1964 | Klinisk vurdering (ukontrollert, historisk) | Current Therapeutic Research | Klinisk vurdering av oksybutynin ved gastrointestinale sykdommer. Ingen kontrollerte data. |

---

## Markedsinformasjon for Norge

| Tillatelsesnummer | Produktnavn | Doseringsform | Godkjent indikasjon |
|---------|------|------|-----------|
| EMEA/H/C/000532 | Kentera (tidligere Oxybutynin Nicobrand) | Ikke oppgitt | Urge-inkontinens (status: trukket tilbake) |

---

## Sikkerhetsvurderinger

Pakningsvedlegg med advarsler og kontraindikasjoner var ikke tilgjengelig i de innsamlede dataene. Se pakningsvedlegget for fullstendig sikkerhetsinformasjon.

**Kontraindikasjoner fra kunnskapsgrafen (PrimeKG, ikke preparatomtale):**
Følgende sykdommer er koblet til oksybutynin som mulige kontraindikasjoner i kunnskapsgrafen. De bør verifiseres mot offisiell preparatomtale:
- **Øye:** trangvinklet glaukom
- **Nevromuskulært:** myasthenia gravis
- **Mage-tarm:** paralytisk ileus, tarmobstruksjon, toksisk megakolon, ulcerøs kolitt/inflammatorisk tarmsykdom, gastroøsofageal reflukssykdom, øsofagitt, hiatushernie
- **Urinveier:** blærehalsobstruksjon, godartet prostataforstørrelse
- **Hjerte og kar:** hypertensjon, koronarsykdom, hjerteledningssykdom, plutselig hjertestans
- **Andre:** nyresykdom, leversykdom, gallblæresykdom, hypertyreose/Graves sykdom

**Legemiddelinteraksjoner:** Totalt 100 interaksjoner er funnet; et utvalg av de første 20 vises her.
- **Alvorlig (Major):** kaliumsitrat, kaliumklorid
- **Moderat:** andre antikolinergika (hyoscyamin, atropin, glykopyrronium, klidinium, disyklomin, trospium, mepenzolat, metskopolamin, propantelin), opioider (morfin, opium, loperamid, eluxadolin), metoklopramid, aprepitant og pramlintid

Merk at oksybutynin som antikolinergikum kan gi additive antikolinerge effekter ved kombinasjon med andre antikolinergika, og at kalium i fast form kan gi økt risiko for skade i mage-tarmkanalen på grunn av redusert motilitet.

---

## Konklusjon og neste steg

**Beslutning: Hold**

**Begrunnelse:**
Prediksjonen for restless legs-syndrom støttes kun av en datamodell (L5), uten kliniske studier eller litteratur, og den farmakologiske sammenhengen er svak, med mulig forverring av symptomer. I tillegg er den eneste norske/europeiske tillatelsen trukket tilbake.

**For å gå videre kreves følgende:**
- Detaljerte data om virkningsmekanisme (MOA) fra DrugBank
- Pakningsvedlegg med advarsler og kontraindikasjoner for sikkerhetsscreening (blokkerende datagap)
- Prekliniske eller mekanistiske studier som kan underbygge en kobling til RLS
- Litteratursøk og registersøk spesifikt for oksybutynin ved RLS
- Avklaring av tilgjengelige administrasjonsveier og markedsstatus i Norge
## Ansvarsfraskrivelse

Dette innholdet er kun til forskningsformål og utgjør ikke medisinsk rådgivning.
Klinisk validering kreves før enhver klinisk anvendelse.

---

