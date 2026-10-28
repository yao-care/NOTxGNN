---
layout: default
title: Belimumab
parent: Kun modellprediksjon (L5)
nav_order: 54
evidence_level: L5
indication_count: 6
last_modified_at: 2026-10-15
description: "Belimumab: predikert ny indikasjon Primær frigjøringsforstyrrelse i blodplater (evidensnivå L5). Opprinnelig indikasjon: Systemisk lupus erythematosus"
monitor_inn: "BELIMUMAB"
predicted_indications: ["primary release disorder of platelets", "pseudo-von Willebrand disease", "Glanzmann thrombasthenia", "fetal and neonatal alloimmune thrombocytopenia", "severe nonproliferative diabetic retinopathy", "autosomal dominant macrothrombocytopenia"]
---

# Belimumab
{: .fs-9 }

Evidensnivå: **L5** | Predikerte indikasjoner: **6** stk.
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

## Belimumab: Fra systemisk lupus erythematosus til primær frigjøringsforstyrrelse i blodplater
{: .text-alpha }

## Oppsummering i én setning

Belimumab er et monoklonalt antistoff som hemmer det løselige proteinet BLyS (BAFF), og det var opprinnelig godkjent for behandling av **systemisk lupus erythematosus**.
TxGNN-modellen predikerer at legemidlet kan være effektivt for **primær frigjøringsforstyrrelse i blodplater**, men **ingen kliniske studier** og **ingen publikasjoner** støtter denne prediksjonen i dag. Den er kun en modellprediksjon.

---

## Hurtigoversikt

| Punkt | Innhold |
|------|------|
| Opprinnelig indikasjon | Systemisk lupus erythematosus |
| Predikert ny indikasjon | Primær frigjøringsforstyrrelse i blodplater |
| TxGNN-prediksjonsscore | 0,9996 |
| Evidensnivå | L5 |
| Markedsstatus i Norge | Markedsført (gyldige tillatelser: 1 av 1) |
| Antall godkjenninger | 1 (gyldige: 1) |
| Anbefalt beslutning | Hold |

---

## Hvorfor er denne prediksjonen (ikke) rimelig?

Detaljerte data om virkningsmekanisme er foreløpig ikke tilgjengelige i de innsamlede dataene. Ut fra kjent informasjon hemmer belimumab BLyS (BAFF), noe som reduserer overlevelsen av B-celler og produksjonen av autoantistoffer. Dette forklarer effekten ved systemisk lupus erythematosus, som er en autoimmun sykdom.

Primære frigjøringsforstyrrelser i blodplater er imidlertid vanligvis kvalitative funksjonsdefekter i blodplatene, ofte arvelige, og de drives ikke primært av B-celler eller autoantistoffer. Det er derfor ingen etablert direkte mekanistisk kobling mellom belimumabs virkning og denne tilstanden. Den svært høye TxGNN-scoren (0,9996) er en ren modellprediksjon uten støtte i studier eller litteratur.

**Øvrige predikerte indikasjoner** (alle på evidensnivå L5, beslutning Hold):

| Rangering | Predikert indikasjon | TxGNN-score | Mekanistisk vurdering |
|------|------|------|------|
| 2 | Pseudo-von Willebrand sykdom | 0,9996 | Skyldes genetisk gain-of-function i blodplatereseptoren GPIbα, ikke en autoimmun prosess. Ingen plausibel BLyS-mekanisme. |
| 3 | Glanzmanns trombasteni | 0,9988 | Arvelig mangel eller dysfunksjon av integrin αIIbβ3. Kun en spekulativ, tangentiell kobling via alloantistoffer etter transfusjon. |
| 4 | Føtal og neonatal alloimmun trombocytopeni (FNAIT) | 0,9959 | Biologisk mest sammenhengende, siden sykdommen skyldes maternelle alloantistoffer. Belimumabs effekt på etablerte plasmaceller er begrenset, og sikkerhetsdata i svangerskap er utilstrekkelige. Standardbehandling er IVIG med eller uten kortikosteroider. |
| 5 | Alvorlig ikke-proliferativ diabetisk retinopati | 0,9905 | Drives av mikrovaskulær skade og VEGF-signalering. En rolle for BAFF/B-cellebaner er spekulativ. |
| 6 | Autosomal dominant makrotrombocytopeni | 0,9904 | Arvelige defekter i megakaryopoiese eller cytoskjelett. Ikke autoimmun, og BLyS-hemming forventes ikke å ha nytte. |

---

## Klinisk studieevidens

Foreløpig er det ikke registrert noen relaterte kliniske studier.

---

## Litteraturevidens

Foreløpig finnes det ingen relatert litteratur.

---

## Informasjon om det norske markedet

| Godkjenningsnummer | Produktnavn | Doseringsform | Godkjent indikasjon |
|---------|------|------|-----------|
| EMEA/H/C/002015 | Benlysta | Ikke oppgitt | Systemisk lupus erythematosus |

Merk: Legemidlet er markedsført i Norge, og 1 av 1 godkjenninger er gyldig i de innsamlede dataene.

---

## Sikkerhetsvurderinger

**Legemiddelinteraksjoner:** Totalt 69 interaksjoner er registrert. Blant dem som er oppført i dataene:

- **Alvorlige (Major):** adalimumab, baricitinib, certolizumab pegol, levende BCG-vaksine (Tice-stammen)
- **Moderate:** roflumilast, azatioprin, alefacept, alemtuzumab, anakinra, kanakinumab, tetanustoksoid, miltbrannvaksine, adenovirusvaksine (type 4), levende kolera-vaksine, *Candida albicans*, *Bifidobacterium longum infantis*
- **Mindre (Minor):** sinkacetat, sinkglukonat, sinksulfat, sinkklorid

Hovedmønsteret er additiv immunsuppresjon ved samtidig bruk av andre biologiske og immunmodulerende midler, samt forsiktighet ved levende vaksiner.

Se preparatomtalen for øvrig sikkerhetsinformasjon.

---

## Konklusjon og neste steg

**Beslutning: Hold**

**Begrunnelse:**
Alle predikerte indikasjoner støttes kun av modellprediksjon (evidensnivå L5), uten kliniske studier eller litteratur. For de to høyest rangerte indikasjonene finnes det ingen plausibel mekanistisk kobling til BLyS-hemming. Belimumab er dessuten markedsført i Norge, med 1 gyldig godkjenning av 1.

**For å gå videre kreves følgende:**
- Data om virkningsmekanisme (MOA) fra DrugBank
- Preparatomtale med advarsler og kontraindikasjoner fra DMP, som er nødvendig for sikkerhetsscreening
- Prekliniske data eller litteraturgjennomgang, først og fremst for FNAIT som den mest biologisk sammenhengende kandidaten
- Vurdering av sikkerhet i svangerskap (placentaoverføring av IgG og effekter på føtale B-celler) dersom FNAIT følges opp
- Avklaring av markedsstatus og tilgjengelige administrasjonsveier i Norge
## Ansvarsfraskrivelse

Dette innholdet er kun til forskningsformål og utgjør ikke medisinsk rådgivning.
Klinisk validering kreves før enhver klinisk anvendelse.

---

