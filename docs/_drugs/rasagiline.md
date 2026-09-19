---
layout: default
title: Rasagiline
parent: Kun modellprediksjon (L5)
nav_order: 296
evidence_level: L5
indication_count: 6
---

# Rasagiline
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

# Rasagilin: Fra Parkinsons sykdom (MAO‑B-hemming) til PLA2G6-assosiert nevrodegenerasjon

## Sammenfatning i en setning

> Rasagilins originalindikasjon er ikke dokumentert i det gjeldende datasettet, selv om det klinisk er kjent som en selektiv, irreversibel MAO‑B-hemmer brukt i Parkinsons sykdom.
> TxGNN-modellens topprangerete forutsigelse er **PLA2G6-assosiert nevrodegenerasjon**, en sjelden nevrodegenerativ lidelse med en parkinsonisme-fenotype.
> Dette er en **ren beregningsbasert forutsigelse** — **0 kliniske studier** og **0 publikasjoner** støtter for øyeblikket denne retningen.

---

## Rask oversikt

| Element | Innhold |
|---------|---------|
| Originalindikasjon | Ikke dokumentert i dette datasettet (datakløft). Klinisk kjent bruk: MAO‑B-hemmerterapi i Parkinsons sykdom |
| Forutsagt ny indikasjon | PLA2G6-assosiert nevrodegenerasjon |
| TxGNN prediksjonspoeng | 99.71% |
| Bevisgrad | L5 |
| Markedsstatus i Norge | Ikke markedsført |
| Antall autorisasjoner | 0 |
| Anbefalt beslutning | Avvente |

---

## Hvorfor er denne prediksjonen rimelig?

Detaljert virkningsmekanismedata er ikke tilgjengelig i dette datasettet (merket som en datakløft med høy alvorlighetsgrad). Basert på generell farmakologisk kunnskap som refereres i bevissamlingen selv, er rasagilin en selektiv, irreversibel MAO‑B-hemmer, en medikamentklasse som er etablert for å redusere dopaminabbygning og gi neuroproteksjon ved Parkinsons sykdom.

Den topprangerete kandidaten, PLA2G6-assosiert nevrodegenerasjon (PLAN), har en subtype med oppstart i voksen alder (PARK14) som presenterer seg med dystoni-parkinsonisme og basal ganglia dopaminerg degenerasjon. Dette skaper en plausibel, men rent teoretisk, mekanistisk bro: redusert dopaminkatabolisme via MAO‑B-hemming kunne i prinsippet gi symptomatisk eller neuroprotektiv fordel i denne parkinsonisme-spektrum-fenotypen.

Det er viktig å merke seg at denne mekanistiske koblingen **ikke har dedikert klinisk studie- eller litteraturstøtte** — den er utledet av TxGNN fra nettverksstruktur og generell sykdomsklassesimilaritet, ikke fra noen direkte bevis på effektivitet i PLAN.

---

## Bevis fra kliniske studier

For øyeblikket ingen relaterte kliniske studier registrert.

---

## Litteraturbevis

For øyeblikket ingen relatert litteratur tilgjengelig.

---

## Markedsinformasjon for Norge

Rasagilin er for øyeblikket ikke markedsført i Norge, og ingen markedsføringsauktorisasjonsposter er tilgjengelige i dette datasettet (0 lisenser).

---

## Sikkerhetshensyn

Vennligst se pakningsvedlegget for sikkerhetsinformasjon. Merk: TFDA-merkingdata (advarsler og kontraindikasjoner) er for øyeblikket en **blokkerende datakløft** og har ikke blitt vurdert — ingen formell sikkerhetsgjennomgang (S1) kan fullføres før dette er løst.

---

## Andre forutsagte indikasjoner (for kontekst)

Bevissamlingen inneholder 5 ytterligere TxGNN-kandidater, alle på bevisgrad L5 uten støttekliniske studier eller litteratur:

| Rangering | Sykdom | TxGNN-poeng | Mekanistisk plausibilitet | Anbefaling |
|-----------|--------|------------|---------------------------|-----------|
| 2 | Rasmussens subakutt encefalitt | 99.56% | Ingen (autoimmun/inflammatorisk, ikke relatert til MAO‑B-vei) | Avvente |
| 3 | Myelitt | 99.32% | Ingen (inflammatorisk/infeksiøs ryggmargssykdom) | Avvente |
| 4 | Paralysis agitans, juvenil, av Hunt | 99.25% | **Sterk** — historisk term for juvenil parkinsonisme, samme sykdomsspektrum som Rasagilins kjente bruk | Forskningsspørsmål |
| 5 | Transaldolase-mangel | 99.19% | Ingen (pentosfosfatvei-defekt) | Avvente |
| 6 | Polimikrogyria, perisylvisk, med cerebellær hypoplasi og artrogryposi | 99.01% | Ingen (strukturell utviklingsmessig hjernefeilbildning) | Avvente |

Rangering 4 ("Hunts juvenile paralysis agitans") er mekanistisk den mest sammenhengne kandidaten, siden den faller innenfor samme parkinsonisme-spektrum som Rasagilins etablerte farmakologi, men den mangler noen subtype-spesifikk studie- eller kasuistisk bevis og forblir kun en forskningshypotese.

---

## Konklusjon og neste trinn

**Beslutning: Avvente**

**Begrunnelse:**
Alle seks forutsagte indikasjoner er på bevisgrad L5 (modellforutsigelse kun, ingen klinisk eller litteraturstøtte). I tillegg er TFDA-sikkerhetsmerkingdata en blokkerende kløft som hindrer noen formell sikkerhetsgjennomgang, og medikamentet er ikke markedsført i Norge.

**For å fortsette, er følgende nødvendig:**
- TFDA/regulatorisk merkedata (advarsler, kontraindikasjoner) for å løse den blokkerende sikkerhetsdatakløften (DG001)
- Bekreftet virkningsmekanismedata fra DrugBank (DG002)
- Originalindikasjonhistorikk for medikamentet (for øyeblikket mangler i datasettet)
- Prekliniske eller mekanistiske studier som spesifikt adresserer MAO‑B-hemming i PLAN eller juvenil parkinsonisme-spektrum-lidelser før du går videre utover hypotesestadiet

## Ansvarsfraskrivelse

Dette innholdet er kun til forskningsformål og utgjør ikke medisinsk rådgivning.
Klinisk validering kreves før enhver klinisk anvendelse.

---

