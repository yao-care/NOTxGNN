---
layout: default
title: Pibrentasvir
parent: Moderat evidens (L3-L4)
nav_order: 326
evidence_level: L4
indication_count: 10
last_modified_at: 2026-10-15
description: "Pibrentasvir: predikert ny indikasjon Hepatitt B-virusinfeksjon (evidensnivå L5). Opprinnelig indikasjon: Kronisk hepatitt C"
monitor_inn: "PIBRENTASVIR"
predicted_indications: ["hepatitis B virus infection", "HIV infectious disease", "hepatitis E virus infection", "hepatitis A virus infection", "hepatitis, viral, animal", "Omsk hemorrhagic fever", "Kyasanur forest disease", "simian immunodeficiency virus infection", "feline acquired immunodeficiency syndrome", "neurodevelopmental disorder with ataxic gait, absent speech, and decreased cortical white matter"]
---

# Pibrentasvir
{: .fs-9 }

Evidensnivå: **L4** | Predikerte indikasjoner: **10** stk.
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

## Pibrentasvir: Fra kronisk hepatitt C til hepatitt B-virusinfeksjon
{: .text-alpha }

## Oppsummering i én setning

Pibrentasvir er en NS5A-hemmer som brukes mot kronisk hepatitt C, i praksis som del av kombinasjonen glekaprevir/pibrentasvir (Maviret).
TxGNN-modellen predikerer at legemidlet kan være virksomt mot **hepatitt B-virusinfeksjon**, men dataene som er sammenstilt for denne rapporten viser **ingen kliniske studier** og **ingen litteratur som viser anti-HBV-effekt**. Prediksjonen er foreløpig kun modellbasert.

---

## Hurtigoversikt

| Punkt | Innhold |
|------|------|
| Opprinnelig indikasjon | Kronisk hepatitt C |
| Predikert ny indikasjon | Hepatitt B-virusinfeksjon |
| TxGNN-prediksjonsscore | 0,9984 |
| Evidensnivå | L4 (ifølge dataene; i praksis ingen HBV-spesifikk evidens, nærmere L5) |
| Status på det norske markedet | Markedsført (gyldige tillatelser: 1 av 1) |
| Antall godkjenninger | 1 (gyldige: 1) |
| Antall tillatelser | 1 (avregistrert) |
| Anbefalt beslutning | Hold |

---

## Hvorfor er denne prediksjonen rimelig?

Detaljerte data om virkningsmekanisme er ikke tilgjengelige for dette legemidlet. Basert på kjent informasjon er pibrentasvir en hemmer av HCV NS5A-proteinet, og effekten er godt dokumentert ved hepatitt C.

Hepatitt B og hepatitt C er begge virusinfeksjoner i leveren. Scoren kommer fra TxGNN-modellen (dyp læring) og kan gjenspeile likheter modellen har lært mellom beslektede sykdommer, ikke biologisk evidens. Mekanistisk er koblingen svak: HBV har ikke noe NS5A-protein og har en annen replikasjonsstrategi (cccDNA og revers transkriptase). Det finnes derfor ingen etablert direkte mekanistisk forbindelse.

Relevansen er i praksis begrenset til håndtering av HBV/HCV-koinfeksjon, der HCV behandles og HBV-reaktivering må overvåkes. Den øvrige litteraturen gjelder utelukkende HCV.

---

## Dokumentasjon fra kliniske studier

Foreløpig finnes ingen registrerte kliniske studier for hepatitt B-virusinfeksjon.

*Til orientering: Den nest høyest rangerte prediksjonen (HIV) har flere Phase 3-studier, men de gjelder behandling av HCV hos personer med HIV-koinfeksjon, ikke behandling av HIV. Eksempler: [NCT02738138](https://clinicaltrials.gov/study/NCT02738138) (EXPEDITION-2, fase 3, fullført, n=153) og [NCT03222583](https://clinicaltrials.gov/study/NCT03222583) (fase 3, fullført, n=546).*

---

## Litteraturdokumentasjon

| PMID | År | Type | Tidsskrift | Hovedfunn |
|------|-----|------|------|---------|
| [31981264](https://pubmed.ncbi.nlm.nih.gov/31981264/) | 2020 | Kohort | J Viral Hepat | Glekaprevir/pibrentasvir ved HCV og alvorlig nyresvikt (CKD 4–5) hos 108 pasienter i Taiwan |
| [30982721](https://pubmed.ncbi.nlm.nih.gov/30982721/) | 2019 | Oversikt | Lancet Gastroenterol Hepatol | HCV-infeksjon hos barn og ungdom; direktevirkende antivirale midler har endret behandlingen |
| [31041789](https://pubmed.ncbi.nlm.nih.gov/31041789/) | 2019 | Oversikt | Semin Liver Dis | Ny behandling av HCV-pasienter med DAA-svikt |
| [31114957](https://pubmed.ncbi.nlm.nih.gov/31114957/) | 2019 | Oversikt | Clin Pharmacokinet | Farmakokinetiske og farmakodynamiske vurderinger ved HCV-behandling |
| [34092970](https://pubmed.ncbi.nlm.nih.gov/34092970/) | 2021 | Oversikt | World J Gastroenterol | Behandling av virushepatitt B og C hos barn |
| [42127258](https://pubmed.ncbi.nlm.nih.gov/42127258/) | 2026 | Oversikt | Top Antivir Med | Konferanserapport fra CROI 2026 om virushepatitt; ingen data om pibrentasvir ved HBV |
| [35579223](https://pubmed.ncbi.nlm.nih.gov/35579223/) | 2022 | Oversikt | Eur J Gen Pract | Diagnostikk og behandling av kronisk HCV |
| [29369303](https://pubmed.ncbi.nlm.nih.gov/29369303/) | 2018 | Oversikt | AIDS Rev | Rapport fra den internasjonale konferansen om virushepatitt 2017 |

Ingen av publikasjonene viser at pibrentasvir har effekt mot HBV.

---

## Informasjon om det norske markedet

| Tillatelsesnummer | Produktnavn | Doseringsform | Godkjent indikasjon |
|---------|------|------|-----------|
| EMEA/H/C/004430 | Maviret | Ikke oppgitt | Kronisk hepatitt C (status: godkjent) |

---

## Sikkerhetsvurderinger

Se preparatomtalen for sikkerhetsinformasjon. Det er ikke funnet registrerte legemiddelinteraksjoner i dataene som er sammenstilt for denne rapporten.

---

## Konklusjon og neste steg

**Beslutning: Hold**

**Begrunnelse:**
Den høye TxGNN-scoren (0,9984) mangler støtte i kliniske data, litteratur og en plausibel mekanisme. HBV har ingen NS5A-analog, og all tilgjengelig dokumentasjon gjelder HCV. Legemidlet er markedsført i Norge, med 1 gyldig markedsføringstillatelse av 1.

**For å gå videre kreves følgende:**
- Data om virkningsmekanisme (MOA) fra DrugBank
- Preparatomtale med advarsler og kontraindikasjoner (blokkerende datamangel for sikkerhetsscreening)
- In vitro-data som viser eventuell antiviral aktivitet mot HBV
- Kliniske data for HBV/HCV-koinfeksjon, med overvåking av HBV-reaktivering
- Avklaring av regulatorisk status i Norge

---

*Merknad om øvrige prediksjoner: HIV (score 0,9980), hepatitt E, hepatitt A, virushepatitt hos dyr, omsk hemorragisk feber, Kyasanur-skogsykdom, SIV, felint ervervet immunsviktsyndrom og en sjelden nevroutviklingsforstyrrelse har alle evidensnivå L4–L5 og anbefalingen «Hold». Studiene som er knyttet til HIV og hepatitt A gjelder HCV-behandling, ikke de predikerte sykdommene, og utgjør derfor ikke evidens for disse indikasjonene.*
## Ansvarsfraskrivelse

Dette innholdet er kun til forskningsformål og utgjør ikke medisinsk rådgivning.
Klinisk validering kreves før enhver klinisk anvendelse.

---

