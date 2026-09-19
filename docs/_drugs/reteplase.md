---
layout: default
title: Reteplase
parent: Kun modellprediksjon (L5)
nav_order: 303
evidence_level: L5
indication_count: 10
---

# Reteplase
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

# Reteplase: Fra akutt myokardialinfarkst til posteroinferior myokardialinfarkst

## Sammendrag i én setning

Reteplase (rekombinant plasminogenaktivator, DB00015) er et etablert trombolitikum som brukes for akutt myokardialinfarkst, bekreftet av flere forsøk i denne evidenspakken (f.eks. GUSTO-V, SPEED/GUSTO-4).
TxGNN-modellen forutsier at det også kan være effektivt for den anatomisk distinkte subtypien **posteroinferior myokardialinfarkst**,
men denne spesifikke prediksjonen støttes for øyeblikket av **0 kliniske forsøk** og **0 publikasjoner** — det er en ren modellforutsigelse (L5).

## Hurtig oversikt

| Element | Innhold |
|---------|---------|
| Original indikasjon | Akutt myokardialinfarkst (trombolitisk terapi) — utledet fra sitatforsøk/litteraturkontekst; ingen norsk godkjenningsjournal tilgjengelig |
| Forutsagt ny indikasjon | Posteroinferior myokardialinfarkst |
| TxGNN prediksjonsresultat | 99.90% |
| Evidensnivå | L5 |
| Markedsstatus Norge | ✗ Ikke markedsført |
| Antall godkjennelser | 0 |
| Anbefalt beslutning | Utsett |

## Hvorfor er denne prediksjonen fornuftig?

For øyeblikket er detaljert virkningsmekanisme-data ikke tilgjengelig (datakløft DG002). Basert på informasjon som er innebygd i evidenspakken, er reteplase en rekombinant vevs-plasminogenaktivator (også referert til som BM 06.022), et trombolitikum som løser opp koronartrombuser. Effektiviteten ved akutt myokardialinfarkst — den generelle tilstanden — har blitt demonstrert over flere store forsøk (f.eks. NCT00046228, PMID 11079647, PMID 15800019), som alle omfattet reteplase for akutt MI i ulike kliniske innstillinger.

Posteroinferior myokardialinfarkst er en anatomisk lokaliserings-subtype av akutt MI, ikke en distinkt sykdom med annen patofysiologi. Siden reteplase allerede løser opp den årsaksgivende koronartrombosen uavhengig av infarktplassering, er den mekanistiske begrunnelsen for denne "nye" indikasjonen sterkt i prinsippet. Imidlertid gjenspeiler den meget høye TxGNN-poengsum sannsynligvis sykdomsontologi-granularitet (et lokaliserings-spesifikt ICD/ontologi-term nestet under en bredere indikasjon allerede behandlet med legemidlet) snarere enn en genuint ny terapihypotese — derfor eksisterer det ingen dedikerte forsøk eller litteratur for denne spesifikke subtypien.

## Klinisk forsøksevidens

Ingen relaterte kliniske forsøk er for øyeblikket registrert.

## Litteratursevidens

Ingen relatert litteratur er for øyeblikket tilgjengelig.

## Markedsinformasjon Norge

Reteplase er for øyeblikket **ikke markedsført** i Norge. Ingen godkjenningsjournal (0 godkjennelser) er tilgjengelig i evidenspakken, så ingen dosering eller godkjent indikasjonstekst kan ekstraheres.

## Sikkerhetshensyn

Se pakningsinformasjonen for sikkerhetsinformasjon.

> Merk: TFDA/Norge merkingsadvarsler og kontraindikasjoner (DG001) er markert som en **blokkering** datakløft i denne evidenspakken — dette forhindrer formell S1 sikkerhetsscreening for denne kandidaten.

## Konklusjon og neste steg

**Beslutning: Utsett**

**Begrunnelse:**
Den topprangerte forutsagte indikasjonen (posteroinferior MI) har ingen støttende kliniske forsøk eller litteratur — det er evidensnivå L5 (bare modellforutsigelse). Kombinert med datakløften i TFDA sikkerhet/merking-data, kan denne kandidaten ikke gå videre forbi S0/S1-gjennomgang på dette tidspunktet.

**For å gå videre, er følgende nødvendig:**
- TFDA/Norge pakningsinformasjon (advarsler, kontraindikasjoner) — for øyeblikket blokkering (DG001)
- Bekreftet virkningsmekanisme-data fra DrugBank (DG002)
- Subtype-spesifikk (posteroinferior MI) forsøks- eller registerdata, hvis de finnes utenfor PubMed/ClinicalTrials.gov
- **Vurder å re-evaluere denne kandidatprofilen ved bruk av en bedre-evidensiert forutsagt indikasjon fra samme pakke**: rangering 3 "septalt myokardialinfarkst" (L2, ett fullført fase 3-RCT — NCT00046228) eller rangering 5 "koronarstenose" (L3, seks støttende publikasjoner inkludert data fra fasilitert PCI kohort) viser vesentlig sterkere evidensgrunnlag innenfor denne samme legemiddelets prediksjonsresultat.

## Ansvarsfraskrivelse

Dette innholdet er kun til forskningsformål og utgjør ikke medisinsk rådgivning.
Klinisk validering kreves før enhver klinisk anvendelse.

---

