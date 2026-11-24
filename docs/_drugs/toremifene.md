---
layout: default
title: Toremifene
parent: Kun modellprediksjon (L5)
nav_order: 428
evidence_level: L5
indication_count: 1
last_modified_at: 2026-11-24
description: "Toremifene: predikert ny indikasjon HIV-infeksjon (evidensnivå L5). Opprinnelig indikasjon: Brystkreft (Breast Neoplasms)"
monitor_inn: "TOREMIFENE"
predicted_indications: ["HIV infectious disease"]
---

# Toremifene
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

## Toremifen: Fra brystkreft til HIV-infeksjon
{: .text-alpha }

## Oppsummering i én setning

Toremifen er en østrogenreseptorantagonist som opprinnelig brukes til behandling av brystkreft.
TxGNN-modellen forutsier at den kan ha effekt mot **HIV-infeksjon**, men dette er foreløpig kun en modellprediksjon: det finnes **ingen registrerte kliniske studier** og bare **1 publikasjon** (en prekliniske studie av soppinfeksjon, ikke HIV).

---

## Hurtigoversikt

| Punkt | Innhold |
|------|------|
| Opprinnelig indikasjon | Brystkreft (Breast Neoplasms) |
| Predikert ny indikasjon | HIV-infeksjon |
| TxGNN-prediksjonsscore | 0,9941 |
| Evidensnivå | L5 |
| Markedsstatus i Norge | Markedsført (gyldige tillatelser: 1 av 1) |
| Antall godkjenninger | 1 (gyldige: 1) |
| Anbefalt beslutning | Hold |

---

## Hvorfor er denne prediksjonen rimelig?

Ifølge avsnittet «Mechanism of Action» i preparatomtalen som er godkjent av amerikanske FDA (Prescribing Information), for Toremifene (uoffisiell oversettelse): «Toremifen er et ikke-steroid trifenyletylenderivat. Toremifen bindes til østrogenreseptorer og kan utøve østrogen eller antiøstrogen aktivitet, eller begge deler, avhengig av behandlingsvarighet, dyreart, kjønn, målorgan eller valgt endepunkt.» Engelsk originaltekst: "Toremifene is a nonsteroidal triphenylethylene derivative. Toremifene binds to estrogen receptors and may exert estrogenic, antiestrogenic, or both activities, depending upon the duration of treatment, animal species, gender, target organ, or endpoint selected." ([DailyMed: Fareston (toremifene citrate) prescribing information, Kyowa Kirin, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=2cab8dd1-3a10-48e6-86ce-0e5275ed49e5), versjon av 2024-11-13; hentet 2026-11-19). Basert på kjent informasjon er toremifen en selektiv østrogenreseptormodulator (SERM) i samme klasse som tamoxifen. Effekten er dokumentert ved brystkreft, men mekanismen gir ingen opplagt forbindelse til HIV.

TxGNN-scoren er svært høy (0,9941), men den er utelukkende en modellprediksjon. Den eneste støttende publikasjonen (PMID 24520056, 2014) viser at østrogenreseptorantagonister, inkludert toremifen og tamoxifen, har aktivitet mot *Cryptococcus*. De binder seg til EF-hand kalsiumbindende proteiner som kalmodulin, og virker synergistisk med flukonazol. Kryptokokkose er en vanlig opportunistisk soppinfeksjon ved avansert HIV (kryptokokkmeningitt), men det er ikke det samme som HIV-infeksjon.

Koblingen til HIV er dermed indirekte. Funnene kan på sikt støtte tilleggsbehandling av HIV-assosiert kryptokokkose, men det finnes ingen dokumentasjon for antiviral aktivitet mot HIV eller klinisk nytte ved HIV-sykdom.

---

## Evidens fra kliniske studier

Foreløpig er ingen relaterte kliniske studier registrert.

---

## Litteraturevidens

| PMID | År | Type | Tidsskrift | Hovedfunn |
|------|-----|------|------|---------|
| [24520056](https://pubmed.ncbi.nlm.nih.gov/24520056/) | 2014 | Preklinisk (in vitro/in vivo) | mBio | Tamoxifen og toremifen er soppdrepende mot *Cryptococcus* og virker synergistisk med flukonazol og amfotericin B. Effekten forklares ved binding til EF-hand-proteiner. Gjelder soppinfeksjon, ikke HIV direkte. |

---

## Markedsinformasjon for Norge

<!-- licenses:begin -->

| Godkjenningsnummer | Preparatnavn (EMA) | Virkestoff(er) (EMA, engelsk) | Terapeutisk område (EMA, engelsk) | Status |
|------|------|------|------|------|
| EMEA/H/C/000091 | Fareston | toremifene | Breast Neoplasms | Gyldig |

Kilde: EMA – Medicines output (sentralt godkjente legemidler til mennesker); preparatnavn, virkestoffer og terapeutisk område er gjengitt i engelsk original. Nasjonale markedsføringstillatelser (DMP) og veterinærpreparater er ikke med i disse dataene.

<!-- licenses:end -->

---

## Cytotoksisitet

| Punkt | Innhold |
|------|------|
| Cytotoksisitetsklassifisering | Hormonell/målrettet behandling (SERM), ikke konvensjonelt cytotoksisk middel |
| Myelosuppresjonsrisiko | Lav. Kunnskapsgrafen nevner trombocytopeni og leukopeni som mulige kontraindikasjoner, så blodtellinger bør følges |
| Emetogenisitetsklassifisering | Lav |
| Overvåkingspunkter | Blodstatus (CBC), lever- og nyrefunksjon, elektrolytter (kalium, kalsium), EKG/QT-intervall |
| Håndteringsbeskyttelse | Se preparatomtalen for retningslinjer for håndtering |

---

## Sikkerhetsvurderinger

**Kontraindikasjoner fra kunnskapsgrafen (PrimeKG, ikke preparatomtale):**
Long QT-syndrom, familiært long QT-syndrom, torsades de pointes, trombocytopeni, kaliummangel, hyperkalsemi, nefrokalsinose, forstyrrelser i fosformetabolismen, leukopeni og endometriehyperplasi.

**Legemiddelinteraksjoner:** 100 interaksjoner er registrert. Et utvalg:
- **Alvorlige (Major):** deksametason, klaritromycin, levofloksacin, dolasetron, palonosetron, pikosulfat, polyetylenglykol (3350 med elektrolytter), natriumsulfat
- **Moderate:** famotidin, cimetidin, pioglitazon, loperamid, aprepitant, bisakodyl, metreleptin, mikonazol, nateglinid, laktitol, laktulose
- **Mindre (Minor):** metronidazol

Det er særlig viktig å være forsiktig ved samtidig bruk av andre QT-forlengende legemidler, inkludert flere antiretrovirale og soppmidler, som er relevante i en HIV-populasjon.

Se preparatomtalen for øvrig sikkerhetsinformasjon.

---

## Konklusjon og neste steg

**Beslutning: Hold**

**Begrunnelse:**
Prediksjonen bygger kun på en modellscore uten kliniske studier, og den eneste litteraturen gjelder soppinfeksjon, ikke HIV.

<!-- review:begin no-lic-20261106-toremifene-1 -->

> **Kontrollrettelse (2026-11-06)**: Opprinnelig sto det: «Prediksjonen bygger kun på en modellscore uten kliniske studier, og den eneste litteraturen gjelder soppinfeksjon, ikke HIV. Kombinert med at godkjenningen i Norge er opphevet og at QT-risiko og mange interaksjoner begrenser praktisk bruk, er evidensen for svak til å gå videre.» Fjernet: opplysningen om at godkjenningene er avregistrert eller at ingen gyldig godkjenning finnes, stemte ikke med EMAs data om sentrale EU-godkjenninger (2026-11-06). Oppdaterte antall og statuser for godkjenningene står i hurtigoversikten og i lisenstabellen under markedsinformasjonen. Kilde: [EMA – Medicines output: medicines report](https://www.ema.europa.eu/en/documents/report/medicines-output-medicines-report_en.xlsx); [European Medicines Agency](https://www.ema.europa.eu/).

<!-- review:end no-lic-20261106-toremifene-1 -->

**For å gå videre kreves følgende:**
- Data om virkningsmekanisme (MOA)
- Preparatomtale med advarsler og kontraindikasjoner
- Preklinisk dokumentasjon for antiviral aktivitet mot HIV, eller en avklaring av om fokus bør være HIV-assosiert kryptokokkose
- Vurdering av QT-risiko og interaksjoner med antiretrovirale legemidler og soppmidler
- Avklaring av markedsstatus og tilgjengelige produkter i Norge

<!-- review:begin log -->

## Kontrollogg

Nedenfor er kontrolloggen for denne siden: opplysninger kontrollert mot EMAs data om sentrale EU-godkjenninger. Rettelser gjelder bare grunnleggende faktaopplysninger; modellens prediksjoner, evidensnivåer og konklusjoner er ikke skrevet om. Setningen om at data om virkningsmekanismen ikke var tilgjengelige, er erstattet med et utdrag fra den oppgitte offisielle preparatomtalen (med uoffisiell oversettelse).

| Kontrolldato | Punkt | Tiltak | Kilde |
|------|------|------|------|
| 2026-11-06 | Fjernet: «Kombinert med at godkjenningen i Norge er opphevet og at QT-risiko og mange interaksjoner begrenser praktisk bruk, er evidensen for svak til» | Rettet (revidert 2026-11-24; tidligere versjon er lagret i posten) | [EMA – Medicines output: medicines report](https://www.ema.europa.eu/en/documents/report/medicines-output-medicines-report_en.xlsx); [European Medicines Agency](https://www.ema.europa.eu/) |
| 2026-11-19 | Setningen «data om virkningsmekanismen er ikke tilgjengelige» erstattet med utdrag fra amerikansk preparatomtale | Setning om manglende data om virkningsmekanismen erstattet med et utdrag med kilde | [DailyMed: Fareston (toremifene citrate) prescribing information, Kyowa Kirin, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=2cab8dd1-3a10-48e6-86ce-0e5275ed49e5) |

<!-- review:end log -->

## Ansvarsfraskrivelse

Dette innholdet er kun til forskningsformål og utgjør ikke medisinsk rådgivning.
Klinisk validering kreves før enhver klinisk anvendelse.

---

