---
layout: default
title: Tenecteplase
parent: Kun modellprediksjon (L5)
nav_order: 408
evidence_level: L5
indication_count: 7
last_modified_at: 2026-10-15
monitor_inn: "TENECTEPLASE"
predicted_indications: ["congenital coronary artery anomaly", "coronary stenosis", "partial deletion of the short arm of chromosome 16", "beta-thalassemia with other manifestations", "hemolytic anemia due to glucophosphate isomerase deficiency", "pyropoikilocytosis, hereditary", "pyruvate kinase deficiency of red cells"]
description: "Tenecteplase: predikert ny indikasjon Congenital coronary artery anomaly (evidensnivå L5). Opprinnelig indikasjon: Myocardial Infarction"
---

# Tenecteplase
{: .fs-9 }

Evidensnivå: **L5** | Predikerte indikasjoner: **7** stk.
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

## Tenecteplase: Congenital coronary artery anomaly
{: .text-alpha }

## Oppsummering

Tenekteplase er et fibrinspesifikt trombolytikum (vevsplasminogenaktivator) som opprinnelig brukes til behandling av akutt hjerteinfarkt.
TxGNN-modellen forutsier at legemidlet kan være effektivt ved **posteroinferiort hjerteinfarkt**, men dette er en anatomisk undertype av den godkjente indikasjonen, ikke en reell ny indikasjon.
Det er **ingen kliniske studier** og **ingen publikasjoner** som direkte støtter denne spesifikke prediksjonen.

---

## Hurtigoversikt

| Punkt | Innhold |
|------|------|
| Opprinnelig indikasjon | Myocardial Infarction |
| Predikert ny indikasjon | Congenital coronary artery anomaly |
| TxGNN-prediksjonsscore | 0.9961 |
| Evidensnivå | L5 |
| Markedsstatus i Norge | Markedsført (gyldige tillatelser: 1 av 1) |
| Antall godkjenninger | 1 (gyldige: 1) |
| Antall tillatelser | 1 |
| Anbefalt beslutning | Hold |

---

## Hvorfor er denne prediksjonen rimelig?

Data om virkningsmekanisme er ikke tilgjengelig i dataene som er samlet inn for denne rapporten. Basert på kjent informasjon er tenekteplase en fibrinspesifikk vevsplasminogenaktivator. Den omdanner plasminogen til plasmin, som løser opp fibrin i blodproppen som blokkerer en kransarterie. Effekten er godt dokumentert ved akutt hjerteinfarkt med ST-elevasjon.

Posteroinferiort hjerteinfarkt er en anatomisk undertype av hjerteinfarkt. Den høye scoren gjenspeiler i hovedsak overlapp med den opprinnelige indikasjonen, og ikke et nytt repurposing-signal. Mekanismen (oppløsning av trombe i den okkluderte kransarterien) er i prinsippet like relevant, men prediksjonen er i praksis en gjentakelse av den godkjente bruken.

Blant de ti øverste prediksjonene er flere uten plausibel mekanisme (for eksempel kromosomdelesjon, beta-talassemi og røde blodcellers enzymmangler).

---

## Evidens fra kliniske studier

Foreløpig er det ingen relaterte kliniske studier registrert for posteroinferiort hjerteinfarkt.

---

## Evidens fra litteratur

Foreløpig finnes det ingen relevant litteratur for denne spesifikke prediksjonen.

For øvrig predikert indikasjon på rang 5 (koronarstenose) fant man indirekte litteratur, blant annet en randomisert pilotstudie av intrakoronar tenekteplase under primær PCI (PMID 31870492, n = 40). Dette er likevel ikke evidens for hovedprediksjonen.

---

## Markedsinformasjon for Norge

| Tillatelsesnummer | Produktnavn | Doseringsform | Godkjent indikasjon |
|---------|------|------|-----------|
| EMEA/H/C/000306 | Metalyse | Ikke oppgitt | Hjerteinfarkt (status: godkjent/godkjent) |

---

## Sikkerhetsvurderinger

- **Legemiddelinteraksjoner**: Totalt 100 interaksjoner er registrert i dataene. Blant de som er oppført finnes følgende hovedgrupper:
  - **Alvorlige (Major)**: antikoagulantia og blodplatehemmere/relaterte midler som apiksaban, betriksaban og abciksimab, samt deferasirox, akalabrutinib, avapritinib, ibritumomab tiuksetan og tositumomab. Felles for mange er økt blødningsrisiko.
  - **Moderate**: acetylsalisylsyre, NSAID (ibuprofen, ketorolac, celekoksib, topisk diklofenak), aminokapronsyre, omega-3-fettsyrer, samt deksfenfluramin, fenfluramin og sibutramin.

Se preparatomtalen for øvrig sikkerhetsinformasjon, inkludert advarsler og kontraindikasjoner.

---

## Konklusjon og neste steg

**Beslutning: Hold**

**Begrunnelse:**
Prediksjonen er en undertype av den allerede godkjente indikasjonen og representerer ikke en ny repurposing-mulighet.

**For å gå videre trengs følgende:**
- Preparatomtale med advarsler og kontraindikasjoner (blokkerende datamangel for sikkerhetsscreening)
- Data om virkningsmekanisme (MOA) fra DrugBank
- Avklaring av hvorfor tillatelsen er tilbakekalt/avregistrert, og om en ny tillatelse er aktuell
- Vurdering av mer reelle kandidatindikasjoner (for eksempel koronarstenose, der det finnes indirekte, småskala evidens for intrakoronar bruk), fortrinnsvis med kontrollerte studier
## Ansvarsfraskrivelse

Dette innholdet er kun til forskningsformål og utgjør ikke medisinsk rådgivning.
Klinisk validering kreves før enhver klinisk anvendelse.

---

