---
layout: default
title: Sotatercept
parent: Kun modellprediksjon (L5)
nav_order: 331
evidence_level: L5
indication_count: 10
---

# Sotatercept
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

# Sotatercept: Fra Pulmonal Arteriell Hypertensjon til Akutt Lymfoblastisk Leukemi

## Sammendrag på en setning

> Sotatercept (DB12118) er et ActRIIA-Fc fusjonprotein som for tiden er markedsført for pulmonal arteriell hypertensjon (PAH) og fungerer som en aktivin/TGF-β superfamilie signallingsfelle.
> TxGNN-modellen forutsier at det kan være effektivt for **Akutt Lymfoblastisk Leukemi**,
> men denne prediksjonen er for tiden støttet av **0 kliniske forsøk** og **0 publikasjoner** — det er et rent modelltopologisignalt uten noen bekreftelsesevidens.

---

## Rask oversikt

| Element | Innhold |
|---------|---------|
| Original indikasjon | Ikke tilgjengelig i strukturerte data (lisenser tomme); legemiddel er globalt kjent som behandling for pulmonal arteriell hypertensjon per grunnlagstekst |
| Forutsagt ny indikasjon | Akutt Lymfoblastisk Leukemi (sykdom) |
| TxGNN Prediksjonspoengsum | 99.78% |
| Evidensnivå | L5 (kun modellprediksjon, ingen klinisk eller litteraturstøtte) |
| Markedsstatus Norge | ✗ Ikke markedsført |
| Antall autorisasjoner | 0 |
| Anbefalt beslutning | Avvent |

---

## Hvorfor er denne prediksjonen rimelig?

For tiden er detaljert virkningsmekanisme-data ikke tilgjengelig i den strukturerte legemiddelposten (`original_moa` = Datakløft). Basert på kontekstinformasjon innebygd i evidenspakkens grunnlagstekst, beskrives sotatercept som et ActRIIA-Fc fusjonprotein som fanger aktivin/TGF-β superfamilie-ligander, primært som regulerer erytrocyttmodning og vaskulær remodellering — mekanismer som er konsistent med dets kjente godkjente bruk ved pulmonal arteriell hypertensjon (PAH).

Det finnes ingen kjent patofysiologisk forbindelse mellom PAH og akutt lymfoblastisk leukemi. Evidenspakken selv uttaler klart: *"Det finnes ingen kjent patofysiologisk forbindelse mellom PAH og ALL, høy TxGNN-poengsum reflekterer kun kunnskapsgrafs topologiske likhet, ikke mekanismebevis"* — det vil si at høy TxGNN-poengsum reflekterer graftopologisk likhet i kunnskapsgrafen snarere enn noen biologisk mekanisme som knytter de to tilstandene sammen.

Bemerkelsesverdig er det at 9 av de 10 forutsagte indikasjonene i denne evidenspakken (alvorlig diabetisk retinopati, legemiddelutløst osteoporose, HER2+ brystkreft, flere sjeldne undertyper av urothelial karsinoma, osv.) viser samme mønster: høye TxGNN-poengsum med null støttende forsøk eller litteratur. Den gjentatte klyngingen av urothelial karsinoma-undertyper (ranger 7–10) spesielt foreslår en systematisk modellartefakt — sannsynligvis nodeSparsitet i kunnskapsgrafen for disse sjeldne kreftsubtypene — snarere enn et genuint repurposeringsignalt. Ingen av de 10 kandidatene stiger for tiden over L5-bevis.

---

## Evidens fra kliniske forsøk

For tiden ingen relaterte kliniske forsøk registrert

---

## Litteraturbevis

For tiden ingen relatert litteratur tilgjengelig

---

## Markedsinformasjon Norge

Sotatercept er for tiden **ikke markedsført i Norge** — ingen produktautorisasjoner er registrert (`total_licenses = 0`).

---

## Sikkerhetsvurderinger

Se pakningsvedlegget for sikkerhetsinformasjon.

*(Merk: `taiwan_regulatory` advarsler/kontraindikasjoner og TFDA-etikettdata er flagget som en **Blokkering** datakløft (DG001) i denne evidenspakken — sikkerhetsvurdering kan ikke gå videre til fase S1 før dette er løst.)*

---

## Konklusjon og neste trinn

**Beslutning: Avvent**

**Grunnlag:**
Den høyest rangerte prediksjonen (akutt lymfoblastisk leukemi) — og alle 9 andre kandidater i denne pakken — hviler helt og holdent på TxGNN topologisk poengsum (L5) med null kliniske forsøk og null litteraturstøtte. Det finnes ingen plausibel mekanistisk bro mellom sotatercepts kjente aktivinfelle/PAH-farmakologi og hematologisk ondartelse. Flere lavere rangerte kandidater foreslår ytterligere modelstøy fra sparsomatiske grafinoter (f.eks. gjentatte sjeldne urothelial karsinoma-undertyper) snarere enn genuint signalt.

**For å fortsette er følgende nødvendig:**
- Løs DG001 (Blokkering): skaff TFDA/reguleringsetikettadvarsler og kontraindikasjoner før noen S1-sikkerhetsskrenning kan begynne
- Løs DG002 (Høy): skaff bekreftet virkningsmekanisme (MOA) fra DrugBank API for å korrekt kunne evaluere mekanistisk plausibilitet
- Hvis ALL-hypotesen forfølges videre, etabler en målrettet litteratur-/preklinisk søk spesielt på aktivin/TGF-β signallering i leukemisk benmargsnisjé før noen investeringer på forsøksstadiet
- Gitt mønsteret av klyngede, ustøttede urothelial karsinoma-prediksjoner, vurder å flagge dette legemidlets KG-nabolag for gjennomgang av potensielle datasparsitets-artefakter i den underliggende TxGNN-modellen

## Ansvarsfraskrivelse

Dette innholdet er kun til forskningsformål og utgjør ikke medisinsk rådgivning.
Klinisk validering kreves før enhver klinisk anvendelse.

---

