---
layout: default
title: Gimeracil
parent: Kun modellprediksjon (L5)
nav_order: 160
evidence_level: L5
indication_count: 10
---

# Gimeracil
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

# Gimeracil: Fra DPD-hemming komponent i S-1 til kolonom

## Sammendrag på en setning

> Gimeracil har ingen godkjent selvstendig indikasjon — det er DPD (dihydropyrimidin dehydrogenase)-hemmer komponenten i S-1 kombinasjonen (tegafur/gimeracil/oteracil), der det virker ved å blokkere hurtig nedbrytning av 5-FU i stedet for å utøve direkte cytotoksisitet selv.
> TxGNN-modellen predikerer at S-1-regimet som inneholder gimeracil kan være effektivt for **kolonom**,
> med **8 kliniske forsøk** (inkludert 2 fullførte fase 3 RCT-er) og **15 publikasjoner** som for tiden støtter denne retningen.

---

## Rask oversikt

| Element | Innhold |
|------|------|
| Original indikasjon | Ingen selvstendig godkjent — gimeracil er en farmakokinetisk forsterker i S-1 kombinasjonen (tegafur/gimeracil/oteracil), ikke en selvstendig antineoplastisk agent |
| Forutsagt ny indikasjon | Kolonom |
| TxGNN prediksjonspoeng | 99.88% |
| Bevisnivå | L1 (2 fullførte fase 3 RCT-er) |
| Markedsstatus Norge | ✗ Ikke markedsført |
| Antall godkjennelser | 0 |
| Anbefalt beslutning | Fortsett med sikringsmekanismer |

---

## Hvorfor er denne prediksjonen rimelig?

Detaljerte mekanisme-for-handling-data fra DrugBank for gimeracil er for øyeblikket ikke tilgjengelige (Datagap). Basert på kjent farmakologi er gimeracil en kompetitiv DPD-hemmer og er ikke cytotoksisk på egen hånd. Innenfor S-1 kombinasjonen blokkerer det DPD-mediert nedbrytning av 5-FU (generert fra tegafur), og forlenger og stabiliserer dermed systemisk 5-FU eksponering. Dette er en farmakokinetisk forsterker rolle, ikke en uavhengig antitumørmekanisme.

Fordi 5-FU-basert kjemoterapi er en hjørnesten i behandling av kolorektalkreft, og S-1 allerede har mottatt regulatorisk godkjennelse for kolorektalkreft i Japan og andre asiatiske markeder, er den mekanistiske begrunnelsen for å utvide S-1 (og dermed gimeracil som dets muliggjørende komponent) til kolonom godt etablert i onkologisk praksis.

**Viktig forbehold**: Dette "omformål"-signalet gjenspeiler faktisk en eksisterende kombinasjonsproduktbruk snarere enn en virkelig ny mekanistisk utvidelse. All støttende klinisk bevis kommer fra S-1 tre-legemiddel kombinasjonen — ingen isolerer gimeracils uavhengige bidrag. Enhver regulatorisk eller klinisk beslutning bør behandle dette som bevis for S-1 regimet, ikke for gimeracil monoterapi.

---

## Klinisk forsøksbevis

| Forsøknummer | Fase | Status | Innrullering | Viktige funn |
|---------|------|------|------|---------|
| [NCT00660894](https://clinicaltrials.gov/study/NCT00660894) | Fase 3 | Fullført | 1535 | S-1 versus UFT+leukvorin som adjuvant terapi for stadium III tykktarmskreft; største fullførte head-to-head forsøk, undersøkte også genekspresjon prediktive faktorer |
| [NCT01918852](https://clinicaltrials.gov/study/NCT01918852) | Fase 3 | Fullført | 161 | SALTO-forsøk: S-1 versus kapesitabin som førstlinjers behandling for metastatisk kolorektalkreft; sikkerhetsevaluering av orale fluorpyrimidiner |
| [NCT03448549](https://clinicaltrials.gov/study/NCT03448549) | Fase 3 | Ukjent | 1191 | SOX (S-1+oksaliplatinum) versus XELOX som adjuvant kjemoterapi for stadium III kolorektalkreft; stort utvalg men resultatstatus ikke rapportert |
| [NCT02618356](https://clinicaltrials.gov/study/NCT02618356) | Fase 2 | Ukjent | 82 | Raltitreksed + S-1 ved metastatisk kolorektalkreft etter svikt av standardkjemoterapi; primært endepunkt PFS |
| [NCT00524706](https://clinicaltrials.gov/study/NCT00524706) | Fase 1/2 | Ukjent | 42 | S-1 + oral leukvorin + oksaliplatinum (SOL-regime) ved ubehandlet metastatisk kolorektalkreft |
| [NCT00974389](https://clinicaltrials.gov/study/NCT00974389) | Fase 2 | Ukjent | 40 | S-1 + bevacizumab ved uopererbar/gjentakende kolorektalkreft etter svikt av irinotekan/oksaliplatinum |
| [NCT02216149](https://clinicaltrials.gov/study/NCT02216149) | Fase 2 | Avsluttet | 20 | Kardiak sikkerhet sammenligning (koronar arterie blodstrøm) av S-1/kapesitabin + oksaliplatinum ved metastatisk GI adenokarsinom |
| [NCT06255379](https://clinicaltrials.gov/study/NCT06255379) | Fase 2 | Rekruttering ikke startet | 52 | Furkvintiinib + S-1 som tredjeljers behandling for avansert metastatisk kolorektalkreft |

---

## Litteraturbevis

| PMID | År | Type | Tidsskrift | Viktige funn |
|------|-----|------|------|---------|
| [41724114](https://pubmed.ncbi.nlm.nih.gov/41724114/) | 2026 | Populasjonsbasert kohorte | Eur J Cancer | Populasjonsbasert studie: S-1 gjennomførbar og sikker etter kapesitabin-indusert HFS/kardiotoksisitet ved adjuvant tykktarmskreft behandling |
| [21875473](https://pubmed.ncbi.nlm.nih.gov/21875473/) | 2011 | Kohorte | Zhonghua Zhong Liu Za Zhi | Effektivitet og bivirkninger av oksaliplatinum + S-1 kombinasjon ved postoperativ kolorektalkreft |
| [21084813](https://pubmed.ncbi.nlm.nih.gov/21084813/) | 2010 | Kohorte | Gan To Kagaku Ryoho | Risikofaktorer for grad 3–4 hematologisk toksisitet med S-1 + irinotekan ved avansert/gjentakende tykktarmskreft (16.1% insidens) |
| [20811661](https://pubmed.ncbi.nlm.nih.gov/20811661/) | 2010 | Preklinisk/xenograft | Oncology Reports | Irinotekan overkommet 5-FU resistens via timidylat syntase nedregulering i S-1-behandlet tykktarmskreft xenografts |
| [18630468](https://pubmed.ncbi.nlm.nih.gov/18630468/) | 2008 | Pasientrapport | Anticancer Research | Komplett respons oppnådd og opprettholdt med S-1 + CPT-11 ved tykktarmskreft hepatiske metastaser |
| [29394831](https://pubmed.ncbi.nlm.nih.gov/29394831/) | 2017 | Pasientrapport | Gan To Kagaku Ryoho | SOX (S-1+oksaliplatinum) + panitumumab nedstaging muliggjørende to-etappe hepatektomi for irresektabel kolorektal levermetastase |
| [29483452](https://pubmed.ncbi.nlm.nih.gov/29483452/) | 2018 | Pasientrapport | Gan To Kagaku Ryoho | Kjemoterapistyring av tversgående tykktarmskreft med levermetastase og portalvene tumortrombose |
| [20841935](https://pubmed.ncbi.nlm.nih.gov/20841935/) | 2010 | Farmakokinetiskstudie | Gan To Kagaku Ryoho | S-1 farmakokenetikk i en mus peritonealt metastasemodell avledet fra tykktarmskreft |
| [35444144](https://pubmed.ncbi.nlm.nih.gov/35444144/) | 2022 | Pasientrapport | Gan To Kagaku Ryoho | Laparoskopisk reseksjon av peritonealt gjentakelse etter kolorektal kreftreseksjon med S-1-inneholdende adjuvant terapi |
| [32936722](https://pubmed.ncbi.nlm.nih.gov/32936722/) | 2021 | Pasientrapport (toksisitet) | J Oncol Pharm Pract | Hypertriglyseridemi indusert av S-1 under kolorektal kreftbehandling — nytt toksisitetssignal |

---

## Markedsinformasjon Norge

Gimeracil (som del av S-1 kombinasjonen) er for øyeblikket **ikke markedsført i Norge**; ingen autorisasjonsoppgaver er tilgjengelige (0 lisenser på fil).

---

## Cytotoksisitet

Gimeracil selv er ikke-cytotoksisk (en DPD-hemmer), men administreres alltid som en integrert komponent av S-1 fluorpyrimidin kjemoterapiregimet. Det bør derfor håndteres under konvensjonelle cytotoksisk kjemoterapiprotokoller.

| Element | Innhold |
|------|------|
| Cytotoksisitetsklassifikasjon | Ikke-cytotoksisk PK-forsterker innenfor et konvensjonelt cytotoksisk regime (fluorpyrimidin klasse, S-1) |
| Myelosuppresjon risiko | Moderat — grad 3–4 hematologisk toksisitet rapportert hos ~16.1% av pasienter som mottok S-1 + irinotekan for tykktarmskreft (PMID 21084813) |
| Emetogenisitet klassifikasjon | Lav til moderat (i samsvar med orale fluorpyrimidin regimer) |
| Overvåkingselementer | CBC med differensial, lever- og nyrefunksjon, serum triglyserider (hypertriglyseridemi rapportert, PMID 32936722), hud/mukøs toksisitetsovervåking |
| Håndteringsvern | Standard forholdsregler for håndtering av cytotoksiske legemidler gjelder, ettersom gimeracil ko-administreres som del av S-1 cytotoksisk regime |

---

## Sikkerhetshensyn

Vennligst se pakningsvedlegget for sikkerhetsinformasjon. Legemiddelspesifikke advarsler, kontraindikasjoner og legemiddel-interaksjon data for gimeracil er for øyeblikket ikke tilgjengelige (flagget som et blokkeringsgap som venter på TFDA etikett anskaffelse).

---

## Konklusjon og neste trinn

**Beslutning: Fortsett med sikringsmekanismer**

**Begrunnelse:**
To fullførte fase 3 RCT-er (NCT00660894, n=1535; NCT01918852, n=161) støtter S-1 — kombinasjonen som inneholder gimeracil — ved kolorektal/tykktarmskreft, som gir L1 bevisstyrke. Imidlertid gjelder all bevis for S-1 kombinasjonsproduktet, ikke gimeracil alene, og produktnivå sikkerhetsetikett (advarsler/kontraindikasjoner) mangler fortsatt.

**For å fortsette, er følgende nødvendig:**
- TFDA/produsentprodukt etikett med advarsler og kontraindikasjoner (Blokkeringsgap, DG001)
- Bekreftet mekanisme-for-handling dokumentasjon fra DrugBank (Høy prioritering gap, DG002)
- Eksplisitt avklaring i enhver regulatorisk innlevering at effektivitetsbevis gjelder S-1 kombinasjonen, ikke gimeracil monoterapi
- Vurdering av Norges markedsadgang/autoriseringssti, ettersom produktet ikke er markedsført der for øyeblikket

*Notat: Ni tilleggspredikerte indikasjoner (rangeringer 2–10) ble gjennomgått men er ikke detaljert her — alle bortsett fra "kardiakreft" (L4, Forskningsspørsmål) bærer kun TxGNN prediksjonspoeng uten støttende forsøk eller litteratur (L5, Vente), inkludert flere biologisk usannsynlige kandidater (for eksempel godartede lesioner som lipom av kolon, kolon lymphangiom) som ikke bør forfølges.*

## Ansvarsfraskrivelse

Dette innholdet er kun til forskningsformål og utgjør ikke medisinsk rådgivning.
Klinisk validering kreves før enhver klinisk anvendelse.

---

