---
layout: default
title: Elvitegravir
parent: Kun modellprediksjon (L5)
nav_order: 127
evidence_level: L5
indication_count: 3
---

# Elvitegravir
{: .fs-9 }

Evidensnivå: **L5** | Predikerte indikasjoner: **3** stk.
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

# Elvitegravir: Fra HIV-1-infeksjon til Feline Immunodeficiency Virus (FIV)-infeksjon

## Sammendrag på én setning

Elvitegravir er kjent i bevissamlingens egne mekanistiske notater som en HIV-1-integrase-strandoverføringshemmer (INSTI); imidlertid er det ikke tilstede noen formell opprinnelig indikasjon eller MOA-registrering i kildedata (begge er flagget som datamangler).
TxGNN-modellens toppforutsigelse er **Feline Acquired Immunodeficiency Syndrome (FIV)** — en veterinær, ikke-menneskelig sykdom — med en poengsum på **99.89%**, men denne rangeringen er støttet av **0 kliniske forsøk** og **0 publikasjoner**.
En andrerangert kandidat, Simian Immunodeficiency Virus (SIV)-infeksjon, har faktisk støttende litteratur (7 artikler), men disse er forskningstoolstudier av HIV-medikamentresistans i makak-modeller, ikke en menneskelig klinisk indikasjon. Samlet sett er beviset som støtter denne kandidaten som en genuin menneskelig legemiddelomlegging-mulighet veldig svakt.

## Hurtigoversikt

| Element | Innhold |
|---------|---------|
| Opprinnelig indikasjon | Ikke angitt i bevissamlingen (`original_indications` tom; mekanistiske notater beskriver elvitegravir som en HIV-1-integrasehemmer) |
| Forutsagt ny indikasjon | Feline Acquired Immunodeficiency Syndrome (FIV) |
| TxGNN-forutsigelsespoeng | 99.89% |
| Bevisnivå | L5 |
| Status på norskmarkedet | Ikke markedsført (Ikke markedsført) |
| Antall autorisasjoner | 0 |
| Anbefalt beslutning | Vente |

## Hvorfor er denne forutsigelsen rimelig?

For tiden er detaljerte virkningsmekanismedata ikke tilgjengelig (datamangel DG002). Basert på de mekanistiske notatene innebygd i bevissamlingen, er elvitegravir en HIV-1-integrase-strandoverføringshemmer (INSTI), en klasse som blokkerer retroviralt DNA-integrasjon inn i vertens genom.

Den topprangerte forutsagte indikasjonen — Feline Immunodeficiency Virus (FIV)-infeksjon — er biologisk knyttet til elvitegravirs mekanisme bare gjennom et bredt taksonomiargument: FIV og HIV er begge lentivirus, og integraserettet hemming er teoretisk tversartsanvendbar. Imidlertid er denne begrunnelsen eksplisitt notert i bevissamlingen som **kun teoretisk**, uten noen in vitro eller in vivo FIV-spesifikk data, og FIV er en veterinær (felint) sykdom snarere enn et typisk menneskelig legemiddelomleggingsmål.

En sekundær kandidat, SIV-infeksjon (rang 2), har sterkere mekanistisk støtte — flere in vitro- og ikke-menneske-primatstudier bekrefter elvitegravirs antiviralt aktivitet og resistensprofil mot SIV/SHIV, gitt den høye homologien mellom SIV og HIV-integrasesekvenser. Kritisk imidlertid, disse studiene bruker SIV/SHIV-makak-modeller rent som **forskningsverktøy for å studere HIV-medikamentresistans**, ikke som et behandlingsmål for en apesykdom. Heller ingen av de forutsagte indikasjonene representerer derfor en troverdig kandidat for menneskelig legemiddelomlegging under standard legemiddelomleggingskriterier.

## Bevis fra kliniske forsøk

For tiden ingen relaterte kliniske forsøk registrert

## Litteraturbevis

For tiden ingen relatert litteratur tilgjengelig

*(Merknad: den topprangerte forutsagte indikasjonen, FIV, har ingen støttende litteratur. Rang-2-kandidaten, SIV-infeksjon, har 7 støttende publikasjoner — primært in vitro-resistens-/mekanisme-studier i SIV/SHIV-modeller — men disse tjener som HIV-integrasehemmer-forskningsverktøy snarere enn bevis for en distinkt menneskelig indikasjon, og er derfor ikke tabulert her i henhold til rang-1-rapporteringskonvensjonen.)*

## Norges markedsinformasjon

Dette legemidlet har for tiden ingen markedsføringstillatelse i Norge (Ikke markedsført / Ikke markedsført); `total_licenses` = 0 og ingen lisensoppføringer er tilgjengelig i bevissamlingen.

## Sikkerhetshensyn

Se pakningsvedlegget for sikkerhetsinformasjon.

*(Merknad: datamangel DG001 — TFDA/lokalt pakningsvedlegg advarsler og kontraindikasjoner — er flagget som et **blokkert** alvorlighetsmangler, som betyr at denne kandidaten ennå ikke kan bestå innledende sikkerhetsvurdering (S1).)*

## Konklusjon og neste steg

**Beslutning: Vente**

**Begrunnelse:**
Den topprangerte forutsagte indikasjonen (FIV) er en veterinærsykdom uten kliniske forsøk eller litteraturstøtte (Bevisnivå L5, beslutningsfase S0), og er ikke et troverdig menneskelig legemiddelomleggingsmål. Neste beste kandidat (SIV-infeksjon) er støttet bare av HIV-resistensforskningsverktøystudier i dyremodeller, ikke en genuin sykdomsindikasjon. Kombinert med et **blokkert** datamangel (DG001) og manglende MOA-dokumentasjon (DG002), møter denne kandidaten ikke terskelen for å gå videre.

**For å gå videre, kreves følgende:**
- TFDA/regulatorisk pakningsvedlegg (advarsler, kontraindikasjoner) — nødvendig for å fjerne det **blokkerte** datamangler (DG001) før noen S1-sikkerhetsvurdering
- Bekreftet MOA-dokumentasjon via DrugBank API (DG002)
- Ny screening av TxGNN-resultater for å identifisere om høyere-kvalitet, menneskelig-relevante forutsagte indikasjoner finnes utover de nåværende topp 3 (rang 3, en sjelden nevrouviklingsforstyrrelselse, antas å være modelstøy uten biologisk plausibilitet)
- Hvis interesse gjenstår i SIV-relatert forskningsvinkel, avklaring av tiltenkt menneskelig befolkning og klinisk translasjonsbarhet, siden nåværende bevis er begrenset til ikke-menneske-primat-medikamentresistans-modellering

## Ansvarsfraskrivelse

Dette innholdet er kun til forskningsformål og utgjør ikke medisinsk rådgivning.
Klinisk validering kreves før enhver klinisk anvendelse.

---

