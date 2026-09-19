---
layout: default
title: Crizotinib
parent: Kun modellprediksjon (L5)
nav_order: 93
evidence_level: L5
indication_count: 10
---

# Crizotinib
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

# Crizotinib: Fra ALK-positiv ikke-småcellet lungecancer til fibromatosis, gingival

## Ensetnings sammendrag

Crizotinib er en oral ALK/ROS1/MET-tyrosinkinasehemmer; formelle taiwanske regulatoriske og DrugBank MOA-poster mangler for øyeblikket fra denne bevisspakken, men litteraturen som er inkludert i dette kandidatsett identifiserer konsistent dens etablerte bruk som ALK/ROS1-omarrangert ikke-småcellet lungecancer (NSCLC). TxGNN-modellens høyest rangerte prediksjon i denne gruppen er **Gingival fibromatosis (Fibromatosis, Gingival)**, men denne prediksjonen støttes for øyeblikket av **null kliniske studier** og **null publikasjoner**, noe som gjør det til en rent beregningmessig hypotese uten mekanistisk bekrefting.

---

## Hurtigoversikt

| Punkt | Innhold |
|-------|---------|
| Opprinnelig indikasjon | Ikke registrert i taiwanske regulatoriske data (legemiddel ikke markedsført, 0 lisenser); litteraturen i denne bevisspakken indikerer at etablert bruk er ALK/ROS1-positiv NSCLC |
| Predikert ny indikasjon | Gingival fibromatosis |
| TxGNN prediksjonspoeng | 99.81% |
| Bevisnivå | L5 (kun modellprediksjon, ingen støttende studier) |
| Taiwan markedsstatus | Ikke markedsført (Ikke markedsført) |
| Antall godkjenninger | 0 |
| Anbefalt beslutning | Stopp |

---

## Hvorfor er denne prediksjonen rimelig?

Detaljerte virkningsmekanisme-data for crizotinib er ikke direkte registrert i denne bevisspakken (Datagap DG002, høy alvorlighetsgrad). Basert på litteraturbeviser vedlagt andre steder i dette samme kandidatsettett, er crizotinib kjent for å være en ATP-kompetitiv småmolekyl-hemmer av reseptor-tyrosinkinasene ALK, ROS1 og c-Met/MET, godkjent for NSCLC med EML4-ALK omarrangeringer og ROS1-fusjoner.

Gingival fibromatosis er en godartad, ikke-neoplastisk fibrøs overvekst av gingivalt bindevev, typisk drevet av genetiske (f.eks. *SOS1*) eller legemiddelinduserte fibroblast-proliferasjonveier — en biologi som ikke er knyttet til ALK/ROS1/MET-reseptor-tyrosinkinase-signalering. Beviskasets eget resonnement for denne kandidaten sier eksplisitt: *"無任何機轉關聯報導；牙齦纖維瘤病與 ALK/ROS1/MET 路徑無已知連結，僅為 TxGNN 純預測分數"* (ingen mekanistisk sammenheng rapportert; ingen kjent forbindelse mellom ALK/ROS1/MET og gingival fibromatosis patogenese — dette er en ren TxGNN poengsum uten støttende biologi).

Bemerkelsesverdig nok inneholder denne samme kandidatgruppen flere andre crizotinib-predikerte indikasjoner med markant sterkere beviser — f.eks. rangering 4 "lungehilus-karsinom" (L3, Fortsett med sikringstiltak) og rangering 5 "godartad lungesvulst" (L1, 20 publikasjoner, selv om det sannsynligvis er en ontologi-etikettfeilmatch som peker tilbake til crizotinibs allerede kjente ALK/ROS1-positive NSCLC-indikasjon). Dette tyder på at modellens sanne, biologisk funderte signal for crizotinib grupperer seg rundt lunge/ALK-ROS1-drevne svulster, ikke gingival fibromatosis, noe som forsterker at den høyest rangerte prediksjonen her bør behandles med forsiktighet snarere enn som den sterkeste omformålskandidaten i dette settet.

---

## Bevis fra kliniske studier

For øyeblikket er ingen relaterte kliniske studier registrert.

---

## Litteraturbeviser

For øyeblikket er ingen relatert litteratur tilgjengelig.

---

## Taiwan markedsinformasjon

Ingen markedsføringstillatelser er for øyeblikket registrert i Taiwan — crizotinib er ikke markedsført i Taiwan under denne kandidatposten (0 lisenser).

---

## Cytotoksisitet

Crizotinib er et antineoplastisk middel (målrettet terapi) basert på litteraturen som er inkludert i denne bevisspakken, selv om formelle DrugBank-kategori-/toksisitetsfelt ikke ble gitt.

| Punkt | Innhold |
|-------|---------|
| Klassifisering av cytotoksisitet | Målrettet terapi (ALK/ROS1/MET-tyrosinkinasehemmer), ikke konvensjonell cytotoksisk kjemoterapi |
| Risiko for myelosuppresjon | Vennligst se pakningsvedlegget for advarsler og forholdsregler (ingen toksisitetsdata gitt i denne bevisspakken) |
| Klassifisering av emetogenisitet | Vennligst se pakningsvedlegget for advarsler og forholdsregler |
| Overvåkingspunkter | Vennligst se pakningsvedlegget for advarsler og forholdsregler |
| Håndteringsbeskyttelse | Vennligst se pakningsvedlegget for advarsler og forholdsregler |

---

## Sikkerhetshensyn

Vennligst se pakningsvedlegget for sikkerhetsinformasjon.

*Merk: TFDA advarsler/kontraindikasjoner datahenting er for øyeblikket flagget som et blokkerende datagap (DG001) — dette må løses før noen S1-sikkerhetsvurdering kan fortsette.*

---

## Konklusjon og neste trinn

**Beslutning: Stopp**

**Begrunnelse:**
Den høyest rangerte prediksjonen (Gingival fibromatosis) har et L5-bevisnivå — ingen kliniske studier, ingen publikasjoner, og ingen plausibel mekanistisk sammenheng med crizotinibs kjente ALK/ROS1/MET-mål. Kombinert med et blokkerende gap i TFDA-etikett data og et gap med høy alvorlighetsgrad i bekreftet MOA, oppfyller denne spesifikke kandidaten ikke minimumskravet til bevis for å fortsette.

**For å fortsette, er følgende nødvendig:**
- TFDA pakningsvedlegg (advarsler/kontraindikasjoner) — Blokkering datagap DG001
- Bekreftet DrugBank MOA-post — Høy alvorlighetsgrad datagap DG002
- Preklinisk eller mekanistisk beviser som direkte knytter ALK/ROS1/MET-signalering til gingival fibromatosis patogenese
- Revurdere denne kandidatsettets høyere-bevis poster (rangering 4 "lungehilus-karsinom," L3; rangering 5 "godartad lungesvulst," L1) som mer lovende omformålsretninger, avhengig av ontologi-etikettverifisering mot crizotinibs kjente NSCLC-indikasjon

## Ansvarsfraskrivelse

Dette innholdet er kun til forskningsformål og utgjør ikke medisinsk rådgivning.
Klinisk validering kreves før enhver klinisk anvendelse.

---

