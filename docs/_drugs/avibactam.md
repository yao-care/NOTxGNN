---
layout: default
title: Avibactam
parent: Kun modellprediksjon (L5)
nav_order: 48
evidence_level: L5
indication_count: 6
last_modified_at: 2026-10-15
description: "Avibactam: predikert ny indikasjon Streptokokkpneumoni (evidensnivå L5). Opprinnelig indikasjon: Bakteriell pneumoni, bløtdelsinfeksjoner…"
---

# Avibactam
{: .fs-9 }

Evidensnivå: **L5** | Predikerte indikasjoner: **6** stk.
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

# Avibaktam: Fra bakterielle infeksjoner til streptokokkpneumoni

## Sammendrag i én setning

Avibaktam er en beta-laktamasehemmer uten egen antibakteriell effekt, brukt i kombinasjon med ceftazidim (Zavicefta) og aztreonam (Emblaveo) mot gramnegative bakterielle infeksjoner, urinveisinfeksjoner, pneumoni og bløtdelsinfeksjoner.
TxGNN-modellen forutsier at legemidlet kan være effektivt mot **streptokokkpneumoni**, men i de data som er sammenstilt for denne rapporten finnes **ingen kliniske studier** og **ingen publikasjoner** som støtter prediksjonen.

---

## Hurtigoversikt

| Punkt | Innhold |
|------|------|
| Opprinnelig indikasjon | Bakteriell pneumoni, bløtdelsinfeksjoner, urinveisinfeksjoner og gramnegative bakterielle infeksjoner |
| Predikert ny indikasjon | Streptokokkpneumoni |
| TxGNN-prediksjonsscore | 99,70 % |
| Evidensnivå | L5 |
| Markedsstatus i Norge | Kun kansellerte godkjenninger |
| Antall godkjenninger | 2 (begge kansellert) |
| Anbefalt beslutning | Hold |

---

## Hvorfor er denne prediksjonen rimelig (eller ikke)?

Detaljerte data om virkningsmekanisme er ikke tilgjengelige i det sammenstilte datagrunnlaget. Ut fra kjent informasjon er avibaktam en ikke-beta-laktam beta-laktamasehemmer som hemmer klasse A-, klasse C- og enkelte klasse D-enzymer. Den har ingen egen antibakteriell aktivitet og brukes i kombinasjon med et beta-laktamantibiotikum.

De godkjente indikasjonene omfatter allerede pneumoni (sykehuservervet og ventilatorassosiert), så streptokokkpneumoni ligger biologisk nær den opprinnelige bruken. Den mekanistiske merverdien er likevel svak: *Streptococcus pneumoniae* er vanligvis ikke avhengig av de beta-laktamasene avibaktam hemmer, og resistens skyldes hovedsakelig endrede penicillinbindende proteiner. Den høye TxGNN-scoren gjenspeiler sannsynligvis nærhet i nettverket til eksisterende pneumoniindikasjoner, ikke en egen terapeutisk begrunnelse.

### Andre predikerte indikasjoner (for sammenligning)

| Predikert indikasjon | TxGNN-score | Vurdering |
|------|------|------|
| Influensa, alvorlig, mottakelighet | 99,28 % | Ingen plausibel mekanisme. Genetisk mottakelighetsfenotype, trolig en grafartefakt. |
| Tuberkulose i urinleder | 99,11 % | Svak og spekulativ. Avibaktam hemmer *M. tuberculosis* sin BlaC in vitro, men kun prekliniske data, og det trengs en partner-beta-laktam. |
| Urinær schistosomiasis | 99,06 % | Ingen troverdig mekanisme. Parasitt uten beta-laktamaseavhengig biologi, praziquantel er standardbehandling. |
| Hyperamylasemi | 99,01 % | Ingen terapeutisk begrunnelse. Laboratoriefunn, trolig grafartefakt. |
| Polyklonalt hyperviskositetssyndrom | 99,01 % | Ingen plausibel mekanisme. Identisk score med hyperamylasemi tyder på en lite informativ prediksjon. |

---

## Norsk markedsinformasjon

| Godkjenningsnummer | Produktnavn | Doseringsform | Godkjent indikasjon |
|---------|------|------|-----------|
| EMEA/H/C/004027 | Zavicefta | Ikke oppgitt | Bakteriell pneumoni, bløtdelsinfeksjoner, pneumoni, urinveisinfeksjoner, gramnegative bakterielle infeksjoner (status: kansellert) |
| EMEA/H/C/006113 | Emblaveo | Ikke oppgitt | Gramnegative bakterielle infeksjoner, urinveisinfeksjoner, helsetjenesteassosiert pneumoni, bløtdelsinfeksjoner (status: kansellert) |

---

## Sikkerhetsvurderinger

Se pakningsvedlegget (preparatomtalen) for sikkerhetsinformasjon. Det er ikke funnet registrerte legemiddelinteraksjoner i de sammenstilte dataene, og kunnskapsgrafen oppgir ingen kontraindikasjoner.

---

## Konklusjon og neste steg

**Beslutning: Hold**

**Begrunnelse:**
Prediksjonen er kun modellbasert (L5), uten kliniske studier eller litteratur. Den mekanistiske merverdien for streptokokkpneumoni er svak, og begge godkjenningene i Norge er kansellert.

**For å gå videre kreves følgende:**
- Hente og analysere pakningsvedlegg med advarsler og kontraindikasjoner (blokkerende datagap for sikkerhetsscreening)
- Fullstendige data om virkningsmekanisme fra DrugBank
- Litteratur- og studiesøk spesifikt for avibaktam-kombinasjoner ved streptokokkpneumoni
- Vurdering av klinisk nytte sammenlignet med eksisterende standardbehandling for *S. pneumoniae*, som ikke primært er avhengig av beta-laktamaser
- Avklaring av tilgjengelighet i Norge, siden alle godkjenninger er kansellert
- Av de øvrige prediksjonene er tuberkulose det eneste sporet med et prekliniske, biologisk rimelig grunnlag (BlaC-hemming), og kan vurderes separat i prekliniske studier
## Ansvarsfraskrivelse

Dette innholdet er kun til forskningsformål og utgjør ikke medisinsk rådgivning.
Klinisk validering kreves før enhver klinisk anvendelse.

---

