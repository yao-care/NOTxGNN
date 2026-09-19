---
layout: default
title: Ezetimibe
parent: Høy evidens (L1-L2)
nav_order: 146
evidence_level: L1
indication_count: 4
---

# Ezetimibe
{: .fs-9 }

Evidensnivå: **L1** | Predikerte indikasjoner: **4** stk.
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

# Ezetimibe: Fra hyperkolesterolemi til hyperlipoproteinemi

## Sammendrag i én setning

> Ezetimibe er en NPC1L1-inhibitor som blokkerer intestinal kolesterolabsorpsjon, etablert som tilleggsbehandling for hyperkolesterolemi og dyslipidemier.
> TxGNN-modellens toppresultat, **Hyperlipoproteinemi**, støttes av **80+ kliniske forsøk** og **20+ publikasjoner** — men denne bevissamlingens egen mekanistiske begrunnelse markerer det som legemidlets *eksisterende* godkjente bruk snarere enn et genuint nytt bruksområde.
> Et mer novelt, men betydelig svakere signal vises lenger ned på den rangerte listen (se forbehold nedenfor).

---

## Rask oversikt

| Element | Innhold |
|------|------|
| Originalindikasjon | Ikke dokumentert i norske regulatoriske dokumenter (legemiddel ikke markedsført lokalt, 0 autoriseringer); litteratur i denne pakken bekrefter at ezetimbes etablerte bruk er LDL-C-senking / hyperkolesterolemibehandling |
| Predikert ny indikasjon | Hyperlipoproteinemi |
| TxGNN-prediksjonspoengsum | 99.63% |
| Bevisnivå | L1 |
| Norges markedsstatus | ✗ Ikke markedsført |
| Antall autoriseringer | 0 |
| Anbefalt beslutning | Gå videre med sikringsmekanismer |

---

## Hvorfor er denne prediksjonen rimelig?

For tiden er det ingen strukturert virkningsmåte-felt tilgjengelig (`original_moa: [Data Gap]`), men bevissamlingens mekanistiske begrunnelse gir den underliggende farmakologien: **ezetimibe blokkerer selektivt NPC1L1 (Niemann-Pick C1-Like 1)-transportøren på tarmens børstegrenseflate**, blokkerer absorpsjon av dietetisk og biliær kolesterol. Dette senker LDL-C og produserer en synergistisk lipidsenkende effekt når det kombineres med statiner.

**Viktig forbehold:** modellens rang-1-prediksjon, *hyperlipoproteinemi*, er eksplisitt kommentert i bevissamlingens egen `repurposing_rationale` som *"legemidlets eksisterende godkjente indikasjon, ikke et nytt brukssignal"* (原文: 此為藥物之既有核准適應症，非新用途訊號). Rang-2-prediksjonen, *familiær hyperkolesterolemi*, er på samme måte beskrevet som en *"standard tilleggsbehandling"* allerede i klinisk bruk — ikke en ombrukskandidat. Begge er derfor best lest som **modellvalidering** (TxGNN korrekt gjenhenter kjente indikasjoner) snarere enn nye ombruksmuligheter.

Det genuint utforsket signalet i dette kandidatsett er rang 3, *hyperkolesterolemi på grunn av CYP7A1 (kolesterol 7α-hydroxylase)-mangel* — en sjelden monogen gallesyresynteseforstyrrelse der NPC1L1-blokkering teoretisk kunne redusere kolesterol/gallesyre-resirkulering. Imidlertid har dette kun **L4-bevis** (mekanistisk ekstrapolering, ingen kliniske forsøk) og er arrangert som et **Forsøksspørsmål**, ikke klart for videre tiltak. Rang 4 (CETP-mangel) er ustøttet (L5, Hold) siden denne tilstanden typisk presenteres med forhøyet, ikke mangel, HDL-C — mekanistisk frakoblet fra ezetimbes virkning.

---

## Kliniske forsøksbevis

*(Bevis for rang-1-prediksjon: Hyperlipoproteinemi)*

| Forsøksnummer | Fase | Status | Antall deltakere | Hovedfunn |
|---------|------|------|------|---------|
| [NCT00093899](https://clinicaltrials.gov/study/NCT00093899) | Fase 3 | Fullført | 611 | Ezetimibe/simvastatin + fenofibratt samadministrering senker kolesterol og triglyserider ved blandet hyperlipidemier |
| [NCT06005597](https://clinicaltrials.gov/study/NCT06005597) | Fase 3 | Fullført | 407 | Obicetrapib + ezetimibe fastdose-kombinasjon i tillegg til maksimal lipidsenkende terapi ved HeFH/ASCVD |
| [NCT01763827](https://clinicaltrials.gov/study/NCT01763827) | Fase 3 | Fullført | 615 | Ezetimibe som aktiv komparator mot evolocumab for LDL-C-senking |
| [NCT01043380](https://clinicaltrials.gov/study/NCT01043380) | Fase 4 | Fullført | 245 | PRECISE-IVUS: ezetimibe+statin mot statin alene på koronar plakk-regresjon ved intravaskulær ultralyd |
| [NCT00092833](https://clinicaltrials.gov/study/NCT00092833) | Fase 3 | Avsluttet | 49 | Ezetimibe 10 mg/dag åpen-label behandlingsforsøk ved homozygot FH / homozygot sitosterolemi |
| [NCT00092560](https://clinicaltrials.gov/study/NCT00092560) | Fase 3 | Fullført | 587 | Fenofibratt + ezetimibe samadministrering effektivitet/sikkerhet ved blandet hyperlipidemier |
| [NCT00349284](https://clinicaltrials.gov/study/NCT00349284) | Fase 3 | Fullført | 181 | Fenofibratt mot ezetimibe mot kombinasjon ved type IIb dyslipidemier forbundet med metabolsk syndrom |
| [NCT00843661](https://clinicaltrials.gov/study/NCT00843661) | Fase 4 | Ukjent | 60 | Ezetimibe+fenofibratt mot pravastatin-monoterapi ved HIV-pasienter på proteasehemmere |
| [NCT03434613](https://clinicaltrials.gov/study/NCT03434613) | Fase 4 | Fullført | 64 | Statinmonoterapi mot statin/ezetimibe-kombinasjons effekt på hepatisk steatose ved NAFLD |
| [NCT04862260](https://clinicaltrials.gov/study/NCT04862260) | Tidlig fase 1 | Aktiv, ikke rekrutterer | 3 | Utforskende kolesterol-metabolismeomprogrammering (ezetimibe+atorvastatin+evolocumab) ved pankreatisk adenokarsinom |

---

## Litteraturbevis

*(Bevis for rang-1-prediksjon: Hyperlipoproteinemi)*

| PMID | År | Type | Tidsskrift | Hovedfunn |
|------|-----|------|------|---------|
| [40347969](https://pubmed.ncbi.nlm.nih.gov/40347969/) | 2025 | RCT | Lancet | TANDEM-forsøk: obicetrapib+ezetimibe fastdose-kombinasjon reduserer LDL-C betydelig |
| [41206969](https://pubmed.ncbi.nlm.nih.gov/41206969/) | 2026 | RCT | JAMA | Oral PCSK9-inhibitor enlicitide evaluert ved HeFH-pasienter ikke ved målnivå på standard lipidsenkende terapi (inkl. ezetimibe) |
| [25939291](https://pubmed.ncbi.nlm.nih.gov/25939291/) | 2015 | Gjennomgang | Cardiology Clinics | Ezetimibe blant etablerte tilleggsbehandlinger for familiær hyperkolesterolemi |
| [38599725](https://pubmed.ncbi.nlm.nih.gov/38599725/) | 2024 | Gjennomgang | Indian Heart Journal | FH-underdiagnose/underbehandling; ezetimbes rolle i standardbehandling |
| [35593194](https://pubmed.ncbi.nlm.nih.gov/35593194/) | 2022 | Gjennomgang | J Cardiovasc Pharmacol Ther | PCSK9-hemmere gjennomgått mot bakgrunn statin/ezetimibe-terapi ved statin-intolerant og FH-pasienter |
| [40682836](https://pubmed.ncbi.nlm.nih.gov/40682836/) | 2025 | — | Molecular Medicine Reports | Gjennomgang av gjeldende hyperlipidemier-legemiddelklasser, inkl. kolesterolabsorpsjonshemmere |
| [33766264](https://pubmed.ncbi.nlm.nih.gov/33766264/) | 2021 | — | J American College of Cardiology | Nye/oppdukkende LDL-C- og ApoB-senkende terapier plassert ved siden av ezetimibe/PCSK9i |
| [30702994](https://pubmed.ncbi.nlm.nih.gov/30702994/) | 2019 | — | Circulation Research | Oversikt over kolesterolsenkende agentklasser, inkl. ezetimbes NPC1L1-mekanisme |
| [19654419](https://pubmed.ncbi.nlm.nih.gov/19654419/) | 2009 | — | Drug and Therapeutics Bulletin | Direkte gjennomgang/oppdatering av ezetimbes effektivitets- og sikkerhetsbeviser på den tiden |
| [34480646](https://pubmed.ncbi.nlm.nih.gov/34480646/) | 2021 | — | Current Cardiology Reports | Global byrde og behandlingstilnærminger for FH, inkl. ezetimibe |

---

## Norges markedsinformasjon

Ingen autorisasjonsposter finnes i bevissamlingen — `market_status = Ikke markedsført (Not Marketed)` med `total_licenses = 0`. Ezetimibe har for tiden ingen registrert produktlisens i Norge etter tilgjengelige data.

---

## Sikkerhetshensyn

Se pakningsvedlegget for sikkerhetsinformasjon. (`key_warnings`, `contraindications` og DDI-registre er alle flagget som datakløfter i denne bevissamlingen, og DDI-søkestatus er `not_found`.)

---

## Konklusjon og neste trinn

**Beslutning: Gå videre med sikringsmekanismer**

**Begrunnelse:**
Rang-1-signalet (hyperlipoproteinemi, L1-bevis) støttes av omfattende fase 3 RCT-data, men denne bevissamlingen selv identifiserer det som legemidlets *eksisterende* indikasjon snarere enn en ny ombruksmulighet — så "Gå videre med sikringsmekanismer"-kallet skal forstås som validering av ezetimbes etablerte bruk, ikke grønnlys for en ny indikasjon. Den ene kandidaten som ville representere genuint ombruk (CYP7A1-mangelshyperkolesterolemi, rang 3) forblir ved L4/Forsøksspørsmål-stadium og er ennå ikke handlingsbar.

**For å gå videre er det nødvendig med:**
- TFDA/norsk regulatorisk etikett-data (DG001, Blocking) — nødvendig før noen S1 sikkerhet pre-assessment
- Formell DrugBank-virkningsmåte-bekreftelse (DG002, High) for å erstatte den rationale-utledet mekanistiske oppsummeringen brukt her
- Hvis man forfølger CYP7A1-mangel-signalet: dedikert preklinisk/mekanistisk forskning, siden det ikke finnes kliniske forsøk for denne ultra-sjeldne indikasjonen
- Omdefiner rammeverket for "ny indikasjon" for denne kandidaten, siden rangene 1–2 i vesentlig grad overlapper med ezetimbes kjente etikett

## Ansvarsfraskrivelse

Dette innholdet er kun til forskningsformål og utgjør ikke medisinsk rådgivning.
Klinisk validering kreves før enhver klinisk anvendelse.

---

