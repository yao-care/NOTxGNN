---
layout: default
title: Abiraterone Acetate
parent: Kun modellprediksjon (L5)
nav_order: 15
evidence_level: L5
indication_count: 0
---

# Abiraterone Acetate
{: .fs-9 }

Evidensnivå: **L5** | Predikerte indikasjoner: **0** stk.
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

# Abiraterone acetat: Evaluering avventer — ingen forutsagt indikasjon tilgjengelig

## Sammendrag i én setning

Abiraterone acetat er en CYP17A1-hemmer opprinnelig utviklet for behandling av metastatisk kastrationresistent prostatakrefft (mCRPC). TxGNN-modellen har **ikke ennå generert en forutsagt ny indikasjon** for dette legemidlet. Den nåværende bevissamlingen inneholder betydelige datahull som må løses før evaluering kan fortsette.

## Hurtigoversikt

| Element | Innhold |
|---------|---------|
| Original indikasjon | Metastatisk kastrationresistent prostatakrefft (mCRPC)¹ |
| Forutsagt ny indikasjon | — (Ingen prediksjon tilgjengelig) |
| TxGNN-prediksjonsresultat | — |
| Bevisnivå | L5 (Ingen prediksjon eller støttende studier) |
| Status på Taiwans marked | ✗ Ikke markedsført |
| Antall godkjenninger | 0 |
| Anbefalt beslutning | **Avvent** |

> ¹ Basert på globalt etablert bruk; ingen TFDA-lisensdata tilgjengelig i denne bevissamlingen.

## Hvorfor er denne prediksjonen rimelig?

For tiden har ingen ny indikasjon blitt forutsagt av TxGNN for abiraterone acetat, så mekanistisk plausibilitet kan ikke vurderes på dette tidspunktet.

For kontekst er abiraterone acetat et prodrug av abiraterone, som irreversibelt hemmer CYP17A1 (17α-hydroxylase/C17,20-lyase), et nøkkelenzym i androgenbiosyntesen. Ved å blokkere androgenproduktsjonen i testiklene, binyrenene og prostatakrefftvevsene, hemmer det tumorveksten som er drevet av androgenreseptorsignalering. Det er globalt godkjent (FDA, EMA) for bruk i kombinasjon med prednison for mCRPC og metastatisk høyrisiko kastrasjonssensitiv prostatakrefft (mCSPC).

Detaljerte data om virkningsmekanisme var ikke inkludert i bevissamlingen (identifisert som datahull DG002). Når TxGNN genererer en forutsagt indikasjon, bør data om virkningsmekanisme hentes fra DrugBank for å vurdere om CYP17A1-hemningsbanen – eller sekundære farmakologiske effekter – kunne være relevant for den nye målsykdommen.

## Klinisk forsøksbevis

For tiden har ingen forutsagt indikasjon blitt generert; derfor ble ingen indikasjonsspesifikk klinisk forsøkssøking utført.

## Litteraturbevis

For tiden har ingen forutsagt indikasjon blitt generert; derfor ble ingen indikasjonsspesifikk litteratursøking utført.

## Taiwans markedsinformasjon

Abiraterone acetat har **ingen TFDA-godkjente lisenser** registrert i denne bevissamlingen. Legemidlet er oppført som "Ikke markedsført" i Taiwan.

## Cytotoksisitet

Abiraterone acetat er et antineoplastisk middel (androgenbiosyntesehemmer) og krever derfor vurdering av cytotoksisitet.

| Element | Innhold |
|---------|---------|
| Cytotoksisitetsklassifisering | Målrettet terapi (Hormonell / Androgenbiosyntesehemmer) |
| Myelosuppresjonrisiko | Lav (ikke et konvensjonelt cytotoksikum; anemi er en kjent bivirkning) |
| Emetogenitetsklassifisering | Lav |
| Parametre som skal overvåkes | Leverfunksjon (ALT/AST — hepatotoksisitetrisiko), blodtrykk, serumkalium, serumkortisol, CBC, hjertfunksjon |
| Håndtelingskrav | Standardforholdsregler; ikke klassifisert som konvensjonelt cytotoksikum — ingen spesiell lukket systemhåndtering påkrevd, men gravide kvinner bør unngå håndtering av knuste/oppbrutte tabletter |

## Sikkerhetshensyn

Ingen TFDA-pakningsvedleggsdata, advarsler, kontraindikasjoner eller legemiddel–legemiddelinteraksjonsdata var tilgjengelig i denne bevissamlingen.

> Vennligst se pakningsvedlegget for sikkerhetsinformasjon. Viktige globale sikkerhetshensyn inkluderer:
> - **Hepatotoksisitet** — ALT/AST-elevasjoner som krever overvåking
> - **Mineralokortikoidoverskudd** — Høyt blodtrykk, hypokalemi, væskeretensjon (på grunn av CYP17A1-blokkering oppstrøms for mineralokortikoidbiosyntese)
> - **Binyrebarkeinsufficiens** — Krever samtidig administrering av kortikosteroid
> - **Hjertesykdommer** — Hjertesvikt, atrieflimmer rapportert

## Konklusjon og neste trinn

**Beslutning: Avvent**

**Begrunnelse:**
TxGNN-modellen har ikke ennå produsert en forutsagt ny indikasjon for abiraterone acetat, og det finnes flere blokkerende datahull (TFDA-merking, data om virkningsmekanisme). Uten en målindikasjon kan ingen bevisnivåvurdering eller go/no-go-anbefaling gis.

**For å fortsette er følgende nødvendig:**
- Kjør TxGNN-prediksjonsrørledningen for abiraterone acetat for å generere kandidatindikasjonene
- Løs **DG001** (Blokkering): Hent TFDA-pakningsvedleggets advarsler og kontraindikasjoner, eller noter at legemidlet ikke er markedsført i Taiwan og hent sikkerhetsinformasjon fra FDA/EMA-etiketter i stedet
- Løs **DG002** (Høy): Søk i DrugBank etter data om virkningsmekanisme og farmakologisk klassifisering (DrugBank ID: [DB05812](https://go.drugbank.com/drugs/DB05812))
- Klargjør Taiwans regulatoriske vei — hvis legemidlet ikke er markedsført i Taiwan, bestem om en TFDA-importvei eller ordning for spesiell tilgang gjelder
- Regenerer bevissamlingen når de ovennevnte gapene er fylt og TxGNN-prediksjoner er tilgjengelige

## Ansvarsfraskrivelse

Dette innholdet er kun til forskningsformål og utgjør ikke medisinsk rådgivning.
Klinisk validering kreves før enhver klinisk anvendelse.

---

