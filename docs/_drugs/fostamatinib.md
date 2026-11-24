---
layout: default
title: Fostamatinib
parent: Kun modellprediksjon (L5)
nav_order: 181
evidence_level: L5
indication_count: 2
last_modified_at: 2026-11-24
description: "Fostamatinib: predikert ny indikasjon Autosomal trombocytopeni med normale blodplater (evidensnivå L5). Opprinnelig indikasjon: Trombocytopeni"
monitor_inn: "Fostamatinib"
predicted_indications: ["autosomal thrombocytopenia with normal platelets", "non-syndromic esophageal malformation"]
---

# Fostamatinib
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

## Fostamatinib: Fra trombocytopeni til autosomal trombocytopeni med normale blodplater
{: .text-alpha }

## Oppsummering

Fostamatinib er et legemiddel som opprinnelig brukes mot **trombocytopeni** (lavt antall blodplater).
TxGNN-modellen forutsier at det kan ha effekt ved **autosomal trombocytopeni med normale blodplater**,
men det finnes foreløpig **ingen kliniske studier** og **ingen publikasjoner** som støtter denne prediksjonen.

---

## Hurtigoversikt

| Punkt | Innhold |
|------|------|
| Opprinnelig indikasjon | Trombocytopeni |
| Predikert ny indikasjon | Autosomal trombocytopeni med normale blodplater |
| TxGNN-prediksjonsscore | 0.9945 |
| Evidensnivå | L5 |
| Markedsstatus i Norge | Markedsført (gyldige tillatelser: 1 av 1) |
| Antall godkjenninger | 1 (gyldige: 1) |
| Anbefalt beslutning | Hold |

---

## Hvorfor er denne prediksjonen rimelig (eller ikke)?

Ifølge avsnittet «Mechanism of Action» i preparatomtalen som er godkjent av amerikanske FDA (Prescribing Information), for Fostamatinib (uoffisiell oversettelse): «Fostamatinib er en tyrosinkinasehemmer med påvist aktivitet mot miltens tyrosinkinase (SYK). Hovedmetabolitten av fostamatinib, R406, hemmer signaltransduksjon fra Fc-aktiverende reseptorer og B-cellereseptoren.» Engelsk originaltekst: "Fostamatinib is a tyrosine kinase inhibitor with demonstrated activity against spleen tyrosine kinase (SYK). The major metabolite of fostamatinib, R406, inhibits signal transduction of Fc-activating receptors and B-cell receptor." ([DailyMed: Tavalisse (fostamatinib) prescribing information, Rigel Pharmaceuticals, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=21149cc3-049b-43e2-b141-c9499160556c), versjon av 2025-11-05; hentet 2026-11-19). Fostamatinib er kjent som en hemmer av milttyrosinkinase (SYK). Den aktive metabolitten R406 reduserer nedbrytningen av blodplater som skjer via Fc-reseptorer i makrofager. Dette er grunnlaget for bruk ved immun trombocytopeni (ITP).

Den predikerte sykdommen er en arvelig (autosomal) tilstand, som vanligvis henger sammen med genetiske feil i produksjon eller funksjon av blodplater, og ikke med immunmediert nedbrytning. SYK-hemming forventes derfor ikke å ramme den underliggende patologien. Den høye scoren kommer fra TxGNN-modellen (deep learning) og kan gjenspeile likheter modellen har lært mellom relaterte sykdommer, ikke biologisk evidens.

Samlet sett er den mekanistiske koblingen spekulativ og ikke støttet av dataene.

Den nest rangerte prediksjonen, **ikke-syndromisk øsofagusmisdannelse** (score 0,9905), har ingen plausibel mekanistisk kobling. Slike medfødte strukturelle utviklingsfeil lar seg neppe korrigere med SYK-hemming. Heller ikke her finnes studier eller litteratur.

---

## Evidens fra kliniske studier

Det er foreløpig ingen relaterte kliniske studier registrert.

---

## Litteraturevidens

Det finnes foreløpig ingen relatert litteratur.

---

## Informasjon om det norske markedet

<!-- licenses:begin -->

| Godkjenningsnummer | Preparatnavn (EMA) | Virkestoff(er) (EMA, engelsk) | Terapeutisk område (EMA, engelsk) | Status |
|------|------|------|------|------|
| EMEA/H/C/005012 | Tavlesse | Fostamatinib disodium | Thrombocytopenia | Gyldig |

Kilde: EMA – Medicines output (sentralt godkjente legemidler til mennesker); preparatnavn, virkestoffer og terapeutisk område er gjengitt i engelsk original. Nasjonale markedsføringstillatelser (DMP) og veterinærpreparater er ikke med i disse dataene.

<!-- licenses:end -->

Merk: Det finnes 1 gyldig godkjenning av 1 i Norge, og legemidlet er markedsført.

---

## Sikkerhetsvurderinger

### Legemiddelinteraksjoner

Interaksjonssøket er gjennomført og ga 100 registrerte interaksjoner. Et utvalg er vist under.

- **Alvorlig (Major):** Klaritromycin
- **Moderat (Moderate):** blant annet rabeprazol, omeprazol, dekslansoprazol, cimetidin, hydrokortison, deksametason, betametason, budesonid, triamcinolon, aprepitant, alosetron, alvimopan, dolasetron, dronabinol, eliglustat, empagliflozin, loperamid, pioglitazon og morfin

Øvrige sikkerhetsopplysninger finnes i preparatomtalen (pakningsvedlegget).

---

## Konklusjon og neste steg

**Beslutning: Hold**

**Begrunnelse:**
Prediksjonene bygger kun på modellscore (evidensnivå L5), uten kliniske studier eller litteratur. Den mekanistiske koblingen til en arvelig blodplatesykdom og til en medfødt øsofagusmisdannelse er svak eller fraværende.

<!-- review:begin no-lic-20261124b-fostamatinib-1 -->

> **Kontrollrettelse (2026-11-24)**: Opprinnelig sto det: «I tillegg er den eneste norske godkjenningen kansellert.» Fjernet: opplysningen om at godkjenningen(e) er kansellert, stemte ikke med EMAs data om sentrale EU-godkjenninger (2026-11-12), der godkjenningene står som gyldige (Authorised). Oppdaterte antall og statuser for godkjenningene står i hurtigoversikten og i lisenstabellen under markedsinformasjonen. Kilde: [EMA – Medicines output: medicines report](https://www.ema.europa.eu/en/documents/report/medicines-output-medicines-report_en.xlsx); [European Medicines Agency](https://www.ema.europa.eu/).

<!-- review:end no-lic-20261124b-fostamatinib-1 -->

**For å gå videre kreves følgende:**
- Data om virkningsmekanisme (MOA) fra DrugBank
- Advarsler og kontraindikasjoner fra preparatomtalen, som er nødvendig for sikkerhetsscreening
- Prekliniske eller mekanistiske studier som kan vise at SYK-hemming er relevant for den predikerte sykdommen

<!-- review:begin no-lic-20261124b-fostamatinib-2 -->

> **Kontrollrettelse (2026-11-24)**: Opprinnelig sto det: «Avklaring av hvorfor godkjenningen i Norge ble kansellert, og om en ny godkjenning er aktuell» Fjernet: oppfølgingspunktet bygde på at godkjenningen(e) er kansellert, noe som ikke stemte med EMAs data om sentrale EU-godkjenninger (2026-11-12), der godkjenningene står som gyldige (Authorised). Oppdaterte antall og statuser for godkjenningene står i hurtigoversikten og i lisenstabellen under markedsinformasjonen. Kilde: [EMA – Medicines output: medicines report](https://www.ema.europa.eu/en/documents/report/medicines-output-medicines-report_en.xlsx); [European Medicines Agency](https://www.ema.europa.eu/).

<!-- review:end no-lic-20261124b-fostamatinib-2 -->

<!-- review:begin log -->

## Kontrollogg

Nedenfor er kontrolloggen for denne siden: opplysninger kontrollert mot EMAs data om sentrale EU-godkjenninger. Rettelser gjelder bare grunnleggende faktaopplysninger; modellens prediksjoner, evidensnivåer og konklusjoner er ikke skrevet om. Setningen om at data om virkningsmekanismen ikke var tilgjengelige, er erstattet med et utdrag fra den oppgitte offisielle preparatomtalen (med uoffisiell oversettelse).

| Kontrolldato | Punkt | Tiltak | Kilde |
|------|------|------|------|
| 2026-11-19 | Setningen «data om virkningsmekanismen er ikke tilgjengelige» erstattet med utdrag fra amerikansk preparatomtale | Setning om manglende data om virkningsmekanismen erstattet med et utdrag med kilde | [DailyMed: Tavalisse (fostamatinib) prescribing information, Rigel Pharmaceuticals, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=21149cc3-049b-43e2-b141-c9499160556c) |
| 2026-11-24 | Fjernet: «I tillegg er den eneste norske godkjenningen kansellert.» | Rettet | [EMA – Medicines output: medicines report](https://www.ema.europa.eu/en/documents/report/medicines-output-medicines-report_en.xlsx); [European Medicines Agency](https://www.ema.europa.eu/) |
| 2026-11-24 | Fjernet: «Avklaring av hvorfor godkjenningen i Norge ble kansellert, og om en ny godkjenning er aktuell» | Rettet | [EMA – Medicines output: medicines report](https://www.ema.europa.eu/en/documents/report/medicines-output-medicines-report_en.xlsx); [European Medicines Agency](https://www.ema.europa.eu/) |

<!-- review:end log -->

## Ansvarsfraskrivelse

Dette innholdet er kun til forskningsformål og utgjør ikke medisinsk rådgivning.
Klinisk validering kreves før enhver klinisk anvendelse.

---

