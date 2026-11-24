---
layout: default
title: Lopinavir
parent: Kun modellprediksjon (L5)
nav_order: 251
evidence_level: L5
indication_count: 3
monitor_inn: "LOPINAVIR"
predicted_indications: ["simian immunodeficiency virus infection", "feline acquired immunodeficiency syndrome", "neurodevelopmental disorder with ataxic gait, absent speech, and decreased cortical white matter"]
last_modified_at: 2026-11-24
description: "Lopinavir: predikert ny indikasjon simianuvirus-immunsviktinfeksjon (simian immunodeficiency virus infection) (evidensnivå L5). Opprinnelig indikasjon: HIV Infections"
---

# Lopinavir
{: .fs-9 }

Evidensnivå: **L5** | Predikerte indikasjoner: **3** stk.
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

## Lopinavir: HIV-1-proteasehemmer → simianuvirus-immunsviktinfeksjon (simian immunodeficiency virus infection)
{: .text-alpha }

## Oppsummering i én setning

Lopinavir er en HIV-proteasehemmer som brukes mot HIV-infeksjon. TxGNN-modellen forutsier at legemidlet kan ha effekt mot **simianuvirus-immunsviktinfeksjon (simian immunodeficiency virus infection)**, men støtten består kun av **3 prekliniske publikasjoner** på aper og **ingen kliniske studier**. Dette er en dyremodell, ikke en ny human indikasjon.

---

## Hurtigoversikt

| Punkt | Innhold |
|------|------|
| Opprinnelig indikasjon | HIV Infections |
| Foreslått ny indikasjon | simianuvirus-immunsviktinfeksjon (simian immunodeficiency virus infection) |
| TxGNN-prediksjonsscore | 0,9990 |
| Evidensnivå | L5 |
| Markedsstatus i Norge | Markedsført (gyldige tillatelser: 2 av 2) |
| Antall godkjenninger | 2 (gyldige: 2) |
| Anbefalt beslutning | Hold |

---

## Hvorfor er denne prediksjonen rimelig?

Ifølge ChEMBL (EMBL-EBI) er den registrerte virkningsmekanismen for Lopinavir (uoffisiell oversettelse): «Proteasehemmer for humant immunsviktvirus type 1». Engelsk originaltekst: "Human immunodeficiency virus type 1 protease inhibitor" ([ChEMBL CHEMBL729 (lopinavir): drug mechanism](https://www.ebi.ac.uk/chembl/explore/compound/CHEMBL729), CC BY-SA 3.0; hentet 2026-11-19). Lopinavir er kjent som en HIV-1-proteasehemmer. SIV er et nært beslektet lentivirus med en strukturelt lignende protease, så antiviral aktivitet er mekanistisk plausibel.

Den støttende litteraturen er prekliniske studier på makaker. De omfatter blant annet kombinasjonsbehandling med flere antiretrovirale midler og en SHIV-konstruksjon med et HIV-1-avledet proteasegen. Dette er i praksis samme antivirale mekanisme som ved HIV, anvendt i en dyremodell, og ikke en ny human sykdom. Ingen av publikasjonene studerer lopinavir alene mot SIV-infeksjon i en klinisk setting.

---

## Evidensnivå

Ingen av de siterte studiene er kliniske, og de er heller ikke direkte studier av lopinavir som behandling for denne sykdommen hos mennesker. Evidensnivået settes derfor til **L5** (kun modellprediksjon uten tilstrekkelig direkte studier).

---

## Klinisk studiedokumentasjon

Det er for øyeblikket ingen relaterte kliniske studier registrert.

---

## Litteraturevidens

| PMID | År | Type | Tidsskrift | Hovedfunn |
|------|-----|------|------|---------|
| [16973590](https://pubmed.ncbi.nlm.nih.gov/16973590/) | 2006 | Preklinisk dyrestudie | Journal of Virology | Rask viral nedgang hos SIV-infiserte makaker som fikk firedobbel antiretroviral behandling |
| [17350308](https://pubmed.ncbi.nlm.nih.gov/17350308/) | 2007 | Preklinisk dyrestudie | Microbes and Infection | SHIV-konstruksjon med HIV-1-avledet proteasegen i rhesusmakaker, et verktøy for å teste proteasehemmere in vivo |
| [12951220](https://pubmed.ncbi.nlm.nih.gov/12951220/) | 2003 | Preklinisk dyrestudie | Journal of Virological Methods | Oral HAART (AZT, 3TC og lopinavir/ritonavir) hos kronisk SHIV-infiserte aper og effekten på CD8-delmengden |

---

## Informasjon om markedet i Norge

<!-- licenses:begin -->

| Godkjenningsnummer | Preparatnavn (EMA) | Virkestoff(er) (EMA, engelsk) | Terapeutisk område (EMA, engelsk) | Status |
|------|------|------|------|------|
| EMEA/H/C/000368 | Kaletra | lopinavir; ritonavir | HIV Infections | Gyldig |
| EMEA/H/C/004025 | Lopinavir/Ritonavir Viatris (previously Ritonavir Mylan) | lopinavir; ritonavir | HIV Infections | Gyldig |

Kilde: EMA – Medicines output (sentralt godkjente legemidler til mennesker); preparatnavn, virkestoffer og terapeutisk område er gjengitt i engelsk original. Nasjonale markedsføringstillatelser (DMP) og veterinærpreparater er ikke med i disse dataene.

<!-- licenses:end -->

---

## Sikkerhetsvurderinger

Se pakningsvedlegget for sikkerhetsinformasjon.

**Legemiddelinteraksjoner:** Totalt 65 interaksjoner er registrert. Blant dem som er oppført i dataene, er følgende klassifisert som alvorlige (Major):
- Dolasetron
- Papaverin

Mange andre interaksjoner er klassifisert som moderate, blant annet med acarbose, metformin, dapagliflozin, famotidin, levofloksacin, ondansetron og palonosetron, samt flere laksantia.

---

## Konklusjon og neste steg

**Beslutning: Hold**

**Begrunnelse:**
Støtten for denne prediksjonen er kun prekliniske apestudier uten kliniske studier, og indikasjonen er en dyremodell av samme virkemekanisme som ved HIV. Den gir ikke grunnlag for en ny human bruk.

**For å gå videre kreves følgende:**
- Data om virkningsmekanisme (MOA)
- Informasjon fra pakningsvedlegget om advarsler og kontraindikasjoner
- Klargjøring av om prediksjonen har noen relevans utover veterinær- og forskningsbruk

<!-- review:begin log -->

## Kontrollogg

Nedenfor er gjennomgangsloggen for denne siden. Setningen om at data om virkningsmekanismen ikke var tilgjengelige, er erstattet med et utdrag fra den oppgitte offisielle preparatomtalen (med uoffisiell oversettelse); modellprediksjoner, evidensnivåer og konklusjoner er ikke omskrevet.

| Kontrolldato | Punkt | Tiltak | Kilde |
|------|------|------|------|
| 2026-11-19 | Setningen «data om virkningsmekanismen er ikke tilgjengelige» erstattet med utdrag fra amerikansk preparatomtale | Setning om manglende data om virkningsmekanismen erstattet med et utdrag med kilde (revidert 2026-11-20; tidligere versjon er lagret i posten) | [ChEMBL CHEMBL729 (lopinavir): drug mechanism](https://www.ebi.ac.uk/chembl/explore/compound/CHEMBL729) |

<!-- review:end log -->

## Ansvarsfraskrivelse

Dette innholdet er kun til forskningsformål og utgjør ikke medisinsk rådgivning.
Klinisk validering kreves før enhver klinisk anvendelse.

---

