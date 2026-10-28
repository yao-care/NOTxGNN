---
layout: default
title: Chenodeoxycholic Acid
parent: Kun modellprediksjon (L5)
nav_order: 96
evidence_level: L5
indication_count: 5
last_modified_at: 2026-10-28
description: "Chenodeoxycholic Acid: predikert ny indikasjon Homozygot familiær hyperkolesterolemi (evidensnivå L5). Opprinnelig indikasjon: Cerebrotendinøs xantomatose"
monitor_inn: "CHENODEOXYCHOLIC ACID"
predicted_indications: ["homozygous familial hypercholesterolemia", "brain small vessel disease 1 with or without ocular anomalies", "autosomal dominant familial hematuria-retinal arteriolar tortuosity-contractures syndrome", "obsolete familial combined hyperlipidemia", "obsolete hyperuricemia (disease)"]
---

# Chenodeoxycholic Acid
{: .fs-9 }

Evidensnivå: **L5** | Predikerte indikasjoner: **5** stk.
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

## Kenodeoksykolsyre: Fra cerebrotendinøs xantomatose til homozygot familiær hyperkolesterolemi
{: .text-alpha }

## Oppsummering

Kenodeoksykolsyre (CDCA) er en primær gallesyre som opprinnelig brukes til å behandle cerebrotendinøs xantomatose (CTX) og medfødte stoffskiftefeil.
TxGNN-modellen predikerer at legemidlet kan ha effekt ved **homozygot familiær hyperkolesterolemi**, men det finnes **ingen kliniske studier** og **ingen litteratur som direkte omhandler denne indikasjonen**. Den eneste tilknyttede publikasjonen er en oversikt om CTX, altså den allerede godkjente indikasjonen.

## Hurtigoversikt

| Punkt | Innhold |
|------|------|
| Opprinnelig indikasjon | Cerebrotendinøs xantomatose; medfødte stoffskiftefeil |
| Predikert ny indikasjon | Homozygot familiær hyperkolesterolemi |
| TxGNN-prediksjonsscore | 0,9957 |
| Evidensnivå | L5 (kun indirekte mekanistisk grunnlag, ingen studier på den nye indikasjonen) |
| Status på det norske markedet | Markedsført (gyldige tillatelser: 1 av 1) |
| Antall godkjenninger | 1 (gyldige: 1) |
| Anbefalt beslutning | Hold |

## Hvorfor er denne prediksjonen rimelig (eller ikke)?

CDCA er en primær gallesyre som undertrykker leverens syntese av kolesterol og gallesyrer via FXR-aktivering og negativ tilbakekobling på CYP7A1 og CYP27A1. Ved CTX, som skyldes mangel på enzymet sterol-27-hydroksylase, reduserer dette opphopningen av kolesterol og kolestanol i vev. Data om detaljert virkningsmekanisme fra legemiddeldatabasen er ikke tilgjengelig i de sammenstilte dataene, så beskrivelsen over bygger på en mekanistisk vurdering.

Koblingen til homozygot familiær hyperkolesterolemi (HoFH) er indirekte. HoFH skyldes dysfunksjon i LDL-reseptoren, og i prinsippet kan modulering av gallesyresyntesen påvirke kolesterolhomeostasen. CDCA er imidlertid historisk rapportert å kunne øke LDL-kolesterol i enkelte situasjoner, så nytte ved HoFH er ikke støttet. Den høye scoren kommer fra TxGNN-modellen (deep learning) og kan gjenspeile likheter modellen har lært mellom beslektede sykdommer, ikke biologisk evidens eller dokumentert klinisk effekt.

De fire neste prediksjonene (småkarsykdom i hjernen type 1, familiært hematuri-retinal arteriolær tortuositet-kontrakturer-syndrom, foreldet familiær kombinert hyperlipidemi og foreldet hyperurikemi) har ingen identifisert mekanistisk sammenheng eller klinisk evidens. De ser ut til å være beregningsmessige artefakter og får anbefalingen «Hold».

## Evidens fra kliniske studier

Foreløpig er det ingen relaterte kliniske studier registrert.

## Litteraturevidens

| PMID | År | Type | Tidsskrift | Hovedfunn |
|------|-----|------|------|---------|
| [25424010](https://pubmed.ncbi.nlm.nih.gov/25424010/) | 2014 | Oversiktsartikkel | Orphanet J Rare Dis | Omfattende gjennomgang av patogenese, klinikk, diagnostikk og behandling av CTX. Gjelder den godkjente indikasjonen, ikke HoFH. |

## Informasjon om det norske markedet

| Godkjenningsnummer | Produktnavn | Doseringsform | Godkjent indikasjon |
|---------|------|------|-----------|
| EMEA/H/C/004061 | Chenodeoxycholic acid Leadiant (tidligere Chenodeoxycholic acid sigma-tau) | Ikke oppgitt | Cerebrotendinøs xantomatose; medfødte stoffskiftefeil (status: godkjent) |

## Sikkerhetsvurderinger

Pakningsvedlegg med advarsler og kontraindikasjoner er ikke tilgjengelig i de sammenstilte dataene. Se pakningsvedlegget for fullstendig sikkerhetsinformasjon.

- **Mulige kontraindikasjoner (fra kunnskapsgraf, ikke preparatomtale)**: leversykdom, gallblæresykdom, diarésykdom, kolestase, godartet tilbakevendende intrahepatisk kolestase, familiær intrahepatisk kolestase, sklerosende kolangitt, primær biliær kolangitt og Reynolds syndrom.
- **Legemiddelinteraksjoner**: Totalt 56 interaksjoner er registrert. Blant de 20 som er listet, er alle av moderat alvorlighetsgrad. De viktigste gruppene er:
  - Østrogener: etinylestradiol, østradiol, konjugerte østrogener
  - Fibrater og kolesterolsenkende midler: gemfibrozil, fenofibrat, klofibrat, ezetimib
  - Gallesyrebindere: kolestyramin, kolesevelam, kolestipol
  - Antacida: aluminiumhydroksid
  - Asparaginaser og kreftlegemidler: asparaginase (E. coli og Erwinia), kalaspargase pegol, brentuksimab vedotin, klofarabin
  - Andre: cannabidiol, bedakvilin, anisindion

Merk at gallesyrebindere kan binde CDCA og redusere opptaket, og at kombinasjon med lipidsenkende midler krever vurdering i en eventuell HoFH-setting.

## Konklusjon og neste steg

**Beslutning: Hold**

**Begrunnelse:**
Det finnes ingen kliniske studier eller direkte litteratur som støtter bruk ved HoFH, og CDCA kan tvert imot øke LDL-kolesterol. Den høye prediksjonsscoren kommer fra TxGNN-modellen (deep learning) og kan gjenspeile likheter modellen har lært mellom beslektede sykdommer, ikke biologisk evidens. I tillegg er legemidlet markedsført i Norge, og den eneste godkjenningen (1 av 1) er gyldig.

**For å komme videre trengs følgende:**
- Pakningsvedlegg med advarsler og kontraindikasjoner (blokkerende datamangel for sikkerhetsscreening)
- Data om virkningsmekanisme fra legemiddeldatabasen
- Prekliniske eller kliniske data som viser effekt og sikkerhet på LDL-kolesterol hos HoFH-pasienter
- Vurdering av udekket behov i forhold til eksisterende HoFH-behandlinger
- Avklaring av doseringsform og administrasjonsvei
## Ansvarsfraskrivelse

Dette innholdet er kun til forskningsformål og utgjør ikke medisinsk rådgivning.
Klinisk validering kreves før enhver klinisk anvendelse.

---

