---
layout: default
title: Fentanyl
parent: Kun modellprediksjon (L5)
nav_order: 174
evidence_level: L5
indication_count: 2
last_modified_at: 2026-10-15
description: "Fentanyl: predikert ny indikasjon Nefrogent syndrom med uhensiktsmessig antidiurese (evidensnivå L5). Opprinnelig indikasjon: Smerte"
monitor_inn: "FENTANYL"
predicted_indications: ["nephrogenic syndrome of inappropriate antidiuresis", "Tourette syndrome"]
---

# Fentanyl
{: .fs-9 }

Evidensnivå: **L5** | Predikerte indikasjoner: **2** stk.
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

# Fentanyl: Fra smerte og kreft til nefrogent syndrom med uhensiktsmessig antidiurese

## Oppsummering

Fentanyl er en potent mu-opioidagonist som opprinnelig brukes til behandling av smerte, særlig kreftrelatert smerte.
TxGNN-modellen predikerer at legemidlet kan ha effekt ved **nefrogent syndrom med uhensiktsmessig antidiurese (NSIAD)**,
men **ingen kliniske studier** og **ingen publikasjoner** støtter denne retningen i dataene som er sammenstilt for denne rapporten.

---

## Hurtigoversikt

| Punkt | Innhold |
|------|------|
| Opprinnelig indikasjon | Smerte; kreft |
| Predikert ny indikasjon | Nefrogent syndrom med uhensiktsmessig antidiurese |
| TxGNN-prediksjonsscore | 99,46 % |
| Evidensnivå | L5 |
| Markedsstatus i Norge | Kun avregistrerte (opphevede) godkjenninger |
| Antall godkjenninger | 3 (alle avregistrert) |
| Anbefalt beslutning | Hold |

Merk: Godkjenningene i dataene er europeiske sentrale godkjenninger (EMEA/H/C-nummer), og det er ikke dokumentert noen gyldig nasjonal godkjenning.

---

## Hvorfor er denne prediksjonen (ikke) rimelig?

Detaljerte data om virkningsmekanisme er foreløpig ikke tilgjengelige. Fentanyl er kjent som en mu-opioidagonist, og effekten ved smerte, inkludert gjennombruddssmerte hos kreftpasienter, er veletablert.

NSIAD skyldes gain-of-function-mutasjoner i vasopressin V2-reseptoren (AVPR2), som gir vannretensjon uavhengig av vasopressin. Fentanyl har ingen kjent direkte virkning på V2-reseptoren eller nyrenes vannhåndtering. Opioider kan dessuten påvirke vasopressinfrisetting sentralt og gi SIADH-lignende effekter, noe som ville forverret snarere enn behandlet antidiurese.

Den høye TxGNN-scoren er en ren kunnskapsgraf-prediksjon uten identifisert biologisk begrunnelse. Vurderingen er at det ikke finnes en klar mekanistisk kobling mellom fentanyls opprinnelige bruk og den predikerte indikasjonen.

### Alternativ prediksjon: Tourettes syndrom (rang 2)

Modellen predikerer også **Tourettes syndrom** (score 99,05 %). Koblingen er svak og spekulativ: Det endogene opioidsystemet samspiller med dopaminerge baner i striatum, og noen få små studier har undersøkt andre opioidmodulatorer (f.eks. naltrekson, buprenorfin) mot tics. Dette er ikke evidens for fentanyl, som har høy misbruks- og avhengighetsrisiko, risiko for respirasjonsdepresjon og dårlig sikkerhetsprofil for en kronisk, ofte pediatrisk, nevroutviklingsrelatert tilstand. Heller ikke her er det identifisert kliniske studier eller litteratur.

---

## Evidens fra kliniske studier

Foreløpig er ingen relaterte kliniske studier registrert.

---

## Litteraturevidens

Foreløpig er ingen relatert litteratur tilgjengelig.

---

## Markedsinformasjon for Norge

| Godkjenningsnummer | Produktnavn | Doseringsform | Godkjent indikasjon |
|---------|------|------|-----------|
| EMEA/H/C/000833 | Effentora | Ikke oppgitt | Smerte; kreft (avregistrert) |
| EMEA/H/C/001164 | PecFent | Ikke oppgitt | Smerte; kreft (avregistrert) |
| EMEA/H/C/000959 | Instanyl | Ikke oppgitt | Smerte; kreft (avregistrert) |

---

## Sikkerhetsvurderinger

- **Kontraindikasjoner fra kunnskapsgrafen (ikke preparatomtale):** TxGNN-kunnskapsgrafen (PrimeKG) knytter fentanyl til en rekke kontraindikasjonsrelasjoner, blant annet:
  - Hjerte- og sirkulasjon: hypertensjon, ortostatisk hypotensjon, postural ortostatisk takykardisyndrom, lavt blodtrykk, langt QT-syndrom (inkl. familiært) og torsades de pointes
  - Lunge: kols og astma (inkl. allergisk og intrinsikk astma)
  - Lever, nyre og mage-tarm: leversvikt, leversykdom, nyresykdom, pyoureter, pankreatitt, galleblæresykdom og inflammatorisk tarmsykdom
  - Nevrologi og psykiatri: multisystematrofi, sykdom i basalgangliene, fokal håndtrekk (dystoni), blefarospasme, angstlidelse, nevrotisk lidelse, dystymi og rusmiddelmisbruk/-avhengighet
  - Andre: kaliummangel og benign prostatahyperplasi
- **Legemiddelinteraksjoner:** 100 interaksjoner er registrert. Viktige eksempler med alvorlighetsgrad **Major**: alvimopan, aprepitant, bupropion, klaritromycin, klotrimazol, deksametason, deksfenfluramin, dolasetron, fenfluramin, granisetron og lorkaserin. Eksempler med **Moderat** alvorlighetsgrad: atropin, cimetidin, klidinium, dicyklomin, dronabinol, eluxadolin, glyserolfenylbutyrat, glykopyrronium og hyoscyamin.

Det er ikke innhentet informasjon om advarsler og kontraindikasjoner fra preparatomtalen. Se preparatomtalen for fullstendig sikkerhetsinformasjon.

---

## Konklusjon og neste steg

**Beslutning: Hold**

**Begrunnelse:**
Prediksjonen bygger kun på en modellscore (evidensnivå L5), uten kliniske studier, litteratur eller plausibel mekanistisk kobling. Fentanyl har dessuten betydelige sikkerhetsrisikoer, mange interaksjoner, og kun avregistrerte godkjenninger i Norge.

**For å gå videre kreves følgende:**
- Innhente preparatomtale med advarsler og kontraindikasjoner (blokkerende datagap for sikkerhetsscreening)
- Innhente data om virkningsmekanisme (MOA) fra DrugBank
- Påvise en biologisk begrunnelse for effekt ved NSIAD (eller Tourettes syndrom), for eksempel gjennom prekliniske studier
- Vurdere om administrasjonsvei og formulering er forenlige med den nye indikasjonen
- Gjennomgå risiko–nytte, særlig knyttet til avhengighet, respirasjonsdepresjon og interaksjoner
## Ansvarsfraskrivelse

Dette innholdet er kun til forskningsformål og utgjør ikke medisinsk rådgivning.
Klinisk validering kreves før enhver klinisk anvendelse.

---

