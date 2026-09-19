---
layout: default
title: Turoctocog Alfa
parent: Kun modellprediksjon (L5)
nav_order: 373
evidence_level: L5
indication_count: 10
---

# Turoctocog Alfa
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

# Turoctocog alfa: Fra faktor VIII-erstatning til primær utgivelsesforstyrring av blodplater

## Sammenfatting i en setning

Turoctocog alfa er et rekombinant faktor VIII-produkt (FVIII); ifølge bevisepakkens egne mekanistiske merknader er dens etablerte terapeutiske rolle faktor VIII-erstatning (f.eks. faktor VIII-mangel/hemofili A), selv om denne bevisepakken ikke inneholder bekreftet originalindikasjon eller virkningsmekanismedata. TxGNNs toppprediksjon er **Primær utgivelsesforstyrring av blodplater**, men **0 kliniske forsøk** og **0 publikasjoner** støtter foreløpig denne retningen, og modellens egen begrunnelse angir at den mekanistiske koblingen er svak (en blodplategranuløs utgivelsesdefekt, ikke en koagulasjonsfaktor-veibanedefekt).

---

## Rask oversikt

| Element | Innhold |
|---------|---------|
| Original indikasjon | Ikke spesifisert i bevisepakken (datakløft). Rasjonalitetsmerknader beskriver stoffet som rekombinant FVIII, vanligvis brukt for faktor VIII-mangel (hemofili A) |
| Predikert ny indikasjon | Primær utgivelsesforstyrring av blodplater |
| TxGNN-prediksjonsscore | 99.99% |
| Bevisnivå | L5 |
| Norsk markedsstatus | Ikke markedsført (Ikke markedsført) |
| Antall godkjennelser | 0 |
| Anbefalt beslutning | Hold |

---

## Hvorfor er denne prediksjonen rimelig?

Foreløpig er det ikke tilgjengelig detaljert virkningsmekanismedata for turoctocog alfa i denne bevisepakken (virkningsmekanisme = datakløft). Basert på de mekanistiske rasjonalitetsmerknader som er knyttet til hver prediksjon, forstås stoffet som et rekombinant faktor VIII-erstatningsprodukt (FVIII), hvis etablert farmakologi opererer i sekundær hemostase-veibanen (trombingenerering).

Den topprankede predikerte indikasjonen, primær utgivelsesforstyrring av blodplater, innebærer en defekt i blodplategranuløs utgivelse — en **primær hemostase**-mekanisme som ikke har noe å gjøre med koagulasjonsfaktor-kaskaden som FVIII virker på. Bevisepakkens egen `repurposing_rationale.mechanistic_link`-felt angir dette eksplisitt: *"為血小板顆粒釋放機制缺陷，非凝血因子路徑異常，FVIII 補充無直接治療機轉"* (en blodplategranuløs utgivelsesdefekt, ikke en koagulasjonsfaktor-veibaneanomali; FVIII-supplemenering har ingen direkte terapeutisk mekanisme).

Dette er et viktig forbehold: til tross for en meget høy TxGNN-likhetscore (99.99%), argumenterer den mekanistiske merknad for denne spesifikke prediksjonen **mot** biologisk plausibilitet snarere enn for den. Dette mønsteret gjentas over de fleste av de 10 beste prediksjoner for dette stoffet (se nedenfor) — flere er blodplate-funksjon eller blodplate-antall-forstyrrelser som ikke er relatert til FVIII-veibanen, og en (trombotisk trombocytopeni purpura) er flagget som en potensiell **sikkerhetsbetenkeligiet i motsatt retning** (FVIII/vWF-veibanen er patologisk forhøyet i TTP; ytterligere FVIII-supplemenering kunne teoretisk forverring trombotisk risiko). Bare rangering 5 (ervervet koagulasjonsfaktor-mangel) viser en plausibel mekanistisk overlapping, og selv det er kvalifisert som svakt på grunn av den typiske tilstedeværelsen av FVIII-inhibitorer i denne befolkningen, der omgåelsesmidler snarere enn FVIII-erstatning er standardbehandling.

---

## Klinisk forsøksbevis

Foreløpig ingen relaterte kliniske forsøk registrert

---

## Litteraturbevis

Foreløpig ingen relatert litteratur tilgjengelig

---

## Norsk markedsinformasjon

Dette stoffet er foreløpig ikke markedsført i Norge (Ikke markedsført); ingen autorisasjonsjournaler er tilgjengelig i bevisepakken.

---

## Andre predikerte indikasjoner (ikke prioritert)

For transparens er de gjenværende 10 beste TxGNN-prediksjoner og deres mekanistiske begrunnelse oppsummert nedenfor. Alle bærer bevisnivå L5 (modellprediksjon bare) uten støttende forsøk eller litteratur, og alle er scoret «Hold».

| Rangering | Predikert indikasjon | Score | Mekanistisk vurdering (per bevisepakken) |
|-----------|---------------------|-------|------------------------------------------|
| 2 | Pseudo-von Willebrand-sykdom | 99.99% | Blodplate GPIbα gain-of-function-defekt, ikke FVIII/vWF-mangel — svak kobling |
| 3 | Glanzmann-trombasteni | 99.99% | Blodplate GPIIb/IIIa-reseptor-defekt, ikke koagulasjonsfaktor-mangel — ikke relatert |
| 4 | Scott-syndrom | 99.95% | Blodplate-membranscramblase-defekt, ikke FVIII-mangel — ikke relatert |
| 5 | Ervervet koagulasjonsfaktor-mangel | 99.95% | Plausibel overlapping med ervervet hemofili A, men inhibitorer krever vanligvis omgåelsesmidler snarere enn kun FVIII — moderat men ubekreftet |
| 6 | Blødningsforstyrring på grunn av kollagenreseptor-defekt | 99.91% | Blodplate GPVI (primær hemostase) defekt, forskjellig fra FVIII-rolle i sekundær hemostase — ikke relatert |
| 7 | Blødningsforstyrring på grunn av konstitusjonell trombocytopeni | 99.91% | Blodplate-antall/produksjon-defekt; FVIII påvirker ikke blodplate-generering — ikke relatert |
| 8 | «Flood-faktor-mangel» | 99.61% | Sykdomsetikett uklar/mulig databasenavngvingsgjenstand; intet grunnlag for mekanistisk vurdering |
| 9 | Trombotisk trombocytopeni purpura | 99.54% | FVIII/vWF-akse allerede patologisk forhøyet i TTP; ytterligere FVIII kunne teoretisk forverring trombotisk risiko — potensielt sikkerhetsbetenkeligiet |
| 10 | Arvelig trombocytose med tversgående lemdefekt | 99.52% | Sjelden medfødt syndrom knyttet til hematopoetiske/skjelettgener, ikke FVIII-veibane — ikke relatert |

---

## Sikkerhetshensyn

Vennligst se pakningsvedlegget for sikkerhetsinformasjon.

---

## Konklusjon og neste trinn

**Beslutning: Hold**

**Begrunnelse:**
Alle 10 topprankede prediksjoner er bevisnivå L5 (modellprediksjon bare), uten støttende kliniske forsøk eller litteratur. Enda viktigere argumenterer bevisepakkens egen mekanistiske begrunnelse mot biologisk plausibilitet for 8 av de 10 kandidater (blodplate-funksjon/antall-forstyrrelser som ikke er relatert til FVIII-koagulasjonveibanen), og flagger en kandidat (TTP) som en potensiell sikkerhetsbetenkeligiet i motsatt terapeutisk retning.

**For å fortsette kreves følgende:**
- TFDA/regulatorisk merkdata (advarsler, kontraindikasjoner) — foreløpig en blokkerande datakløft (DG001)
- Bekreftet originalindikasjon og virkningsmekanisme for turoctocog alfa (DG002)
- Hvis man forfølger rangering 5 (ervervet koagulasjonsfaktor-mangel) som den mest mekanistisk plausible kandidaten, dedikert litteratur/forsøkssøk spesifikk for ervervet hemofili A og inhibitorstatus
- Uavhengig farmakologisk gjennomgang før noen videre evalueringsstadium, gitt den selvmotsigende naturen til det nåværende prediksjonssettet

## Ansvarsfraskrivelse

Dette innholdet er kun til forskningsformål og utgjør ikke medisinsk rådgivning.
Klinisk validering kreves før enhver klinisk anvendelse.

---

