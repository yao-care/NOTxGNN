---
layout: default
title: Mometasone
parent: Kun modellprediksjon (L5)
nav_order: 234
evidence_level: L5
indication_count: 1
---

# Mometasone
{: .fs-9 }

Evidensnivå: **L5** | Predikerte indikasjoner: **1** stk.
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

# Mometason: Fra kortikosteroid-responsive dermatologiske/allergiske tilstander til primær kutanøs T-cellelymfom

## Sammendrag i én setning

> Mometason er et kortikosteroid som konvensjonelt brukes til å behandle inflammatoriske dermatologiske og allergiske tilstander (spesifikk original indikasjon er ikke registrert i denne bevissamlingen).
> TxGNN-modellen forutsier at det kan være effektivt for **Primær kutanøs T-cellelymfom**,
> men for øyeblikket er det **0 kliniske studier** og bare **2 caserapport-publikasjoner** tilgjengelig, og en av dem rapporterer faktisk behandlingssvikt med mometason i en relatert tilstand.

---

## Rask oversikt

| Punkt | Innhold |
|------|--------|
| Original indikasjon | Ikke registrert i bevissamlingen (ingen `original_indications` eller Norges lisenstekst tilgjengelig); mometason er generelt klassifisert som et kortikosteroid |
| Forutsagt ny indikasjon | Primær kutanøs T-cellelymfom |
| TxGNN-prediksjonsscore | 99.36% |
| Bevisnivå | L5 (modellprediksjon bare — ingen direkte støttende studier) |
| Norges markedsstatus | ✗ Ikke markedsført |
| Antall godkjennelser | 0 |
| Anbefalt beslutning | Avvent |

---

## Hvorfor er denne prediksjonen rimelig?

For øyeblikket er detaljerte data om virkningsmekanisme ikke tilgjengelig for dette legemidlet i bevissamlingen. Basert på generell farmakologisk kunnskap er mometason et kortikosteroid med anti-inflammatoriske og immunosuppressive egenskaper, som vanlig brukes for inflammatoriske hud- og allergiske/respiratoriske tilstander. En plausibel mekanistisk begrunnelse for bruken ved kutanøs T-cellelymfom (CTCL) er at topikale kortikosteroider kan undertrykke kutanøs lymfocyttinfiltrasjon og inflammasjon, som er en del av standard støttende/tilleggsbehandling i tidligstadium mycosis fungoides (en form for CTCL).

Imidlertid gir de to litteraturelementene som ble hentet for denne prediksjonen ikke direkte positiv støtte: ett beskriver et tilfelle av kutanøs pseudolymfom (en *etterligner* av CTCL, ikke CTCL selv) der mometasonbehandling var **mislykket**, og det andre er en pediatrisk mycosis fungoides caserapport hvis sammendrag ikke nevner mometason i det hele tatt. Dette betyr at modellens høye score for øyeblikket ikke støttes av direkte klinisk bevis — assosiasjonen ser ut til å være drevet av nettverks-/embedding-likhet snarere enn dokumentert effektivitet.

---

## Klinisk studiebevis

For øyeblikket ingen relaterte kliniske studier registrert.

---

## Litteraturbevis

| PMID | År | Type | Tidsskrift | Viktige funn |
|------|-----|------|--------|--------------|
| [40821495](https://pubmed.ncbi.nlm.nih.gov/40821495/) | 2025 | Caserapport | Proceedings (Baylor University Medical Center) | Kutanøs pseudolymfom (en CTCL-etterligner) på nesen; **både mometason og takrolimus var mislykket**; tilfelle behandlet til slutt med tapinarof |
| [25442255](https://pubmed.ncbi.nlm.nih.gov/25442255/) | 2015 | Caserapport | Journal of Cutaneous Pathology | Pediatrisk (11 år gammel) CD8+CD56+ mycosis fungoides (en primær CTCL-subtype); sammendrag nevner ikke mometasonbehandling |

⚠️ Ingen av publikasjonene demonstrerer effektivitet av mometason for primær kutanøs T-cellelymfom; den ene dokumenterer eksplisitt behandlingssvikt i en relatert men distinkt diagnose.

---

## Markeds informasjon for Norge

Mometason er for øyeblikket **ikke markedsført** i Norge under denne bevissamlingen (`market_status: Not marketed`, 0 godkjennelser på fil). Ingen produktlisensrekorder er tilgjengelig.

---

## Sikkerhetshensyn

Se pakningsvedlegget for sikkerhetsinformasjon.

*(Merk: TFDA-etikettadvarsler/kontraindikasjoner og legemiddel-legemiddel-interaksjonsdata er oppført som datahull (DG001, blokkerende alvorlighetsgrad) i bevissamlingens metadelseksjon og må løses før noen klinisk sikkerhetsvurdering.)*

---

## Konklusjon og neste trinn

**Beslutning: Avvent**

**Begrunnelse:**
Til tross for en høy TxGNN-prediksjonsscore er det ingen klinisk studiebevis og de eneste to litteraturhenvisningene støtter ikke — og i ett tilfelle motsier — effektivitet for denne indikasjonen. Kombinert med manglende MOA-data og et blokkerende gap i TFDA sikkerhet/etikett-informasjon, oppfyller denne kandidaten ennå ikke terskelen for videre evaluering.

**For å fortsette kreves følgende:**
- Løse DG001 (TFDA-etikettadvarsler/kontraindikasjoner) — blokkerer for øyeblikket sikkerhetsvurdering
- Løse DG002 (virkningsmekanisme) via DrugBank for å vurdere mekanistisk plausibilitet for CTCL
- Identifisere litteratur eller prekliniske studier som spesifikt evaluerer kortikosteroider (mometason eller klasse) ved primær kutanøs T-cellelymfom/mycosis fungoides, i stedet for tangensielle caserapporter
- Revurdere om de to hentede caserapportene er genuint relevante, gitt at den ene viser behandlingssvikt i en differensialdiagnose-tilstand

## Ansvarsfraskrivelse

Dette innholdet er kun til forskningsformål og utgjør ikke medisinsk rådgivning.
Klinisk validering kreves før enhver klinisk anvendelse.

---

