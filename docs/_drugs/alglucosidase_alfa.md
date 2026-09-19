---
layout: default
title: Alglucosidase Alfa
parent: Kun modellprediksjon (L5)
nav_order: 22
evidence_level: L5
indication_count: 10
---

# Alglucosidase Alfa
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

# Alglucosidase alfa: Fra Pompe-sykdom til voksne polyglukosan-kropp-sykdom

## Sammendrag i én setning

> Alglucosidase alfa er en rekombinant menneskelig sur α-glukosidase (rhGAA) enzymersatningsbehandling kjent for behandling av Pompe-sykdom (glykogenlageringsykdom type II). TxGNN-modellen forutsier at det kan være effektivt for **voksne polyglukosan-kropp-sykdom**, men denne retningen er for øyeblikket støttet av **0 kliniske forsøk** og **0 publikasjoner**, og bevispaketets egen mekanistiske analyse flaggar forutsigelsen som et sannsynlig ontologi-/innebygd-romlig artefakt snarere enn et ekte farmakologisk signal.

---

## Rask oversikt

| Punkt | Innhold |
|------|---------|
| Opprinnelig indikasjon | Pompe-sykdom (utledet fra mekanistisk begrunnelse — ingen offisiell norsk autorisasjonstekst tilgjengelig; legemidlet markedsføres ikke) |
| Forutsagt ny indikasjon | Voksne polyglukosan-kropp-sykdom |
| TxGNN forutsigelsesscore | 99.47% |
| Bevisnivå | L5 (modellforutsigelse bare, ingen kliniske forsøk eller litteratur) |
| Markedsstatus i Norge | ✗ Ikke markedsført |
| Antall autorisasjoner | 0 |
| Anbefalt beslutning | Avvent |

---

## Hvorfor er denne forutsigelsen rimelig?

For tiden er legemidlets offisielle virkningsmekanisme-felt markert som et datahull i denne bevispakningen. Imidlertid, basert på den mekanistiske begrunnelsen som følger med forutsigelsene, forstås alglucosidase alfa å være rekombinant menneskelig sur α-glukosidase (rhGAA), brukt for å erstatte det manglende GAA-enzymet hos Pompe-sykdom-pasienter slik at lysosomale glykogenansamlinger kan brytes ned.

Voksne polyglukosan-kropp-sykdom (APBD) er derimot forårsaket av mangel på glykogenforgreningsenzym (GBE1), som fører til unormale, dårlig forgrenet polyglukosan-legemer som akkumuleres i nevronalt cytoplasma — en ikke-lysosomale, cytoplasmatisk metabolsk prosess atskilt fra den lysosomale GAA-banen som alglucosidase alfa virker på. Selv om begge tilstander faller inn under den brede kategorien av «glykogenlageringsykdom», skiller de årsaksforhold-enzymer, akkumuleringssteder og patologiske mekanismer seg ut, og rhGAA-erstatning kan ikke korrigere en GBE1-funksjonell defekt.

Bemerkelsesverdig gjentar samme mekanisme-mismatch-mønster seg på tvers av alle 10 av legemidlets beste TxGNN-forutsigelser i dette bevispakket — inkludert to andre GBE1-relaterte GSD IV-subtyper (ranger 2–3) og seks ikke-relaterte medfødt oftalmologisk/kranial-nerve-lidelser (ranger 4, 5, 6, 7, 8, 9, 10: medfødt entropion/ektropion, Horners syndrom, ptose-stemmebåndsparalyse-syndrom, camptodactyly-myopi-fibrose-syndrom, epiblefaron, og ptose-strabismus-ektopiske pupiller-syndrom). Ingen av disse har noen kjent eller hypotetisert biologisk bane som forbinder det til GAA-enzymersatningsbehandling. Dette gjentakende mønsteret tyder sterkt på at de høye TxGNN-score reflekterer sykdoms-ontologi eller innebygd-romlig nærhet (f.eks. delt «glykogenlageringsykdom»-merking, eller generell sjelden-sykdom-clustering) snarere enn ekte farmakologisk plausibilitet, og hele forutsigelsessettet bør behandles som et sannsynlig støycluster snarere enn individuelt lovende ledetråder.

---

## Bevis fra kliniske forsøk

For tiden ingen relaterte kliniske forsøk registrert

---

## Litteraturbevis

For tiden ingen relatert litteratur tilgjengelig

---

## Sikkerhetshensyn

Vennligst se pakningsvedlegget for sikkerhetsinformasjon.

---

## Konklusjon og neste steg

**Beslutning: Avvent**

**Begrunnelse:**
- Alle 10 topprankerte forutsagte indikasjoner er bevisnivå L5 (modellforutsigelse bare, null kliniske forsøk, null litteratur), og den mekanistiske begrunnelsen som følger hver forutsigelse flaggar eksplisitt mekanismeavvik eller ikke-relatert patologi — som peker mot et sannsynlig innebygd-romlig artefakt snarere enn et troverdig ombruk-signal for voksne polyglukosan-kropp-sykdom eller noen av de andre 9 forutsagte indikasjonene.
- Et blokkerende datahull finnes også på TFDA/regulatorisk sikkerhetsetikett (advarsler, kontraindikasjoner), som uavhengig forhindrer denne kandidaten fra å gå videre til en fase 1-sikkerhetsgjennomgang uavhengig av ombrukssignalstyrken.

**For å gå videre kreves følgende:**
- Offisiell virkningsmekanisme (MOA) data bekreftet via DrugBank eller produsentens etikett (for tiden et datahull)
- TFDA/EMA pakningsvedlegg advarsler og kontraindikasjoner (for tiden et blokkerende datahull)
- Uavhengig våt-lab eller genetisk/biomarkør-evidens som forbinder GAA-enzymersatning til GBE1-medieret polyglukosan-ansamling, før ytterligere evaluering av denne ombruksretningen er berettiget
- En gjennomgang av hele 10-forutsigelsesklyngen for å bestemme om et systematisk ontologi-likhet-artefakt som påvirker dette legemidlets TxGNN-utdata bør flagges til modell-/datateamet

## Ansvarsfraskrivelse

Dette innholdet er kun til forskningsformål og utgjør ikke medisinsk rådgivning.
Klinisk validering kreves før enhver klinisk anvendelse.

---

