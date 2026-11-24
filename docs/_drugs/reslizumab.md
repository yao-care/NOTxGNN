---
layout: default
title: Reslizumab
parent: Kun modellprediksjon (L5)
nav_order: 356
evidence_level: L5
indication_count: 2
last_modified_at: 2026-11-24
description: "Reslizumab: predikert ny indikasjon immunmediert trombocytopeni (evidensnivå L5). Opprinnelig indikasjon: Astma"
monitor_inn: "RESLIZUMAB"
predicted_indications: ["thrombocytopenia due to immune destruction", "primary release disorder of platelets"]
---

# Reslizumab
{: .fs-9 }

Evidensnivå: **L5** | Predikerte indikasjoner: **2** stk.
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

## Reslizumab: Fra astma til immunmediert trombocytopeni
{: .text-alpha }

## Oppsummering i én setning

Reslizumab er et monoklonalt antistoff mot interleukin-5 (IL-5) som opprinnelig ble brukt til behandling av astma.
TxGNN-modellen forutsier at legemidlet kan ha effekt ved **trombocytopeni på grunn av immunmediert destruksjon**,
men det finnes foreløpig **0 kliniske studier** og **0 publikasjoner** som støtter denne retningen. Prediksjonen er ren modellbasert.

---

## Hurtigoversikt

| Punkt | Innhold |
|------|------|
| Opprinnelig indikasjon | Astma |
| Foreslått ny indikasjon | Trombocytopeni på grunn av immunmediert destruksjon |
| TxGNN-prediksjonsscore | 0,9953 |
| Evidensnivå | L5 |
| Markedsstatus i Norge | Markedsført (gyldige tillatelser: 1 av 1) |
| Antall godkjenninger | 1 (gyldige: 1) |
| Anbefalt beslutning | Hold |

---

## Hvorfor er denne prediksjonen rimelig?

Reslizumab er et anti-IL-5-antistoff som reduserer eosinofilenes overlevelse og aktivering. Ifølge avsnittet «Mechanism of Action» i preparatomtalen som er godkjent av amerikanske FDA (Prescribing Information), for Reslizumab (uoffisiell oversettelse): «Reslizumab er en interleukin-5-antagonist (IgG4, kappa). IL-5 er det viktigste cytokinet som er ansvarlig for vekst og differensiering, rekruttering, aktivering og overlevelse av eosinofiler. Reslizumab bindes til IL-5 med en dissosiasjonskonstant på 81 pM, og hemmer bioaktiviteten til IL-5 ved å blokkere bindingen til alfakjeden i IL-5-reseptorkomplekset som uttrykkes på eosinofilenes overflate.» Engelsk originaltekst: "Reslizumab is an interleukin-5 antagonist (IgG4, kappa). IL-5 is the major cytokine responsible for the growth and differentiation, recruitment, activation, and survival of eosinophils. Reslizumab binds to IL-5 with a dissociation constant of 81 pM, inhibiting the bioactivity of IL-5 by blocking its binding to the alpha chain of the IL-5 receptor complex expressed on the eosinophil surface." ([DailyMed: Cinqair (reslizumab) prescribing information, Teva Respiratory, LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=053b9158-2a5b-48b9-bf47-5fa78a35ec33), versjon av 2020-02-29; hentet 2026-11-19).

Det er ikke etablert noen kjent kobling mellom IL-5-blokade og immunmediert trombocytopeni. Et spekulativt resonnement er at enkelte autoimmune cytopenier kan ha en immunregulatorisk komponent med Th2-/eosinofilaktivitet, men dette er ikke støttet av kliniske data eller litteratur. Den høye TxGNN-scoren (0,9953) er kun en beregningsbasert prediksjon.

---

## Kliniske studier

Foreløpig er det ingen relaterte kliniske studier registrert for denne indikasjonen.

---

## Litteraturevidens

Foreløpig er det ingen relatert litteratur tilgjengelig for denne indikasjonen.

---

## Markedsinformasjon for Norge

<!-- licenses:begin -->

| Godkjenningsnummer | Preparatnavn (EMA) | Virkestoff(er) (EMA, engelsk) | Terapeutisk område (EMA, engelsk) | Status |
|------|------|------|------|------|
| EMEA/H/C/003912 | Cinqaero | reslizumab | Asthma | Gyldig |

Kilde: EMA – Medicines output (sentralt godkjente legemidler til mennesker); preparatnavn, virkestoffer og terapeutisk område er gjengitt i engelsk original. Nasjonale markedsføringstillatelser (DMP) og veterinærpreparater er ikke med i disse dataene.

<!-- licenses:end -->

Merk: Legemidlet er markedsført, og 1 av 1 markedsføringstillatelser er gyldig.

---

## Sikkerhetsvurderinger

Se pakningsvedlegget for sikkerhetsinformasjon.

---

## Konklusjon og neste steg

**Beslutning: Hold**

**Begrunnelse:**
Prediksjonen bygger kun på en beregningsmodell uten støtte fra kliniske studier eller litteratur, og det er ikke etablert noen mekanistisk kobling mellom IL-5-blokade og immunmediert trombocytopeni.

<!-- review:begin no-lic-20261106-reslizumab-1 -->

> **Kontrollrettelse (2026-11-06)**: Opprinnelig sto det: «Prediksjonen bygger kun på en beregningsmodell uten støtte fra kliniske studier eller litteratur, og det er ikke etablert noen mekanistisk kobling mellom IL-5-blokade og immunmediert trombocytopeni. I tillegg er legemidlets eneste godkjenning avregistrert.» Fjernet: opplysningen om at godkjenningene er avregistrert eller at ingen gyldig godkjenning finnes, stemte ikke med EMAs data om sentrale EU-godkjenninger (2026-11-06). Oppdaterte antall og statuser for godkjenningene står i hurtigoversikten og i lisenstabellen under markedsinformasjonen. Kilde: [EMA – Medicines output: medicines report](https://www.ema.europa.eu/en/documents/report/medicines-output-medicines-report_en.xlsx); [European Medicines Agency](https://www.ema.europa.eu/).

<!-- review:end no-lic-20261106-reslizumab-1 -->

**For å gå videre kreves følgende:**
- Data om virkningsmekanisme (MOA) for å vurdere den mekanistiske koblingen
- Sikkerhetsinformasjon fra pakningsvedlegget (advarsler og kontraindikasjoner), som er en forutsetning for sikkerhetsscreening
- Prekliniske eller kliniske data som belyser IL-5/eosinofiler ved immunmediert trombocytopeni
- Avklaring av legemidlets regulatoriske status og tilgjengelighet i Norge

---

## Tilleggsprediksjon: Primær frigjøringsforstyrrelse av blodplater

TxGNN rangerer også **primær frigjøringsforstyrrelse av blodplater** (score 0,9925, evidensnivå L5, beslutning **Hold**). Den eneste tilgjengelige referansen er en oversiktsartikkel om hypereosinofilt syndrom, inkludert mepolizumab:

| PMID | År | Type | Tidsskrift | Hovedfunn |
|------|-----|------|------|---------|
| [20565230](https://pubmed.ncbi.nlm.nih.gov/20565230/) | 2010 | Oversikt | Current Medical Research and Opinion | Behandling av hypereosinofilt syndrom, inkludert anti-IL-5-antistoffet mepolizumab. Gjelder eosinofil sykdom, ikke blodplatefunksjon |

Artikkelen støtter legemiddelklassens aktivitet ved eosinofilstyrte tilstander, men ikke denne indikasjonen. Det finnes ingen kliniske studier.

<!-- review:begin log -->

## Kontrollogg

Nedenfor er kontrolloggen for denne siden: opplysninger kontrollert mot EMAs data om sentrale EU-godkjenninger. Rettelser gjelder bare grunnleggende faktaopplysninger; modellens prediksjoner, evidensnivåer og konklusjoner er ikke skrevet om. Setningen om at data om virkningsmekanismen ikke var tilgjengelige, er erstattet med et utdrag fra den oppgitte offisielle preparatomtalen (med uoffisiell oversettelse).

| Kontrolldato | Punkt | Tiltak | Kilde |
|------|------|------|------|
| 2026-11-06 | Fjernet: «I tillegg er legemidlets eneste godkjenning avregistrert» | Rettet (revidert 2026-11-24; tidligere versjon er lagret i posten) | [EMA – Medicines output: medicines report](https://www.ema.europa.eu/en/documents/report/medicines-output-medicines-report_en.xlsx); [European Medicines Agency](https://www.ema.europa.eu/) |
| 2026-11-19 | Setningen «data om virkningsmekanismen er ikke tilgjengelige» erstattet med utdrag fra amerikansk preparatomtale | Setning om manglende data om virkningsmekanismen erstattet med et utdrag med kilde | [DailyMed: Cinqair (reslizumab) prescribing information, Teva Respiratory, LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=053b9158-2a5b-48b9-bf47-5fa78a35ec33) |

<!-- review:end log -->

## Ansvarsfraskrivelse

Dette innholdet er kun til forskningsformål og utgjør ikke medisinsk rådgivning.
Klinisk validering kreves før enhver klinisk anvendelse.

---

