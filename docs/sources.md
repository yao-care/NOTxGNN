---
layout: default
title: Datakilder
nav_order: 93
permalink: /sources/
description: "Datakildene bak NOTxGNN: registreringsdata fra DMP, TxGNN, ClinicalTrials.gov, PubMed og DrugBank."
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
<tr><td>Registreringsdata</td><td><a href="https://www.dmp.no/">DMP</a></td><td>Liste over godkjente legemidler og virkestoffer i Norge</td></tr>
<tr><td>Prediksjonsmodell</td><td><a href="https://zitniklab.hms.harvard.edu/projects/TxGNN/">TxGNN</a></td><td>Prediksjon av sammenhenger mellom legemiddel og sykdom</td></tr>
<tr><td>Kliniske studier</td><td><a href="https://clinicaltrials.gov/">ClinicalTrials.gov</a></td><td>Evidensgradering (NCT)</td></tr>
<tr><td>Litteratur</td><td><a href="https://pubmed.ncbi.nlm.nih.gov/">PubMed</a></td><td>Evidensgradering (PMID)</td></tr>
<tr><td>Legemiddelinformasjon</td><td><a href="https://go.drugbank.com/">DrugBank</a></td><td>Kobling av virkestoffer og data om målmolekyler</td></tr>
<tr><td>Interaksjoner</td><td><a href="https://ddinter2.scbdd.com/">DDInter</a></td><td>Data om interaksjoner mellom legemidler</td></tr>
</tbody>
</table>

---

## Lisensiering

Hver kilde har sin egen lisens — kontroller den før du siterer:

- **TxGNN**: akademisk bruk; siter Huang et al. (2023)
- **ClinicalTrials.gov / PubMed**: offentlige data fra US NIH
- **DrugBank**: ikke-kommersiell bruk underlagt lisensvilkårene
- **DMP**: underlagt vilkårene for åpne data hos legemiddelmyndigheten i Norge

---

## Oppdateringsfrekvens

| Data | Frekvens |
|------|-----------|
| Registreringsdata | Etter hvert som legemiddelmyndigheten publiserer |
| Evidens fra studier / litteratur | Samles inn på nytt med jevne mellomrom |
| Interaksjonsdata | Gjennomgås kvartalsvis |

---

## Akademisk sitering

> Huang, K., et al. (2023). A foundation model for clinician-centered drug repurposing. *Nature Medicine*.
> [DOI: 10.1038/s41591-023-02233-x](https://doi.org/10.1038/s41591-023-02233-x)

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
