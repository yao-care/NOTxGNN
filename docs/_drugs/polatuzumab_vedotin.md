---
layout: default
title: Polatuzumab Vedotin
parent: Kun modellprediksjon (L5)
nav_order: 283
evidence_level: L5
indication_count: 1
---

# Polatuzumab Vedotin
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

# Polatuzumab Vedotin: Fra B-cellelymfom til HER2-positivt brystkreft

## Sammendrag i én setning

Polatuzumab vedotin er et antistoff-legemiddel-konjugat (ADC) som retter seg mot CD79b, og er for tiden godkjent for B-cellemaligniteter som diffust storcellet B-cellelymfom (DLBCL). TxGNN forutsier en mulig sammenheng med **HER2-positivt brystkreft**, men denne prediksjon støttes for tiden ikke av **noen kliniske forsøk og ingen publisert litteratur** — den hviler utelukkende på et modellresultat (**bevisnivå L5**).

---

## Kort oversikt

| Emne | Innhold |
|------|------|
| Opprinnelig indikasjon | Diffust storcellet B-cellelymfom (DLBCL) og andre B-cellemaligniteter (basert på beskrivelse av legemiddelmekanisme; ikke tilstede som strukturerte data) |
| Forutsagt ny indikasjon | HER2-positivt brystkreft |
| TxGNN prediksjonspoeng | 99.34 % |
| Bevisnivå | L5 |
| Markedsstatus | Ikke markedsført |
| Antall godkjenninger | 0 |
| Anbefalt beslutning | Avvente |

---

## Hvorfor er denne prediksjonen rimelig?

Polatuzumab vedotin er et antistoff-legemiddel-konjugat som selektivt leverer det cytotoksiske legemidlet MMAE (monomethyl auristatin E) til B-celler som uttrykker CD79b, en komponent av B-celle-reseptorkomplekset. Det er for tiden godkjent for DLBCL og andre B-cellemaligniteter. Feltet `original_moa` i evidenspakken er merket som datamangel, men denne mekanismen kan utledes fra modellens begrunnelsestekst.

HER2-positivt brystkreft og DLBCL tilhører helt ulike tumorbiologi-kategorier — førstnevnte er en epitelial tumor drevet av HER2-overekspresjon, mens sistnevnte er en hematologisk malignitet av B-celle-opprinnelse. CD79b er ikke en markør som uttrykkes på HER2-positive brystkreftceller, så det er ingen delt mål mellom opprinnelig og forutsagt indikasjon.

Gitt dette, bør gjeldende prediksjon behandles som en statistisk assosiasjon produsert av TxGNN-grafmodellen snarere enn en mekanistisk begrunnet hypotese. Uten noen støttende mekanistisk, klinisk eller litteraturbevis, er denne kandidaten best klassifisert som et falskt positivt resultat på dette stadiet.

---

## Bevis fra kliniske forsøk

For tiden ingen relaterte kliniske forsøk registrert

---

## Bevis fra litteratur

For tiden ingen relatert litteratur tilgjengelig

---

## Markedsinformasjon

Det er for tiden ingen markedsføringstillatelser registrert for dette legemidlet (0 lisenser, markedsstatus: ikke markedsført).

---

## Cytotoksisitet

Polatuzumab vedotin er et antistoff-legemiddel-konjugat som leverer en cytotoksisk nyttelast (MMAE) og er klassifisert som et antineoplastisk middel.

| Emne | Innhold |
|------|------|
| Cytotoksisitetsklassifisering | Målrettet terapi — antistoff-legemiddel-konjugat (ADC) som leverer cytotoksisk nyttelast (MMAE) |
| Risiko for myelosuppresjon | Se pakningsvedlegg for advarsler og forholdsregler |
| Klassifisering av emetogenitet | Se pakningsvedlegg for advarsler og forholdsregler |
| Overvåkingspunkter | Se pakningsvedlegg for advarsler og forholdsregler |
| Beskyttelse ved håndtering | Må følge regelverket for håndtering av cytotoksiske legemidler, i samsvar med ADC/cytotoksisk nyttelast-agenser |

---

## Sikkerhetshensyn

Se pakningsvedlegg for sikkerhetsinformasjon.

---

## Konklusjon og neste skritt

**Beslutning: Avvente**

**Begrunnelse:**
Denne kandidaten har bevisnivå L5 — ingen kliniske forsøk, ingen litteratur, og ingen sannsynlig mekanistisk sammenheng mellom CD79b-målet og HER2-positiv brystkreft-biologi. Prediksjon gjenspeiler for tiden utelukkende en statistisk assosiasjon på modellnivå og oppfyller ikke terskelen for å avansere.

**For å fortsette, trengs følgende:**
- Bekreftet virkningsmekanisme (MOA)-data fra DrugBank (for tiden datamangel, DG002)
- TFDA-pakningsvedlegg advarsler, kontraindikasjoner og legemiddelinteraksjonsdata (for tiden blokkerende datamangel, DG001)
- Eventuell preklinisk eller mekanistisk bevis som forbinder CD79b/MMAE-veivaktivitet til HER2-positiv brystkreft-biologi, før ytterligere evaluering er berettiget

## Ansvarsfraskrivelse

Dette innholdet er kun til forskningsformål og utgjør ikke medisinsk rådgivning.
Klinisk validering kreves før enhver klinisk anvendelse.

---

