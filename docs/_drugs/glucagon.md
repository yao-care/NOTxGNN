---
layout: default
title: Glucagon
parent: Kun modellprediksjon (L5)
nav_order: 164
evidence_level: L5
indication_count: 1
---

# Glucagon
{: .fs-9 }

Evidensnivå: **L5** | Predikerte indikasjoner: **1** stk.
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

# Glucagon: TxGNN-signal for irritabel tarmsyndrom — Advarsel om bevisinkongruens

## Sammendrag i én setning

> Glucagon (DrugBank DB00040) har ingen opprinnelig indikasjon eller virkemekanisme-data tilgjengelig i denne bevissamlingen, og det er ikke for tiden markedsført i Norge.
> TxGNN tildeler det en **99.24%** score for **Irritabel tarmsyndrom (IBS)**, men nesten alle de støttende **11 kliniske forsøkene** og **20 publikasjonene** handler faktisk om **GLP-1-receptor-agonister** (liraglutide, ROSE-010, exendin-4) — et hormon som deler en genefamilie med glucagon, men virker gjennom en annen reseptor med den **motsatte fysiologiske effekten**. Dette ser ut til å være et navn-basert forvirrings-signal heller enn en genuin gjenbruksmulig.

## Rask oversikt

| Element | Innhold |
|------|------|
| Opprinnelig indikasjon | Ikke gitt i evidenspakken (ingen Norge-lisens; virkemekanisme-datakløft registrert som DG002) |
| Predikert ny indikasjon | Irritabel tarmsyndrom (IBS) |
| TxGNN prediksjons-score | 99.24% |
| Bevisnivå | L5 |
| Norges-markeds-status | Ikke markedsført |
| Antall autorisasjoner | 0 |
| Anbefalt beslutning | Avvente |

## Hvorfor er denne prediksjonen rimelig?

For øyeblikket er detaljerte virkemekanisme-data for glucagon ikke tilgjengelig (DG002). Basert på generell farmakologi er glucagon og GLP-1 (glucagon-lignende peptid-1) begge spalteringsprodukter fra samme forløper, proglucagon, men de virker på ulike reseptorer — GCGR for glucagon kontra GLP-1R for GLP-1 — og gir **motsatte metabolske effekter**: glucagon øker blodsukkeret via hepatisk glykogenolyse, mens GLP-1-receptor-agonister senker glukose, bremser magetomlekking, og reduserer tarmbevegelse.

Når man gjennomgår den faktiske evidenspakken, handler **hvert klinisk forsøk og nesten hver publikasjon som støtter denne prediksjonen om GLP-1-receptor-agonister** (liraglutide, ROSE-010, exendin-4), ikke glucagon selv. Feltet for gjenbruksrasjonale flaggerer eksplisitt dette som sannsynlig "navn-basert forvirring" mellom genefamiliemedlemmene i proglucagon. Ingen forsøk eller publikasjon i denne pakken tester glucagon-administrering for IBS, og det finnes ingen mekanistisk vei som er foreslått der glucagon (et hyperglykemisk hormon) ville lindre IBS-symptomer på samme måte som sin reseptor-motsatte frende GLP-1 gjør.

**Kort sagt: dette er svært sannsynlig et falskt-positivt signal drevet av delt navn og genefamilies-avstamning, ikke en gyldig legemiddel-gjenbruksmulig for glucagon.**

## Klinisk forsøks-bevis

| Forsøks-nummer | Fase | Status | Inkludering | Viktige funn |
|---------|------|------|------|---------|
| [NCT05249023](https://clinicaltrials.gov/study/NCT05249023) | NA | Fullført | 37 | Butyraters rolle i kolons helse — ingen glucagon eller GLP-1-forbindelse |
| [NCT03256266](https://clinicaltrials.gov/study/NCT03256266) | N/A | Aktiv, rekrutterer ikke | 375 | Respons på nutrient/agenser hos organoid i tyndtarmen — urelatert til glucagon |
| [NCT04763564](https://clinicaltrials.gov/study/NCT04763564) | Fase 2 | Avsluttet | 8 | Liraglutide (en GLP-1-agonist, **ikke glucagon**) hos pasienter med ileal pouch; forsøk avsluttet tidlig med bare 8 deltakere |
| [NCT06333717](https://clinicaltrials.gov/study/NCT06333717) | NA | Fullført | 33 | Fullkorns rugbrødeffekt på tarm-hjerne-aksen — urelatert til glucagon |
| [NCT00802971](https://clinicaltrials.gov/study/NCT00802971) | NA | Fullført | 12 | Frukto-oligosakkarid-tilskudd og reaktiv hypoglykemi — ikke IBS/glucagon-terapi |
| [NCT04230655](https://clinicaltrials.gov/study/NCT04230655) | NA | Ukjent | 110 | Lavenergi-diett + magballongkirurgi for fedme — urelatert |
| [NCT06113146](https://clinicaltrials.gov/study/NCT06113146) | NA | Fullført | 41 | Spiseraten av ultraprosessert mat på stoffskiftet — urelatert |
| [NCT06408610](https://clinicaltrials.gov/study/NCT06408610) | NA | Fullført | 66 | Treningseffekt på tarmsdysbiose og **GLP-1** hos IBS-pasienter — igjen GLP-1, ikke glucagon |
| [NCT02731664](https://clinicaltrials.gov/study/NCT02731664) | Fase 1 | Fullført | 12 | Native **GLP-1** hemmer GI-motilitet — mekanistisk motsatt til glucagon |
| [NCT01056107](https://clinicaltrials.gov/study/NCT01056107) | Fase 1/2 | Fullført | 52 | ROSE-010 (en **GLP-1-analog**, ikke glucagon) ved forstoppelsesdominert IBS |

**Ingen av forsøkene ovenfor administrerer glucagon selv for IBS.**

## Litteratur-bevis

| PMID | År | Type | Tidsskrift | Viktige funn |
|------|-----|------|------|---------|
| [40134805](https://pubmed.ncbi.nlm.nih.gov/40134805/) | 2025 | Systematisk gjennomgang/Meta-analyse | Frontiers in Endocrinology | GLP-1-receptor-agonister forbedrer IBS-symptomer — bevis er for GLP-1-RA, ikke glucagon |
| [35234561](https://pubmed.ncbi.nlm.nih.gov/35234561/) | 2022 | RCT (sub-analyse) | Scandinavian Journal of Gastroenterology | ROSE-010 (GLP-1-analog) reduserer smerte under IBS-anfall hos en spesifikk subpopulasjon |
| [22517769](https://pubmed.ncbi.nlm.nih.gov/22517769/) | 2012 | RCT | Am J Physiol Gastrointest Liver Physiol | Randomisert, dobbeltblind, placebokontrollert dose-respons-studie av ROSE-010 (GLP-1-analog) på GI-motorfunksjon ved IBS-C |
| [30444291](https://pubmed.ncbi.nlm.nih.gov/30444291/) | 2019 | Gjennomgang | Experimental Physiology | Foreslår en rolle for GLP-1-sekreterende L-celler i IBS-patofysiologi |
| [28215540](https://pubmed.ncbi.nlm.nih.gov/28215540/) | 2017 | Klinisk studie | Clinics and Research in Hepatology and Gastroenterology | Lavere serum-GLP-1 korrelerer med buksmerte hos IBS-C-pasienter |
| [31602785](https://pubmed.ncbi.nlm.nih.gov/31602785/) | 2020 | Dyrestudie | Neurogastroenterology and Motility | Exendin-4 (en GLP-1-agonist) forbedret GI-dysfunksjon i en IBS-rottemodell |
| [23338623](https://pubmed.ncbi.nlm.nih.gov/23338623/) | 2013 | Dyrestudie | International Journal of Molecular Medicine | GLP-1s rolle i patogenesen av eksperimentelle IBS-rottemodeller |
| [40880735](https://pubmed.ncbi.nlm.nih.gov/40880735/) | 2025 | Klinisk studie | Frontiers in Nutrition | Lavt FODMAP-diett øker sirkulerende GLP-1 hos IBS-pasienter |
| [21694813](https://pubmed.ncbi.nlm.nih.gov/21694813/) | 2011 | Gjennomgang | Therapeutic Advances in Gastroenterology | Generelt IBS-behandlingslandskap (5-HT-midler, antidepressiver); diskuterer ikke glucagon |
| [30023410](https://pubmed.ncbi.nlm.nih.gov/30023410/) | 2018 | Gjennomgang | Cellular and Molecular Gastroenterology and Hepatology | Hjerne-tarm-mikrobiota-akse; generell bakgrunn, ikke glucagon-spesifikk |

**Hver relevant publikasjon diskuterer GLP-1 eller dets analoga — ingen studerer glucagon selv ved IBS.**

## Norges-markeds-informasjon

Glucagon (DB00040) har **ingen Norges-markeds-autorisasjon** i denne evidenspakken (0 lisenser, status: ikke markedsført).

## Sikkerhetshensyn

Se pakningsvedlegget for sikkerhetsinformasjon. Detaljerte advarsler, motindikasjoner og legemiddelinteraksjons-data for glucagon kunne ikke hentes for denne evalueringen (datakløft DG001 — TFDA-etikettadvarsler/motindikasjoner; blokkering for S1 sikkerhetsvurdering).

## Konklusjon og neste skritt

**Beslutning: Avvente**

**Rasjonale:**
TxGNN-scoren er høy, men i hovedsak alle støttende kliniske og litteratur-bevis gjelder GLP-1-receptor-agonister i stedet for glucagon selv. Glucagon og GLP-1, til tross for at de deler en genefamilies opprinnelse (proglucagon), virker på ulike reseptorer med motsatte fysiologiske effekter, så dette beviset kan ikke ekstrapoleres til å støtte glucagon-gjenbruk. Dette er konsistent med modellens egen bevis-nivå-vurdering (L5 — predikasjon kun, ingen direkte støttende studier) og pakkens egen gjenbruksrasjonale, som eksplisitt flaggerer sannsynlig navn-forvirring i proglucagon-genefamilien.

**For å fortsette er følgende nødvendig:**
- Løse DG001 (TFDA/offisiell etikett-advarsler og motindikasjoner) og DG002 (glucagon MOA) før videre sikkerhetsstadium-vurdering
- Kjør en målrettet litteratur/forsøks-søk begrenset til glucagon (GCGR-agonisme), unntatt GLP-1/GLP-1R-agonister, for å sjekke om noen direkte bevis finnes
- Hvis ingen direkte glucagon-spesifikke bevis finnes, nedprioriteringskandidat og registrer den som sannsynlig TxGNN falskt-positivt signal på grunn av navn-forvirring i proglucagon-genefamilien, for modell-QA-tilbakemelding

## Ansvarsfraskrivelse

Dette innholdet er kun til forskningsformål og utgjør ikke medisinsk rådgivning.
Klinisk validering kreves før enhver klinisk anvendelse.

---

