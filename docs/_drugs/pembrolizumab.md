---
layout: default
title: Pembrolizumab
parent: Kun modellprediksjon (L5)
nav_order: 318
evidence_level: L5
indication_count: 9
last_modified_at: 2026-10-15
description: "Pembrolizumab: predikert ny indikasjon Gingival fibromatose (evidensnivå L5). Opprinnelig indikasjon: Melanom"
monitor_inn: "PEMBROLIZUMAB"
predicted_indications: ["fibromatosis, gingival", "inclusion body myopathy with early-onset Paget disease with or without frontotemporal dementia", "hamartoma of lung", "fibroma of lung", "lung benign neoplasm", "ovarioleukodystrophy", "lung germ cell tumor", "pulmonary sulcus neoplasm", "Leukomelanoderma-infantilism-intellectual disability-hypodontia-hypotrichosis syndrome"]
---

# Pembrolizumab
{: .fs-9 }

Evidensnivå: **L5** | Predikerte indikasjoner: **9** stk.
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

## Pembrolizumab: Fra melanom og andre kreftformer til gingival fibromatose
{: .text-alpha }

## Oppsummering i én setning

Pembrolizumab er et PD-1-hemmende antistoff (immunsjekkpunkthemmer) som opprinnelig brukes mot kreft, blant annet melanom, Hodgkin-lymfom, nyrecellekarsinom, ikke-småcellet lungekreft, urotelkarsinom, hode-halskreft og livmorkreft.
TxGNN-modellen forutsier at legemidlet kan være effektivt mot **gingival fibromatose** (tilvekst av tannkjøttvev), men det finnes **ingen kliniske studier og ingen publikasjoner** som støtter denne retningen.
Prediksjonen er derfor kun modellbasert og har svært svakt evidensgrunnlag.

---

## Hurtigoversikt

| Punkt | Innhold |
|------|------|
| Opprinnelig indikasjon | Melanom; Hodgkin-lymfom; nyrecellekarsinom; ikke-småcellet lungekreft; urotelkarsinom; plateepitelkarsinom i hode og hals; urologiske neoplasmer; endometrieneoplasmer |
| Foreslått ny indikasjon | Gingival fibromatose |
| TxGNN-prediksjonsscore | 0.9940 |
| Evidensnivå | L5 |
| Markedsstatus i Norge | Markedsført (gyldige tillatelser: 1 av 1) |
| Antall godkjenninger | 1 (gyldige: 1) |
| Antall tillatelser | 1 (kansellert) |
| Anbefalt beslutning | Hold |

---

## Hvorfor er denne prediksjonen (ikke) rimelig?

Detaljerte data om virkningsmekanisme er ikke tilgjengelige i datagrunnlaget. Pembrolizumab er kjent som et monoklonalt antistoff mot PD-1-reseptoren (PDCD1/CD279). Ved å blokkere PD-1 løsnes bremsen på T-cellene, slik at immunsystemet lettere angriper kreftceller.

Gingival fibromatose er en godartet, fibrotisk tilstand i tannkjøttet, ofte genetisk eller legemiddelutløst. Den har ingen opplagt kobling til PD-1-banen, og immunaktivering ventes ikke å være gunstig. Den høye prediksjonsscoren kommer fra TxGNN-modellen (deep learning) og kan gjenspeile likheter modellen har lært mellom beslektede sykdommer, ikke biologisk evidens.

Lignende vurderinger gjelder for de andre topprangerte prediksjonene (blant annet inklusjonslegememyopati med Paget sykdom, godartede lungesvulster, ovarioleukodystrofi): ingen plausibel PD-1-mekanisme, og for enkelte kan immunaktivering være skadelig (for eksempel kan sjekkpunkthemmere gi immunrelatert myositt). Den eneste prediksjonen med reell klinisk nærhet er hilært lungekarsinom, som i praksis er en indikasjon innenfor ikke-småcellet lungekreft der pembrolizumab allerede er godkjent, og dermed en utvidelse av eksisterende bruk snarere enn ekte repurposing.

---

## Evidens fra kliniske studier

Det er for tiden ingen registrerte kliniske studier knyttet til gingival fibromatose.

---

## Litteraturevidens

Det er for tiden ingen relevant litteratur tilgjengelig for gingival fibromatose.

---

## Informasjon om det norske markedet

| Tillatelsesnummer | Produktnavn | Doseringsform | Godkjent indikasjon |
|---------|------|------|-----------|
| EMEA/H/C/003820 | Keytruda | Ikke oppgitt | Melanom; Hodgkin-lymfom; nyrecellekarsinom; ikke-småcellet lungekreft; urotelkarsinom; plateepitelkarsinom i hode og hals... (status: kansellert) |

Merk: Legemidlet er markedsført i Norge, og 1 av 1 tillatelser i datagrunnlaget er gyldig.

---

## Cytotoksisitet

| Punkt | Innhold |
|------|------|
| Cytotoksisitetsklassifisering | Immunterapi (PD-1-hemmer, monoklonalt antistoff); ikke konvensjonelt cytotoksisk |
| Myelosuppresjonsrisiko | Lav; ikke et typisk myelosuppressivt legemiddel. Se pakningsvedlegget for detaljer |
| Emetogenisitet | Lav |
| Overvåkingspunkter | Blodtelling, lever- og nyrefunksjon, skjoldbruskkjertel- og binyrefunksjon (immunrelaterte bivirkninger) |
| Håndteringsbeskyttelse | Se pakningsvedleggets advarsler og forholdsregler |

---

## Sikkerhetsvurderinger

**Legemiddelinteraksjoner** (13 registrert i datagrunnlaget):

- **Alvorlig (Major):** lenalidomid, pomalidomid, talidomid.
- **Moderat:** kortikosteroider, inkludert hydrokortison, triamcinolon, deksametason, betametason, budesonid, prednisolon, prednison, metylprednisolon og deflazakort. Kortikosteroider kan svekke effekten av immunterapi.
- Farmakologidata bekrefter at målet er PD-1 (PDCD1).

Annen sikkerhetsinformasjon: se pakningsvedlegget. Fra litteraturen er det kjent at sjekkpunkthemmere kan gi immunrelaterte bivirkninger (blant annet endokrinopatier, myositt, myokarditt og nevrologiske komplikasjoner).

---

## Konklusjon og neste steg

**Beslutning: Hold**

**Begrunnelse:**
Prediksjonen for gingival fibromatose bygger kun på modellscore (L5), uten kliniske studier eller litteratur og uten plausibel mekanisme. Risikoen ved systemisk immunterapi er ikke forsvarlig uten støttende evidens for en godartet tilstand.

**For å gå videre kreves:**
- Dokumentasjon av virkningsmekanisme (MOA) og en mekanistisk hypotese for PD-1-blokade ved gingival fibromatose
- Prekliniske data eller observasjonsdata som støtter effekt
- Gjennomgang av pakningsvedlegget (advarsler og kontraindikasjoner), som mangler i datagrunnlaget
- Avklaring av norsk markedsstatus, siden den registrerte tillatelsen er kansellert
- Vurdering av om en annen prediksjon (for eksempel hilært lungekarsinom) er en mer realistisk kandidat, siden den ligger innenfor eksisterende godkjent bruk
## Ansvarsfraskrivelse

Dette innholdet er kun til forskningsformål og utgjør ikke medisinsk rådgivning.
Klinisk validering kreves før enhver klinisk anvendelse.

---

