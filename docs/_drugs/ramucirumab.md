---
layout: default
title: Ramucirumab
parent: Kun modellprediksjon (L5)
nav_order: 345
evidence_level: L5
indication_count: 10
last_modified_at: 2026-11-24
monitor_inn: "RAMUCIRUMAB"
predicted_indications: ["uterine ligament adenocarcinoma", "endocervical carcinoma", "adenoid cystic carcinoma of the cervix uteri", "uterine ligament serous adenocarcinoma", "signet ring cell variant cervical mucinous adenocarcinoma", "cervical adenosquamous carcinoma, glassy cell variant", "uterine ligament endometrioid adenocarcinoma", "uterine ligament clear cell adenocarcinoma", "uterine ligament mucinous adenocarcinoma", "intestinal variant cervical mucinous adenocarcinoma"]
description: "Ramucirumab: predikert ny indikasjon Adenokarsinom i livmorligamentet (uterine ligament adenocarcinoma) (evidensnivå L5). Opprinnelig indikasjon: Stomach Neoplasms"
---

# Ramucirumab
{: .fs-9 }

Evidensnivå: **L5** | Predikerte indikasjoner: **10** stk.
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

## Ramucirumab: Adenokarsinom i livmorligamentet (uterine ligament adenocarcinoma)
{: .text-alpha }

## Oppsummering i én setning

Ramucirumab er et legemiddel som opprinnelig brukes til behandling av magekreft (ventrikkelkreft).
TxGNN-modellen forutsier at det kan ha effekt mot **adenokarsinom i livmorligamentet** (uterine ligament adenocarcinoma),
men for øyeblikket finnes **ingen registrerte kliniske studier og ingen publikasjoner** i de innsamlede dataene som støtter denne retningen.

## Hurtigoversikt

| Punkt | Innhold |
|------|------|
| Opprinnelig indikasjon | Stomach Neoplasms |
| Predikert ny indikasjon | Adenokarsinom i livmorligamentet (uterine ligament adenocarcinoma) |
| TxGNN-prediksjonsscore | 0.9995 |
| Evidensnivå | L5 |
| Markedsstatus i Norge | Markedsført (gyldige tillatelser: 1 av 1) |
| Antall godkjenninger | 1 (gyldige: 1) |
| Anbefalt beslutning | Hold |

## Hvorfor er denne prediksjonen rimelig?

Ifølge avsnittet «Mechanism of Action» i preparatomtalen som er godkjent av amerikanske FDA (Prescribing Information), for Ramucirumab (uoffisiell oversettelse): «Ramucirumab er en VEGFR2-antagonist som binder seg spesifikt til VEGFR2 og blokkerer binding av VEGFR-ligandene VEGF-A, VEGF-C og VEGF-D. Som et resultat hemmer ramucirumab ligandstimulert aktivering av VEGFR2, og hemmer dermed ligandindusert proliferasjon og migrasjon av humane endotelceller. Ramucirumab hemmet angiogenese i en in vivo-dyremodell.» Engelsk originaltekst: "Ramucirumab is a VEGFR2 antagonist that specifically binds VEGFR2 and blocks binding of VEGFR ligands, VEGF-A, VEGF-C, and VEGF-D. As a result, ramucirumab inhibits ligand-stimulated activation of VEGFR2, thereby inhibiting ligand-induced proliferation, and migration of human endothelial cells. Ramucirumab inhibited angiogenesis in an in vivo animal model." ([DailyMed: Cyramza (ramucirumab) prescribing information, Eli Lilly and Company](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=c6080942-dee6-423e-b688-1272c2ae90d4), versjon av 2026-06-09; hentet 2026-11-19). Basert på generell kunnskap er ramucirumab en VEGFR-2-antagonist (hemmer av vaskulær endotelial vekstfaktorreseptor 2). Effekten ved magekreft er etablert, og mekanistisk kan angiogenesehemming være aktuelt også for adenokarsinomer i kvinnelige kjønnsorganer.

Kreftformene har til felles at de er adenokarsinomer der tumorvekst kan avhenge av nydannelse av blodkar. Dette gir en biologisk plausibel, men uverifisert kobling. Høy TxGNN-score kan delvis gjenspeile nærhet i sykdomsontologien til andre karsinomer i livmorhals og kjønnsorganer, snarere enn sykdomsspesifikk evidens.

Andre høyt rangerte prediksjoner er blant annet endocervikalt karsinom (0.9995), adenoid cystisk karsinom i livmorhalsen (0.9995) og flere histologiske varianter av livmorhals- og livmorligamentkreft. For endocervikalt karsinom er VEGF-rettet behandling (bevacizumab) kjent å ha aktivitet ved livmorhalskreft, noe som styrker den biologiske plausibiliteten. Noen mucinøse og «signet ring»-varianter har en løs histologisk likhet med mage-adenokarsinom. Heller ikke for disse finnes studier eller litteratur i dataene.

## Klinisk studieevidens

Foreløpig finnes ingen relaterte kliniske studier registrert.

## Litteraturevidens

Foreløpig er ingen relatert litteratur tilgjengelig.

## Informasjon om det norske markedet

<!-- licenses:begin -->

| Godkjenningsnummer | Preparatnavn (EMA) | Virkestoff(er) (EMA, engelsk) | Terapeutisk område (EMA, engelsk) | Status |
|------|------|------|------|------|
| EMEA/H/C/002829 | Cyramza | ramucirumab | Stomach Neoplasms | Gyldig |

Kilde: EMA – Medicines output (sentralt godkjente legemidler til mennesker); preparatnavn, virkestoffer og terapeutisk område er gjengitt i engelsk original. Nasjonale markedsføringstillatelser (DMP) og veterinærpreparater er ikke med i disse dataene.

<!-- licenses:end -->

Godkjenningen er registrert som kansellert (produsent: Eli Lilly Nederland B.V.).

## Cytotoksisitet

| Punkt | Innhold |
|------|------|
| Klassifisering | Målrettet behandling (monoklonalt antistoff mot VEGFR-2), ikke konvensjonelt cytotoksisk |
| Risiko for myelosuppresjon | Se preparatomtalen for advarsler og forsiktighetsregler |
| Emetogenisitet | Se preparatomtalen for advarsler og forsiktighetsregler |
| Overvåkingspunkter | Se preparatomtalen for advarsler og forsiktighetsregler |
| Håndteringsvern | Se preparatomtalen for advarsler og forsiktighetsregler |

## Sikkerhetsvurderinger

- **Legemiddelinteraksjoner:** Totalt 100 interaksjoner er registrert i de innsamlede dataene. Av de 20 som er vist, er de fleste klassifisert som **alvorlige (Major)**, hovedsakelig knyttet til økt blødningsrisiko ved samtidig bruk av stoffer som påvirker blodstørrelse og blodplatefunksjon:
  - Blodplatehemmere: acetylsalisylsyre, klopidogrel, cilostazol, abciksimab, kangrelor
  - Antikoagulantia og trombolytika: apiksaban, betriksaban, dalteparin, bivalirudin, alteplase, antitrombin III, defibrotid, kaplacizumab
  - Andre alvorlige: deferasiroks, ibritumomab tiuxetan, tositumomab (inkl. I-131)
  - Moderate: deksfenfluramin, fenfluramin, sibutramin

For øvrig sikkerhetsinformasjon, se preparatomtalen.

## Konklusjon og neste steg

**Beslutning: Hold**

**Begrunnelse:**
Prediksjonen bygger kun på TxGNN-score (evidensnivå L5), uten kliniske studier eller litteratur. Markedsgodkjenningen i Norge er kansellert, og mekanismedata og preparatomtale mangler.

**For å gå videre kreves følgende:**
- Hente og analysere preparatomtalens advarsler og kontraindikasjoner (blokkerende datamangel for sikkerhetsvurdering)
- Supplere data om virkningsmekanisme (MOA) fra DrugBank
- Gjennomføre litteratur- og studiesøk spesifikt for ramucirumab ved gynekologiske adenokarsinomer
- Avklare årsaken til at godkjenningen i Norge er kansellert og om tilgang er mulig
- Vurdere prekliniske data eller en tidlig klinisk studie dersom prediksjonen skal følges opp

<!-- review:begin log -->

## Kontrollogg

Nedenfor er gjennomgangsloggen for denne siden. Setningen om at data om virkningsmekanismen ikke var tilgjengelige, er erstattet med et utdrag fra den oppgitte offisielle preparatomtalen (med uoffisiell oversettelse); modellprediksjoner, evidensnivåer og konklusjoner er ikke omskrevet.

| Kontrolldato | Punkt | Tiltak | Kilde |
|------|------|------|------|
| 2026-11-19 | Setningen «data om virkningsmekanismen er ikke tilgjengelige» erstattet med utdrag fra amerikansk preparatomtale | Setning om manglende data om virkningsmekanismen erstattet med et utdrag med kilde | [DailyMed: Cyramza (ramucirumab) prescribing information, Eli Lilly and Company](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=c6080942-dee6-423e-b688-1272c2ae90d4) |

<!-- review:end log -->

## Ansvarsfraskrivelse

Dette innholdet er kun til forskningsformål og utgjør ikke medisinsk rådgivning.
Klinisk validering kreves før enhver klinisk anvendelse.

---

