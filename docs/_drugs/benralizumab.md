---
layout: default
title: Benralizumab
parent: Kun modellprediksjon (L5)
nav_order: 56
evidence_level: L5
indication_count: 5
monitor_inn: "BENRALIZUMAB"
predicted_indications: ["thrombocytopenia due to immune destruction", "dermatitis", "acne keloid", "neonatal dermatomyositis", "amyopathic dermatomyositis"]
last_modified_at: 2026-10-30
description: "Benralizumab: predikert ny indikasjon Trombocytopeni som skyldes immunologisk destruksjon (thrombocytopenia due to immune destruction) (evidensnivå L5). Opprinnelig indikasjon: Asthma"
---

# Benralizumab
{: .fs-9 }

Evidensnivå: **L5** | Predikerte indikasjoner: **5** stk.
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

## Benralizumab: IL-5Rα-hemmer (monoklonalt antistoff) → Trombocytopeni som skyldes immunologisk destruksjon (thrombocytopenia due to immune destruction)
{: .text-alpha }

## Oppsummering i én setning

Benralizumab er et monoklonalt antistoff som blokkerer IL-5-reseptor alfa og tømmer eosinofile og basofile celler.
TxGNN-modellen predikerer at det kan ha effekt ved **trombocytopeni som skyldes immunologisk destruksjon (thrombocytopenia due to immune destruction)**, men det finnes **ingen kliniske studier og ingen publikasjoner** som støtter denne retningen. Prediksjonen er rent beregningsbasert.

## Hurtigoversikt

| Punkt | Innhold |
|------|------|
| Opprinnelig indikasjon | Asthma |
| Predikert ny indikasjon | Trombocytopeni som skyldes immunologisk destruksjon (thrombocytopenia due to immune destruction) |
| TxGNN-prediksjonsscore | 0,9934 |
| Evidensnivå | L5 |
| Markedsstatus i Norge | Markedsført (gyldige tillatelser: 1 av 1) |
| Antall godkjenninger | 1 (gyldige: 1) |
| Anbefalt beslutning | Hold |

## Hvorfor er denne prediksjonen rimelig?

Ifølge avsnittet «Mechanism of Action» i preparatomtalen som er godkjent av amerikanske FDA (Prescribing Information), for Benralizumab (uoffisiell oversettelse): «Benralizumab er et humanisert, afukosylert, monoklonalt antistoff (IgG1, kappa) som bindes direkte til alfa-subenheten av human interleukin-5-reseptor (IL-5Rα) med en dissosiasjonskonstant på 11 pM. IL-5-reseptoren uttrykkes på overflaten av eosinofiler og basofiler.» Engelsk originaltekst: "Benralizumab is a humanized afucosylated, monoclonal antibody (IgG1, kappa) that directly binds to the alpha subunit of the human interleukin-5 receptor (IL-5Rα) with a dissociation constant of 11 pM. The IL-5 receptor is expressed on the surface of eosinophils and basophils." ([DailyMed: Fasenra (benralizumab) prescribing information, AstraZeneca Pharmaceuticals LP](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=da6aca1a-19ed-44a4-abb7-696c7d58b784), versjon av 2026-05-13; hentet 2026-11-19). Ut fra kjent informasjon bindes benralizumab til IL-5-reseptorens alfa-underenhet (IL5RA) og gir tømming av eosinofile og basofile celler via forsterket antistoffavhengig cellemediert cytotoksisitet (ADCC).

Immun trombocytopeni drives hovedsakelig av autoantistoffer og T-celle-dysregulering. En direkte kobling til eosinofil tømming er derfor ikke etablert. En rolle ved sekundære immuncytopenier forbundet med eosinofili er spekulativ.

Den høye scoren (0,9934) er en beregningsmessig prediksjon og bør ikke tolkes som klinisk dokumentasjon.

## Evidens fra kliniske studier

Det er for tiden ingen relaterte kliniske studier registrert.

## Litteraturevidens

Det er for tiden ingen relatert litteratur tilgjengelig.

## Informasjon om det norske markedet

| Godkjenningsnummer | Produktnavn | Doseringsform | Godkjent indikasjon |
|---------|------|------|-----------|
| EMEA/H/C/004433 | Fasenra | – | Se lokale lisensdata |

## Sikkerhetsvurderinger

- **Legemiddelinteraksjoner:** Det er ikke registrert noen klassiske legemiddelinteraksjoner. Den eneste oppføringen gjelder målmolekylet, IL-5-reseptor alfa-underenheten (IL5RA), som er benralizumabs farmakologiske mål.

Se preparatomtalen for øvrig sikkerhetsinformasjon.

## Konklusjon og neste steg

**Beslutning: Hold**

**Begrunnelse:**
Prediksjonen bygger kun på modellberegning. Det finnes ingen kliniske studier eller publikasjoner for denne sykdommen, og den mekanistiske koblingen mellom eosinofil tømming og autoimmun trombocytopeni er svak. Evidensnivået er L5.

**For å gå videre trengs følgende:**
- Prekliniske eller mekanistiske data som viser en rolle for eosinofiler eller IL-5-signalering ved immun trombocytopeni
- Data om virkningsmekanisme fra legemiddeldatabaser
- Gjennomgang av preparatomtalens advarsler og kontraindikasjoner
- Eventuelt en liten eksplorativ studie i pasienter med eosinofiliassosiert immuncytopeni

<!-- review:begin log -->

## Kontrollogg

Nedenfor er gjennomgangsloggen for denne siden. Setningen om at data om virkningsmekanismen ikke var tilgjengelige, er erstattet med et utdrag fra den oppgitte offisielle preparatomtalen (med uoffisiell oversettelse); modellprediksjoner, evidensnivåer og konklusjoner er ikke omskrevet.

| Kontrolldato | Punkt | Tiltak | Kilde |
|------|------|------|------|
| 2026-11-19 | Setningen «data om virkningsmekanismen er ikke tilgjengelige» erstattet med utdrag fra amerikansk preparatomtale | Setning om manglende data om virkningsmekanismen erstattet med et utdrag med kilde | [DailyMed: Fasenra (benralizumab) prescribing information, AstraZeneca Pharmaceuticals LP](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=da6aca1a-19ed-44a4-abb7-696c7d58b784) |

<!-- review:end log -->

## Ansvarsfraskrivelse

Dette innholdet er kun til forskningsformål og utgjør ikke medisinsk rådgivning.
Klinisk validering kreves før enhver klinisk anvendelse.

---

