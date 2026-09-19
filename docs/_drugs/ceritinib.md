---
layout: default
title: Ceritinib
parent: Kun modellprediksjon (L5)
nav_order: 81
evidence_level: L5
indication_count: 10
---

# Ceritinib
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

# Ceritinib: Fra ALK-positiv NSCLC til gingival fibromatose

## En-setnings-sammenfatting

> Ceritinib er en andregrenerasjons ALK/ROS1 tyrosinkinasehemmer opprinnelig utviklet for ALK-positiv ikke-småcellet lungekreft (NSCLC).
> TxGNN-modellen forutsier at det kan være effektivt for **gingival fibromatose**,
> men denne kandidaten har for øyeblikket **0 kliniske forsøk** og **0 publikasjoner** som støtter det — det er en uverifisert modellhypotese, og modellens egen begrunnelse flagger den mekanistiske forbindelsen som svak.

---

## Rask oversikt

| Punkt | Innhold |
|------|--------|
| Opprinnelig indikasjon | ALK-positiv ikke-småcellet lungekreft (NSCLC) — utledet fra litteraturkontekst; ikke registrert som strukturerte data i dette bevisematerialet |
| Forutsagt ny indikasjon | Gingival fibromatose |
| TxGNN-prediksjonspoengsum | 99.86% |
| Bevisnivå | L5 (kun modellprediksjon, ingen støttende studier) |
| Markedsstatus Norge | ✗ Ikke markedsført |
| Antall autorisasjoner | 0 |
| Anbefalt beslutning | **Avvent** |

---

## Hvorfor er denne prediksjonen rimelig?

Detaljerte data om virkningsmekanisme er ikke tilgjengelige for ceritinib i dette bevisematerialet (flagget som et høyt-alvor datakløft, DG002). Basert på modellens egen genererte begrunnelse, er ceritinib kjent som en ALK/ROS1 tyrosinkinasehemmer hvis effektivitet i ALK-positiv ikke-småcellet lungekreft er godt etablert.

Gingival fibromatose er imidlertid en godartad fibrøs overvekstbetingelse drevet av SOS1/REST-mutasjoner eller ciklosporin-assosiert fibroblastproliferasjon. Den har ingen etablert forbindelse til ALK-signalering. Modellens egen begrunnelse slår eksplisitt fast at den høye poengsummen sannsynligvis gjenspeiler semantisk nærhet i innebygningsrommet (delt «tumor/proliferasjons»-språk) snarere enn en genuine delt biologisk mekanisme. Ingen klinisk forsøks- eller litteraturbevis eksisterer for dette spesifikke paret, så denne prediksjonen bør behandles som en uverifisert hypotese snarere enn et handlingsrettet omdisponeringsignal.

**En merknad om det bredere kandidatsettet:** blant de 10 TxGNN-forutsagte indikasjonene som er gitt for ceritinib, bærer en (rangering 5, «lungegodartet neoplasme») uvanlig sterk bevis — 1 fullført fase 3 RCT (ASCEND-4) og 20 publikasjoner. Ved inspeksjon er imidlertid alle disse bevisene for ALK-omordnet **malignt** NSCLC, som er ceritinibs *allerede-godkjente* indikasjon, ikke en godartet neoplasme. Dette indikerer en sykdomsetikett-kartleggingsfeil i den underliggende kunnskapsgrafen snarere enn et genuine nytt-indikasjons-signal, og bør rapporteres tilbake til pipeline/datateamet som et datakvalitets-problem snarere enn fremmet som en omdisponeringskandidat.

---

## Klinisk forsøksbevis

For øyeblikket er det ingen relaterte kliniske forsøk registrert.

---

## Litteraturbevis

For øyeblikket er det ingen relatert litteratur tilgjengelig.

---

## Markedsinformasjon Norge

Ceritinib har for øyeblikket ingen markedsføringsautoralisasjon i Norge (`market_status`: Not Marketed, 0 lisenser på fil). Ingen produkt-/doseringsform-data er tilgjengelig for dette bevisematerialet.

---

## Cytotoksisitet

Ceritinib er en antineoplastisk agens (ALK/ROS1 tyrosinkinasehemmer brukt i onkologi). DrugBank-nivå-toksisitetsdata ble ikke levert i dette bevisematerialet; oppføringene nedenfor er avledet fra litteratur knyttet til ceritinib andre steder i denne pakken, sitert for transparens.

| Punkt | Innhold |
|------|--------|
| Cytotoksisitetsklassifisering | Målrettet terapi (små-molekyl ALK/ROS1 tyrosinkinasehemmer) |
| Myelosuppresjonrisiko | Lav — sikkerhetslitteratur om ALK-TKIer (PMID [37597303](https://pubmed.ncbi.nlm.nih.gov/37597303/), [34864500](https://pubmed.ncbi.nlm.nih.gov/34864500/)) understreker ikke-hematologiske toksisiteter (GI, hepatisk, kardial) snarere enn myelosuppresjon |
| Emetogenisitetsklassifisering | Moderat til høy — GI-toksisitet (kvalme, oppkastning, diarré) er en vel-dokumentert, doseavhengig toksisitet av ceritinib (PMID [35344649](https://pubmed.ncbi.nlm.nih.gov/35344649/), ASCEND-8) |
| Overvåkingselementer | Leverenzymer; ECG/QTc-intervall (PMID [29413968](https://pubmed.ncbi.nlm.nih.gov/29413968/), [26008987](https://pubmed.ncbi.nlm.nih.gov/26008987/)); CBC; GI-symptomer; tromboembolismerisiko (PMID [39349372](https://pubmed.ncbi.nlm.nih.gov/39349372/)) |
| Sikker håndtering | Oral små-molekyl antineoplastisk agens — håndter i henhold til institusjonelle protokoller for håndtering av farlige/antineoplastiske medikamenter; ingen DrugBank-spesifikke håndteringsdata er tilgjengelig i dette bevisematerialet |

---

## Sikkerhetshensyn

Vennligst se pakningsvedlegget for sikkerhetsinformasjon.

---

## Konklusjon og neste trinn

**Beslutning: Avvent**

**Begrunnelse:**
Alle 10 TxGNN-forutsagte indikasjonene for ceritinib i dette bevisematerialet har en «Avvent»-anbefaling. Topprangert-kandidaten (gingival fibromatose) har null støttende klinisk eller litteraturbevis (L5) og en erkjent usannsynlig mekanistisk forbindelse. Kandidaten med det sterkeste beviset i settet (lungegodartet neoplasme, L1) er faktisk en sykdomsetikett-mismatch som peker tilbake til ceritinibs eksisterende godkjente indikasjon (ALK+ NSCLC), ikke en genuine ny indikasjon.

**For å fortsette er følgende nødvendig:**
- TFDA/regulatorisk-klasse pakningsvedlegg advarsler og kontraindikasjoner (for øyeblikket et blokkerende datakløft, DG001)
- En bekreftet virkningsmekanisme-post fra DrugBank (for øyeblikket et høyt-alvor datakløft, DG002)
- Rettelse av sykdomsetikett-kartleggingen i TxGNN-pipelinen for «lungegodartet neoplasme» og «lunge-kjønnscelle-tumor»-kandidater, som dokumenterer ceritinibs eksisterende indikasjon snarere enn en ny
- Hvis gingival fibromatose skal forfølges videre, dediserte prekliniske/mekanistiske studier som etablerer biologisk plausibilitet, siden ingen for øyeblikket eksisterer

## Ansvarsfraskrivelse

Dette innholdet er kun til forskningsformål og utgjør ikke medisinsk rådgivning.
Klinisk validering kreves før enhver klinisk anvendelse.

---

