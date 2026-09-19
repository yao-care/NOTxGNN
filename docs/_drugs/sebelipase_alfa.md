---
layout: default
title: Sebelipase Alfa
parent: Kun modellprediksjon (L5)
nav_order: 320
evidence_level: L5
indication_count: 10
---

# Sebelipase Alfa
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

# Sebelipase alfa: Fra uten markedsstatus i Norge til Lysosomal Acid Lipase Deficiency (Wolman-sykdom / Cholesteryl Ester Storage Disease)

## Sammendrag i en setning

Sebelipase alfa er ikke for tiden på det norske markedet og har ingen lokalt registrert godkjent indikasjon.
TxGNN-modellen — etter filtrering av flere mekanistisk usannsynlige toppsjanser — konvergerer korrekt på **Lysosomal Acid Lipase Deficiency (LAL-D)**, som spenner over infantil-debut-formen (**Wolman-sykdom**) og senere-debut-formen (**Cholesteryl Ester Storage Disease, CESD**), støttet av **9 kliniske forsøk (inkludert 1 fullført fase 3 RCT)** og **~19 publikasjoner**.

---

## Rask oversikt

| Punkt | Innhold |
|------|------|
| Opprinnelig indikasjon | Ingen på fil — ikke markedsført i Norge (dataforskjell). Globalt godkjent som Kanuma® for LAL-D siden 2015 (PMID 26452566). |
| Forutsagt ny indikasjon | Lysosomal Acid Lipase Deficiency (Wolman-sykdom / Cholesteryl Ester Storage Disease) |
| TxGNN prediksjonspoengsum | ~99.7% (Wolman-sykdom 99.72% / CESD 99.72%) |
| Bevisnivå | L2 (1 fullført pivot fase 3 RCT — ARISE, NCT01757184 — pluss flere langsiktige kohort-/forlengelsestudier) |
| Norsk markedsstatus | ✗ Ikke markedsført |
| Antall godkjennelser | 0 |
| Anbefalt avgjørelse | Fortsett med sikkerhetstiltak |

---

## Hvorfor er denne prediksjonen rimelig?

DrugBank-kildendatafeltets virkningsmekanisme i denne evidenspakken er en bekreftet datahull. Imidlertid etablerer litteraturbeviset som er hentet for denne kandidaten mekanismen uavhengig: sebelipase alfa er en **rekombinant humant lysosomal acid lipase (rhLAL)** enzymerstattingsterapi (Shirley, *Drugs* 2015, PMID 26452566). Det leverer direkte enzymet som er fraværende eller mangelfull i LAL-D — en 1:1 enzym-substratkorrigering, ikke en indirekte lighetsteheuristikk.

Dette er viktig fordi råTxGNN-rangeringen (predicted_indications ranger 1–10) er dominert av andre lysosomale lagringssykdommer som deler fenotypisk innebygd plass, men har **urelated mangelfule enzymer**: Scheie/Hurler-syndrom (α-L-iduronidase), Gaucher-sykdom (glukoserebrosidasee), Tay-Sachs-sykdom (heksosaminidase A). Ingen av disse ville blitt korrigert av rhLAL, og evidenspakkens egen rasjonale merking markerer eksplisitt dem som mekanistisk ustøttet (Hold, L5, ingen kliniske bevis). I kontrast er Wolman-sykdom og CESD rett og slett de to endene av det **samme LAL-D-sykdomsspekteret** som sebelipase alfa opprinnelig ble utviklet for — forsøksprogrammet som er oppført under "cholesteryl ester storage disease" (rang 4) innrullerte faktisk både infantile Wolman-sykdomspasienter og senoppstått CESD-pasienter, noe som forklarer hvorfor Wolman-sykdom-posten (rang 5) viser 0 forsøk i sin egen registrering til tross for å ha en fullført L2/S3 evidensvurdering — en databaseklassifiseringsartefakt snarere enn et datahull.

I praksis er denne "prediksjonen" ikke en nyskapende ombrukshypotese, men en **gjenidentifisering av medikamentets eget etablerte globale indikasjon** i et marked (Norge) der det for tiden ikke har noen autorisasjon. Den kliniske nytten av denne rapporten er derfor mindre om ny farmakologi og mer om å identifisere et markeds-inngangs-/autorisasjonshull.

---

## Klinisk prøvebevis

| Forsøksnummer | Fase | Status | Antall innrullert | Viktige funn |
|---------|------|------|------|---------|
| [NCT01757184](https://clinicaltrials.gov/study/NCT01757184) | Fase 3 | Fullført | 66 | Pivot randomisert placebokontrollert forsøk (ARISE) med sebelipase alfa 1 mg/kg IV hver annen uke ved senoppstått LAL-D (CESD) |
| [NCT02112994](https://clinicaltrials.gov/study/NCT02112994) | Fase 2 | Fullført | 31 | Flersenter åpen sikkerhet/effektivitetsstudie på tvers av bred LAL-D-populasjon |
| [NCT02193867](https://clinicaltrials.gov/study/NCT02193867) | Fase 2 | Avsluttet | 10 | Ukentlige infusjoner opp til 3 år hos spedbarn med raskt progrederende LAL-D (Wolman-sykdom) |
| [NCT01371825](https://clinicaltrials.gov/study/NCT01371825) | Fase 2/3 | Fullført | 9 | Dosestegringsstudie hos barn med vekstsvikt på grunn av LAL-D, ukentlig dosering opp til 5 år |
| [NCT01488097](https://clinicaltrials.gov/study/NCT01488097) | Fase 2 | Fullført | 8 | Fortsettelsesstudie som evaluerer langsiktig sikkerhet/tolerabilitet hos voksne med LAL-D-relatert leversvikt |
| [NCT01307098](https://clinicaltrials.gov/study/NCT01307098) | Fase 1/2 | Fullført | 9 | Første-hos-mennesker dosestegringsstudie hos voksne med LAL-D-relatert leversvikt |
| [NCT02376751](https://clinicaltrials.gov/study/NCT02376751) | N/A | Ikke lenger tilgjengelig | N/A | Protokoll for utvidet tilgang for LAL-D-pasienter i påvente av kommersiell tilgjengelighet |
| [NCT02926872](https://clinicaltrials.gov/study/NCT02926872) | N/A | Avsluttet | 22 | DETECT: screening for LAL-D som underliggende årsak til pediatrisk leverskade |
| [NCT04532047](https://clinicaltrials.gov/study/NCT04532047) | Fase 1 | Rekrutterer | 10 | PEARL basket-forsøk: in-utero enzymerstattingsgjennomførbarhet på tvers av flere LSDs (ikke LAL-D-spesifikk; lav direkte relevans) |

---

## Litteraturbevis

| PMID | År | Type | Tidsskrift | Viktige funn |
|------|-----|------|------|---------|
| [34774639](https://pubmed.ncbi.nlm.nih.gov/34774639/) | 2022 | RCT (forlengelse) | Journal of Hepatology | Endelige resultater fra fase 3 ARISE-studie; sebelipase alfa effektivitet/sikkerhet hos barn og voksne med LAL-D |
| [35442238](https://pubmed.ncbi.nlm.nih.gov/35442238/) | 2022 | Kohort | J Pediatr Gastroenterol Nutr | Langsiktige behandlingsresultater fra enkeltarms åpen studie (NCT02112994) |
| [34906190](https://pubmed.ncbi.nlm.nih.gov/34906190/) | 2021 | Kohort (10-år) | Orphanet J Rare Dis | Nasjonal kohort av ERT ved Wolman-sykdom med opp til 10 års oppfølging |
| [29628368](https://pubmed.ncbi.nlm.nih.gov/29628368/) | 2018 | Kohort | J Clin Lipidol | Sebelipase alfa forbedrer aterogeniske biomerker (fase 3 ARISE-data) |
| [38918870](https://pubmed.ncbi.nlm.nih.gov/38918870/) | 2024 | Kasusserie | Orphanet J Rare Dis | To ganger ukentlig dosering redder alvorlig syke spedbarn med Wolman-sykdom |
| [28179030](https://pubmed.ncbi.nlm.nih.gov/28179030/) | 2017 | Åpen dosestegringsstudie | Orphanet J Rare Dis | Overlevelsesresultater hos spedbarn behandlet med sebelipase alfa |
| [33407676](https://pubmed.ncbi.nlm.nih.gov/33407676/) | 2021 | Langsiktig oppfølging | Orphanet J Rare Dis | Langsiktig overlevelse med sebelipase alfa ved raskt progrederende LAL-D (endelige resultater, 2 åpne studier) |
| [40781810](https://pubmed.ncbi.nlm.nih.gov/40781810/) | 2025 | Register | Liver International | Internasjonale registerdata: sebelipase alfa forbedrer aminotransferasenivåer |
| [39770929](https://pubmed.ncbi.nlm.nih.gov/39770929/) | 2024 | Oversikt | Nutrients | Praktiske anbefalinger for diagnose/behandling av LAL-D, fokus på Wolman-sykdom |
| [26452566](https://pubmed.ncbi.nlm.nih.gov/26452566/) | 2015 | Oversikt | Drugs | Sebelipase alfa: første globale godkjenning |

---

## Norsk markedsinformasjon

Sebelipase alfa har for tiden ingen markedsføringstillatelse i Norge, og ingen lisensregistreringer er tilgjengelige i evidenspakken (`total_licenses: 0`).

---

## Sikkerhetshensyn

Vennligst se pakningsvedlegget for sikkerhetsinformasjon.

> Merknad: Evidensgrunnlaget indikerer uavhengig at infusjonsrelatert hypersensitivitet er et kjent klinisk problem med sebelipase alfa (f.eks. PMID 38572778 beskriver en 14-trinns desensitiseringsprotokoll for en Wolman-sykdomspassient), men ingen strukturerte advarsler, kontraindikasjoner eller DDI-data er tilstede i DrugBank-kilder sikkerhetsfeltene i denne evidenspakken (DG001, blocking severity).

---

## Konklusjon og neste trinn

**Avgjørelse: Fortsett med sikkerhetstiltak**

**Begrunnelse:**
Kjernemedikament-sykdom-parringen (sebelipase alfa → LAL-D/Wolman-sykdom/CESD) er mekanistisk direkte og støttet av en fullført pivot fase 3 RCT (ARISE) pluss flere langsiktige kohort- og registerstudier — dette er faktisk medikamentets eget globalt godkjent indikasjon (Kanuma®, godkjent siden 2015), ikke en spekulativ ombrukshypotese. Imidlertid er medikamentet helt uten markedsføring i Norge, og denne spesifikke evidenspakken mangler sikkerhet/merkingdata, så det passende neste trinnet er en forsiktig regulatorisk inngangs-vei snarere enn et ubetinget "Go."

**For å fortsette, er følgende nødvendig:**
- TFDA/norsk-tilsvarende merkingdata — viktige advarsler, kontraindikasjoner (DG001, blocking; krever PDF-merkingsforspørsel)
- Strukturert DrugBank MOA-post (DG002)
- Formell vurdering av norsk markedsautorisasjon/importlisens, siden medikamentet ikke har noe lokalt regulatorisk fotavtrykk
- Eksplisitt eksklusjon av de andre TxGNN top-10-kandidatene (Scheie-syndrom, Hurler-syndrom, veksthormoninsensitivitetssyndrom, Gaucher-sykdom, lysosomale lagringssykdommer med skjelettbetegnelse, autosomalt ichthyosis-syndrom, Tay-Sachs-sykdom, godartet binyresvulst) fra videre gjennomgang — alle mangler mekanistisk plausibilitet og støttende bevis per rasjonale merknader i denne pakken

## Ansvarsfraskrivelse

Dette innholdet er kun til forskningsformål og utgjør ikke medisinsk rådgivning.
Klinisk validering kreves før enhver klinisk anvendelse.

---

