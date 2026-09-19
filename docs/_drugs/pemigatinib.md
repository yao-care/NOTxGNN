---
layout: default
title: Pemigatinib
parent: Kun modellprediksjon (L5)
nav_order: 274
evidence_level: L5
indication_count: 10
---

# Pemigatinib
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

# Pemigatinib: Fra FGFR-drevet onkologibruk til multippel endokrin neoplasi

## Oppsummering i én setning

Pemigatinib er referert til i denne bevissamlingen som en FGFR1-3 kinase-hemmer; dens opprinnelig godkjente indikasjon er ikke registrert i det aktuelle datasettet.
TxGNN-modellen predikerer at det kan være effektivt for **multippel endokrin neoplasi**,
men denne retningen er for øyeblikket støttet av **0 kliniske forsøk** og **0 publikasjoner**, og modellens egen begrunnelsestekst flagger den mekanistiske linken som svak og sannsynligvis en artefakt i kunnskapsgrafen.

---

## Rask oversikt

| Element | Innhold |
|---------|---------|
| Originalt indikasjonsområde | Ikke tilgjengelig i gjeldende bevissamling |
| Predikert nytt indikasjonsområde | Multippel endokrin neoplasi |
| TxGNN prediksjonspoeng | 99.71% |
| Bevisnivå | L5 |
| Status på norsk marked | ✗ Ikke markedsført |
| Antall godkjenninger | 0 |
| Anbefalt beslutning | Avvent |

---

## Hvorfor er denne prediksjonen rimelig?

For øyeblikket er detaljerte mekanisme-av-handling-data for pemigatinib ikke tilgjengelige i denne bevissamlingen. Basert på informasjon innebygd andre steder i samlingen (begrunnelsestekst for ombruk av andre kandidater), beskrives pemigatinib konsistent som en **FGFR1-3 kinase-hemmer**, brukt i en sammenheng som kan sammenlignes med andre FGFR-hemmere som infigratinib. Dette er konsistent med dens kjente legemiddelklasse, men er ikke uavhengig bekreftet av et strukturert MOA-felt her.

Forholdet mellom pemigatinibs (uregistrert) originale indikasjon og multippel endokrin neoplasi kan ikke etableres fra dataene som er gitt, siden ingen original indikasjon er oppført og ingen lisenser er på fil. Det som bevissamlingen faktisk inneholder, er modellens egen mekanistiske vurdering, som er ugunstig: MEN-syndrom drives primært av **MEN1 og RET**-mutasjoner, og har ingen etablert forbindelse til **FGFR1-3** signaleringsaksen som pemigatinib retter seg mot.

På grunn av dette misforholdet konkluderer pakkens egen begrunnelse at den høye TxGNN-poengene mest sannsynlig reflekterer en **indirekte kunnskapsograf-assosiasjon** — for eksempel delt nærhet til andre endokrine tumor-noder — heller enn en genuin farmakologisk mekanisme. Dette bør behandles som et lavtillitssignal kun for hypotesegenerering, ikke som en mekanistisk begrunnet ombrukskandidat.

---

## Klinisk forsøksbevis

For øyeblikket er det ingen relaterte kliniske forsøk registrert.

---

## Litteraturbevis

For øyeblikket er det ingen relatert litteratur tilgjengelig.

---

## Informasjon om norsk marked

Pemigatinib er for øyeblikket **ikke markedsført** i Norge (markedsstatus: Ikke markedsført) og ingen godkjennelsesopplysninger finnes i denne bevissamlingen (totalt lisenser: 0). Ingen produkttabell kan genereres på dette tidspunktet.

---

## Cytotoksisitet

Pemigatinib er referert til i denne bevissamlingen som en FGFR1-3 kinase-hemmer brukt i onkologikontekster (f.eks. diskusjon av FGFR-drevet resistens i HER2+ brystkreft, og sammenligning med andre FGFR-hemmere som er utforsket i FGFR3-drevet skjelettsykdom). På det grunnlaget behandles det her som en antineoplastisk, målrettet småmolekyl terapi, selv om denne klassifiseringen er sluttet heller enn bekreftet via et strukturert DrugBank-kategorifelt.

| Element | Innhold |
|---------|---------|
| Cytotoksisitetsklassifisering | Målrettet terapi (FGFR1-3 kinase-hemmer) |
| Myelosuppresjonrisiko | Se pakningsvedlegget for advarsler og forholdsregler |
| Emetogenisitetsklassifisering | Se pakningsvedlegget for advarsler og forholdsregler |
| Overvåkingspunkter | Se pakningsvedlegget for advarsler og forholdsregler |
| Håndteringsbeskyttelse | Se pakningsvedlegget for advarsler og forholdsregler |

---

## Sikkerhetshensyn

Se pakningsvedlegget for sikkerhetsinformasjon.

---

## Konklusjon og neste trinn

**Beslutning: Avvent**

**Begrunnelse:**
Den topprangerte prediksjonen (multippel endokrin neoplasi) har null støttende kliniske forsøk eller litteratur, og modellens egen mekanistiske begrunnelse uttaler eksplisitt at FGFR1-3-signaleringsaksen ikke har noen etablert forbindelse til MEN-patogenese — dette er et L5-signal basert kun på hypotese, med angitt risiko for å være kunnskapsograf-støy.

**For å fortsette er følgende nødvendig:**
- TFDA/regulatorisk merkedata (advarsler, kontraindikasjoner) — flagget som en *Blokkerende* datakløft (DG001)
- Bekreftet mekanisme-av-handling (MOA) fra DrugBank eller tilsvarende kilde — flagget som *Høy* alvorlighetsgrad datakløft (DG002)
- Bekreftelse av pemigatinibs faktisk opprinnelig godkjent indikasjon(er), for øyeblikket fraværende fra denne pakken
- Uavhengig mekanistisk eller preklinisk bevis som knytter FGFR-hemming til MEN før noen ytterligere evalueringsfase vurderes

## Ansvarsfraskrivelse

Dette innholdet er kun til forskningsformål og utgjør ikke medisinsk rådgivning.
Klinisk validering kreves før enhver klinisk anvendelse.

---

