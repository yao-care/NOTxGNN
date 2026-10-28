---
layout: default
title: Brodalumab
parent: Kun modellprediksjon (L5)
nav_order: 67
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-28
description: "Brodalumab: predikert ny indikasjon Strongyloidiasis (evidensnivå L5). Opprinnelig indikasjon: Psoriasis"
monitor_inn: "BRODALUMAB"
predicted_indications: ["strongyloidiasis", "eye disease", "vitamin deficiency disorder", "von Hippel anomaly", "optic perineuritis", "chronic relapsing inflammatory optic neuropathy", "isolated optic neuritis", "recurrent idiopathic neuroretinitis", "nodular episcleritis", "episcleritis periodica fugax"]
---

# Brodalumab
{: .fs-9 }

Evidensnivå: **L5** | Predikerte indikasjoner: **10** stk.
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

## Brodalumab: Fra psoriasis til strongyloidiasis
{: .text-alpha }

## Oppsummering i én setning

Brodalumab er et monoklonalt antistoff mot IL-17-reseptor A, opprinnelig godkjent for behandling av psoriasis.
TxGNN-modellen predikerer at det kan være virksomt mot **strongyloidiasis**, men det finnes **ingen kliniske studier** og **ingen publikasjoner** som støtter denne retningen.
Prediksjonen er kun modellbasert, og biologisk begrunnelse taler snarere mot den.

---

## Hurtigoversikt

| Punkt | Innhold |
|------|------|
| Opprinnelig indikasjon | Psoriasis |
| Predikert ny indikasjon | Strongyloidiasis |
| TxGNN-prediksjonsscore | 0,9984 |
| Evidensnivå | L5 |
| Markedsstatus i Norge | Markedsført (gyldige tillatelser: 1 av 1) |
| Antall godkjenninger | 1 (gyldige: 1) |
| Anbefalt beslutning | Hold |

---

## Hvorfor er (eller er ikke) denne prediksjonen rimelig?

Data om virkningsmekanisme er ikke tilgjengelig i de innsamlede dataene. Basert på kjent informasjon blokkerer brodalumab IL-17RA og dermed signalering via IL-17A, IL-17F og IL-25. Effekten ved psoriasis er godt etablert.

For strongyloidiasis, en parasittinfeksjon forårsaket av rundorm (helminter), er den biologiske begrunnelsen svak. IL-17 bidrar til vertens forsvar ved slimhinne- og barrieroverflater, og IL-25 fremmer type 2-immunitet mot helminter. Blokkering av denne signalveien kan derfor plausibelt svekke, ikke styrke, immunforsvaret mot parasitten. Den høye TxGNN-scoren kommer fra TxGNN-modellen (deep learning) og kan gjenspeile likheter modellen har lært mellom beslektede sykdommer, ikke biologisk evidens.

Det er også verdt å merke seg at de neste ni predikerte indikasjonene (blant annet øyesykdom, optikusnevritt og episkleritt) heller ikke har direkte klinisk støtte, og at flere av dem er rent modellbaserte.

---

## Klinisk evidens

Det er for øyeblikket ingen registrerte kliniske studier knyttet til denne indikasjonen.

---

## Litteraturevidens

Det er for øyeblikket ingen relevant litteratur tilgjengelig for denne indikasjonen.

---

## Markedsinformasjon for Norge

| Godkjenningsnummer | Produktnavn | Doseringsform | Godkjent indikasjon |
|---------|------|------|-----------|
| EMEA/H/C/003959 | Kyntheum | Ikke oppgitt | Psoriasis |

Legemidlet er markedsført, og 1 av 1 markedsføringstillatelse er gyldig.

---

## Sikkerhetsvurderinger

- **Kontraindikasjoner fra kunnskapsgraf (ikke preparatomtale):** Crohns sykdom, inflammatorisk tarmsykdom og Crohns kolitt. Dette er kontraindikasjonskanter i TxGNN-kunnskapsgrafen og må verifiseres mot preparatomtalen.
- **Legemiddelinteraksjoner:** 68 interaksjoner er registrert. Eksempler på de mest alvorlige (grad «Major»):
  - Adalimumab
  - Baricitinib
  - Certolizumab pegol
  - Levende BCG-vaksine (Bacillus Calmette-Guérin)

  Interaksjoner av moderat grad omfatter blant annet roflumilast, alemtuzumab, anakinra, kanakinumab og flere vaksiner. Interaksjoner med sinksalter er av liten betydning (Minor).
- **Immunsuppresjon:** Kombinasjon med andre immundempende midler og levende vaksiner krever særlig forsiktighet. Dette er spesielt relevant ved en parasittinfeksjon som strongyloidiasis, der svekket immunforsvar kan gi alvorlig forløp.

---

## Konklusjon og neste steg

**Beslutning: Hold**

**Begrunnelse:**
Prediksjonen er kun modellbasert (L5) uten kliniske studier eller litteratur, og virkningsmekanismen (IL-17RA/IL-25-blokade) kan tvert imot svekke forsvaret mot helminter. I tillegg er preparatet avregistrert i Norge.

**For å gå videre kreves følgende:**
- Detaljerte data om virkningsmekanisme fra DrugBank
- Preparatomtale med advarsler og kontraindikasjoner (blokkerende datamangel for sikkerhetsscreening)
- Prekliniske data som viser en mulig gunstig rolle for IL-17RA-blokade ved strongyloidiasis
- Vurdering av om andre predikerte indikasjoner (for eksempel uveitt/øyesykdom) er mer lovende. Foreløpig finnes bare indirekte litteratur, inkludert en kasuistikk om Behçets sykdom som oppsto etter oppstart av brodalumab, som peker mot mulig skade snarere enn nytte.
## Ansvarsfraskrivelse

Dette innholdet er kun til forskningsformål og utgjør ikke medisinsk rådgivning.
Klinisk validering kreves før enhver klinisk anvendelse.

---

