---
layout: default
title: Eculizumab
parent: Kun modellprediksjon (L5)
nav_order: 138
evidence_level: L5
indication_count: 10
last_modified_at: 2026-11-24
description: "Eculizumab: predikert ny indikasjon Syklisk hematopoese (evidensnivå L5). Opprinnelig indikasjon: Paroksysmal nattlig hemoglobinuri (PNH)"
monitor_inn: "ECULIZUMAB"
predicted_indications: ["cyclic hematopoiesis", "autosomal recessive severe congenital neutropenia due to JAGN1 deficiency", "X-linked severe congenital neutropenia", "congenital neutropenia-myelofibrosis-nephromegaly syndrome", "adult idiopathic neutropenia", "autosomal recessive severe congenital neutropenia due to CXCR2 deficiency", "primary immunodeficiency syndrome due to p14 deficiency", "autosomal recessive severe congenital neutropenia due to CSF3R deficiency", "severe congenital neutropenia", "primary release disorder of platelets"]
---

# Eculizumab
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

## Eculizumab: Fra paroksysmal nattlig hemoglobinuri til syklisk hematopoese
{: .text-alpha }

## Oppsummering i én setning

Eculizumab er en komplementhemmer (C5-hemmer) som opprinnelig brukes til behandling av paroksysmal nattlig hemoglobinuri (PNH). TxGNN-modellen forutsier at legemidlet kan være effektivt ved **syklisk hematopoese** (syklisk nøytropeni), men det finnes **ingen kliniske studier** og **ingen publikasjoner** som støtter denne spesifikke indikasjonen. Prediksjonen er foreløpig kun modellbasert.

---

## Hurtigoversikt

| Punkt | Innhold |
|------|------|
| Opprinnelig indikasjon | Paroksysmal nattlig hemoglobinuri (PNH) |
| Predikert ny indikasjon | Syklisk hematopoese |
| TxGNN-prediksjonsscore | 0,9997 |
| Evidensnivå | L5 |
| Markedsstatus i Norge | Markedsført (gyldige tillatelser: 3 av 3) |
| Antall godkjenninger | 3 (gyldige: 3) |
| Anbefalt beslutning | Hold |

---

## Hvorfor er denne prediksjonen (ikke) rimelig?

Ifølge avsnittet «Mechanism of Action» i preparatomtalen som er godkjent av amerikanske FDA (Prescribing Information), for Eculizumab (uoffisiell oversettelse): «Ekulizumab, virkestoffet i SOLIRIS, er et monoklonalt antistoff som bindes spesifikt og med høy affinitet til komplementproteinet C5, og hemmer dermed spaltingen til C5a og C5b og forhindrer dannelsen av det terminale komplementkomplekset C5b-9. SOLIRIS hemmer terminal komplementmediert intravaskulær hemolyse hos pasienter med PNH og komplementmediert trombotisk mikroangiopati (TMA) hos pasienter med aHUS.» Engelsk originaltekst: "Eculizumab, the active ingredient in SOLIRIS, is a monoclonal antibody that specifically binds to the complement protein C5 with high affinity, thereby inhibiting its cleavage to C5a and C5b and preventing the generation of the terminal complement complex C5b-9. SOLIRIS inhibits terminal complement-mediated intravascular hemolysis in PNH patients and complement-mediated thrombotic microangiopathy (TMA) in patients with aHUS." ([DailyMed: Soliris (eculizumab) prescribing information, Alexion Pharmaceuticals Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=ebcd67fa-b4d1-4a22-b33d-ee8bf6b9c722), versjon av 2026-07-08; hentet 2026-11-19). Basert på kjent informasjon er eculizumab et monoklonalt antistoff som hemmer komplementprotein C5 og dermed blokkerer den terminale komplementveien. Effekten ved PNH er godt dokumentert, ettersom sykdommen skyldes ukontrollert komplementaktivering etter tap av CD55 og CD59.

Syklisk nøytropeni skyldes derimot hovedsakelig ELANE-mutasjoner og syklisk svikt i benmargen. Det er ikke påvist noen komplementmediert mekanisme som C5-hemming kan påvirke. Den høye modellscoren kommer fra TxGNN-modellen (deep learning) og kan gjenspeile likheter modellen har lært mellom beslektede sykdommer, ikke biologisk evidens.

De øvrige topprangerte prediksjonene er også nøytropenirelaterte tilstander (blant annet alvorlig medfødt nøytropeni med ulike genetiske årsaker, idiopatisk nøytropeni hos voksne og primær immunsvikt på grunn av p14-mangel). For ingen av dem er det funnet en plausibel kobling til C5-blokade. Hos nøytropene eller immunsviktige pasienter kan eculizumabs kjente risiko for meningokokkinfeksjon dessuten være særlig bekymringsfull.

---

## Klinisk studieevidens

Det er for øyeblikket ingen relaterte kliniske studier registrert for denne indikasjonen.

---

## Litteraturevidens

Det er for øyeblikket ingen relatert litteratur tilgjengelig for den predikerte indikasjonen «syklisk hematopoese».

Merk at for andre lavt rangerte prediksjoner ble det funnet publikasjoner, men de gjelder hovedsakelig etablerte eller komplementrelaterte eculizumab-tilstander (PNH, atypisk hemolytisk uremisk syndrom, trombotisk mikroangiopati, myasthenia gravis og CD59-mangel). De omtaler ikke de predikerte sykdommene og støtter dermed ikke de nye indikasjonene.

---

## Informasjon om det norske markedet

<!-- licenses:begin -->

| Godkjenningsnummer | Preparatnavn (EMA) | Virkestoff(er) (EMA, engelsk) | Terapeutisk område (EMA, engelsk) | Status |
|------|------|------|------|------|
| EMEA/H/C/000791 | Soliris | Eculizumab | Hemoglobinuria, Paroxysmal | Gyldig |
| EMEA/H/C/005652 | Bekemv | Eculizumab | Hemoglobinuria, Paroxysmal | Gyldig |
| EMEA/H/C/006036 | Epysqli | Eculizumab | Hemoglobinuria, Paroxysmal | Gyldig |

Kilde: EMA – Medicines output (sentralt godkjente legemidler til mennesker); preparatnavn, virkestoffer og terapeutisk område er gjengitt i engelsk original. Nasjonale markedsføringstillatelser (DMP) og veterinærpreparater er ikke med i disse dataene.

<!-- licenses:end -->

Legemidlet er markedsført, og alle tre godkjenningene (3 av 3) er gyldige i datagrunnlaget.

---

## Sikkerhetsvurderinger

**Legemiddelinteraksjoner:** Fire interaksjoner er funnet (alle av graden «Minor», fra DDInter), alle med humant immunglobulin G (intravenøst, subkutant, intramuskulært, og intravenøst/subkutant).

For øvrig sikkerhetsinformasjon (advarsler og kontraindikasjoner), se preparatomtalen (SPC). Generelt bør man være oppmerksom på risikoen for alvorlige meningokokkinfeksjoner ved komplementhemming, noe som er særlig relevant ved nøytropeni.

---

## Konklusjon og neste steg

**Beslutning: Hold**

**Begrunnelse:**
Prediksjonen er kun modellbasert (evidensnivå L5), uten kliniske studier eller sykdomsspesifikk litteratur, og det finnes ingen plausibel mekanistisk kobling mellom C5-hemming og syklisk nøytropeni. I tillegg er infeksjonsrisikoen ved komplementhemming en bekymring hos nøytropene pasienter.

<!-- review:begin no-lic-20261124b-eculizumab-1 -->

> **Kontrollrettelse (2026-11-24)**: Opprinnelig sto det: «I tillegg er alle norske/europeiske godkjenninger i datagrunnlaget kansellert, og infeksjonsrisikoen ved komplementhemming er en bekymring hos nøytropene pasienter.» Rettet: opplysningen om at godkjenningen(e) er kansellert, er tatt ut fordi den ikke stemte med EMAs data om sentrale EU-godkjenninger (2026-11-12), der godkjenningene står som gyldige (Authorised); resten av setningen er uendret. Oppdaterte antall og statuser for godkjenningene står i hurtigoversikten og i lisenstabellen under markedsinformasjonen. Kilde: [EMA – Medicines output: medicines report](https://www.ema.europa.eu/en/documents/report/medicines-output-medicines-report_en.xlsx); [European Medicines Agency](https://www.ema.europa.eu/).

<!-- review:end no-lic-20261124b-eculizumab-1 -->

**For å gå videre kreves følgende:**
- Data om virkningsmekanisme (MOA), for eksempel fra DrugBank
- Preparatomtale med advarsler og kontraindikasjoner fra DMP (blokkerende datamangel for sikkerhetsscreening)
- Prekliniske eller mekanistiske studier som viser en komplementrolle ved syklisk nøytropeni
- Avklaring av gjeldende markedsstatus i Norge
- Vurdering av andre kandidatindikasjoner med sterkere komplementrelatert begrunnelse

<!-- review:begin no-lic-20261124b-eculizumab-2 -->

> **Kontrollrettelse (2026-11-24)**: Opprinnelig sto det: «Avklaring av gjeldende markedsstatus i Norge, siden alle godkjenninger er registrert som kansellert» Rettet: begrunnelsen om at godkjenningen(e) er kansellert, er tatt ut fordi den ikke stemte med EMAs data om sentrale EU-godkjenninger (2026-11-12), der godkjenningene står som gyldige (Authorised); selve oppfølgingspunktet er beholdt. Oppdaterte antall og statuser for godkjenningene står i hurtigoversikten og i lisenstabellen under markedsinformasjonen. Kilde: [EMA – Medicines output: medicines report](https://www.ema.europa.eu/en/documents/report/medicines-output-medicines-report_en.xlsx); [European Medicines Agency](https://www.ema.europa.eu/).

<!-- review:end no-lic-20261124b-eculizumab-2 -->

<!-- review:begin log -->

## Kontrollogg

Nedenfor er kontrolloggen for denne siden: opplysninger kontrollert mot EMAs data om sentrale EU-godkjenninger. Rettelser gjelder bare grunnleggende faktaopplysninger; modellens prediksjoner, evidensnivåer og konklusjoner er ikke skrevet om. Setningen om at data om virkningsmekanismen ikke var tilgjengelige, er erstattet med et utdrag fra den oppgitte offisielle preparatomtalen (med uoffisiell oversettelse).

| Kontrolldato | Punkt | Tiltak | Kilde |
|------|------|------|------|
| 2026-11-19 | Setningen «data om virkningsmekanismen er ikke tilgjengelige» erstattet med utdrag fra amerikansk preparatomtale | Setning om manglende data om virkningsmekanismen erstattet med et utdrag med kilde | [DailyMed: Soliris (eculizumab) prescribing information, Alexion Pharmaceuticals Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=ebcd67fa-b4d1-4a22-b33d-ee8bf6b9c722) |
| 2026-11-24 | Rettet: «I tillegg er alle norske/europeiske godkjenninger i datagrunnlaget kansellert, og infeksjonsrisikoen ved komplementhemming er en bekymring hos nøytropene pasienter.» → «I tillegg er infeksjonsrisikoen ved komplementhemming en bekymring hos nøytropene pasienter.» | Rettet | [EMA – Medicines output: medicines report](https://www.ema.europa.eu/en/documents/report/medicines-output-medicines-report_en.xlsx); [European Medicines Agency](https://www.ema.europa.eu/) |
| 2026-11-24 | Rettet: «Avklaring av gjeldende markedsstatus i Norge, siden alle godkjenninger er registrert som kansellert» → «Avklaring av gjeldende markedsstatus i Norge» | Rettet | [EMA – Medicines output: medicines report](https://www.ema.europa.eu/en/documents/report/medicines-output-medicines-report_en.xlsx); [European Medicines Agency](https://www.ema.europa.eu/) |

<!-- review:end log -->

## Ansvarsfraskrivelse

Dette innholdet er kun til forskningsformål og utgjør ikke medisinsk rådgivning.
Klinisk validering kreves før enhver klinisk anvendelse.

---

