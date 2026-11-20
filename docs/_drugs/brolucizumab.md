---
layout: default
title: Brolucizumab
parent: Kun modellprediksjon (L5)
nav_order: 68
evidence_level: L5
indication_count: 4
last_modified_at: 2026-11-12
description: "Brolucizumab: predikert ny indikasjon Mitokondriell oksidativ fosforyleringssykdom på grunn av kjerne-DNA-avvik (evidensnivå L5). Opprinnelig indikasjon: Våt makuladegenerasjon"
monitor_inn: "BROLUCIZUMAB"
predicted_indications: ["mitochondrial oxidative phosphorylation disorder due to nuclear DNA anomalies", "esophageal varices without bleeding", "esophageal varices with bleeding", "exocrine pancreatic insufficiency"]
---

# Brolucizumab
{: .fs-9 }

Evidensnivå: **L5** | Predikerte indikasjoner: **4** stk.
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

## Brolucizumab: Fra våt makuladegenerasjon til Mitokondriell oksidativ fosforyleringssykdom på grunn av kjerne-DNA-avvik
{: .text-alpha }

## Oppsummering

Brolucizumab er et anti-VEGF-A-antistoffragment (enkeltkjede) som opprinnelig ble brukt til behandling av **våt makuladegenerasjon**.
TxGNN-modellen predikerer at legemidlet kan ha effekt ved **mitokondriell oksidativ fosforyleringsforstyrrelse som skyldes kjerne-DNA-avvik**, men dette er en ren modellprediksjon.
Det finnes **ingen kliniske studier** og **ingen publikasjoner** i de innsamlede dataene som støtter denne retningen.

---

## Hurtigoversikt

| Punkt | Innhold |
|------|------|
| Opprinnelig indikasjon | Våt makuladegenerasjon |
| Predikert ny indikasjon | Mitokondriell oksidativ fosforyleringsforstyrrelse som skyldes kjerne-DNA-avvik |
| TxGNN-prediksjonsscore | 0,9967 |
| Evidensnivå | L5 |
| Markedsstatus i Norge | Markedsført (gyldige tillatelser: 1 av 1) |
| Antall godkjenninger | 1 (gyldige: 1) |
| Antall tillatelser | 1 |
| Anbefalt beslutning | Hold |

---

## Hvorfor er denne prediksjonen (ikke) rimelig?

Ifølge avsnittet «Mechanism of Action» i preparatomtalen som er godkjent av amerikanske FDA (Prescribing Information), for Brolucizumab (uoffisiell oversettelse): «Brolucizumab er en human VEGF-hemmer. Brolucizumab bindes til de tre hovedisoformene av VEGF-A (f.eks. VEGF 110, VEGF 121 og VEGF 165 ), og forhindrer dermed interaksjon med reseptorene VEGFR-1 og VEGFR-2. Ved å hemme VEGF-A undertrykker brolucizumab endotelcelleproliferasjon, neovaskularisering og vaskulær permeabilitet.» Engelsk originaltekst: "Brolucizumab is a human VEGF inhibitor. Brolucizumab binds to the three major isoforms of VEGF-A (e.g., VEGF 110, VEGF 121, and VEGF 165 ), thereby preventing interaction with receptors VEGFR-1 and VEGFR-2. By inhibiting VEGF-A, brolucizumab suppresses endothelial cell proliferation, neovascularization, and vascular permeability." ([DailyMed: Beovu (brolucizumab) prescribing information, Novartis Pharmaceuticals Corporation](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=5d1dc1fa-a2d3-46ed-9e9a-c1a036590d3d), versjon av 2026-10-26; hentet 2026-11-19). Basert på kjent informasjon er brolucizumab et anti-VEGF-A-antistoffragment som er gitt intravitrealt, og effekten ved våt makuladegenerasjon bygger på hemming av VEGF-drevet karnydannelse og lekkasje.

Det ble ikke identifisert noen tydelig mekanistisk sammenheng mellom VEGF-A-hemming og oksidative fosforyleringsforstyrrelser som skyldes kjerne-DNA-avvik. Den høye scoren (0,9967) er utelukkende grafbasert og er ikke underbygget av kliniske studier eller litteratur. Likhet med den opprinnelige indikasjonen er ikke vurdert.

Prediksjonen bør derfor betraktes som en hypotese som krever grunnleggende mekanistisk arbeid før videre vurdering.

### Andre predikerte indikasjoner (til orientering)

| Rang | Predikert indikasjon | TxGNN-score | Evidensnivå | Kommentar |
|------|------|------|------|------|
| 2 | Øsofagusvaricer uten blødning | 0,9912 | L5 | Spekulativ VEGF-/angiogenese-begrunnelse; systemisk VEGF-hemming gir blødnings-, tromboemboli- og hypertensjonsrisiko. Intravitreal administrasjon gir ingen plausibel systemisk rute. |
| 3 | Øsofagusvaricer med blødning | 0,9912 | L5 | Samme begrunnelse; større sikkerhetsbekymring ved aktiv blødning, da hemostase og tilheling kan svekkes. |
| 4 | Eksokrin pankreasinsuffisiens | 0,9907 | L5 | Ingen identifisert mekanistisk kobling til VEGF-A-hemming. |

Alle fire prediksjonene har anbefalingen «Hold».

---

## Kliniske studier

Foreløpig er det ikke registrert noen relaterte kliniske studier.

---

## Litteraturevidens

Foreløpig finnes det ingen relatert litteratur.

---

## Informasjon om det norske markedet

| Tillatelsesnummer | Produktnavn | Doseringsform | Godkjent indikasjon |
|---------|------|------|-----------|
| EMEA/H/C/004913 | Beovu | Ikke oppgitt | Våt makuladegenerasjon |

Legemidlet er markedsført, og tillatelsen er gyldig (1 av 1 gyldige tillatelser).

---

## Sikkerhetsvurderinger

- **Kontraindikasjoner fra kunnskapsgraf (ikke preparatomtale):** TxGNNs kunnskapsgraf (PrimeKG) har kontraindikasjonskoblinger mellom brolucizumab og følgende tilstander: uveitt, irissykdom, sykdom i ciliarlegemet, panuveitt, infeksjonssykdom i øyet og konjunktivitt. Dette er grafbaserte data og må verifiseres mot preparatomtalen.

Ytterligere sikkerhetsinformasjon (advarsler, kontraindikasjoner og legemiddelinteraksjoner) finnes ikke i de innsamlede dataene. Se preparatomtalen for fullstendig sikkerhetsinformasjon.

---

## Konklusjon og neste steg

**Beslutning: Hold**

**Begrunnelse:**
Prediksjonen er basert utelukkende på en grafmodell (L5) uten støtte fra kliniske studier eller litteratur, og det er ikke identifisert noen plausibel mekanistisk sammenheng.

<!-- review:begin no-lic-20261031-brolucizumab-1 -->

> **Kontrollrettelse (2026-10-31)**: Opprinnelig sto det: «Prediksjonen er basert utelukkende på en grafmodell (L5) uten støtte fra kliniske studier eller litteratur, og det er ikke identifisert noen plausibel mekanistisk sammenheng. I tillegg er produktet i Norge kun registrert som avregistrert, og sikkerhetsdata fra preparatomtalen mangler.» Fjernet: opplysningen om at godkjenningene er avregistrert eller at ingen gyldig godkjenning finnes, stemte ikke med EMAs data om sentrale EU-godkjenninger (2026-10-31). Antall godkjenninger i dataene: 1, hvorav gyldige: 1; oppdaterte tall står i hurtigoversikten og i markedsinformasjonen. Kilde: [EMA – Medicines output: medicines report](https://www.ema.europa.eu/en/documents/report/medicines-output-medicines-report_en.xlsx); [European Medicines Agency](https://www.ema.europa.eu/).

<!-- review:end no-lic-20261031-brolucizumab-1 -->

**For å gå videre kreves følgende:**
- Innhenting og gjennomgang av preparatomtalen (advarsler og kontraindikasjoner), som er en blokkerende datamangel
- Data om virkningsmekanisme (MOA), for eksempel fra DrugBank
- Prekliniske eller mekanistiske studier som kan underbygge en kobling mellom VEGF-A-hemming og den predikerte indikasjonen
- Vurdering av administrasjonsvei og rutekompatibilitet for den predikerte indikasjonen
- Litteratur- og studiesøk som kan identifisere eventuell støttende evidens

<!-- review:begin log -->

## Kontrollogg

Nedenfor er kontrolloggen for denne siden: opplysninger kontrollert mot EMAs data om sentrale EU-godkjenninger. Rettelser gjelder bare grunnleggende faktaopplysninger; modellens prediksjoner, evidensnivåer og konklusjoner er ikke skrevet om. Setningen om at data om virkningsmekanismen ikke var tilgjengelige, er erstattet med et utdrag fra den oppgitte offisielle preparatomtalen (med uoffisiell oversettelse).

| Kontrolldato | Punkt | Tiltak | Kilde |
|------|------|------|------|
| 2026-10-31 | Fjernet: «I tillegg er produktet i Norge kun registrert som avregistrert, og sikkerhetsdata fra preparatomtalen mangler» | Rettet | [EMA – Medicines output: medicines report](https://www.ema.europa.eu/en/documents/report/medicines-output-medicines-report_en.xlsx); [European Medicines Agency](https://www.ema.europa.eu/) |
| 2026-11-19 | Setningen «data om virkningsmekanismen er ikke tilgjengelige» erstattet med utdrag fra amerikansk preparatomtale | Setning om manglende data om virkningsmekanismen erstattet med et utdrag med kilde | [DailyMed: Beovu (brolucizumab) prescribing information, Novartis Pharmaceuticals Corporation](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=5d1dc1fa-a2d3-46ed-9e9a-c1a036590d3d) |

<!-- review:end log -->

## Ansvarsfraskrivelse

Dette innholdet er kun til forskningsformål og utgjør ikke medisinsk rådgivning.
Klinisk validering kreves før enhver klinisk anvendelse.

---

