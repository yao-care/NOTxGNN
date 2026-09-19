---
layout: default
title: Tadalafil
parent: Kun modellprediksjon (L5)
nav_order: 336
evidence_level: L5
indication_count: 8
---

# Tadalafil
{: .fs-9 }

Evidensnivå: **L5** | Predikerte indikasjoner: **8** stk.
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

# Tadalafil: Fra PDE5-mediert vaskulær indikasjon til Ambras type hypertrichosis universalis congenita — evidens utilstrekkelig

## Oppsummering i én setning

> Tadalafil er en PDE5 (fosfodiesteeras type 5)-hemmer hvis etablerte farmakologi virker på vaskulær glatt muskulatur og corpus cavernosum-vev, men ingen godkjent indikasjon eller MOA-journal er til stede i denne evidenspakken.
> TxGNNs topprangerte prediksjon — **Ambras type hypertrichosis universalis congenita** — har **ingen kliniske studier og ingen støttende litteratur**, og modellens egen begrunnelse markerer den som sannsynligvis en embedding-artefakt snarere enn et biologisk plausibelt signal.
> Av alle 8 screenede kandidatindikasjonene når ingen et forsvarlig evidensnivå; det eneste mest klinisk relevante litteraturtreffet (en kasusrapport) beskriver faktisk tadalafil-*forårsaket* migreneaura, dvs. en uønsket effekt, ikke et terapeutisk signal.

---

## Hurtigoversikt

| Element | Innhold |
|---------|---------|
| Originalindikasjon | Ikke registrert i evidenspakken (ingen godkjente indikasjoner i saksmappe); kjent PDE5-hemmer farmakologi retter seg mot vaskulær glatt muskulatur / corpus cavernosum |
| Forutsagt ny indikasjon | Ambras type hypertrichosis universalis congenita |
| TxGNN-prediksjonspoengsum | 99.98% |
| Evidensnivå | L5 |
| Markedsstatus Norge | Ikke markedsført |
| Antall godkjennelser | 0 |
| Anbefalt beslutning | Avvent |

---

## Hvorfor er denne prediksjonen rimelig?

For tiden er ikke detaljerte mekanisme-data tilgjengelige (flagget som en blokkering/høy-alvorlighetsgrad datakløft i denne pakken). Basert på fragmentene som er tilgjengelige, er tadalafil kjent for å virke som en **PDE5-hemmer**, med farmakologiske effekter på vaskulær glatt muskulatur og corpus cavernosum-vev — det mekanistiske grunnlaget som typisk siteres for tadalafils etablerte bruksområder (erektil dysfunksjon, BPH, pulmonal arteriell hypertensjon), selv om den spesifikke originalindikasjonen ikke i seg selv er registrert i denne evidenspakken.

Den topprangerte prediksjonen, Ambras type hypertrichosis universalis congenita, er en sjelden medfødt hårvekstforstyrrelse. Det er ingen kjent eller antatt vei som knytter PDE5/cGMP-mediiert vasodilatation til follikelvekstregulering. Modellens egen begrunnelse angir eksplisitt at dette poengsum gjenspeiler en "embedding-artefakt" snarere enn et biologisk basert signal — en konklusjon gjentatt for rang #2, #4, #5, og #6 (hypertrichosis, Dandy-Walker-assosiiert syndrom, hårstaftabnormitet, trichomegaly), som alle skorer >99.6% med **null kliniske studier og null litteraturstøtte**.

Rang #3 (et periodontalt/odontalt malformasjonssyndrom) ser opprinnelig bedre ut med 20 litteraturtreff, men ved nærmere gjennomgang adresserer hver artikkel generell periodontalpataofysiologi eller behandling — **ingen nevner tadalafil eller PDE5-hemmere i det hele tatt**. Dette er støy fra medforekomst av sykdomsbegreper, ikke legemiddelrelevant evidens. Rang #7 (kyphoskoliotisk hjertesykdom) har en teoretisk sammenhengsfull hypotese (PDE5-hemmere brukes i pulmonal hypertensjon, som kan komplisere kyphoskoliose) men null støttende studier eller litteratur. Samlet sett klarer ingen kandidat i denne pakken selv en preliminær mekanistisk-plausibilitetskriteria med virkelighetsbasert evidens.

---

## Klinisk prøvebevis

For tiden er ingen relaterte kliniske studier registrert.

---

## Litteraturbevis

For tiden ingen relatert litteratur tilgjengelig for topprangerte indikasjon (Ambras type hypertrichosis universalis congenita).

---

## Markedsinformasjon Norge

Ingen markedsføringstillatelser er registrert for tadalafil i denne evidenspakken. Markedsstatus er registrert som **"Ikke markedsført"** med **0 totale lisenser** og ingen dosisformer/ruter oppført.

---

## Andre screenede kandidatindikasjonser (kontekst)

Fordi denne evidenspakken evaluerte 8 kandidater for tadalafil, oppsummerer tabellen nedenfor hvorfor hver enkelt ble screenet ut, for fullstendighet:

| Rang | Sykdom | TxGNN-poengsum | Evidens | Vurdering |
|------|--------|----------------|---------|-----------|
| 2 | Hypertrichosis (sykdom) | 99.98% | Ingen | Ingen mekanistisk kobling |
| 3 | Odontalt/periodontalt malformasjonssyndrom | 99.97% | 20 arbeider, ingen legemiddelspesifikk | Medforekomst-støy |
| 4 | Dandy-Walker malformasjonssyndrom | 99.97% | Ingen | Ingen mekanistisk kobling |
| 5 | Isolert genetisk hårstaftabnormitet | 99.96% | Ingen | Ingen mekanistisk kobling |
| 6 | Familiær isolert trichomegaly | 99.65% | Ingen | Ingen mekanistisk kobling |
| 7 | Kyphoskoliotisk hjertesykdom | 99.43% | Ingen | Teoretisk PAH-overlap-hypotese bare, ubekreftet |
| 8 | Migrene med hjernestammeavura | 99.08% | 1 kasusrapport ([PMID 17059442](https://pubmed.ncbi.nlm.nih.gov/17059442/)) | **Uønsket-effekt-signal, ikke terapeutisk evidens** — se Sikkerhet nedenfor |

---

## Sikkerhet

- **Viktige advarsler / Kontraindikasjoner**: Ikke tilgjengelig i denne evidenspakken (TFDA/etikett-data flagget som en blokkering datakløft — DG001).
- **Legemiddelinteraksjoner**: Ingen DDI-data returnert (spørringsstatus: ikke funnet).
- **Litteraturutledet sikkerhetssignal**: En kasusrapport ([PMID 17059442](https://pubmed.ncbi.nlm.nih.gov/17059442/), *Cephalalgia*, 2006) beskriver tadalafil-assosiiert typisk migreneaura uten hodepine. Dette antyder at PDE5-hemmer–mediiert cerebral vasodilatation kan *utløse* migrene-aura-lignende hendelser — det motsatte av en terapeutisk effekt for migrene, og verdt å merke som en advarsel snarere enn en repurposing-kandidat.

---

## Konklusjon og neste trinn

**Beslutning: Avvent**

**Begrunnelse:**
Alle 8 kandidatindikasjonene ligger på evidensnivå L5 (eller L4 for en enkelt uønsket-effekt kasusrapport), med `decision_stage: S0` og ingen klinisk studie- eller legemiddelspesifikk litteraturstøtte. De høyest-scorende prediksjoner er eksplisitt flagget av modellens egen begrunnelse som embedding-artefakter. Ingen kandidat i denne pakken når terskelen for å avansere forbi initiell screening.

**For å fortsette er følgende nødvendig:**
- Løs DG001 (Blokkering): skaff TFDA/etikett-advarsler og kontraindikasjoner — påkrevd før noen S1 sikkerhet pre-vurdering kan begynne.
- Løs DG002 (Høy): skaff bekreftet MOA og godkjente indikasjoner fra DrugBank — påkrevd for å etablere en genuint mekanistisk begrunnelse for en kandidat.
- Hvis du forfølger rang #7 (kyphoskoliotisk hjertesykdom / pulmonal hypertensjon-overlap) videre, bestill et målrettet litteratursøk for tadalafil i kyphoskoliose-assosiiert pulmonal hypertensjon spesifikt, siden den nåværende pakken fant ingen legemiddelspesifikke studier.
- Ingen ytterligere handling anbefales for rang #1–6, #8 uten nye eksperimentelle eller kliniske data — disse er ikke levedyktige kandidater for legemiddelombruk basert på nåværende evidens.

## Ansvarsfraskrivelse

Dette innholdet er kun til forskningsformål og utgjør ikke medisinsk rådgivning.
Klinisk validering kreves før enhver klinisk anvendelse.

---

