---
layout: default
title: Alglucosidase Alfa
parent: Kun modellprediksjon (L5)
nav_order: 24
evidence_level: L5
indication_count: 8
last_modified_at: 2026-11-24
description: "Alglucosidase Alfa: predikert ny indikasjon Voksen polyglukosanlegemesykdom (evidensnivå L5). Opprinnelig indikasjon: Glykogenlagringssykdom type II"
monitor_inn: "ALGLUCOSIDASE ALFA"
predicted_indications: ["adult polyglucosan body disease", "congenital entropion", "congenital ectropion", "congenital Horner syndrome (disease)", "ptosis-vocal cord paralysis syndrome", "camptodactyly, myopia, and fibrosis of the medial rectus muscle of eye", "epiblepharon", "ptosis-strabismus-ectopic pupils syndrome"]
---

# Alglucosidase Alfa
{: .fs-9 }

Evidensnivå: **L5** | Predikerte indikasjoner: **8** stk.
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

## Alglukosidase alfa: Fra Glykogenlagringssykdom type II til Voksen polyglukosanlegemesykdom
{: .text-alpha }

## Oppsummering

Alglukosidase alfa er et rekombinant enzym (syre-alfa-glukosidase) som opprinnelig brukes som enzymerstatningsbehandling ved glykogenlagringssykdom type II (Pompes sykdom).
TxGNN-modellen forutsier at legemidlet kan ha effekt ved **voksen polyglukosanlegemesykdom** (adult polyglucosan body disease), men det finnes for øyeblikket **ingen kliniske studier** og **ingen publikasjoner** som støtter denne retningen. Prediksjonen er kun modellbasert.

---

## Hurtigoversikt

| Punkt | Innhold |
|------|------|
| Opprinnelig indikasjon | Glykogenlagringssykdom type II |
| Predikert ny indikasjon | Voksen polyglukosanlegemesykdom |
| TxGNN-prediksjonsscore | 0,9947 |
| Evidensnivå | L5 |
| Markedsstatus i Norge | Markedsført (gyldige tillatelser: 1 av 1) |
| Antall godkjenninger | 1 (gyldige: 1) |
| Anbefalt beslutning | Hold (avvent) |

---

## Hvorfor er denne prediksjonen rimelig (eller ikke)?

Ifølge avsnittet «Mechanism of Action» i preparatomtalen som er godkjent av amerikanske FDA (Prescribing Information), for Alglucosidase Alfa (uoffisiell oversettelse): «Pompes sykdom (sur maltase-mangel, glykogenlagringssykdom type II, GSD II, glykogenose type II) er en arvelig sykdom i glykogenmetabolismen forårsaket av fravær av eller uttalt mangel på det lysosomale enzymet GAA. Alglukosidase alfa gir en eksogen kilde til GAA.» Engelsk originaltekst: "Pompe disease (acid maltase deficiency, glycogen storage disease type II, GSD II, glycogenosis type II) is an inherited disorder of glycogen metabolism caused by the absence or marked deficiency of the lysosomal enzyme GAA. Alglucosidase alfa provides an exogenous source of GAA." ([DailyMed: Lumizyme (alglucosidase alfa) prescribing information, Genzyme Corporation](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=d6bfbc45-2d34-439e-8aad-59ee2d53d4df), versjon av 2025-01-10; hentet 2026-11-19). Ut fra kjent informasjon er alglukosidase alfa et rekombinant syre-alfa-glukosidase-enzym som bryter ned lysosomalt glykogen via alfa-1,4- og alfa-1,6-bindinger. Effekten ved Pompes sykdom er dokumentert.

Voksen polyglukosanlegemesykdom skyldes mangel på glykogenforgreningsenzym (GBE1), som gir opphopning av dårlig forgrenet, uløselig polyglukosan i nervevev. Det finnes dermed en konseptuell kobling gjennom felles glykogenlagringspatologi. Koblingen er imidlertid svak av to grunner:

- Polyglukosan hoper seg hovedsakelig opp i cytosol i nevroner og astrocytter, ikke i lysosomer, som er enzymets målområde.
- Enzymet krysser ikke blod-hjerne-barrieren effektivt.

Den høye TxGNN-scoren er derfor kun en prediksjon uten støtte i kliniske data.

---

## Kliniske studier

Foreløpig finnes ingen registrerte kliniske studier for denne indikasjonen.

---

## Litteraturevidens

Foreløpig er det ingen relevant litteratur tilgjengelig.

---

## Markedsinformasjon for Norge

<!-- licenses:begin -->

| Godkjenningsnummer | Preparatnavn (EMA) | Virkestoff(er) (EMA, engelsk) | Terapeutisk område (EMA, engelsk) | Status |
|------|------|------|------|------|
| EMEA/H/C/000636 | Myozyme | alglucosidase alfa | Glycogen Storage Disease Type II | Gyldig |

Kilde: EMA – Medicines output (sentralt godkjente legemidler til mennesker); preparatnavn, virkestoffer og terapeutisk område er gjengitt i engelsk original. Nasjonale markedsføringstillatelser (DMP) og veterinærpreparater er ikke med i disse dataene.

<!-- licenses:end -->

Legemidlet er markedsført, og 1 av 1 markedsføringstillatelse er gyldig.

---

## Andre predikerte indikasjoner

Modellen ga ytterligere ni prediksjoner. Ingen av dem har kliniske studier eller litteratur, og alle har evidensnivå L5.

| Rangering | Sykdom | Score | Vurdering |
|------|------|------|------|
| 4 | Medfødt entropion | 0,9922 | Scoren kommer fra TxGNN-modellen (deep learning) og kan gjenspeile likheter modellen har lært mellom beslektede sykdommer, ikke biologisk evidens |
| 5 | Medfødt ektropion | 0,9917 | Ingen plausibel mekanisme; Hold |
| 6 | Medfødt Horners syndrom | 0,9917 | Ingen mekanistisk begrunnelse; Hold |
| 7 | Ptose–stemmebåndslammelse-syndrom | 0,9915 | Kun overlappende nevromuskulære trekk; Hold |
| 8 | Kamptodaktyli, myopi og fibrose av mediale rectus-muskel | 0,9911 | Ingen kjent kobling; Hold |
| 9 | Epiblefaron | 0,9911 | Ingen plausibel mekanisme; Hold |
| 10 | Ptose–strabisme–ektopiske pupiller-syndrom | 0,9910 | Ingen kobling til glykogenomsetning; Hold |

---

## Sikkerhetsvurderinger

For sikkerhetsinformasjon, se preparatomtalen (pakningsvedlegget). Data om advarsler og kontraindikasjoner var ikke tilgjengelige i de innsamlede dataene, og det ble ikke funnet registrerte legemiddelinteraksjoner.

---

## Konklusjon og neste steg

**Beslutning: Hold (avvent)**

**Begrunnelse:**
Prediksjonen bygger kun på en modell uten kliniske studier eller litteratur (evidensnivå L5). Mekanismen er svak fordi polyglukosan ligger i cytosol og enzymet krysser blod-hjerne-barrieren dårlig.

<!-- review:begin no-lic-20261124b-alglucosidase_alfa-1 -->

> **Kontrollrettelse (2026-11-24)**: Opprinnelig sto det: «I tillegg er den eneste norske godkjenningen kansellert.» Fjernet: opplysningen om at godkjenningen(e) er kansellert, stemte ikke med EMAs data om sentrale EU-godkjenninger (2026-11-12), der godkjenningene står som gyldige (Authorised). Oppdaterte antall og statuser for godkjenningene står i hurtigoversikten og i lisenstabellen under markedsinformasjonen. Kilde: [EMA – Medicines output: medicines report](https://www.ema.europa.eu/en/documents/report/medicines-output-medicines-report_en.xlsx); [European Medicines Agency](https://www.ema.europa.eu/).

<!-- review:end no-lic-20261124b-alglucosidase_alfa-1 -->

**For å gå videre kreves følgende:**
- Preparatomtale med advarsler og kontraindikasjoner (blokkerende datamangel for sikkerhetsscreening)
- Detaljerte data om virkningsmekanisme (MOA), f.eks. fra DrugBank
- Prekliniske data som viser at enzymet kan nå cytosolisk polyglukosan i nervevev, inkludert vurdering av hjernepenetrasjon
- Litteraturgjennomgang og eventuelle kasuistikker ved GBE1-relaterte sykdommer
- Avklaring av tilgjengelighet og administrasjonsvei i Norge

<!-- review:begin no-lic-20261124b-alglucosidase_alfa-2 -->

> **Kontrollrettelse (2026-11-24)**: Opprinnelig sto det: «Avklaring av tilgjengelighet og administrasjonsvei i Norge, gitt at produktet er kansellert» Rettet: begrunnelsen om at godkjenningen(e) er kansellert, er tatt ut fordi den ikke stemte med EMAs data om sentrale EU-godkjenninger (2026-11-12), der godkjenningene står som gyldige (Authorised); selve oppfølgingspunktet er beholdt. Oppdaterte antall og statuser for godkjenningene står i hurtigoversikten og i lisenstabellen under markedsinformasjonen. Kilde: [EMA – Medicines output: medicines report](https://www.ema.europa.eu/en/documents/report/medicines-output-medicines-report_en.xlsx); [European Medicines Agency](https://www.ema.europa.eu/).

<!-- review:end no-lic-20261124b-alglucosidase_alfa-2 -->

<!-- review:begin log -->

## Kontrollogg

Nedenfor er kontrolloggen for denne siden: opplysninger kontrollert mot EMAs data om sentrale EU-godkjenninger. Rettelser gjelder bare grunnleggende faktaopplysninger; modellens prediksjoner, evidensnivåer og konklusjoner er ikke skrevet om. Setningen om at data om virkningsmekanismen ikke var tilgjengelige, er erstattet med et utdrag fra den oppgitte offisielle preparatomtalen (med uoffisiell oversettelse).

| Kontrolldato | Punkt | Tiltak | Kilde |
|------|------|------|------|
| 2026-11-19 | Setningen «data om virkningsmekanismen er ikke tilgjengelige» erstattet med utdrag fra amerikansk preparatomtale | Setning om manglende data om virkningsmekanismen erstattet med et utdrag med kilde | [DailyMed: Lumizyme (alglucosidase alfa) prescribing information, Genzyme Corporation](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=d6bfbc45-2d34-439e-8aad-59ee2d53d4df) |
| 2026-11-24 | Fjernet: «I tillegg er den eneste norske godkjenningen kansellert.» | Rettet | [EMA – Medicines output: medicines report](https://www.ema.europa.eu/en/documents/report/medicines-output-medicines-report_en.xlsx); [European Medicines Agency](https://www.ema.europa.eu/) |
| 2026-11-24 | Rettet: «Avklaring av tilgjengelighet og administrasjonsvei i Norge, gitt at produktet er kansellert» → «Avklaring av tilgjengelighet og administrasjonsvei i Norge» | Rettet | [EMA – Medicines output: medicines report](https://www.ema.europa.eu/en/documents/report/medicines-output-medicines-report_en.xlsx); [European Medicines Agency](https://www.ema.europa.eu/) |

<!-- review:end log -->

## Ansvarsfraskrivelse

Dette innholdet er kun til forskningsformål og utgjør ikke medisinsk rådgivning.
Klinisk validering kreves før enhver klinisk anvendelse.

---

