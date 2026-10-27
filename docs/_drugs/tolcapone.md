---
layout: default
title: Tolcapone
parent: Kun modellprediksjon (L5)
nav_order: 425
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-15
description: "Tolcapone: predikert ny indikasjon Rasmussens subakutte encefalitt (evidensnivå L5). Opprinnelig indikasjon: Parkinsons sykdom"
monitor_inn: "TOLCAPONE"
predicted_indications: ["Rasmussen subacute encephalitis", "myelitis", "PLA2G6-associated neurodegeneration", "transaldolase deficiency", "fructose-1,6-bisphosphatase deficiency", "Lewy body dementia", "X-linked intellectual disability-ataxia-apraxia syndrome", "polymicrogyria, perisylvian, with cerebellar hypoplasia and arthrogryposis", "X-linked intellectual disability-cerebellar hypoplasia syndrome", "paralysis agitans, juvenile, of Hunt"]
---

# Tolcapone
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

## Tolkapon: Fra Parkinsons sykdom til Rasmussens subakutte encefalitt
{: .text-alpha }

## Oppsummering i én setning

Tolkapon er en COMT-hemmer som opprinnelig brukes til behandling av Parkinsons sykdom.
TxGNN-modellen forutsier at legemidlet kan ha effekt ved **Rasmussens subakutte encefalitt**, men det finnes foreløpig **ingen kliniske studier** og **ingen publikasjoner** som støtter denne retningen. Prediksjonen er rent beregningsbasert.

---

## Hurtigoversikt

| Punkt | Innhold |
|------|------|
| Opprinnelig indikasjon | Parkinsons sykdom |
| Predikert ny indikasjon | Rasmussens subakutte encefalitt |
| TxGNN-prediksjonsscore | 99,93 % |
| Evidensnivå | L5 |
| Markedsstatus i Norge | Kun avregistrerte (tilbakekalte/opphørte) godkjenninger |
| Antall godkjenninger | 1 (0 gyldige, 1 avregistrert) |
| Anbefalt beslutning | Hold |

---

## Hvorfor er denne prediksjonen rimelig?

Detaljerte data om virkningsmekanisme er ikke tilgjengelige i datagrunnlaget. Tolkapon er kjent som en hemmer av enzymet katekol-O-metyltransferase (COMT), som bryter ned blant annet levodopa og katekolaminer. Ved Parkinsons sykdom forlenger dette effekten av levodopa.

Rasmussens encefalitt er en immunmediert, kronisk betennelsessykdom i hjernen, vanligvis i én hjernehalvdel. Det er ikke påvist noen mekanistisk sammenheng mellom COMT-hemming og denne tilstanden. Den høye scoren er trolig et resultat av grafstruktur i kunnskapsgrafen, ikke av kjent biologi.

For oversiktens skyld vurderte modellen også andre kandidater. Disse er heller ikke støttet av kliniske data:

| Rangering | Predikert indikasjon | Score | Kommentar |
|------|------|------|------|
| 2 | Myelitt | 99,90 % | Ingen plausibel mekanisme |
| 3 | PLA2G6-assosiert nevrodegenerasjon | 99,88 % | Parkinsonlignende trekk kan forklare nærheten, men gir ikke effekt på den underliggende lipidmetabolismefeilen |
| 4 | Transaldolasemangel | 99,85 % | Sannsynligvis drevet av grafstruktur |
| 5 | Fruktose-1,6-bisfosfatasemangel | 99,78 % | Ingen kobling til COMT |
| 6 | Lewy body-demens | 99,64 % | Biologisk plausibel (dopaminerg dysfunksjon og alfa-synuklein), men uten klinisk evidens |
| 10 | Juvenil paralysis agitans (Hunt) | 99,52 % | I praksis den eksisterende indikasjonen under et annet navn |

---

## Evidens fra kliniske studier

Foreløpig er det ingen registrerte kliniske studier knyttet til denne prediksjonen.

---

## Litteraturevidens

Foreløpig finnes det ingen relevant litteratur for Rasmussens subakutte encefalitt.

For den sjette kandidaten, Lewy body-demens, er én publikasjon funnet:

| PMID | År | Type | Tidsskrift | Hovedfunn |
|------|-----|------|------|---------|
| [39259788](https://pubmed.ncbi.nlm.nih.gov/39259788/) | 2024 | Preklinisk (iPSC-organoidmodell) | Science Advances | Modellering av Lewy body-sykdom med kortikale organoider fra pasienter med SNCA-triplikasjon, og identifisering av mulige legemidler. Studien viser ikke klinisk evidens for tolkapon. |

---

## Markedsinformasjon for Norge

| Godkjenningsnummer | Produktnavn | Legemiddelform | Godkjent indikasjon |
|---------|------|------|-----------|
| EMEA/H/C/000132 | Tasmar (Viatris Healthcare Limited) | Ikke oppgitt | Parkinsons sykdom |

Godkjenningen har status avregistrert.

---

## Sikkerhetsvurderinger

Opplysninger fra pakningsvedlegg om advarsler og kontraindikasjoner er ikke tilgjengelige i datagrunnlaget. Se preparatomtalen for fullstendig sikkerhetsinformasjon.

**Kontraindikasjoner fra kunnskapsgrafen** (kunnskapsgrafen PrimeKG, ikke fra preparatomtale):
- Leversykdom
- Galleblæresykdom
- Melanom
- Hypotensive tilstander
- Rabdomyolyse
- Nodulær fasciitt
- Tardiv dyskinesi
- Lingual-facial-bukkal dyskinesi

Tolkapon er i tillegg kjent for leverskade (hepatotoksisitet), som er grunnen til at bruken er begrenset. Dette er en vesentlig sikkerhetsbekymring ved enhver ny bruk.

**Legemiddelinteraksjoner:** Totalt 65 interaksjoner er registrert. Blant de viste er:
- **Alvorlig (Major):** Metylenblått
- **Moderat:** Epinefrin (inkl. oftalmisk og topisk), morfin (inkl. liposomal), opium, kodein, dronabinol, nabilon, naltrekson, metoklopramid, etanol, prometazin, klorfeniramin, cetirizin, dekstrometorfan
- **Mindre (Minor):** Warfarin, dikumarol
- **Ukjent nivå:** Omeprazol

---

## Konklusjon og neste steg

**Beslutning: Hold**

**Begrunnelse:**
Prediksjonen for Rasmussens subakutte encefalitt støttes verken av kliniske studier eller litteratur, og det finnes ingen kjent mekanistisk sammenheng. Evidensnivået er L5 (kun modellprediksjon). I tillegg er tolkapons godkjenning i Norge avregistrert, og leverskaderisikoen er en betydelig barriere.

**For å gå videre kreves følgende:**
- Data om virkningsmekanisme (MOA) fra DrugBank
- Advarsler og kontraindikasjoner fra preparatomtalen (kritisk datahull som blokkerer sikkerhetsscreening)
- Prekliniske studier som tester en mulig sammenheng mellom COMT-hemming og Rasmussens encefalitt
- Vurdering av leversikkerhet og overvåkingsplan før noen klinisk utprøving
- Eventuelt vurdere Lewy body-demens som en mer biologisk plausibel kandidat for videre litteraturgjennomgang
## Ansvarsfraskrivelse

Dette innholdet er kun til forskningsformål og utgjør ikke medisinsk rådgivning.
Klinisk validering kreves før enhver klinisk anvendelse.

---

