---
layout: default
title: Turoctocog Alfa Pegol
parent: Kun modellprediksjon (L5)
nav_order: 439
evidence_level: L5
indication_count: 10
---

# Turoctocog Alfa Pegol
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

# Turoctocog alfa pegol: Fra hemofili A til primær frigjøringsforstyrrelse i blodplater

## Oppsummering

Turoctocog alfa pegol er et PEGylert rekombinant koagulasjonsfaktor VIII-preparat (markedsført som Esperoct), opprinnelig brukt til behandling av **hemofili A**.
TxGNN-modellen forutsier at legemidlet kan ha effekt ved **primær frigjøringsforstyrrelse i blodplater** (primary release disorder of platelets), men det finnes **ingen kliniske studier** og **ingen publikasjoner** som støtter denne retningen.
Prediksjonen er derfor kun en modellberegning (evidensnivå L5).

---

## Hurtigoversikt

| Punkt | Innhold |
|------|------|
| Opprinnelig indikasjon | Hemofili A |
| Predikert ny indikasjon | Primær frigjøringsforstyrrelse i blodplater |
| TxGNN-prediksjonsscore | 99,997 % |
| Evidensnivå | L5 |
| Markedsstatus i Norge | Kun opphevede (trukkede) autorisasjoner |
| Antall autorisasjoner | 1 |
| Anbefalt beslutning | Hold (avvent) |

---

## Hvorfor er denne prediksjonen (ikke) rimelig?

Det foreligger for tiden ikke detaljerte data om virkningsmekanisme for dette legemidlet. Turoctocog alfa pegol er et PEGylert rekombinant faktor VIII-produkt. Det erstatter manglende faktor VIII hos pasienter med hemofili A, og effekten er etablert for denne indikasjonen.

Primær frigjøringsforstyrrelse i blodplater skyldes imidlertid en defekt i blodplatefunksjonen (sekresjon fra granula), ikke mangel på faktor VIII. Det er derfor ingen tydelig mekanistisk begrunnelse for å bruke et faktor VIII-preparat. Den høye scoren (0,99997) er trolig drevet av nærhet i nettverket innenfor gruppen av blødningsforstyrrelser, og er ikke et uttrykk for klinisk støtte.

### Andre predikerte indikasjoner

Modellen foreslår også andre tilstander. Ingen av dem har kliniske studier eller litteratur i datagrunnlaget, og alle er vurdert til L5 og Hold:

| Rang | Sykdom | Score | Mekanistisk vurdering |
|------|------|------|------|
| 2 | Pseudo-von Willebrands sykdom | 99,996 % | Plausibel kun på signalveinivå (VWF bærer og stabiliserer FVIII), men faktor VIII korrigerer ikke reseptordefekten i blodplatene |
| 3 | Glanzmanns trombasteni | 99,996 % | Defekt i integrin αIIbβ3; faktor VIII adresserer ikke dette. Standardbehandling er blodplatetransfusjon eller rekombinant FVIIa |
| 4 | Ervervet koagulasjonsfaktormangel | 99,974 % | Mekanistisk mest sammenhengende (f.eks. ervervet hemofili A), men hemmende autoantistoffer gjør ofte erstatning lite effektiv. Kategorien er bred og uensartet |
| 5 | Scott syndrom | 99,973 % | Defekt fosfatidylserin-eksponering (TMEM16F/ANO6); mer FVIII gjenoppretter ikke overflaten som kreves. Spekulativ kobling |
| 6 | Blødningstendens ved kollagenreseptordefekt | 99,949 % | Defekt i GPVI eller α2β1, uten sammenheng med FVIII |
| 7 | Hemoragisk forstyrrelse ved konstitusjonell trombocytopeni | 99,948 % | Blødning skyldes blodplatemangel, ikke FVIII-mangel |
| 8 | «Flood factor deficiency» | 99,752 % | Sykdomsnavnet virker ikke-standard eller et ontologi-artefakt og bør verifiseres |
| 9 | Hereditær trombocytose med transversal lemdefekt | 99,694 % | Ikke en FVIII-mangeltilstand; FVIII kan være uønsket pga. tromboserisiko. Trolig grafartefakt |
| 10 | Føtal og neonatal alloimmun trombocytopeni | 99,693 % | Immunmediert blodplateødeleggelse; behandles med IVIG, kortikosteroider og kompatible blodplater |

---

## Klinisk evidens

Det er for tiden ingen relaterte kliniske studier registrert.

---

## Litteraturevidens

Det foreligger for tiden ingen relevant litteratur.

---

## Informasjon om det norske markedet

| Autorisasjonsnummer | Produktnavn | Doseringsform | Godkjent indikasjon |
|---------|------|------|-----------|
| EMEA/H/C/004883 | Esperoct | Ikke oppgitt | Hemofili A |

Autorisasjonen er opphevet, og det finnes ingen gyldige autorisasjoner (produsent: Novo Nordisk A/S).

---

## Sikkerhetsvurderinger

Se pakningsvedlegget for sikkerhetsinformasjon.

---

## Konklusjon og neste steg

**Beslutning: Hold**

**Begrunnelse:**
Prediksjonene bygger kun på modellberegning (L5) uten kliniske studier eller litteratur, og for de fleste tilstandene mangler en plausibel mekanisme fordi sykdommene skyldes blodplatedefekter og ikke FVIII-mangel. I tillegg er produktet ikke lenger gyldig autorisert på markedet.

**For å gå videre kreves følgende:**
- Data om virkningsmekanisme (MOA) fra DrugBank
- Advarsler og kontraindikasjoner fra pakningsvedlegget, som er nødvendig for sikkerhetsscreening
- Verifisering av sykdomsnavn som «flood factor deficiency» mot en sykdomsdatabase
- Systematisk litteratur- og studiesøk for den mest sammenhengende kandidaten (ervervet koagulasjonsfaktormangel, f.eks. ervervet hemofili A)
- Avklaring av markedsstatus og tilgjengelighet i Norge dersom videre utredning er aktuelt
## Ansvarsfraskrivelse

Dette innholdet er kun til forskningsformål og utgjør ikke medisinsk rådgivning.
Klinisk validering kreves før enhver klinisk anvendelse.

---

