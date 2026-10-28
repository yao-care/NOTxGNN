---
layout: default
title: Temozolomide
parent: Kun modellprediksjon (L5)
nav_order: 406
evidence_level: L5
indication_count: 1
monitor_inn: "TEMOZOLOMIDE"
predicted_indications: ["cauda equina neoplasm"]
last_modified_at: 2026-10-23
description: "Temozolomide: predikert ny indikasjon Cauda equina-neoplasme (evidensnivå L5). Opprinnelig indikasjon: Gliom"
---

# Temozolomide
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

## Temozolomid: Fra gliom til cauda equina-neoplasme
{: .text-alpha }

## Oppsummering i én setning

Temozolomid er et oralt alkylerende legemiddel som er godkjent i Norge for behandling av gliom. TxGNN-modellen predikerer at det kan ha effekt ved **cauda equina-neoplasme**. Per nå finnes **ingen registrerte kliniske studier** og kun **3 publikasjoner** (alle kasuistikker), hvorav bare én gjelder en svulst i dette området.

---

## Hurtigoversikt

| Punkt | Innhold |
|------|------|
| Opprinnelig indikasjon | Gliom |
| Predikert ny indikasjon | Cauda equina-neoplasme |
| TxGNN-prediksjonsscore | 0,9930 |
| Evidensnivå | L5 |
| Status på det norske markedet | Markedsført (gyldige tillatelser: 5 av 5) |
| Antall godkjenninger | 5 (gyldige: 5) |
| Anbefalt beslutning | Hold |

---

## Hvorfor er denne prediksjonen rimelig?

Detaljerte data om virkningsmekanisme er foreløpig ikke tilgjengelige i dataene som er sammenstilt for denne rapporten. Ut fra generell kunnskap er temozolomid et alkylerende middel som metylerer DNA (særlig O6-guanin) og gir cytotoksiske skader i delende svulstceller. Effekten reduseres når MGMT-enzymet uttrykkes.

Svulster i cauda equina er som regel spinale myxopapillære ependymomer, som stammer fra gliaceller i sentralnervesystemet. Det gir et biologisk plausibelt grunnlag, siden temozolomid er etablert ved gliom. Det mangler imidlertid data om MGMT-status eller kjemosensitivitet i disse svulstene. Den høye TxGNN-scoren er en beregningsbasert prediksjon og ikke klinisk evidens.

---

## Evidens fra kliniske studier

Foreløpig er det ingen registrerte kliniske studier knyttet til denne indikasjonen.

---

## Litteraturevidens

| PMID | År | Type | Tidsskrift | Hovedfunn |
|------|-----|------|------|---------|
| [29270703](https://pubmed.ncbi.nlm.nih.gov/29270703/) | 2018 | Kasuistikk | European Spine Journal | Temozolomid viste tydelig effekt ved residivert spinal myxopapillært ependymom med spredning i spinalvæsken |
| [42760727](https://pubmed.ncbi.nlm.nih.gov/42760727/) | 2026 | Kasuistikk | Medicine | Nasalt NUT-karsinom med gjentatte responser under multimodal behandling med strålebehandling; ikke direkte relevant for cauda equina |
| [18706663](https://pubmed.ncbi.nlm.nih.gov/18706663/) | 2009 | Kasuistikk | Neuro-Chirurgie | Atypisk kryptokokkinfeksjon hos en pasient behandlet for pontint gliom; ikke relevant for effekt ved cauda equina-neoplasme |

Den eneste publikasjonen som er relevant, er en enkelt kasuistikk om spinalt myxopapillært ependymom. Den gjelder en svulst av samme type som ofte oppstår i cauda equina, men studerer ikke cauda equina-neoplasme som sådan.

---

## Informasjon om det norske markedet

| Godkjenningsnummer | Produktnavn | Doseringsform | Godkjent indikasjon |
|---------|------|------|-----------|
| EMEA/H/C/001125 | Temozolomide Accord | – | Gliom |
| EMEA/H/C/001124 | Temomedac | – | Gliom |
| EMEA/H/C/001126 | Temozolomide Teva | – | Gliom |
| EMEA/H/C/000229 | Temodal | – | Gliom |
| EMEA/H/C/002198 | Temozolomide Sun | – | Gliom |

---

## Cytotoksisitet

| Punkt | Innhold |
|------|------|
| Klassifisering av cytotoksisitet | Konvensjonelt cytotoksisk middel (alkylerende middel) |
| Risiko for myelosuppresjon | Relevant. Kunnskapsgrafen registrerer kontraindikasjonsrelasjoner til blant annet trombocytopeni, nøytropeni, pancytopeni og aplastisk anemi |
| Emetogenisitet | Se preparatomtalen for advarsler og forsiktighetsregler |
| Overvåkingsparametere | Blodstatus (CBC med differensialtelling), lever- og nyrefunksjon |
| Håndteringsbeskyttelse | Følg gjeldende regler for håndtering av cytotoksiske legemidler |

---

## Sikkerhetsvurderinger

- **Kontraindikasjoner registrert i kunnskapsgrafen (ikke fra preparatomtale):** leversvikt, trombocytopeni, nøytropeni, agranulocytose, anemi, makrocytær anemi, pneumocystose, pancytopeni, lymfopeni, myelodysplastisk syndrom, idiopatisk aplastisk anemi og aplastisk anemi.
- **Legemiddelinteraksjoner:** 100 interaksjoner er registrert i dataene. Blant de som er klassifisert, er **moderat**: naltrekson, og **mindre**: levofloksacin. Øvrige (for eksempel kalsitriol, pantoprazol, doksycyklin, morfin, metformin, omeprazol, prednison og hydrokortison) har ukjent alvorlighetsgrad.

For fullstendig sikkerhetsinformasjon, se preparatomtalen.

---

## Konklusjon og neste steg

**Beslutning: Hold**

**Begrunnelse:**
Evidensen er på nivå L5: ingen kliniske studier og kun én kasuistikk som berører en beslektet svulsttype, ikke cauda equina-neoplasme direkte. Den høye TxGNN-scoren er ren modellprediksjon. Mekanismen er biologisk plausibel, men ikke underbygd av data.

**For å gå videre kreves følgende:**
- Data om virkningsmekanisme (MOA) og MGMT-status i myxopapillære ependymomer
- Systematisk litteraturgjennomgang og eventuelle retrospektive serier eller kliniske studier på spinale ependymomer/cauda equina-svulster
- Gjennomgang av preparatomtalen for advarsler og kontraindikasjoner
- Sikkerhetsplan med overvåking av blodstatus og leverfunksjon
## Ansvarsfraskrivelse

Dette innholdet er kun til forskningsformål og utgjør ikke medisinsk rådgivning.
Klinisk validering kreves før enhver klinisk anvendelse.

---

