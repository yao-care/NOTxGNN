---
layout: default
title: Methotrexate
parent: Kun modellprediksjon (L5)
nav_order: 227
evidence_level: L5
indication_count: 10
---

# Methotrexate
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

# Methotrexate: Fra antifolatekjemoterapi/immunmodulatorisk bruk til lungeblastom

## Sammendrag i én setning

> Methotrexate (DrugBank DB00563) er en dihydrofolatreduktase (DHFR) inhibitor som lenge har vært brukt innen onkologi og autoimmun sykdompraksis, selv om ingen formell originalindikasjon eller regulatorisk dokumentasjon er til stede i denne bevissamlingen. TxGNNs topprangerte prediksjon er **lungeblastom**, men denne kandidaten støttes for tiden av **0 kliniske prøver** og **0 publikasjoner** — det er en ren modellutgang uten klinisk eller mekanistisk bekrefelse til dags dato.

---

## Rask oversikt

| Element | Innhold |
|---------|---------|
| Originalindikasjon | Ikke på register — `taiwan_regulatory.licenses` er tom og `original_indications` er tom (se Datakløfter DG001/DG002) |
| Forutsagt ny indikasjon | Lungeblastom |
| TxGNN prediksjonspoeng | 99.45% |
| Bevisnivå | L5 |
| Norges markedsstatus | ✗ Ikke markedsført |
| Antall autorisasjoner | 0 |
| Anbefalt beslutning | Avvent |

---

## Hvorfor er denne prediksjonen rimelig?

Detaljerte data om virkningsmekanisme er flagget som en datakløft i denne bevissamlingen (`original_moa: [Data Gap]`, DG002, alvorlighetsgrad Høy). Basert på den mekanistiske begrunnelsen knyttet til denne kandidaten, virker methotrexate som en DHFR inhibitor, som blokkerer folatavhengig purin- og pyrimidinsyntese og derved utøver cytotoksisk press på raskt delende celler — en mekanisme som bredt gjelder for mange maligniteter.

Lungeblastom er imidlertid en ekstremt sjelden sarkomalignende lungetumor. Begrunnelsen sier eksplisitt at det for tiden ikke finnes noen mekanistisk diskusjon eller klinisk data som forbinder methotrexate til denne spesifikke tumortypen — assosiasjonen eksisterer utelukkende som et resultat av TxGNN-nettverkssimilaritetsmodellen, uten noen bekreftet prøve- eller litteratursignal.

Gitt det fullstendige fraværet av støttende bevis, bør denne spesifikke prediksjonen behandles som hypotesegenererende kun, ikke som grunnlag for klinisk eller forskningsprioritering på dette tidspunktet.

---

## Bevis fra kliniske prøver

Ingen relaterte kliniske prøver er for tiden registrert.

---

## Litteraturbevis

Ingen relatert litteratur er for tiden tilgjengelig.

---

## Norges markedsinformasjon

Ingen markedsautoriseringer er på register for dette produktet i det nåværende datasettet (`total_licenses = 0`, `market_status = Not marketed / Not Marketed`). Ingen lisenstabell kan fylles ut.

---

## Cytotoksisitet

Methotrexate er en konvensjonell antimetabolitt/antifolatcytotoksisk agent (kriterium: kjent cytotoksisk kjemoterapiklasse), så denne delen gjelder.

| Element | Innhold |
|---------|---------|
| Cytotoksisitetsklassifisering | Konvensjonell cytotoksisk (antimetabolitt / antifolat — DHFR inhibitor) |
| Myelosuppresjonrisiko | Høy — litteratur innen denne bevissamlingen dokumenterer gjentatt dosebegrensende hematologisk toksisitet og nefrotoksisitetsrelatert forlenget eksponering som krever redningstiltak (f.eks. leukovorinredning, høyflukshemodialyse) i høydoseregimer |
| Emetogenitetsklassifisering | Lav til moderat, doseavhengig (høyere med høydose IV-regimer) |
| Overvåkingsparametere | Blodcelletal med differensial, nyreverkskapasitet (kreatinin/eGFR), leverfunksjon, serum MTX-nivåer for høydoseregimer, slimhinneinflammasjon/oral toksisitet |
| Håndteringsbeskyttelse | Må følge regler for håndtering av cytotoksiske og farlige legemidler under preparering og administrasjon |

---

## Sikkerhetshensyn

Se pakningsvedlegget for sikkerhetsinformasjon. (Nøkkeladvarsler, kontraindikasjoner og DDI-data er alle markert som datakløfter i denne bevissamlingen — DG001, Blocking severity.)

---

## Konklusjon og neste trinn

**Beslutning: Avvent**

**Begrunnelse:**
Den topprangerte prediksjonen (lungeblastom) har et L5 bevisnivå — ingen kliniske prøver og ingen litteratur støtter denne spesifikke indikasjonen. Det er rent en algoritmisk utgang og kan ikke gå videre til sikkerhet eller klinisk evaluering uten uavhengig bekrefelse.

**For å fortsette, er følgende nødvendig:**
- TFDA/Norges pakningsvedlegg-data (advarsler, kontraindikasjoner, DDI) — for tiden Blocking (DG001)
- Bekreftet dokumentasjon av virkningsmekanisme fra DrugBank (DG002)
- Uavhengig mekanistisk eller preklinisk begrunnelse som forbinder methotrexate til lungeblastom spesifikt, før noen prøve- eller litteratursøk er berettiget
- **Merk:** innen denne samme bevissamlingen har andre forutsagte indikasjoner for methotrexate vesentlig sterkere bevis (f.eks. *Hodgkins lymfom* og *rabdomyosarkom*, begge L2/S2 "Fortsett med sikkerhetstiltak"). Hvis målet er evaluering av nær-tids ombruk, fortjener disse kandidatene separate rapporter og bør prioriteres fremfor lungeblastom.

## Ansvarsfraskrivelse

Dette innholdet er kun til forskningsformål og utgjør ikke medisinsk rådgivning.
Klinisk validering kreves før enhver klinisk anvendelse.

---

