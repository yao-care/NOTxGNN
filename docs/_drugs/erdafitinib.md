---
layout: default
title: Erdafitinib
parent: Kun modellprediksjon (L5)
nav_order: 138
evidence_level: L5
indication_count: 6
---

# Erdafitinib
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

# Erdafitinib: Fra FGFR-alterert ondartetsykdom til pulmonær hypertensjon

## Sammendrag på én setning

Erdafitinib er en pan-FGFR1-4-tyrosinkinasehemmer som brukes innen onkologi; den spesifikke originale indikasjonenn er ikke tilgjengelig i denne evidenspakken, og legemidlet er for tiden **ikke markedsført i Norge**.
TxGNN-modellen forutsier at det kan være effektivt for **pulmonær hypertensjon**, men dette er for tiden støttet av **0 kliniske forsøk** og **0 publikasjoner** — prediksjonen er kun modellbasert, og selv den mekanistiske begrunnelsen flagrer at effektens retning (beskyttende vs. skadelig) er ubekreftet.

---

## Rask oversikt

| Punkt | Innhold |
|-------|---------|
| Original indikasjon | Ikke dokumentert i evidenspakken (legemidlet er ikke markedsført i Norge; ingen lisensoppføringer tilgjengelig) |
| Forutsagt ny indikasjon | Pulmonær hypertensjon |
| TxGNN-prediksjonspoeng | 99.38% (rang 6453) |
| Bevisnivå | L5 (kun modellpreduksjon, ingen klinisk/litteraturstøtte) |
| Markedsstatus i Norge | ✗ Ikke markedsført |
| Antall godkjennelser | 0 |
| Anbefalt beslutning | Avvent |

---

## Hvorfor er denne prediksjonen rimelig?

For tiden er detaljerte data om virkningsmekanisme ikke tilgjengelig (flagget som et høyalvor datakløft, DG002). Basert på informasjonen i denne evidenspakken er erdafitinib beskrevet som en **pan-FGFR1-4-hemmer**, og dets begrunnelsestekst noterer at FGF/FGFR1-signalisering er kjent for å delta i pulmonær vaskulær remodellering og PAH-patogenese — en rolle tidligere utforsket med andre multi-kinasehemmere som imatinib i PAH-forskning.

Imidlertid er retningslinjen for dette forholdet eksplisitt usikker: FGFR-signalisering kan enten drive eller beskytte mot vaskulær remodellering avhengig av kontekst, og evidenspakken selv angir at erdafitinib's effekt på denne veien "尚待驗證，亦可能有害" (retning ubekreftet, potensial for skade). Dette betyr at den mekanistiske linken er teoretisk plausibel, men ikke validert, og bør behandles som en forskningshypotese snarere enn en etablert farmakologisk begrunnelse.

Ingen data som forbinder erdafitinib's (ukjent, per denne pakken) originale indikasjon til pulmonær hypertensjon er tilgjengelig, så lignende indikasjonsbegrunnelse kan ikke vurderes på dette tidspunktet.

---

## Evidens fra kliniske forsøk

For tiden ingen relaterte kliniske forsøk registrert.

---

## Litteraturbevis

For tiden ingen relatert litteratur tilgjengelig.

---

## Markedsopplysninger for Norge

Erdafitinib har for tiden **ingen markedsføringstillatelser i Norge** (0 lisenser, markedsstatus: Ikke markedsført). Ingen data på produktnivå (legemiddelform, godkjent indikasjonnnstekst) er tilgjengelig.

---

## Cytotoksisitet

Erdafitinib er et antineoplasmamiddel (pan-FGFR1-4-kinasehemmer brukt ved FGFR-alterert ondartetsykdom), så denne delen gjelder.

| Punkt | Innhold |
|-------|---------|
| Cytotoksisitetsklassifisering | Målrettet terapi (FGFR1-4-tyrosinkinasehemmer) |
| Risiko for myelosuppresjon | Se pakningsvedlegget for advarsler og forholdsregler |
| Emetogenitetsklassifisering | Se pakningsvedlegget for advarsler og forholdsregler |
| Overvåkingspunkter | Se pakningsvedlegget for advarsler og forholdsregler |
| Håndteringsbeskyttelse | Se pakningsvedlegget for advarsler og forholdsregler |

---

## Sikkerhetshensyn

Se pakningsvedlegget for sikkerhetsinformasjon.

*(Merk: TFDA/Norge-etikettvarsler og kontraindikasjoner er flagget som et blokkerende datakløft (DG001) — dette må løses før noen Stage 1-sikkerhetsvurdering kan fortsette.)*

---

## Andre forutsagte indikasioner (lavere selvtillit, samme modellkjøring)

For kontekst flagret TxGNN også fem ytterligere kandidatindikasioner for erdafitinib, alle på bevisnivå L5 uten støttende kliniske forsøk eller litteratur (bortsett fra én ikke-spesifikk oversikt for revmatoid artritt). Ingen endrer den overordnede anbefalingen:

| Rang | Sykdom | Poeng | Anbefaling | Mekanistisk merknad |
|------|--------|-------|------------|-------------------|
| 2 | Kyfoskoliotisk hjertesykdom | 99.27% | Avvent | Ingen direkte mekanistisk forbindelse; sekundær hjertesykdom, ikke FGFR-drevet |
| 3 | Amenoré | 99.26% | Avvent | Ingen kjent mekanistisk forbindelse |
| 4 | Revmatoid artritt | 99.25% | Avvent | Kun én ikke-spesifikk 2020 kinasehemmer-oversikt (PMID 31862477); ingen RA-spesifikk data |
| 5 | Amyotrofisk lateral sklerose | 99.06% | Avvent | Mekanismen kan løpe i motsatt retning (FGF/FGFR-agonisme, ikke inhibisjon, er neuroprotektiv) |
| 6 | Brachydaktyly-syndaktyly-syndrom | 99.03% | Forskningsspørsmål | Sterkeste mekanistisk plausibilitet (FGFR1-3-gevinst av-funksjon driver disse skjelettsyndromerene), men null klinisk/preklinisk data |

---

## Konklusjon og neste trinn

**Beslutning: Avvent**

**Begrunnelse:**
Prognosen for pulmonær hypertensjon støttes kun av en TxGNN-poengsum med null kliniske forsøk og null litteratur, og den mekanistiske begrunnelsen selv innrømmer at effektens retning er ubekreftet og potensielt skadelig — dette er en ren S0/L5-forskningshypotese, ikke et handlingsbar reposisjonseringssignal.

**For å fortsette, er følgende nødvendig:**
- Løs DG001 (TFDA/Norge-etikettvarsler og kontraindikasjoner) — for tiden blokkering
- Løs DG002 (bekreftet virkningsmekanisme fra DrugBank)
- Preklinisk bevis som etablerer om FGFR-inhibisjon hjelper eller forverrer pulmonær vaskulær remodellering
- Et dedikert litteratur-/klinisk forsøkssøk spesielt for "erdafitinib + pulmonær hypertensjon"
- Bekrefting av markedsføringstilstatus i Norge (for tiden 0 lisenser på fil)

## Ansvarsfraskrivelse

Dette innholdet er kun til forskningsformål og utgjør ikke medisinsk rådgivning.
Klinisk validering kreves før enhver klinisk anvendelse.

---

