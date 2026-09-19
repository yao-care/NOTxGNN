---
layout: default
title: Busulfan
parent: Høy evidens (L1-L2)
nav_order: 65
evidence_level: L2
indication_count: 10
---

# Busulfan
{: .fs-9 }

Evidensnivå: **L2** | Predikerte indikasjoner: **10** stk.
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

# Busulfan: Fra alkylerende kjemoterapiagent til myelodystrofisk syndrom

## Sammendrag i én setning

> Busulfan er et bifunksjonelt alkylerende middel som klassisk brukes i kjemototerapi og, mer nylig, som en hjørnesten i pre-transplantasjonskondisjoneringsskjemaer; denne dokumentasjonen inneholder ikke et formelt kodet «opprinnelig indikasjons»-felt, men de underliggende mekanistiske dataene beskriver det som en standardkomponent i allogeneisk hematopoietisk stamcelletransplantasjon (HSCT) kondisjoneringen.
> TxGNN-modellen predikerer at det kan være effektivt for **Myelodystrofisk syndrom (MDS)**,
> støttet av **50 kliniske studier** og **20 publikasjoner** — mye av dette gjenspeiler allerede etablert standardbehandling snarere enn et virkelig nytt omdisponerings-signal.

---

## Rask oversikt

| Element | Innhold |
|---------|---------|
| Opprinnelig indikasjon | Ikke dokumentert i denne dokumentasjonen (`original_indications` er tom; `original_moa` markert som datamangel). Busulfan er et klassisk alkylerende middel historisk brukt for cytoreduktiv kjemoterapi og som HSCT-kondisjonerig. |
| Predikert ny indikasjon | Myelodystrofisk syndrom (MDS) |
| TxGNN-prediksjonspoengsum | 99,62% |
| Bevisnivå | L2 |
| Markedsstatus Norge | ✗ Ikke markedsført |
| Antall autorisasjoner | 0 |
| Anbefalt avgjørelse | Fortsett med forholdsregler |

---

## Hvorfor er denne prediksjonen rimelig?

Detaljerte formelle MOA-data (DrugBank `original_moa`) er ikke tilgjengelige i denne dokumentasjonen. Basert på den mekanistiske begrunnelsen som *er* fanget i dokumentasjonens `repurposing_rationale`, er busulfan et bifunksjonelt alkylerende middel som danner tverrbindinger i DNA, som produserer potent, dose-avhengig myelotoksisitet. Denne egenskapen har historisk blitt utnyttet for cytoreduktiv kjemoterapi (klassisk ved kronisk myeloid leukemi, før tyrosinkinase-inhibitor-epoken) og — mer sentralt for bevisene samlet her — som en standardkomponent i myeloablativ eller redusert-intensitets **kondisjoneringsskjemaer** før allogeneisk HSCT, typisk kombinert med fludarabin eller syklofosfamid.

Forholdet mellom busulfans etablerte farmakologi og den øverste predikerte indikasjonen, MDS, er direkte snarere enn spekulativt: MDS er en klonal hematopoietisk stamcellesykdom som allogeneisk HSCT er det eneste potensielt kurative alternativet for, og busulfan-basert kondisjonerig er allerede den kliniske standarden som brukes til å ablate den syke hematopoietiske klonen og muliggjøre donorens stamcelle-engraftment. Som dokumentasjonen selv bemerker for denne kandidaten: *«dette er ikke en virkelig ny indikasjon, men snarere en konsolidering av bevis for en allerede etablert standardklinisk bruk.»*

Mekanistisk er denne cytotoksiske/myeloablative handlingen sykdomsuavhengig med hensyn til hvilken abnorm hematopoietisk klon som blir slettet — som er hvorfor modellens neste flere rangerte prediksjoner (refraktær cytopeni i barndom, uklassifisert MDS, 5q- delesjonssyndrom, aregenerativ/alvorlig aplastisk anemi) alle klynges rundt samme underliggende mekanisme: busulfan renser margen for å muliggjøre transplantasjon. Et mer eksplorativt signal — busulfan-kondisjonerig for å muliggjøre engraftment av CCR5-modifiserte eller genredigerte CD34+-celler i HIV-kurstrategier (rang 7) — utvider samme mekanisme til en eksperimental, ikke-onkologisk kontekst og har vesentlig svakere, stort sett fase 1-bevis.

---

## Bevis fra kliniske studier
*(for topprankert predikert indikasjon: Myelodystrofisk syndrom)*

| Studie-nummer | Fase | Status | Registrering | Viktige funn |
|---------|------|------|------|---------|
| [NCT06477549](https://clinicaltrials.gov/study/NCT06477549) | Fase 2 | Rekrutterer | 220 | RCT sammenligner bendamustine kontra ruxolitinib lagt til fludarabin/busulfan-kondisjonerig i haploidentisk HSCT; gradert A relevans — stor, direkte på-mekanisme. |
| [NCT02250937](https://clinicaltrials.gov/study/NCT02250937) | Fase 2 | Aktiv, ikke rekrutterende | 116 | Randomisert studie av venetoclax med tidspunkt-sekvensielt busulfan/cladribin/fludarabin-kondisjonerig i AML og MDS; gradert A relevans. |
| [NCT00416598](https://clinicaltrials.gov/study/NCT00416598) | Fase 2 | Avsluttet | 546 | Stor studie av decitabin vedlikeholdelse etter busulfan-inneholdende induksjon/intensivasjon i AML; gradert B (busulfan som bakgrunnsagent). |
| [NCT00454480](https://clinicaltrials.gov/study/NCT00454480) | Fase 2/3 | Avsluttet | 2000 | Stort behandlingsutviklingsprogram for eldre AML- og høyrisikopasienter med MDS som inkorporerer busulfan-baserte skjemaer. |
| [NCT00226512](https://clinicaltrials.gov/study/NCT00226512) | Fase 3 | Trukket tilbake | 203 | Multisenter-RCT av ikke-myeloablativ fludarabin/busulfan-kondisjonerig ± anti-lymfocytt-antistoff for AML/MDS allo-HSCT. |
| [NCT00002989](https://clinicaltrials.gov/study/NCT00002989) | Fase 3 | Ukjent | 207 | Randomisert studie som vurderer intensivering av kondisjoneringsskjemaet for allo-HSCT i leukemi/MDS med høyt recidivrisiko. |
| [NCT00301834](https://clinicaltrials.gov/study/NCT00301834) | Fase 2 | Avsluttet | 35 | Fludarabin/busulfan/alemtuzumab som redusert-toksisitet ablativ kondisjonerig for barn med marvfeilsyndromer eller MDS/leukemi. |
| [NCT01177371](https://clinicaltrials.gov/study/NCT01177371) | Fase 2 | Avsluttet | 13 | Høydose busulfan + syklofosfamid etterfulgt av allogeneisk BMT for leukemi, MDS, myelom og lymfom. |
| [NCT00186342](https://clinicaltrials.gov/study/NCT00186342) | N/A | Avsluttet | 120 | Busulfan/etopid/syklofosfamid-kondisjonerig; tolerabilitet/effektivitet i akutt leukemi og MDS/MPD-pasienter i alderen 51–60. |
| [NCT02861417](https://clinicaltrials.gov/study/NCT02861417) | Fase 2 | Aktiv, ikke rekrutterende | 204 | Tidspunkt-sekvensielt busulfan pluss post-transplantasjons-syklofosfamid for allogeneisk transplantasjon i blodkrefttyper. |

*40 ytterligere studier i dokumentasjonen ble ikke inkludert ovenfor for brevhetens skyld; de fleste er generelle hematologisk-malignitet/HSCT-kondisjoneringsstudier der busulfan er en bakgrunnskomponent snarere enn primær studieintervensjon.*

---

## Litteraturbeviser
*(for topprankert predikert indikasjon: Myelodystrofisk syndrom)*

| PMID | År | Type | Tidsskrift | Viktige funn |
|------|-----|------|------|---------|
| [35617104](https://pubmed.ncbi.nlm.nih.gov/35617104/) | 2022 | RCT | American Journal of Hematology | Sluttanalyse av en fase III RCT: treosulfan-basert kondisjonerig viser ikke-inferiør/overlegen event-fri overlevelse kontra redusert-intensitets busulfan hos eldre AML/MDS-pasienter. |
| [31606445](https://pubmed.ncbi.nlm.nih.gov/31606445/) | 2020 | RCT | The Lancet Haematology | Randomisert, ikke-inferiøritets fase 3 studie: treosulfan kontra busulfan+fludarabin-kondisjonerig før allo-HSCT hos eldre AML/MDS-pasienter. |
| [36702138](https://pubmed.ncbi.nlm.nih.gov/36702138/) | 2023 | RCT (fase 3) | The Lancet Haematology | Åpen-etikett, multisenter-RCT: G-CSF+decitabin+busulfan-syklofosfamid kontra busulfan-syklofosfamid-kondisjonerig for å redusere recidiv i MDS/sekundær AML. |
| [28380315](https://pubmed.ncbi.nlm.nih.gov/28380315/) | 2017 | RCT (fase 3) | Journal of Clinical Oncology | Randomisert sammenligning av myeloablativ kontra redusert-intensitets kondisjonerig (busulfan-inneholdende) for AML/MDS allo-HSCT. |
| [34692485](https://pubmed.ncbi.nlm.nih.gov/34692485/) | 2021 | Meta-analyse av RCT | Frontiers in Oncology | Redusert-intensitets kondisjonerig viser sammenlignbare resultater med myeloablativ kondisjonerig for AML/MDS allo-HSCT. |
| [33425740](https://pubmed.ncbi.nlm.nih.gov/33425740/) | 2020 | Systematisk oversikt/Meta-analyse | Frontiers in Oncology | Langtidsresultater av treosulfan- kontra busulfan-basert kondisjonerig for MDS og AML før HSCT. |
| [40079242](https://pubmed.ncbi.nlm.nih.gov/40079242/) | 2025 | Oversikt | American Journal of Hematology | Samtidsoversikt over allogeneisk HSCT for myelofibrose og MDS, inkludert valg av kondisjoneringsskjema. |
| [34489555](https://pubmed.ncbi.nlm.nih.gov/34489555/) | 2021 | Kohorte (register, propensity-matchet) | Bone Marrow Transplantation | Nasjonalt japansk register: fludarabin/busulfan kontra busulfan/syklofosfamid myeloablativ kondisjonerig for MDS. |
| [33471943](https://pubmed.ncbi.nlm.nih.gov/33471943/) | 2021 | Kohorte | Cancer | Fraksjonert IV busulfan myeloablativ kondisjonerig forbedrer overlevelse hos eldre AML/MDS-pasienter. |
| [37856098](https://pubmed.ncbi.nlm.nih.gov/37856098/) | 2024 | Bevisbasert risikovurdering | Pediatric Blood & Cancer | Bevisbasert vurdering av busulfan-eksponering og påfølgende malignitetsrisiko, relevant for ikke-malignt/genterapi-kondisjoneringbruk. |

*10 ytterligere publikasjoner i dokumentasjonen (stort sett retrospektive kohortestudier og kasuistikker om treosulfan/busulfan-sammenligninger og langsiktig toksisitet) ble ikke inkludert ovenfor for brevhetens skyld.*

---

## Markedsinformasjon Norge

Busulfan har for tiden **ingen markedsføringstillatelser** i det regelverksregister som er fanget opp av denne dokumentasjonen (`market_status`: ikke markedsført; `total_licenses`: 0). Ingen produktnavn, doseringsstyrke eller godkjent-indikajonstekst er tilgjengelig for uttrukking fra `taiwan_regulatory.licenses`.

---

## Cytotoksisitet

Busulfan oppfyller kriteriene for antineoplastisk/cytotoksisk: det er en klassisk alkylerende middel, og dokumentasjonens egen mekanistiske begrunnelse beskriver eksplisitt at det induserer «DNA-tverrbinding som fører til myeloablativ cytotoksisitet.»

| Element | Innhold |
|---------|---------|
| Cytotoksisitetsklassifisering | Konvensjonell cytotoksisk (alkylerende middel, alkylsulfon-klasse) |
| Myelosuprsjons risiko | Høy — busulfan brukes spesifikt for dets potente, myeloablative benmarg-rensende effekt i kondisjoneringsskjemaer; dypfinnende og vedvarende cytopenier forventes og er tilsiktet i denne sammenhengen. |
| Emetogenisitetsklassifisering | Moderat til høy (typisk for IV alkylerende midler ved myeloablativ/kondisjoneringsdoser; bekreft eksakt kategori mot pakningsvedlegget) |
| Overvåkingselementer | CBC med differensial, hepatisk funksjon (veno-oklusiv sykdom/SOS-risiko er en kjent busulfan-klassekonsern), lungekapasitet, og — der det brukes ved myeloablativ dosering — krampeprofylakse og plasmanivå (PK-veiledning) overvåking |
| Håndteringsbeskyttelse | Ja — standardiserte cytotoksisk/farlig stoff-håndteringsprinsipp kreves for klargjøring og administrasjon |

---

## Sikkerhetshensyn

Se pakningsvedlegget for sikkerhetsinformasjon. (`key_warnings`, `contraindications` og stoff-vekselvirkningsdata er alle markert som datamangel i denne dokumentasjonen; ingen DDI-poster ble funnet.)

---

## Konklusjon og neste trinn

**Avgjørelse: Fortsett med forholdsregler**

**Begrunnelse:**
Den øverst predikerte indikasjonen (MDS) støttes av sterke, stort sett fase 2–3 bevis (L2), inkludert flere randomiserte studier som direkte sammenligner busulfan-baserte kondisjoneringsskjemaer i denne populasjonen — dette er mindre en «ny» omdisponerings-hypotese og mer en datadrevet bekrefting av busulfans allerede-standardrolle i HSCT-kondisjonerig for MDS. Lavere-rangerte prediksjoner i denne dokumentasjonen spenner fra moderat støttet (refraktær cytopeni i barndom, alvorlig aplastisk anemi — L2/L3) til i hovedsak ikke-støttet modellartefakter (5q- delesjonssyndrom, seborrøisk keratose, felin AIDS — L5, ingen studier eller litteratur), og bør ikke avanseres uten dedikert bevis.

**For å fortsette er følgende nødvendig:**
- Offisiell Taiwan/Norge pakningsvedlegg (PI) advarsler og kontraindikasjoner — for tiden et **blokkerende datamangel (DG001)**; uten dette kan kandidaten ikke formelt passere S1 sikkerhets-pre-screening til tross for styrken av effektivitetsbevisene.
- Bekreftet DrugBank MOA-post (DG001/DG002) for å erstatte den antatte mekanistiske sammenfattingen som brukes i denne rapporten.
- Formelle `original_indications` og licensieringsdata, siden ingen var til stede i denne dokumentasjonen.
- Gitt at busulfan allerede mangler markedsføring tillatelse i Norge, en vurdering av markedsadgang/registreringsvei før ytterligere arbeider med klinisk posisjonering.

## Ansvarsfraskrivelse

Dette innholdet er kun til forskningsformål og utgjør ikke medisinsk rådgivning.
Klinisk validering kreves før enhver klinisk anvendelse.

---

