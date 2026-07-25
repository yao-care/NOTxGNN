---
layout: default
title: Nedlastinger
nav_order: 94
permalink: /downloads/
description: "Åpne data til nedlasting fra NOTxGNN: FHIR-ressurser, prediksjonsresultater og søkeindeks."
---

# Nedlastinger

<div class="key-takeaway">
Prediksjonene publiseres i FHIR R4-format, klare til å integreres med journalsystemer.
</div>

---

## FHIR-ressurser

Dette nettstedet publiserer prediksjoner som FHIR R4-ressurser, som kan brukes direkte av SMART on FHIR-apper:

| Ressurs | Sti | Beskrivelse |
|----------|------|-------------|
| CapabilityStatement | `/fhir/metadata` | Kapabilitetserklæring for FHIR-serveren |
| MedicationKnowledge | `/fhir/MedicationKnowledge/` | Legemiddelressurser |
| ClinicalUseDefinition | `/fhir/ClinicalUseDefinition/` | Predikerte indikasjoner |
| Bundle | `/fhir/Bundle/all-predictions.json` | Alle prediksjoner samlet |

---

## Søkeindeks

`/data/search-index.json` gir en søkeindeks over legemidler og indikasjoner, slik at du kan bygge
ditt eget grensesnitt for oppslag.

---

## Bruksvilkår

<ol class="actionable-steps">
<li>Dataene på dette nettstedet er <strong>kun ment som referanse for forskning</strong> og skal ikke brukes som grunnlag for medisinske beslutninger.</li>
<li>Ved sitering skal du kreditere NOTxGNN (藥提醒科技有限公司) og sitere den opprinnelige TxGNN-artikkelen.</li>
<li>Videre bruk av dataene er fortsatt underlagt lisensvilkårene til hver enkelt opprinnelige kilde (se <a href="{{ '/sources/' | relative_url }}">Datakilder</a>).</li>
</ol>

---

## Om utvikleren

Denne plattformen er utviklet og drives av **藥提醒科技有限公司** (yao.care, organisasjonsnummer
83620786, 12F, No. 220, Sec. 2, Taiwan Blvd., West Dist., Taichung City, Taiwan).

NOTxGNN er Norge-nettstedet i selskapets produktlinje «TxGNN Drug Repurposing».
Det samme systemet er satt i drift i 30 land og regioner, hvert med navnet `{CC}TxGNN`
(JpTxGNN, UsTxGNN, DETxGNN og så videre) på `{cc}txgnn.yao.care`.
Produktoversikt: <https://www.yao.care/medical/txgnn/>.

Selve TxGNN-modellen ble utviklet av Zitnik Lab ved Harvard Medical School og publisert
i *Nature Medicine*. Denne plattformen er produksjonssystemet som 藥提醒科技有限公司 har bygget oppå
den modellen, og omfatter integrasjon av nasjonale legemiddelregistreringsdata, dobbel prediksjon
med kunnskapsgraf og dyp læring, evidensgradering fra PubMed / ClinicalTrials samt integrasjon mot
elektronisk pasientjournal via SMART on FHIR.

---

<div class="disclaimer">
<strong>Ansvarsfraskrivelse</strong><br>
Denne rapporten er kun ment som referanse for akademisk forskning og <strong>utgjør ikke medisinske råd</strong>. Følg alltid legens anvisninger; juster aldri medisineringen på egen hånd. Enhver beslutning om legemiddelreposisjonering krever fullstendig klinisk validering og regulatorisk gjennomgang.
<br><br>
<small>Gjennomgått av: 藥提醒科技有限公司 (yao.care)</small>
</div>
