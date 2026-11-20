---
layout: default
title: Fulvestrant
parent: Moderat evidens (L3-L4)
nav_order: 183
evidence_level: L4
indication_count: 10
last_modified_at: 2026-10-28
description: "Fulvestrant: predikert ny indikasjon HIV-infeksjon (evidensnivå L4). Opprinnelig indikasjon: Brystkreft (Breast Neoplasms)"
monitor_inn: "FULVESTRANT"
predicted_indications: ["HIV infectious disease", "multiple endocrine neoplasia", "simian immunodeficiency virus infection", "feline acquired immunodeficiency syndrome", "neurodevelopmental disorder with ataxic gait, absent speech, and decreased cortical white matter", "rheumatoid arthritis", "acne (disease)", "brachydactyly-syndactyly syndrome", "hemoglobinopathy", "colobomatous microphthalmia-rhizomelic dysplasia syndrome"]
---

# Fulvestrant
{: .fs-9 }

Evidensnivå: **L4** | Predikerte indikasjoner: **10** stk.
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

## Fulvestrant: Fra brystkreft til HIV-infeksjon
{: .text-alpha }

## Oppsummering

Fulvestrant er en østrogenreseptor-antagonist og -nedbryter som opprinnelig brukes til behandling av brystkreft.
TxGNN-modellen predikerer at legemidlet kan ha effekt mot **HIV-infeksjon**,
men så langt finnes **ingen kliniske studier** og bare **2 publikasjoner** (hvorav én er en preklinisk mekanistisk studie) som støtter denne retningen.

---

## Hurtigoversikt

| Punkt | Innhold |
|------|------|
| Opprinnelig indikasjon | Brystkreft (Breast Neoplasms) |
| Predikert ny indikasjon | HIV-infeksjon |
| TxGNN-prediksjonsscore | 0,9991 |
| Evidensnivå | L4 |
| Markedsstatus i Norge | Markedsført (gyldige tillatelser: 2 av 2) |
| Antall godkjenninger | 2 (gyldige: 2) |
| Anbefalt beslutning | Hold |

---

## Hvorfor er denne prediksjonen rimelig?

Ifølge avsnittet «Mechanism of Action» i preparatomtalen som er godkjent av amerikanske FDA (Prescribing Information), for Fulvestrant (uoffisiell oversettelse): «Mange brystkreftsvulster har østrogenreseptorer (ER), og veksten av disse svulstene kan stimuleres av østrogen. Fulvestrant er en østrogenreseptorantagonist som bindes til østrogenreseptoren på en kompetitiv måte med en affinitet som er sammenlignbar med østradiols, og nedregulerer ER-proteinet i humane brystkreftceller.» Engelsk originaltekst: "Many breast cancers have estrogen receptors (ER) and the growth of these tumors can be stimulated by estrogen. Fulvestrant is an estrogen receptor antagonist that binds to the estrogen receptor in a competitive manner with affinity comparable to that of estradiol and downregulates the ER protein in human breast cancer cells." ([DailyMed: Cligavyx (fulvestrant) prescribing information, AVYXA Pharma, LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=e20d8ca3-8837-4003-8b01-1ebec342062a), versjon av 2026-10-16; hentet 2026-11-19). Fulvestrant er kjent som en selektiv østrogenreseptor-antagonist og -nedbryter (ERα), og effekten ved hormonreseptorpositiv brystkreft er godt dokumentert.

Østrogenreseptor α finnes i CD4+ T-celler, og en studie fra 2026 (PMID 42430506) undersøkte hvordan ERα-ligander og midler som reverserer HIV-latens påvirker denne reseptoren. Fulvestrant kan derfor i teorien påvirke HIV-latens og immunsignalering via ERα.

Koblingen er imidlertid preklinisk og indirekte. Artikkelen om HTLV-1 (PMID 40343334) gjelder et beslektet retrovirus og tester ikke fulvestrant direkte. Prediksjonen bør derfor betraktes som en hypotese, ikke som en etablert terapeutisk mulighet.

---

## Evidens fra kliniske studier

Det er for tiden ingen kliniske studier registrert for HIV-infeksjon.

---

## Litteraturevidens

| PMID | År | Type | Tidsskrift | Hovedfunn |
|------|-----|------|------|---------|
| [42430506](https://pubmed.ncbi.nlm.nih.gov/42430506/) | 2026 | Preklinisk mekanistisk studie | JCI Insight | Undersøker effekten av østrogen, fulvestrant og HIV-latensreverserende midler på ERα i CD4+ T-celler |
| [40343334](https://pubmed.ncbi.nlm.nih.gov/40343334/) | 2025 | Beregningsmessig tverr-omikanalyse | Research Square | Analyse av sykdomsmekanismer ved HTLV-1-assosiert myelopati; gjelder et beslektet retrovirus og tester ikke fulvestrant direkte |

---

## Markedsinformasjon for Norge

| Godkjenningsnummer | Produktnavn | Doseringsform | Godkjent indikasjon |
|---------|------|------|-----------|
| EMEA/H/C/000540 | Faslodex (AstraZeneca AB) | Ikke oppgitt | Brystkreft (kansellert) |
| EMEA/H/C/004649 | Fulvestrant Mylan (Mylan Pharmaceuticals Limited) | Ikke oppgitt | Brystkreft (kansellert) |

---

## Cytotoksisitet

Fulvestrant er et legemiddel mot kreft, men er en hormonell behandling (østrogenreseptor-nedbryter) og ikke et konvensjonelt cytotoksisk middel.

| Punkt | Innhold |
|------|------|
| Klassifisering | Hormonell/målrettet behandling (ikke konvensjonelt cytotoksisk) |
| Risiko for myelosuppresjon | Se pakningsvedlegg for advarsler og forsiktighetsregler |
| Emetogenisitet | Se pakningsvedlegg for advarsler og forsiktighetsregler |
| Overvåkingspunkter | Se pakningsvedlegg for advarsler og forsiktighetsregler |
| Håndtering og vern | Se pakningsvedlegg for advarsler og forsiktighetsregler |

---

## Sikkerhetsvurderinger

- **Kontraindikasjoner fra kunnskapsgraf (ikke preparatomtale):** TxGNN-kunnskapsgrafen (PrimeKG) peker på mulige kontraindikasjoner ved leversykdom, gallblæresykdom, trombocytopeni og blodkoagulasjonssykdom. Dette er grafbaserte koblinger og ikke godkjent preparattekst.
- **Legemiddelinteraksjoner:** Totalt 92 mulige interaksjoner er registrert i DDInter, alle med uklassifisert alvorlighetsgrad. Eksempler: pantoprazol, morfin, metformin, omeprazol, prednison, simvastatin, acetylsalisylsyre, deksametason og warfarin. Spesielt interaksjon med warfarin bør vurderes nøye, gitt de grafbaserte signalene om koagulasjonsforstyrrelser.

Offisielle advarsler og kontraindikasjoner fra preparatomtalen mangler i de sammenstilte dataene. Se pakningsvedlegget for fullstendig sikkerhetsinformasjon.

---

## Konklusjon og neste steg

**Beslutning: Hold**

**Begrunnelse:**
Evidensen for HIV-infeksjon er begrenset til én preklinisk mekanistisk studie og én indirekte retrovirusanalyse, uten kliniske studier. Fulvestrant er dessuten markedsført i Norge med 2 gyldige markedsføringstillatelser av 2, og preparatomtalens sikkerhetsdata mangler, noe som hindrer videre sikkerhetsscreening.

**For å gå videre kreves følgende:**
- Hente og analysere preparatomtalen (advarsler og kontraindikasjoner), som er en blokkerende datamangel
- Hente data om virkningsmekanisme fra DrugBank
- Utvide prekliniske studier (in vitro og dyremodeller) av fulvestrants effekt på HIV-latens i CD4+ T-celler
- Avklare regulatorisk status og tilgjengelighet i Norge, siden begge godkjenninger er kansellert
- Vurdere sikkerhet ved langtidsbruk i en ikke-onkologisk populasjon med tanke på hormonell nedregulering

---

**Merknad om andre prediksjoner:** Ingen av de øvrige ni predikerte indikasjonene har kliniske studier eller solid litteratur som støtter dem. For «multiple endokrine neoplasier» gjelder de 13 treffende studiene brystkreft (opprinnelig indikasjon) og skyldes sannsynligvis en term-/ontologikobling, ikke reell evidens. Revmatoid artritt (evidensnivå L4) har kun indirekte og retningsmessig tvetydig evidens, der en dyremodell tyder på at østrogenhemming kan forverre betennelse, og kan eventuelt være et forskningsspørsmål.

<!-- review:begin log -->

## Kontrollogg

Nedenfor er gjennomgangsloggen for denne siden. Setningen om at data om virkningsmekanismen ikke var tilgjengelige, er erstattet med et utdrag fra den oppgitte offisielle preparatomtalen (med uoffisiell oversettelse); modellprediksjoner, evidensnivåer og konklusjoner er ikke omskrevet.

| Kontrolldato | Punkt | Tiltak | Kilde |
|------|------|------|------|
| 2026-11-19 | Setningen «data om virkningsmekanismen er ikke tilgjengelige» erstattet med utdrag fra amerikansk preparatomtale | Setning om manglende data om virkningsmekanismen erstattet med et utdrag med kilde | [DailyMed: Cligavyx (fulvestrant) prescribing information, AVYXA Pharma, LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=e20d8ca3-8837-4003-8b01-1ebec342062a) |

<!-- review:end log -->

## Ansvarsfraskrivelse

Dette innholdet er kun til forskningsformål og utgjør ikke medisinsk rådgivning.
Klinisk validering kreves før enhver klinisk anvendelse.

---

