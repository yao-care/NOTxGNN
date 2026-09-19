---
layout: default
title: Avapritinib
parent: Kun modellprediksjon (L5)
nav_order: 40
evidence_level: L5
indication_count: 10
---

# Avapritinib
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

# Avapritinib: Fra uavklart originalindikasjon til aksiell spondylometafyseal dysplasi

## Oppsummering på én setning

> Avapritinibs original godkjent indikasjon og fullstendig mekanisme-for-virkning-data er for øyeblikket utilgjengelig i denne evidenspakken, selv om det refereres til det andre steder som en selektiv KIT/PDGFRA-hemmer.
> TxGNN-modellen forutsier at det kan være effektivt for **aksiell spondylometafyseal dysplasi**, en sjelden skjeletdysplasi,
> men denne prediksjonen er for øyeblikket støttet av **0 kliniske forsøk** og **0 publikasjoner** — det er et signal fra modellen alene.

---

## Rask oversikt

| Element | Innhold |
|---------|---------|
| Original indikasjon | Ikke tilgjengelig (datagap — ingen godkjent indiksjonstekst på fil) |
| Predikert ny indikasjon | Aksiell spondylometafyseal dysplasi |
| TxGNN prediksjonspoeng | 99.92% |
| Evidensnivå | L5 |
| Status på norskmarkedet | Ikke markedsført |
| Antall godkjenninger | 0 |
| Anbefalt beslutning | Avvent |

---

## Hvorfor er denne prediksjonen rimelig?

For øyeblikket er detaljerte mekanisme-for-virkning-data ikke tilgjengelig i denne evidenspakken. Basert på de mekanistiske notatene som følger modellutsendingen, beskrives avapritinib som en **selektiv KIT/PDGFRA tyrosinkinase-hemmer**. PDGFRA-signalering spiller en rolle i brusk- og benutvikling, som er det teoretiske grunnlaget som tilbys for en forbindelse til dette ultrasjeldne skjeletdysplasi-syndromet.

Imidlertid er modellens egen begrunnelsestekst eksplisitt i at denne forbindelsen er spekulativ: den sier at det er «ingen konkret bevis for overlapping av patogenetisk mekanisme med avapritinibs mål» for denne sykdommen, og at prediksjonen er «rent et høyt-scorende TxGNN-utdata uten klinisk eller litteraturstøtte». Den samme forbehold gjelder på tvers av alle ti rangerte prediksjoner i denne pakken — flere klynger rundt ALS og motorneuronsjukdom (begrunnelsen påkaller en indirekte PDGFRα-rolle i oligodendrocytt-forløperceller og blod-hjerne-barriere-integritet), mens andre (sjeldne skjelet-/nevro-utviklingssyndrom) har **ingen kjent mekanistisk forbindelse i det hele tatt** til KIT/PDGFRA-banen.

Fordi både originalindikasjon og MOA-felt er datagap, og fordi ingen av de ti predikterte indikasjonene har noen korroborerende klinisk forsøks- eller litteraturbevis, skal denne kandidaten behandles som et tidlig-fase hypotesegenererende utdata alene, ikke en gjenbrukskandidat klar for evaluering.

---

## Klinisk forsøksbevis

For øyeblikket ingen registrerte relaterte kliniske forsøk

---

## Litteraturbevis

For øyeblikket ingen tilgjengelig litteratur

---

## Informasjon om norskmarkedet

Avapritinib markedsføres for øyeblikket ikke i Norge (0 godkjenninger på fil); ingen lisensoppføringer er tilgjengelige for denne evidenspakken.

---

## Cytotoksisitet

Basert på den mekanistiske beskrivelsen som er tilgjengelig (selektiv KIT/PDGFRA tyrosinkinase-hemmer), faller avapritinib inn i klassen for målrettet kreftterapibehandling snarere enn konvensjonell cytotoksisk kjemoterapi. Ingen strukturert toksisitetsdata er inkludert i denne evidenspakken.

| Element | Innhold |
|---------|---------|
| Cytotoksisitet klassifisering | Målrettet terapi (KIT/PDGFRA tyrosinkinase-hemmer) |
| Risiko for myelosuppresjon | Vennligst se advarslene og forholdsreglene i pakningsvedlegget |
| Emetogenitet klassifisering | Vennligst se advarslene og forholdsreglene i pakningsvedlegget |
| Overvakingspunkter | Vennligst se advarslene og forholdsreglene i pakningsvedlegget |
| Beskyttelse ved håndtering | Vennligst se advarslene og forholdsreglene i pakningsvedlegget |

---

## Sikkerhetshensyn

Vennligst se pakningsvedlegget for sikkerhetsinformasjon.

---

## Konklusjon og neste steg

**Beslutning: Avvent**

**Begrunnelse:**
Alle ti predikterte indikasjonene har evidensnivå L5 (kun modellprediksjoner) med null korroborerende kliniske forsøk eller litteratur. Kombinert med legemidlets umarkedsførte status i Norge og et blokkerende datagap vedrørende TFDA-etikettadvarsler/kontraindikasjoner, er det intet grunnlag for å fremme noen av disse kandidatene utover hypotesestadium.

**For å fortsette er følgende nødvendig:**
- Bekreftet original indikasjon(er) og godkjent merkningstekst
- Detaljert mekanisme-for-virkning (MOA) data, ideelt hentet fra DrugBank
- TFDA-tilsvarende merknadsadvarsler og kontraindikasjoner (for øyeblikket et blokkerende gap, DG001)
- Minst preklinisk eller kasuistisk bevis som knytter avapritinib til noen av de rangerte predikterte indikasjonene før S1-sikkerhetskontroll kan begynne

## Ansvarsfraskrivelse

Dette innholdet er kun til forskningsformål og utgjør ikke medisinsk rådgivning.
Klinisk validering kreves før enhver klinisk anvendelse.

---

