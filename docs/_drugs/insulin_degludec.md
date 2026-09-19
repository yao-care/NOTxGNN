---
layout: default
title: Insulin Degludec
parent: Kun modellprediksjon (L5)
nav_order: 183
evidence_level: L5
indication_count: 6
---

# Insulin Degludec
{: .fs-9 }

Evidensnivå: **L5** | Predikerte indikasjoner: **6** stk.
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

# Insulin degludec: En selvhenvisende prediksjon (Diabetes mellitus → Type 1 diabetes mellitus)

## Sammendrag i en setning

> Insulin degludec er en langtvirkende (ultralangtirkende) basal insulinanalog som brukes til behandling av diabetes mellitus. TxGNN-modellens topprangerte prediksjon (**Type 1 diabetes mellitus**, poengsum 99.44%) er ikke et genuint repurposering-signal — det tilsvarer legemidlets egen kjente kliniske bruk — men bevissamlingen er godt støttet av **58 kliniske forsøk** og **20 publikasjoner**, inkludert flere fullførte fase 3 RCT-er. De resterende fem rangerte kandidatene i denne samlingen er svakere, eksplorerende signaler med lite eller ingen direkte bevis.

---

## Rask oversikt

| Element | Innhold |
|------|------|
| Opprinnelig indikasjon | Diabetes mellitus, basal insulinterapi (eksakt regulatorisk indikasjon tekst ikke gitt i bevissamlingen — datakløft) |
| Predikert ny indikasjon | Type 1 diabetes mellitus *(selvhenvisende — se forbehold nedenfor)* |
| TxGNN prediksjonspoengsum | 99.44% |
| Bevisnivå | L1 (≥2 fullførte fase 3 RCT-er) |
| Taiwans markedsstatus | Ikke markedsført |
| Antall godkjennelser | 0 |
| Anbefalt beslutning | **Hold** (for repurposering-formål — se begrunnelse) |

---

## Hvorfor er denne prediksjonen rimelig?

For tiden er detaljert virkningsmekanisme-informasjon for insulin degludec ikke tilgjengelig i denne bevissamlingen (datakløft). Basert på etablert farmakologisk kunnskap, er insulin degludec en ultralangtirkende basal insulinanalog som danner løselige multiheksamer etter subkutan injeksjon, som deretter frigjøres langsomt og kontinuerlig til sirkulasjonen — noe som gir den en flat, stabil, ~24+ time virkningsprofil. Den brukes som eksogen erstatningsterapi for pasienter med absolutt eller relativ insulinmangel.

**Viktig forbehold om Rang 1:** Repurposering-begrunnelsen gitt med denne bevissamlingen sier eksplisitt at «type 1 diabetes mellitus» er insulin degludecs **opprinnelige, allerede godkjente indikasjon** — ikke en ny repurposering-kandidat. TxGNN har effektivt gjenoppdaget legemidlets egen kjente bruk. Dette er en kjent begrensning av grafbaserte legemiddel–sykdom lenke-prediksjonsmodeller: høysikre kantlinjer kan reflektere eksisterende kunnskap allerede innebygd i treningsgrafien i stedet for en genuint ny terapeutisk hypotese. Det omfattende kliniske forsøk og litteraturbevis nedenfor skal derfor leses som **bekreftende bevis for etablert effektivitet**, ikke som støtte for en ny indikasjon.

De genuint eksplorerende kandidatene i denne samlingen (rangeringer 2–6, oppsummert videre nedenfor) er mekanistisk mye svakere: de fleste reflekterer **sykdomskomorbidet** (f.eks. delt anti-GAD65 autoimmunitet mellom type 1 diabetes og stiff person syndrome) i stedet for en direkte farmakologisk effekt av insulin på den predikerte sykdommen selv.

---

## Klinisk forsøksbevis

*(for predicted_indications[0] — «type 1 diabetes mellitus», som er legemidlets kjente/opprinnelige indikasjon)*

| Forsøksnummer | Fase | Status | Inkludering | Nøkkelfunn |
|---------|------|------|------|---------|
| [NCT05463744](https://clinicaltrials.gov/study/NCT05463744) | Fase 3 | Fullført | 692 | Insulin efsitora alfa en gang per uke vs. insulin degludec hos T1D-pasienter på flere daglige injeksjoner |
| [NCT03214367](https://clinicaltrials.gov/study/NCT03214367) | Fase 3 | Fullført | 1392 | PRONTO-T1D: LY900014 vs. insulin lispro, begge kombinert med glargine eller degludec, hos T1D |
| [NCT02500706](https://clinicaltrials.gov/study/NCT02500706) | Fase 3 | Fullført | 1108 | Raskere virkende insulin aspart vs. NovoRapid, begge kombinert med degludec, hos voksne med T1D |
| [NCT01835431](https://clinicaltrials.gov/study/NCT01835431) | Fase 3 | Fullført | 362 | IDegAsp en gang daglig + aspart vs. detemir en/to ganger daglig + aspart hos barn/ungdom med T1D |
| [NCT04450407](https://clinicaltrials.gov/study/NCT04450407) | Fase 2 | Fullført | 266 | LY3209590 vs. insulin degludec hos T1D-pasienter tidligere på flere daglige injeksjoner |
| [NCT05767255](https://clinicaltrials.gov/study/NCT05767255) | Fase 3 | Ukjent | 66 | Basal-bolus insulin (inkl. degludec) vs. basal insulin + GLP-1 analog for hypoglykemi-risiko ved sykehusutskrivning |
| [NCT02536859](https://clinicaltrials.gov/study/NCT02536859) | Fase 1 | Fullført | 60 | PK/PD sammenligning av degludec vs. glargine U300 ved steady state hos T1D |
| [NCT00841087](https://clinicaltrials.gov/study/NCT00841087) | Fase 2 | Fullført | 65 | Sikkerhet av degludec + NovoRapid vs. detemir + NovoRapid, basal-bolus regimen, hos japanske T1D-pasienter |
| [NCT03400501](https://clinicaltrials.gov/study/NCT03400501) | Tidlig fase 1 | Fullført | 32 | Skoleveiledning degludec vs. glargine for å redusere ketose-risiko hos ungdom med dårlig kontrollert T1D |
| [NCT00992537](https://clinicaltrials.gov/study/NCT00992537) | Fase 1 | Fullført | 27 | PK/PD sammenligning av IDegAsp, degludec, og insulin aspart hos T1D |

---

## Litteraturbevis

| PMID | År | Type | Tidsskrift | Nøkkelfunn |
|------|-----|------|------|---------|
| [37863084](https://pubmed.ncbi.nlm.nih.gov/37863084/) | 2023 | RCT | Lancet | ONWARDS 6: insulin icodec en gang per uke vs. degludec daglig, basal-bolus regimen, hos T1D |
| [39270686](https://pubmed.ncbi.nlm.nih.gov/39270686/) | 2024 | RCT | Lancet | QWINT-5: insulin efsitora alfa en gang per uke vs. degludec daglig hos voksne med T1D |
| [36623517](https://pubmed.ncbi.nlm.nih.gov/36623517/) | 2023 | RCT | Lancet Diabetes Endocrinol | EXPECT: degludec vs. detemir (begge + aspart) hos gravide med T1D — non-inferiority studie |
| [34643020](https://pubmed.ncbi.nlm.nih.gov/34643020/) | 2022 | RCT | Diabetes Obes Metab | HypoDeg: degludec vs. glargine U100 hos T1D-pasienter utsatt for alvorlig nattlig hypoglykemi |
| [36610544](https://pubmed.ncbi.nlm.nih.gov/36610544/) | 2023 | RCT | Diabetes Res Clin Pract | INEOX: degludec 100 IE/mL vs. glargine 300 IE/mL effektivitet/sikkerhet hos T1D |
| [34763071](https://pubmed.ncbi.nlm.nih.gov/34763071/) | 2022 | RCT | Endocr Pract | BIGLEAP: degludec vs. aspart via insulinpumpe hos godt kontrollert T1D, crossover design |
| [36516429](https://pubmed.ncbi.nlm.nih.gov/36516429/) | 2023 | RCT | Diabetes Technol Ther | ULTRAFLEXI-1: glargine U300 vs. degludec U100 rundt spontan trening hos T1D |
| [36763996](https://pubmed.ncbi.nlm.nih.gov/36763996/) | 2022 | Systematisk gjennomgang / Meta-analyse | Clin Ther | Degludec vs. andre langtvirkende basale insuliner hos T1D/T2D — effektivitet og tolerabilitet |
| [35476308](https://pubmed.ncbi.nlm.nih.gov/35476308/) | 2022 | Systematisk gjennomgang | Int J Clin Pharm | Degludec U100 vs. glargine U300 hos T1D — sikkerhet, effektivitet, kostnadseffektivitet |
| [29477399](https://pubmed.ncbi.nlm.nih.gov/29477399/) | 2018 | Systematisk gjennomgang / Nettverks meta-analyse | Value Health | Basale insulinregimer for voksne med T1D — sammenlignende effektivitet og sikkerhet |

---

## Andre predikerte indikasioner (Eksplorerende, lavere bevis)

Denne bevissamlingen inneholder fem ytterligere TxGNN-rangerte kandidater. Ingen har for tiden støttende kliniske forsøk eller litteratur. Oppsummert for fullstendighet:

| Rangering | Sykdom | Poengsum | Bevisnivå | Anbefaling | Merknad |
|------|---------|-------|----------------|-----------------|------|
| 2 | Autoimmt oofritt | 99.23% | L5 | Hold | Ingen mekanistisk link identifisert utover mulig sameksistens i autoimmt polyglandulært syndrom; rent modellartefakt |
| 3 | Opsismodysplasi | 99.12% | L5 | Hold | Sjelden skjelettal dysplasi (INPPL1-mutasjon); ingen kjent vekselvirkning med insulinsignalering |
| 4 | Tiamin-responsivt dysfunksjonssyndrom (TRMA) | 99.10% | L4 | Forskningsspørsmål | TRMA inkluderer diabetes som del av dens triade; insulin ville bare behandlet den diabetiske komponenten symptomatisk, ikke den underliggende B1-transportørdefekten |
| 5 | Klassisk stiff person syndrome | 99.08% | L4 | Forskningsspørsmål | Deler anti-GAD65 autoantistoff-patofysiologi med T1D (forekommer sammen hos ~30–40% av SPS-pasienter); insulin behandler bare komorbid diabetes, ikke SPS nevrologiske symptomer |
| 6 | Fokal stiff limb syndrome | 99.08% | L4 | Forskningsspørsmål | SPS-spektrumvariant; samme anti-GAD65/T1D komorbidet forbehold som Rang 5 |

Ingen av disse bør fremmes uten uavhengig mekanistisk eller klinisk bevis.

---

## Informasjon om Taiwans marked

Insulin degludec innehar for tiden **ingen markedsføringstillatelser i Taiwan** (markedsstatus: Ikke markedsført; 0 lisenser på fil).

---

## Sikkerhetshensyn

Se pakningsvedlegget for sikkerhetsinformasjon. Ingen viktige advarsler, kontraindikasjoner eller legemiddelinteraksjonsvarsler var tilgjengelig i denne bevissamlingen.

---

## Konklusjon og neste trinn

**Beslutning: Hold**

**Begrunnelse:**
Den topprangerte kandidaten (Type 1 diabetes mellitus) er ikke en ny repurposering-mulighet — det er insulin degludecs eksisterende godkjente indikasjon, så det tilbyr ingen ny forretnings- eller klinisk verdi til tross for sitt sterke L1-bevisgrunnlag. De resterende fem kandidatene har alle svakt bevis (L4–L5), og flere (autoimmt oofritt, opsismodysplasi) mangler noen troverdig mekanistisk begrunnelse. De to mest biologisk plausible eksplorerende lederne — stiff person syndrome og fokal stiff limb syndrome — representerer sykdomskomorbidet via delt anti-GAD65 autoimmunitet, ikke en direkte farmakologisk effekt av insulin på den nevrologiske lidelsen selv, og støtter derfor ikke for tiden et repurposering-krav.

**For å fortsette er følgende nødvendig:**
- Løs **DG001** (Blokkering): få TFDA-merking/pakningsvedlegg (advarsler, kontraindikasjoner) før noen S1-sikkerhetsevaluering kan begynne
- Løs **DG002** (Høy): hent formell virkningsmekanisme-data fra DrugBank
- Hvis stiff person syndrome-hypotesen forfølges, bestill en målrettet litteraturgjennomgang av anti-GAD65 autoimmunitet og insulins potensielle immunomodulatoriske (ikke glykemiske) rolle — gjeldende bevissamling inneholder null støttende sitater
- Deprioritiser autoimmt oofritt og opsismodysplasi med mindre ny mekanistisk bevis fremkommer

## Ansvarsfraskrivelse

Dette innholdet er kun til forskningsformål og utgjør ikke medisinsk rådgivning.
Klinisk validering kreves før enhver klinisk anvendelse.

---

