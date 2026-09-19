---
layout: default
title: Lonoctocog Alfa
parent: Kun modellprediksjon (L5)
nav_order: 214
evidence_level: L5
indication_count: 4
---

# Lonoctocog Alfa
{: .fs-9 }

Evidensnivå: **L5** | Predikerte indikasjoner: **4** stk.
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

# Lonoctocog Alfa: Fra Hemofili A til Pseudo-von Willebrand-sykdom

## Oppsummering på én setning

Lonoctocog alfa er et rekombinant single-chain Factor VIII-produkt som brukes som erstatningsterapi for hemofili A. TxGNN-modellen forutsier at det kan være effektivt for **pseudo-von Willebrand-sykdom**, men denne prediksjonen støttes av **0 kliniske studier** og **0 publikasjoner**, og den medfølgende mekanistiske analysen finner eksplisitt ingen meningsfull farmakologisk sammenheng mellom legemidlet og denne blodplate-reseptor-forstyrrelsen.

## Hurtig oversikt

| Punkt | Innhold |
|------|---------|
| Opprinnelig indikasjon | Hemofili A (Factor VIII-erstatningsterapi) — ikke inkludert i bevisematerialet selv; utledet fra legemidlets kjente klassifisering som rekombinant FVIII-produkt (DrugBank DB13998) |
| Predikert ny indikasjon | Pseudo-von Willebrand-sykdom |
| TxGNN-prediksjons-score | 99.85% |
| Bevisnivå | L5 (kun modellprediksjon, ingen støttestudier) |
| Markedsstatus i Taiwan | Ikke markedsført |
| Antall godkjenninger | 0 |
| Anbefalt beslutning | Avvent |

## Hvorfor er denne prediksjonen rimelig?

For øyeblikket er detaljerte data om virkningsmekanisme ikke tilgjengelig for lonoctocog alfa i dette bevisematerialet (flagget som et alvorlig datahull). Basert på generell farmakologisk kunnskap fungerer det som en rekombinant Factor VIII-erstatning som gjenoppretter aktiviteten til intrinsic-pathway tenase-kompleksen hos pasienter med FVIII-mangel.

Imidlertid argumenterer grunnlaget for gjenbruk oppgitt for den høyest rangerte predikerte indikasjonen direkte mot mekanistisk plausibilitet: pseudo-von Willebrand-sykdom er forårsaket av en gain-of-function-mutasjon i blodplate GPIb-reseptoren, som fører til abnormalt høy affinitet for VWF og akselerert blodplate/VWF-klarering. FVIII-nivåene er vanligvis normale ved denne tilstanden, og standard behandlingstilnærming er antiplatelet-terapi — ikke faktor-erstatning. Bevisematerialet selv sier "無機轉關聯" (ingen mekanistisk sammenheng) for denne kandidaten.

De tre andre predikerte indikasjonene i denne pakken viser samme mønster: primær blodplate-frigjøringsstilstand (granulesekresjondefekt), Glanzmanns trombasteni (GPIIb/IIIa-mangel) og Scott-syndrom (ANO6/TMEM16F phospholipid-scramblase-defekt) er alle blodplate-funktionsforstyrrelser der FVIII ikke er den manglende faktoren. Scott-syndrom har nærmest konseptuell nærhet (det påvirker fosfolipid-plattformen der FVIIIa/FIXa-komplekser monteres), men selv der konkluderer begrunnelsen at FVIII-supplementering ikke kan korrigere den underliggende defekten. Kort sagt synes de høye TxGNN-likhetsscore å være drevet av nærhet på graf-nivå i kunnskapsgrafen (alle er arvelige blødningsforstyrrelser) snarere enn av en faktisk handlingsbar mekanisme.

## Bevis fra kliniske studier

Ingen relaterte kliniske studier registrert for øyeblikket

## Bevis fra litteratur

Ingen relevant litteratur tilgjengelig for øyeblikket

## Taiwan-markedsinformasjon

Ikke markedsført i Taiwan — ingen produktgodkjenninger er registrert (total_licenses = 0).

## Sikkerhetshensyn

Vennligst referer til pakningsvedlegget for sikkerhetsinformasjon.

## Konklusjon og neste trinn

**Beslutning: Avvent**

**Begrunnelse:**
Denne kandidaten er på beslutningsstadium S0 med bevisnivå L5 — kun en TxGNN-score, med null kliniske studier, null litteratur, og en mekanistisk begrunnelse som eksplisitt tilbakeviser farmakologisk relevans for den høyest rangerte predikerte indikasjonen (pseudo-von Willebrand-sykdom er en blodplate-reseptor-forstyrrelse, ikke en FVIII-mangel). De tre neste-rangerte prediksjonene (primær blodplate-frigjøringsstilstand, Glanzmanns trombasteni, Scott-syndrom) deler samme diskvalifiserende mønster. Det er ingen grunnlag for å avansere denne kandidaten forbi innledende screening.

**For å fortsette, er følgende nødvendig:**
- Faktiske MOA-data fra DrugBank (DG002) for å ordentlig karakterisere FVIII-farmakologi
- TFDA-etikettadvarsler/kontraindikasjoner (DG001) — for øyeblikket en blokkering som forhindrer noen S1-sikkerhetsvurdering
- Enhver faktisk eller mekanistisk bevis som ville forene TxGNN-prediksjonen med den dokumenterte mangelen på farmakologisk overlap, før denne kandidaten kunne vurderes på nytt

## Ansvarsfraskrivelse

Dette innholdet er kun til forskningsformål og utgjør ikke medisinsk rådgivning.
Klinisk validering kreves før enhver klinisk anvendelse.

---

