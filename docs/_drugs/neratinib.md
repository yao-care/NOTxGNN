---
layout: default
title: Neratinib
parent: Høy evidens (L1-L2)
nav_order: 240
evidence_level: L2
indication_count: 4
---

# Neratinib
{: .fs-9 }

Evidensnivå: **L2** | Predikerte indikasjoner: **4** stk.
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

# Neratinib: Fra HER2-positiv brystkreft til progesteronreseptor-positiv brystkreft

## En-linjers sammenfatning

> Neratinib er en irreversibel pan-HER (EGFR/HER1, HER2, HER4) tyrosinkinasehemmer hvis etablerte bruk — ifølge den pivotale ExteNET Phase 3-studien og andre studier inneholdt i denne evidenspakken — er HER2-positiv brystkreft; merk at «original indication»-feltet til stoffet selv er flagget som et datakløft i dette registeret og krever manuell verifisering.
> TxGNN-modellen forutsier at det også kan være effektivt for **progesteronreseptor (PR)-positiv brystkreft**,
> med **5 kliniske studier** og **10 publikasjoner** som for tiden støtter denne retningen, selv om evidensgrunnlaget fortsatt er på et tidlig stadium (L2).

---

## Rask oversikt

| Element | Innhold |
|---------|---------|
| Original indikasjon | Ikke tilgjengelig i dette registeret (`original_indications` tom, `market_status` = Ikke markedsført/Not Marketed) — et flagget datakløft; litteratur i denne pakken indikerer at stoffets etablerte bruk er HER2-positiv brystkreft |
| Forutsagt ny indikasjon | Progesteronreseptor-positiv brystkreft |
| TxGNN-prediksjonspoeng | 99.68% |
| Evidensnivå | L2 |
| Norges markedsstatus | ✗ Ikke markedsført |
| Antall godkjenninger | 0 |
| Anbefalt beslutning | Fortsett med sikringssystemer |

---

## Hvorfor er denne prediksjonen rimelig?

Neratinib er en irreversibel pan-HER tyrosinkinasehemmer som blokkerer signalering gjennom EGFR/HER1, HER2 og HER4. Klinisk er det best etablert i HER2-positiv brystkreft, hvor det har vist fordeler både som utvidet adjuvant terapi etter trastuzumab (ExteNET, PMID 26874901) og i kombinasjonsregimer for metastatisk sykdom. PR-status i seg selv er ikke neratinib sitt direkte molekylære mål, men PR-positiv sykdom forekommer hyppig sammen med HER2-positivitet («triple-positive», HR+/HER2+ subgruppen), og det finnes en klar farmakologisk rasjonale for å kombinere neratinib med endokrin terapi (f.eks. fulvestrant, aromatashemmere) i denne populasjonen — HER2-veiaktivering er en anerkjent mekanisme for endokrin resistens, og å blokkere den med neratinib er ment å gjenopprette endokrin følsomhet.

Flere studier i denne evidenspakken tester direkte denne kombinasjonsstrategi i HR+/HER2+-sykdom (f.eks. NCT04886531: neodjuvant neratinib + aromatashemmer + trastuzumab i ER+/HER2+-kreft), som støtter den biologiske plausibiliteten til TxGNN-prediksjonen.

**Viktig forbehold flagget i de underliggende dataene:** denne evidenspakken registrerer `original_indications` som tom og Norges `market_status` som «Ikke markedsført» med 0 godkjenninger, som er inkonsistent med neratinib sitt kjente regulatoriske historie (f.eks. FDA-godkjent som Nerlynx for HER2+ brystkreft). Denne uoverensstemmelsen er eksplisitt notert av analyserørledningen selv og bør verifiseres manuelt mot kildedatabasen før denne kandidaten går videre.

---

## Klinisk prøvebevis

| Studienummer | Fase | Status | Rekruttering | Viktige funn |
|---------|------|------|------|---------|
| [NCT04901299](https://clinicaltrials.gov/study/NCT04901299) | Fase 2 | Trukket tilbake | 0 | Planlagt å evaluere neratinib + fulvestrant i tidligere behandlet HR+/HER2-negativ metastatisk brystkreft; trukket tilbake før rekruttering, ingen data generert |
| [NCT04886531](https://clinicaltrials.gov/study/NCT04886531) | Fase 2 | Rekrutterer | 30 | Preoperativ neratinib + aromatashemmer + trastuzumab i ER-positiv, HER2-positiv brystkreft; resultater utstår |
| [NCT06131424](https://clinicaltrials.gov/study/NCT06131424) | N/A (retrospektiv) | Fullført | 1,151 | Multisenterstudium retrospektiv studie av HER2-lavprevalens, karakteristikker og behandlingsmønstre i HER2-negativ metastatisk brystkreft; ikke en intervensjonell effektivitetsstudie |
| [NCT04460430](https://clinicaltrials.gov/study/NCT04460430) | Fase 2 | Avbrutt | 12 | Neratinib som målrettet mot EGFR/ERBB2 i HR-positiv/HER2-negativ, HER2-anriket avansert/metastatisk brystkreft; avbrutt tidlig med begrenset rekruttering |
| [NCT05599334](https://clinicaltrials.gov/study/NCT05599334) | N/A (retrospektiv) | Fullført | 111 | Retrospektiv observasjonsstudie av neratinib som utvidet adjuvant terapi i tidlig HER2-positiv brystkreft under det europeiske Early Access Program; bare beskrivende data |

---

## Litteraturbevis

| PMID | År | Type | Tidsskrift | Viktige funn |
|------|-----|------|------|---------|
| [26874901](https://pubmed.ncbi.nlm.nih.gov/26874901/) | 2016 | RCT | Lancet Oncology | ExteNET: Phase 3 RCT som viser at 12 måneder med neratinib etter trastuzumab-basert adjuvant terapi forbedrer resultater i tidlig HER2-positiv brystkreft |
| [27406346](https://pubmed.ncbi.nlm.nih.gov/27406346/) | 2016 | RCT | New England Journal of Medicine | I-SPY 2 adaptiv Phase 2-studie som evaluerer neratinib blant andre nye midler lagt til neodjuvant kjemoterapi i høyrisiko brystkreft |
| [35640077](https://pubmed.ncbi.nlm.nih.gov/35640077/) | 2022 | Oversikt | J Clin Oncol | ASCO-retningslinjeoppdatering om systemisk terapi for avansert HER2-positiv brystkreft |
| [29784737](https://pubmed.ncbi.nlm.nih.gov/29784737/) | 2018 | Oversikt | JNCCN | NCCN-retningslinjeoppdatering om brystkreft, som dekker endokrin og HER2-rettet behandlingsalgoritmer |
| [32139271](https://pubmed.ncbi.nlm.nih.gov/32139271/) | 2020 | Oversikt | Clinical Breast Cancer | Ekspertrundetabell om HER2-positiv brystkreft-behandlingsutviklinger, inkludert neratinib og lapatinib |
| [33726508](https://pubmed.ncbi.nlm.nih.gov/33726508/) | 2021 | Oversikt | Future Oncology | Aktuelle behandlingstrender i HR-positiv/HER2-positiv brystkreft, som diskuterer neratinib-baserte kombinasjoner |
| [24892840](https://pubmed.ncbi.nlm.nih.gov/24892840/) | 2013 | Oversikt | Clin Adv Hematol Oncol | Oversikt som integrerer de siste metastatiske brystkreft-data etter reseptor-undertype |
| [39153126](https://pubmed.ncbi.nlm.nih.gov/39153126/) | 2024 | Kohort | Breast Cancer Res Treat | Virkelige verden mønstre av adjuvant neratinib-bruk og tolerabilitet i HR+/HER2+ tidlig-stadium brystkreft; merker betydelig GI-toksisitet som driver avbrudd |
| [32782013](https://pubmed.ncbi.nlm.nih.gov/32782013/) | 2020 | Kohort | Breast Cancer Research | In silico-analyse av ERBB2-mutasjonsstatus som en prognostisk/targetbar markør i ER-positiv, ERBB2 ikke-forsterket lobulær brystkreft |
| [35251981](https://pubmed.ncbi.nlm.nih.gov/35251981/) | 2022 | Caseserier | Frontiers in Oncology | Casusrapport/litteraturreview om varig respons med pyrotinib + vinorelbine i HER2-positiv brystkreft med leptomeningeal sykdom (indirekte relevans) |

---

## Markedsinformasjon for Norge

Neratinib er for øyeblikket ikke markedsført i Norge — evidenspakken viser 0 produktgodkjenninger, så ingen lisenstabel kan produseres.

---

## Celleskade

Neratinib er et antineoplastisk middel (målrettet småmolekyl-kinasehemmer brukt i brystkreft), så denne delen gjelder.

| Element | Innhold |
|---------|---------|
| Klassifisering av celleskade | Målrettet terapi — irreversibel pan-HER (EGFR/HER2/HER4) tyrosinkinasehemmer; ikke en konvensjonell cytotoksisk kjemoterapi |
| Risiko for benmargssuppresjon | Ikke direkte rapportert i denne evidenspakken; litteratur fra virkelig verden (PMID 39153126) indikerer at den dominante behandlingsbegrensende toksisiteten er gastrointestinal (diarré) snarere enn benmargssuppresjon — formale hematologiske toksisitetsdata bør bekreftes via pakningsvedlegget |
| Klassifisering av emetogenitet | Vennligst se pakningsvedlegget for advarsler og forsiktighetsregler |
| Overvåkingspunkter | Leverenzymer; nær overvåking og proaktiv behandling av diarré/GI-toksisitet (ifølge litteratur); CBC som standard onkologiovervåking |
| Håndteringsbeskyttelse | Vennligst se pakningsvedlegget for advarsler og forsiktighetsregler; oral formulering — institusjonelle cytotoksiske/farlige midler-håndteringsprotokoller bør bekreftes lokalt |

---

## Sikkerhetshensyn

Vennligst se pakningsvedlegget for sikkerhetsinformasjon.

---

## Konklusjon og neste skritt

**Beslutning: Fortsett med sikringssystemer**

**Rasjonale:**
PR-positiv brystkreft-prediksjonen er biologisk plausibel gitt neratinib sin etablerte mekanisme i HER2-drevet, hormonreseptor-positiv sykdom, og er støttet av pågående/fullførte Phase 1–2-studier pluss et sterkt presedens fra Phase 3 ExteNET-studien i den bredere HER2-positive populasjonen (L2 evidens). Imidlertid hindrer to blokkerings-nivå datakløfter en fullstendig go-beslutning på dette tidspunktet.

**For å fortsette, er følgende nødvendig:**
- Løs TFDA/lokal produktetikett sikkerhetsdatakløft (advarsler, kontraindikasjoner) — for øyeblikket blokkerer noen S1-sikkerhetsvaluering
- Bekreft mekanisme for handling (MOA) direkte via DrugBank snarere enn å stole bare på studie-utledet rasjonale
- Manuelt verifiser uoverensstemmelsen mellom denne datasettets «ikke markedsført / ingen original indikasjon» status og neratinib sin kjente regulatoriske historie (f.eks. FDA-godkjenning som Nerlynx) før du er avhengig av denne evidenspakken for nedstrøms beslutninger
- Innhent resultater fra den pågående PR+/HR+-spesifikke studien (NCT04886531) når den er tilgjengelig, siden gjeldende PR+-spesifikke studiobevis ikke har noen fullførte resultater

## Ansvarsfraskrivelse

Dette innholdet er kun til forskningsformål og utgjør ikke medisinsk rådgivning.
Klinisk validering kreves før enhver klinisk anvendelse.

---

