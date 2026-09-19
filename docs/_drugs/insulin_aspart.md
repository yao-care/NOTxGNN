---
layout: default
title: Insulin Aspart
parent: Kun modellprediksjon (L5)
nav_order: 182
evidence_level: L5
indication_count: 10
---

# Insulin Aspart
{: .fs-9 }

Evidensnivå: **L5** | Predikerte indikasjoner: **10** stk.
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

# Insulin aspart: Fra diabetes mellitus til type 1 diabetes mellitus

## Sammendrag på én setning

Insulin aspart er et hurtigvirkende humaninsulinanalog som allerede brukes til å kontrollere blodsukker hos personer med diabetes mellitus.
TxGNN-modellens toppprediksjon er **type 1 diabetes mellitus**, støttet av **69 kliniske forsøk** og **20 publikasjoner**.
Dette er imidlertid legemidlets allerede etablerte kjerneindikasjoner snarere enn et nytt bruksområdessignal — se forbehold nedenfor.

## Oversikt

| Element | Innhold |
|---------|---------|
| Original indikasjon | Diabetes mellitus (type 1 og type 2) — per litteraturbevis (f.eks. PMID [12215068](https://pubmed.ncbi.nlm.nih.gov/12215068/)); ingen norsk lisenspost eksisterer for å bekrefte den formelle indikasjonsteksten |
| Forutsagt ny indikasjon | Type 1 diabetes mellitus |
| TxGNN prediktskår | 99.95% |
| Bevisnivå | L1 (≥2 fullførte fase 3 RCT-forsøk, f.eks. NCT02546401, NCT00474045, NCT00312156, NCT00046150) |
| Markedsstatus i Norge | ✗ Ikke markedsført |
| Antall autorisasjoner | 0 |
| Anbefalt beslutning | Avvent |

## Hvorfor er denne prediksjonen rimelig?

For tiden er detaljerte data for virkningsmekanisme ikke tilgjengelige (datakløft DG002). Basert på kjent informasjon er insulin aspart et hurtigvirkende humaninsulinanalog (en aminosyresubstitusjon på posisjon B28 av humaninsulin), og dets effektivitet ved senking av postprandielt glukose ved diabetes mellitus er allerede vel etablert og omfattende dokumentert i litteraturen og klinisk forsøksjournal gitt i denne bevisesken.

**Viktig forbehold:** I motsetning til en typisk bruksområdeskandidaten er TxGNN's topprangerte prediksjon her — «type 1 diabetes mellitus» — ikke en *ny* indikasjon. Det er legemidlets opprinnelig, allerede godkjent terapeutisk bruk. Dette mønsteret er vanlig når en legemiddel-sykdom-kant allerede er sterkt representert i kunnskapsgrafen som brukes til å trene TxGNN: modellen reproduserer i hovedsak en kjent assosiasjon snarere enn å avdekke en genuint ny bruksområdeshypotese. Det store volumet av fase 3 RCT-forsøk og oversikter bekrefter den *kjente* indikasjonen, men det bør ikke leses som bevis for en ny bruk.

Genuint nye kandidater på denne listen — som rang 2 «autoimmun ooforitt», rang 3 «opsismodysplasi», rang 6/7 varianter av stiv person-syndrom — har for tiden **ingen klinisk forsøks- eller litteraturstøtte**, så de kan ennå ikke evalueres. Rang 8 «pankreatisk agenesis» og rang 5 «permanent neonatal diabetes mellitus» er mekanistisk nærmere en sann sjelden-sykdom-bruksområdeshystorie (insulin brukes allerede off-label ved neonatal diabetes-syndromer) men har bare 1–2 støttepublikasjoner hver, utilstrekkelig for et formelt bevisnivå over L4.

## Klinisk forsøksbeviser

| Forsøksnummer | Fase | Status | Deltakere | Nøkkelfunn |
|---------|------|------|------|---------|
| [NCT02546401](https://clinicaltrials.gov/study/NCT02546401) | Fase 3 | Fullført | 22 | Insulin aspart før og etter måltid-timing ved bolus hos T1D-pasienter på insulinpumpe |
| [NCT00474045](https://clinicaltrials.gov/study/NCT00474045) | Fase 3 | Fullført | 470 | Insulin detemir vs NPH-insulin, begge kombinert med insulin aspart-bolus, hos gravide med T1D |
| [NCT00312156](https://clinicaltrials.gov/study/NCT00312156) | Fase 3 | Fullført | 347 | Insulin detemir vs NPH-insulin med måltidsinsulin aspart hos barn/ungdom med T1D |
| [NCT00046150](https://clinicaltrials.gov/study/NCT00046150) | Fase 3 | Fullført | 59 | HMR1964 vs insulin aspart sikkerhet i CSII-pumper for T1D |
| [NCT00992537](https://clinicaltrials.gov/study/NCT00992537) | Fase 1 | Fullført | 27 | PK/PD sammenligning av IDegAsp vs IDeg vs insulin aspart i T1D |
| [NCT01464099](https://clinicaltrials.gov/study/NCT01464099) | Fase 1 | Fullført | 24 | Bioequivalens av NovoLog 100 U/mL vs 200 U/mL formuleringer i T1D |
| [NCT03436498](https://clinicaltrials.gov/study/NCT03436498) | Fase 1 | Fullført | 45 | Sikkerhet av SAR341402 vs NovoLog i CSII-pumper hos voksne med T1D |
| [NCT00607087](https://clinicaltrials.gov/study/NCT00607087) | Fase 4 | Fullført | 289 | Insulin glulisine vs aspart vs lispro via CSII-pumpeparametere i T1D |
| [NCT02568280](https://clinicaltrials.gov/study/NCT02568280) | Fase 1 | Fullført | 42 | Postprandielt glukosemetabolisme med hurtigere virkende insulin aspart i T1D |
| [NCT00095446](https://clinicaltrials.gov/study/NCT00095446) | Fase 4 | Fullført | 513 | Ekstern CSII med insulin aspart vs insulin lispro i T1D og insulinkrevende T2D |

## Litteraturbeviser

| PMID | År | Type | Journal | Nøkkelfunn |
|------|-----|------|------|---------|
| [37863084](https://pubmed.ncbi.nlm.nih.gov/37863084/) | 2023 | RCT (fase 3a) | Lancet | ONWARDS 6: ukentlig insulin icodec vs daglig degludec, begge med insulin aspart-bolus, i T1D |
| [36623517](https://pubmed.ncbi.nlm.nih.gov/36623517/) | 2023 | RCT | Lancet Diabetes Endocrinol | EXPECT: insulin degludec vs detemir, begge med insulin aspart, hos gravide med T1D |
| [37804858](https://pubmed.ncbi.nlm.nih.gov/37804858/) | 2023 | RCT | Lancet Diabetes Endocrinol | CopenFast: hurtigere virkende insulin aspart vs insulin aspart i T1D/T2D graviditet og etter fødsel |
| [21333580](https://pubmed.ncbi.nlm.nih.gov/21333580/) | 2011 | Systematisk oversikt | Diabetes Metab | Effektivitet/sikkerhet av insulin aspart vs regulært humaninsulin i T1D og T2D |
| [35746893](https://pubmed.ncbi.nlm.nih.gov/35746893/) | 2023 | Metaanalyse | Diabetes Metab J | Hurtigere virkende aspart vs aspart via insulinpumpe i T1D |
| [41697686](https://pubmed.ncbi.nlm.nih.gov/41697686/) | 2026 | Oversikt | JAMA | Generell oversikt over type 1 diabetes patofysiologi og behandling |
| [37290466](https://pubmed.ncbi.nlm.nih.gov/37290466/) | 2023 | Oversikt | Lancet Diabetes Endocrinol | Behandling av T1D under graviditet: livsstil, farmakologi, teknologi |
| [15871555](https://pubmed.ncbi.nlm.nih.gov/15871555/) | 2003 | Oversikt | Treat Endocrinol | Fokusert oversikt over insulin aspart i T1D og T2D |
| [12215068](https://pubmed.ncbi.nlm.nih.gov/12215068/) | 2002 | Oversikt | Drugs | Omfattende oversikt over insulin asparts rolle i T1D og T2D-behandling |
| [25143741](https://pubmed.ncbi.nlm.nih.gov/25143741/) | 2014 | Oversikt | Vasc Health Risk Manag | Insulin degludec/aspart-kombinasjon for T1D og T2D |

## Norsk markedsinformasjon

For tiden ingen markedsautorisasjon på register — insulin aspart er ikke markedsført i Norge per tilgjengelige regulatoriske data (`market_status: Not marketed`, `total_licenses: 0`).

## Sikkerhetshensyn

Vær vennlig å se pakningsvedlegget for sikkerhetsinformasjon. **Merk:** datakløft DG001 (TFDA/pakningsvedlegg advarsler og kontraindikasjoner) er merket som *Blokkerande* i bevisesken — dette forhindrer en formell S1 sikkerhetspre-vurdering og må løses før noen beslutning utover Avvent.

## Konklusjon og neste trinn

**Beslutning: Avvent**

**Begrunnelse:**
Topprangeringen («type 1 diabetes mellitus») dupliserer insulin asparts allerede etablerte kjerneindikasjoner snarere enn å representere en genuint ny bruksområdesmulighet, så den gir begrenset inkrementell verdi. I tillegg forhindrer en blokkerande datakløft (manglende produktvedlegg/sikkerhet advarsler, DG001) og manglende MOA-data (DG002) en forsvarlig sikkerhetspre-vurdering, og legemidlet har for tiden ingen markedsautorisasjon i Norge.

**For å fortsette, er følgende nødvendig:**
- Løs DG001: innhent og analyser offisielle produktvedlegg advarsler/kontraindikasjoner
- Løs DG002: bekreft virkningsmekanisme via DrugBank API
- Omdefiner bruksområdespørsmålet mot lavere rangerte, genuint nye kandidater (f.eks. permanent neonatal diabetes mellitus, pankreatisk agenesis) og samle dedikert klinisk/litteraturbevis for disse, siden de for tiden bare har 1–2 støttepublikasjoner hver
- Klargjør norsk marked/licensing-vei, siden legemidlet ikke er markedsført der for tiden

## Ansvarsfraskrivelse

Dette innholdet er kun til forskningsformål og utgjør ikke medisinsk rådgivning.
Klinisk validering kreves før enhver klinisk anvendelse.

---

