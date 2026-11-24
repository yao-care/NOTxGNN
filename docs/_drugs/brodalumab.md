---
layout: default
title: Brodalumab
parent: Kun modellprediksjon (L5)
nav_order: 67
evidence_level: L5
indication_count: 10
last_modified_at: 2026-11-24
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

Ifølge avsnittet «Mechanism of Action» i preparatomtalen som er godkjent av amerikanske FDA (Prescribing Information), for Brodalumab (uoffisiell oversettelse): «Brodalumab er et humant monoklonalt IgG2-antistoff som bindes selektivt til humant IL-17RA og hemmer dets interaksjoner med cytokinene IL-17A, IL-17F, IL-17C, IL-17A/F-heterodimer og IL-25. IL-17RA er et protein som uttrykkes på celleoverflaten og er en nødvendig komponent i reseptorkomplekser som benyttes av flere cytokiner i IL-17-familien.» Engelsk originaltekst: "Brodalumab is a human monoclonal IgG2 antibody that selectively binds to human IL-17RA and inhibits its interactions with cytokines IL-17A, IL-17F, IL-17C, IL-17A/F heterodimer, and IL-25. IL-17RA is a protein expressed on the cell surface and is a required component of receptor complexes utilized by multiple IL-17 family cytokines." ([DailyMed: Siliq (brodalumab) prescribing information, Bausch Health US LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=1a550c33-456a-4833-814e-8591aea7c688), versjon av 2026-05-28; hentet 2026-11-19). Basert på kjent informasjon blokkerer brodalumab IL-17RA og dermed signalering via IL-17A, IL-17F og IL-25. Effekten ved psoriasis er godt etablert.

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

<!-- licenses:begin -->

| Godkjenningsnummer | Preparatnavn (EMA) | Virkestoff(er) (EMA, engelsk) | Terapeutisk område (EMA, engelsk) | Status |
|------|------|------|------|------|
| EMEA/H/C/003959 | Kyntheum | brodalumab | Psoriasis | Gyldig |

Kilde: EMA – Medicines output (sentralt godkjente legemidler til mennesker); preparatnavn, virkestoffer og terapeutisk område er gjengitt i engelsk original. Nasjonale markedsføringstillatelser (DMP) og veterinærpreparater er ikke med i disse dataene.

<!-- licenses:end -->

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
Prediksjonen er kun modellbasert (L5) uten kliniske studier eller litteratur, og virkningsmekanismen (IL-17RA/IL-25-blokade) kan tvert imot svekke forsvaret mot helminter.

<!-- review:begin no-lic-20261106-brodalumab-1 -->

> **Kontrollrettelse (2026-11-06)**: Opprinnelig sto det: «Prediksjonen er kun modellbasert (L5) uten kliniske studier eller litteratur, og virkningsmekanismen (IL-17RA/IL-25-blokade) kan tvert imot svekke forsvaret mot helminter. I tillegg er preparatet avregistrert i Norge.» Fjernet: opplysningen om at godkjenningene er avregistrert eller at ingen gyldig godkjenning finnes, stemte ikke med EMAs data om sentrale EU-godkjenninger (2026-11-06). Oppdaterte antall og statuser for godkjenningene står i hurtigoversikten og i lisenstabellen under markedsinformasjonen. Kilde: [EMA – Medicines output: medicines report](https://www.ema.europa.eu/en/documents/report/medicines-output-medicines-report_en.xlsx); [European Medicines Agency](https://www.ema.europa.eu/).

<!-- review:end no-lic-20261106-brodalumab-1 -->

**For å gå videre kreves følgende:**
- Detaljerte data om virkningsmekanisme fra DrugBank
- Preparatomtale med advarsler og kontraindikasjoner (blokkerende datamangel for sikkerhetsscreening)
- Prekliniske data som viser en mulig gunstig rolle for IL-17RA-blokade ved strongyloidiasis
- Vurdering av om andre predikerte indikasjoner (for eksempel uveitt/øyesykdom) er mer lovende. Foreløpig finnes bare indirekte litteratur, inkludert en kasuistikk om Behçets sykdom som oppsto etter oppstart av brodalumab, som peker mot mulig skade snarere enn nytte.

<!-- review:begin log -->

## Kontrollogg

Nedenfor er kontrolloggen for denne siden: opplysninger kontrollert mot EMAs data om sentrale EU-godkjenninger. Rettelser gjelder bare grunnleggende faktaopplysninger; modellens prediksjoner, evidensnivåer og konklusjoner er ikke skrevet om. Setningen om at data om virkningsmekanismen ikke var tilgjengelige, er erstattet med et utdrag fra den oppgitte offisielle preparatomtalen (med uoffisiell oversettelse).

| Kontrolldato | Punkt | Tiltak | Kilde |
|------|------|------|------|
| 2026-11-06 | Fjernet: «I tillegg er preparatet avregistrert i Norge» | Rettet (revidert 2026-11-24; tidligere versjon er lagret i posten) | [EMA – Medicines output: medicines report](https://www.ema.europa.eu/en/documents/report/medicines-output-medicines-report_en.xlsx); [European Medicines Agency](https://www.ema.europa.eu/) |
| 2026-11-19 | Setningen «data om virkningsmekanismen er ikke tilgjengelige» erstattet med utdrag fra amerikansk preparatomtale | Setning om manglende data om virkningsmekanismen erstattet med et utdrag med kilde | [DailyMed: Siliq (brodalumab) prescribing information, Bausch Health US LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=1a550c33-456a-4833-814e-8591aea7c688) |

<!-- review:end log -->

## Ansvarsfraskrivelse

Dette innholdet er kun til forskningsformål og utgjør ikke medisinsk rådgivning.
Klinisk validering kreves før enhver klinisk anvendelse.

---

