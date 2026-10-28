---
layout: default
title: Fenofibrate
parent: Kun modellprediksjon (L5)
nav_order: 173
evidence_level: L5
indication_count: 1
monitor_inn: "FENOFIBRATE"
predicted_indications: ["cholesterol-ester transfer protein deficiency"]
last_modified_at: 2026-10-23
description: "Fenofibrate: predikert ny indikasjon Kolesterolester-transferprotein-mangel (evidensnivå L5). Opprinnelig indikasjon: Dyslipidemi"
---

# Fenofibrate
{: .fs-9 }

Evidensnivå: **L5** | Predikerte indikasjoner: **1** stk.
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

## Fenofibrat: Fra dyslipidemi til kolesterolester-transferprotein-mangel
{: .text-alpha }

## Sammendrag i én setning

Fenofibrat brukes opprinnelig til behandling av dyslipidemi. TxGNN-modellen predikerer at det kan være effektivt ved **kolesterolester-transferprotein-mangel (CETP-mangel)**, men støtten er svak: det finnes **ingen registrerte kliniske studier** og bare **3 publikasjoner**, som alle er prekliniske eller mekanistiske og ikke undersøker sykdommen direkte.

## Hurtigoversikt

| Punkt | Innhold |
|------|------|
| Opprinnelig indikasjon | Dyslipidemi |
| Predikert ny indikasjon | Kolesterolester-transferprotein-mangel |
| TxGNN-prediksjonsscore | 0,9961 |
| Evidensnivå | L5 |
| Markedsstatus i Norge | Markedsført (gyldige tillatelser: 2 av 2) |
| Antall godkjenninger | 2 (gyldige: 2) |
| Anbefalt beslutning | Hold |

## Hvorfor er denne prediksjonen rimelig?

Data om virkningsmekanisme er ikke tilgjengelig i de innsamlede dataene. Fenofibrat er imidlertid kjent som en PPARα-agonist som øker HDL-kolesterol og senker triglyserider. Dette skjer blant annet via økt lipoproteinlipase og apolipoprotein A-I/A-II, og via påvirkning av lipidtransferproteiner.

Den tilgjengelige litteraturen peker på en indirekte kobling. I transgene mus ga kombinasjonen av PPARα-agonisme og CETP-hemming økt HDL-C og lavere LDL-C (PMID 20332533). Induksjon av genet for fosfolipidtransferprotein (PLTP) forklarer HDL-økningen under fibratbehandling (PMID 11342537). Disse funnene beskriver modulering av HDL- og lipidtransportveien, men viser ikke at fenofibrat behandler CETP-mangel.

CETP-mangel er en genetisk tilstand med markant forhøyet HDL-C. Ytterligere HDL-økning er ikke et åpenbart behandlingsmål, så den kliniske begrunnelsen for indikasjonen er uklar. Den høye TxGNN-scoren er en beregningsmessig prediksjon og må ikke leses som klinisk evidens.

## Kliniske studier

Foreløpig er det ingen relaterte kliniske studier registrert.

## Litteraturevidens

| PMID | År | Type | Tidsskrift | Hovedfunn |
|------|-----|------|------|---------|
| [20332533](https://pubmed.ncbi.nlm.nih.gov/20332533/) | 2010 | Preklinisk/mekanistisk | J Cardiovasc Pharmacol Ther | CETP-hemming kombinert med PPARα-agonisme (fenofibrat) økte HDL-C og reduserte LDL-C i transgene mus |
| [11342537](https://pubmed.ncbi.nlm.nih.gov/11342537/) | 2001 | Mekanistisk | J Biol Chem | Induksjon av PLTP-genet forklarer HDL-forstørrelse hos mus behandlet med fenofibrat |
| [30271349](https://pubmed.ncbi.nlm.nih.gov/30271349/) | 2018 | Mekanistisk/translasjonell | Front Physiol | Manglende korrelasjon mellom plasma-HDL og fekal kolesterolutskillelse og kolesterol-efflukskapasitet; understreker HDL-funksjon |

Ingen av publikasjonene undersøker CETP-mangel hos mennesker, og ingen studerer fenofibrat som behandling av denne sykdommen.

## Informasjon om det norske markedet

| Godkjenningsnummer | Produktnavn | Doseringsform | Godkjent indikasjon |
|---------|------|------|-----------|
| EMEA/H/C/002559 | Cholib | – | Dyslipidemi |
| EMEA/H/C/001243 | Pravafenix | – | Dyslipidemi |

## Sikkerhetsvurderinger

Se preparatomtalen for sikkerhetsinformasjon om advarsler og kontraindikasjoner.

- **Relasjoner registrert i kunnskapsgrafen (ikke merketekst):** Kunnskapsgrafen (PrimeKG) har kontraindikasjonsrelasjoner til blant annet leversvikt, leversykdom, pankreatitt, gallesteinssykdom (kolelitiasis), myopati, rabdomyolyse, nedsatt nyrefunksjon, trombocytopeni, anemi, leukopeni og nøytropeni.
- **Legemiddelinteraksjoner:** 100 interaksjoner er registrert. De viste har moderat alvorlighetsgrad og omfatter blant annet:
  - sulfonylurea-antidiabetika (acetoheksamid, klorpropamid, glimepirid, glipizid, glibenklamid)
  - ulike insulinpreparater (humant insulin, insulin aspart, degludek, detemir, glargin, glulisin, lispro)
  - kenodeoksykolsyre
  - esomeprazol

## Konklusjon og neste steg

**Beslutning: Hold**

**Begrunnelse:**
Ingen studier undersøker CETP-mangel direkte, så evidensnivået er L5 (kun modellprediksjon). Den kliniske begrunnelsen er uklar, siden CETP-mangel allerede gir høyt HDL-C. Den høye TxGNN-scoren er ikke tilstrekkelig til å gå videre.

**For å gå videre kreves følgende:**
- Data om virkningsmekanisme fra DrugBank
- Preparatomtale med advarsler og kontraindikasjoner fra det norske legemiddelregisteret
- Klinisk eller translasjonell dokumentasjon som viser at fenofibrat gir terapeutisk nytte ved CETP-mangel, med en klar klinisk begrunnelse for behandlingsmålet
- Vurdering av administrasjonsvei og doseringsform (opplysninger mangler i dag)
## Ansvarsfraskrivelse

Dette innholdet er kun til forskningsformål og utgjør ikke medisinsk rådgivning.
Klinisk validering kreves før enhver klinisk anvendelse.

---

