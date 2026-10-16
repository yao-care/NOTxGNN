---
layout: default
title: Ivabradine
parent: Kun modellprediksjon (L5)
nav_order: 225
evidence_level: L5
indication_count: 6
last_modified_at: 2026-10-15
description: "Ivabradine: predikert ny indikasjon Hypertrikose (evidensnivå L5). Opprinnelig indikasjon: Angina pectoris"
---

# Ivabradine
{: .fs-9 }

Evidensnivå: **L5** | Predikerte indikasjoner: **6** stk.
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

# Ivabradin: Fra angina pectoris og hjertesvikt til hypertrikose

## Oppsummering i én setning

Ivabradin er et legemiddel som opprinnelig brukes mot **angina pectoris og hjertesvikt**. TxGNN-modellen forutsier at det kan ha effekt ved **hypertrikose (uvanlig sterk hårvekst)**, men prediksjonen bygger kun på en modellberegning: det finnes **ingen kliniske studier** og **ingen publikasjoner** som støtter den i de innsamlede dataene.

---

## Hurtigoversikt

| Punkt | Innhold |
|------|------|
| Opprinnelig indikasjon | Angina pectoris; hjertesvikt |
| Predikert ny indikasjon | Hypertrikose |
| TxGNN-prediksjonsscore | 99,79 % |
| Evidensnivå | L5 |
| Markedsstatus i Norge | Kun kansellerte godkjenninger |
| Antall godkjenninger | 5 (alle kansellert) |
| Anbefalt beslutning | Hold |

---

## Hvorfor er denne prediksjonen (ikke) rimelig?

Detaljerte data om virkningsmekanismen er for øyeblikket ikke tilgjengelige i datagrunnlaget. Ut fra allmenn kunnskap blokkerer ivabradin HCN-kanalen (If, den såkalte «funny current») i sinusknuten og senker dermed hjertefrekvensen. Effekten er symptomatisk og rettet mot hjertet.

Det er ingen dokumentert sammenheng mellom HCN-hemming og regulering av hårvekst. Den høye scoren (0,998) gjenspeiler trolig nærhet i nettverksgrafen, ikke en biologisk begrunnelse. Det samme gjelder de øvrige predikerte tilstandene:

- **Ambras-type hypertrichosis universalis congenita** (score 99,72 %): en sjelden medfødt tilstand knyttet til genomiske omleiringer nær TRPS1. Relevansen av HCN-blokkade er ikke etablert.
- **Misdannelsessyndrom med tann- og/eller periodontal komponent** (99,72 %): en heterogen gruppe utviklingsforstyrrelser. Et pulsreduserende legemiddel er lite sannsynlig å påvirke slik patologi.
- **Syndrom med Dandy-Walker-malformasjon** (99,70 %): en strukturell utviklingsanomali i bakre skallegrop, uten kjent rolle for HCN-hemming.
- **Isolert genetisk hårskaftavvik** (99,69 %): HCN-kanaler er omtalt i enkelte rapporter om hårsekkrelaterte celler, men det finnes ingen data på at ivabradin påvirker hårskaftets struktur.
- **Nefrogent syndrom med uhensiktsmessig antidiurese** (99,08 %): skyldes aktiverende varianter i vasopressin V2-reseptoren (AVPR2), en signalvei ivabradin ikke virker på.

---

## Klinisk evidens

Foreløpig er ingen relaterte kliniske studier registrert.

---

## Litteraturevidens

Foreløpig er ingen relatert litteratur tilgjengelig.

---

## Markedsinformasjon for Norge

Alle fem godkjenninger er kansellert, og ingen er gyldige i dag.

| Godkjenningsnummer | Produktnavn | Doseringsform | Godkjent indikasjon |
|---------|------|------|-----------|
| EMEA/H/C/004187 | Ivabradine Anpharm | – | Angina pectoris; hjertesvikt |
| EMEA/H/C/004241 | Ivabradine Accord | – | Angina pectoris; hjertesvikt |
| EMEA/H/C/000597 | Procoralan | – | Angina pectoris; hjertesvikt |
| EMEA/H/C/000598 | Corlentor | – | Angina pectoris; hjertesvikt |
| EMEA/H/C/004117 | Ivabradine Zentiva | – | Angina pectoris; hjertesvikt |

---

## Sikkerhetsvurderinger

- **Legemiddelinteraksjoner**: Det er funnet 100 registrerte interaksjoner. Blant de første 20 som ble gjennomgått, er følgende av **alvorlig (Major)** grad:
  - Aprepitant, klaritromycin, kobicistat, klotrimazol (kan øke ivabradinnivået via CYP3A4-hemming og/eller forsterke effekten)
  - Dolasetron, palonosetron, granisetron, ondansetron, cisaprid, levofloksacin, papaverin (kan bidra til QT-forlengelse eller hjerterytmeforstyrrelser)

  Interaksjoner av **moderat** grad omfatter famotidin, ranitidin (også med vismutsitrat), cimetidin, nizatidin, deksametason, metreleptin, mikonazol og troglitazon.

For øvrig sikkerhetsinformasjon (advarsler og kontraindikasjoner) må preparatomtalen konsulteres.

---

## Konklusjon og neste steg

**Beslutning: Hold**

**Begrunnelse:**
Prediksjonen er kun beregnet av modellen (evidensnivå L5). Det finnes verken kliniske studier, publikasjoner eller en dokumentert mekanistisk sammenheng mellom HCN-hemming og hårvekst. I tillegg er alle norske godkjenninger kansellert.

**For å gå videre kreves følgende:**
- Detaljerte data om virkningsmekanisme (MOA)
- Preparatomtale med advarsler og kontraindikasjoner, som er en forutsetning for sikkerhetsscreening
- Prekliniske studier eller mekanistiske data som undersøker HCN-kanalers rolle i hårsekker
- Avklaring av administrasjonsvei og forhold til opprinnelig indikasjon
- Vurdering av om markedsføringstillatelse må søkes på nytt, siden ingen er gyldig i dag
## Ansvarsfraskrivelse

Dette innholdet er kun til forskningsformål og utgjør ikke medisinsk rådgivning.
Klinisk validering kreves før enhver klinisk anvendelse.

---

