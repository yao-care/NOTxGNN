---
layout: default
title: Avelumab
parent: Kun modellprediksjon (L5)
nav_order: 47
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-15
description: "Avelumab: predikert ny indikasjon Humant herpesvirus 8-relatert tumor (evidensnivå L5). Opprinnelig indikasjon: Nevroendokrine svulster"
---

# Avelumab
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

# Avelumab: Fra nevroendokrine svulster til humant herpesvirus 8-relatert tumor

## Oppsummering i én setning

Avelumab er et anti-PD-L1-antistoff, og den registrerte opprinnelige indikasjonen i de innsamlede dataene er nevroendokrine svulster.
TxGNN-modellen forutsier at legemidlet kan være effektivt mot **humant herpesvirus 8-relatert tumor**.
Det finnes foreløpig **0 kliniske studier** og **0 publikasjoner** i dataene som støtter denne prediksjonen, så den bygger kun på modellen.

---

## Hurtigoversikt

| Punkt | Innhold |
|------|------|
| Opprinnelig indikasjon | Nevroendokrine svulster |
| Predikert ny indikasjon | Humant herpesvirus 8-relatert tumor |
| TxGNN-prediksjonsscore | 99,97 % |
| Evidensnivå | L5 |
| Markedsstatus i Norge | Kun tilbakekalt/avregistrert (cancelled) |
| Antall markedsføringstillatelser | 1 |
| Anbefalt beslutning | Hold |

---

## Hvorfor er denne prediksjonen rimelig?

Detaljerte data om virkningsmekanisme er foreløpig ikke tilgjengelige i datagrunnlaget. Avelumab er imidlertid kjent som et anti-PD-L1-antistoff (immunsjekkpunkthemmer).

HHV-8-relaterte svulster, for eksempel Kaposi sarkom, viser immununndragelse og PD-L1-uttrykk. Sjekkpunkthemming er derfor biologisk plausibelt. Koblingen til den opprinnelige indikasjonen (nevroendokrine svulster) er imidlertid ikke vurdert (likhet: ikke avklart).

Det er viktig å understreke at dataene ikke inneholder verken studier eller litteratur for denne indikasjonen. Scoren er en ren modellprediksjon.

---

## Evidens fra kliniske studier

Foreløpig er ingen relaterte kliniske studier registrert.

---

## Litteraturevidens

Foreløpig er ingen relatert litteratur tilgjengelig.

---

## Markedsinformasjon for Norge

| Tillatelsesnummer | Produktnavn | Doseringsform | Godkjent indikasjon |
|---------|------|------|-----------|
| EMEA/H/C/004338 | Bavencio | – | Nevroendokrine svulster |

Tillatelsen har status «cancelled», og det finnes ingen gyldige tillatelser for tiden.

---

## Cytotoksisitet

| Punkt | Innhold |
|------|------|
| Klassifisering | Immunterapi (anti-PD-L1 monoklonalt antistoff), ikke konvensjonelt cytotoksisk |
| Risiko for myelosuppresjon | Se pakningsvedlegget for advarsler og forholdsregler |
| Emetogenisitet | Se pakningsvedlegget for advarsler og forholdsregler |
| Overvåkingspunkter | Se pakningsvedlegget for advarsler og forholdsregler |
| Håndteringsvern | Se pakningsvedlegget for advarsler og forholdsregler |

---

## Sikkerhetsvurderinger

- **Legemiddelinteraksjoner**: Tre interaksjoner av alvorlighetsgrad «Major» er identifisert (kilde: DDInter):
  - Lenalidomid
  - Pomalidomid
  - Talidomid

Se pakningsvedlegget for øvrig sikkerhetsinformasjon, inkludert advarsler og kontraindikasjoner.

---

## Andre predikerte indikasjoner (til orientering)

| Rang | Predikert indikasjon | TxGNN-score | Evidensnivå | Anbefaling |
|---|---|---|---|---|
| 2 | Nevroendokrin tumor i mellomøret | 99,97 % | L5 | Hold |
| 3 | Malignt kutant granulærcelletumor i huden | 99,97 % | L5 | Hold |
| 4 | Ektomesenkymom | 99,97 % | L5 | Hold |
| 5 | Adenosindeaminase-mangel | 99,95 % | L5 | Hold |
| 6 | Retikulær dysgenese | 99,94 % | L5 | Hold |
| 7 | Immunoerytromyeloid hypoplasi | 99,94 % | L5 | Hold |
| 8 | Ikke-alvorlig kombinert immunsvikt | 99,92 % | L5 | Hold |
| 9 | Urotelialt karsinom i prostatisk uretra | 99,92 % | L5 | Forskningsspørsmål |
| 10 | Sarkomatoid overgangscellekarsinom i nyrebekkenet | 99,91 % | L5 | Forskningsspørsmål |

Prediksjonene for primære immunsviktlidelser (rang 5–8) mangler en plausibel mekanisme og er sannsynligvis artefakter fra kunnskapsgrafen. De to urotelkarsinomene (rang 9–10) skiller seg ut: avelumab er etablert som vedlikeholdsbehandling ved avansert urotelialt karsinom etter platinabasert kjemoterapi (fase 3-studien JAVELIN Bladder 100). Disse er mest interessante for videre vurdering, men uten indikasjonsspesifikke data i grunnlaget er de likevel gradert som L5.

---

## Konklusjon og neste steg

**Beslutning: Hold**

**Begrunnelse:**
Prediksjonen for HHV-8-relatert tumor er biologisk plausibel, men støttes ikke av kliniske studier eller litteratur (L5). Den norske tillatelsen er i tillegg kansellert, og sentrale sikkerhetsdata mangler.

**For å gå videre kreves følgende:**
- Pakningsvedlegg med advarsler og kontraindikasjoner (blokkerende datamangel)
- Data om virkningsmekanisme (MOA) fra DrugBank
- Systematisk litteratur- og studiesøk for HHV-8-relaterte svulster, særlig Kaposi sarkom
- Vurdering av de urotelkarsinom-relaterte prediksjonene (rang 9–10) opp mot eksisterende fase 3-evidens og godkjent indikasjon
- Avklaring av administrasjonsvei og tilgjengelighet i Norge, gitt at tillatelsen er kansellert
## Ansvarsfraskrivelse

Dette innholdet er kun til forskningsformål og utgjør ikke medisinsk rådgivning.
Klinisk validering kreves før enhver klinisk anvendelse.

---

