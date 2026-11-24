---
layout: default
title: Octreotide
parent: Kun modellprediksjon (L5)
nav_order: 293
evidence_level: L5
indication_count: 2
last_modified_at: 2026-11-24
description: "Octreotide: predikert ny indikasjon Vulvær inversert follikulær keratose (evidensnivå L5). Opprinnelig indikasjon: Akromegali"
monitor_inn: "Octreotide"
predicted_indications: ["vulvar inverted follicular keratosis", "seborrheic keratosis"]
---

# Octreotide
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

## Oktreotid: Fra akromegali til vulvær inversert follikulær keratose
{: .text-alpha }

## Oppsummering

Oktreotid er en somatostatinanalog som opprinnelig brukes til behandling av akromegali. TxGNN-modellen predikerer at legemidlet kan ha effekt ved **vulvær inversert follikulær keratose**. Det finnes foreløpig **ingen kliniske studier** og **ingen publikasjoner** som støtter denne retningen, så prediksjonen er rent beregningsbasert.

---

## Hurtigoversikt

| Punkt | Innhold |
|------|------|
| Opprinnelig indikasjon | Akromegali |
| Predikert ny indikasjon | Vulvær inversert follikulær keratose |
| TxGNN-prediksjonsscore | 0,9958 |
| Evidensnivå | L5 |
| Markedsstatus i Norge | Markedsført (gyldige tillatelser: 1 av 1) |
| Antall godkjenninger | 1 (gyldige: 1) |
| Anbefalt beslutning | Hold |

---

## Hvorfor kan denne prediksjonen være rimelig?

Oktreotid er en somatostatinanalog (peptid) som virker på somatostatinreseptorene SSTR2, SSTR3 og SSTR5. Gjennom disse hemmer det blant annet utskillelsen av veksthormon og IGF-1, noe som er grunnlaget for bruken ved akromegali. Ifølge avsnittet «Mechanism of Action» i preparatomtalen som er godkjent av amerikanske FDA (Prescribing Information), for Octreotide (uoffisiell oversettelse): «Sandostatin injeksjonsvæske har farmakologiske virkninger som ligner det naturlige hormonet somatostatin. Det er en enda mer potent hemmer av GH, glukagon og insulin enn somatostatin. […] I kraft av disse farmakologiske virkningene har oktreotid blitt brukt til å behandle symptomene forbundet med metastatiske karsinoide tumorer (flushing og diaré) og VIP-utskillende adenomer (vandig diaré).» Engelsk originaltekst: "Sandostatin Injection exerts pharmacologic actions similar to the natural hormone, somatostatin. It is an even more potent inhibitor of GH, glucagon, and insulin than somatostatin. […] By virtue of these pharmacological actions, octreotide has been used to treat the symptoms associated with metastatic carcinoid tumors (flushing and diarrhea), and VIP secreting adenomas (watery diarrhea)." ([DailyMed: Sandostatin (octreotide acetate) prescribing information, Novartis Pharmaceuticals Corporation](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=4e2c9856-1836-49f0-9472-4dbeeb408f39), versjon av 2026-07-22; hentet 2026-11-19).

Det er ikke påvist noen etablert mekanistisk sammenheng mellom akromegali og vulvær inversert follikulær keratose. En teoretisk kobling forutsetter at somatostatinreseptorer uttrykkes i follikulære keratinocyttlesjoner, eller at IGF-1/vekstfaktorsignalering spiller en rolle i lesjonenes proliferasjon. Ingen av delene er støttet av de tilgjengelige dataene.

Den høye TxGNN-scoren (0,9958) er kun en beregningsmessig prediksjon uten støtte fra kliniske data eller litteratur. Den bør ses som et hypotesegenererende signal, ikke som en etablert kandidat for reposisjonering.

Modellen predikerer også **seboreisk keratose** (score 0,9955, evidensnivå L5, anbefaling Hold). Heller ikke her finnes det studier eller litteratur. En hypotetisk forklaring er modulering av IGF-1/vekstfaktorsignalering i godartede epidermale proliferasjoner, men ingen data kobler oktreotid til denne tilstanden.

---

## Klinisk studieevidens

Det er for øyeblikket ingen relaterte kliniske studier registrert.

---

## Litteraturevidens

Det er for øyeblikket ingen relatert litteratur tilgjengelig.

---

## Markedsinformasjon for Norge

<!-- licenses:begin -->

| Godkjenningsnummer | Preparatnavn (EMA) | Virkestoff(er) (EMA, engelsk) | Terapeutisk område (EMA, engelsk) | Status |
|------|------|------|------|------|
| EMEA/H/C/006322 | Oczyesa | octreotide hydrochloride | Acromegaly | Gyldig |

Kilde: EMA – Medicines output (sentralt godkjente legemidler til mennesker); preparatnavn, virkestoffer og terapeutisk område er gjengitt i engelsk original. Nasjonale markedsføringstillatelser (DMP) og veterinærpreparater er ikke med i disse dataene.

<!-- licenses:end -->

Oktreotid er markedsført, og det finnes 1 gyldig godkjenning av 1 i de sammenstilte dataene.

---

## Sikkerhetsvurderinger

Det foreligger ingen opplysninger fra preparatomtale i dataene. Følgende er hentet fra en kunnskapsgraf (PrimeKG) og er ikke basert på godkjent produkttekst, og må derfor verifiseres mot preparatomtalen.

- **Mulige kontraindikasjoner/risikotilstander (kunnskapsgraf):** hyperglykemi, hypoglykemi, diabetes mellitus, diabetisk ketoacidose, hypotyreose (inkludert myxødem og kongenital hypotyreose), levercirrhose, leversykdom, gallblæresykdom, gallestein (kolelitiasis, kolecystolitiasis, koledokolitiasis), ileus, tarmobstruksjon, hjertestans, hjerteledningsforstyrrelser, nyresvikt, uremi og vitamin B12-mangel.
- **Legemiddelinteraksjoner:** Spørringen er fullført, men har ikke identifisert noen legemiddelinteraksjoner av klinisk nivå. Resultatene beskriver kun farmakologisk binding til somatostatinreseptorene SSTR2, SSTR3 og SSTR5.

Se preparatomtalen for fullstendig sikkerhetsinformasjon.

---

## Konklusjon og neste steg

**Beslutning: Hold**

**Begrunnelse:**
Prediksjonen bygger kun på en modellscore uten kliniske studier, litteratur eller en påvist mekanistisk kobling. I tillegg mangler sikkerhetsdata fra preparatomtale.

<!-- review:begin no-lic-20261124b-octreotide-1 -->

> **Kontrollrettelse (2026-11-24)**: Opprinnelig sto det: «I tillegg er den eneste norske/europeiske godkjenningen kansellert, og sikkerhetsdata fra preparatomtale mangler.» Rettet: opplysningen om at godkjenningen(e) er kansellert, er tatt ut fordi den ikke stemte med EMAs data om sentrale EU-godkjenninger (2026-11-12), der godkjenningene står som gyldige (Authorised); resten av setningen er uendret. Oppdaterte antall og statuser for godkjenningene står i hurtigoversikten og i lisenstabellen under markedsinformasjonen. Kilde: [EMA – Medicines output: medicines report](https://www.ema.europa.eu/en/documents/report/medicines-output-medicines-report_en.xlsx); [European Medicines Agency](https://www.ema.europa.eu/).

<!-- review:end no-lic-20261124b-octreotide-1 -->

**For å gå videre kreves følgende:**
- Data om virkningsmekanisme (MOA) fra legemiddeldatabasen
- Preparatomtale med advarsler og kontraindikasjoner
- Dokumentasjon på somatostatinreseptoruttrykk (SSTR2/SSTR5) eller IGF-1-involvering i vulvær inversert follikulær keratose og seboreisk keratose
- Prekliniske eller første kliniske studier som kan støtte hypotesen
- Vurdering av administrasjonsvei og formulering (topisk versus injeksjon), som ikke er avklart

<!-- review:begin log -->

## Kontrollogg

Nedenfor er kontrolloggen for denne siden: opplysninger kontrollert mot EMAs data om sentrale EU-godkjenninger. Rettelser gjelder bare grunnleggende faktaopplysninger; modellens prediksjoner, evidensnivåer og konklusjoner er ikke skrevet om. Setningen om at data om virkningsmekanismen ikke var tilgjengelige, er erstattet med et utdrag fra den oppgitte offisielle preparatomtalen (med uoffisiell oversettelse).

| Kontrolldato | Punkt | Tiltak | Kilde |
|------|------|------|------|
| 2026-11-19 | Setningen «data om virkningsmekanismen er ikke tilgjengelige» erstattet med utdrag fra amerikansk preparatomtale | Setning om manglende data om virkningsmekanismen erstattet med et utdrag med kilde | [DailyMed: Sandostatin (octreotide acetate) prescribing information, Novartis Pharmaceuticals Corporation](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=4e2c9856-1836-49f0-9472-4dbeeb408f39) |
| 2026-11-24 | Rettet: «I tillegg er den eneste norske/europeiske godkjenningen kansellert, og sikkerhetsdata fra preparatomtale mangler.» → «I tillegg mangler sikkerhetsdata fra preparatomtale.» | Rettet | [EMA – Medicines output: medicines report](https://www.ema.europa.eu/en/documents/report/medicines-output-medicines-report_en.xlsx); [European Medicines Agency](https://www.ema.europa.eu/) |

<!-- review:end log -->

## Ansvarsfraskrivelse

Dette innholdet er kun til forskningsformål og utgjør ikke medisinsk rådgivning.
Klinisk validering kreves før enhver klinisk anvendelse.

---

