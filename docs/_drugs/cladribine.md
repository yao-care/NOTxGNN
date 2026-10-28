---
layout: default
title: Cladribine
parent: Kun modellprediksjon (L5)
nav_order: 100
evidence_level: L5
indication_count: 7
monitor_inn: "CLADRIBINE"
predicted_indications: ["parameningeal embryonal rhabdomyosarcoma", "botryoid-type embryonal rhabdomyosarcoma of the vagina", "embryonal extrahepatic bile duct rhabdomyosarcoma", "prostate embryonal rhabdomyosarcoma", "extrahepatic bile duct rhabdomyosarcoma", "rhabdomyosarcoma (disease)", "liver sarcoma"]
last_modified_at: 2026-10-27
description: "Cladribine: predikert ny indikasjon Parameningeal embryonal rabdomyosarkom (parameningeal embryonal rhabdomyosarcoma) (evidensnivå L5). Opprinnelig indikasjon: Multiple Sclerosis"
---

# Cladribine
{: .fs-9 }

Evidensnivå: **L5** | Predikerte indikasjoner: **7** stk.
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

## Kladribin: nukleosidanalog → parameningeal embryonal rabdomyosarkom (parameningeal embryonal rhabdomyosarcoma)
{: .text-alpha }

## Oppsummering

Kladribin er en purinnukleosidanalog som brukes ved lymfoide sykdommer og multippel sklerose.
TxGNN-modellen forutsier at den kan ha effekt mot **parameningeal embryonal rabdomyosarkom (parameningeal embryonal rhabdomyosarcoma)**.
Det finnes **ingen kliniske studier** og **ingen publikasjoner** som direkte støtter denne prediksjonen, så dette er en ren modellprediksjon.

## Hurtigoversikt

| Punkt | Innhold |
|------|------|
| Opprinnelig indikasjon | Multiple Sclerosis; Leukemia, Hairy Cell |
| Predikert ny indikasjon | Parameningeal embryonal rabdomyosarkom (parameningeal embryonal rhabdomyosarcoma) |
| TxGNN-prediksjonsscore | 0,9977 |
| Evidensnivå | L5 |
| Markedsstatus i Norge | Markedsført (gyldige tillatelser: 2 av 2) |
| Antall godkjenninger | 2 (gyldige: 2) |
| Anbefalt beslutning | Avvent |

## Hvorfor er denne prediksjonen rimelig?

Detaljerte mekanismedata er ikke tilgjengelige i de sammenstilte dataene. Ut fra generell kunnskap er kladribin (2-klordeoksyadenosin) en purinnukleosidanalog som er motstandsdyktig mot enzymet adenosindeaminase. Den fører til DNA-trådbrudd og apoptose i lymfocytter og monocytter. Virkningen avhenger av et høyt forhold mellom deoksycytidinkinase og 5'-nukleotidase, som er typisk for lymfoide celler.

Det finnes ingen holdepunkter for at en tilsvarende mekanisme gjelder ved rabdomyosarkom, som er en solid svulst av bløtvev. Den høye scoren skyldes sannsynligvis nærhet til andre kreftmidler i modellens nettverk, ikke en validert sammenheng. Standardbehandling av rabdomyosarkom bygger på vinkristin, daktinomycin, cyklofosfamid og lignende regimer, og kladribin har ingen etablert rolle.

Modellen gir også svært like scorer til flere beslektede rabdomyosarkomtyper (blant annet botryoid type i vagina, embryonal i ekstrahepatiske galleganger, prostata og den overordnede betegnelsen). Dette tyder på ett felles signal fremfor uavhengige bekreftelser.

## Evidens fra kliniske studier

Det er for tiden ingen relaterte kliniske studier registrert.

## Litteraturevidens

Det er for tiden ingen relatert litteratur tilgjengelig for den predikerte indikasjonen.

## Markedsinformasjon for Norge

| Godkjenningsnummer | Produktnavn | Doseringsform | Godkjent indikasjon |
|---------|------|------|-----------|
| EMEA/H/C/004230 | Mavenclad | Ikke oppgitt | Multippel sklerose |
| EMEA/H/C/000504 | Litak | Ikke oppgitt | Hårcelleleukemi |

## Cytotoksisitet

| Punkt | Innhold |
|------|------|
| Cytotoksisitetsklassifisering | Konvensjonelt cytotoksisk (purinnukleosidanalog) |
| Risiko for myelosuppresjon | Høy (nøytropeni, trombocytopeni og anemi er kjent) |
| Emetogenisitet | Lav |
| Overvåkingspunkter | Fullstendig blodstatus med differensialtelling, lever- og nyrefunksjon |
| Håndteringsbeskyttelse | Følg gjeldende regler for håndtering av cytotoksiske legemidler |

## Sikkerhetsvurderinger

- **Tilstander registrert som kontraindikasjoner i modellens data (ikke fra preparatomtale):** nyresykdom, pyoureter, trombocytopeni, hyperurikemi, nøytropeni, agranulocytose, sykdom i det perifere nervesystemet, perifer nevropati, anemi og makrocytær anemi.
- **Legemiddelinteraksjoner:** Til sammen 100 interaksjoner er registrert. Blant de viktigste med alvorlighetsgrad «Major» er kortikosteroider (hydrokortison, triamcinolon, deksametason, betametason, budesonid, prednisolon, prednison), deferipron samt radiofarmaka og radioimmunterapi (ibritumomab tiuxetan, jobenguan (I-131), tositumomab, samarium (153Sm) leksidronam, strontiumklorid Sr-89). Palifermin, dipyridamol, cilostazol og eltrombopag er registrert med moderat alvorlighetsgrad.

Se preparatomtalen for fullstendig sikkerhetsinformasjon.

## Konklusjon og neste steg

**Beslutning: Avvent**

**Begrunnelse:**
Prediksjonen bygger kun på modellscore, uten kliniske studier, litteratur eller en plausibel mekanisme i rabdomyosarkom. Kladribins lymfoidselektive biologi gjør nytte ved solide svulster usikker, og de like scorene i rabdomyosarkomgruppen er trolig ikke uavhengige.

**For å gå videre kreves følgende:**
- Prekliniske data (cellelinjer og dyremodeller) for rabdomyosarkom
- Data om virkningsmekanisme og uttrykk av deoksycytidinkinase og 5'-nukleotidase i rabdomyosarkomceller
- Gjennomgang av preparatomtalens advarsler og kontraindikasjoner, spesielt med tanke på myelosuppresjon
- Vurdering av nytte opp mot etablerte behandlingsregimer
## Ansvarsfraskrivelse

Dette innholdet er kun til forskningsformål og utgjør ikke medisinsk rådgivning.
Klinisk validering kreves før enhver klinisk anvendelse.

---

