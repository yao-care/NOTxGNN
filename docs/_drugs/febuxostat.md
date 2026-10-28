---
layout: default
title: Febuxostat
parent: Moderat evidens (L3-L4)
nav_order: 171
evidence_level: L4
indication_count: 3
last_modified_at: 2026-10-15
description: "Febuxostat: predikert ny indikasjon Renal hypourikemi (hypouricemia, renal) (evidensnivå L4). Opprinnelig indikasjon: Gikt"
monitor_inn: "FEBUXOSTAT"
predicted_indications: ["hypouricemia, renal", "hypoxanthine guanine phosphoribosyltransferase partial deficiency", "Lesch-Nyhan syndrome"]
---

# Febuxostat
{: .fs-9 }

Evidensnivå: **L4** | Predikerte indikasjoner: **3** stk.
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

## Febuxostat: Fra gikt til renal hypourikemi
{: .text-alpha }

## Oppsummering i én setning

Febuxostat er en xantinoksidasehemmer som opprinnelig brukes til behandling av gikt og hyperurikemi.
TxGNN-modellen predikerer at legemidlet kan ha effekt ved **renal hypourikemi**, men støtten er svært svak: kun **1 klinisk studie** (med uklar relevans) og **2 publikasjoner** (en oversiktsartikkel og en kasuistikk) peker i denne retningen. Mekanistisk er forslaget dessuten tvilsomt, siden legemidlet senker urinsyre ytterligere hos pasienter som allerede har lav urinsyre.

---

## Hurtigoversikt

| Punkt | Innhold |
|------|------|
| Opprinnelig indikasjon | Gikt |
| Predikert ny indikasjon | Renal hypourikemi (hypouricemia, renal) |
| TxGNN-prediksjonsscore | 0,9999 |
| Evidensnivå | L4 |
| Markedsstatus i Norge | Markedsført (gyldige tillatelser: 3 av 3) |
| Antall godkjenninger | 3 (gyldige: 3) |
| Anbefalt beslutning | Hold |

---

## Hvorfor er denne prediksjonen rimelig (eller ikke)?

Detaljerte data om virkningsmekanisme er foreløpig ikke tilgjengelige i dataene som er samlet inn for denne rapporten. Febuxostat er likevel kjent som en ikke-purin, selektiv hemmer av xantinoksidoreduktase, som senker serumurinsyre. Effekten ved gikt og hyperurikemi er godt etablert.

Renal hypourikemi kjennetegnes av lav serumurinsyre på grunn av defekt reabsorpsjon av urat i nyrene (for eksempel tap av funksjon i URAT1/SLC22A12 eller GLUT9). Å senke urinsyren ytterligere er mekanistisk kontraintuitivt. Den eneste plausible koblingen er et tilfelle i litteraturen der febuxostat ble forsøkt for å forebygge treningsutløst akutt nyreskade (EIAKI) hos en ung pasient med renal hypourikemi. Mulige mekanismer er redusert urat-belastning i urinen og mindre oksidativt stress fra xantinoksidase. Dette er en hypotese, ikke påvist klinisk nytte.

Den svært høye TxGNN-scoren kommer fra TxGNN-modellen (dyp læring) og kan gjenspeile likheter modellen har lært mellom beslektede sykdommer, ikke biologisk evidens, snarere enn et reelt terapeutisk rasjonale.

**Andre predikerte indikasjoner (kort omtale):**
- **Partiell HPRT-mangel** (score 0,9998): Febuxostat reduserer urinsyreproduksjonen og kan være et alternativ til allopurinol, men korrigerer ikke enzymdefekten. Økt xantinbelastning gir risiko for xantinnefropati eller steiner. Støtten består kun av kasuistikker. Evidensnivå L4.
- **Lesch-Nyhans syndrom** (score 0,9968): Febuxostat kan kontrollere hyperurikemi og urat-relaterte komplikasjoner, men påvirker ikke de nevrologiske og atferdsmessige symptomene. Støtten er begrenset til små pediatriske serier og en kasuistikk. Evidensnivå L4.

---

## Evidens fra kliniske studier

| Studienummer | Fase | Status | Antall deltakere | Hovedfunn |
|---------|------|------|------|---------|
| [NCT04398251](https://clinicaltrials.gov/study/NCT04398251) | Fase 4 | Ukjent | 100 | Prospektiv kontrollert studie av hvordan urinsyrekontroll påvirker tilbakefall av steiner og nyrefunksjon hos pasienter med hyperurikemi og nyrestein. Relevansen for renal hypourikemi er lav (vurdert som C), og studien kan ikke regnes som direkte evidens. |

---

## Litteraturevidens

| PMID | År | Type | Tidsskrift | Hovedfunn |
|------|-----|------|------|---------|
| [36754409](https://pubmed.ncbi.nlm.nih.gov/36754409/) | 2023 | Kasuistikk/oversikt | Internal Medicine | 16 år gammel japansk fotballspiller med familiær renal hypourikemi (URAT1-mutasjoner) og tilbakevendende treningsutløst nyreskade; febuxostat vurdert som profylakse når hydrering ikke var nok. |
| [31650389](https://pubmed.ncbi.nlm.nih.gov/31650389/) | 2020 | Oversiktsartikkel | Clinical Rheumatology | Narrativ oppdatering om hypourikemi (serumurat < 2 mg/dL), årsaker og hva revmatologer bør vite. |

---

## Markedsinformasjon for Norge

Alle tre markedsføringstillatelsene er gyldige, og legemidlet er markedsført.

| Godkjenningsnummer | Produktnavn | Doseringsform | Godkjent indikasjon |
|---------|------|------|-----------|
| EMEA/H/C/000777 | Adenuric | Ikke oppgitt | Gikt |
| EMEA/H/C/004773 | Febuxostat Krka | Ikke oppgitt | Hyperurikemi, gikt |
| EMEA/H/C/004374 | Febuxostat Viatris (tidligere Febuxostat Mylan) | Ikke oppgitt | Hyperurikemi, urinsyregikt, gikt |

---

## Sikkerhetsvurderinger

- **Kunnskapsgrafbaserte kontraindikasjoner** (fra TxGNN-kunnskapsgrafen, ikke fra preparatomtale): hjerneslag/cerebrovaskulær sykdom, cerebralt infarkt, hjerteinfarkt, koronar trombose og hemoglobinopati.
- **Legemiddelinteraksjoner** (22 registrert totalt). Alvorlige (Major):
  - Merkaptopurin
  - Azatioprin
  - Leflunomid
  - Teriflunomid

  Moderate interaksjoner omfatter blant annet teofyllin, dyfyllin, aminofyllin, oksytrifyllin, metotreksat, tioguanin, klofarabin, epirubicin, trabektedin, brentuksimab vedotin, naltrekson, asparaginase, pegaspargase og interferon beta-1a/-1b/peginterferon beta-1a.

Se preparatomtalen for fullstendig informasjon om advarsler og kontraindikasjoner.

---

## Konklusjon og neste steg

**Beslutning: Hold**

**Begrunnelse:**
Mekanismen er motstridende (ytterligere senking av en allerede lav urinsyre), og evidensen består av én studie med uklar relevans samt en oversikt og en kasuistikk. Den høye TxGNN-scoren kommer fra TxGNN-modellen (dyp læring) og kan gjenspeile likheter modellen har lært mellom beslektede sykdommer, ikke biologisk evidens. Febuxostat er markedsført i Norge med 3 gyldige markedsføringstillatelser av 3.

**For å gå videre kreves følgende:**
- Data om virkningsmekanisme (MOA) fra DrugBank
- Preparatomtale med advarsler og kontraindikasjoner (kritisk datamangel som blokkerer sikkerhetsscreening)
- Verifisering av NCT04398251 (tilstand, intervensjon og relevans)
- Kontrollerte data eller større kasuistiske serier som viser nytte og sikkerhet ved renal hypourikemi
- Vurdering av kardiovaskulær risiko, gitt kontraindikasjonssignalene for hjerte- og hjernekarsykdom
- Avklaring av regulatorisk status i Norge
## Ansvarsfraskrivelse

Dette innholdet er kun til forskningsformål og utgjør ikke medisinsk rådgivning.
Klinisk validering kreves før enhver klinisk anvendelse.

---

