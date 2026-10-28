---
layout: default
title: Ibuprofen
parent: Kun modellprediksjon (L5)
nav_order: 203
evidence_level: L5
indication_count: 7
last_modified_at: 2026-10-28
description: "Ibuprofen: predikert ny indikasjon Akromesomelisk dysplasi, Hunter-Thompson-type (evidensnivå L5). Opprinnelig indikasjon: Persistent ductus arteriosus (Ductus Arteriosus, Patent)"
monitor_inn: "IBUPROFEN"
predicted_indications: ["acromesomelic dysplasia, Hunter-Thompson type", "brachyolmia-amelogenesis imperfecta syndrome", "myosclerosis", "brachyolmia", "brachydactyly-syndactyly syndrome", "pseudoachondroplasia", "colobomatous microphthalmia-rhizomelic dysplasia syndrome"]
---

# Ibuprofen
{: .fs-9 }

Evidensnivå: **L5** | Predikerte indikasjoner: **7** stk.
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

## Ibuprofen: Fra persistent ductus arteriosus til akromesomelisk dysplasi, Hunter-Thompson-type
{: .text-alpha }

## Oppsummering i én setning

Ibuprofen er en ikke-selektiv COX-hemmer som i Norge/EØS-sammenheng er godkjent for å lukke persistent ductus arteriosus (PDA) hos premature nyfødte.
TxGNN-modellen forutsier at legemidlet kan være effektivt mot **akromesomelisk dysplasi, Hunter-Thompson-type**, men det finnes **ingen kliniske studier** og **ingen publikasjoner** som støtter denne prediksjonen.

---

## Hurtigoversikt

| Punkt | Innhold |
|------|------|
| Opprinnelig indikasjon | Persistent ductus arteriosus (Ductus Arteriosus, Patent) |
| Predikert ny indikasjon | Akromesomelisk dysplasi, Hunter-Thompson-type |
| TxGNN-prediksjonsscore | 0,9974 |
| Evidensnivå | L5 |
| Markedsstatus i Norge | Markedsført (gyldige tillatelser: 2 av 2) |
| Antall godkjenninger | 2 (gyldige: 2) |
| Anbefalt beslutning | Hold |

---

## Hvorfor er denne prediksjonen (ikke) rimelig?

Data om detaljert virkningsmekanisme er foreløpig ikke tilgjengelig i datagrunnlaget. Ibuprofen er kjent som en ikke-selektiv COX-hemmer med antiinflammatorisk og smertestillende effekt. Ved PDA fører COX-hemming til redusert prostaglandinsyntese, som igjen fremmer lukking av ductus.

Akromesomelisk dysplasi, Hunter-Thompson-type, er en sjelden genetisk skjelettsykdom forårsaket av funksjonstapsmutasjoner i CDMP1/GDF5, som påvirker beinvekst. Ibuprofen virker ikke på GDF5/BMP-signalveien, og det er ikke identifisert noen troverdig mekanistisk kobling til den opprinnelige indikasjonen. Den høye TxGNN-scoren (0,9974) er kun en prediksjon fra TxGNN-modellen (dyp læring). Ved ytterligere bruk kan ibuprofen i beste fall gi symptomatisk smertelindring, noe som ikke er en sykdomsmodifiserende indikasjon.

Det er også verdt å merke seg at de øvrige topp-prediksjonene (blant annet brachyolmia, pseudoachondroplasi, brachydaktyli-syndaktyli-syndrom og myosklerose) i hovedsak er sjeldne skjelett- eller utviklingsforstyrrelser. Scorene kommer fra TxGNN-modellen (dyp læring) og kan gjenspeile likheter modellen har lært mellom beslektede sykdommer, ikke biologisk evidens.

---

## Klinisk studieevidens

Foreløpig er det ingen relaterte kliniske studier registrert.

---

## Litteraturevidens

Foreløpig er det ingen relatert litteratur tilgjengelig.

---

## Markedsinformasjon for Norge

| Godkjenningsnummer | Produktnavn | Doseringsform | Godkjent indikasjon |
|---------|------|------|-----------|
| EMEA/H/C/000549 | Pedea (Recordati Rare Diseases) | – | Persistent ductus arteriosus (opphevet) |
| EMEA/H/C/006129 | Ibuprofen Gen.Orph (Gen.Orph) | – | Persistent ductus arteriosus (opphevet) |

---

## Sikkerhetsvurderinger

**Kontraindikasjoner fra kunnskapsgrafen** (hentet fra TxGNN/PrimeKG-relasjoner mellom legemiddel og sykdom, ikke fra preparatomtale). Blant annet:
- Hjerte- og karsykdommer: hypertensjon, hypotensjon, hjerteinfarkt, hjerneslag, cerebrovaskulære sykdommer, cerebralt infarkt
- Lever- og nyresykdommer: leversvikt, leversykdom, nyresykdom, gallblæresykdom
- Mage-tarm: magesår, inflammatorisk tarmsykdom
- Blod: trombocytopeni, blodkoagulasjonsforstyrrelser
- Metabolske og endokrine: diabetes mellitus, diabetisk ketoacidose, hypotyreose (inkl. myksødem og medfødt hypotyreose), kaliummangel
- Andre: epilepsi, kronisk obstruktiv lungesykdom, systemisk lupus erythematosus, godartet prostatahyperplasi, rusmiddelmisbruk/avhengighet, pyoureter

**Legemiddelinteraksjoner** (100 registrerte interaksjoner; utvalg):
- **Alvorlig (Major):** acetylsalisylsyre
- **Moderat:** kortikosteroider (betametason, budesonid, deksametason, hydrokortison), sulfonylurea-preparater (acetoheksamid, klorpropamid, glimepirid, glipizid, glyburid), eksenatid, aprepitant, balsalazid, fenfluramin og deksfenfluramin, kanamycin, levofloksacin
- **Mindre (Minor):** famotidin, ranitidin, cimetidin

Ved prenatal eksponering for NSAID er det i tillegg kjent risiko for blant annet innsnevring av ductus arteriosus og nyrepåvirkning, noe som er relevant for tilstander med medfødte misdannelser.

Fullstendige advarsler og kontraindikasjoner fra preparatomtalen mangler i datagrunnlaget; se preparatomtalen for sikkerhetsinformasjon.

---

## Konklusjon og neste steg

**Beslutning: Hold**

**Begrunnelse:**
Prediksjonen er kun modellbasert (L5) uten kliniske studier eller litteratur, og det finnes ingen troverdig mekanistisk kobling mellom COX-hemming og GDF5-relatert skjelettdysplasi. Ibuprofen er i dag markedsført i Norge, med 2 gyldige godkjenninger av 2.

**For å gå videre kreves følgende:**
- Data om virkningsmekanisme (MOA) fra DrugBank
- Preparatomtale med advarsler og kontraindikasjoner fra den relevante godkjenningsmyndigheten
- Prekliniske eller mekanistiske studier som viser en mulig effekt på GDF5/BMP-signalveien eller på sykdomsforløpet
- Vurdering av om symptomatisk smertelindring er det eneste realistiske bruksområdet, og i så fall om dette er relevant som repurposing-mål
## Ansvarsfraskrivelse

Dette innholdet er kun til forskningsformål og utgjør ikke medisinsk rådgivning.
Klinisk validering kreves før enhver klinisk anvendelse.

---

