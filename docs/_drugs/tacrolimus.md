---
layout: default
title: Tacrolimus
parent: Høy evidens (L1-L2)
nav_order: 395
evidence_level: L1
indication_count: 2
last_modified_at: 2026-11-24
monitor_inn: "TACROLIMUS"
predicted_indications: ["seborrheic dermatitis", "parapsoriasis"]
description: "Tacrolimus: predikert ny indikasjon Seboreisk dermatitt (seborrheic dermatitis) (evidensnivå L1). Opprinnelig indikasjon: Graft Rejection"
---

# Tacrolimus
{: .fs-9 }

Evidensnivå: **L1** | Predikerte indikasjoner: **2** stk.
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

## Tacrolimus: Seboreisk dermatitt (seborrheic dermatitis)
{: .text-alpha }

## Oppsummering i én setning

Tacrolimus er en kalsineurinhemmer som opprinnelig brukes til å forebygge avstøtning etter organtransplantasjon (lever og nyre) og til å behandle atopisk dermatitt.
TxGNN-modellen predikerer at legemidlet kan være effektivt ved **seboreisk dermatitt**,
og dette støttes foreløpig av **2 kliniske studier** (inkludert én fullført fase 3-studie) og **flere publikasjoner** om topisk bruk.

---

## Hurtigoversikt

| Punkt | Innhold |
|------|------|
| Opprinnelig indikasjon | Graft Rejection; Dermatitis, Atopic; Liver Transplantation;Kidney Transplantation |
| Predikert ny indikasjon | Seboreisk dermatitt (seborrheic dermatitis) |
| TxGNN-prediksjonsscore | 0.9926 |
| Evidensnivå | L1 (jf. merknad under) |
| Markedsstatus i Norge | Markedsført (gyldige tillatelser: 5 av 5) |
| Antall godkjenninger | 5 (gyldige: 5) |
| Anbefalt beslutning | Proceed with Guardrails (fortsett med forhåndsregler) |

*Merknad om evidensnivå:* Datagrunnlaget angir L1. Strengt tatt er det bare én fullført fase 3-studie (NCT02004860) pluss en fase 4-studie for seboreisk dermatitt, så nivået bør tolkes med forsiktighet.

---

## Hvorfor er denne prediksjonen rimelig?

Ifølge avsnittet «Mechanism of Action» i preparatomtalen som er godkjent av amerikanske FDA (Prescribing Information), for Tacrolimus (uoffisiell oversettelse): «Takrolimus bindes til et intracellulært protein, FKBP-12. Et kompleks av takrolimus-FKBP-12, kalsium, kalmodulin og kalsineurin (et allestedsnærværende intracellulært enzym hos pattedyr) dannes deretter, og fosfataseaktiviteten til kalsineurin hemmes.» Engelsk originaltekst: "Tacrolimus binds to an intracellular protein, FKBP-12. A complex of tacrolimus-FKBP-12, calcium, calmodulin, and calcineurin (an ubiquitous mammalian intracellular enzyme) is then formed and the phosphatase activity of calcineurin inhibited." ([DailyMed: Envarsus Xr (tacrolimus) prescribing information, Veloxis Pharmaceuticals, Inc](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=de2315b0-6344-43ac-9aea-3e3b68d828e7), versjon av 2025-02-26; hentet 2026-11-19). Basert på kjent informasjon hemmer tacrolimus kalsineurin, noe som blokkerer NFAT-avhengig T-celleaktivering og produksjonen av IL-2 og andre proinflammatoriske cytokiner.

Seboreisk dermatitt er en kronisk, relapserende betennelsestilstand i huden, med en T-cellemediert og cytokindrevet komponent som delvis utløses av gjær av slekten *Malassezia*. Atopisk dermatitt, som tacrolimus allerede er godkjent for, har en tilsvarende betennelsesmekanisme. Koblingen er derfor mekanistisk plausibel.

Topisk bruk gir i tillegg antiinflammatorisk effekt uten hudatrofien som forbindes med langvarig bruk av kortikosteroider, noe som er relevant ved vedlikeholdsbehandling i ansiktet.

---

## Klinisk studieevidens

| Studienummer | Fase | Status | Antall deltakere | Hovedfunn |
|---------|------|------|------|---------|
| [NCT02004860](https://clinicaltrials.gov/study/NCT02004860) | Fase 3 | Fullført | 120 | Vedlikeholdsbehandling med tacrolimussalve (Protopic) ved alvorlig seboreisk dermatitt i ansiktet hos voksne, for å redusere residiv. Resultater er ikke oppgitt i datagrunnlaget. |
| [NCT01591070](https://clinicaltrials.gov/study/NCT01591070) | Fase 4 | Fullført | 104 | Proaktiv bruk av 0,1 % tacrolimussalve én til to ganger i uken for å holde seboreisk dermatitt i ansiktet i remisjon. Resultater er ikke oppgitt. |

---

## Litteraturevidens

| PMID | År | Type | Tidsskrift | Hovedfunn |
|------|-----|------|------|---------|
| [26512166](https://pubmed.ncbi.nlm.nih.gov/26512166/) | 2015 | Klinisk studie | Annals of Dermatology | Vedlikeholdsbehandling av seboreisk dermatitt i ansiktet med 0,1 % tacrolimussalve |
| [27804089](https://pubmed.ncbi.nlm.nih.gov/27804089/) | 2017 | Systematisk oversikt | Am J Clin Dermatol | Topisk behandling av seboreisk dermatitt i ansiktet |
| [19222250](https://pubmed.ncbi.nlm.nih.gov/19222250/) | 2009 | Oversikt | Am J Clin Dermatol | Topiske kalsineurinhemmere er et trygt alternativ ved seboreisk dermatitt, og blokkerer den inflammatoriske kaskaden |
| [24171300](https://pubmed.ncbi.nlm.nih.gov/24171300/) | 2013 | Klinisk studie | Annals of Parasitology | Sammenligning av sertakonazol 2 % og tacrolimus 0,03 % krem hos 60 pasienter med seboreisk dermatitt |
| [19213227](https://pubmed.ncbi.nlm.nih.gov/19213227/) | 2009 | Oversikt | J Drugs Dermatol | Status og terapeutiske muligheter ved seboreisk dermatitt i ansiktet |
| [31476936](https://pubmed.ncbi.nlm.nih.gov/31476936/) | 2019 | Oversikt | J Cutan Med Surg | Off-label bruk av topiske kalsineurinhemmere ved ulike hudsykdommer |
| [39219446](https://pubmed.ncbi.nlm.nih.gov/39219446/) | 2024 | Systematisk oversikt/nettverksmetaanalyse | Clin Exp Allergy | Topiske antiinflammatoriske midler ved eksem (indirekte relevans) |
| [15461548](https://pubmed.ncbi.nlm.nih.gov/15461548/) | 2004 | Oversikt | Expert Opin Pharmacother | Tacrolimussalve ved atopisk dermatitt og andre inflammatoriske hudsykdommer |
| [17685874](https://pubmed.ncbi.nlm.nih.gov/17685874/) | 2007 | Oversikt | Expert Opin Investig Drugs | Nye bruksområder for topisk tacrolimus |
| [11770914](https://pubmed.ncbi.nlm.nih.gov/11770914/) | 2001 | Oversikt | Semin Cutan Med Surg | Topiske immunmodulatorer ved blant annet psoriasis og seboreisk dermatitt |

---

## Markedsinformasjon for Norge

<!-- licenses:begin -->

| Godkjenningsnummer | Preparatnavn (EMA) | Virkestoff(er) (EMA, engelsk) | Terapeutisk område (EMA, engelsk) | Status |
|------|------|------|------|------|
| EMEA/H/C/000374 | Protopic | tacrolimus | Dermatitis, Atopic | Gyldig |
| EMEA/H/C/000712 | Advagraf | tacrolimus | Graft Rejection | Gyldig |
| EMEA/H/C/000954 | Modigraf | tacrolimus | Graft Rejection | Gyldig |
| EMEA/H/C/002655 | Envarsus | tacrolimus | Graft Rejection | Gyldig |
| EMEA/H/C/004435 | Tacforius | tacrolimus monohydrate | Liver Transplantation; Kidney Transplantation | Gyldig |

Kilde: EMA – Medicines output (sentralt godkjente legemidler til mennesker); preparatnavn, virkestoffer og terapeutisk område er gjengitt i engelsk original. Nasjonale markedsføringstillatelser (DMP) og veterinærpreparater er ikke med i disse dataene.

<!-- licenses:end -->

---

## Sikkerhetsmomenter

- **Kontraindikasjoner fra kunnskapsgrafen (ikke preparatomtale):** Kunnskapsgrafen (PrimeKG) knytter tacrolimus til en rekke tilstander, blant annet hypertensjon, langt QT-syndrom og torsades de pointes, leversvikt, nyresykdom, epilepsi, hyperglykemi og diabetes, ketoacidose, alvorlige infeksjoner (herpes simplex, herpes zoster, progressiv multifokal leukoencefalopati, kronisk EBV-infeksjon), kreft og lymfom (inkludert primært CNS-lymfom), posterior leukoencefalopatisyndrom samt aplastisk anemi. Disse bør vurderes som signaler, ikke som bekreftede kontraindikasjoner.
- **Legemiddelinteraksjoner:** Totalt 100 interaksjoner er registrert. Alvorlige (Major) interaksjoner omfatter blant annet amfotericin B (også lipidkompleks), loperamid, mesalazin, omeprazol og balsalazid. Moderate interaksjoner omfatter blant annet famotidin, rabeprazol, hydrokortison, deksametason, betametason, triamcinolon, budesonid, metformin, pioglitazon, aprepitant og metronidazol.
- **Topisk bruk, relevante forhåndsregler:** Det må tas hensyn til advarselen om langtidssikkerhet (malignitet og infeksjonsrisiko), begrenset bruk hos små barn og avgrensing til områder med aktiv sykdom. En metaanalyse om kreftrisiko ved topiske kalsineurinhemmere (PMID 36370744) er relevant for videre vurdering.

Advarsler og kontraindikasjoner fra preparatomtalen er ikke innhentet; se preparatomtalen for fullstendig sikkerhetsinformasjon.

---

## Konklusjon og neste steg

**Beslutning: Proceed with Guardrails (fortsett med forhåndsregler)**

**Begrunnelse:**
Det finnes en fullført fase 3-studie og en fase 4-studie direkte på seboreisk dermatitt, og mekanismen er den samme som ved den etablerte indikasjonen atopisk dermatitt. Evidensen for seboreisk dermatitt er imidlertid begrenset til to studier med moderat størrelse.

<!-- review:begin no-lic-20261124b-tacrolimus-1 -->

> **Kontrollrettelse (2026-11-24)**: Opprinnelig sto det: «Evidensen for seboreisk dermatitt er imidlertid begrenset til to studier med moderat størrelse, og alle norske godkjenninger er kansellert.» Rettet: opplysningen om at godkjenningen(e) er kansellert, er tatt ut fordi den ikke stemte med EMAs data om sentrale EU-godkjenninger (2026-11-12), der godkjenningene står som gyldige (Authorised); resten av setningen er uendret. Oppdaterte antall og statuser for godkjenningene står i hurtigoversikten og i lisenstabellen under markedsinformasjonen. Kilde: [EMA – Medicines output: medicines report](https://www.ema.europa.eu/en/documents/report/medicines-output-medicines-report_en.xlsx); [European Medicines Agency](https://www.ema.europa.eu/).

<!-- review:end no-lic-20261124b-tacrolimus-1 -->

**For å gå videre kreves følgende:**
- Hente og analysere resultatene fra NCT02004860 og NCT01591070 (effekt og residivrate)
- Innhente advarsler og kontraindikasjoner fra preparatomtalen (kritisk datahull som blokkerer sikkerhetsscreening)
- Innhente detaljerte data om virkningsmekanisme
- Lage en plan for sikkerhetsoppfølging ved langtidsbruk (malignitet, infeksjon, begrensning hos barn)

---

*Merknad om øvrige prediksjoner:* Parapsoriasis (score 0,9924, kun kasuistikker, evidensnivå L4) er et forskningsspørsmål og ikke modent for beslutning. Generell «dermatitt» er ikke en prediksjon på denne siden, siden den domineres av den allerede godkjente indikasjonen atopisk dermatitt og derfor ikke er en reell ny indikasjon.

<!-- review:begin log -->

## Kontrollogg

Nedenfor er kontrolloggen for denne siden: opplysninger kontrollert mot EMAs data om sentrale EU-godkjenninger. Rettelser gjelder bare grunnleggende faktaopplysninger; modellens prediksjoner, evidensnivåer og konklusjoner er ikke skrevet om. Setningen om at data om virkningsmekanismen ikke var tilgjengelige, er erstattet med et utdrag fra den oppgitte offisielle preparatomtalen (med uoffisiell oversettelse).

| Kontrolldato | Punkt | Tiltak | Kilde |
|------|------|------|------|
| 2026-11-19 | Setningen «data om virkningsmekanismen er ikke tilgjengelige» erstattet med utdrag fra amerikansk preparatomtale | Setning om manglende data om virkningsmekanismen erstattet med et utdrag med kilde | [DailyMed: Envarsus Xr (tacrolimus) prescribing information, Veloxis Pharmaceuticals, Inc](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=de2315b0-6344-43ac-9aea-3e3b68d828e7) |
| 2026-11-24 | Rettet: «Evidensen for seboreisk dermatitt er imidlertid begrenset til to studier med moderat størrelse, og alle norske godkjenninger er kansellert.» → «Evidensen for seboreisk dermatitt er imidlertid begrenset til to studier med moderat størrelse.» | Rettet | [EMA – Medicines output: medicines report](https://www.ema.europa.eu/en/documents/report/medicines-output-medicines-report_en.xlsx); [European Medicines Agency](https://www.ema.europa.eu/) |

<!-- review:end log -->

## Ansvarsfraskrivelse

Dette innholdet er kun til forskningsformål og utgjør ikke medisinsk rådgivning.
Klinisk validering kreves før enhver klinisk anvendelse.

---

