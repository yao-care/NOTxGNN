---
layout: default
title: Evolocumab
parent: Kun modellprediksjon (L5)
nav_order: 169
evidence_level: L5
indication_count: 6
last_modified_at: 2026-11-24
description: "Evolocumab: predikert ny indikasjon Symptomatisk hemofili hos kvinnelige bærere (evidensnivå L5). Opprinnelig indikasjon: Dyslipidemi"
monitor_inn: "EVOLOCUMAB"
predicted_indications: ["symptomatic form of hemophilia in female carriers", "familial apolipoprotein C-II deficiency", "thrombocytopenic purpura", "factor XI deficiency", "hemophilia A with vascular abnormality", "disease of catalytic activity"]
---

# Evolocumab
{: .fs-9 }

Evidensnivå: **L5** | Predikerte indikasjoner: **6** stk.
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

## Evolocumab: Fra hyperkolesterolemi til symptomatisk hemofili hos kvinnelige bærere
{: .text-alpha }

## Oppsummering i én setning

Evolocumab er et monoklonalt antistoff som hemmer PCSK9, opprinnelig brukt til behandling av dyslipidemi og hyperkolesterolemi.
TxGNN-modellen forutsier at legemidlet kan være effektivt mot **symptomatisk hemofili hos kvinnelige bærere**,
men det finnes **0 kliniske studier** og **0 publikasjoner** som støtter denne prediksjonen. Prediksjonen er ren modellbasert og har ingen sannsynlig mekanistisk kobling.

---

## Hurtigoversikt

| Punkt | Innhold |
|------|------|
| Opprinnelig indikasjon | Dyslipidemi; hyperkolesterolemi |
| Predikert ny indikasjon | Symptomatisk hemofili hos kvinnelige bærere |
| TxGNN-prediksjonsscore | 0.9982 |
| Evidensnivå | L5 |
| Markedsstatus i Norge | Markedsført (gyldige tillatelser: 1 av 1) |
| Antall godkjenninger | 1 (gyldige: 1) |
| Anbefalt beslutning | Hold |

---

## Hvorfor er denne prediksjonen (ikke) rimelig?

Ifølge avsnittet «Mechanism of Action» i preparatomtalen som er godkjent av amerikanske FDA (Prescribing Information), for Evolocumab (uoffisiell oversettelse): «Evolokumab er et humant monoklonalt IgG2 rettet mot human proproteinkonvertase subtilisin/kexin type 9 (PCSK9). PCSK9 bindes til lavdensitetslipoproteinreseptoren (LDLR) på overflaten av hepatocytter og fremmer nedbrytning av LDLR i leveren.» Engelsk originaltekst: "Evolocumab is a human monoclonal IgG2 directed against human proprotein convertase subtilisin kexin type 9 (PCSK9). PCSK9 binds to the low-density lipoprotein receptor (LDLR) on the surface of hepatocytes to promote LDLR degradation within the liver." ([DailyMed: Repatha (evolocumab) prescribing information, Amgen USA Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=cd61e902-166d-4aa6-9f3c-a18c1008d07e), versjon av 2026-10-12; hentet 2026-11-19). Ut fra kjent informasjon er evolocumab et PCSK9-hemmende monoklonalt antistoff. Ved å binde PCSK9 øker det tilgjengeligheten av LDL-reseptorer og senker LDL-kolesterol. Effekten er godt dokumentert ved hyperkolesterolemi, inkludert heterozygot og homozygot familiær form.

Symptomer hos kvinnelige hemofilibærere skyldes redusert nivå av koagulasjonsfaktor VIII eller IX som følge av X-bundne varianter. Dette er en mekanisme uten kjent forbindelse til PCSK9 eller lipidmetabolisme. Vi har ikke identifisert noen plausibel mekanistisk kobling.

Den høye TxGNN-scoren (0,9982) er utelukkende en prediksjon fra TxGNN-modellen (dyp læring) og støttes ikke av noen studie eller publikasjon. Den bør derfor tolkes med stor forsiktighet.

### Andre predikerte indikasjoner (til orientering)

| Rang | Predikert indikasjon | TxGNN-score | Vurdering |
|------|------|------|------|
| 2 | Familiær apolipoprotein C-II-mangel | 0,9950 | Kun indirekte biologisk plausibilitet. Evolocumab senker hovedsakelig LDL-C og korrigerer ikke defekten i LPL-aktivering. Nytte er lite sannsynlig. |
| 3 | Trombocytopenisk purpura | 0,9942 | Ingen kjent mekanistisk kobling til PCSK9-hemming. |
| 4 | Faktor XI-mangel | 0,9929 | Evolocumab påvirker ikke koagulasjonskaskaden. |
| 5 | Hemofili A med vaskulær abnormitet | 0,9922 | PCSK9-hemming påvirker ikke produksjon eller funksjon av faktor VIII. |
| 6 | Sykdom med katalytisk aktivitet | 0,9908 | Svært bred ontologikategori, ikke en klinisk indikasjon som kan evalueres. |

Alle har evidensnivå L5 og anbefalingen Hold.

---

## Evidens fra kliniske studier

Foreløpig er ingen relaterte kliniske studier registrert.

---

## Litteraturevidens

Foreløpig finnes ingen relatert litteratur.

---

## Markedsinformasjon for Norge

<!-- licenses:begin -->

| Godkjenningsnummer | Preparatnavn (EMA) | Virkestoff(er) (EMA, engelsk) | Terapeutisk område (EMA, engelsk) | Status |
|------|------|------|------|------|
| EMEA/H/C/003766 | Repatha | Evolocumab | Dyslipidemias; Hypercholesterolemia | Gyldig |

Kilde: EMA – Medicines output (sentralt godkjente legemidler til mennesker); preparatnavn, virkestoffer og terapeutisk område er gjengitt i engelsk original. Nasjonale markedsføringstillatelser (DMP) og veterinærpreparater er ikke med i disse dataene.

<!-- licenses:end -->

Det finnes 1 gyldig godkjenning av 1, og legemidlet er markedsført i Norge.

---

## Sikkerhetsvurderinger

- **Legemiddelinteraksjoner**: Spørringen er gjennomført og ga én farmakologisk oppføring. Den gjelder bindingen til legemidlets målprotein, PCSK9 (proproteinkonvertase subtilisin/kexin type 9), og er ikke en interaksjon med et annet legemiddel. Ingen alvorlighetsgrad er angitt.

For øvrig sikkerhetsinformasjon, se preparatomtalen.

---

## Konklusjon og neste steg

**Beslutning: Hold**

**Begrunnelse:**
Prediksjonen er kun modellbasert (L5), uten kliniske studier eller publikasjoner, og det finnes ingen plausibel mekanistisk kobling mellom PCSK9-hemming og hemofili hos kvinnelige bærere.

<!-- review:begin no-lic-20261124b-evolocumab-1 -->

> **Kontrollrettelse (2026-11-24)**: Opprinnelig sto det: «Produktet har dessuten kun kansellert registrering i Norge.» Fjernet: opplysningen om at godkjenningen(e) er kansellert, stemte ikke med EMAs data om sentrale EU-godkjenninger (2026-11-12), der godkjenningene står som gyldige (Authorised). Oppdaterte antall og statuser for godkjenningene står i hurtigoversikten og i lisenstabellen under markedsinformasjonen. Kilde: [EMA – Medicines output: medicines report](https://www.ema.europa.eu/en/documents/report/medicines-output-medicines-report_en.xlsx); [European Medicines Agency](https://www.ema.europa.eu/).

<!-- review:end no-lic-20261124b-evolocumab-1 -->

**For å gå videre kreves følgende:**
- Innhenting og gjennomgang av preparatomtale (advarsler og kontraindikasjoner), som er en blokkerende datamangel for sikkerhetsscreening
- Detaljerte data om virkningsmekanisme (MOA), f.eks. fra DrugBank
- Et biologisk begrunnet hypotesegrunnlag og prekliniske data før eventuell videre vurdering
- Avklaring av markedsstatus og tilgjengelige administrasjonsveier i Norge

<!-- review:begin log -->

## Kontrollogg

Nedenfor er kontrolloggen for denne siden: opplysninger kontrollert mot EMAs data om sentrale EU-godkjenninger. Rettelser gjelder bare grunnleggende faktaopplysninger; modellens prediksjoner, evidensnivåer og konklusjoner er ikke skrevet om. Setningen om at data om virkningsmekanismen ikke var tilgjengelige, er erstattet med et utdrag fra den oppgitte offisielle preparatomtalen (med uoffisiell oversettelse).

| Kontrolldato | Punkt | Tiltak | Kilde |
|------|------|------|------|
| 2026-11-19 | Setningen «data om virkningsmekanismen er ikke tilgjengelige» erstattet med utdrag fra amerikansk preparatomtale | Setning om manglende data om virkningsmekanismen erstattet med et utdrag med kilde | [DailyMed: Repatha (evolocumab) prescribing information, Amgen USA Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=cd61e902-166d-4aa6-9f3c-a18c1008d07e) |
| 2026-11-24 | Fjernet: «Produktet har dessuten kun kansellert registrering i Norge.» | Rettet | [EMA – Medicines output: medicines report](https://www.ema.europa.eu/en/documents/report/medicines-output-medicines-report_en.xlsx); [European Medicines Agency](https://www.ema.europa.eu/) |

<!-- review:end log -->

## Ansvarsfraskrivelse

Dette innholdet er kun til forskningsformål og utgjør ikke medisinsk rådgivning.
Klinisk validering kreves før enhver klinisk anvendelse.

---

