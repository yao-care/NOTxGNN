---
layout: default
title: Serine
parent: Kun modellprediksjon (L5)
nav_order: 381
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-15
description: "Serine: predikert ny indikasjon Familiær visceral myopati (evidensnivå L5). Opprinnelig indikasjon: Lønnesirupsyke (Maple Syrup Urine Disease)"
---

# Serine
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

# Serin: Fra lønnesirupsyke til familiær visceral myopati

## Oppsummering i én setning

Serin er en aminosyre som i EU er godkjent under handelsnavnet Maapliv, opprinnelig for behandling av **lønnesirupsyke** (Maple Syrup Urine Disease). TxGNN-modellen forutsier at serin kan ha effekt ved **familiær visceral myopati**, men det finnes **ingen kliniske studier og ingen relevant litteratur** som støtter dette. Prediksjonen er rent modellbasert.

---

## Hurtigoversikt

| Punkt | Innhold |
|------|------|
| Opprinnelig indikasjon | Lønnesirupsyke (Maple Syrup Urine Disease) |
| Predikert ny indikasjon | Familiær visceral myopati |
| TxGNN-prediksjonsscore | 99,99 % |
| Evidensnivå | L5 |
| Markedsstatus i Norge | Kun tilbakekalt/avregistrert (ingen gyldige godkjenninger) |
| Antall godkjenninger | 1 (0 gyldige, 1 avregistrert) |
| Anbefalt beslutning | Hold (avvent) |

---

## Hvorfor er denne prediksjonen (ikke) rimelig?

Data om virkningsmekanisme (MOA) for serin er for øyeblikket ikke tilgjengelig. Serin er en naturlig forekommende aminosyre, og det finnes ingen dokumentasjon i datagrunnlaget for at serintilskudd påvirker sykdomsmekanismen ved familiær visceral myopati.

Familiær visceral myopati er en sjelden arvelig sykdom i tarmens glatte muskulatur (for eksempel ACTG2-relatert). Det er ikke påvist noen mekanistisk kobling mellom serin og denne patologien. Den høye TxGNN-scoren (0,9999) er en ren grafbasert prediksjon, og tilsvarende score for flere beslektede tarmmotilitetssykdommer tyder på at signalet delvis er delt gjennom kunnskapsgrafen, ikke spesifikt for serin.

Det er også verdt å merke seg at litteratursøk for andre predikerte indikasjoner (tarmobstruksjon og vinkelblokkglaukom) i hovedsak ga treff på nøkkelord som «serinprotease» og «serin/treoninkinase» (for eksempel STK11 ved Peutz-Jeghers syndrom og PRSS56 ved glaukom). Dette er gen- og proteinnavn og sier ingenting om serin som legemiddel.

---

## Klinisk studiedokumentasjon

Det er for øyeblikket ingen relaterte kliniske studier registrert for familiær visceral myopati. Heller ikke de øvrige ni predikerte indikasjonene har registrerte kliniske studier.

---

## Litteraturdokumentasjon

Det er for øyeblikket ingen relatert litteratur tilgjengelig for den predikerte hovedindikasjonen, familiær visceral myopati.

For nærliggende predikerte indikasjoner (tarmobstruksjon, vinkelblokkglaukom) ble det funnet 17 og 5 publikasjoner, men disse er nøkkelordtreff (serinproteaser, serin/treoninkinaser, Peutz-Jeghers syndrom, PRSS56) og vurderes som **ikke relevante** som støtte for serin som behandling.

---

## Informasjon om det norske markedet

| Godkjenningsnummer | Produktnavn | Doseringsform | Godkjent indikasjon |
|---------|------|------|-----------|
| EMEA/H/C/005557 | Maapliv | Ikke oppgitt | Lønnesirupsyke (Maple Syrup Urine Disease) |

Godkjenningen er registrert som avregistrert/tilbakekalt. Det finnes ingen gyldige godkjenninger for serin i Norge.

---

## Sikkerhetsvurderinger

Data fra preparatomtale (pakningsvedlegg) om advarsler og kontraindikasjoner er ikke tilgjengelig. Det ble ikke funnet registrerte legemiddelinteraksjoner.

Kunnskapsgrafen (PrimeKG) har imidlertid kontraindikasjonskoblinger mellom serin og en rekke tilstander. Disse stammer fra grafen og ikke fra preparatomtale, og må verifiseres. Eksempler:

- **Nyre- og urinveissykdommer:** kronisk nyresykdom, nyresvikt i sluttstadiet, nefrolitiasis, nefrokalsinose
- **Hjerte- og karsykdommer:** hjertesykdom, kardiovaskulær sykdom, ventrikkelflimmer, digitalisforgiftning
- **Psykiske og nevrologiske sykdommer:** epilepsi, angstlidelse, psykotiske lidelser, schizoaffektiv lidelse, rusavhengighet
- **Stoffskiftesykdommer:** diabetes mellitus, diabetisk ketoacidose, hyperkalsemi, fosforstoffskiftesykdom
- **Andre:** sarkoidose, vitamin B12-mangel, megaloblastær anemi

For øvrig henvises det til preparatomtalen for sikkerhetsinformasjon.

---

## Konklusjon og neste steg

**Beslutning: Hold (avvent)**

**Begrunnelse:**
Prediksjonen er utelukkende modellbasert (evidensnivå L5) uten kliniske studier, uten relevant litteratur og uten kjent mekanistisk kobling. I tillegg er det ingen gyldig markedsføringstillatelse i Norge, og viktige sikkerhetsdata mangler.

**For å gå videre kreves følgende:**
- Data om virkningsmekanisme (MOA) fra DrugBank
- Preparatomtale med advarsler og kontraindikasjoner fra DMP (kritisk for sikkerhetsscreening)
- Mekanistisk og prekliniske studier som kobler serin til patologien ved visceral myopati
- Manuell gjennomgang av litteratur for å skille serin som aminosyre fra serinproteaser og -kinaser
- Avklaring av vurderingen av kontraindikasjonene fra kunnskapsgrafen
- Avklaring av administrasjonsvei og tilgjengelige formuleringer
## Ansvarsfraskrivelse

Dette innholdet er kun til forskningsformål og utgjør ikke medisinsk rådgivning.
Klinisk validering kreves før enhver klinisk anvendelse.

---

