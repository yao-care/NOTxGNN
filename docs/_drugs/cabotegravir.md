---
layout: default
title: Cabotegravir
parent: Kun modellprediksjon (L5)
nav_order: 67
evidence_level: L5
indication_count: 5
---

# Cabotegravir
{: .fs-9 }

Evidensnivå: **L5** | Predikerte indikasjoner: **5** stk.
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

# Cabotegravir: Fra udeterminert originalindikasjon til revmatoid artritt

## Sammenfatting i én setning

> Cabotegravir (DrugBank ID: DB11751) har for tiden ingen verifisert originalindikasjon eller virkningsmekanisme registrert, og legemidlet er ikke ennå markedsført i Taiwan (TFDA).
> TxGNN-modellen predikerer en mulig ny indikasjon for **revmatoid artritt**,
> men denne prediksjonen støttes av **0 kliniske forsøk** og **0 publikasjoner**, og modellens egen begrunnelse angir ingen kjent mekanistisk overlapping.

---

## Kort oversikt

| Element | Innhold |
|---------|---------|
| Originalindikasjon | Ikke tilgjengelig — ingen lisens- eller indikasjonsdata på fil |
| Predikert ny indikasjon | Revmatoid artritt |
| TxGNN-prediksjonspoeng | 99.45% |
| Bevisgrad | L5 (kun modellpreduksjon, ingen understøttende studier) |
| Markedsstatus i Taiwan | ✗ Ikke markedsført |
| Antall autorisasjoner | 0 |
| Anbefalt beslutning | Utsette |

---

## Hvorfor er denne prediksjonen rimelig?

For tiden er detaljerte data om virkningsmekanisme ikke tilgjengelige for cabotegravir i denne bevissamlingen, og ingen originalindikasjon er registrert. Basert på allmenn farmakologisk klassekunnskap som refereres i bevissamlingens egen begrunnelse, er cabotegravir en HIV-integrase-strandoverføringsinhibitor (INSTI), som virker ved å blokkere viral DNA-integrasjon inn i vertscellenes genom.

Bevissamlingens egen mekanistiske begrunnelse for topprediksjonen sier eksplisitt at denne integrase-inhibisjon-mekanismen har **ingen kjent overlapping** med revmatoid artritts patofysiologi (TNF-α, IL-6, synoviale proliferasjonsstier). Begrunnelsen bemerker videre at manglende originalindikasjon-data kan ha destabilisert modellens embedding, som kunne forklare den uvanlig høye poengstillingen til tross for mangel på biologisk plausibilitet.

De gjenværende fire rangerte kandidater (skleroserande kolangitt, bronkitt, kolobomatøs mikroftalmi–rizzomeli dysplasi-syndrom, alvorlig ikke-proliferativ diabetisk retinopati) viser det samme mønsteret: høye TxGNN-poeng med eksplisitt angitt fravær av mekanistisk forbindelse, ingen kliniske forsøk, og ingen litteratur. Dette er konsistent med modellstøy heller enn et kredibelt gjenbrukssignal.

---

## Bevis fra kliniske forsøk

For tiden er det ingen relaterte kliniske forsøk registrert

---

## Litteraturbevis

For tiden er ingen relatert litteratur tilgjengelig

---

## Markedsinformasjon for Taiwan

Ingen godkjente lisenser på fil — cabotegravir er ikke for tiden markedsført i Taiwan (0 autorisasjoner).

---

## Sikkerhetshensyn

Sikkerhetsdata er for tiden utilgjengelig (TFDA-etikett, kontraindikasjoner og legemiddelinteraksjonsdata er alle merket som sikkerhetsdatagap som blokkerer — se DG001). Vennligst konsulter pakningsvedlegget når det blir tilgjengelig for sikkerhetsinformasjon.

---

## Konklusjon og neste trinn

**Beslutning: Utsette**

**Begrunnelse:**
Prediksjonen hviler utelukkende på en L5-modellpoeng uten klinisk forsøk- eller litteraturstøtte, og bevissamlingens egen mekanistiske analyse finner ingen kjent biologisk forbindelse mellom HIV-integrase-inhibisjon og revmatoid artritt. Kombinert med et sikkerhetsdatagap som blokkerer (ingen TFDA-etikett) og legemidlets umarkedsført status i Taiwan, er det ingen basis for å fremme denne kandidaten.

**For å komme videre er følgende nødvendig:**
- TFDA-produktetikett (advarsler, kontraindikasjoner) — løser DG001 (blokkering)
- Verifisert virkningsmekanisme fra DrugBank — løser DG002
- Verifisert originalindikasjon(er) for legemidlet
- Uavhengig preklinisk eller mekanistisk bevis som knytter INSTI-farmakologi til autoimmun-/reumatologiske stier før videre evalueringsstadium (S1+)

## Ansvarsfraskrivelse

Dette innholdet er kun til forskningsformål og utgjør ikke medisinsk rådgivning.
Klinisk validering kreves før enhver klinisk anvendelse.

---

