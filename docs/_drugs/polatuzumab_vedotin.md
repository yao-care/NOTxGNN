---
layout: default
title: Polatuzumab Vedotin
parent: Kun modellprediksjon (L5)
nav_order: 331
evidence_level: L5
indication_count: 1
last_modified_at: 2026-10-28
description: "Polatuzumab Vedotin: predikert ny indikasjon HER2-positivt brystkarsinom (evidensnivå L5). Opprinnelig indikasjon: B-cellelymfom"
monitor_inn: "POLATUZUMAB VEDOTIN"
predicted_indications: ["HER2 positive breast carcinoma"]
---

# Polatuzumab Vedotin
{: .fs-9 }

Evidensnivå: **L5** | Predikerte indikasjoner: **1** stk.
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

## Polatuzumab vedotin: Fra B-cellelymfom til HER2-positivt brystkarsinom
{: .text-alpha }

## Oppsummering i én setning

Polatuzumab vedotin er et antistoff-legemiddelkonjugat som opprinnelig brukes mot B-cellelymfom.
TxGNN-modellen forutsier at det kan være effektivt mot **HER2-positivt brystkarsinom**,
men det finnes foreløpig **ingen kliniske studier** og **ingen publikasjoner** som støtter denne retningen. Prediksjonen er kun modellbasert.

---

## Hurtigoversikt

| Punkt | Innhold |
|------|------|
| Opprinnelig indikasjon | B-cellelymfom |
| Predikert ny indikasjon | HER2-positivt brystkarsinom |
| TxGNN-prediksjonsscore | 0,9934 |
| Evidensnivå | L5 |
| Markedsstatus i Norge | Markedsført (gyldige tillatelser: 1 av 1) |
| Antall godkjenninger | 1 (gyldige: 1) |
| Antall markedsføringstillatelser | 1 |
| Anbefalt beslutning | Hold |

---

## Hvorfor kan denne prediksjonen være rimelig?

Detaljerte data om virkningsmekanisme er foreløpig ikke tilgjengelige i dataene som er sammenstilt for denne rapporten. Basert på kjent informasjon er polatuzumab vedotin et antistoff-legemiddelkonjugat rettet mot CD79b, en del av B-cellereseptoren. Det leverer MMAE, et giftstoff som forstyrrer mikrotubuli. Effekten er dokumentert ved B-cellelymfom.

Koblingen til HER2-positivt brystkarsinom er svak og indirekte. CD79b er ikke et anerkjent mål i brystkreft, og det er ikke vist at målet uttrykkes i brystkreftvev. Et tenkelig argument er den cytotoksiske MMAE-nyttelasten, som deles med andre vedotin-konjugater. Dette er imidlertid ikke validert for denne indikasjonen.

HER2-positiv brystkreft har dessuten allerede godkjente HER2-rettede antistoff-legemiddelkonjugater (trastuzumab emtansin og trastuzumab deruxtekan). Et CD79b-rettet konjugat har derfor ingen åpenbar mekanistisk fordel. Scoren er en ren beregningsmessig prediksjon og må valideres eksperimentelt, for eksempel ved å undersøke CD79b-uttrykk i brysttumorer og cytotoksisitet in vitro.

---

## Kliniske studier

Det er foreløpig ingen relaterte kliniske studier registrert.

---

## Litteraturevidens

Det er foreløpig ingen relatert litteratur tilgjengelig.

---

## Markedsinformasjon for Norge

| Tillatelsesnummer | Produktnavn | Doseringsform | Godkjent indikasjon |
|---------|------|------|-----------|
| EMEA/H/C/004870 | Polivy | Ikke oppgitt | B-cellelymfom (status: godkjent) |

---

## Cytotoksisitet

| Punkt | Innhold |
|------|------|
| Klassifisering av cytotoksisitet | Målrettet terapi (antistoff-legemiddelkonjugat med MMAE-nyttelast, et mikrotubuli-hemmende middel) |
| Risiko for myelosuppresjon | Se pakningsvedlegget for advarsler og forsiktighetsregler |
| Emetogent potensial | Se pakningsvedlegget for advarsler og forsiktighetsregler |
| Overvåkingspunkter | Se pakningsvedlegget for advarsler og forsiktighetsregler |
| Håndtering og beskyttelse | Se pakningsvedlegget for advarsler og forsiktighetsregler. Cytotoksiske legemidler krever normalt egne håndteringsrutiner. |

---

## Sikkerhetsvurderinger

- **Legemiddelinteraksjoner**: Det er funnet 100 registrerte interaksjoner. De viktigste av dem som er oppgitt i dataene (alvorlighetsgrad «Major»):
  - Klaritromycin
  - Kobicistat
  - Deferipron
  - Samarium (153Sm) lexidronam

  Flere interaksjoner av moderat alvorlighetsgrad er også registrert, blant annet med aprepitant, cimetidin, naltrekson, metronidazol, mikonazol, rosuvastatin, simvastatin, tinidazol, klotrimazol, tikagrelor, klorokin og hydroksyklorokin.

Øvrig sikkerhetsinformasjon (advarsler og kontraindikasjoner) finnes i pakningsvedlegget.

---

## Konklusjon og neste steg

**Beslutning: Hold**

**Begrunnelse:**
Den eneste støtten er en høy TxGNN-score. Det finnes ingen kliniske studier eller litteratur, mekanismen er svakt koblet til indikasjonen (CD79b er ikke et kjent mål i HER2-positiv brystkreft), og godkjente HER2-rettede konjugater finnes allerede. I tillegg er den eneste norske tillatelsen avregistrert.

**For å gå videre trengs følgende:**
- Pakningsvedlegg med advarsler og kontraindikasjoner (blokkerende datamangel for sikkerhetsscreening)
- Data om virkningsmekanisme (MOA), for eksempel fra DrugBank
- Eksperimentell validering: CD79b-uttrykk i HER2-positive brysttumorer og in vitro-cytotoksisitet
- Systematisk litteratur- og studiesøk for å bekrefte at det ikke finnes støttende evidens
- Avklaring av markedsstatus og tilgjengelighet i Norge
## Ansvarsfraskrivelse

Dette innholdet er kun til forskningsformål og utgjør ikke medisinsk rådgivning.
Klinisk validering kreves før enhver klinisk anvendelse.

---

