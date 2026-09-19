---
layout: default
title: Lorlatinib
parent: Kun modellprediksjon (L5)
nav_order: 216
evidence_level: L5
indication_count: 10
---

# Lorlatinib
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

# Lorlatinib: Fra ALK-positiv NSCLC til fibromatose gingivalis

## Oppsummering i én setning

> Lorlatinib er en tredje generasjons ALK/ROS1 tyrosinkinasehemmer som er etablert for behandling av ALK-positiv avansert ikke-småcellet lungekreft (NSCLC), støttet av fase 3-studien CROWN som er inkludert i denne bevissamlingen.
> TxGNN-modellens toppprediksjon er **fibromatose gingivalis** (en godartad fibøs overgroing av tannkjøttet), med en poengsum på **99.81%**,
> men denne prediksjonen støttes for tiden av **null kliniske forsøk** og **null publikasjoner** — det er et rent embedding-similaritetssignal uten kjent mekanistisk eller klinisk grunnlag.

---

## Rask oversikt

| Element | Innhold |
|---------|---------|
| Etablert indikasjon | Ikke dokumentert i norske regulatoriske data (legemiddelet er ikke markedsført der). Basert på vedlagt litteratur (CROWN fase 3 RCT, osv.), er den etablerte originalindikasjonen **ALK-positiv avansert/metastatisk NSCLC** |
| Forutsagt ny indikasjon | Fibromatose gingivalis |
| TxGNN-prediksjonspoengsum | 99.81% |
| Bevisnivå | L5 (kun modellprediksjon, ingen støttende forsøk eller litteratur) |
| Status på det norske markedet | Ikke markedsført |
| Antall autorisasjoner | 0 |
| Anbefalt beslutning | Avvent |

---

## Hvorfor er denne prediksjonen rimelig?

Detaljerte data om virkningsmåten for lorlatinib var ikke tilgjengelige i den strukturerte legemiddelregistreringen (`original_moa: [Data Gap]`). Basert på vedlagt litteratur (CROWN-studien og relaterte publikasjoner) er lorlatinib imidlertid en hjernepenetrant, tredje generasjons ALK/ROS1 tyrosinkinasehemmer med bevist effektivitet ved ALK-positiv NSCLC og bred aktivitet mot ALK-resistensmutasjoner.

Fibromatose gingivalis er en godartad, ikke-neoplastisk fibøs overgroing av tannkjøttet, som oftest forårsaket av genetiske mutasjoner (f.eks. *SOS1*, *REST*) eller connexin-relaterte signalveier, eller legemiddelindusert (fenytoin, syklosporin, calciumkanalblokkerer). Det har ingen etablert forbindelse til ALK/ROS1-signalering, tyrosinkinasehemming eller noen onkogen drivervei som lorlatinib retter seg mot.

`repurposing_rationale` som er vedlagt denne prediksjonen uttaler klart at det er **ingen kjent mekanistisk forbindelse** — legemidlets begrunnelsesfelt beskriver dette som et rent TxGNN embedding-similaritetsartefakt med «ingen støttende litteratur eller forsøk». Dette betyr at den topprangerte prediksjonen i denne bevissamlingen bør behandles som biologisk implausibel i stedet for et genuint omkvalifiseringssignal, og rapporten nedenfor gjenspeiler det ærlig.

**Merk om datakvalitet:** Flere kandidater med lavere rangering i denne bevissamlingen (ranger 5, 7, 8, 10) har litteratur som ikke stemmer med deres sykdomsetiketter — f.eks. NSCLC RCT-data (CROWN-studien) klassifisert under «benign lungeneplasme», nevroblastaoma/gliom-caserapporter klassifisert under «lungens kimcelletur», frontotemporaldemens-oversikter klassifisert under et urelatert genetisk syndrom (IBMPFD), og lorlatinib bivirknings-caserapporter klassifisert under et urelatert dysmorfologisyndrom. Disse ser ut til å være knowledge-graph-/ontologi-kartleggingsfeil og bør ikke tolkes som klinisk støtte for disse spesifikke kandidatindikasjonene. Kun **rang 4 (lungehilus karsinoma)** viser en plausibel mekanistisk forbindelse, siden det er en anatomisk-stedsundertype av ALK+ NSCLC — men støttes kun av en enkelt neoadjuvant caserapport (L4/S1), og kan kanskje sies å representere en omformulering av legemiddelens kjente indikasjon i stedet for et virkelig nytt omkvalifiseringsmål.

---

## Bevis fra kliniske forsøk

For tiden er ingen relaterte kliniske forsøk registrert.

---

## Litteraturbevis

For tiden er ingen relatert litteratur tilgjengelig.

---

## Informasjon om det norske marked

Ingen autorisasjonsdata tilgjengelige — Lorlatinib er for tiden **ikke markedsført** i Norge (`total_licenses: 0`).

---

## Cytotoksisitet (kun antineoplastiske legemidler)

Lorlatinib er klassifisert som antineoplastisk basert på sin etablerte bruk ved NSCLC (per vedlagt litteratur) og sin legemiddelklasse (ALK/ROS1 tyrosinkinasehemmer).

| Element | Innhold |
|---------|---------|
| Cytotoksisitetsklassifisering | Målrettet terapi (tredje generasjons ALK/ROS1 tyrosinkinasehemmer) — ikke et konvensjonelt cytotoksisk middel |
| Risiko for myelosuppresjon | Lav. Rapporterte bivirkninger i vedlagt litteratur er hovedsakelig metabolske og nevrologiske snarere enn hematologiske — hyperkolesterolemi, hypertriglyseridemi, vektøkning, ødem og CNS/humøreffekter er karakteristiske toksisiteter (per farmakooversyn og litteratur om bivirkningshåndtering) |
| Emetogenisitetsklassifisering | Lav (oralt målrettet middel; ikke forbundet med høyt emetogenitetspotensial) |
| Overvåkingselementer | Fastende lipidpanel (kolesterol, triglyserider), vekt, CNS/kognitiv/humørvurdering, blodtrykk, lever- og nyrerfunksjon; sjeldne rapporter om nefrotisk syndrom og pulmonær toksisitet påkaller overvåking for proteinuri og respiratoriske symptomer |
| Håndteringsbeskyttelse | Oralt småmolekyl-tyrosinkinasehemmer — standard orale forsiktigheter ved håndtering av farlige stoffer (f.eks. per NIOSH-listen over farlige stoffer) er hensiktsmessige; krever ikke IV cytotoksisk-stoff-håndteringsprotokoller |

---

## Sikkerhetshensyn

Vennligst se pakningsvedlegget for sikkerhetsinformasjon.

---

## Konklusjon og neste steg

**Beslutning: Avvent**

**Begrunnelse:**
TxGNN-modellens topprangerte prediksjon (Fibromatose gingivalis, 99.81 % poengsum) har null korroborerende kliniske forsøk eller litteratur, og modellens egen begrunnelse bekrefter ingen kjent mekanistisk forbindelse mellom ALK/ROS1-hemming og denne godartade, ikke-onkologiske tilstanden. Dette er en usupportert L5 (kun modell) prediksjon og oppfyller ikke terskelen for videre evaluering.

**For å gå videre er følgende nødvendig:**
- DG001 (Blokkering): TFDA/regionale advarsler på legemiddelens etikett og kontraindikasjoner — påkrevd før noen S1 sikkerhetskontroll kan gjennomføres
- DG002 (Høy): Verifiserte MOA-data via DrugBank API for å behørig vurdere mekanistisk plausibilitet for noen fremtidig kandidatindikasjon
- En datakvalitetskontroll av TxGNN-til-litteratur-kartleggingspipelinen, gitt tilsynelatende sykdomsetikett-mismatches identifisert i ranger 5, 7, 8 og 10 av denne bevissamlingen
- Hvis videre utforsking er berettiget, priorisering av rang 4 (lungehilus karsinoma) som et forskningsspørsmål — det er den eneste kandidaten med en plausibel mekanistisk forbindelse og casesnivå klinisk bevis, selv om det sannsynligvis faller innenfor legemiddelens allerede godkjente ALK+ NSCLC-indikasjon i stedet for å representere en sann ny indikasjon

## Ansvarsfraskrivelse

Dette innholdet er kun til forskningsformål og utgjør ikke medisinsk rådgivning.
Klinisk validering kreves før enhver klinisk anvendelse.

---

