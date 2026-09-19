---
layout: default
title: Nilotinib
parent: Moderat evidens (L3-L4)
nav_order: 243
evidence_level: L4
indication_count: 1
---

# Nilotinib
{: .fs-9 }

Evidensnivå: **L4** | Predikerte indikasjoner: **1** stk.
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

# Nilotinib: Fra kronisk myeloid leukemi til dermatofibrosarkom protuberans

## Oppsummering i en setning

Nilotinib er en andregennerasjons tyrosinkinasehemmer opprinnelig utviklet for Philadelphia-kromosom-positiv kronisk myeloid leukemi (Ph+ CML). TxGNN-modellen predikerer at det kan være effektivt for **dermatofibrosarkom protuberans (DFSP)**, men denne retningen støttes for øyeblikket av bare **0 kliniske studier** og **1 publikasjon**, noe som betyr at evidensgrunnlaget er mekanistisk snarere enn klinisk på dette stadiet.

## Rask oversikt

| Element | Innhold |
|---------|---------|
| Opprinnelig indikasjon | Kronisk myeloid leukemi (Ph+ CML)† |
| Predikert ny indikasjon | Dermatofibrosarkom protuberans |
| TxGNN-prediksjonspoeng | 99.31% |
| Evidensnivå | L4 |
| Markedsstatus i Norge | ✗ Ikke på markedet |
| Antall godkjennelser | 0 |
| Anbefalt beslutning | Avvent |

† Ikke tilstede i `original_indications`/`original_moa`-feltene i evidenspakken (flagget som datakløft, DG002). Dette er basert på generelt kjent informasjon om nilotinib snarere enn på det leverte evidensmaterialet.

## Hvorfor er denne prediksjonen rimelig?

For øyeblikket er detaljerte mekanisme-av-virkning-data ikke tilgjengelig i evidenspakken (datakløft DG002). Basert på generelt kjent informasjon er nilotinib en andregennerasjons BCR-ABL-tyrosinkinasehemmer (TKI) hvis effektivitet ved Ph+-kronisk myeloid leukemi er veletablert; den har også anerkjent off-target-inhibitorisk aktivitet mot PDGFR-α/β og KIT.

Dermatofibrosarkom protuberans (DFSP) er et bløtvevssarkom som karakteristisk drives av en COL1A1-PDGFB-genfusjon, som forårsaker konstitutiv aktivering av PDGFR-β-signalveien. Imatinib, en førstegennerasjons TKI i samme farmakologiske klasse som nilotinib, er allerede en etablert behandling for irresektabelt eller metastatisk DFSP nettopp på grunn av sin anti-PDGFR-aktivitet. Dette skaper en plausibel mekanistisk forbindelse mellom nilotinibs kjente målprofil og DFSP-biologi.

Det eneste hentede litteraturpunktet (PMID 29408302) gjennomgår den bredere rollen til småmolekyl PDGFR-inhibitorer — som en klasse — ved neoplastisk sykdom, noe som er konsistent med denne begrunnelsen, men gir ikke nilotinib-spesifikk eller DFSP-spesifikk klinisk resultatdata. Prediksjonen bør derfor betraktes som mekanistisk plausibel, men ikke ennå klinisk validert.

## Klinisk prøvebevis

Ingen relaterte kliniske studier er for øyeblikket registrert

## Litteraturbevis

| PMID | År | Type | Tidsskrift | Viktige funn |
|------|-----|------|---------|---------|
| [29408302](https://pubmed.ncbi.nlm.nih.gov/29408302/) | 2018 | Oversikt | Pharmacological Research | Gjennomgår rollen til småmolekyl PDGFR-inhibitorer (en klasse som inkluderer nilotinib) i behandling av neoplastiske lidelser; støtter en mekanistisk, men ikke DFSP-spesifikk, begrunnelse for PDGFR-drevne tumorer |

## Markedsinformasjon for Norge

Nilotinib er for øyeblikket ikke på markedet i Norge — ingen markedsføringssamtykker er registrert i evidenspakken.

## Cytotoksisitet

Nilotinib er et antineoplastisk middel (opprinnelig indikasjon er en hematologisk ondartelse, CML), så denne delen gjelder.

| Element | Innhold |
|---------|---------|
| Cytotoksisitetsklassifisering | Målrettet terapi (BCR-ABL/PDGFR/KIT-tyrosinkinasehemmer) |
| Risiko for myelosuppresjon | Se advarsler og forsiktighetsregler i pakningsvedlegget |
| Emetogenitetsklassifisering | Se advarsler og forsiktighetsregler i pakningsvedlegget |
| Overvåkingselementer | Se advarsler og forsiktighetsregler i pakningsvedlegget |
| Håndteringsbeskyttelse | Se advarsler og forsiktighetsregler i pakningsvedlegget |

## Sikkerhetshensyn

Se pakningsvedlegget for sikkerhetsinformasjon.

## Konklusjon og neste trinn

**Beslutning: Avvent**

**Begrunnelse:**
- TxGNN-poengsum er høyt, men det underliggende evidensgrunnlaget er begrenset til en enkelt mekanisme-klassegjennomgang med ingen DFSP-spesifikk eller nilotinib-spesifikk klinisk data, og null registrerte kliniske studier — noe som plasserer dette på Evidensnivå L4 (kun mekanisme).
- Kritisk sikkerhetsinformasjon (TFDA/produktetikett-advarsler og kontraindikasjoner) er merket som en **blokkerende** datakløft (DG001), som per definisjon hindrer denne kandidaten fra å gå inn i S1-stadiet for sikkerhetsprelimær evaluering.

**For å fortsette, kreves følgende:**
- TFDA-pakningsvedlegg-data (advarsler, kontraindikasjoner) — for øyeblikket blokkerende, må løses først
- Bekreftet mekanisme-av-virkning (MOA) detalj fra DrugBank (datakløft DG002)
- Sykdomsspesifikk bevis for nilotinib ved DFSP, særlig ved imatinib-resistente eller PDGFB-omgjorte tilfeller
- Stoff-stoff-interaksjon (DDI) profil, for øyeblikket uløst (`not_found`)
- Bekrefting av norsk markedsførings-/importvei, gitt at stoffet for øyeblikket ikke er på markedet

## Ansvarsfraskrivelse

Dette innholdet er kun til forskningsformål og utgjør ikke medisinsk rådgivning.
Klinisk validering kreves før enhver klinisk anvendelse.

---

