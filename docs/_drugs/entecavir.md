---
layout: default
title: Entecavir
parent: Moderat evidens (L3-L4)
nav_order: 133
evidence_level: L4
indication_count: 10
---

# Entecavir
{: .fs-9 }

Evidensnivå: **L4** | Predikerte indikasjoner: **10** stk.
{: .fs-6 .fw-300 }

---

## Innholdsfortegnelse
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## Farmasøytens vurderingsrapport

</div>

# Entecavir: Fra kronisk hepatitt B til kronisk hepatitt C-virusinfeksjon

## Oppsummering i en setning

Entecavir er en guanosin nukleosidanallog hvis etablerte, virkelige kliniske bruk er behandling av kronisk hepatitt B-virusinfeksjon (HBV) — selv om denne originalindikasjonen ikke fanges opp i kildedata (datahull). TxGNN-modellens høyest rangerte prediksjon peker på **kronisk hepatitt C-virusinfeksjon (HCV)**, men medfølgende bevis — 45 kliniske studier og 20 publikasjoner — består nesten utelukkende av HBV-fokuserte studier uten direkte anti-HCV-effektivitetsdata, og den mekanistiske begrunnelsen argumenterer eksplisitt **mot** biologisk plausibilitet (HCV har ikke reversoppskrivingstrinn for entecavir å målrette).

---

## Hurtigoversikt

| Element | Innhold |
|---------|---------|
| Originalindikasjon | Kronisk hepatitt B-virusinfeksjon (veletablert klinisk bruk; ikke til stede i kildedata for regulering/godkjenning) |
| Prediktert ny indikasjon | Kronisk hepatitt C-virusinfeksjon |
| TxGNN prediksjonspoeng | 99.98% |
| Bevisnivå | L4 |
| Status på det norske marked | Ikke markedsført |
| Antall godkjenninger | 0 |
| Anbefalt beslutning | Avvent |

---

## Hvorfor er denne prediksjonen rimelig?

Detaljerte virkningsmekanisme-data for entecavir er ikke tilgjengelige i denne bevisspakken (datahull, ID: DG002). Basert på etablert farmakologi er entecavir en guanosin nukleosidanallog som gjennomgår intracellulær fosforylasjøn for å konkurrere med det naturlige substratet for inkorporering av HBV-reverstranskriptase, som blokkerer primeringsreaksjon, reversoppskrivning og DNA-syntese. Denne mekanismen er spesifikk for reversoppskrivende virus.

Hepatitt C-virus er imidlertid et positivt-strenget RNA-virus som replikeres via en RNA-avhengig RNA-polymerase og har ingen reversoppskrivingstrinn. Ombruksbegrunnelsen knyttet til denne kandidaten er eksplisitt på dette punktet: *"Entecavir 標的為 HBV 反轉錄酶，HCV 為 RNA 病毒依賴 RNA 聚合酶（無反轉錄步驟），機轉上無直接抑制 HCV 複製之理論基礎"* — det er ingen direkte teoretisk grunnlag for at entecavir inhiberer HCV-replikasjon. Nesten alle kliniske studier hentet for denne kandidaten involverer entecavir som brukes til å håndtere **HBV-komponenten** av HBV/HCV-saminfeksjon (f.eks. forebygging av HBV-reaktivering under HCV-DAA-terapi), ikke som et anti-HCV-middel i seg selv.

**Forbeholdelse:** Dette datasettet viser `original_indications` som tomt, som ser ut til å være et datainsamlingshull i stedet for et sant fravær av indikasjon — entecavirs veldokumenterte kjerneindikasjon er kronisk HBV-infeksjon (dette er uavhengig bekreftet av rang-2-bevis i samme bevisspakke, som har et L1-bevisnivå og en "Fortsett med sikringsmekanismer"-anbefaling). Lesere bør behandle HCV-prediksjonen nedenfor som et **lavkonfidensielt, høy-poengsum TxGNN-artefakt** snarere enn en validert ombruksmulighet.

---

## Klinisk studibevis

| Studienummer | Fase | Status | Innrullering | Viktige funn |
|---------|------|------|------|---------|
| [NCT02555943](https://clinicaltrials.gov/study/NCT02555943) | Fase 2/3 | Avsluttet | 23 | HCV/HBV-saminfeksjonsstudie; entecavir brukt kun til å håndtere HBV-reaktiveringrisiko under DAA-terapi for HCV — ikke testet som HCV-behandling (relevansvurdering C) |
| [NCT00065507](https://clinicaltrials.gov/study/NCT00065507) | Fase 3 | Avsluttet | 195 | Entecavir vs. adefovir i HBV med hepatisk dekompensasjon; kun HBV-studie, ingen HCV-relevans (relevansvurdering C) |
| [NCT00371150](https://clinicaltrials.gov/study/NCT00371150) | Fase 4 | Avsluttet | 131 | Observasjonsmessig antiviruseffekt av entecavir hos sorte/hispansktalige pasienter med kronisk HBV (ikke HCV) |
| [NCT00412529](https://clinicaltrials.gov/study/NCT00412529) | Fase 3 | Avsluttet | 44 | Viruskinetikk av telbivudin vs. entecavir i HBeAg-positive kronisk HBV |
| [NCT00096785](https://clinicaltrials.gov/study/NCT00096785) | Fase 3 | Avsluttet | 69 | Entecavir vs. adefovir virusmengde-reduksjon i nukleosid-naive kronisk HBV |
| [NCT01037166](https://clinicaltrials.gov/study/NCT01037166) | Fase 2 | Avsluttet | 84 | Entecavir antivirusaktivitet hos japanske HBV-pasienter med ufullstendig lamivudin-respons |
| [NCT01022801](https://clinicaltrials.gov/study/NCT01022801) | Fase 2 | Avsluttet | 120 | Entecavir vs. lamivudin dose-respons hos japanske pasienter med kronisk HBV |
| [NCT02881008](https://clinicaltrials.gov/study/NCT02881008) | Fase 1/2 | Avsluttet | 48 | Myrcludex B vs. entecavir i HBeAg-negative kronisk HBV |

**Merknad:** Ingen av de hentet studiene tester direkte entecavirs effektivitet mot HCV; alle involverer HBV-behandling eller HBV-håndtering innenfor HBV/HCV-saminfiserte populasjoner.

---

## Litteraturbevis

| PMID | År | Type | Tidsskrift | Viktige funn |
|------|-----|------|------|---------|
| [36146665](https://pubmed.ncbi.nlm.nih.gov/36146665/) | 2022 | Kohort | Viruses | Hos anti-HCV-antistoff-positive pasienter med kronisk HBV behandlet med nukleosid(t)idanaloger (inkludert entecavir), ble HCV RNA-nivåer fulgt, men ingen antiviruseffekt mot HCV ble demonstrert |
| [24773464](https://pubmed.ncbi.nlm.nih.gov/24773464/) | 2014 | Oversikt | Expert Opin Pharmacother | Gjennomgår behandlingsfremskritt for HBV/HCV-saminfeksjon; entecavir diskutert kun som HBV-rettet terapi |
| [32527114](https://pubmed.ncbi.nlm.nih.gov/32527114/) | 2021 | Oversikt | Chin Clin Oncol | Diskuterer timing av HBV- og HCV-antivirusbehandling hos HCC-pasienter; ingen direkte anti-HCV-rolle for entecavir |
| [28230928](https://pubmed.ncbi.nlm.nih.gov/28230928/) | 2017 | Kohort | J Gastroenterol Hepatol | Undersøker HBV-reaktiveringrisiko under DAA-terapi for HCV hos saminfiserte pasienter |
| [22959099](https://pubmed.ncbi.nlm.nih.gov/22959099/) | 2013 | Kasuistikk/Oversikt | Clin Res Hepatol Gastroenterol | Beskriver terapeutiske utfordringer ved dual HBV/HCV-infeksjon; entecavir brukt til HBV-komponenten |
| [36873880](https://pubmed.ncbi.nlm.nih.gov/36873880/) | 2023 | Kasuistikk | Frontiers in Medicine | Rapporterer uvanlig virusevolvering etter antivirusbehandling hos en samtidig HBV/HCV-infisert pasient |

---

## Norsk markedsinformasjon

Entecavir er for tiden **ikke markedsført i Norge** ifølge kildedata (0 godkjenninger, ingen lisensregistreringer tilgjengelige).

---

## Sikkerhetshensyn

Vennligst se pakningsvedlegget for sikkerhetsinformasjon. Et legemiddeletikett-/sikkerhetsadvarselsdatasett var ikke tilgjengelig for denne evalueringen (datahull DG001, merket som blokkering — dette forhindrer for tiden en formell S1-sikkerhet-preevaluering).

---

## Konklusjon og neste trinn

**Beslutning: Avvent**

**Begrunnelse:**
Den høyest rangerte TxGNN-prediksjonen (HCV) mangler en plausibel mekanistisk grunnlag — entecavir målretter HBV-reverstranskriptase, mens HCV-replikasjon ikke involverer reversoppskrivning — og ingen hentet klinisk studie eller publikasjon demonstrerer direkte anti-HCV-effektivitet; alt støttende bevis reflekterer i stedet entecavirs etablerte rolle i å håndtere HBV hos HBV/HCV-saminfiserte pasienter. Kombinert med et blokkeringsdatahull på sikkerhetsmerkinger fra regulatoriske myndigheter, møter denne kandidaten for tiden ikke standarden for å fortsette.

**For å fortsette, er følgende nødvendig:**
- TFDA/offisielt produktvedlegg (advarsler, kontraindikasjoner) for å avklare blokkeringsdatahuller (DG001)
- Bekreftet virkningsmekanisme-dokumentasjon (DG002)
- Hvis det forfølges videre, en re-evaluering av hvorvidt "kronisk hepatitt C" er det korrekte målet — vurder i stedet å gjennomgå den medfølgende **kronisk hepatitt B-virusinfeksjon**-prediksjonen (bevisnivå L1, "Fortsett med sikringsmekanismer"), som reflekterer entecavirs sanne, veletablerte indikasjon og er bedre støttet for enhver ombruk eller legemiddellevetid-forlengelsesanalyse

## Ansvarsfraskrivelse

Dette innholdet er kun til forskningsformål og utgjør ikke medisinsk rådgivning.
Klinisk validering kreves før enhver klinisk anvendelse.

---

