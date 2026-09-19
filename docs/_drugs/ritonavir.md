---
layout: default
title: Ritonavir
parent: Kun modellprediksjon (L5)
nav_order: 310
evidence_level: L5
indication_count: 3
---

# Ritonavir
{: .fs-9 }

Evidensnivå: **L5** | Predikerte indikasjoner: **3** stk.
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

# Ritonavir: Fra uspesifisert originalindikasjon til felint ervervet immunsviktssyndrom

## Oppsummering i en setning

> Ritonavirs originalindikasjon og virkningsmekanisme er ikke dokumentert i denne bevispakken (merket som datagap DG001/DG002).
> TxGNN-modellen forutsier en mulig sammenheng med **felint ervervet immunsviktssyndrom** (score 99.92%),
> men dette støttes bare av **1 klinisk forsøk** — som undersøker human HIV-1, ikke felint AIDS — og **0 direkte relevante publikasjoner**.

---

## Rask oversikt

| Element | Innhold |
|---------|---------|
| Originalindikasjon | Ikke tilgjengelig i bevispakken (`original_indications: []`) |
| Forutsagt ny indikasjon | Felint ervervet immunsviktssyndrom |
| TxGNN prediksjonsresultat | 99.92% (rang 1134) |
| Bevisnivå | L5 — det eneste tilknyttede forsøket undersøker ikke den forutsagte (felinte) indikasjonen; ingen litteratur |
| Status på Taiwan-markedet | Ikke markedsført (Ikke markedsført) |
| Antall godkjennelser | 0 |
| Anbefalt beslutning | **Vente** |

---

## Hvorfor er denne prediksjonen rimelig?

For tiden er detaljerte virkningsmekanismedata ikke tilgjengelig i bevispakken (datagap **DG002**, høy alvorlighetsgrad). Legemidlets originalindikasjonhistorie er heller ikke dokumentert (`original_indications` er tom), så forholdet mellom ritonavirs etablerte bruk og den forutsagte nye indikasjonen kan ikke bekreftes fra de oppgitte dataene alene.

Særskilt er den forutsagte indikasjonen selv — felint ervervet immunsviktssyndrom — en veterinærsykdom hos katter (forårsaket av felint immunsviktsvirus, FIV), ikke en menneskelig tilstand. Det eneste kliniske forsøket som er vedlagt som støttende bevis (NCT02770508) inkluderer faktisk human HIV-1-pasienter, ikke katter med FIV-infeksjon. Dette populasjonsmisforholdet antyder at TxGNN-poengene sannsynligvis reflekterer likhetsinnebygning av kunnskapsgraf mellom lentivirale sykdomsnoder (HIV-1 ~ FIV) snarere enn direkte klinisk støtte for bruk av ritonavir ved felint AIDS. Uten bekreftet MOA-data og uten noen veterinærfarmakologisk eller doserelatert bevis, kan mekanistisk plausibilitet ikke bekreftes uavhengig her.

---

## Bevis fra kliniske forsøk

| Forsøksnummer | Fase | Status | Inklusjon | Hovedfunn |
|---------|------|------|------|---------|
| [NCT02770508](https://clinicaltrials.gov/study/NCT02770508) | Fase 4 | Fullført | 145 | Sammenlignet ritonavir-forsterket darunavir + lamivudin vs. forsterket darunavir + emtricitabin/tenofovir eller lamivudin/tenofovir hos behandlingsnaive human HIV-1-pasienter. *Merknad: dette forsøket undersøker human HIV-1, ikke felint AIDS; relevansvurdering er fortsatt merket som «avventer» i kildedata.* |

---

## Bevis fra litteratur

For tiden er ingen relevant litteratur tilgjengelig for denne forutsagte indikasjonen (felint ervervet immunsviktssyndrom).

---

## Markedsinformasjon for Taiwan

Ingen godkjenningsregistre er tilgjengelige — ritonavir er ikke for tiden markedsført på Taiwan ifølge denne bevispakken (`total_licenses: 0`).

---

## Sikkerhetshensyn

Et datagap med blokkering-alvorlighetsgrad (**DG001**) er identifisert: TFDA-pakningsvedlegg advarsler og kontraindikasjoner har ikke blitt hentet ennå, noe som betyr at denne kandidaten ikke kan gå videre til sikkerhetsforkontroll på S1 til dette er utbedret. Alle andre sikkerhetsfelt i denne bevispakken (viktige advarsler, kontraindikasjoner, legemiddel-legemiddel-interaksjoner) er ikke fylt ut (`query_status: not_found`).

Vær vennlig å referere til pakningsvedlegget for sikkerhetsinformasjon når det blir tilgjengelig.

---

## Konklusjon og neste trinn

**Beslutning: Vente**

**Begrunnelse:**
- Et blokkering datagap (DG001 — manglende TFDA-merke/-advarsler) forhindrer eksplisitt inngang til sikkerhetsforkontroll (S1).
- Den forutsagte indikasjonen er en ikke-menneskelig (felint) sykdom, og det eneste støttende kliniske forsøket undersøker faktisk ikke den indikasjonen; det generelle bevisnivået er L5.
- Legemidlet er ikke for tiden markedsført på Taiwan (0 godkjennelser), og MOA-data som er nødvendige for å vurdere mekanistisk plausibilitet mangler (DG002).

**For å fortsette er følgende nødvendig:**
- Hent TFDA-pakningsvedlegg (advarsler/kontraindikasjoner) for å lukke DG001 (Blokkering)
- Hent DrugBank MOA-data for å lukke DG002 (Høy)
- Avklar om TxGNN-prediksjonen for «felint ervervet immunsviktssyndrom» reflekterer et genuint fornyingssignal eller en tverrarts kunnskapsgrafartefakt før videre evaluering
- Fullfor relevansvurdering for avventende forsøk-/litteraturklassifikasjoner (vurder også å se på nytt rang 2, «simian immunsviktsvirus-infeksjon,» som har mer litteratur men fortsatt er en dyremodellindikasjon)

## Ansvarsfraskrivelse

Dette innholdet er kun til forskningsformål og utgjør ikke medisinsk rådgivning.
Klinisk validering kreves før enhver klinisk anvendelse.

---

