---
layout: default
title: Lusutrombopag
parent: Kun modellprediksjon (L5)
nav_order: 220
evidence_level: L5
indication_count: 10
---

# Lusutrombopag
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

# Lusutrombopag: Fra trombocytopeni (TPO-RA-terapi) til arvelig trombocytopeni med normale trombocytter

## Sammendrag i én setning

> Lusutrombopag er en thrombopoietin-reseptor (TPO/MPL) agonist; dens opprinnelige godkjente indikasjon er ikke dokumentert i denne evidenspakken (ingen norske lisensregistreringer finnes).
> TxGNN-modellen forutsier at det kan være effektivt for **arvelig trombocytopeni med normale trombocytter**,
> men denne prediksjonen støttes for tiden av **0 kliniske forsøk** og **0 publikasjoner** — det er en ren modellgenerert hypotese.

---

## Rask oversikt

| Element | Innhold |
|---------|---------|
| Opprinnelig indikasjon | Ikke tilgjengelig — ingen norske lisensregistreringer finnes for dette produktet |
| Forutsagt ny indikasjon | Arvelig trombocytopeni med normale trombocytter |
| TxGNN-prediksjonsscore | 99.995% (samlet rangering 88) |
| Bevisnivå | L5 |
| Norsk markedsstatus | ✗ Ikke markedsført |
| Antall godkjennelser | 0 |
| Anbefalt beslutning | Avvent |

---

## Hvorfor er denne prediksjonen rimelig?

Det strukturerte `original_moa`-feltet for dette legemidlet er for tiden et datahull (DG002, høy alvorlighetsgrad). Imidlertid identifiserer modellens egen begrunnelsestekst lusutrombopag som en **TPO-reseptor (MPL) agonist** — en legemiddelklasse som stimulerer megakaryocy tt-proliferasjon og differensiering for å øke trombocy tt-tallet.

Mekanistisk plasserer dette lusutrombopag på samme farmakologiske akse som **trombocy tt-produksjonsmangel-lidelser**. Arvelig trombocytopeni med normale trombocytter (dvs. lavt trombocy tt-tall uten ledsagende strukturelle/funksjonelle trombocy tt-defekter) er i prinsippet en plausibel utvidelse av TPO-reseptor-agonisme, siden den underliggende mangelen er kvantitativ (utilstrekkelig produksjon) i stedet for kvalitativ (defekt trombocy ttfunksjon).

Når det er sagt, er dette en genetisk/arvelig tilstand, og ingen klinisk forsøk eller publisert bevis finnes for tiden for å bekrefte effektivitet eller sikkerhet for en TPO-RA i denne spesifikke populasjonen. Koblingen bør kun behandles som en mekanistisk plausibel forskningshypotese, ikke en validert terapeutisk vei.

---

## Bevis fra kliniske forsøk

For tiden registrert ingen relaterte kliniske forsøk

---

## Litteraturbevis

Ingen relatert litteratur er for tiden tilgjengelig

---

## Norsk markedsinformasjon

Lusutrombopag har **ingen markedsføringstillatelser registrert i Norge** (`total_licenses: 0`, `market_status: Not marketed`). Ingen produkt-/lisens-tabell kan genereres fra den gjeldende evidenspakken.

---

## Sikkerhetshensyn

Vennligst se pakningsvedlegget for sikkerhetsinformasjon.

*(Merk: TFDA/etikettadvarsler, kontraindikasjoner og DDI-data er for tiden ikke tilgjengelige — merket som DG001, blokkerings-alvorlighet, i evidenspakken. Dette hullet må lukkes før noen sikkerhetsvurdering i Fase 1 kan gjennomføres.)*

---

## Konklusjon og neste trinn

**Beslutning: Avvent**

**Begrunnelse:**
Prediksjonsscore er høy, og TPO-reseptor-agonist-mekanismen gir en plausibel biologisk begrunnelse, men det finnes null klinisk forsøk eller litteraturstøtte, ingen bekreftet virkningsmekanisme-post, ingen sikkerhet/etikettdata, og legemidlet er ikke for tiden markedsført i Norge. Dette faller klart inn under bevisnivå L5 (kun modellprediksjon) og oppfyller ikke grensen for å gå videre forbi Fase 0/1.

**For å fortsette, er følgende nødvendig:**
- Løs DG001 (blokkering): få og analyser den offisielle etiketten (advarsler, kontraindikasjoner) fra relevant regulatorisk myndighet
- Løs DG002 (høy): bekreft virkningsmekanisme via DrugBank API eller primærlitteratur
- Identifiser og dokumenter legemidlets faktiske opprinnelige godkjente indikasjon(er)
- Søk etter eventuelle prekliniske eller saksnivå-bevis spesifikt for arvelig trombocytopeni (normal-trombocy tt-undertype) før du vurderer ytterligere investering
- Re-evaluer markeds-/registreringsstatus hvis kommersiell tilgjengelighet blir relevant for gjennomførbarhet

## Ansvarsfraskrivelse

Dette innholdet er kun til forskningsformål og utgjør ikke medisinsk rådgivning.
Klinisk validering kreves før enhver klinisk anvendelse.

---

