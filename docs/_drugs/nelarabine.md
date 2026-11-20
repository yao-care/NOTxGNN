---
layout: default
title: Nelarabine
parent: Kun modellprediksjon (L5)
nav_order: 279
evidence_level: L5
indication_count: 1
last_modified_at: 2026-10-28
monitor_inn: "NELARABINE"
predicted_indications: ["relapsing-remitting multiple sclerosis"]
description: "Nelarabine: predikert ny indikasjon Relapsing-remitting multippel sklerose (relapsing-remitting multiple sclerosis) (evidensnivå L5). Opprinnelig indikasjon: Precursor T-Cell Lymphoblastic Leukemia-L…"
---

# Nelarabine
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

## Nelarabine: Relapsing-remitting multippel sklerose (relapsing-remitting multiple sclerosis)
{: .text-alpha }

## Oppsummering

Nelarabin er et legemiddel som opprinnelig ble godkjent for behandling av prekursor T-celle lymfoblastisk leukemi/lymfom.
TxGNN-modellen predikerer at det kan ha effekt ved **relapsing-remitting multippel sklerose**,
men for øyeblikket finnes **ingen kliniske studier** og **ingen publikasjoner** som støtter denne retningen.
Nelarabin er dessuten kjent for alvorlig nevrotoksisitet, noe som utgjør en betydelig sikkerhetsutfordring ved en demyeliniserende sykdom.

---

## Hurtigoversikt

| Punkt | Innhold |
|------|------|
| Opprinnelig indikasjon | Precursor T-Cell Lymphoblastic Leukemia-Lymphoma |
| Predikert ny indikasjon | Relapsing-remitting multippel sklerose (relapsing-remitting multiple sclerosis) |
| TxGNN-prediksjonsscore | 0.9943 |
| Evidensnivå | L5 |
| Markedsstatus i Norge | Markedsført (gyldige tillatelser: 1 av 1) |
| Antall godkjenninger | 1 (gyldige: 1) |
| Anbefalt beslutning | Hold |

---

## Hvorfor er denne prediksjonen rimelig?

Nelarabin er et prodrug av ara-G, en deoksyguanosin-analog som er særlig toksisk for T-lymfocytter. Virkningen skjer ved opphopning av ara-GTP, som hemmer DNA-syntesen. Ifølge avsnittet «Mechanism of Action» i preparatomtalen som er godkjent av amerikanske FDA (Prescribing Information), for Nelarabine (uoffisiell oversettelse): «Nelarabin er et prodrug av deoksyguanosinanalogen 9-β- D -arabinofuranosylguanin (ara-G), en nukleosidmetabolismehemmer. Nelarabin demetyleres av ADA til ara-G, monofosforyleres av deoksyguanosinkinase og deoksycytidinkinase, og omdannes deretter til det aktive 5’-trifosfatet, ara-GTP.» Engelsk originaltekst: "Nelarabine is a prodrug of the deoxyguanosine analogue 9-β- D -arabinofuranosylguanine (ara-G), a nucleoside metabolic inhibitor. Nelarabine is demethylated by ADA to ara-G, mono-phosphorylated by deoxyguanosine kinase and deoxycytidine kinase, and subsequently converted to the active 5’-triphosphate, ara-GTP." ([DailyMed: Arranon (nelarabine) prescribing information, Sandoz Inc](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=0f9051de-5c4d-4c0f-8c19-e15214498cca), versjon av 2025-03-31; hentet 2026-11-19).

En mulig, men ubekreftet, begrunnelse er at utarming av patogene lymfocyttpopulasjoner kan være relevant ved multippel sklerose. Andre purinanaloger, som kladribin, er godkjent for relapsing MS, og det gir en viss mekanistisk analogi.

Det finnes imidlertid en stor motsetning: nelarabin er velkjent for alvorlig nevrotoksisitet, inkludert demyelinisering, perifer nevropati, Guillain-Barré-lignende syndromer, kramper og søvnighet. Dette er svært problematisk ved en demyeliniserende sykdom. Den mekanistiske koblingen er derfor spekulativ og kan ikke regnes som støttet.

---

## Evidens fra kliniske studier

Foreløpig er det ingen relaterte kliniske studier registrert.

---

## Litteraturevidens

Foreløpig er det ingen relatert litteratur tilgjengelig.

---

## Markedsinformasjon for Norge

| Godkjenningsnummer | Produktnavn | Doseringsform | Godkjent indikasjon |
|---------|------|------|-----------|
| EMEA/H/C/000752 | Atriance (Sandoz Pharmaceuticals d.d.) | – | Prekursor T-celle lymfoblastisk leukemi/lymfom |

Legemidlet er markedsført i Norge, og 1 av 1 markedsføringstillatelse er gyldig.

---

## Cytotoksisitet

| Punkt | Innhold |
|------|------|
| Cytotoksisitetsklassifisering | Konvensjonelt cytotoksisk (purinnukleosidanalog, antimetabolitt) |
| Emetogenisitetsklassifisering | Se pakningsvedlegget for advarsler og forsiktighetsregler |
| Overvåkingspunkter | Blodstatus (CBC med differensialtelling), lever- og nyrefunksjon, samt nevrologisk overvåking |
| Håndteringsbeskyttelse | Må følge gjeldende regler for håndtering av cytotoksiske legemidler |

---

## Sikkerhetsvurderinger

**Kontraindikasjoner fra kunnskapsgrafen (TxGNN/PrimeKG).** Disse er hentet fra relasjoner mellom legemiddel og sykdom i kunnskapsgrafen, ikke fra preparatomtalen:
- Nevrologiske: epilepsi, perifer nevropati, sykdom i det perifere nervesystemet, demyeliniserende sykdom, inflammatorisk demyeliniserende polyradikuloneuropati, lærevansker, intellektuell funksjonsnedsettelse
- Hematologiske: trombocytopeni, nøytropeni, agranulocytose, anemi, makrocytær anemi
- Lever og nyre: leversvikt, hyperbilirubinemi, arvelig hyperbilirubinemi, Gilberts syndrom, nedsatt nyrefunksjon

**Legemiddelinteraksjoner.** Totalt 100 interaksjoner er funnet. Blant de 20 som er listet i dataene:
- **Alvorlige (Major):** bupropion, deferipron, iopamidol, ioheksol, samarium (153Sm) leksidronam
- **Moderate:** pikosulfat, polyetylenglykol (3350 med elektrolytter), natriumsulfat, metronidazol, rosuvastatin, simvastatin, tinidazol, palifermin, strontiumklorid Sr-89, klorokin, disulfiram, secnidazol, benznidazol, hydroksyklorokin, lindan

Advarsler og kontraindikasjoner fra preparatomtalen er ikke tilgjengelige i de innsamlede dataene. Se pakningsvedlegget for fullstendig sikkerhetsinformasjon.

---

## Konklusjon og neste steg

**Beslutning: Hold**

**Begrunnelse:**
Det eneste som støtter prediksjonen er en høy TxGNN-score (evidensnivå L5), uten kliniske studier eller litteratur. I tillegg er nelarabins alvorlige nevrotoksisitet, inkludert demyelinisering, i direkte konflikt med behandling av multippel sklerose. Preparatet er markedsført i Norge, med 1 gyldig markedsføringstillatelse av 1.

**For å gå videre kreves følgende:**
- Hente og analysere preparatomtalens advarsler og kontraindikasjoner (blokkerende datamangel)
- Hente detaljerte data om virkningsmekanisme (MOA), f.eks. fra DrugBank
- Prekliniske data eller studier som viser at nevrotoksisiteten kan håndteres ved MS
- Systematisk litteratursøk og søk etter kliniske studier
- En grundig nytte-risikovurdering mot godkjente alternativer, som kladribin

<!-- review:begin log -->

## Kontrollogg

Nedenfor er gjennomgangsloggen for denne siden. Setningen om at data om virkningsmekanismen ikke var tilgjengelige, er erstattet med et utdrag fra den oppgitte offisielle preparatomtalen (med uoffisiell oversettelse); modellprediksjoner, evidensnivåer og konklusjoner er ikke omskrevet.

| Kontrolldato | Punkt | Tiltak | Kilde |
|------|------|------|------|
| 2026-11-19 | Setningen «data om virkningsmekanismen er ikke tilgjengelige» erstattet med utdrag fra amerikansk preparatomtale | Setning om manglende data om virkningsmekanismen erstattet med et utdrag med kilde | [DailyMed: Arranon (nelarabine) prescribing information, Sandoz Inc](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=0f9051de-5c4d-4c0f-8c19-e15214498cca) |

<!-- review:end log -->

## Ansvarsfraskrivelse

Dette innholdet er kun til forskningsformål og utgjør ikke medisinsk rådgivning.
Klinisk validering kreves før enhver klinisk anvendelse.

---

