---
layout: default
title: Rasagiline
parent: Kun modellprediksjon (L5)
nav_order: 348
evidence_level: L5
indication_count: 6
last_modified_at: 2026-10-15
description: "Rasagiline: predikert ny indikasjon PLA2G6-assosiert nevrodegenerasjon (evidensnivå L5). Opprinnelig indikasjon: Parkinsons sykdom"
monitor_inn: "RASAGILINE"
predicted_indications: ["PLA2G6-associated neurodegeneration", "Rasmussen subacute encephalitis", "myelitis", "paralysis agitans, juvenile, of Hunt", "transaldolase deficiency", "polymicrogyria, perisylvian, with cerebellar hypoplasia and arthrogryposis"]
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

# Rasagilin: Fra Parkinsons sykdom til PLA2G6-assosiert nevrodegenerasjon

## Oppsummering i én setning

Rasagilin er en MAO-B-hemmer som opprinnelig brukes til behandling av **Parkinsons sykdom**.
TxGNN-modellen predikerer at legemidlet kan ha effekt på **PLA2G6-assosiert nevrodegenerasjon**, men det finnes foreløpig **ingen kliniske studier** og **ingen publikasjoner** i de innsamlede dataene som støtter denne retningen. Prediksjonen er rent beregningsbasert.

---

## Hurtigoversikt

| Punkt | Innhold |
|------|------|
| Opprinnelig indikasjon | Parkinsons sykdom |
| Predikert ny indikasjon | PLA2G6-assosiert nevrodegenerasjon |
| TxGNN-prediksjonsscore | 99,71 % |
| Evidensnivå | L5 |
| Markedsstatus i Norge | Kun opphevede (avregistrerte) godkjenninger |
| Antall godkjenninger | 3 (alle opphevet, ingen gyldige) |
| Anbefalt beslutning | Hold |

---

## Hvorfor er denne prediksjonen rimelig?

Data om virkningsmekanisme (MOA) er ikke tilgjengelig i det innsamlede materialet. Ut fra allment kjent kunnskap er rasagilin en irreversibel MAO-B-hemmer som reduserer nedbrytningen av dopamin og dermed øker tilgjengeligheten av dopamin. Effekten ved Parkinsons sykdom er godt etablert, og legemidlet kan i tillegg ha nevrobeskyttende egenskaper. Denne mekanismebeskrivelsen er ikke hentet fra de innsamlede dataene.

PLA2G6-assosiert nevrodegenerasjon omfatter blant annet infantil nevroaksonal dystrofi og PLA2G6-relatert dystoni-parkinsonisme. Disse tilstandene har fellestrekk med Parkinsons sykdom, som dopaminerg dysfunksjon, alfa-synuklein-patologi og mitokondriell/oksidativ stress. Symptomlindring ved den parkinsonistiske fenotypen er derfor teoretisk plausibel.

Koblingen er imidlertid kun teoretisk. Det finnes ingen støtte for at rasagilin påvirker den underliggende defekten i lipidmetabolismen. Den svært høye TxGNN-scoren (0,997) er en beregningsmessig prediksjon og ikke klinisk evidens.

---

## Klinisk studieevidens

Foreløpig er det ingen relaterte kliniske studier registrert.

---

## Litteraturevidens

Foreløpig er det ingen relatert litteratur tilgjengelig.

---

## Markedsinformasjon for Norge

Alle tre godkjenningene er opphevet. Det finnes ingen gyldige godkjenninger.

| Godkjenningsnummer | Produktnavn | Legemiddelform | Godkjent indikasjon |
|---------|------|------|-----------|
| EMEA/H/C/004064 | Rasagiline Viatris (tidligere Rasagiline Mylan) | – | Parkinsons sykdom |
| EMEA/H/C/003957 | Rasagiline ratiopharm | – | Parkinsons sykdom |
| EMEA/H/C/000574 | Azilect | – | Parkinsons sykdom |

---

## Sikkerhetsvurderinger

Pakningsvedlegget er ikke tilgjengelig i de innsamlede dataene, så advarsler og kontraindikasjoner fra preparatomtalen kan ikke gjengis. Se pakningsvedlegget for fullstendig sikkerhetsinformasjon.

- **Kontraindikasjoner fra kunnskapsgrafen (ikke fra preparatomtale)**: TxGNNs kunnskapsgraf (PrimeKG) knytter rasagilin til følgende tilstander: hypertensjon, multippel systematrofi, posturalt ortostatisk takykardisyndrom, ortostatisk hypotensjon, legemiddelindusert dyskinesi, epilepsi, bipolar lidelse, alvorlig affektiv lidelse, leversykdom, gallblæresykdom, melanom, feokromocytom (binyre), duodenalkreft, tynntarmskreft, hjertekreft, binyrekreft og sympatisk paragangliom.
- **Legemiddelinteraksjoner**: Søket er gjennomført og fant 100 registrerte interaksjoner. Blant de første 20 som ble hentet, er de viktigste:
  - **Alvorlig (Major)**: bupropion, morfin
  - **Moderat**: epinefrin, klorpropamid, cimetidin, dietylpropion, difenoksin, difenoksylat, dronabinol, obetikolsyre, fentermin, glimepirid samt flere insulinpreparater (aspart, degludec, detemir, glargin, glulisin, humant isofan, humant regulært, inhalert hurtigvirkende)

---

## Konklusjon og neste steg

**Beslutning: Hold**

**Begrunnelse:**
Prediksjonen bygger kun på modellscore (evidensnivå L5), uten kliniske studier eller publikasjoner. Mekanismekoblingen er spekulativ, MOA-data mangler, og sikkerhetsdata fra preparatomtalen er ikke tilgjengelig. Alle norske godkjenninger er dessuten opphevet.

**For å gå videre kreves følgende:**
- Hente og analysere pakningsvedlegg/preparatomtale (advarsler og kontraindikasjoner), som er en blokkerende datamangel
- Hente data om virkningsmekanisme (MOA) fra DrugBank
- Systematisk litteratur- og studiesøk spesifikt for PLA2G6-assosiert nevrodegenerasjon
- Prekliniske data som viser effekt i relevante modeller
- Vurdering av sikkerhet og dosering i barn og unge

**Tilleggsmerknad om andre prediksjoner:**
Blant de øvrige predikerte indikasjonene er **juvenil parkinsonisme (Hunt-type)** (score 99,25 %, evidensnivå L4, anbefaling «forskningsspørsmål») den mest troverdige kandidaten. Den ligger nær den godkjente indikasjonen Parkinsons sykdom, men evidensen er indirekte (ekstrapolert) og krever målrettet gjennomgang. De øvrige (Rasmussen-encefalitt, myelitt, transaldolasemangel og polymikrogyri med cerebellær hypoplasi) har svake eller ingen mekanistiske koblinger og anbefales som Hold.
## Ansvarsfraskrivelse

Dette innholdet er kun til forskningsformål og utgjør ikke medisinsk rådgivning.
Klinisk validering kreves før enhver klinisk anvendelse.

---

