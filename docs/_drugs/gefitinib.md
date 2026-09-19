---
layout: default
title: Gefitinib
parent: Kun modellprediksjon (L5)
nav_order: 159
evidence_level: L5
indication_count: 10
---

# Gefitinib
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

# Gefitinib: Fra ikke-småcellet lungekarsinom til Fibromatose, Gingival

## Ensetningssammendrag

> Gefitinib er en EGFR-tyrosinkinasehemmer av første generasjon (EGFR-TKI) kjent klinisk for behandling av EGFR-mutant ikke-småcellet lungekarsinom (NSCLC).
> TxGNN-modellen forutsier at det kan være effektivt for **Fibromatose, Gingival**, men denne retningen støttes for tiden av **0 kliniske forsøk** og **0 publikasjoner** — det er en modellscore-bare-prediksjon uten mekanistisk eller empirisk grunnlag.

---

## Rask oversikt

| Emne | Innhold |
|------|---------|
| Opprinnelig indikasjon | Ikke registrert i det lokale regulatoriske registeret (0 lisenser på fil). Basert på kjent farmakologi er gefitinib en EGFR-TKI indisert for EGFR-mutasjonspositivt ikke-småcellet lungekarsinom (NSCLC). |
| Prediktert ny indikasjon | Fibromatose, Gingival |
| TxGNN-prediktjonsscore | 99.89% |
| Bevisnivoå | L5 |
| Markedsstatus i Norge | Ikke markedsført (Ikke markedsført) |
| Antall autorisasjoner | 0 |
| Anbefalt beslutning | Avvent |

---

## Hvorfor er denne prediksjonen rimelig?

For tiden er detaljerte virkningsmekanisme-data ikke tilgjengelig fra det lokale registeret (datagap DG002). Basert på kjent farmakologisk informasjon fra bevisepakken selv, er gefitinib en EGFR-tyrosinkinasehemmer av første generasjon som blokkerer EGFR-autofosforyering og nedstrøms RAS/MEK/ERK-signalering, og det er standard-behandlings-mekanismen for EGFR-mutant NSCLC.

Gingival fibromatose er imidlertid en godartet bindevevs-vekstsyndrom uten etablert forbindelse til EGFR-drevet onkogen signalering. Bevisepakkens egen mekanistiske vurdering for denne kandidaten sier eksplisitt at det **ikke finnes noen kjent mekanistisk forbindelse** mellom gefitinibs EGFR-TKI-aktivitet og gingival fibromatose, og det finnes ingen klinisk forsøk eller litteraturbevis som støtter assosiasjonen. Denne kandidaten ser derfor ut til å være et rent kunnskapsgraff-score-artefakt (TxGNN rank 1590) snarere enn en biologisk grunnfestet ombrukshypotese.

Det er verdt å merke seg at flere lavere-rangerte prediksjoner i denne bevisepakken (f.eks. lungerot-karsinom, lunges gjermcelletumor, pulmonalt sulkus-neoplasme) er anatomisk og mekanistisk nærmere gefitinibs etablerte NSCLC-indikasjon, selv om selv disse mangler indikasjonsspesifikk forsøks- eller litteraturbekrefelse. Se Konklusjon for videre diskusjon.

---

## Bevis for kliniske forsøk

For tiden er det ingen relaterte kliniske forsøk registrert.

---

## Litteraturbevis

For tiden er det ingen relatert litteratur tilgjengelig.

---

## Markedsinformasjon for Norge

Gefitinib har for tiden **ingen markedsføringstillatelse** i Norge (0 lisenser på fil; markedsstatus: Ikke markedsført / Ikke markedsført).

---

## Cytotoksisitet

Gefitinib er et anti-neoplastisk middel (opprinnelig indikasjonklasse: NSCLC; stoffklasse bekreftet på tvers av bevisepakkens egen mekanistiske begrunnelse som en EGFR-tyrosinkinasehemmer).

| Emne | Innhold |
|------|---------|
| Cytotoksisitetsklassifisering | Målrettet terapi (EGFR-tyrosinkinasehemmer; ikke et konvensjonelt cytotoksisk kjemoterapi-middel) |
| Risiko for myelosuppresjon | Vær vennlig å se pakkeseddelens advarsler og forholdsregler |
| Emetogenisitetsklassifisering | Vær vennlig å se pakkeseddelens advarsler og forholdsregler |
| Overvåkingselementer | Vær vennlig å se pakkeseddelens advarsler og forholdsregler |
| Håndteringsbeskyttelse | Vær vennlig å se pakkeseddelens advarsler og forholdsregler |

---

## Sikkerhetshensyn

Vær vennlig å se pakkesedlen for sikkerhetsinformasjon.

---

## Konklusjon og neste trinn

**Beslutning: Avvent**

**Begrunnelse:**
Den presenterte prediksjonen (gingival fibromatose, TxGNN-score 99.89%) har ingen klinisk forsøks- eller litteraturstøtte og ingen plausibel mekanistisk forbindelse — det er en modellscore-bare (L5) assosiasjon. Dette forverres av et **blokkerende** datagap (DG001: TFDA/lokale merkininger for advarsler og kontraindikasjoner utilgjengelige), som forhindrer selv en innledende sikkerhetskontroll (S1), og ved at stoffet ikke har noen markedsføringstillatelser lokalt.

**For å fortsette, trengs følgende:**
- Løse DG001 (få tak i og tolke den offisielle pakkeseddelen for advarsler/kontraindikasjoner) før noen S1-sikkerhetsevaluering kan foregå.
- Løse DG002 (bekrefte MOA via DrugBank API) for å riktig dokumentere mekanistisk begrunnelse.
- Hvis gingival fibromatose forblir målet, generere en spesifikk mekanistisk hypotese og søke preklinisk/casenivå-bevis — ingen finnes for tiden.
- Vurder å omfokusere evalueringen mot de mer anatomisk plausible kandidatene i denne pakken (rank 5, lungerot-karsinom, som nådde beslutningstrin S1 / «Forskningsspørsmål»), som — selv om fortsatt svakt støttet — er mekanistisk nærmere gefitinibs etablerte NSCLC-aktivitet.

## Ansvarsfraskrivelse

Dette innholdet er kun til forskningsformål og utgjør ikke medisinsk rådgivning.
Klinisk validering kreves før enhver klinisk anvendelse.

---

