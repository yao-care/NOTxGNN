---
layout: default
title: Brodalumab
parent: Kun modellprediksjon (L5)
nav_order: 60
evidence_level: L5
indication_count: 10
---

# Brodalumab
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

# Brodalumab: fra uspesifisert original indikasjon til strongyloidiasis (flagget som reversert-retnings signal)

## Sammenfatning i én setning

> Brodalumabs originale indikasjon er ikke registrert i denne evidenspakken, men det er kjent at det virker som en **IL-17RA antagonist**.
> TxGNN-modellens toppprediksjon — **strongyloidiasis** — er ikke støttet av noen kliniske forsøk eller litteratur, og modellens egen mekanistiske begrunnelse indikerer at assosiasjonen går i *motsatt* retning: IL-17 blokkering er en kjent **risikofaktor** for strongyloidiasis, ikke en behandling for det.
> Dette tolkes best som et sikkerhetssignal som er misoppfattet som en omformål-mulighet, ikke en levedyktig kandidat.

---

## Raskt oversikt

| Element | Innhold |
|---------|---------|
| Original indikasjon | Ikke oppgitt i denne evidenspakken (`original_indications` tom) |
| Forutsagt ny indikasjon | Strongyloidiasis ⚠️ (mekanistisk reversert — se nedenfor) |
| TxGNN prediksjonspoengsum | 99.84% |
| Evidensnivå | L5 (ingen kliniske forsøk, ingen litteratur) |
| Markedsstatus i Norge | Ikke markedsført |
| Antall godkjennelser | 0 |
| Anbefalt avgjørelse | **Hold** |

---

## Hvorfor er denne prediksjonen rimelig?

Formale virkningsmekanisme-data (DrugBank `original_moa`) er ikke tilgjengelig i denne evidenspakken. Imidlertid identifiserer modellens egne rasjonale-anmerkninger brodalumab som en **IL-17RA (interleukin-17 reseptor A) antagonist**, som blokkerer IL-17-medierad signalering. IL-17RA-målrettede biologiske midler som en klasse brukes til å undertrykke IL-17-drevne inflammatoriske responser.

Det originale indikasjonsfelt er tomt i denne pakken, så ingen direkte sammenligning til den forutsagte indikasjon kan gjøres fra de strukturerte dataene. Hva som *kan* vurderes er den mekanistiske plausibiliteten til den topprangerte prediksjonen på egne betingelser — og her flagget evidenspakken et kritisk problem.

**Denne prediksjonen er ikke rimelig, og evidenspakken selv sier det.** IL-17 er en nøkkelverts-forsvars-cytokin mot intestinale rundormer, inkludert *Strongyloides stercoralis*. Klinisk er inhibitorer av IL-17-banen (brodalumab, secukinumab og relaterte midler) kjent for å *øke* risikoen for strongyloidosis-reaktivering/hyperinfeksjon — pakningsvedlegg for denne middelklassen krever typisk screening og behandling av latent strongyloidiasis *før* initiering av terapi. TxGNNs topologiske likhets-scoring ser ut til å ha plukket opp et reelt biologisk forhold (IL-17RA ↔ strongyloidiasis), men tilordnet det feil kausal retning — en kjent feilmodus der "risiko-assosiasjon" og "terapeutisk indikasjon"-kanter blir sammenblandet i kunnskapsgrafen. Dette bør behandles som et **kontraindikasjons-signal**, ikke en omformål-mulighet.

---

## Klinisk forsøksevidence

For tiden ingen relaterte kliniske forsøk registrert.

---

## Litteraturevidence

For tiden ingen relatert litteratur tilgjengelig.

---

## Markedsinformasjon for Norge

Brodalumab har **0 godkjennelser** på journalen og er **ikke markedsført** i Norge (`Not marketed`) per denne evidenspakken. Ingen lisensoppføringer er tilgjengelige for tabulering.

---

## Sikkerhetshensyn

- **Mekanistisk sikkerhetssignal (fra prediksjons begrunnelse, ikke formell merking):** Evidenspakkens egen analyse merker at IL-17-veiblokkering — mekanismen for brodalumab — er assosiert med en *økt* risiko for *Strongyloides* infeksjon/hyperinfeksjonssyndrom. Dette speiler kjent klassenivå-veiledning for IL-17 inhibitorer som krever strongyloidiasis screening før behandlingsinitiering.
- Formale pakningsvedlegg-advarsler, kontraindikasjoner og legemiddel-legemiddel interaksjonsdata er ikke tilgjengelig i denne evidenspakken (flagget som et **blokkering** datagap, DG001). Vennligst referer til det offisielle pakningsvedlegget for fullstendig sikkerhetsinformasjon når det blir tilgjengelig.

---

## Konklusjon og neste steg

**Avgjørelse: Hold**

**Begrunnelse:**
Den topprangerte prediksjonen (strongyloidiasis) er motsatt rettet — det beskriver en kjent risiko for midlets mekanisme, ikke en terapeutisk mulighet — og har null støttekliniske forsøk eller litteratur (L5). Ingen annen kandidat i topp 10 (rangeringer 2–10, alle oftalmologiske/inflammatoriske tilstander) når videre enn L4/L5, og flere (f.eks. isolert optisk neuritt) har sine egne retnings-usikkerheter, siden IL-17 inhibitorer har vært assosiert med case reports av CNS demyeliniserings-sykdom forverring.

**For å fortsette, er følgende nødvendig:**
- Formale DrugBank/TFDA-data for original indikasjon og MOA, for å etablere en ekte grunnlinje for mekanistisk sammenligning
- TFDA pakningsvedlegg (advarsler, kontraindikasjoner, DDI) for å lukke blokkering datagap DG001
- Noen brodalumab-spesifikke (ikke klassenivå) case reports eller farmakovigilans-data på strongyloidiasis, for å bekrefte retningen på risikoen i stedet for å utlede den
- Hvis du forfølger optisk neuritt/CRION-klyngen (rangeringer 5–8) som en lengre-shot-hypotese, målrettet litteratursøk for Th17/IL-17 involvering i demyeliniserende optisk neuropatier, sammen med eksplisitt gjennomgang av risiko for CNS demyelinisering assosiert med IL-17 inhibitor bruk

## Ansvarsfraskrivelse

Dette innholdet er kun til forskningsformål og utgjør ikke medisinsk rådgivning.
Klinisk validering kreves før enhver klinisk anvendelse.

---

