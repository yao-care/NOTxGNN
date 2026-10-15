---
layout: default
title: Lonoctocog Alfa
parent: Kun modellprediksjon (L5)
nav_order: 250
evidence_level: L5
indication_count: 4
---

# Lonoctocog Alfa
{: .fs-9 }

Evidensnivå: **L5** | Predikerte indikasjoner: **4** stk.
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

# Lonoktokog alfa: Fra hemofili A til pseudo-von Willebrand sykdom

## Oppsummering i én setning

Lonoktokog alfa er en rekombinant, enkeltkjedet faktor VIII med avkortet B-domene, opprinnelig utviklet for behandling av hemofili A.
TxGNN-modellen predikerer at legemidlet kan ha effekt ved **pseudo-von Willebrand sykdom**, men det finnes foreløpig **ingen kliniske studier** og **ingen publikasjoner** som støtter denne retningen. Prediksjonen er ren modellberegning.

---

## Hurtigoversikt

| Punkt | Innhold |
|------|------|
| Opprinnelig indikasjon | Hemofili A |
| Predikert ny indikasjon | Pseudo-von Willebrand sykdom |
| TxGNN-prediksjonsscore | 99,85 % |
| Evidensnivå | L5 |
| Markedsstatus i Norge | Kun trukket tilbake (kansellert) |
| Antall godkjenninger | 1 |
| Anbefalt beslutning | Hold |

Merk: Den eneste registrerte godkjenningen (EMEA/H/C/004075) er en sentral europeisk markedsføringstillatelse, og den er kansellert.

---

## Hvorfor er denne prediksjonen rimelig?

Data om virkningsmekanisme (MOA) er foreløpig ikke tilgjengelig. Basert på kjent informasjon er lonoktokog alfa et rekombinant faktor VIII-preparat (rVIII-SingleChain) med bevist effekt ved hemofili A, der det erstatter manglende faktor VIII i koagulasjonskaskaden.

Pseudo-von Willebrand sykdom (blodplatetype VWD) skyldes funksjonsøkende varianter i GP1BA. Disse øker blodplatenes GPIb-affinitet for von Willebrand-faktor (VWF) og fører til økt opprydding av høymolekylære VWF-multimerer. Faktor VIII-erstatning korrigerer ikke denne reseptordefekten. Plasmanivået av FVIII kan imidlertid bli sekundært redusert på grunn av tap av VWF, så det finnes en teoretisk kobling, men den er indirekte.

Den høye TxGNN-scoren er derfor en beregningsmessig prediksjon, uten støtte i kliniske data.

### Øvrige predikerte indikasjoner

| Rang | Sykdom | TxGNN-score | Evidensnivå | Vurdering av mekanistisk kobling |
|------|------|------|------|------|
| 2 | Primær frigjøringsforstyrrelse av blodplater | 99,84 % | L5 | Defekten ligger i blodplatene. FVIII korrigerer ikke sekresjonsdefekter. Scoren gjenspeiler trolig nærhet i nettverket mellom blødningslidelser. |
| 3 | Glanzmanns trombasteni | 99,76 % | L5 | Skyldes mangel på eller dysfunksjon av integrin αIIb/β3. Koagulasjonskaskaden er normal. Standardbehandling er blodplatetransfusjon, rekombinant FVIIa og antifibrinolytika. |
| 4 | Scotts syndrom | 99,44 % | L5 | Defekt eksponering av fosfatidylserin på aktiverte blodplater (TMEM16F/ANO6). Løs konseptuell kobling til tenase-komplekset, men FVIII forventes ikke å korrigere defekten. |

---

## Klinisk studieevidens

Foreløpig er det ingen relaterte kliniske studier registrert.

---

## Litteraturevidens

Foreløpig er det ingen relatert litteratur tilgjengelig.

---

## Informasjon om det norske markedet

| Godkjenningsnummer | Produktnavn | Doseringsform | Godkjent indikasjon |
|---------|------|------|-----------|
| EMEA/H/C/004075 | Afstyla (CSL Behring GmbH) | Ikke oppgitt | Hemofili A |

Status: kansellert.

---

## Sikkerhetsvurderinger

Se pakningsvedlegget for sikkerhetsinformasjon. Data om advarsler og kontraindikasjoner er ikke innhentet for denne rapporten, og det er ikke funnet registrerte legemiddelinteraksjoner i de samlede dataene.

---

## Konklusjon og neste steg

**Beslutning: Hold**

**Begrunnelse:**
Alle fire prediksjonene er på evidensnivå L5, uten kliniske studier eller publikasjoner. Den mekanistiske koblingen er svak eller indirekte, fordi de predikerte sykdommene primært skyldes blodplate- eller VWF-relaterte defekter som FVIII-erstatning ikke korrigerer. I tillegg er den eneste godkjenningen kansellert.

**For å gå videre kreves følgende:**
- Pakningsvedlegg med advarsler og kontraindikasjoner (blokkerende datamangel, hindrer sikkerhetsscreening)
- Data om virkningsmekanisme (MOA) fra DrugBank
- Prekliniske eller mekanistiske studier som viser om FVIII-erstatning har noen rolle ved sekundær FVIII-reduksjon ved pseudo-von Willebrand sykdom
- Avklaring av administrasjonsvei og forholdet til den opprinnelige indikasjonen
- Litteratursøk og søk i studieregistre med tanke på kasuistikker eller kliniske data
## Ansvarsfraskrivelse

Dette innholdet er kun til forskningsformål og utgjør ikke medisinsk rådgivning.
Klinisk validering kreves før enhver klinisk anvendelse.

---

