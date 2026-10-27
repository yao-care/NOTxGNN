---
layout: default
title: Tagraxofusp
parent: Kun modellprediksjon (L5)
nav_order: 397
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-15
description: "Tagraxofusp: predikert ny indikasjon Esotropi (evidensnivå L5). Opprinnelig indikasjon: Lymfom"
monitor_inn: "TAGRAXOFUSP"
predicted_indications: ["esotropia", "pre-malignant neoplasm", "inner ear neoplasm", "benign neoplasm of tongue", "bronchial adenomas/carcinoids childhood", "chondroid hamartoma", "ductal or ductular proliferation", "non-seminomatous lesion", "cystic neoplasm", "thyroglossal duct cyst"]
---

# Tagraxofusp
{: .fs-9 }

Evidensnivå: **L5** | Predikerte indikasjoner: **10** stk.
{: .fs-6 .fw-300 }

---

## Innholdsfortegnelse
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist" markdown="1">

## Farmasøytens vurderingsrapport

</div>

## Tagraxofusp: Fra lymfom til esotropi
{: .text-alpha }

## Oppsummering i én setning

Tagraxofusp er et CD123-rettet cytotoksisk fusjonsprotein (interleukin-3 koblet til avkortet difteritoksin), som i de innsamlede dataene er registrert med lymfom som opprinnelig indikasjon.
TxGNN-modellen forutsier at legemidlet kan være effektivt mot **esotropi**, men det finnes **0 kliniske studier** og **0 publikasjoner** som støtter denne retningen.
Prediksjonen bygger kun på modellen og har ingen dokumentert støtte.

---

## Hurtigoversikt

| Punkt | Innhold |
|------|------|
| Opprinnelig indikasjon | Lymfom |
| Foreslått ny indikasjon | Esotropi |
| TxGNN-prediksjonsscore | 99,73 % |
| Evidensnivå | L5 |
| Markedsstatus i Norge | Kun kansellert godkjenning |
| Antall godkjenninger | 1 |
| Anbefalt beslutning | Hold (avvent) |

---

## Hvorfor er denne prediksjonen (ikke) rimelig?

Data om virkningsmekanisme var ikke tilgjengelig i de innsamlede dataene. Ut fra allmenn kunnskap er tagraxofusp rettet mot CD123 (IL-3-reseptorens alfa-kjede) og dreper celler som uttrykker denne reseptoren. Legemidlet er i praksis knyttet til hematologiske maligniteter.

Esotropi er en øyemotorisk tilstand (skjeling innover) uten kjent CD123-drevet patologi. Det finnes derfor ingen plausibel mekanistisk kobling mellom den opprinnelige indikasjonen og den foreslåtte nye indikasjonen. Den høye TxGNN-scoren skyldes mest sannsynlig nærhet i kunnskapsgrafen og ikke et biologisk begrunnet forhold.

Også de øvrige ni predikerte indikasjonene (blant annet premaligne neoplasmer, indre øre-neoplasmer, godartet tungesvulst, kystiske neoplasmer og thyreoglossal gangcyste) mangler dokumentert CD123-rasjonale og har kun evidensnivå L5. De fleste av dem er godartede tilstander som vanligvis behandles kirurgisk eller lokalt, og en systemisk cytotoksisk behandling med betydelig toksisitet vil gi en ugunstig nytte-risiko-balanse.

---

## Klinisk studieevidens

Det er for øyeblikket ingen relaterte kliniske studier registrert.

---

## Litteraturevidens

Det er for øyeblikket ingen relatert litteratur tilgjengelig.

---

## Markedsinformasjon for Norge

| Godkjenningsnummer | Produktnavn | Doseringsform | Godkjent indikasjon |
|---------|------|------|-----------|
| EMEA/H/C/005031 | Elzonris | Ikke oppgitt | Lymfom |

Denne godkjenningen er registrert som kansellert, og det finnes ingen gyldige godkjenninger.

---

## Cytotoksisitet

| Punkt | Innhold |
|------|------|
| Cytotoksisitetsklassifisering | Målrettet cytotoksisk fusjonsprotein (CD123-rettet; IL-3 koblet til difteritoksin) |
| Risiko for myelosuppresjon | Se pakningsvedlegg for advarsler og forsiktighetsregler |
| Emetogenisk klassifisering | Se pakningsvedlegg for advarsler og forsiktighetsregler |
| Overvåkingspunkter | Lever- og nyrefunksjon, blodtelling; kapillærlekkasjesyndrom bør overvåkes (basert på allmenn kunnskap) |
| Håndteringsbeskyttelse | Følg gjeldende retningslinjer for håndtering av cytotoksiske legemidler |

---

## Sikkerhetsvurderinger

- **Legemiddelinteraksjoner**: Det er identifisert 66 mulige interaksjoner. De 20 som er vist i de innsamlede dataene er alle av moderat alvorlighetsgrad og gjelder hovedsakelig antidiabetika, blant annet:
  - Metformin, pioglitazon, glimepirid, klorpropamid, akarbose
  - GLP-1-agonister (albiglutid, dulaglutid, semaglutid)
  - DPP-4-hemmere (alogliptin, linagliptin, saksagliptin)
  - SGLT2-hemmere (kanagliflozin, dapagliflozin, empagliflozin)
  - Insuliner (aspart, degludek, detemir, glargin, glulisin, human isophan)
- **Allmenn kunnskap om toksisitet** (ikke fra dataene): kapillærlekkasjesyndrom og levertoksisitet er kjente alvorlige bivirkninger, og de gjør bruk ved godartede tilstander og tidlige stadier uakseptabel uten en definert målgruppe.

Advarsler og kontraindikasjoner fra pakningsvedlegget var ikke tilgjengelige. Se pakningsvedlegget for fullstendig sikkerhetsinformasjon.

---

## Konklusjon og neste steg

**Beslutning: Hold (avvent)**

**Begrunnelse:**
Prediksjonen har kun modellstøtte (L5), uten kliniske studier eller litteratur, og det mangler en plausibel CD123-basert mekanisme for esotropi. I tillegg er den eneste norske godkjenningen kansellert, og legemidlets kjente toksisitet gir en ugunstig nytte-risiko-balanse for en ikke-malign øyetilstand.

**For å gå videre kreves følgende:**
- Pakningsvedlegg med advarsler og kontraindikasjoner (blokkerende datamangel for sikkerhetsscreening)
- Detaljerte data om virkningsmekanisme (MOA) fra DrugBank
- Et biologisk rasjonale for CD123-involvering i esotropi, eller en omprioritering mot hematologiske CD123-positive tilstander
- Prekliniske eller observasjonelle data som støtter en ny indikasjon, før noen klinisk vurdering
## Ansvarsfraskrivelse

Dette innholdet er kun til forskningsformål og utgjør ikke medisinsk rådgivning.
Klinisk validering kreves før enhver klinisk anvendelse.

---

