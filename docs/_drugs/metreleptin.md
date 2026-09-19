---
layout: default
title: Metreleptin
parent: Kun modellprediksjon (L5)
nav_order: 229
evidence_level: L5
indication_count: 10
---

# Metreleptin
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

# Metreleptin: Fra leptin-mangel (lipodystrofi) til familial generalisert lentiginose

## Sammenfatting i en setning

Metreleptin er en rekombinant leptin-analog som brukes til å behandle leptin-mangel ved generalisert lipodystrofi. TxGNN-modellens toppprediksjon er **Familial generalisert lentiginose**, med en **99.71%** prediksjonspoeng, men det finnes for øyeblikket **0 kliniske prøver** og **0 publikasjoner** som støtter denne retningen — evidenspakkens egen mekanistiske analyse finner heller ingen plausibel biologisk forbindelse.

---

## Kort oversikt

| Punkt | Innhold |
|-------|---------|
| Opprinnelig indikasjon | Ikke til stede i evidenspakken (datamanko). Metreleptin er generelt kjent som behandling for leptin-mangel forbundet med generalisert lipodystrofi |
| Predikert ny indikasjon | Familial generalisert lentiginose |
| TxGNN prediksjonspoeng | 99.71% |
| Bevisnivå | L5 |
| Markedsstatus i Norge | ✗ Ikke markedsført |
| Antall autorisasjoner | 0 |
| Anbefalt beslutning | Avvent |

---

## Hvorfor er denne prediksjonen rimelig?

For øyeblikket er detaljert virkningsmåtedata ikke tilgjengelig (datamanko). Basert på begrenset informasjon i evidenspakken, fungerer metreleptin som en leptin-reseptor agonist, som primært regulerer hypotalamisk energimetabolisme og signalering av fettvev.

Familial generalisert lentiginose er en autosomalt dominant pigmentær hudsykdom. Evidenspakkens egen rasjonale-analyse sier at det **ikke er noen kjent mekanistisk forbindelse** mellom leptin-signalveien og patologien til denne sykdommen, og ingen hypotese kunne etableres på grunn av manglende virkningsmåtedata.

Det samme mønsteret gjelder over alle topp-10 TxGNN-kandidater for dette legemidlet (se sykdomsliste i kildedataene): sjeldne pigmentære syndromer (gastrokutant syndrom, Moynahan-syndrom, akromelanose, osv.), tumorentiteter drevet av urelaterte veier (rabdomyoid tumor via SMARCB1/INI1-tap, schwannoma via NF2/merlin-tap), og andre sjeldne multisystem-syndromer — hvorav ingen har en etablert eller plausibel forbindelse til leptin-reseptor-signalering per den gitte rasjonalen. Dette tyder på at prediksjonen er drevet primært av nettverksbasert likhet i TxGNN-modellen heller enn en forsvarbelig biologisk mekanisme.

---

## Kliniske prøvebevis

For øyeblikket ingen relaterte kliniske prøver registrert.

---

## Litteraturbevis

For øyeblikket ingen relatert litteratur tilgjengelig.

---

## Markedsinformasjon for Norge

Metreleptin har for øyeblikket **ingen markedsføringsautoriseringer i Norge** (0 lisenser på register); legemidlet er ikke markedsført i dette markedet.

---

## Sikkerhetshensyn

Se pakningsvedlegget for sikkerhetsinformasjon.

Merk: TFDA/Norge etikett-advarsler og kontraindikasjoner (DG001) er flagget som en **Blokkerende** datamanko i kildeevidsenpakken, noe som betyr at en formell sikkerhetsevaluering (S1) ikke kan fullføres for øyeblikket for denne kandidaten.

---

## Konklusjon og neste trinn

**Beslutning: Avvent**

**Rasjonale:**
Alle topp-10 predikerte indikasjoner for metreleptin ligger på bevisnivå L5 (modellprediksjon kun — ingen kliniske prøver, ingen litteratur), og evidenspakkens egen mekanistiske gjennomgang fant ingen plausibel biologisk rasjonale som knytter leptin-reseptor-signalering til noen av kandidatsykdommene. Kombinert med en Blokkerende-alvorlighetsgrad sikkerhetsdatamanko og null markedstilstedeværelse i Norge, finnes det for øyeblikket ikke grunnlag for å fremme denne kandidaten.

**For å gå videre er følgende nødvendig:**
- TFDA/Norge etikett-advarsler, kontraindikasjoner og DDI-data (DG001, Blokkerende)
- Bekreftet virkningsmåte fra DrugBank eller primærlitteratur (DG002)
- Målrettet litteratur-/klinisk prøvesøk spesifikt for topprangerte kandidatsykdommer for å kontrollere for eventuelle bevis som TxGNNs treningsdata kanskje ikke avdekket
- Uavhengig farmakologisk plausibilitetsvurdering før videre evalueringsressurser tildeles til dette legemiddel-indikasjon-paret

## Ansvarsfraskrivelse

Dette innholdet er kun til forskningsformål og utgjør ikke medisinsk rådgivning.
Klinisk validering kreves før enhver klinisk anvendelse.

---

