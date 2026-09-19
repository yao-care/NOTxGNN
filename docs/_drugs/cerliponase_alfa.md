---
layout: default
title: Cerliponase Alfa
parent: Kun modellprediksjon (L5)
nav_order: 82
evidence_level: L5
indication_count: 10
---

# Cerliponase Alfa
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

# Cerliponase alfa: Fra CLN2 disease til Scheie syndrom

## Oppsummering på én setning

> Cerliponase alfa er en rekombinant humant TPP1 enzymerstattningsterapi som opprinnelig ble utviklet for CLN2 disease (en form for nevroal seroid lipofuscinose / Batten sykdom).
> TxGNN-modellen spår at det kan være effektivt for **Scheie syndrom** (en undertype av MPS I),
> men denne prediksjonen støttes for tiden av **0 kliniske forsøk** og **0 publikasjoner**, og det underliggende mekanistiske grunnlaget virker svakt.

---

## Rask oversikt

| Element | Innhold |
|---------|---------|
| Original indikasjon | Ikke registrert i bevispaket (legemiddel ikke markedsført i Norge). Basert på legemidlets kjente mekanisme referert i ombruk-rasjonalen, brukes cerliponase alfa for **CLN2 disease** (TPP1-mangel) |
| Predikert ny indikasjon | Scheie syndrom |
| TxGNN prediktsjonsresultat | 99.98% |
| Bevisnivå | L5 (kun modellprediksjon, ingen støttestudier) |
| Status på norskmarkedet | ✗ Ikke markedsført |
| Antall godkjennelser | 0 |
| Anbefalt beslutning | Avvent |

---

## Hvorfor er denne prediksjonen rimelig?

For tiden er detaljerte mekanisme-data for cerliponase alfa ikke tilgjengelige (`original_moa` = datakløft). Basert på informasjon innebygd i ombruk-rasjonalen, er cerliponase alfa en **rekombinant humant TPP1 (tripeptidyl peptidase 1) enzymerstattningsterapi**, spesifikt indisert for å supplere TPP1-enzymet som mangler hos CLN2-pasienter.

Den topprangerte prediksjonen, Scheie syndrom, er en mild form av mukopolysakkaridose type I (MPS I), forårsaket av mangel på **alpha-L-iduronidase (IDUA)** — et helt annet enzym uten substratoverlapping med TPP1. Det samme mønsteret gjelder for de fleste av de øverste 10-kandidatene (Hurler syndrom, kolesterol ester lagringssykdom, Gaucher sykdom, Wolman sykdom): hver er en distinkt lisosomalt lagringssykdom drevet av et annet forårsaker-enzym (IDUA, LAL, glucocerebrosidase). De høye TxGNN-poengene gjenspeiler mest sannsynlig **kunnskapsgrafs-nærhet mellom lysosomal lagringssykdommer som en sykdomsklasse**, i stedet for en validert enzymatisk eller farmakologisk kryssreaktivitet.

Unntakelse verdt å merke seg: rang 8, "juvenil myoklonisk epilepsi, mottakelighet for," ble separat klassifisert av modellen som et **forskningsspørsmål** i stedet for "Avvent." Progredient myoklonisk epilepsi er et velkjent klinisk trekk ved CLN2 disease selv, så denne forbindelsen kan reflektere en genuin fenotype-nivå-link mellom TPP1/CLN2 biologi og epilepsi-nettverk — selv om den fortsatt mangler enhver klinisk forsøk eller litteraturvalidering og bør ikke tolkes som bevis for Scheie syndrom (den topprangerte kandidaten).

---

## Bevis fra kliniske forsøk

For tiden er det ingen registrerte relaterte kliniske forsøk.

---

## Litteraturbevis

For tiden er ingen relatert litteratur tilgjengelig.

---

## Informasjon om norskmarkedet

Ingen godkjennelser for cerliponase alfa på det norske markedet er for tiden registrert (`market_status`: ikke markedsført / Ikke markedsført; `total_licenses`: 0).

---

## Sikkerhetshensyn

Vennligst se pakningsvedlegget for sikkerhetsinformasjon. (Viktige advarsler, kontraindikasjoner og data om legemiddel-legemiddel-interaksjon er alle flagget som datakløfter i bevispaket; TFDA-merkeavisingshenting er oppført som en **blokkerende** datakløft — DG001.)

---

## Konklusjon og neste trinn

**Beslutning: Avvent**

**Begrunnelse:**
TxGNN-poenget er høyt, men det er null klinisk forsøk eller litteraturstøtte for den topprangerte kandidaten (Scheie syndrom), og den mekanistiske linken er svak — Scheie syndrom og CLN2 disease drives av helt ulike enzymer (IDUA kontra TPP1) uten kjent substratoverlapping. Dette mønsteret av grafnærhet-uten-mekanisme gjentar seg på tvers av 9 av de 10 beste kandidatene, noe som indikerer at prediksjonen reflekterer sykdomsklasse-clustering i stedet for en validert biologisk hypotese.

**For å fortsette, følgende er nødvendig:**
- TFDA merkeavarsler og kontraindikasjoner (DG001, blokkering) — påkrevd før noen S1 sikkerhetspre-vurdering kan begynne
- Verifisert mekanisme-data fra DrugBank (DG002, høy prioritet) — nødvendig for å riktig vurdere mekanistisk plausibilitet
- Hvis du fortsetter, prioriter rang 8 "juvenil myoklonisk epilepsi" signal som en forskningshypotese (fenotype-nivå-link til CLN2 disease) i stedet for den topprangerte Scheie syndrom-kandidaten, som for tiden ikke har mekanistisk eller empirisk støtte

## Ansvarsfraskrivelse

Dette innholdet er kun til forskningsformål og utgjør ikke medisinsk rådgivning.
Klinisk validering kreves før enhver klinisk anvendelse.

---

