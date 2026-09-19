---
layout: default
title: Ravulizumab
parent: Kun modellprediksjon (L5)
nav_order: 298
evidence_level: L5
indication_count: 10
---

# Ravulizumab
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

# Ravulizumab: Fra komplement-mediert sykdom til medfødt nøytropeni (G6PC3-mangel)

## Sammendrag i en setning

> Ravulizumab er en langtidsvirkende terminal komplementinhibitor (C5); dens opprinnelige godkjente indikasjon er ikke tilgjengelig i det nåværende datasettet.
> TxGNN-modellen forutsier at det kan være effektivt for **autosomalt recessiv alvorlig medfødt nøytropeni på grunn av G6PC3-mangel**,
> men denne prediksjonen støttes for tiden av **0 kliniske studier** og **0 publikasjoner** — bevis hviler helt på modellens embedding-space-likhet, og bevismaterialet selv markerer den mekanistiske begrunnelsen som sannsynlig usann.

---

## Rask oversikt

| Element | Innhold |
|---------|---------|
| Opprinnelig indikasjon | Ikke tilgjengelig i nåværende datasett (ingen godkjent indikasjon i norske regulatoriske registre) |
| Forutsagt ny indikasjon | Autosomalt recessiv alvorlig medfødt nøytropeni på grunn av G6PC3-mangel |
| TxGNN-prediksjonscore | 99.96% |
| Bevisnivå | L5 |
| Status på det norske markedet | ✗ Ikke markedsført |
| Antall godkjennelser | 0 |
| Anbefalt beslutning | Avvent |

---

## Hvorfor er denne prediksjonen rimelig?

For tiden er detaljerte mekanismedata ikke tilgjengelige i det strukturerte MOA-feltet. Imidlertid beskriver bevismaterialet sitt eget gjenbruksrationale ravulizumab som en langtidsvirkende C5-komplementinhibitor (et derivat av eculizumab), hvilket betyr at dens virkningsmåte blokkerer terminal komplementkaskade (C5-kløyvning → C5a/C5b-9-dannelse).

Den forutsagte indikasjonen — medfødt nøytropeni på grunn av G6PC3-mangel — drives av endoplasmatisk retikulum-stress og apoptose i nøytrofil-prekursorer, en mekanisme som er forankret i glykogen-/glukosemetabolisme heller enn komplementaktivering. Ifølge bevismaterialet sitt eget mekanistiske vurdering, **finnes det ingen kjent direkte biologisk sammenheng mellom C5-komplementbanen og G6PC3-mangel-nøytropeni**. Den høye TxGNN-scoren reflekterer sannsynligvis embedding-space-likhet på tvers av en klynge av nøytrofil-relaterte sykdommer i kunnskapsgrafen, heller enn en genulin, validert mekanistisk forbindelse.

Denne forbehold er konsistent på tvers av de andre topprankede prediksjonen i dette bevismaterialet (syklisk hematopoiese, CXCR2-deficient nøytropeni, X-linked SCN) — alle er nøytrofil-/hematopoietiske lidelser med distinkte, ikke-komplement-drevne etiologier, noe som forsterker at modellen kan gruppere på fenotypisk likhet (nøytropeni) heller enn delt legemiddel-målbiologi.

---

## Bevis fra kliniske studier

For tiden ingen relevante kliniske studier registrert

---

## Bevis fra litteratur

For tiden ingen relevant litteratur tilgjengelig

---

## Informasjon om det norske marked

Ravulizumab er ikke for tiden markedsført i Norge, og ingen godkjennelsesregistre er tilgjengelige i datasettet.

---

## Sikkerhetshensyn

Vennligst se pakningsvedlegget for sikkerhetsinformasjon.

*Merk: TFDA-merkingadvarsler/kontraindikasjoner (DG001) er markert som en **kritisk** datagap i bevismaterialet — dette legemidlet kan ikke gå videre til sikkerhet før-vurdering (S1) inntil disse dataene er innhentet.*

---

## Konklusjon og neste trinn

**Beslutning: Avvent**

**Begrunnelse:**
Denne prediksjonen støttes kun av en L5-modelscore (rangering 731/~, ingen kliniske studier, ingen litteratur), og bevismaterialet sitt eget mekanistiske analyse stiller eksplisitt spørsmål ved den biologiske plausibilitet av C5-banen/G6PC3-nøytropeni-koblingen, og tilskriver den høye scoren til sykdoms-embedding-likhet heller enn genulin målrelevans. Kombinert med en kritisk datagap på TFDA-sikkerhetsmerkingen, oppfyller denne kandidaten ikke terskelen for å avansere forbi S0.

**For å fortsette, trengs følgende:**
- Strukturerte MOA-data fra DrugBank/merkingskjelder (for tiden en datagap med høy alvorlighetsgrad, DG001/DG002)
- TFDA/regulatorisk merking (advarsler, kontraindikasjoner) for å muliggjøre sikkerhet før-vurdering (S1) (kritisk datagap)
- Uavhengig litteratur eller preklinisk bevis som direkte knytter komplement C5-aktivitet til G6PC3-mangel nøytrofil-patologi
- Bekreftelse av legemidlets faktiske opprinnelige godkjente indikasjon(er), som for tiden mangler i regulatoriske registre

## Ansvarsfraskrivelse

Dette innholdet er kun til forskningsformål og utgjør ikke medisinsk rådgivning.
Klinisk validering kreves før enhver klinisk anvendelse.

---

