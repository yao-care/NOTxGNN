---
layout: default
title: Posaconazole
parent: Moderat evidens (L3-L4)
nav_order: 333
evidence_level: L4
indication_count: 1
last_modified_at: 2026-11-20
description: "Posaconazole: predikert ny indikasjon pneumocystosis (evidensnivå L4)."
monitor_inn: "POSACONAZOLE"
predicted_indications: ["pneumocystosis"]
---

# Posaconazole
{: .fs-9 }

Evidensnivå: **L4** | Predikerte indikasjoner: **1** stk.
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

## Posakonazol: pneumocystosis
{: .text-alpha }

## Oppsummering i én setning

Posakonazol er et triazol-soppmiddel som opprinnelig brukes mot mykoser, blant annet candidiasis, koksidioidomykose og aspergillose.
TxGNN-modellen forutsier at det kan ha effekt mot **pneumocystose**,
men det finnes foreløpig **ingen kliniske studier som direkte tester posakonazol** for denne indikasjonen, og de **5 publikasjonene** som er funnet gir kun indirekte bakgrunn. Mekanistisk er prediksjonen tvilsom.

---

## Hurtigoversikt

| Punkt | Innhold |
|------|------|
| Opprinnelig indikasjon | Mykoser (soppinfeksjoner) |
| Foreslått ny indikasjon | Pneumocystose |
| TxGNN-prediksjonsscore | 0,9977 |
| Evidensnivå | L4 |
| Markedsstatus i Norge | Markedsført (gyldige tillatelser: 3 av 3) |
| Antall godkjenninger | 3 (gyldige: 3) |
| Anbefalt beslutning | Hold |

---

## Hvorfor er denne prediksjonen rimelig (eller ikke)?

Posakonazol er et triazol-soppmiddel som hemmer soppenzymet lanosterol 14-alfa-demetylase (CYP51) og dermed blokkerer syntesen av ergosterol. Ifølge avsnittene «Mechanism of Action» og «Microbiology» i preparatomtalen som er godkjent av amerikanske FDA (Prescribing Information), for Posaconazole (uoffisiell oversettelse): «Posakonazol er et antimykotikum av azoltypen. […] Posakonazol blokkerer syntesen av ergosterol, en nøkkelkomponent i soppens cellemembran, ved å hemme det cytokrom P-450-avhengige enzymet lanosterol-14α-demetylase, som er ansvarlig for omdannelsen av lanosterol til ergosterol i soppens cellemembran. Dette fører til en opphopning av metylerte sterolforstadier og en uttømming av ergosterol i cellemembranen, noe som svekker strukturen og funksjonen til soppens cellemembran.» Engelsk originaltekst: "Posaconazole is an azole antifungal agent. […] Posaconazole blocks the synthesis of ergosterol, a key component of the fungal cell membrane, through the inhibition of cytochrome P-450 dependent enzyme lanosterol 14α-demethylase responsible for the conversion of lanosterol to ergosterol in the fungal cell membrane. This results in an accumulation of methylated sterol precursors and a depletion of ergosterol within the cell membrane thus weakening the structure and function of the fungal cell membrane." ([DailyMed: Noxafil (posaconazole) prescribing information, Merck Sharp & Dohme LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=b073b082-7b57-4423-8c06-4fd4263d6f84), versjon av 2026-02-13; hentet 2026-11-19).

Pneumocystis jirovecii mangler imidlertid i hovedsak ergosterol i cellemembranen og bruker kolesterolliknende steroler. Den azolbaserte mekanismen har derfor lite biologisk grunnlag mot denne organismen. Den høye TxGNN-scoren (0,9977) kommer fra TxGNN-modellen (dyp læring) og kan gjenspeile likheter modellen har lært mellom beslektede sykdommer, ikke biologisk evidens for en spesifikk effekt mot Pneumocystis.

Prediksjonen bør derfor leses som en modellassosiasjon og ikke som en mekanistisk begrunnet hypotese.

---

## Evidens fra kliniske studier

| Studienummer | Fase | Status | Antall deltakere | Hovedfunn |
|---------|------|------|------|---------|
| [NCT04368559](https://clinicaltrials.gov/study/NCT04368559) | Fase 3 | Fullført | 602 | ReSPECT-studien: rezafungin (et ekinokandin) mot standard antimikrobiell behandling for å forebygge invasive soppinfeksjoner etter allogen blod- og margtransplantasjon. Posakonazol er ikke dokumentert som studiearm eller komparator. |

Studien gir ingen direkte evidens for posakonazol og kan ikke telle mot evidensnivå L1.

---

## Litteraturevidens

| PMID | År | Type | Tidsskrift | Hovedfunn |
|------|-----|------|------|---------|
| [41232547](https://pubmed.ncbi.nlm.nih.gov/41232547/) | 2026 | Retningslinje/oversikt | The Lancet Infectious Diseases | Oppdaterte britiske anbefalinger for diagnostikk av alvorlige soppsykdommer |
| [41362140](https://pubmed.ncbi.nlm.nih.gov/41362140/) | 2025 | Retningslinje/oversikt | Zhonghua Jie He He Hu Xi Za Zhi | Kinesiske retningslinjer for diagnostikk og behandling av invasive lungesoppsykdommer |
| [26901377](https://pubmed.ncbi.nlm.nih.gov/26901377/) | 2016 | Oversikt | Swiss Medical Weekly | Oversikt over invasiv candidiasis, aspergillose, kryptokokkose og Pneumocystis-pneumoni. Profylakse med posakonazol har redusert invasiv candidiasis og aspergillose hos høyrisiko hemato-onkologiske pasienter. |
| [21973267](https://pubmed.ncbi.nlm.nih.gov/21973267/) | 2011 | Oversikt (farmakokinetikk) | Clinical Pharmacokinetics | Penetrasjon av soppmidler inn i lungenes epitelforingsvæske |
| [35596686](https://pubmed.ncbi.nlm.nih.gov/35596686/) | 2022 | Kohortstudie | Transplant Infectious Disease | Infeksjonskomplikasjoner ved akutt graft-versus-host-sykdom etter levertransplantasjon |

Ingen av publikasjonene er randomiserte studier som viser effekt av posakonazol mot pneumocystose.

---

## Markedsinformasjon for Norge

| Godkjenningsnummer | Produktnavn | Legemiddelform | Godkjent indikasjon |
|---------|------|------|-----------|
| EMEA/H/C/005005 | Posaconazole Accord | Ikke oppgitt | Mykoser (kansellert) |
| EMEA/H/C/000610 | Noxafil | Ikke oppgitt | Candidiasis, mykoser, koksidioidomykose, aspergillose (kansellert) |
| EMEA/H/C/005028 | Posaconazole AHCL | Ikke oppgitt | Mykoser (kansellert) |

Alle tre godkjenningene er gyldige.

---

## Sikkerhetsvurderinger

Data om advarsler og kontraindikasjoner fra preparatomtalen mangler. Se preparatomtalen for fullstendig sikkerhetsinformasjon.

**Legemiddelinteraksjoner:** Totalt 100 interaksjoner er registrert, og 20 er vist i datagrunnlaget. Alvorlighetsgrad «Major» gjelder:
- Loperamid
- Triamcinolon
- Budesonid

Flere har moderat alvorlighetsgrad, blant annet:
- Syrehemmere: famotidin, ranitidin, rabeprazol, omeprazol, cimetidin
- Kortikosteroider: hydrokortison, deksametason, betametason
- Andre: aprepitant, klaritromycin, saksagliptin, bisakodyl, pikosulfat og polyetylenglykol

---

## Konklusjon og neste steg

**Beslutning: Hold**

**Begrunnelse:**
Prediksjonen mangler både direkte klinisk evidens og et plausibelt mekanistisk grunnlag, siden Pneumocystis mangler ergosterol som er målet for azoler. Posakonazol er for øyeblikket markedsført i Norge, med tre gyldige godkjenninger av tre.

**For å gå videre trengs følgende:**
- Direkte kliniske eller prekliniske data på posakonazol mot Pneumocystis jirovecii
- Opplysninger om virkningsmekanisme fra legemiddeldatabasen
- Advarsler og kontraindikasjoner fra preparatomtalen (blokkerende datamangel før sikkerhetsscreening)
- Avklaring av markedsstatus og administrasjonsveier i Norge
- Vurdering av relevansen av interaksjoner for aktuell pasientgruppe, særlig immunsupprimerte pasienter

<!-- review:begin log -->

## Kontrollogg

Nedenfor er gjennomgangsloggen for denne siden. Setningen om at data om virkningsmekanismen ikke var tilgjengelige, er erstattet med et utdrag fra den oppgitte offisielle preparatomtalen (med uoffisiell oversettelse); modellprediksjoner, evidensnivåer og konklusjoner er ikke omskrevet.

| Kontrolldato | Punkt | Tiltak | Kilde |
|------|------|------|------|
| 2026-11-19 | Setningen «data om virkningsmekanismen er ikke tilgjengelige» erstattet med utdrag fra amerikansk preparatomtale | Setning om manglende data om virkningsmekanismen erstattet med et utdrag med kilde | [DailyMed: Noxafil (posaconazole) prescribing information, Merck Sharp & Dohme LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=b073b082-7b57-4423-8c06-4fd4263d6f84) |

<!-- review:end log -->

## Ansvarsfraskrivelse

Dette innholdet er kun til forskningsformål og utgjør ikke medisinsk rådgivning.
Klinisk validering kreves før enhver klinisk anvendelse.

---

