---
layout: default
title: Epinephrine
parent: Kun modellprediksjon (L5)
nav_order: 155
evidence_level: L5
indication_count: 3
last_modified_at: 2026-10-30
description: "Epinephrine: predikert ny indikasjon Obstruktiv lungesykdom (evidensnivå L1). Opprinnelig indikasjon: Anafylaksi"
monitor_inn: "EPINEPHRINE"
predicted_indications: ["obstructive lung disease", "Rienhoff syndrome", "respiratory malformation"]
---

# Epinephrine
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

## Epinefrin: Fra anafylaksi til obstruktiv lungesykdom
{: .text-alpha }

## Oppsummering i en setning

Epinefrin er en adrenerg agonist som opprinnelig brukes til behandling av anafylaksi. TxGNN-modellen forutsier at den kan være effektiv ved **obstruktiv lungesykdom** (hovedsakelig astma), og i dataene som er sammenstilt for denne rapporten finnes det **15 kliniske studier** og **20 publikasjoner** som berører denne retningen. Det sterkeste beviset kommer fra fase 3-studier av inhalert epinefrin ved astma. Støtten for bronkiolitt er derimot ikke konsistent.

---

## Hurtigoversikt

| Punkt | Innhold |
|------|------|
| Opprinnelig indikasjon | Anafylaksi |
| Predikert ny indikasjon | Obstruktiv lungesykdom |
| TxGNN-prediksjonsscore | 0,9971 |
| Evidensnivå | L5 |
| Markedsstatus i Norge | Markedsført (gyldige tillatelser: 1 av 1) |
| Antall godkjenninger | 1 (gyldige: 1) |
| Antall tillatelser | 1 (annullert) |
| Anbefalt beslutning | Proceed with Guardrails (gå videre med forbehold) |

---

## Hvorfor er denne prediksjonen rimelig?

Detaljerte data om virkningsmekanisme er ikke tilgjengelige i de innhentede dataene. Epinefrin er imidlertid en kjent ikke-selektiv adrenerg agonist. Stimulering av beta-2-reseptorer gir avslapning av bronkial glatt muskulatur og dermed bronkodilatasjon, mens alfa-1-stimulering reduserer slimhinneødem.

Den opprinnelige indikasjonen, anafylaksi, innebærer ofte bronkospasme og luftveisødem. De samme reseptoreffektene som reverserer disse symptomene ved anafylaksi, er direkte relevante ved reversibel luftveisobstruksjon som astma. Inhalert epinefrin (E004, Primatene Mist) er utviklet spesifikt for astma.

Forbehold: Evidensen støtter først og fremst mild intermitterende astma, ikke kronisk obstruktiv lungesykdom (KOLS). Ved bronkiolitt viser Cochrane-oversikter og nettverksmetaanalyse inkonsistent eller begrenset nytte, så rutinebruk støttes ikke.

---

## Klinisk studiedokumentasjon

Tabellen viser de 10 mest relevante studiene (rangert etter relevans for astma/obstruktiv sykdom).

| Studienummer | Fase | Status | Antall deltakere | Hovedfunn |
|---------|------|------|------|---------|
| [NCT01357642](https://clinicaltrials.gov/study/NCT01357642) | Fase 3 | Fullført | 373 | 12 ukers effekt og sikkerhet for epinefrin-inhalasjonsaerosol (HFA-MDI) mot placebo og Primatene Mist ved astma |
| [NCT01476904](https://clinicaltrials.gov/study/NCT01476904) | Fase 3 | Fullført | 208 | 3 måneders sikkerhetsforlengelse (totalt 6 måneder) for inhalert epinefrin ved astma |
| [NCT01460511](https://clinicaltrials.gov/study/NCT01460511) | Fase 3 | Fullført | 70 | 4 ukers placebokontrollert studie av E004 hos barn (4–11 år) med astma |
| [NCT01737905](https://clinicaltrials.gov/study/NCT01737905) | Fase 3 | Fullført | 28 | Enkeltdose, dobbeltblind crossover-studie av E004 hos barn med astma |
| [NCT01705964](https://clinicaltrials.gov/study/NCT01705964) | Fase 4 | Fullført | 49 | Intramuskulært epinefrin som tillegg ved alvorlig astmaforverring hos barn |
| [NCT04207840](https://clinicaltrials.gov/study/NCT04207840) | Fase 4 | Fullført | 28 | Systemisk eksponering for Primatene Mist mot intramuskulær injeksjon og ProAir hos friske |
| [NCT01834820](https://clinicaltrials.gov/study/NCT01834820) | Fase 4 | Fullført | 120 | Pilotstudie av epinefrin, deksametason og hypertont saltvann ved bronkiolitt |
| [NCT00817466](https://clinicaltrials.gov/study/NCT00817466) | Fase 4 | Ukjent | 500 | Optimal inhalasjonsbehandling ved akutt bronkiolitt hos spedbarn (0–12 måneder) |
| [NCT01255709](https://clinicaltrials.gov/study/NCT01255709) | Fase 2 | Fullført | 24 | Farmakokinetikk for inhalert epinefrin (E004) hos friske frivillige |
| [NCT01276821](https://clinicaltrials.gov/study/NCT01276821) | Fase 4 | Fullført | 100 | Forstøvet hypertont saltvann ved bronkiolitt (epinefrin er ikke hovedintervensjon) |

Merk: Flere av studiene gjelder bronkiolitt eller farmakokinetikk og viser ikke effekt direkte. De fire fase 3-studiene av inhalert epinefrin ved astma utgjør kjernen i evidensen.

---

## Litteraturdokumentasjon

| PMID | År | Type | Tidsskrift | Hovedfunn |
|------|-----|------|------|---------|
| [33893229](https://pubmed.ncbi.nlm.nih.gov/33893229/) | 2021 | Nettverksmetaanalyse | Pediatrics | Sammenlignende effekt av bronkiolittintervensjoner ved akutt behandling |
| [35093318](https://pubmed.ncbi.nlm.nih.gov/35093318/) | 2022 | RCT | The Journal of Pediatrics | Kortikosteroider og inhalert epinefrin ved bronkiolitt hos barn på intensivavdeling |
| [21678340](https://pubmed.ncbi.nlm.nih.gov/21678340/) | 2011 | Systematisk oversikt (Cochrane) | Cochrane Database Syst Rev | Epinefrin ved bronkiolitt |
| [14974006](https://pubmed.ncbi.nlm.nih.gov/14974006/) | 2004 | Systematisk oversikt (Cochrane) | Cochrane Database Syst Rev | Epinefrin ved bronkiolitt (tidligere versjon) |
| [35953216](https://pubmed.ncbi.nlm.nih.gov/35953216/) | 2022 | Oversikt | Emerg Med Clin North Am | Vurdering og behandling av astma- og KOLS-forverring på akuttmottak |
| [30488718](https://pubmed.ncbi.nlm.nih.gov/30488718/) | 2019 | Oversikt | Expert Rev Respir Med | Terapeutiske strategier ved bronkiolitt hos barn (rasemisk epinefrin, kortikosteroider m.m.) |
| [21157348](https://pubmed.ncbi.nlm.nih.gov/21157348/) | 2011 | Oversikt | Curr Opin Pediatr | Oppdatering om behandling av bronkiolitt; ingen behandling har entydig endret sykdomsforløpet |
| [23393929](https://pubmed.ncbi.nlm.nih.gov/23393929/) | 2012 | Oversikt | Duodecim | Bronkiolitt hos spedbarn; inhalasjon av rasemisk epinefrin ved behov |
| [30856157](https://pubmed.ncbi.nlm.nih.gov/30856157/) | 2019 | Kommentar | Medical Letter | Primatene Mist er tilbake som reseptfritt legemiddel |
| [20876171](https://pubmed.ncbi.nlm.nih.gov/20876171/) | 2010 | Kostnadseffektivitet | Pediatrics | Kostnadseffektivitet av epinefrin og deksametason ved bronkiolitt |

---

## Informasjon om det norske markedet

| Tillatelsesnummer | Produktnavn | Doseringsform | Godkjent indikasjon |
|---------|------|------|-----------|
| EMEA/H/C/006139 | Eurneffy | Ikke oppgitt | Anafylaksi |

Legemidlet er markedsført, og den ene tillatelsen (1 av 1) for epinefrin er gyldig.

---

## Sikkerhetsvurderinger

Informasjon fra preparatomtale (varsler og kontraindikasjoner) er ikke tilgjengelig i dataene. Se preparatomtalen for fullstendig sikkerhetsinformasjon.

**Sykdommer med registrert kontraindikasjon i kunnskapsgrafen (TxGNN/PrimeKG, ikke merketekst):** hypertensjon, hjerte- og karsykdom, hjertesykdom, koronarsykdom, hjerteinfarkt, atrieflimmer, hjerteledningsforstyrrelser, plutselig hjertestans, lever- og nyresvikt, diabetes mellitus og diabetisk ketoacidose, hypertyreose, epilepsi, trangvinklet glaukom, benign prostatahyperplasi, myasthenia gravis, respirasjonssvikt, kaliummangel, gallblæresykdom og hemoglobinopati.

**Legemiddelinteraksjoner:** 100 interaksjoner er registrert. Blant dem som er vist, er de viktigste:
- **Alvorlige (Major):** amitriptylin, amoksapin
- **Moderate:** betablokkere (acebutolol, atenolol, betaksolol), beta-2-agonister (formoterol, salbutamol, arformoterol), sentralstimulerende midler (metylfenidat, amfetamin, atomoksetin), antidiabetika (acarbose, acetoheksamid, albiglutid, alogliptin) og antipsykotika (amisulprid, aripiprazol, asenapin)

Kardiovaskulær sikkerhet (takykardi, hypertensjon, arytmi) må overvåkes, særlig hos eldre og pasienter med hjertesykdom.

---

## Konklusjon og neste steg

**Beslutning: Proceed with Guardrails (gå videre med forbehold)**

**Begrunnelse:**
- Flere fullførte fase 3-studier av inhalert epinefrin ved astma, inkludert barn, gir evidensnivå L1, og mekanismen er biologisk rimelig. Evidensen er imidlertid begrenset til mild intermitterende astma, støtter ikke KOLS eller rutinebruk ved bronkiolitt, og legemidlet er markedsført med 1 gyldig norsk tillatelse av 1.

**For å gå videre kreves følgende:**
- Verifisere regulatorisk status for hver formulering i Norge, siden eneste tillatelse er annullert
- Innhente preparatomtale med advarsler og kontraindikasjoner (kritisk datamangel)
- Innhente detaljerte data om virkningsmekanisme
- Plan for kardiovaskulær sikkerhetsovervåking, særlig hos eldre og pasienter med hjertesykdom
- Avklare tiltenkt populasjon (mild intermitterende astma) og utelukke KOLS og bronkiolitt som mål

---

## Andre predikerte indikasjoner (kort oversikt)

| Predikert indikasjon | Score | Evidensnivå | Anbefaling | Kommentar |
|------|------|------|------|------|
| Matavhengig anstrengelsesutløst anafylaksi | 0,9957 | L5 | Forskningsspørsmål | Ingen registrerte studier. Ligger innenfor dagens anafylaksiindikasjon og er ikke ekte repurposing. Litteraturen er oversikter og kasuistikker som anbefaler epinefrin |
| Rienhoff syndrom | 0,9957 | L5 | Hold | Ingen mekanistisk kobling, studier eller litteratur. Høy score er trolig en modellartefakt |
| Respiratorisk misdannelse | 0,9956 | L3 | Forskningsspørsmål | Strukturelle misdannelser kan ikke korrigeres av epinefrin. Eneste signal er en fase 1-studie ved forbigående tachypné hos nyfødte. Mesteparten av litteraturen er irrelevant |
## Ansvarsfraskrivelse

Dette innholdet er kun til forskningsformål og utgjør ikke medisinsk rådgivning.
Klinisk validering kreves før enhver klinisk anvendelse.

---

