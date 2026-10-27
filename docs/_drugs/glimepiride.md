---
layout: default
title: Glimepiride
parent: Kun modellprediksjon (L5)
nav_order: 191
evidence_level: L5
indication_count: 9
last_modified_at: 2026-10-15
description: "Glimepiride: predikert ny indikasjon Fokalt stivt lem-syndrom (evidensnivå L5). Opprinnelig indikasjon: Diabetes mellitus, type 2"
monitor_inn: "GLIMEPIRIDE"
predicted_indications: ["focal stiff limb syndrome", "classic stiff person syndrome", "opsismodysplasia", "thiamine-responsive dysfunction syndrome", "drug-induced localized lipodystrophy", "centrifugal lipodystrophy", "pressure-induced localized lipoatrophy", "idiopathic localized lipodystrophy", "pancreatic agenesis"]
---

# Glimepiride
{: .fs-9 }

Evidensnivå: **L5** | Predikerte indikasjoner: **9** stk.
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

## Glimepirid: Fra type 2-diabetes til fokalt stivt lem-syndrom
{: .text-alpha }

## Oppsummering i én setning

Glimepirid er et sulfonylurea-legemiddel som opprinnelig brukes til behandling av type 2-diabetes.
TxGNN-modellen forutsier at det kan være effektivt mot **fokalt stivt lem-syndrom** (og beslektede tilstander som klassisk stiff person-syndrom),
men **ingen kliniske studier og ingen relevant litteratur** støtter denne retningen i dag. Prediksjonen er rent beregningsbasert.

---

## Hurtigoversikt

| Punkt | Innhold |
|------|------|
| Opprinnelig indikasjon | Diabetes mellitus, type 2 |
| Predikert ny indikasjon | Fokalt stivt lem-syndrom |
| TxGNN-prediksjonsscore | 99,75 % |
| Evidensnivå | L5 |
| Markedsstatus i Norge | Kun trukket tilbake (ingen gyldige markedsføringstillatelser) |
| Antall tillatelser | 1 (trukket tilbake) |
| Anbefalt beslutning | Hold |

---

## Hvorfor er denne prediksjonen (ikke) rimelig?

Data om virkningsmekanisme er ikke tilgjengelige i de sammenstilte dataene. Glimepirid er kjent som et sulfonylurea som virker på KATP-kanaler i betaceller i bukspyttkjertelen og stimulerer insulinfrigjøring. Dette er godt dokumentert ved type 2-diabetes.

Stivt lem-syndrom og stiff person-syndrom er nevroimmunologiske sykdommer knyttet til nedsatt GABAerg/glycinerg hemming, ofte med anti-GAD65-antistoffer. Tilstandene forekommer hyppig sammen med diabetes og andre autoimmune sykdommer. Den høye scoren skyldes trolig denne nettverksassosiasjonen i kunnskapsgrafen, og ikke en reell terapeutisk effekt. Glimepirid behandler hyperglykemi, ikke den underliggende nevroimmune sykdommen, og etablerte behandlinger (benzodiazepiner, baklofen, IVIG) har en klar begrunnelse som glimepirid mangler.

Øvrige topp-prediksjoner følger samme mønster:

| Rang | Predikert sykdom | Score | Vurdering |
|------|------|------|------|
| 2 | Klassisk stiff person-syndrom | 99,75 % | Indirekte, trolig konfundert assosiasjon via GAD65/diabetes |
| 3 | Opsismodysplasi | 99,74 % | Spekulativ kobling til insulinsignalering; ingen støtte for effekt på skjelettutvikling |
| 4 | Tiaminresponsivt dysfunksjonssyndrom | 99,73 % | Diabetes er en del av syndromet; kan i beste fall påvirke bare den glykemiske komponenten |
| 5–8 | Lokaliserte lipodystrofier (legemiddelindusert, sentrifugal, trykkinduusert, idiopatisk) | 99,56–99,62 % | Ingen plausibel mekanisme; trolig artefakt fra nærhet til diabetes/lipodystrofi i nettverket |
| 9 | Pankreasagenesi | 99,55 % | Mekanistisk usannsynlig uten funksjonelle betaceller; insulin er standardbehandling |

---

## Kliniske studier

Foreløpig er ingen relaterte kliniske studier registrert.

---

## Litteraturevidens

For den høyest rangerte indikasjonen (fokalt stivt lem-syndrom) finnes ingen relevant litteratur.

For pankreasagenesi (rang 9) ble én artikkel funnet, men den er ikke relevant evidens:

| PMID | År | Type | Tidsskrift | Hovedfunn |
|------|-----|------|------|---------|
| [12720536](https://pubmed.ncbi.nlm.nih.gov/12720536/) | 2003 | Annet (diagnostisk bildediagnostikk) | European Journal of Endocrinology | Fallgruver ved endosonografi ved mistenkt insulinom; omhandler ikke behandling med glimepirid |

---

## Informasjon om det norske markedet

| Tillatelsesnummer | Produktnavn | Doseringsform | Godkjent indikasjon |
|---------|------|------|-----------|
| EMEA/H/C/000680 | Tandemact | Ikke oppgitt | Diabetes mellitus, type 2 (status: trukket tilbake) |

Det finnes ingen gyldige tillatelser for glimepirid i de sammenstilte dataene.

---

## Sikkerhetsvurderinger

Pakningsvedlegg med advarsler og kontraindikasjoner var ikke tilgjengelig i de sammenstilte dataene. Se pakningsvedlegget for fullstendig sikkerhetsinformasjon.

**Kontraindikasjoner fra kunnskapsgrafen (ikke fra preparatomtale):** Kunnskapsgrafen (PrimeKG) angir kontraindikasjonskanter til blant annet:
- nyresykdom, leversykdom og galleblæresykdom
- kongestiv hjertesvikt
- hypofyse-insuffisiens og beslektede tilstander (f.eks. hypopituitarisme, Sheehans syndrom, isolert veksthormonmangel, hypogonadotrop hypogonadisme, Kallmanns syndrom)
- osteoporose og postmenopausal osteoporose
- sykdom i thymus og infeksjonssykdom

Disse er modellavledede signaler og må verifiseres mot offisiell preparatomtale.

**Legemiddelinteraksjoner:** Totalt 100 interaksjoner er funnet. Blant de som er vist, er de fleste av moderat alvorlighetsgrad, for eksempel:
- Fenylefrin, epinefrin, salbutamol, formoterol, pseudoefedrin (sympatomimetika)
- Acebutolol (betablokker)
- Famotidin, ranitidin
- Ibuprofen, ketorolak
- Hydrokortison, etinylestradiol, hydroklortiazid, acetazolamid
- Albiglutid, etanol, nitazoksanid, acitretin

Hydrokortison og alklometason til lokal bruk har mindre alvorlig (minor) interaksjon.

---

## Konklusjon og neste steg

**Beslutning: Hold**

**Begrunnelse:**
Alle predikerte indikasjoner har evidensnivå L5: ingen kliniske studier og ingen relevant litteratur. Mekanismen for glimepirid (stimulering av betacellers insulinsekresjon) har ingen etablert kobling til de predikerte nevrologiske, skjelett- eller lipodystrofitilstandene, og scorene gjenspeiler trolig nærhet til diabetes i kunnskapsgrafen. I tillegg er produktet i dag kun registrert med en trukket tilbake tillatelse i Norge.

**For å gå videre kreves følgende:**
- Data om virkningsmekanisme (MOA) fra DrugBank
- Pakningsvedlegg med advarsler og kontraindikasjoner (blokkerende datamangel for sikkerhetsscreening)
- Prekliniske data eller kasuistikker som kan underbygge en faktisk kobling til den predikerte sykdommen
- Avklaring av markedsstatus og tilgjengelige administrasjonsveier i Norge
## Ansvarsfraskrivelse

Dette innholdet er kun til forskningsformål og utgjør ikke medisinsk rådgivning.
Klinisk validering kreves før enhver klinisk anvendelse.

---

