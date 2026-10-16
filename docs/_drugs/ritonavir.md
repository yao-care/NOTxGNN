---
layout: default
title: Ritonavir
parent: Moderat evidens (L3-L4)
nav_order: 364
evidence_level: L4
indication_count: 3
last_modified_at: 2026-10-15
description: "Ritonavir: predikert ny indikasjon Simian immunsviktvirus-infeksjon (evidensnivå L4). Opprinnelig indikasjon: HIV-infeksjon"
monitor_inn: "RITONAVIR"
predicted_indications: ["feline acquired immunodeficiency syndrome", "simian immunodeficiency virus infection", "neurodevelopmental disorder with ataxic gait, absent speech, and decreased cortical white matter"]
---

# Ritonavir
{: .fs-9 }

Evidensnivå: **L4** | Predikerte indikasjoner: **3** stk.
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

# Ritonavir: Fra HIV-infeksjon til simian immunsviktvirus-infeksjon

## Oppsummering i én setning

Ritonavir er en HIV-proteasehemmer som også brukes som farmakokinetisk forsterker (CYP3A4-hemmer), og som opprinnelig er godkjent for behandling av HIV-infeksjon og COVID-19 (som del av Paxlovid).
TxGNN-modellen forutsier at legemidlet kan være effektivt mot **simian immunsviktvirus-infeksjon (SIV)**.
Støtten er begrenset til **11 publikasjoner** (hovedsakelig dyre- og in vitro-studier) og **ingen kliniske studier**, og dette er i praksis en gjentakelse av den eksisterende HIV-indikasjonen.

---

## Hurtigoversikt

| Punkt | Innhold |
|------|------|
| Opprinnelig indikasjon | HIV-infeksjon |
| Predikert ny indikasjon | Simian immunsviktvirus-infeksjon |
| TxGNN-prediksjonsscore | 99,92 % |
| Evidensnivå | L4 |
| Markedsstatus i Norge | Kun opphevede (kansellerte) godkjenninger |
| Antall godkjenninger | 5 (alle kansellert) |
| Anbefalt beslutning | Hold |

Merk: Godkjenningsnumrene i dataene er EMA-numre (EMEA/H/C/...), og alle fem er kansellert. Det finnes ingen gyldige godkjenninger i de samlede dataene.

---

## Hvorfor er denne prediksjonen rimelig?

Detaljerte data om virkningsmekanisme er foreløpig ikke tilgjengelige i de innsamlede dataene. Ut fra kjent informasjon er ritonavir en HIV-1-proteasehemmer og en CYP3A4-hemmer som brukes til farmakokinetisk forsterkning av andre legemidler. Effekten mot HIV er etablert, og mekanistisk kan den være overførbar til nært beslektede lentivirus.

SIV er et primat-lentivirus som er nært beslektet med HIV, og proteasen er følsom for enkelte HIV-1-proteasehemmere. Et in vitro-studie (PMID 12709355) viste at SIVmac239 ble hemmet av ritonavir med en EC50 på ca. 13 nM, mot ca. 25 nM for HIV-1. Det gir et direkte, om enn prekliniskt, holdepunkt for aktivitet.

Det er viktig å understreke at SIV er en dyremodell for HIV. Evidensen støtter derfor preklinisk relevans, ikke en ny terapeutisk indikasjon hos mennesker. Den høye TxGNN-scoren gjenspeiler sannsynligvis nærhet til HIV-relaterte noder i nettverket, ikke direkte evidens.

**Andre predikerte indikasjoner (lavere prioritet):**
- **Felin ervervet immunsviktsyndrom (FIV):** Mekanistisk plausibelt, men FIV-protease har annen substrat- og hemmerspesifisitet, og HIV-1-proteasehemmere har vanligvis redusert aktivitet. Ingen studier er funnet (evidensnivå L5).
- **Nevroutviklingsforstyrrelse med ataksisk gange, fraværende tale og redusert kortikal hvit substans:** Ingen plausibel mekanistisk kobling. Scoren er sannsynligvis kunstig oppblåst (evidensnivå L5).

---

## Evidens fra kliniske studier

Foreløpig er det ikke registrert noen relaterte kliniske studier.

---

## Litteraturevidens

| PMID | År | Type | Tidsskrift | Hovedfunn |
|------|-----|------|------|---------|
| [12709355](https://pubmed.ncbi.nlm.nih.gov/12709355/) | 2003 | In vitro | Antimicrob Agents Chemother | SIVmac239 hemmet av indinavir, saquinavir og ritonavir (ritonavir EC50 ca. 13 nM mot 25 nM for HIV-1) |
| [15040537](https://pubmed.ncbi.nlm.nih.gov/15040537/) | 2004 | In vitro | Antivir Ther | Følsomhet hos HIV-2, SIV og SHIV for 16 godkjente anti-HIV-legemidler, med relevans for behandling og postekspositusprofylakse |
| [12951220](https://pubmed.ncbi.nlm.nih.gov/12951220/) | 2003 | Dyrestudie (makak) | J Virol Methods | Oral HAART inkl. lopinavir/ritonavir hos SHIV-infiserte makaker, effekt på CD8-undergruppen |
| [22737073](https://pubmed.ncbi.nlm.nih.gov/22737073/) | 2012 | Dyrestudie (makak) | PLoS Pathog | Sterkt intensivert ART ga langvarig viral suppresjon og begrenset viralt reservoar i SIV-modell |
| [16973590](https://pubmed.ncbi.nlm.nih.gov/16973590/) | 2006 | Dyrestudie (makak) | J Virol | Rask viral nedgang hos SIV-infiserte makaker på firedobbel antiretroviral behandling |
| [25033210](https://pubmed.ncbi.nlm.nih.gov/25033210/) | 2014 | Dyrestudie (makak) | PLoS One | Kombinasjons-ART og HDAC-hemmeren SAHA hos SIV-infiserte rhesusaper |
| [34903055](https://pubmed.ncbi.nlm.nih.gov/34903055/) | 2021 | Oversikt/dyrestudie | mBio | Lentivirusinfeksjon vedvarer i hjernen til tross for effektiv ART |
| [17350308](https://pubmed.ncbi.nlm.nih.gov/17350308/) | 2007 | Modellutvikling | Microbes Infect | Nytt SHIV med HIV-1-protease som verktøy for in vivo-testing av proteasehemmere |

Merk: De fleste dyrestudiene bruker kombinasjonsregimer, og ritonavirs egen bidrag er ikke isolert. Noen innhentede artikler er utenfor tema og er utelatt (PMID 11364629, 9875393, 12186895).

---

## Markedsinformasjon for Norge

| Godkjenningsnummer | Produktnavn | Doseringsform | Godkjent indikasjon |
|---------|------|------|-----------|
| EMEA/H/C/004549 | Ritonavir Viatris (tidligere Ritonavir Mylan) | – | HIV-infeksjon |
| EMEA/H/C/000127 | Norvir | – | HIV-infeksjon |
| EMEA/H/C/000368 | Kaletra | – | HIV-infeksjon |
| EMEA/H/C/004025 | Lopinavir/Ritonavir Viatris (tidligere Ritonavir Mylan) | – | HIV-infeksjon |
| EMEA/H/C/005973 | Paxlovid | – | COVID-19-infeksjon |

Alle fem godkjenninger har status kansellert.

---

## Sikkerhetsvurderinger

Se preparatomtalen for sikkerhetsinformasjon. Data om advarsler og kontraindikasjoner fra preparatomtale er ikke tilgjengelige i de innsamlede dataene.

**Sykdommer med kontraindikasjonskobling i kunnskapsgrafen (PrimeKG, ikke preparattekst):**
- Hjerterytme og hjerte: langt QT-syndrom (inkl. familiært), torsades de pointes, plutselig hjertestans, ledningsforstyrrelser, atrioventrikulært blokk, kardiomyopati (inkl. hypertrofisk), iskemisk hjertesykdom/koronarsykdom, endomyokardfibrose
- Lever og galle: leversykdom, skrumplever, gallblæresykdom, hyperbilirubinemi (inkl. Gilberts syndrom), kronisk hepatitt B
- Stoffskifte: diabetes, hyperglykemi, diabetisk ketoacidose, hypertriglyseridemi, familiær kombinert hyperlipidemi, kaliummangel, urinsyregikt/hyperurikemi
- Annet: pankreatitt, hemofili

**Legemiddelinteraksjoner** (100 registrert; eksempler fra DDInter):
- **Alvorlige (Major):** loperamid, triamcinolon, budesonid
- **Moderate:** acarbose, hydrokortison, albiglutid, alogliptin, metformin, alosetron, bupropion, aprepitant, deksametason, lorkaserin, betametason, metronidazol, kanagliflozin, klorpropamid, klaritromycin

Interaksjonsmønsteret er forenlig med ritonavirs kraftige CYP3A4-hemming.

---

## Konklusjon og neste steg

**Beslutning: Hold**

**Begrunnelse:**
SIV er en dyremodell for HIV, og den foreslåtte indikasjonen er i praksis en gjentakelse av den eksisterende HIV-indikasjonen, uten kliniske studier. Evidensen er preklinisk (L4), alle norske/europeiske godkjenninger er kansellert, og sikkerhetsdata fra preparatomtalen mangler.

**For å gå videre kreves følgende:**
- Preparatomtale med advarsler og kontraindikasjoner (blokkerende datamangel for sikkerhetsscreening)
- Data om virkningsmekanisme fra DrugBank
- Avklaring av om en slik prediksjon har noen reell terapeutisk verdi utover den eksisterende HIV-indikasjonen (f.eks. som forskningsmodell)
- Avklaring av årsaken til at alle godkjenninger er kansellert og av gjeldende regulatorisk status
## Ansvarsfraskrivelse

Dette innholdet er kun til forskningsformål og utgjør ikke medisinsk rådgivning.
Klinisk validering kreves før enhver klinisk anvendelse.

---

