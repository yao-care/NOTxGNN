---
layout: default
title: Salmeterol
parent: Kun modellprediksjon (L5)
nav_order: 376
evidence_level: L5
indication_count: 3
last_modified_at: 2026-11-24
monitor_inn: "salmeterol"
predicted_indications: ["respiratory malformation", "Rienhoff syndrome", "atopic eczema"]
description: "Salmeterol: predikert ny indikasjon Luftveismisdannelse (respiratory malformation) (evidensnivå L5). Sentrale EU-godkjenninger (EMA): 1 (gyldige: 1)"
---

# Salmeterol
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

## Salmeterol: Luftveismisdannelse (respiratory malformation)
{: .text-alpha }

## Oppsummering i én setning

Salmeterol er en langtidsvirkende beta2-agonist som brukes til behandling av astma. TxGNN-modellen forutsier at legemidlet kan være aktuelt for **luftveismisdannelse (respiratory malformation)**, men dette er kun en beregningsmessig prediksjon: de to registrerte kliniske studiene og litteraturen som er funnet, studerer ikke denne sykdommen direkte.

## Hurtigoversikt

| Punkt | Innhold |
|------|------|
| Opprinnelig indikasjon | Ikke registrert i de lokale dataene |
| Predikert ny indikasjon | Luftveismisdannelse (respiratory malformation) |
| TxGNN-prediksjonsscore | 0.9991 |
| Evidensnivå | L5 |
| Markedsstatus i Norge | Markedsført (gyldige tillatelser: 1 av 1) |
| Antall godkjenninger | 1 (gyldige: 1) |
| Anbefalt beslutning | Avvent (Hold) |

## Hvorfor er denne prediksjonen rimelig?

Ifølge avsnittet «Mechanism of Action» i preparatomtalen som er godkjent av amerikanske FDA (Prescribing Information), for Salmeterol (uoffisiell oversettelse): «Salmeterol er en selektiv LABA. In vitro-studier viser at salmeterol er minst 50 ganger mer selektivt for beta 2 -adrenoseptorer enn salbutamol. Selv om beta 2 -adrenoseptorer er de dominerende adrenerge reseptorene i glatt muskulatur i bronkiene og beta 1 -adrenoseptorer er de dominerende reseptorene i hjertet, finnes det også beta 2 -adrenoseptorer i det humane hjertet, som utgjør 10% til 50% av de totale beta-adrenoseptorene.» Engelsk originaltekst: "Salmeterol is a selective LABA. In vitro studies show salmeterol to be at least 50 times more selective for beta 2 -adrenoceptors than albuterol. Although beta 2 -adrenoceptors are the predominant adrenergic receptors in bronchial smooth muscle and beta 1 -adrenoceptors are the predominant receptors in the heart, there are also beta 2 -adrenoceptors in the human heart comprising 10% to 50% of the total beta-adrenoceptors." ([DailyMed: Serevent Diskus (salmeterol xinafoate) prescribing information, GlaxoSmithKline LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=12d9728e-6b5c-4aee-bfb0-745e542ed2e4), versjon av 2022-10-10; hentet 2026-11-19). Salmeterol tilhører klassen langtidsvirkende beta2-adrenerge agonister, som gir bronkodilatasjon via beta2-reseptorer i luftveiene.

Det finnes ingen tydelig mekanistisk kobling mellom salmeterol og luftveismisdannelse. Den høye scoren gjenspeiler trolig delt annotasjon med luftveissykdommer og ciliedysfunksjon. En spekulativ tanke er at beta2-agonister kan øke cilienes slagfrekvens, noe som kan være relevant ved primær ciliær dyskinesi eller cystisk fibrose. Dette er ikke en etablert bruk av salmeterol ved misdannelser, og en strukturell misdannelse lar seg i utgangspunktet ikke behandle medikamentelt på samme måte som funksjonelle luftveislidelser.

Siden ingen av de siterte studiene direkte omhandler luftveismisdannelse, settes evidensnivået til L5.

## Kliniske studier

| Studienummer | Fase | Status | Antall deltakere | Hovedfunn |
|---------|------|------|------|---------|
| [NCT00005110](https://clinicaltrials.gov/study/NCT00005110) | Ikke angitt | Suspendert | Ikke oppgitt | Langtidseffekt av salmeterol versus albuterol ved cystisk fibrose over 6 måneder; ingen resultater tilgjengelige. Cystisk fibrose er ikke en luftveismisdannelse. |
| [NCT01681979](https://clinicaltrials.gov/study/NCT01681979) | Ikke angitt | Fullført | 1 | Astmabehandling i svangerskap og forekomst av uheldige svangerskapsutfall; omhandler ikke behandling av luftveismisdannelse. |

Ingen av studiene undersøker luftveismisdannelse direkte.

## Litteraturevidens

| PMID | År | Type | Tidsskrift | Hovedfunn |
|------|-----|------|------|---------|
| [34902004](https://pubmed.ncbi.nlm.nih.gov/34902004/) | 2022 | Randomisert klinisk studie | JAMA Pediatrics | Inhalerte kortikosteroider alene og i kombinasjon med langtidsvirkende beta2-agonister ved nedsatt lungefunksjon hos prematurt fødte barn. |
| [15293609](https://pubmed.ncbi.nlm.nih.gov/15293609/) | 2004 | Klinisk studie | European Respiratory Journal | Salmeterol og ventilatorisk respons under anstrengelse ved KOLS. |
| [20528601](https://pubmed.ncbi.nlm.nih.gov/20528601/) | 2010 | Oversikt | Journal of Asthma | Oversikt over budesonid/formoterol ved vedvarende astma. |
| [26229457](https://pubmed.ncbi.nlm.nih.gov/26229457/) | 2015 | Oversikt | Int J Chron Obstruct Pulmon Dis | Dobbel bronkodilatasjon med indakaterol-glykopyrronium ved KOLS. |
| [22608352](https://pubmed.ncbi.nlm.nih.gov/22608352/) | 2012 | Observasjonsstudie | Respiratory Medicine | Redusert cilieslag i nasale celler fra KOLS-pasienter. |
| [30021361](https://pubmed.ncbi.nlm.nih.gov/30021361/) | 2018 | In vitro | Biomedicine & Pharmacotherapy | Timianekstrakt øker cilieslagfrekvensen i celler fra KOLS-pasienter. |
| [37327273](https://pubmed.ncbi.nlm.nih.gov/37327273/) | 2023 | Kasuistikk | Medicine | Pulmonal aspergillose behandlet med omalizumab. |
| [20703071](https://pubmed.ncbi.nlm.nih.gov/20703071/) | 2010 | Kasuistikk | Arerugi | Primær ciliær dyskinesi som tidligere var behandlet som astma. |

Ingen av publikasjonene omhandler luftveismisdannelse direkte.

## Informasjon om det norske markedet

<!-- licenses:begin -->

| Godkjenningsnummer | Preparatnavn (EMA) | Virkestoff(er) (EMA, engelsk) | Terapeutisk område (EMA, engelsk) | Status |
|------|------|------|------|------|
| EMEA/H/C/004881 | Seffalair Spiromax | fluticasone propionate; salmeterol xinafoate | Asthma | Gyldig |

Kilde: EMA – Medicines output (sentralt godkjente legemidler til mennesker); preparatnavn, virkestoffer og terapeutisk område er gjengitt i engelsk original. Nasjonale markedsføringstillatelser (DMP) og veterinærpreparater er ikke med i disse dataene.

<!-- licenses:end -->

## Sikkerhetsvurderinger

**Legemiddelinteraksjoner** (utvalg fra de innsamlede dataene, i alt 600 registrerte interaksjoner):
- **Alvorlig:** klaritromycin
- **Moderat:** akarbose, isometepten, famotidin, adrenalin, albiglutid, alogliptin, kanagliflozin, klorpropamid, dapagliflozin, dietylpropion, dolasetron, dulaglutid, empagliflozin
- **Mindre:** hydrokortison, triamcinolon, deksametason, beklometason, betametason, budesonid

Se preparatomtalen for øvrig sikkerhetsinformasjon, inkludert advarsler og kontraindikasjoner.

## Konklusjon og neste steg

**Beslutning: Avvent (Hold)**

**Begrunnelse:**
Prediksjonen bygger kun på en beregningsmessig modell med høy score (0,9991). Det finnes ingen studier som direkte undersøker salmeterol ved luftveismisdannelse, og ingen klar mekanistisk kobling. Evidensnivået er L5.

**For å gå videre kreves følgende:**
- Data om virkningsmekanisme (MOA) og en avklaring av om en mekanistisk kobling finnes
- Preparatomtalens advarsler og kontraindikasjoner, som mangler i de innsamlede dataene
- Klinisk eller prekliniske studier som direkte undersøker salmeterol ved luftveismisdannelse
- En klinisk avgrensning av hvilke undergrupper (for eksempel funksjonelle ciliedefekter) som eventuelt kan være aktuelle

<!-- review:begin log -->

## Kontrollogg

Nedenfor er kontrolloggen for denne siden: opplysninger kontrollert mot EMAs data om sentrale EU-godkjenninger. Rettelser gjelder bare grunnleggende faktaopplysninger; modellens prediksjoner, evidensnivåer og konklusjoner er ikke skrevet om. Setningen om at data om virkningsmekanismen ikke var tilgjengelige, er erstattet med et utdrag fra den oppgitte offisielle preparatomtalen (med uoffisiell oversettelse).

| Kontrolldato | Punkt | Tiltak | Kilde |
|------|------|------|------|
| 2026-10-31 | Fjernet: «Siden bruken i stor grad overlapper med eksisterende praksis, og fordi preparatet i dag kun har en avregistrert godkjenning i Norge, bør bru» | Finnes ikke lenger etter at rapporten ble generert på nytt (2026-11-12: rapporten ble generert på nytt i november 2026 og inneholder ikke lenger opplysningen; tidligere: Rettet (revidert 2026-11-24; tidligere versjon er lagret i posten)) | [EMA – Medicines output: medicines report](https://www.ema.europa.eu/en/documents/report/medicines-output-medicines-report_en.xlsx); [European Medicines Agency](https://www.ema.europa.eu/) |
| 2026-11-19 | Setningen «data om virkningsmekanismen er ikke tilgjengelige» erstattet med utdrag fra amerikansk preparatomtale | Setning om manglende data om virkningsmekanismen erstattet med et utdrag med kilde | [DailyMed: Serevent Diskus (salmeterol xinafoate) prescribing information, GlaxoSmithKline LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=12d9728e-6b5c-4aee-bfb0-745e542ed2e4) |

<!-- review:end log -->

## Ansvarsfraskrivelse

Dette innholdet er kun til forskningsformål og utgjør ikke medisinsk rådgivning.
Klinisk validering kreves før enhver klinisk anvendelse.

---

