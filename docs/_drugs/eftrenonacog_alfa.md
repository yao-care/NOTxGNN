---
layout: default
title: Eftrenonacog Alfa
parent: Kun modellprediksjon (L5)
nav_order: 123
evidence_level: L5
indication_count: 3
---

# Eftrenonacog Alfa
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

# Eftrenonacog alfa: Fra hemofili B til pseudo-von Willebrand-sykdom

## Sammendrag i en setning

Eftrenonacog alfa er et rekombinant Factor IX-Fc fusjonprotein som brukes som koagulasjonsfaktor-erstatningsterapi for hemofili B.
TxGNN-modellen forutsier at det kan være effektivt for **pseudo-von Willebrand-sykdom**,
men dette signalet støttes foreløpig av **0 kliniske forsøk** og **0 publikasjoner**, og det underliggende mekanistiske resonnementet i seg selv reiser bekymringer om en falsk positiv prediksjon.

## Rask oversikt

| Element | Innhold |
|------|------|
| Original indikasjon | Hemofili B (basert på kjent legemiddelklasse; formell indiksjonstekst er ikke tilgjengelig i dette datasettet) |
| Forutsagt ny indikasjon | Pseudo-von Willebrand-sykdom |
| TxGNN-prediksjonspoeng | 99.48% |
| Bevisnivå | L5 |
| Markedsstatus i Norge | ✗ Ikke markedsført |
| Antall autorisasjoner | 0 |
| Anbefalt beslutning | Avvent |

## Hvorfor er denne prediksjonen rimelig?

For tiden er detaljerte data om virkningsmekanisme ikke tilgjengelig i DrugBank for denne posten. Basert på kjent farmakologi er eftrenonacog alfa et rekombinant Factor IX-Fc fusjonprotein som erstatter mangelfull endogent Factor IX i den indre koaguleringsbanen, og effektiviteten i hemofili B er godt etablert.

De tre beste TxGNN-forutsagte indikasjonene for dette legemidlet — pseudo-von Willebrand-sykdom, primær utslipsforstyrrelse av blodplater og Glanzmann-trombasteni — er imidlertid alle **blodplate-nivå-forstyrrelser** (unormal GPIb–vWF affinitet, defekt granulatutslipping og GPIIb/IIIa-reseptormangel, henholdsvis), ikke koagulasjonsfaktormangel. Factor IX-erstatning virker på trombingenerasjon og har ingen kjent mekanisme for å korrigere blodplate-reseptor- eller granulatdefekter.

Dette avviket antyder at høye TxGNN-poenger sannsynligvis gjenspeiler klyngring av «blødningsforstyrrelse»-noder innen kunnskapsgrafen snarere enn ekte delt farmakologi. Alle tre kandidatene bør behandles som signaler med lav sikkerhet og uklar mekanisme som venter på ytterligere validering, ikke som farmakologisk baserte omdisponeringshypoteser.

## Bevis fra kliniske forsøk

For tiden er ingen relaterte kliniske forsøk registrert

## Bevis fra litteratur

For tiden er ingen relatert litteratur tilgjengelig

## Markedsinformasjon for Norge

Dette legemidlet er ikke for tiden markedsført i Norge (0 autorisasjoner på posten); ingen lisens- eller produktinformasjon er tilgjengelig.

## Sikkerhetshensyn

Se pakningsvedlegget for sikkerhetsinformasjon.

## Konklusjon og neste trinn

**Beslutning: Avvent**

**Begrunnelse:**
Dette er en modell-kun prediksjon (L5) uten støttende kliniske forsøk eller litteratur, og den foreslåtte mekanistiske koblingen mellom Factor IX-erstatning og blodplate-funksjonsforstyrrelser er svak — mønsteret er mer i samsvar med kunnskapsgraf-nodeklyngring enn ekte farmakologisk relevans.

**For å fortsette, kreves følgende:**
- Bekreftet data om virkningsmekanisme (MOA) fra DrugBank eller primærlitteratur (for tiden kritisk datakløft, DG002)
- TFDA/produsentmerking med advarsler og kontraindikasjoner, påkrevd før eventuell sikkerhetspre-screening (kritisk datakløft, DG001)
- Uavhengig mekanistisk eller preklinisk evidens som direkte knytter Factor IX-veiens aktivitet til blodplate-vWF eller blodplate-reseptorforstyrrelser
- Virkelige tilfellerapporter eller registerdata for Factor IX-produkter som brukes i disse blodplate-forstyrrelsene, hvis noen finnes, for å skille ekte signal fra prediksjonsartefakt

## Ansvarsfraskrivelse

Dette innholdet er kun til forskningsformål og utgjør ikke medisinsk rådgivning.
Klinisk validering kreves før enhver klinisk anvendelse.

---

