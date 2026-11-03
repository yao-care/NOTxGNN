---
layout: default
title: Datakilder
nav_order: 93
permalink: /sources/
description: "Datakildene bak NOTxGNN: EMAs Medicines report (sentralt godkjente legemidler i EU), TxGNN, ClinicalTrials.gov, PubMed og DrugBank."
---

# Datakilder

<div class="key-takeaway">
Hver konklusjon kan spores tilbake til en offentlig datakilde — ingenting er en svart boks.
</div>

---

## Oversikt over kilder

<table class="comparison-table">
<thead>
<tr><th>Type</th><th>Kilde</th><th>Brukes til</th></tr>
</thead>
<tbody>
<tr><td>Registreringsdata</td><td><a href="https://www.ema.europa.eu/en/documents/report/medicines-output-medicines-report_en.xlsx">EMA Medicines report</a> (Det europeiske legemiddelkontoret, EMA)</td><td>Legemidler med sentral markedsføringstillatelse i EU (gyldig i alle EU/EØS-land, også Norge): virkestoffer og status for markedsføringstillatelsen</td></tr>
<tr><td>Prediksjonsmodell</td><td><a href="https://zitniklab.hms.harvard.edu/projects/TxGNN/">TxGNN</a></td><td>Prediksjon av sammenhenger mellom legemiddel og sykdom</td></tr>
<tr><td>Kliniske studier</td><td><a href="https://clinicaltrials.gov/">ClinicalTrials.gov</a></td><td>Evidensgradering (NCT)</td></tr>
<tr><td>Litteratur</td><td><a href="https://pubmed.ncbi.nlm.nih.gov/">PubMed</a></td><td>Evidensgradering (PMID)</td></tr>
<tr><td>Legemiddelinformasjon</td><td><a href="https://go.drugbank.com/">DrugBank</a></td><td>Kobling av virkestoffer og data om målmolekyler</td></tr>
<tr><td>Interaksjoner</td><td><a href="https://ddinter2.scbdd.com/">DDInter</a></td><td>Data om interaksjoner mellom legemidler</td></tr>
</tbody>
</table>

Nettstedet bruker ikke DMPs nasjonale legemiddeldata (FEST), så legemidler som bare har nasjonal
markedsføringstillatelse, er ikke med.

---

## Lisensiering

Hver kilde har sin egen lisens — kontroller den før du siterer:

- **TxGNN**: akademisk bruk; siter Huang et al. (2024)
- **ClinicalTrials.gov / PubMed**: offentlige data fra US NIH
- **DrugBank**: ikke-kommersiell bruk underlagt lisensvilkårene
- **EMA Medicines report**: offentlig fil fra Det europeiske legemiddelkontoret som kan lastes ned uten registrering; følg EMAs bruksvilkår

---

## Oppdateringsfrekvens

| Data | Frekvens |
|------|-----------|
| Status for markedsføringstillatelse | Oppdateres automatisk hver uke (mandager) fra EMAs fil |
| Evidens fra studier / litteratur | Samles inn på nytt med jevne mellomrom |
| Interaksjonsdata | Gjennomgås kvartalsvis |

---

## Akademisk sitering

> Huang, K., et al. (2024). A foundation model for clinician-centered drug repurposing. *Nature Medicine*.
> [DOI: 10.1038/s41591-024-03233-x](https://doi.org/10.1038/s41591-024-03233-x)

---

## Om utvikleren

Denne plattformen er utviklet og drives av **藥提醒科技有限公司** (yao.care). Opplysninger om selskapet,
bakgrunnen for TxGNN-modellen og alle nettstedene i produktlinjen finner du på siden <a href="{{ '/about/' | relative_url }}">Om</a>.

---

<div class="disclaimer">
<strong>Ansvarsfraskrivelse</strong><br>
Denne rapporten er kun ment som referanse for akademisk forskning og <strong>utgjør ikke medisinske råd</strong>. Følg alltid legens anvisninger; juster aldri medisineringen på egen hånd. Enhver beslutning om legemiddelreposisjonering krever fullstendig klinisk validering og regulatorisk gjennomgang.
<br><br>
<small>Gjennomgått av: 藥提醒科技有限公司 (yao.care)</small>
</div>
