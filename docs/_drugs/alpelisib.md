---
layout: default
title: Alpelisib
parent: Kun modellprediksjon (L5)
nav_order: 25
evidence_level: L5
indication_count: 1
---

# Alpelisib
{: .fs-9 }

Evidensnivå: **L5** | Predikerte indikasjoner: **1** stk.
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

# Alpelisib: Fra brystkreft til pulmonær hypertensjon

## Sammendrag på en setning

> Alpelisib er en PI3Kα-hemmer hvis virkelige brukssammenheng i bevissamlingen peker på HR+/HER2-negativ avansert eller metastatisk brystkreft (formelle felt for original-indikasjon og MOA er ikke utfylt i dette datasettet).
> TxGNN-modellen forutsier at det kan være effektivt for **Pulmonær hypertensjon**, med en prediksjonspoengsum på **99,03%**, men for øyeblikket støttes denne retningen av **0 direkte relevante kliniske studier** og **2 publikasjoner** — og begge publikasjonene beskriver medisinindusert pulmonær/kardial toksisitet i stedet for terapeutisk nytte.

---

## Rask oversikt

| Element | Innhold |
|---------|---------|
| Originalindikasjon | Brystkreft (HR+/HER2-negativ, avansert/metastatisk) — utledet fra klinisk forsøkskontekst; ikke formelt registrert i `taiwan_regulatory`/`original_indications` |
| Forutsagt ny indikasjon | Pulmonær hypertensjon |
| TxGNN-prediksjonspoengsum | 99,03% |
| Bevisnivå | L5 |
| Markedsstatus i Taiwan | ✗ Ikke markedsført |
| Antall godkjenninger | 0 |
| Anbefalt beslutning | Avvent |

---

## Hvorfor er denne prediksjonen rimelig?

Detaljert mekanismedata for alpelisib er ikke tilgjengelig i denne bevissamlingen (`original_moa: [Data Gap]`). Basert på den hentet litteraturkonteksten er alpelisib en PI3Kα (fosfoinositid-3-kinase alfa)-hemmer som brukes i onkologi, og dens effektivitet ved HR+/HER2-negativ brystkreft er godt etablert i det kliniske forsøksøkosystemet som refereres her (f.eks. den REASSURE virkelige verden-studien).

Den biologiske begrunnelsen bak TxGNN-modellens høye poengsum (0,99) ser ut til å hvile på PI3Kα/AKT/mTOR-signaleringsbanen, som er implisert i preklinisk litteratur som en bidragsyter til vaskulær ombygging i lunger — en kjernepathologisk mekanisme ved pulmonær arteriell hypertensjon (PAH). Denne delte banen er en plausibel grunn for at modellen knytter en brystkreftmedisin til en lungevaskulær sykdom.

Imidlertid støtter den faktiske evidensen som ble hentet for denne kandidaten **ikke** en terapeutisk fordel — den peker i motsatt retning. Det eneste kliniske forsøket som ble identifisert evaluerer en annen medisin (ribociclib) ved brystkreft og har ingen relevans for alpelisib eller pulmonær hypertensjon. De to litteraturkildene beskriver alpelisib-indusert **interstisiell lungesykdom** og **PI3Kα-veiinhibisjon-assosiert biventrikulær kardial atrofi/dysfunksjon** — begge som tyder på at alpelisib kan utgjøre kardiopulmonal risiko hos en populasjon som allerede har nedsatt kardiopulmonal reserve (PH-pasienter), i stedet for å tilby fordel. Dette er et tilfelle av et «prediksjonsbasert, mekanisme-bare» signal uten klinisk støtte og et motstridende sikkerhetssignal.

---

## Bevis fra kliniske studier

For øyeblikket finnes det ingen kliniske studier som direkte støtter alpelisib for pulmonær hypertensjon som er registrert.

*(Én studie, [NCT06705504](https://clinicaltrials.gov/study/NCT06705504), ble hentet av søket men ekskludert — det er en retrospektiv virkelige verden-studie av ribociclib og alpelisib hos HR+/HER2-negative brystkreftpasienter, urelatert til alpelisib eller pulmonær hypertensjon; gradert «C — ikke relevant» i bevisvurderingen.)*

---

## Litteraturbevis

| PMID | År | Type | Tidsskrift | Viktige funn |
|------|-----|------|------|---------|
| [35730191](https://pubmed.ncbi.nlm.nih.gov/35730191/) | 2023 | Kasuistikk | Journal of Oncology Pharmacy Practice | Rapporterer et tilfelle av alpelisib-indusert interstisiell lungesykdom (progressiv lungefibrose) hos en pasient som ble behandlet for avansert brystkreft — et sikkerhetssignal, ikke effektivitetsbevis, for pulmonale indikasjoner |
| [31039672](https://pubmed.ncbi.nlm.nih.gov/31039672/) | 2019 | Preklinisk/Translasjonell | Journal of the American Heart Association | Preklinisk studie som viser at PI3Kα-veiinhibisjon (mekanismeklassen alpelisib tilhører) forårsaker distinkt biventrikulær kardial atrofi, ombygging og høyre ventrikel-dysfunksjon — høyre ventrikel-dysfunksjon er en viktig bekymring i pulmonær hypertensjon-behandling |

---

## Markedsinformasjon for Taiwan

Alpelisib er for øyeblikket **ikke markedsført** i Taiwan — `taiwan_regulatory.total_licenses = 0`, og ingen autorisasjonsposter er tilgjengelig i bevissamlingen.

---

## Cytotoksisitet

*(Inkludert fordi alpelisib er en onkologi-agent per sin kjente kliniske brukssammenheng i den hentet forsøksbevis.)*

| Element | Innhold |
|---------|---------|
| Cytotoksisitetsklassifikasjon | Målrettet terapi (PI3Kα-hemmer) — ikke en konvensjonell cytotoksisk kjemoterapiagent, basert på tilgjengelig kontekst |
| Risiko for myelosuppresjon | Ingen myelosuppresjondata tilgjengelig i denne bevissamlingen — se produktinformasjonen |
| Emetogenitetsklassifikasjon | Ingen data tilgjengelig i denne bevissamlingen — se produktinformasjonen |
| Overvåkingspunkter | Utover rutinemessig CBC/lever/nyreovervåking, tyder de hentet litteraturbiler på at lungefunction/bildeovervåking (risiko for interstisiell lungesykdom) og kardial funksjonsvurdering (risiko for biventrikulær atrofi/høyre ventrikel-dysfunksjon) fortjener oppmerksomhet |
| Håndteringsbeskyttelse | Oral småmolekyl målrettet terapi; intet cytotoksisk-medisin håndteringskrav er etablert i denne bevissamlingen — se institusjonell onkologi-medisin håndtelingspolicy |

---

## Sikkerhetshensyn

Se produktinformasjonen for sikkerhetsinformasjon.

*(Merknad: TFDA-produktinformasjon advarsler og kontraindikasjoner er flagget som en **Blokkering** datakluft (DG001) i denne bevissamlingen — sikkerhetsvurdering for denne kandidaten kan ikke gå videre til fase 1 før dette løses. DDI-spørring returnerte heller ingen data.)*

---

## Konklusjon og neste trinn

**Beslutning: Avvent**

**Begrunnelse:**
Denne kandidaten hviler helt på en modellpreduksjon (Bevisnivå L5) uten støttende kliniske studier og ingen effektivitetslitteratur; den eneste hentet kliniske studien er urelatert, og de to tilgjengelige publikasjonene beskriver i stedet alpelisib-indusert pulmonær og kardial toksisitet — et sikkerhetssignal som går mot bruk ved pulmonær hypertensjon. Kombinert med en blokkering datakluft i TFDA sikkerhetdata, møter denne kandidaten ikke for øyeblikket standarden for å gå videre forbi innledende sikkerhetsvurdering (S0).

**For å fortsette, kreves følgende:**
- TFDA-produktinformasjon / sikkerhetsvarsler og kontraindikasjoner (løser blokkering datakluft DG001)
- Bekreftet mekanismedokumentasjon (MOA) fra DrugBank (DG002)
- Dedikerte prekliniske eller kliniske studier som evaluerer alpelisib spesifikt i pulmonær hypertensjon-modeller eller pasienter
- En kardiopulmonal sikkerhetsvurderingsplan som adresserer interstisiell lungesykdom og høyre ventrikel-dysfunksjon-signalene identifisert i eksisterende litteratur

## Ansvarsfraskrivelse

Dette innholdet er kun til forskningsformål og utgjør ikke medisinsk rådgivning.
Klinisk validering kreves før enhver klinisk anvendelse.

---

