---
layout: default
title: Simoctocog Alfa
parent: Kun modellprediksjon (L5)
nav_order: 384
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-15
description: "Simoctocog Alfa: predikert ny indikasjon Pseudo-von Willebrand sykdom (evidensnivå L5). Opprinnelig indikasjon: Hemofili A"
monitor_inn: "SIMOCTOCOG ALFA"
predicted_indications: ["pseudo-von Willebrand disease", "primary release disorder of platelets", "Glanzmann thrombasthenia", "Scott syndrome", "acquired coagulation factor deficiency", "bleeding diathesis due to a collagen receptor defect", "hemorrhagic disorder due to a constitutional thrombocytopenia", "fetal and neonatal alloimmune thrombocytopenia", "thrombotic thrombocytopenic purpura"]
---

# Simoctocog Alfa
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

## Simoktokog alfa: Fra hemofili A til pseudo-von Willebrand sykdom
{: .text-alpha }

## Sammendrag i én setning

Simoktokog alfa er en rekombinant human koagulasjonsfaktor VIII (B-domene-deletert), opprinnelig brukt til behandling av **hemofili A**.
TxGNN-modellen predikerer at legemidlet kan ha effekt ved **pseudo-von Willebrand sykdom**, men det finnes **ingen kliniske studier** og **ingen publikasjoner** i de samlede dataene som støtter denne retningen. Prediksjonen er kun modellbasert.

---

## Hurtigoversikt

| Punkt | Innhold |
|------|------|
| Opprinnelig indikasjon | Hemofili A |
| Predikert ny indikasjon | Pseudo-von Willebrand sykdom |
| TxGNN-prediksjonsscore | 99,997 % |
| Evidensnivå | L5 |
| Markedsstatus i Norge | Kun avregistrerte (trukket fra markedet) |
| Antall godkjenninger | 2 (begge avregistrert) |
| Anbefalt beslutning | Hold |

---

## Hvorfor er denne prediksjonen (ikke) rimelig?

Detaljerte data om virkningsmekanisme er foreløpig ikke tilgjengelige. Basert på kjent informasjon er simoktokog alfa en rekombinant faktor VIII som erstatter manglende FVIII ved hemofili A, og effekten ved den opprinnelige indikasjonen er etablert.

Pseudo-von Willebrand sykdom er en blodplatelidelse forårsaket av gain-of-function-mutasjon i GP1BA. Den fører til økt binding av høymolekylære VWF-multimerer og økt klaring av blodplater. FVIII-erstatning korrigerer ikke denne defekten i blodplatenes GPIb-reseptor. Den svært høye TxGNN-scoren (0,99997) er trolig drevet av delte assosiasjoner i koagulasjonsnettverket og ikke av en påvist biologisk mekanisme.

Det samme mønsteret gjelder for de øvrige predikerte indikasjonene (rangert 2–10). De fleste er blodplatedefekter eller trombocytopenier der FVIII ikke har noen kjent rolle:

| Rang | Predikert sykdom | Score | Vurdering |
|---|---|---|---|
| 2 | Primær frigjøringsdefekt av blodplater | 99,997 % | Defekt i blodplatesekresjon; FVIII korrigerer ikke dette |
| 3 | Glanzmanns trombasteni | 99,995 % | Defekt i integrin αIIbβ3; standardbehandling er blodplatetransfusjon eller rFVIIa |
| 4 | Scotts syndrom | 99,969 % | Svak teoretisk kobling via tenase-komplekset, men ingen evidens |
| 5 | Ervervet koagulasjonsfaktormangel | 99,952 % | Mekanistisk mest plausibel, men heterogen kategori; ervervet hemofili behandles vanligvis med bypass-midler |
| 6 | Blødningstendens ved kollagenreseptordefekt | 99,921 % | FVIII adresserer ikke reseptordefekten |
| 7 | Blødningslidelse ved konstitusjonell trombocytopeni | 99,917 % | Lavt blodplatetall/-funksjon, ikke FVIII-mangel |
| 8 | Føtal og neonatal alloimmun trombocytopeni | 99,845 % | Alloimmun blodplateødeleggelse; FVIII har ingen rolle |
| 9 | Hemofili A med vaskulær abnormitet | 99,779 % | Dekkes i praksis av den godkjente hemofili A-indikasjonen; ikke en reell ny indikasjon |
| 10 | Trombotisk trombocytopenisk purpura (TTP) | 99,724 % | Potensiell sikkerhetsrisiko: økt FVIII kan øke trombosefaren |

---

## Evidens fra kliniske studier

Foreløpig er det ingen registrerte kliniske studier knyttet til denne prediksjonen.

---

## Litteraturevidens

Foreløpig finnes det ingen relevant litteratur.

---

## Markedsinformasjon for Norge

| Godkjenningsnummer | Produktnavn | Doseringsform | Godkjent indikasjon |
|---------|------|------|-----------|
| EMEA/H/C/002813 | Nuwiq | Ikke oppgitt | Hemofili A (avregistrert) |
| EMEA/H/C/004459 | Vihuma | Ikke oppgitt | Hemofili A (avregistrert) |

Begge godkjenningene er avregistrert, og det finnes ingen gyldige markedsføringstillatelser.

---

## Sikkerhetsvurderinger

- **Legemiddelinteraksjoner:** Ingen interaksjoner ble funnet i de samlede dataene.
- **Spesiell sikkerhetsbekymring (TTP):** Ved trombotisk trombocytopenisk purpura er det en prokoagulant mikroangiopati. Tilførsel av FVIII kan potensielt forverre trombosefaren, og dette er en risiko snarere enn en fordel.

For øvrig sikkerhetsinformasjon, se pakningsvedlegget (preparatomtalen).

---

## Konklusjon og neste steg

**Beslutning: Hold**

**Begrunnelse:**
Prediksjonen er kun modellbasert (L5) uten kliniske studier eller litteratur, og den biologiske mekanismen støtter ikke FVIII-erstatning ved de predikerte blodplatelidelsene. I tillegg er begge produktene avregistrert i Norge, noe som begrenser praktisk gjennomførbarhet.

**For å gå videre kreves følgende:**
- Data om virkningsmekanisme (MOA) fra DrugBank
- Advarsler og kontraindikasjoner fra pakningsvedlegget (preparatomtale), nødvendig for sikkerhetsscreening
- Ved eventuell videre vurdering: avgrens til «ervervet koagulasjonsfaktormangel» (rang 5) med en målrettet litteraturgjennomgang, og utelukk TTP på sikkerhetsgrunnlag
- Avklaring av produktenes tilgjengelighet siden begge godkjenningene er avregistrert
## Ansvarsfraskrivelse

Dette innholdet er kun til forskningsformål og utgjør ikke medisinsk rådgivning.
Klinisk validering kreves før enhver klinisk anvendelse.

---

