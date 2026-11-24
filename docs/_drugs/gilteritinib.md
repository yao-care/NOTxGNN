---
layout: default
title: Gilteritinib
parent: Kun modellprediksjon (L5)
nav_order: 187
evidence_level: L5
indication_count: 1
last_modified_at: 2026-11-24
description: "Gilteritinib: predikert ny indikasjon Bulbær polio (evidensnivå L5). Opprinnelig indikasjon: Akutt myeloid leukemi"
monitor_inn: "Gilteritinib"
predicted_indications: ["bulbar polio"]
---

# Gilteritinib
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

## Gilteritinib: Fra akutt myeloid leukemi til bulbær polio
{: .text-alpha }

## Oppsummering i én setning

Gilteritinib er en tyrosinkinasehemmer som opprinnelig brukes til behandling av akutt myeloid leukemi (AML).
TxGNN-modellen forutsier at legemidlet kan være effektivt mot **bulbær polio**,
men det finnes foreløpig **0 kliniske studier** og **0 publikasjoner** som støtter denne retningen. Prediksjonen er rent beregningsbasert.

---

## Hurtigoversikt

| Punkt | Innhold |
|------|------|
| Opprinnelig indikasjon | Akutt myeloid leukemi |
| Predikert ny indikasjon | Bulbær polio |
| TxGNN-prediksjonsscore | 0,9910 |
| Evidensnivå | L5 |
| Markedsstatus i Norge | Markedsført (gyldige tillatelser: 1 av 1) |
| Antall godkjenninger | 1 (gyldige: 1) |
| Anbefalt beslutning | Hold |

---

## Hvorfor er denne prediksjonen rimelig?

Ifølge avsnittet «Mechanism of Action» i preparatomtalen som er godkjent av amerikanske FDA (Prescribing Information), for Gilteritinib (uoffisiell oversettelse): «Gilteritinib er et småmolekyl som hemmer flere reseptortyrosinkinaser, inkludert FMS-lignende tyrosinkinase 3 (FLT3). Gilteritinib viste evne til å hemme FLT3-reseptorsignalering og proliferasjon i celler som eksogent uttrykker FLT3, inkludert FLT3-ITD og mutasjonene i tyrosinkinasedomenet (TKD) FLT3-D835Y og FLT3-ITD-D835Y, og det induserte apoptose i leukemiceller som uttrykker FLT3-ITD.» Engelsk originaltekst: "Gilteritinib is a small molecule that inhibits multiple receptor tyrosine kinases, including FMS-like tyrosine kinase 3 (FLT3). Gilteritinib demonstrated the ability to inhibit FLT3 receptor signaling and proliferation in cells exogenously expressing FLT3 including FLT3-ITD, tyrosine kinase domain mutations (TKD) FLT3-D835Y and FLT3-ITD-D835Y, and it induced apoptosis in leukemic cells expressing FLT3-ITD." ([DailyMed: Xospata (gilteritinib) prescribing information, Astellas Pharma US, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=b5ff59aa-9c0d-49a8-9053-1f179b482383), versjon av 2026-10-01; hentet 2026-11-19). Ut fra kjent informasjon er gilteritinib en hemmer av FLT3 og AXL, og effekten er vist ved residivert/refraktær AML med FLT3-mutasjon. Prekliniske studier viser at legemidlet hemmer FLT3 (villtype og mutert) med IC50 på omtrent 2–5 nM, og at det også binder seg til andre reseptortyrosinkinaser, blant annet NTRK1, MERTK, LTK, ALK, ROS1 og RET.

Bulbær polio er en virusinfeksjon i motoriske nerveceller i hjernestammen, forårsaket av poliovirus. Det er ikke etablert noen mekanistisk sammenheng mellom kinasehemming og polio, for eksempel gjennom vertsfaktorer for virusinntrengning eller -replikasjon, eller gjennom modulering av nevroinflammasjon. Enhver slik kobling vil være spekulativ. Den høye scoren (0,991) er et resultat av modellens grafbaserte prediksjon og er ikke støttet av kliniske eller litterære data.

Det bør også nevnes at de immunsuppressive og myelosuppressive effektene av en kreftrettet kinasehemmer kan være skadelige ved en akutt virusinfeksjon.

---

## Kliniske studier

Foreløpig er det ingen registrerte kliniske studier knyttet til denne indikasjonen.

---

## Litteraturevidens

Foreløpig er det ingen relevant litteratur tilgjengelig.

---

## Markedsinformasjon for Norge

<!-- licenses:begin -->

| Godkjenningsnummer | Preparatnavn (EMA) | Virkestoff(er) (EMA, engelsk) | Terapeutisk område (EMA, engelsk) | Status |
|------|------|------|------|------|
| EMEA/H/C/004752 | Xospata | gilteritinib fumarate | Leukemia, Myeloid, Acute | Gyldig |

Kilde: EMA – Medicines output (sentralt godkjente legemidler til mennesker); preparatnavn, virkestoffer og terapeutisk område er gjengitt i engelsk original. Nasjonale markedsføringstillatelser (DMP) og veterinærpreparater er ikke med i disse dataene.

<!-- licenses:end -->

---

## Cytotoksisitet

| Punkt | Innhold |
|------|------|
| Cytotoksisitetsklassifisering | Målrettet terapi (tyrosinkinasehemmer, FLT3/AXL) |
| Risiko for myelosuppresjon | Se pakningsvedlegget for advarsler og forholdsregler |
| Emetogenisitet | Se pakningsvedlegget for advarsler og forholdsregler |
| Overvåkingspunkter | Se pakningsvedlegget for advarsler og forholdsregler |
| Håndteringsbeskyttelse | Se pakningsvedlegget for advarsler og forholdsregler |

---

## Sikkerhetsvurderinger

- **Legemiddelinteraksjoner**: Spørringen er fullført og ga 8 treff. Alle gjelder farmakologiske målproteiner og ikke interaksjoner med andre legemidler: FLT3, NTRK1, AXL, MERTK, LTK, ALK, ROS1 og RET. Dette viser at gilteritinib er en bredt virkende kinasehemmer, men gir ingen informasjon om klinisk relevante legemiddelinteraksjoner.

Se pakningsvedlegget for øvrig sikkerhetsinformasjon.

---

## Konklusjon og neste steg

**Beslutning: Hold**

**Begrunnelse:**
Prediksjonen er rent beregningsbasert (evidensnivå L5) uten kliniske studier, litteratur eller en etablert mekanistisk sammenheng. Gilteritinibs immunsuppressive profil kan dessuten være skadelig ved akutt virusinfeksjon.

<!-- review:begin no-lic-20261124b-gilteritinib-1 -->

> **Kontrollrettelse (2026-11-24)**: Opprinnelig sto det: «I tillegg er markedsføringsgodkjenningen i Norge kansellert.» Fjernet: opplysningen om at godkjenningen(e) er kansellert, stemte ikke med EMAs data om sentrale EU-godkjenninger (2026-11-12), der godkjenningene står som gyldige (Authorised). Oppdaterte antall og statuser for godkjenningene står i hurtigoversikten og i lisenstabellen under markedsinformasjonen. Kilde: [EMA – Medicines output: medicines report](https://www.ema.europa.eu/en/documents/report/medicines-output-medicines-report_en.xlsx); [European Medicines Agency](https://www.ema.europa.eu/).

<!-- review:end no-lic-20261124b-gilteritinib-1 -->

**For å gå videre kreves følgende:**
- Detaljerte data om virkningsmekanisme (MOA) og en plausibel biologisk hypotese for kinasehemming ved poliovirusinfeksjon
- Prekliniske data (for eksempel in vitro-studier av poliovirusreplikasjon) som kan støtte hypotesen
- Pakningsvedlegg med advarsler og kontraindikasjoner for sikkerhetsscreening
- Avklaring av regulatorisk status

<!-- review:begin no-lic-20261124b-gilteritinib-2 -->

> **Kontrollrettelse (2026-11-24)**: Opprinnelig sto det: «Avklaring av regulatorisk status, siden den eneste godkjenningen er kansellert» Rettet: begrunnelsen om at godkjenningen(e) er kansellert, er tatt ut fordi den ikke stemte med EMAs data om sentrale EU-godkjenninger (2026-11-12), der godkjenningene står som gyldige (Authorised); selve oppfølgingspunktet er beholdt. Oppdaterte antall og statuser for godkjenningene står i hurtigoversikten og i lisenstabellen under markedsinformasjonen. Kilde: [EMA – Medicines output: medicines report](https://www.ema.europa.eu/en/documents/report/medicines-output-medicines-report_en.xlsx); [European Medicines Agency](https://www.ema.europa.eu/).

<!-- review:end no-lic-20261124b-gilteritinib-2 -->

<!-- review:begin log -->

## Kontrollogg

Nedenfor er kontrolloggen for denne siden: opplysninger kontrollert mot EMAs data om sentrale EU-godkjenninger. Rettelser gjelder bare grunnleggende faktaopplysninger; modellens prediksjoner, evidensnivåer og konklusjoner er ikke skrevet om. Setningen om at data om virkningsmekanismen ikke var tilgjengelige, er erstattet med et utdrag fra den oppgitte offisielle preparatomtalen (med uoffisiell oversettelse).

| Kontrolldato | Punkt | Tiltak | Kilde |
|------|------|------|------|
| 2026-11-19 | Setningen «data om virkningsmekanismen er ikke tilgjengelige» erstattet med utdrag fra amerikansk preparatomtale | Setning om manglende data om virkningsmekanismen erstattet med et utdrag med kilde | [DailyMed: Xospata (gilteritinib) prescribing information, Astellas Pharma US, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=b5ff59aa-9c0d-49a8-9053-1f179b482383) |
| 2026-11-24 | Fjernet: «I tillegg er markedsføringsgodkjenningen i Norge kansellert.» | Rettet | [EMA – Medicines output: medicines report](https://www.ema.europa.eu/en/documents/report/medicines-output-medicines-report_en.xlsx); [European Medicines Agency](https://www.ema.europa.eu/) |
| 2026-11-24 | Rettet: «Avklaring av regulatorisk status, siden den eneste godkjenningen er kansellert» → «Avklaring av regulatorisk status» | Rettet | [EMA – Medicines output: medicines report](https://www.ema.europa.eu/en/documents/report/medicines-output-medicines-report_en.xlsx); [European Medicines Agency](https://www.ema.europa.eu/) |

<!-- review:end log -->

## Ansvarsfraskrivelse

Dette innholdet er kun til forskningsformål og utgjør ikke medisinsk rådgivning.
Klinisk validering kreves før enhver klinisk anvendelse.

---

