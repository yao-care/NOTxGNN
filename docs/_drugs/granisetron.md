---
layout: default
title: Granisetron
parent: Kun modellprediksjon (L5)
nav_order: 197
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-15
description: "Granisetron: predikert ny indikasjon Manisk bipolar lidelse (evidensnivå L5). Opprinnelig indikasjon: Oppkast"
monitor_inn: "GRANISETRON"
predicted_indications: ["manic bipolar affective disorder", "Tourette syndrome", "acute contagious conjunctivitis", "angioedema", "allergic urticaria", "nephrogenic syndrome of inappropriate antidiuresis", "trichotillomania", "bronchitis", "cold urticaria", "conjunctivitis"]
---

# Granisetron
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

# Granisetron: Fra kvalme og oppkast ved kreftbehandling til manisk bipolar lidelse

## Oppsummering

Granisetron er en selektiv 5-HT3-reseptorantagonist, opprinnelig brukt mot oppkast hos kreftpasienter.
TxGNN-modellen forutsier at legemidlet kan ha effekt ved **manisk bipolar lidelse**, men dette er kun en modellprediksjon.
Verken kliniske studier eller publikasjoner i de innsamlede dataene støtter retningen foreløpig.

---

## Hurtigoversikt

| Punkt | Innhold |
|------|------|
| Opprinnelig indikasjon | Oppkast; kreft |
| Predikert ny indikasjon | Manisk bipolar lidelse |
| TxGNN-prediksjonsscore | 99,62 % |
| Evidensnivå | L5 |
| Markedsstatus i Norge | Kun trukket tilbake (kansellert) |
| Antall godkjenninger | 1 |
| Anbefalt beslutning | Hold |

---

## Hvorfor er denne prediksjonen rimelig?

Detaljerte data om virkningsmekanisme er ikke tilgjengelige i datagrunnlaget. Granisetron er kjent som en selektiv 5-HT3-reseptorantagonist, og effekten ved kjemoterapiindusert oppkast er etablert.

Serotonerg og dopaminerg dysregulering antas å spille en rolle ved mani. Hemming av 5-HT3-reseptorer kan derfor tenkes å påvirke disse signalveiene. Koblingen er plausibel, men ubekreftet, og er utledet fra generell farmakologi og ikke fra data om granisetron spesifikt.

Den høye modellscoren (0,996) er ikke i seg selv bevis for klinisk effekt. Den kan også gjenspeile nærhet i kunnskapsgrafen snarere enn biologisk sammenheng.

### Andre predikerte indikasjoner (alle L5, Hold)

| Rang | Predikert indikasjon | Score | Vurdering av mekanisme |
|------|------|------|------|
| 2 | Tourettes syndrom | 99,52 % | Konseptuelt relevant via dopaminerg modulering; ingen data for granisetron |
| 3 | Akutt smittsom konjunktivitt | 99,49 % | Ingen klar mekanisme; trolig nettverksartefakt |
| 4 | Angioødem | 99,36 % | Spekulativ kobling via serotonin og vaskulær permeabilitet |
| 5 | Allergisk urtikaria | 99,32 % | Hypotetisk kobling via kløe og mastcellerespons |
| 6 | Nefrogent syndrom med uhensiktsmessig antidiurese | 99,32 % | Ingen kjent mekanisme; trolig nettverksartefakt |
| 7 | Trikotillomani | 99,23 % | Serotonerg modulering relevant for OCD-spekteret; ingen data |
| 8 | Bronkitt | 99,18 % | Spekulativ; ingen støttende evidens |
| 9 | Kuldeurtikaria | 99,10 % | Spekulativ; ingen definert mekanisme |
| 10 | Konjunktivitt | 99,09 % | Ingen etablert mekanisme |

---

## Evidens fra kliniske studier

Det er for øyeblikket ingen relaterte kliniske studier registrert for manisk bipolar lidelse.

---

## Litteraturevidens

Det er for øyeblikket ingen relatert litteratur tilgjengelig.

---

## Markedsinformasjon for Norge

| Godkjenningsnummer | Produktnavn | Doseringsform | Godkjent indikasjon |
|---------|------|------|-----------|
| EMEA/H/C/002296 | Sancuso | Ikke oppgitt | Oppkast; kreft (status: kansellert) |

Det finnes ingen gyldige markedsføringstillatelser for granisetron i datagrunnlaget.

---

## Sikkerhetsvurderinger

- **Kontraindikasjoner fra kunnskapsgrafen** (kunnskapsgrafrelasjoner, ikke preparatomtale): langt QT-syndrom, familiært langt QT-syndrom, kaliummangel, plutselig hjertestans og hjerteledningsforstyrrelser.
- **Legemiddelinteraksjoner**: 100 interaksjoner er registrert. Et utvalg av de viktigste:
  - **Alvorlige (Major)**: fentanyl, dekstrometorfan, tramadol, alfentanil, almotriptan, sumatriptan, amiodaron, amisulprid, amitriptylin og anagrelid. Mange av disse gjelder QT-forlengelse eller serotonergt syndrom.
  - **Moderate**: abirateron, dihydrokodein, kodein, famotidin, formoterol, adenosin, salbutamol, alfuzosin og propofol.

Viktige advarsler og kontraindikasjoner fra preparatomtalen mangler. Se preparatomtalen for fullstendig sikkerhetsinformasjon.

---

## Konklusjon og neste steg

**Beslutning: Hold**

**Begrunnelse:**
Prediksjonen bygger kun på modellscore uten kliniske studier eller litteratur (evidensnivå L5). Produktet er dessuten trukket tilbake i Norge, og sikkerhetsdata fra preparatomtalen mangler. Kontraindikasjoner knyttet til hjerterytme og mange alvorlige interaksjoner krever nøye vurdering.

**For å gå videre kreves følgende:**
- Hente og analysere preparatomtalen (advarsler og kontraindikasjoner), som er et blokkerende datagap
- Fullstendige data om virkningsmekanisme (MOA)
- Litteratur- og studiesøk spesifikt for 5-HT3-antagonister ved mani og bipolar lidelse
- Vurdering av administrasjonsvei og formulering som passer den nye indikasjonen
- Sikkerhetsplan for QT-forlengelse og serotonerge interaksjoner hos aktuelle pasientgrupper
## Ansvarsfraskrivelse

Dette innholdet er kun til forskningsformål og utgjør ikke medisinsk rådgivning.
Klinisk validering kreves før enhver klinisk anvendelse.

---

