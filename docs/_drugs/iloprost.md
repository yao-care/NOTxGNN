---
layout: default
title: Iloprost
parent: Kun modellprediksjon (L5)
nav_order: 176
evidence_level: L5
indication_count: 9
---

# Iloprost
{: .fs-9 }

Evidensnivå: **L5** | Predikerte indikasjoner: **9** stk.
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

# Iloprost: Fra Pulmonal Arteriell Hypertensjon til Hypotrichosis Simplex av Hodebunnen

## Sammendrag på en Setning

> Iloprost er en syntetisk prostacyclin-analogue (PGI2) med veletablert global bruk i pulmonal arteriell hypertensjon (PAH); det har aldri blitt markedsført i Taiwan.
> TxGNN-modellens høyest rangerte prediksjon er **Hypotrichosis Simplex av Hodebunnen**, en arvelig follikulær keratiniseringssykdom,
> men dette signalet støttes av **0 kliniske forsøk** og **0 publikasjoner** — det er et rent modellinnebygd artefakt uten biologisk begrunnelse.
> Separat flagget denne kjøringen også flere biologisk konsistente PAH-undertype-utvidelser (se «Andre Kandidatindikasjoner» nedenfor) som fortjener uavhengig evaluering.

## Rask Oversikt

| Element | Innhold |
|---------|---------|
| Original Indikasjon | Ikke registrert i Taiwan-bevispaket (medisin ikke markedsført, 0 lisenser); internasjonalt er iloprost indisert for pulmonal arteriell hypertensjon (WHO-gruppe 1) |
| Forutsagt Ny Indikasjon | Hypotrichosis Simplex av Hodebunnen |
| TxGNN-prediksjonspoeng | 99.45% |
| Bevisnivå | L5 |
| Taiwan-markedsstatus | ✗ Ikke Markedsført (Ikke markedsført) |
| Antall Autorisasjoner | 0 |
| Anbefalt Beslutning | Avvent |

## Hvorfor er denne prediksjonen rimelig?

For tiden er detaljerte data om virkningsmekanisme ikke tilgjengelige (datakløft DG002 — MOA avventer DrugBank-spørring). Basert på kjent farmakologisk informasjon aktiverer iloprost prostacyclin IP-reseptor/cAMP-veien, noe som produserer vasodilatation og hemming av plateletaggregering. Klinisk ligger denne mekanismen til grunn for dets etablerte bruk (utenfor Taiwan) i pulmonal arteriell hypertensjon og, i noen markeder, kritisk lemiskkemi.

Hypotrichosis simplex av hodebunnen er en arvelig sykdom av hårfollikkelkeratinisering, assosiert med gener som *APCDD1*, og dens patologi er ikke relatert til vaskulær tone eller blodplatesfunksjon. Det er ingen kjent vei som forbinder PGI2/IP-reseptor-signalering til denne tilstanden. Dette gjenspeiles direkte i modellens egen begrunnelse, som sier at lenken er basert rent på innebygd likhet med «ingen biologisk støtte».

Verdt å merke seg, denne samme TxGNN-kjøringen predikerte også flere pulmonal-arteriell-hypertensjon-undertyper for iloprost (assosiert med medfødt hjertesykdom, bindevevssykdom, HIV-infeksjon, kronisk hemolytisk anemi og schistosomiasis) — alle mekanistisk konsistente med iloprosts kjente PGI2-farmakologi og, i noen tilfeller, støttet av fullførte fase 3-forsøksdata. Disse representerer vesentlig sterkere gjenbrukssignaler enn hypotrichosis-prediksjonen med høyest rangering (se «Andre Kandidatindikasjoner» nedenfor).

## Bevis fra Kliniske Forsøk

For tiden ingen relaterte kliniske forsøk registrert.

## Litteraturbevis

For tiden ingen relatert litteratur tilgjengelig.

## Taiwan-markedsinformasjon

Iloprost er ikke markedsført i Taiwan for tiden. Ingen produktautoriseringer er registrert (0 lisenser).

## Andre Kandidatindikasjoner (Samme Modellkjøring)

For kontekst scoret det samme bevispaket 8 ytterligere TxGNN-prediksjoner for iloprost. I motsetning til hypotrichosis faller de fleste av disse innenfor iloprosts veletablerte PAH-farmakologi og har vesentlig sterkere bevis:

| Rangering | Sykdom | TxGNN-poeng | Bevisnivå | Anbefaling | Viktig Støtte |
|-----------|--------|------------|---------|----------|-------------|
| 6 | PAH forbundet med HIV-infeksjon | 99.21% | L1 | Fortsett med Sikkerhetstiltak | Fullført fase 3 dobbeltblindet, placebokontrollert crossover-RCT (NCT00709956, n=64) |
| 3 | PAH forbundet med medfødt hjertesykdom | 99.32% | L2 | Fortsett med Sikkerhetstiltak | 1 forsøk (NCT01383083, n=42, status ukjent) + 17 støttende publikasjoner |
| 5 | PAH forbundet med bindevevssykdom | 99.21% | L2 | Fortsett med Sikkerhetstiltak | Langtids IV iloprost kohortedata (PMID 27651181) + 20 støttende publikasjoner |
| 7 | PAH forbundet med kronisk hemolytisk anemi | 99.21% | L4 | Forskningsspørsmål | Kun mekanistisk plausibilitet, ingen direkte bevis |
| 8 | PAH forbundet med schistosomiasis | 99.21% | L4 | Forskningsspørsmål | 1 indirekte pediatrisk kasusserie |
| 4 | Pulmonal arteriovenøs malformasjon | 99.31% | L4 | Avvent | 1 indirekte HHT-relatert kasurapport |
| 2 | Medfødt hypotrichosis milia | 99.33% | L5 | Avvent | Ingen bevis, ingen mekanistisk lenke |
| 9 | Diffus alopecia areata | 99.10% | L5 | Avvent | Ingen bevis, ingen mekanistisk lenke |

Hvis man forfølger gjenbruk for iloprost, anbefaler vi å omdirigere evalueringen mot **PAH forbundet med HIV-infeksjon** (rangering 6, L1) som den primære kandidaten, med medfødt-hjertesykdom-PAH og bindevevssykdom-PAH (rangering 3 & 5, L2) som sekundære kandidater.

## Sikkerhetshensyn

Vennligst se pakningsvedlegget for sikkerhetsinformasjon.

## Konklusjon og Neste Steg

**Beslutning: Avvent**

**Begrunnelse:**
Prediksjonen med høyest rangering, hypotrichosis simplex av hodebunnen, har ingen støttende kliniske forsøk, ingen støttende litteratur og ingen kjent biologisk mekanisme som forbinder iloprosts prostacyclin-vei til denne arvelige follikulære sykdommen — dette er et rent modelllikheitsartefakt, ikke et troverdig gjenbrukssignal.

**For å fortsette, er følgende nødvendig:**
- TFDA-merking advarsler/kontraindikasjoner data (DG001, blokkerer — kreves før enhver S1-sikkerhetskontroll)
- Bekreftet virkningsmekanisme fra DrugBank (DG002)
- Hvis gjenbruksinteresse fortsetter, omdefiner evalueringen til PAH-undertype-kandidatene identifisert ovenfor (særlig HIV-assosiert PAH, L1-bevis), snarere enn hypotrichosis simplex

## Ansvarsfraskrivelse

Dette innholdet er kun til forskningsformål og utgjør ikke medisinsk rådgivning.
Klinisk validering kreves før enhver klinisk anvendelse.

---

