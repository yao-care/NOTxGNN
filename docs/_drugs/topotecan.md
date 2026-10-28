---
layout: default
title: Topotecan
parent: Kun modellprediksjon (L5)
nav_order: 427
evidence_level: L5
indication_count: 2
last_modified_at: 2026-10-28
description: "Topotecan: predikert ny indikasjon Brystkreft hos kvinner (female breast carcinoma) (evidensnivå L3). Opprinnelig indikasjon: Livmorhalskreft, småcellet lungekreft"
monitor_inn: "TOPOTECAN"
predicted_indications: ["female breast carcinoma", "adult germ cell tumor"]
---

# Topotecan
{: .fs-9 }

Evidensnivå: **L5** | Predikerte indikasjoner: **2** stk.
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

## Topotecan: Fra livmorhalskreft og småcellet lungekreft til brystkreft hos kvinner
{: .text-alpha }

## Oppsummering

Topotecan er en topoisomerase I-hemmer som opprinnelig ble brukt mot livmorhalskreft, småcellet lungekreft og (for ett av produktene) eggstokkreft.
TxGNN-modellen predikerer at legemidlet kan være effektivt mot **brystkreft hos kvinner**,
men støtten er svak: de tre registrerte kliniske studiene er tidlige eller avsluttet, og litteraturen består i hovedsak av oversiktsartikler og prekliniske studier.

---

## Hurtigoversikt

| Punkt | Innhold |
|------|------|
| Opprinnelig indikasjon | Livmorhalskreft, småcellet lungekreft |
| Predikert ny indikasjon | Brystkreft hos kvinner (female breast carcinoma) |
| TxGNN-prediksjonsscore | 0,9992 |
| Evidensnivå | L5 |
| Status på det norske markedet | Markedsført (gyldige tillatelser: 3 av 3) |
| Antall godkjenninger | 3 (gyldige: 3) |
| Antall tillatelser | 3 (alle kansellert) |
| Anbefalt beslutning | Hold |

---

## Hvorfor er denne prediksjonen rimelig?

Data om virkningsmekanisme (MOA) fra legemiddeldatabasen er ikke tilgjengelig i de innsamlede dataene. Topotecan er imidlertid kjent som en topoisomerase I-hemmer. Den forårsaker DNA-brudd i celler som deler seg raskt, og effekten er dokumentert ved livmorhalskreft og småcellet lungekreft.

Prekliniske data tyder på at enkelte brystkreftsubtyper, særlig MYC-drevne og trippelnegative, kan være følsomme for TOP1-hemming gjennom opphopning av R-løkker og replikasjonsstress (PMID 37987734). Samtidig transporteres topotecan av effluks-transportøren BCRP/ABCG2, som er uttrykt i brystkreftceller og kan gi resistens og begrense effekten (PMID 25236865, PMID 10930538).

Klinisk støtte er begrenset. En fase 2-studie av høydose topotecan i kombinasjonsregime ble avsluttet, og en fase 2-studie fra 1997 med kontinuerlig infusjon ved avansert brystkreft og ikke-småcellet lungekreft fant ingen tegn til økt effekt. Prediksjonen bør derfor regnes som et forskningsspørsmål, ikke en etablert behandlingsmulighet.

---

## Evidens fra kliniske studier

| Studienummer | Fase | Status | Antall deltakere | Hovedfunn |
|---------|------|------|------|---------|
| [NCT00006032](https://clinicaltrials.gov/study/NCT00006032) | Fase 2 | Avsluttet | Ikke oppgitt | Høydose topotecan, ifosfamid/mesna og etoposid (TIME) etterfulgt av autolog stamcellestøtte ved metastatisk brystkreft. Direkte relevant, men avsluttet, og overførbarheten er begrenset |
| [NCT02419495](https://clinicaltrials.gov/study/NCT02419495) | Fase 1 | Avsluttet | 221 | Sikkerhetsstudie av selinexor med flere standard kjemoterapi-/immunterapiregimer; topotecan er bare én av flere partnere |
| [NCT06840886](https://clinicaltrials.gov/study/NCT06840886) | Fase 1 | Rekrutterer | 426 | Førstegangs dose-eskaleringsstudie av PHST001 ved avanserte solide svulster; topotecans rolle er uklar, ingen effektdata ennå |

---

## Litteraturevidens

| PMID | År | Type | Tidsskrift | Hovedfunn |
|------|-----|------|------|---------|
| [9413954](https://pubmed.ncbi.nlm.nih.gov/9413954/) | 1997 | Fase 2-studie | British Journal of Cancer | Kontinuerlig infusjon av topotecan ved avansert brystkreft og ikke-småcellet lungekreft: ingen tegn til økt effekt |
| [11455218](https://pubmed.ncbi.nlm.nih.gov/11455218/) | 2001 | Pilotstudie | Onkologie | Topotecan som primær kjemoterapi ved hjernemetastaser hos pasienter med brystkreft |
| [9425961](https://pubmed.ncbi.nlm.nih.gov/9425961/) | 1997 | Oversikt | Seminars in Oncology | Mulig rolle for topotecan ved avansert brystkreft |
| [37987734](https://pubmed.ncbi.nlm.nih.gov/37987734/) | 2023 | Preklinisk | Cancer Research | TOP1-hemming i MYC-drevet kreft gir opphopning av R-løkker og syntetisk letalitet |
| [10472342](https://pubmed.ncbi.nlm.nih.gov/10472342/) | 1999 | Preklinisk (xenograft) | Anticancer Research | Sammenligning av doksorubicin, cisplatin, irinotekan og topotecan i xenografter fra kolon-, lunge- og brystkreft |
| [10930538](https://pubmed.ncbi.nlm.nih.gov/10930538/) | 2000 | Preklinisk | Biochemical Pharmacology | BCRP-uttrykk i topotecanresistente brystkreftceller |
| [25236865](https://pubmed.ncbi.nlm.nih.gov/25236865/) | 2015 | Oversikt | The AAPS Journal | BCRP/ABCG2 transporterer topotecan og kan begrense effekten |
| [15836850](https://pubmed.ncbi.nlm.nih.gov/15836850/) | 2005 | Preklinisk | J Surg Res | Effekt av kvercetin på topotecans cytotoksisitet i MCF-7- og MDA-MB-231-celler |
| [39657238](https://pubmed.ncbi.nlm.nih.gov/39657238/) | 2024 | Preklinisk | ACS Applied Materials & Interfaces | Nanopartikler med topotecan og antisense-oligonukleotid mot metastatisk brystkreft |
| [9445630](https://pubmed.ncbi.nlm.nih.gov/9445630/) | 1997 | Oversikt | Gynakol Geburtshilfliche Rundsch | Nye legemidler ved brystkreft |

---

## Informasjon om det norske markedet

| Tillatelsesnummer | Produktnavn | Doseringsform | Godkjent indikasjon |
|---------|------|------|-----------|
| EMEA/H/C/001192 | Topotecan Hospira (kansellert) | Ikke oppgitt | Livmorhalskreft, småcellet lungekreft |
| EMEA/H/C/000123 | Hycamtin (kansellert) | Ikke oppgitt | Eggstokkreft, livmorhalskreft, småcellet lungekreft |
| EMEA/H/C/002282 | Potactasol (kansellert) | Ikke oppgitt | Livmorhalskreft, småcellet lungekreft |

---

## Cytotoksisitet

| Punkt | Innhold |
|------|------|
| Cytotoksisitetsklassifisering | Konvensjonelt cytotoksisk (topoisomerase I-hemmer, kamptotecin-derivat) |
| Risiko for myelosuppresjon | Høy (benmargssuppresjon er den viktigste dosebegrensende toksisiteten) |
| Emetogenisitet | Lav til moderat |
| Overvåkingspunkter | Fullstendig blodstatus med differensialtelling, lever- og nyrefunksjon |
| Håndteringsbeskyttelse | Må følge gjeldende regler for håndtering av cytotoksiske legemidler |

Kunnskapsgrafen for legemiddel–sykdom nevner trombocytopeni, nøytropeni, agranulocytose, anemi, interstitiell lungesykdom, diaré, nedsatt nyrefunksjon og lungefibrose som tilstander med kontraindikasjonskobling. Se preparatomtalen for detaljerte advarsler.

---

## Sikkerhetsvurderinger

- **Kontraindikasjoner fra kunnskapsgrafen (ikke fra preparatomtale):** trombocytopeni, nøytropeni, agranulocytose, anemi (inkludert makrocytær anemi), interstitiell lungesykdom, diarésykdom, nedsatt nyrefunksjon, lungefibrose og postinflammatorisk lungefibrose.
- **Legemiddelinteraksjoner:** 100 interaksjoner er funnet totalt. Blant de som er vist, er de viktigste:
  - **Alvorlige (Major):** deferipron, samarium (153Sm) lexidronam
  - **Moderate:** eliglustat, rolapitant, jobenguan (I-131), palifermin, strontiumklorid Sr-89, ibritumomab tiuxetan
  - **Milde:** levofloksacin, koffein
  - Flere andre (blant annet morfin, omeprazol, ondansetron, deksametason) har uklart interaksjonsnivå.

Advarsler og kontraindikasjoner fra preparatomtalen mangler i de innsamlede dataene. Se preparatomtalen for fullstendig sikkerhetsinformasjon.

---

## Konklusjon og neste steg

**Beslutning: Hold**

**Begrunnelse:**
TxGNN-scoren er svært høy, men den kliniske støtten for brystkreft er svak: én avsluttet fase 2-studie med høydose kombinasjon, en fase 2-studie uten tegn til økt effekt og fase 1-studier der topotecan ikke er hovedmiddel. I tillegg er det mulig BCRP-mediert resistens, og alle norske tillatelser er kansellert.

**For å gå videre kreves følgende:**
- Sikkerhetsdata fra preparatomtalen (advarsler og kontraindikasjoner), som er en blokkerende datamangel
- Detaljerte data om virkningsmekanisme fra legemiddeldatabasen
- Kontrollerte kliniske studier som tester topotecan spesifikt ved brystkreft, gjerne i utvalgte subtyper (MYC-drevet, trippelnegativ)
- Vurdering av BCRP-uttrykk som mulig prediktiv biomarkør
- Avklaring av tilgjengelighet i Norge, siden alle tillatelser er kansellert

---

*Merknad om øvrige prediksjoner:* Rangene 2–10 (kjønnscelletumor hos voksne og ulike mønstre av testikulær plommesekksvulst) har enten indirekte evidens (L2, hovedsakelig fra pediatrisk nevroblastom, retinoblastom og gliom) eller ingen studier (L5). De er ikke vurdert i detalj her.
## Ansvarsfraskrivelse

Dette innholdet er kun til forskningsformål og utgjør ikke medisinsk rådgivning.
Klinisk validering kreves før enhver klinisk anvendelse.

---

