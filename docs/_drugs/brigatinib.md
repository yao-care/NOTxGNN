---
layout: default
title: Brigatinib
parent: Kun modellprediksjon (L5)
nav_order: 57
evidence_level: L5
indication_count: 10
---

# Brigatinib
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

# Brigatinib: Fra ALK-positiv NSCLC til gingivale fibromatose

## Sammendrag på én setning

Brigatinib er en andregenrasjons ALK/ROS1-tyrosinkinaseinhibitor hvis etablerte kliniske bruk – dokumentert gjennom denne evidenspakkens egen litteratur – er ALK-positiv ikke-småcellet lungekreft (NSCLC); dette fanges imidlertid ikke opp i det strukturerte `original_indications`-feltet (datagap). TxGNN-modellens **høyest rangerte** prediksjon er **gingivale fibromatose**, men dette spesifikke signalet støttes av **0 kliniske forsøk** og **0 publikasjoner**, og evidenspakkens egen mekanistiske kommentar flagget eksplisitt det som sannsynlig kunnskapsgrafinnebygging-støy snarere enn et genuint biologisk signal.

---

## Hurtigoversikt

| Element | Innhold |
|------|------|
| Original indikasjon | ALK-positiv NSCLC (sluttet fra litteratur innenfor denne pakken; ikke registrert i strukturert lisensdata — se Datagap) |
| Predikert ny indikasjon | Gingivale fibromatose |
| TxGNN prediksjonsscore | 99.89% |
| Evidensnivå | L5 |
| Status på Norges marked | ✗ Ikke markedsført |
| Antall autorisasjoner | 0 |
| Anbefalt beslutning | **Avvente** |

---

## Hvorfor er denne prediksjonen rimelig?

Detaljerte virkningsmekanisme-data er ikke tilgjengelige i det strukturerte `original_moa`-feltet (markert som et datagap). Imidlertid identifiserer evidenspakkens egen begrunnelsestekst gjentatte ganger brigatinib som en **andregenrasjons ALK/ROS1-tyrosinkinaseinhibitor**, i samsvar med dens kjente kliniske rolle i ALK-positiv NSCLC.

For den høyest rangerte prediksjonen, **gingivale fibromatose**, eksisterer ingen mekanistisk sammenheng: denne tilstanden drives av gener som *SOS1* og *REST*, eller av generell fibroblastproliferasjon, og har ingen kjent relasjon til ALK/ROS1-signalering. Det finnes null støttende kliniske forsøk eller publikasjoner. Evidenspakkens egen ombruk-begrunnelse konkluderer eksplisitt at denne høye TxGNN-scoren sannsynligvis er embedding-støy snarere enn et ekte signal — en konklusjon denne rapporten godtar.

**Viktig kontekst utover rangering 1:** av de 10 prediksjoner i denne batchen, 7 (rangeringer 1–4, 6, 7, 9) har ingen støttende litteratur og får riktig score L5/Avvente. De resterende 3 (rangeringer 5, 8, 10) når L4/"Forskningsspørsmål," men nærmere lesning viser at alle tre lider av **sykdomsetikett-mismatch** snarere enn direkte støtte for den navngitte indikasjonen:
- **Rangering 5 ("benign lungetumon")** — den siterte litteraturen (ALTA-1L, NEJM 2018/2021) handler faktisk om ALK+ *ondartet* NSCLC, dvs. brigatinibs kjente godkjente bruk, ikke en ny indikasjon for benigntumon.
- **Rangering 8 ("lunges germcelletumon")** — litteraturen gjelder brigatinibaktivitet i andre sjeldne ALK-fusjonpositive tumorer (neuroblastom, feokromosytom, LCNEC), ikke germcelletumorer spesifikt; dette er indirekte, pan-tumor basket-evidens bare.
- **Rangering 10 ("Leukomelanoderma-infantilisme-intellektuell funksjonshemning-hypodontia-hypotrikose syndrom")** — dette er det mest bemerkelsesverdige funnet i datasettet. Den faktiske litteraturen (inkludert et 2024 *NEJM*-studie, PMID 38904277) dokumenterer brigatinibaktivitet i **NF2-relatert schwannomatose**, en urelatert men reell og mekanistisk plausibel kandidatindikasjon som ingenting har å gjøre med syndromet navngitt i denne raden. Dette virker å være et genuint ombruk-signal feilkoblet til feil sykdomsetikett og ville fortjene en dedikert, riktig-merket evaluering.

Ingen av dette støtter imidlertid rang-1-kandidaten (gingivale fibromatose) som denne rapporten formelt evaluerer.

---

## Evidens fra kliniske forsøk

For tiden er det ingen relaterte kliniske forsøk registrert.

---

## Litteraturbevis

For tiden er ingen relatert litteratur tilgjengelig.

---

## Informasjon om Norges marked

Brigatinib er ikke for tiden markedsført i Norge. Ingen autorisasjoner er registrert (`total_licenses: 0`).

---

## Cytotoksisitet (kun for antineoplastiske legemidler)

| Element | Innhold |
|------|------|
| Cytotoksisitet-klassifisering | Målrettet terapi (ALK/ROS1-tyrosinkinaseinhibitor) |
| Risiko for myelosuppresjon | Se pakningsvedlegg for advarsler og forholdsregler |
| Emetogenisitet-klassifisering | Se pakningsvedlegg for advarsler og forholdsregler |
| Overvåkingspunkter | Se pakningsvedlegg for advarsler og forholdsregler |
| Håndteringsbeskyttelse | Se pakningsvedlegg for advarsler og forholdsregler |

---

## Sikkerhetshensyn

Se pakningsvedlegg for sikkerhetsinformasjon. Merk: TFDA/DMP-etikett-advarsler og kontraindikasjoner er flagget i denne evidenspakken som et **blokkerende** datagap (DG001) — dette legemidlet kan ikke gå videre til en S1 sikkerhetsvurdering før etikett-data er innhentet.

---

## Konklusjon og neste trinn

**Beslutning: Avvente**

**Begrunnelse:**
Den høyest rangerte prediksjonen (gingivale fibromatose) har ingen klinisk, litteraturbasert, eller mekanistisk støtte og er vurdert i killedataene selv som sannsynlig modellstøy. Kombinert med legemidlets ikke-markedsførte status i Norge og et blokkerende gap i etikett-/sikkerheetsdata, finnes det ikke grunnlag for å fremme denne spesifikke kandidaten.

**For å gå videre, kreves følgende:**
- TFDA/DMP-etikett (advarsler, kontraindikasjoner) — Blokkering-gap (DG001)
- Bekreftet virkningsmekanisme-data via DrugBank API — Høy prioritet-gap (DG002)
- Dersom videre arbeid med ombruk av dette legemidlet planlegges, åpne en **separat, riktig-merket evaluering for NF2-relatert schwannomatose**, basert på den ekte fase 2-evidensen (NEJM 2024) som fremkom under rank-10-inngangen — dette er en vesentlig sterkere kandidat enn noen indikasjon som for tiden er rangert i denne batchen

## Ansvarsfraskrivelse

Dette innholdet er kun til forskningsformål og utgjør ikke medisinsk rådgivning.
Klinisk validering kreves før enhver klinisk anvendelse.

---

