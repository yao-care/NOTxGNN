---
layout: default
title: Methylphenidate
parent: Kun modellprediksjon (L5)
nav_order: 269
evidence_level: L5
indication_count: 4
last_modified_at: 2026-10-28
description: "Methylphenidate: predikert ny indikasjon Faciodigitogenital syndrom (evidensnivå L5). Opprinnelig indikasjon: Oppmerksomhetssvikt med hyperaktivitet (ADHD)"
monitor_inn: "Methylphenidate"
predicted_indications: ["faciodigitogenital syndrome", "chondromyxoid fibroma", "specific developmental disorder", "dysthymic disorder"]
---

# Methylphenidate
{: .fs-9 }

Evidensnivå: **L5** | Predikerte indikasjoner: **4** stk.
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

## Metylfenidat: Fra ADHD til familiær-digito-genital syndrom (faciodigitogenital syndrome)
{: .text-alpha }

## Oppsummering i én setning

Metylfenidat er et sentralstimulerende middel som opprinnelig brukes til behandling av oppmerksomhetssvikt med hyperaktivitet (ADHD).
TxGNN-modellen predikerer at det kan ha effekt ved **faciodigitogenital syndrom** (Aarskog-Scott-syndrom), men det finnes **ingen kliniske studier** og **ingen publikasjoner** som støtter denne retningen. Prediksjonen er kun beregningsbasert.

---

## Hurtigoversikt

| Punkt | Innhold |
|------|------|
| Opprinnelig indikasjon | Oppmerksomhetssvikt med hyperaktivitet (ADHD) |
| Predikert ny indikasjon | Faciodigitogenital syndrom |
| TxGNN-prediksjonsscore | 1,0000 |
| Evidensnivå | L5 |
| Markedsstatus i Norge | Markedsført (gyldige tillatelser: 1 av 1) |
| Antall godkjenninger | 1 (gyldige: 1) |
| Antall tillatelser | 1 (0 gyldige, 1 avregistrert) |
| Anbefalt beslutning | Hold (avvent) |

---

## Hvorfor er denne prediksjonen (ikke) rimelig?

Ifølge avsnittet «Mechanism of Action» i preparatomtalen som er godkjent av amerikanske FDA (Prescribing Information), for Methylphenidate (uoffisiell oversettelse): «Metylfenidathydroklorid er et sentralstimulerende middel (CNS-stimulerende middel). Det er ikke kjent hvordan METADATE CD virker terapeutisk ved behandling av ADHD hos pediatriske pasienter fra 6 år. Metylfenidat blokkerer reopptaket av noradrenalin og dopamin i det presynaptiske nevronet og øker frigjøringen av disse monoaminene til det ekstranevronale rommet.» Engelsk originaltekst: "Methylphenidate hydrochloride is a central nervous system (CNS) stimulant. The mode of therapeutic action of METADATE CD in the treatment of ADHD in pediatric patients 6 years of age and older is not known. Methylphenidate blocks the reuptake of norepinephrine and dopamine into the presynaptic neuron and increases the release of these monoamines into the extraneuronal space." ([DailyMed: Metadate Cd (methylphenidate hydrochloride) prescribing information, Lannett Company, LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=29f06562-6b6a-4ca6-b62e-d08a45fb3dd4), versjon av 2026-10-21; hentet 2026-11-19). Basert på kjent informasjon blokkerer metylfenidat transportørene for dopamin (DAT) og noradrenalin (NET), og dette er grunnlaget for den godkjente bruken ved ADHD.

Faciodigitogenital syndrom er en X-bundet utviklingsforstyrrelse forårsaket av mutasjoner i FGD1-genet. ADHD-lignende atferdstrekk kan forekomme ved syndromet, noe som kan forklare hvorfor modellen knytter det til et ADHD-legemiddel. Dette er imidlertid spekulasjon og ikke bevis for nytte ved selve grunnsykdommen. Ingen mekanistisk kobling støttes av de foreliggende dataene.

Den høye scoren er en ren beregningsmessig prediksjon og bør tolkes med forsiktighet.

---

## Klinisk studiedokumentasjon

Foreløpig er ingen relaterte kliniske studier registrert.

---

## Litteraturdokumentasjon

Foreløpig er ingen relatert litteratur tilgjengelig for denne indikasjonen.

---

## Informasjon om det norske markedet

| Tillatelsesnummer | Produktnavn | Doseringsform | Godkjent indikasjon |
|---------|------|------|-----------|
| EMEA/H/C/005975 | Tuzulby | Ikke oppgitt | Oppmerksomhetssvikt med hyperaktivitet (ADHD) (status: godkjent) |

---

## Sikkerhetsmomenter

Sikkerhetsinformasjon fra preparatomtalen er ikke tilgjengelig i datamaterialet. Følgende er hentet fra kunnskapsgrafen (PrimeKG) og er ikke etikett-tekst:

- **Sykdommer med registrert kontraindikasjon i kunnskapsgrafen**:
  - Kardiovaskulære: hypertensjon, koronarsykdom, hjerteinfarkt, hjerneslag/cerebrovaskulær sykdom, plutselig hjertestans, hjerteledningsforstyrrelser
  - Psykiske: bipolar lidelse, schizofreni-lignende og schizoaffektive lidelser, psykotiske lidelser, alvorlig affektiv lidelse, rusmiddelmisbruk/-avhengighet, anorexia nervosa
  - Nevrologiske: epilepsi
  - Hematologiske: trombocytopeni, leukopeni, anemi, hemoglobinopati
  - Øvrige: glaukom, hypertyreose, Graves sykdom, tyreotoksikose
- **Legemiddelinteraksjoner**: Databasen viser kun farmakologiske målproteiner (NET/SLC6A2 og DAT/SLC6A3), ikke klinisk relevante legemiddelinteraksjoner.

Se preparatomtalen for fullstendig sikkerhetsinformasjon.

---

## Konklusjon og neste steg

**Beslutning: Hold (avvent)**

**Begrunnelse:**
Prediksjonen bygger kun på en beregningsmodell uten kliniske studier eller litteratur, og det finnes ingen støttet mekanistisk kobling. Legemidlet er dessuten markedsført i Norge, med 1 gyldig tillatelse av 1.

**For å gå videre kreves følgende:**
- Data om virkningsmekanisme (MOA) fra DrugBank
- Preparatomtale med advarsler og kontraindikasjoner fra det norske legemiddelregisteret
- Systematisk litteratursøk og vurdering av om nytten kan begrenses til ADHD-lignende symptomer ved syndromet
- Avklaring av markedsstatus i Norge

---

## Andre predikerte indikasjoner (til orientering)

| Sykdom | TxGNN-score | Evidensnivå | Anbefaling |
|------|------|------|------|
| Kondromyksoid fibrom | 0,9999 | L5 | Hold – sannsynligvis falsk positiv, ingen plausibel mekanisme |
| Spesifikk utviklingsforstyrrelse | 0,9999 | L5 | Forskningsspørsmål – i stor grad en gjentakelse av eksisterende ADHD-indikasjon, indirekte evidens |
| Dysthymi (dystymisk lidelse) | 0,9911 | L5 | Forskningsspørsmål – kun indirekte evidens fra ADHD med subsyndromal depresjon |

<!-- review:begin log -->

## Kontrollogg

Nedenfor er gjennomgangsloggen for denne siden. Setningen om at data om virkningsmekanismen ikke var tilgjengelige, er erstattet med et utdrag fra den oppgitte offisielle preparatomtalen (med uoffisiell oversettelse); modellprediksjoner, evidensnivåer og konklusjoner er ikke omskrevet.

| Kontrolldato | Punkt | Tiltak | Kilde |
|------|------|------|------|
| 2026-11-19 | Setningen «data om virkningsmekanismen er ikke tilgjengelige» erstattet med utdrag fra amerikansk preparatomtale | Setning om manglende data om virkningsmekanismen erstattet med et utdrag med kilde | [DailyMed: Metadate Cd (methylphenidate hydrochloride) prescribing information, Lannett Company, LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=29f06562-6b6a-4ca6-b62e-d08a45fb3dd4) |

<!-- review:end log -->

## Ansvarsfraskrivelse

Dette innholdet er kun til forskningsformål og utgjør ikke medisinsk rådgivning.
Klinisk validering kreves før enhver klinisk anvendelse.

---

