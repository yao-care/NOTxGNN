---
layout: default
title: Palonosetron
parent: Moderat evidens (L3-L4)
nav_order: 308
evidence_level: L4
indication_count: 4
last_modified_at: 2026-11-24
description: "Palonosetron: predikert ny indikasjon Migrene (migraine disorder) (evidensnivå L4). Opprinnelig indikasjon: Oppkast"
monitor_inn: "PALONOSETRON"
predicted_indications: ["migraine disorder", "migraine with brainstem aura", "atrophoderma vermiculata", "ulerythema ophryogenesis"]
---

# Palonosetron
{: .fs-9 }

Evidensnivå: **L4** | Predikerte indikasjoner: **4** stk.
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

## Palonosetron: Fra kjemoterapiindusert oppkast til migrene
{: .text-alpha }

## Oppsummering i én setning

Palonosetron er en 5-HT3-reseptorantagonist som opprinnelig brukes mot oppkast og kvalme ved kreftbehandling. TxGNN-modellen forutsier at legemidlet kan ha effekt ved **migrene (migraine disorder)**, men støtten er svært svak: **ingen kliniske studier** og bare **1 publikasjon**, et kasuistisk tilfelle som beskriver migrenelignende hodepine *forårsaket* av palonosetron, altså et bivirkningssignal og ikke et tegn på nytte.

---

## Hurtigoversikt

| Punkt | Innhold |
|------|------|
| Opprinnelig indikasjon | Oppkast; kreft (kvalme og oppkast knyttet til kreftbehandling) |
| Foreslått ny indikasjon | Migrene (migraine disorder) |
| TxGNN-prediksjonsscore | 0,9974 |
| Evidensnivå | L4 |
| Markedsstatus i Norge | Markedsført (gyldige tillatelser: 3 av 3) |
| Antall godkjenninger | 3 (gyldige: 3) |
| Anbefalt beslutning | Hold |

---

## Hvorfor er denne prediksjonen (ikke) rimelig?

Ifølge avsnittet «Mechanism of Action» i preparatomtalen som er godkjent av amerikanske FDA (Prescribing Information), for Palonosetron (uoffisiell oversettelse): «Palonosetron er en 5-HT 3 -reseptorantagonist med sterk bindingsaffinitet for denne reseptoren og liten eller ingen affinitet for andre reseptorer. Kjemoterapi mot kreft kan være forbundet med høy forekomst av kvalme og oppkast, særlig når visse midler, som cisplatin, brukes.» Engelsk originaltekst: "Palonosetron is a 5-HT 3 receptor antagonist with a strong binding affinity for this receptor and little or no affinity for other receptors. Cancer chemotherapy may be associated with a high incidence of nausea and vomiting, particularly when certain agents, such as cisplatin, are used." ([DailyMed: Posfrea (palonosetron) prescribing information, Avyxa Pharma, LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=13a201ba-c86d-48c5-a0e1-a3e0b4e6a2a7), versjon av 2025-04-29; hentet 2026-11-19). Basert på kjent informasjon er palonosetron en 5-HT3-reseptorantagonist. Effekten ved kjemoterapiindusert kvalme og oppkast er etablert, og mekanistisk kan serotonerge signalveier også ha betydning ved migrene, så en biologisk sammenheng er plausibel.

Retningen på effekten er imidlertid uavklart. Den eneste publikasjonen som støtter prediksjonen, er en kasuistikk om migrenelignende hodepine utløst av palonosetron. Det peker i motsatt retning av en terapeutisk bruk. Den høye scoren kommer fra TxGNN-modellen (dyp læring) og kan gjenspeile likheter modellen har lært mellom beslektede sykdommer, ikke biologisk evidens.

De øvrige prediksjonene i rangeringen er enda svakere:

| Rangering | Sykdom | Score | Evidensnivå | Kommentar |
|------|------|------|------|------|
| 2 | Migrene med hjernestammeaura | 0,9967 | L5 | Kun prediksjon; undergruppe av migrene |
| 4 | Atrofoderma vermiculata | 0,9913 | L5 | Ingen plausibel mekanisme; trolig grafartefakt |
| 5 | Ulerythema ophryogenes | 0,9907 | L5 | Ingen mekanistisk begrunnelse; kun beregningsmessig |

---

## Klinisk studieevidens

Det er for øyeblikket ingen relaterte kliniske studier registrert.

---

## Litteraturevidens

| PMID | År | Type | Tidsskrift | Hovedfunn |
|------|-----|------|------|---------|
| [21132477](https://pubmed.ncbi.nlm.nih.gov/21132477/) | 2011 | Kasuistikk | Canadian Journal of Anaesthesia | Beskriver migrenelignende hodepine utløst av palonosetron (bivirkningssignal, ikke effekt) |
| [42748473](https://pubmed.ncbi.nlm.nih.gov/42748473/) | 2026 | Oversikt | European Heart Journal – Cardiovascular Pharmacotherapy | Gjennomgang av QT-forlengelse ved antiemetika og et risikostratifisert forskrivningsrammeverk; relevant for hjertesikkerhet, ikke for migreneeffekt |

---

## Informasjon om det norske markedet

Alle tre registrerte godkjenninger er kansellert. Dosering/legemiddelform er ikke oppgitt i dataene.

<!-- licenses:begin -->

| Godkjenningsnummer | Preparatnavn (EMA) | Virkestoff(er) (EMA, engelsk) | Terapeutisk område (EMA, engelsk) | Status |
|------|------|------|------|------|
| EMEA/H/C/000563 | Aloxi | palonosetron hydrochloride | Vomiting; Cancer | Gyldig |
| EMEA/H/C/003728 | Akynzeo | netupitant; palonosetron hydrochloride | Vomiting; Neoplasms; Nausea; Cancer | Gyldig |
| EMEA/H/C/004129 | Palonosetron Accord | palonosetron | Vomiting; Nausea; Cancer | Gyldig |

Kilde: EMA – Medicines output (sentralt godkjente legemidler til mennesker); preparatnavn, virkestoffer og terapeutisk område er gjengitt i engelsk original. Nasjonale markedsføringstillatelser (DMP) og veterinærpreparater er ikke med i disse dataene.

<!-- licenses:end -->

---

## Sikkerhetsvurderinger

**Legemiddelinteraksjoner**: Interaksjonssøket ga 100 treff. Blant de som er vist, er flere klassifisert som **alvorlige (Major)**:

- **Opioider**: fentanyl, alfentanil, tramadol
- **Serotonerge/andre**: dekstrometorfan, amitriptylin
- **Triptaner**: almotriptan, sumatriptan (særlig relevant ved migrenebruk)
- **QT-/rytmerelaterte**: amiodaron, amisulprid, anagrelid

Moderate interaksjoner omfatter blant annet abirateron, dihydrokodein, kodein, famotidin, formoterol, adenosin, salbutamol, alfuzosin, propofol og loperamid.

**Annen sikkerhetsinformasjon**: Gjennomgangen fra 2026 peker på at antiemetika kan forlenge QT-intervallet, noe som bør vurderes ved en eventuell ny bruk. Se preparatomtalen for øvrige advarsler og kontraindikasjoner.

---

## Konklusjon og neste steg

**Beslutning: Hold**

**Begrunnelse:**
Prediksjonen bygger på en høy modellscore, men den eneste litteraturen er en kasuistikk om et bivirkningssignal (migrenelignende hodepine), som går i motsatt retning av ønsket effekt. Det finnes ingen kliniske studier, og alle norske/europeiske godkjenninger er kansellert.

**For å gå videre trengs følgende:**
- Data om virkningsmekanisme (MOA) fra DrugBank
- Advarsler og kontraindikasjoner fra preparatomtalen (blokkerende datamangel for sikkerhetsscreening)
- Avklaring av effektretning: gir palonosetron migrene eller kan det lindre den? Dette krever prekliniske eller mekanistiske studier
- Gjennomgang av litteratur om 5-HT3-antagonister generelt ved migrene
- Vurdering av QT-risiko og interaksjoner med triptaner og andre serotonerge legemidler
- Avklaring av administrasjonsvei og tilgjengelige formuleringer, siden legemidlet er markedsført med 3 gyldige markedsføringstillatelser av 3

<!-- review:begin log -->

## Kontrollogg

Nedenfor er gjennomgangsloggen for denne siden. Setningen om at data om virkningsmekanismen ikke var tilgjengelige, er erstattet med et utdrag fra den oppgitte offisielle preparatomtalen (med uoffisiell oversettelse); modellprediksjoner, evidensnivåer og konklusjoner er ikke omskrevet.

| Kontrolldato | Punkt | Tiltak | Kilde |
|------|------|------|------|
| 2026-11-19 | Setningen «data om virkningsmekanismen er ikke tilgjengelige» erstattet med utdrag fra amerikansk preparatomtale | Setning om manglende data om virkningsmekanismen erstattet med et utdrag med kilde | [DailyMed: Posfrea (palonosetron) prescribing information, Avyxa Pharma, LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=13a201ba-c86d-48c5-a0e1-a3e0b4e6a2a7) |

<!-- review:end log -->

## Ansvarsfraskrivelse

Dette innholdet er kun til forskningsformål og utgjør ikke medisinsk rådgivning.
Klinisk validering kreves før enhver klinisk anvendelse.

---

