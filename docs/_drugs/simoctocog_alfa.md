---
layout: default
title: Simoctocog Alfa
parent: Kun modellprediksjon (L5)
nav_order: 325
evidence_level: L5
indication_count: 10
---

# Simoctocog Alfa
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

# Simoctocog Alfa: Fra Hemofili A til Pseudo-von Willebrand-sykdom

## Ensetnings-sammendrag

> Simoctocog alfa er et rekombinant humant koagulasjonsfaktor VIII (rFVIII)-preparat, kjent for bruk ved Hemofili A.
> TxGNN-modellens toppprediksjon er **Pseudo-von Willebrand-sykdom**, med en skår på **99.99%**,
> men denne prediksjonen er for tiden støttet av **0 kliniske studier** og **0 publikasjoner**, og den mekanistiske begrunnelsen selv er svak.

---

## Rask oversikt

| Element | Innhold |
|------|------|
| Originalindikasjon | Hemofili A (blødingsprofylakse/behandling) — ikke presentert i dette bevispackets godkjenningsdata, basert på kjent rFVIII-produktklasse |
| Predikert ny indikasjon | Pseudo-von Willebrand-sykdom |
| TxGNN-prediksjons skår | 99.99% |
| Bevisnivå | L5 |
| Norsk markedsstatus | Ikke markedsført |
| Antall godkjennelser | 0 |
| Anbefalt beslutning | Avvent |

---

## Hvorfor er denne prediksjonen rimelig?

For tiden er detaljerte data om virkningsmekanisme ikke tilgjengelige (flagget som et datakløft med høy alvorlighetsgrad). Basert på kjent informasjon er simoctocog alfa et rekombinant humant faktor VIII (rFVIII)-preparat som brukes for å erstatte mangelfull endogen FVIII og gjenopprette den indre koagulasjonsbanen hos pasienter med Hemofili A.

Imidlertid er den topprangerte predikerte indikasjonen — pseudo-von Willebrand-sykdom — forårsaket av en abnorm platelett GPIbα-reseptor med overdreven affinitet for von Willebrand-faktor (vWF), **ikke** av FVIII-mangel. I henhold til bevispackets egen mekanistiske vurdering har rFVIII-erstatning ingen direkte patofysiologisk rolle i korrigering av denne platelett-reseptor-defekten. Den høye TxGNN-skåren gjenspeiler mest sannsynlig den nære nærheten til FVIII–vWF-kompleksen i kunnskapsgrafen, snarere enn et kausalt behandlingsforhold.

Det er verdt å merke at blant de 10 kandidatene i dette bevispacket har **rang 9 ("Hemofili A med vaskulær abnormitet")** den sterkeste genuine mekanistiske plausibilitet, siden den ligger innenfor de kjente indikasjonene for FVIII-erstatning — likevel fikk den en langt lavere skår og har null støttende studier eller litteratur. Denne divergensen mellom mekanistisk plausibilitet og modellskår er en viktig forbehold: den topprangerte prediksjonen bør ikke behandles som klinisk handlingsdyktig uten uavhengig mekanistisk og godkjennings-verifisering.

---

## Bevis fra kliniske studier

For tiden ingen relevante kliniske studier registrert

---

## Bevis fra litteratur

For tiden ingen relevant litteratur tilgjengelig

---

## Norsk markedsinformasjon

Dette produktet er for tiden ikke markedsført i Norge; ingen markedsføringsgodkjennelser (0 lisenser) er blitt utstedt, så ingen indikasjonstermer fra godkjenningsdokumenter er tilgjengelig for kryssreferanse.

---

## Sikkerhetshensyn

Vennligst se pakningsvedlegget for sikkerhetsinformasjon.

*(Merk: Advarsler og kontraindikasjoner på godkjenningsnivå fra TFDA er markert som et blokkerende datakløft — dette må løses før noen sikkerhetspre-vurdering (S1) kan fortsette.)*

---

## Konklusjon og neste steg

**Beslutning: Avvent**

**Begrunnelse:**
Bevisnivået er L5 (kun modellprediksjon, ingen kliniske studier eller litteratur), og den topprangerte indikasjonen sin egen mekanistiske begrunnelse tyder på at den gjenspeiler nærhet i kunnskapsgrafen snarere enn et kausalt behandlingsforhold. Et blokkerende datakløft for godkjenningsdata (advarsler/kontraindikasjoner) forhindrer også at saken går inn i sikkerhetspre-vurdering.

**For å fortsette er følgende nødvendig:**
- Bekreftet virkningsmekanisme-data (MOA) fra DrugBank/produsent for å validere eller tilbakevise FVIII–vWF-nærhetshypotesen
- Analyse av TFDA/EMA-godkjennings-PDF for å løse det blokkerende sikkerhetsdatakløftet (advarsler, kontraindikasjoner)
- Manuell klinisk/hematologisk fagekspertvurdering av hvorvidt "pseudo-von Willebrand-sykdom" har noen dokumentert FVIII-respons når brukt utenfor indikasjon, gitt den mekanistiske uoverensstemmelsen
- Re-evaluering av rang 9 ("Hemofili A med vaskulær abnormitet") som en mekanistisk sterkere kandidat, til tross for dens lavere TxGNN-skår, når litteratursøket er utvidet
- Litteratur-/klinisk studiesøk ved bruk av sykdomsspesifikke termer (nåværende søk returnerte null treff på tvers av alle 10 kandidater, noe som tyder på at søkestrategien kanskje må utvides)

## Ansvarsfraskrivelse

Dette innholdet er kun til forskningsformål og utgjør ikke medisinsk rådgivning.
Klinisk validering kreves før enhver klinisk anvendelse.

---

