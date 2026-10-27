---
layout: default
title: Temoporfin
parent: Kun modellprediksjon (L5)
nav_order: 405
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-15
description: "Temoporfin: predikert ny indikasjon Nasofaryngealt teratom (evidensnivå L5). Opprinnelig indikasjon: Hode- og halskreft"
monitor_inn: "TEMOPORFIN"
predicted_indications: ["nasopharyngeal teratoma", "odontogenic cyst", "pre-malignant neoplasm", "epiglottis neoplasm", "tumor of testis and paratestis", "cystic neoplasm", "benign neoplasm of floor of mouth", "benign neoplasm of tongue", "benign neoplasm of hypopharynx", "cervical neuroblastoma"]
---

# Temoporfin
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

## Temoporfin: Fra hode- og halskreft til nasofaryngealt teratom
{: .text-alpha }

## Oppsummering i én setning

Temoporfin er et fotosensibiliserende middel som opprinnelig brukes i fotodynamisk terapi (PDT) ved plateepitelkarsinom i hode og hals.
TxGNN-modellen forutsier at det kan være effektivt ved **nasofaryngealt teratom**,
men det finnes **ingen registrerte kliniske studier** og **ingen publikasjoner** som støtter akkurat denne prediksjonen. Prediksjonen bygger kun på modellen.

---

## Hurtigoversikt

| Punkt | Innhold |
|------|------|
| Opprinnelig indikasjon | Hode- og halskreft; plateepitelkarsinom |
| Predikert ny indikasjon | Nasofaryngealt teratom |
| TxGNN-prediksjonsscore | 99,78 % |
| Evidensnivå | L5 |
| Markedsstatus i Norge | Kun tilbakekalt/avregistrert (ingen gyldig markedsføringstillatelse) |
| Antall tillatelser | 1 (0 gyldige, 1 avregistrert) |
| Anbefalt beslutning | Hold |

---

## Hvorfor er prediksjonen rimelig (eller ikke)?

Data om virkningsmekanisme (MOA) er ikke tilgjengelig for denne rapporten. Temoporfin er et fotosensibiliserende middel brukt i fotodynamisk terapi mot plateepitelkarsinom i hode og hals. Det antas at stoffet hoper seg opp i uregelmessig vev og, når det aktiveres av lys, gir celleskade i proliferende vev.

Koblingen til nasofaryngealt teratom er kun en prediksjon fra kunnskapsgrafen (høy TxGNN-score). Teratomer er biologisk forskjellige fra plateepitelkarsinom, og det finnes verken kliniske studier eller litteratur som støtter bruken. Prediksjonen er derfor svakt underbygd.

### Øvrige prediksjoner (rangert)

Oversikten viser de ti høyest rangerte prediksjonene og en vurdering av hver.

| Rang | Predikert indikasjon | Score | Evidensnivå | Vurdering |
|---|---|---|---|---|
| 1 | Nasofaryngealt teratom | 99,78 % | L5 | Kun kunnskapsgraf; ulik biologi enn plateepitelkarsinom |
| 2 | Odontogen cyste | 99,77 % | L5 | Basert på felles anatomisk område; ingen data for godartede cystiske lesjoner |
| 3 | Premalign neoplasi | 99,77 % | L5 | Mekanistisk mest plausibel (f.eks. oral dysplasi), men trenger egen litteratursøk |
| 4 | Neoplasi i epiglottis | 99,76 % | L5 | Oftest plateepitelkarsinom, nær opprinnelig indikasjon; ingen spesifikke studier |
| 5 | Svulst i testikkel og parateste | 99,76 % | L5 | Ingen tydelig mekanistisk kobling; lyslevering er upraktisk |
| 6 | Cystisk neoplasi | 99,76 % | L4 | Kun indirekte evidens (én publikasjon) |
| 7 | Godartet neoplasi i munngulv | 99,76 % | L5 | Tilgjengelig for lys, men ingen evidens for godartede svulster |
| 8 | Godartet neoplasi i tunge | 99,76 % | L4 | Kun indirekte evidens (én publikasjon) |
| 9 | Godartet neoplasi i hypofarynx | 99,76 % | L5 | Kun anatomisk assosiasjon i kunnskapsgrafen |
| 10 | Cervikalt nevroblastom | 99,76 % | L5 | Annen biologi (nevralkamcelle-avledet); ingen støtte |

---

## Kliniske studier

For den primære prediksjonen (nasofaryngealt teratom) er det for tiden ingen relaterte kliniske studier registrert. Det gjelder også for alle de øvrige ni prediksjonene.

---

## Litteraturevidens

For den primære prediksjonen finnes det for tiden ingen relatert litteratur. To av de øvrige prediksjonene har indirekte litteratur:

| PMID | År | Type | Tidsskrift | Hovedfunn |
|------|-----|------|------|---------|
| [26072296](https://pubmed.ncbi.nlm.nih.gov/26072296/) | 2015 | Kohortestudie | Photodiagnosis and Photodynamic Therapy | PDT som supplement til kirurgi ved tilbakevendende ondartede svulster i bihuler og fremre skallebasis; gjennomførbarhet rapportert. Knyttet til «cystisk neoplasi», men gjelder ondartede svulster generelt |
| [26179387](https://pubmed.ncbi.nlm.nih.gov/26179387/) | 2015 | Kasuistikkserie/kohorte | World Journal of Surgical Oncology | Postoperativ temoporfin-mediert PDT etter robotassistert salvage-kirurgi ved tilbakevendende plateepitelkarsinom i tungebasis. Knyttet til «godartet neoplasi i tunge», men gjelder ondartet sykdom |

Begge publikasjonene er indirekte evidens og støtter ikke de predikerte godartede eller cystiske tilstandene direkte.

---

## Informasjon om markedet i Norge

| Tillatelsesnummer | Produktnavn | Doseringsform | Godkjent indikasjon |
|---------|------|------|-----------|
| EMEA/H/C/000318 | Foscan | Ikke oppgitt | Hode- og halskreft; plateepitelkarsinom |

Tillatelsen er avregistrert, og det finnes ingen gyldige tillatelser i Norge.

---

## Cytotoksisitet

| Punkt | Innhold |
|------|------|
| Cytotoksisitetsklassifisering | Fotosensibilisator for fotodynamisk terapi (lysaktivert cytotoksisk effekt); ikke konvensjonell cellegift |
| Myelosuppresjonsrisiko | Se pakningsvedlegg for advarsler og forholdsregler |
| Emetogenisitet | Se pakningsvedlegg for advarsler og forholdsregler |
| Overvåkingspunkter | Se pakningsvedlegg for advarsler og forholdsregler |
| Håndteringsbeskyttelse | Se pakningsvedlegg for advarsler og forholdsregler |

---

## Sikkerhetsvurderinger

Se pakningsvedlegget for sikkerhetsinformasjon. Det ble ikke funnet registrerte legemiddelinteraksjoner i dataene som er sammenstilt for denne rapporten, og kunnskapsgrafen oppgir ingen kontraindiserte sykdommer.

---

## Konklusjon og neste steg

**Beslutning: Hold**

**Begrunnelse:**
Den primære prediksjonen (nasofaryngealt teratom) har kun modellstøtte (L5) uten kliniske studier eller litteratur, og biologien skiller seg fra den opprinnelige indikasjonen. I tillegg er den norske tillatelsen avregistrert, og sikkerhetsdata fra pakningsvedlegget mangler.

**For å gå videre kreves følgende:**
- Hente og analysere pakningsvedlegget (advarsler og kontraindikasjoner), som er en blokkerende datamangel for sikkerhetsscreening
- Hente data om virkningsmekanisme (MOA) fra DrugBank
- Gjennomføre et målrettet litteratursøk, særlig for **premalign neoplasi** og **neoplasi i epiglottis**, som er de mest mekanistisk plausible kandidatene
- Avklare om det finnes en gyldig markedsføringstillatelse eller alternativ tilgang til temoporfin i Norge
- Vurdere administrasjonsvei og lysleveringsmuligheter for hver aktuelle indikasjon
## Ansvarsfraskrivelse

Dette innholdet er kun til forskningsformål og utgjør ikke medisinsk rådgivning.
Klinisk validering kreves før enhver klinisk anvendelse.

---

