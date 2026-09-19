---
layout: default
title: Tocilizumab
parent: Kun modellprediksjon (L5)
nav_order: 360
evidence_level: L5
indication_count: 10
---

# Tocilizumab
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

# Tocilizumab: Fra revmatoid artritt til ankyloserende spondylitt

## Sammendrag i en setning

Tocilizumab er et humanisert anti-IL-6-reseptor monoklonalt antistoff med etablert bruk ved revmatoid artritt og andre IL-6-drevne inflammatoriske sykdommer. TxGNN-modellen predikerer at det kan være effektivt for **Ankyloserende Spondylitt (AS)**, med **9 kliniske studier** og **19 publikasjoner** tilgjengelige — men det dedikerte fase 3-programmet for denne eksakte indikasjonen ble allerede gjennomført og avsluttet tidlig på grunn av utilstrekkelig effektivitet.

---

## Hurtigoversikt

| Element | Innhold |
|---------|---------|
| Originalindikasjon | Ikke fanget opp i norske regulatoriske lisensdata (legemiddel ikke markedsført i Norge); etablert i litteraturens bevisgrunnlag som revmatoid artritt og andre IL-6-medierte inflammatoriske sykdommer (f.eks. sJIA/pJIA, gigantcellartritt) |
| Predikert ny indikasjon | Ankyloserende spondylitt |
| TxGNN-prediksjonspoeng | 99.99% |
| Bevisnivå | L1 (to dedikerte fase 3-RCT-er finnes, men begge ble avsluttet på grunn av mangel på effektivitet — se forbehold nedenfor) |
| Norgesmarkedsstatus | ✗ Ikke markedsført |
| Antall godkjenninger | 0 |
| Anbefalt beslutning | Vent |

---

## Hvorfor er denne prediksjonen rimelig?

For tiden er detaljerte mekanisme-for-handling-data fra DrugBank ikke tilgjengelige (datakløft DG002). Basert på informasjon som er tilstede i det koblede litteraturbevisgrunnlaget, er tocilizumab et rekombinant humanisert monoklonalt antistoff mot interleukin-6-reseptor (IL-6R), som blokkerer både membranbound og løselig IL-6R-signalering. Effektiviteten ved revmatoid artritt, systemisk/polyartikulær juvenil idiopatisk artritt og gigantcellartritt er godt etablert, og mekanistisk er IL-6 en plausibel drivkraft for enhver kronisk inflammatorisk reumatologisk sykdom — noe som forklarer hvorfor TxGNNs kunnskapsgraf plasserer ankyloserende spondylitt nær tocilizumabs kjente indikasjoner.

Imidlertid har denne mekanistiske hypotesen allerede blitt testet direkte hos pasienter. To dedikerte, spesialdesignede forsøk — en fase 3-studie hos TNF-utilstrekkelig responderende (NCT01209689) og en fase II/III sømløs pivotalstudie hos TNF-naive pasienter (NCT01209702) — ble begge **avsluttet tidlig**, og de samlete resultatene ble publisert som BUILDER-1/BUILDER-2-programmet (PMID 23765873), som konkluderte med at tocilizumab ikke ga klinisk meningsfull symptomatisk nytte ved AS. Den rådende forklaringen i støttende litteratur (f.eks. PMID 22452603, PMID 21803631) er at aksiale spondyloartrititter primært er drevet av IL-17/TNF-aksen i stedet for IL-6, ulikt revmatoid artritt. Den høye TxGNN-likhetsscoren reflekterer derfor sannsynligvis grafnærhet mellom AS og tocilizumabs godkjente indikasjoner snarere enn en validert ny terapeutisk effekt.

---

## Klinisk dokumentasjonsgrunnlag

| Studiernummer | Fase | Status | Innrulling | Nøkkelfunn |
|---------|------|------|------|---------|
| [NCT01209689](https://clinicaltrials.gov/study/NCT01209689) | Fase 3 | Avsluttet | 113 | RCT av tocilizumab (4 eller 8 mg/kg IV) versus placebo hos AS-pasienter med utilstrekkelig respons på tidligere TNF-antagonister; avsluttet tidlig |
| [NCT01209702](https://clinicaltrials.gov/study/NCT01209702) | Fase 2/3 | Avsluttet | 306 | Pivotal sømløs RCT av tocilizumab versus placebo hos TNF-naive, NSAID-refraktære AS-pasienter; avsluttet tidlig |
| [NCT05670301](https://clinicaltrials.gov/study/NCT05670301) | I/T | Rekrutterer | 2 500 | Observasjonell sitokin-/biomarkørprofilering på tvers av systemiske inflammatoriske sykdommer, ikke AS-spesifikk |
| [NCT01965132](https://clinicaltrials.gov/study/NCT01965132) | I/T | Rekrutterer | 10 000 | Koreansk landsdekkende register for biologika/tsDMARD-sikkerhet som omfatter RA-, AS- og PsA-pasienter |
| [NCT02569736](https://clinicaltrials.gov/study/NCT02569736) | I/T | Fullført | 60 | Mekanistisk studie av tocilizumabs effekt på T-follikkelhjelper- og B-cellemodenhet ved RA (ikke AS) |
| [NCT02925338](https://clinicaltrials.gov/study/NCT02925338) | I/T | Fullført | 1 431 | Virkelighetstro observasjonelt register for Inflectra (infliximab), tocilizumabs relevans indirekte |
| [NCT05696106](https://clinicaltrials.gov/study/NCT05696106) | I/T | Ukjent | 750 000 | Stor epidemiologisk studie på risiko for en andre immun-mediert inflammatorisk sykdom hos pasienter som allerede er behandlet for en IMID |
| [NCT07138898](https://clinicaltrials.gov/study/NCT07138898) | Fase 2 | Ennå ikke under rekruttering | 80 | Perioperativ immunsuppressiv håndtering hos reumatologipasienter som gjennomgår skulderartroplastitangi, ikke en AS-effektivitetsstudie |
| [NCT07477795](https://clinicaltrials.gov/study/NCT07477795) | Fase 2 | Ennå ikke under rekruttering | 52 | Secukinumab (ikke tocilizumab)-studie ved Takayasu-arteritt; bare tangensielt relevant via delt IL-6/T-celle-veibasert rasjonale |

---

## Litteraturbevis

| PMID | År | Type | Tidsskrift | Nøkkelfunn |
|------|-----|------|------|---------|
| [23765873](https://pubmed.ncbi.nlm.nih.gov/23765873/) | 2014 | RCT (samlet rapport) | Annals of the Rheumatic Diseases | BUILDER-1/BUILDER-2: tocilizumab klarte ikke å vise meningsfull korttids symptomatisk effektivitet ved AS |
| [26986130](https://pubmed.ncbi.nlm.nih.gov/26986130/) | 2016 | Systematisk gjennomgang / Nettverksmetaanalyse | Medicine | Sammenlignende effektivitet av biologiske regimer for AS; IL-6-blokk er underordnet TNF/IL-17-blokkere |
| [22452603](https://pubmed.ncbi.nlm.nih.gov/22452603/) | 2012 | Gjennomgang | Inflammation & Allergy Drug Targets | Gjennomgår rasjonale og begrenset klinisk bevis for IL-6-antagonisme spesifikt ved AS |
| [21803631](https://pubmed.ncbi.nlm.nih.gov/21803631/) | 2011 | Gjennomgang | Joint Bone Spine | Biologiske midler for AS utover TNFα-antagonister, inkludert IL-6-veimidler |
| [33981717](https://pubmed.ncbi.nlm.nih.gov/33981717/) | 2021 | Kasuistikk / Gjennomgang | Frontiers in Medicine | To tilfeller av vellykket tocilizumab-behandling av AA-amyloidose som kompliserer AS |
| [29290076](https://pubmed.ncbi.nlm.nih.gov/29290076/) | 2018 | Metaanalyse | Clinical Rheumatology | Risiko for alvorlig infeksjon med biologika (inkludert IL-6-hemmer) i aksiale SpA/AS-RCT-er |
| [19822066](https://pubmed.ncbi.nlm.nih.gov/19822066/) | 2009 | Gjennomgang | Clinical and Experimental Rheumatology | Kontrasterer biologisk effektivitet mellom RA og AS, og merker ulik patogenese |
| [28413099](https://pubmed.ncbi.nlm.nih.gov/28413099/) | 2017 | Gjennomgang | Seminars in Arthritis and Rheumatism | Optimalisering av annenlinjeterapibiologikum på tvers av RA, PsA og AS |
| [22450391](https://pubmed.ncbi.nlm.nih.gov/22450391/) | 2012 | Gjennomgang | Current Opinion in Rheumatology | Behandlingsalternativer for AS refraktær overfor TNF-inhibisjon, inkludert alternative cytokinmål |
| [27789989](https://pubmed.ncbi.nlm.nih.gov/27789989/) | 2009 | Gjennomgang | Open Access Rheumatology | Omfattende gjennomgang av biologika tilgjengelig for RA, AS og PsA |

---

## Markedsinformasjon for Norge

Tocilizumab er for tiden **ikke markedsført i Norge** under denne bevissamlingen (`market_status: Not marketed`, `total_licenses: 0`). Ingen godkjenningsregistreringer er tilgjengelige.

---

## Sikkerhetshensyn

Vennligst se pakningsvedlegget for sikkerhetsinformasjon. (Strukturerte advarsler, kontraindikasjoner og interaksjonsdata for legemidler var ikke tilgjengelige i denne bevissamlingen — datakløft DG001, flagget som Blocking alvorlighetsgrad.)

---

## Konklusjon og neste steg

**Beslutning: Vent**

**Begrunnelse:**
Den høye TxGNN-prediksjonsscoren for ankyloserende spondylitt støttes ikke av kliniske utfallsdata — de to dedikerte fase 3-studiene designet spesifikt for å teste denne hypotesen (NCT01209689, NCT01209702) ble avsluttet tidlig på grunn av utilstrekkelig effektivitet, og de publiserte samlete resultatene (PMID 23765873) bekrefter ingen meningsfull symptomatisk nytte. Denne indikasjonen bør ikke gå videre som en gjenbrukskandidat.

**For å gå videre, følgende er nødvendig:**
- TFDA/norsk pakningsvedlegg (advarsler, kontraindikasjoner) — for tiden en Blocking datakløft (DG001)
- Bekreftet DrugBank mekanisme-for-handling-post (DG002)
- Hvis gjenbruksarbeid fortsetter for dette legemiddelet, vurder å omdirigere evalueringen til **revmatoid vaskulitt** (rangering 2 i denne pakken, bevisnivå L4, beslutningsstadium S1, "Forskningsspørsmål") — en alvorlig ekstra-artikulær manifestasjon av legemidlets allerede godkjente moderindikasjon (RA), støttet av refraktærkasuistikker og sterkere mekanistisk plausibilitet, i stedet for ankyloserende spondylitt

## Ansvarsfraskrivelse

Dette innholdet er kun til forskningsformål og utgjør ikke medisinsk rådgivning.
Klinisk validering kreves før enhver klinisk anvendelse.

---

