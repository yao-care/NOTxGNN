---
layout: default
title: Rasburicase
parent: Kun modellprediksjon (L5)
nav_order: 297
evidence_level: L5
indication_count: 10
---

# Rasburicase
{: .fs-9 }

Evidensnivå: **L5** | Predikerte indikasjoner: **10** stk.
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

# Rasburicase: Fra tumørlysesyndrommodassosiiert hyperurikemi til nyrerelatert hypourikemi

## Oppsummering i én setning

Rasburicase er et rekombinant uratoksidase brukt til å håndtere hyperurikemi assosiert med tumørlysesyndom. TxGNN-modellens toppprediksjon er **nyrerelatert hypourikemi**, men denne kandidaten har **null kliniske forsøk og null publikasjoner** som støtter den, og er mekanistisk inkonsistent med legemidlets kjente farmakologi — måltilstanden er en sykdom med *abnormalt lavt* urinsyre, mens Rasburicases kjente effekt er å *senke* urinsyre ytterligere.

---

## Rask oversikt

| Element | Innhold |
|---------|---------|
| Opprinnelig indikasjon | Tumørlysesyndrommodassosiiert hyperurikemi (fra kjent farmakologi; ingen norsk lisensieringsrekord tilgjengelig) |
| Predikert ny indikasjon | Nyrerelatert hypourikemi |
| TxGNN-prediksjonspoengsum | 99.99% |
| Bevisnivå | L5 |
| Norsk markedsstatus | ✗ Ikke markedsført |
| Antall autorisasjoner | 0 |
| Anbefalt beslutning | Vent |

---

## Hvorfor er denne prediksjonen rimelig?

Formale strukturerte data om virkningsmodus (MOA) er for øyeblikket et datakløft (DG002). Basert på farmakologisk beskrivelse tilgjengelig i bevissamlingen, er Rasburicase et rekombinant uratoksidase (urikase)-enzym som katalyserer oksidasjon av urinsyre til allantion, og derved **senker** serum urinsyre-konsentrasjonen. Det er klinisk brukt til å håndtere hyperurikemi assosiert med tumørlysesyndom hos onkologipasienter.

Den topprangerte TxGNN-kandidaten, nyrerelatert hypourikemi, er en tilstand karakterisert ved **abnormalt lavt** serum urinsyre, typisk forårsaket av defekt renale uratreabsorpsjon (f.eks. URAT1/GLUT9-transportørdysfunksjon). Dette er farmakologisk **motsatt** i retning av Rasburicases kjente urinsyrereduserende effekt — det er ingen plausibel klinisk begrunnelse for å administrere et urinsyrereduserende enzym til en pasient som allerede har patologisk lavt urinsyre. Denne mekanistiske motsigelsen er eksplisitt flagget i selve bevissamlingen.

Den høye TxGNN-scoren gjenspeiler sannsynligvis nærhet i grafinnbygging mellom urinsyre/purinmetabolisme-relaterte gener og veier i kunnskapsgrafen, snarere enn et genuint behandlingsforhold. Blant de 10 kandidatene i denne bevissamlingen, har rang #2 (partiell mangel på hypoxantin-guanin fosforibosyltransferase / Kelley-Seegmiller-syndrom) en mer biokjemisk sammenhengende begrunnelse, siden denne tilstanden forårsaker purinbane-drevet *hyperurikemi* — retningen Rasburicase faktisk er kjent for å behandle. Imidlertid har det også for øyeblikket ingen støttende kliniske forsøk eller litteratur.

---

## Bevis fra kliniske forsøk

For øyeblikket ingen relaterte kliniske forsøk registrert

---

## Bevis fra litteratur

For øyeblikket ingen relatert litteratur tilgjengelig

---

## Informasjon om norsk marked

Rasburicase er **ikke markedsført** i Norge; ingen produktautorisasjonsrekorder er tilgjengelige (0 lisenser på fil).

---

## Sikkerhetshensyn

Vennligst se pakningsvedlegget for sikkerhetsinformasjon.

---

## Konklusjon og neste steg

**Beslutning: Vent**

**Begrunnelse:**
Dette er en ren modellprediksjon (L5) uten støtte fra kliniske forsøk eller litteratur, og den topprangerte kandidatindikasjonen er mekanistisk implausibel — den reverserer retningen på Rasburicases kjente farmakologiske effekt. Det er utilstrekkelig grunnlag for å ta denne kandidaten videre.

**For å fortsette, kreves følgende:**
- TFDA/regulatorisk pakningsvedlegg-advarsler og kontraindikasjoner (DG001, **Blokkering** — forhindrer for tiden oppstart av S1-sikkerhetsvurdering)
- Strukturerte data om virkningsmodus (MOA) og DrugBank-kategoridata (DG002, høy alvorlighetsgrad)
- Uavhengig biokjemisk/preklinisk validering av et mekanistisk sammenhengende mål — rang #2 (HGPRT partiell mangel) fortjener nærmere gransking før rang #1
- Hvis forfølgt, en norsk regulatorisk bane-vurdering, siden legemidlet for øyeblikket ikke har noen lokal markedsautorisasjon

## Ansvarsfraskrivelse

Dette innholdet er kun til forskningsformål og utgjør ikke medisinsk rådgivning.
Klinisk validering kreves før enhver klinisk anvendelse.

---

