---
layout: default
title: Pembrolizumab
parent: Kun modellprediksjon (L5)
nav_order: 272
evidence_level: L5
indication_count: 10
---

# Pembrolizumab
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

# Pembrolizumab: Fra PD-1-rettet onkologisk immunterapi (indikasjonstekst ikke levert) til gingivalt fibromatose

## Sammendrag på en setning

Pembrolizumab er et PD-1-blokkerende monoklonalt antistoff som brukes bredt innen onkologi (evidenspakken refererer NSCLC, melanom, MSI-H/dMMR-kreftformer og hepatocellulart karsinom i sitert litteratur, selv om det strukturerte `original_indications`-feltet er tomt).
TxGNN-modellens høyest rangerte prediksjon er **Gingivalt fibromatose**, men denne støttes av **0 kliniske forsøk** og **0 publikasjoner**, og legemidlets eget omforbrukingsgrunnlag angir at mekanismen ikke gjelder for denne benigne tilstanden.

## Raskt oversyn

| Element | Innhold |
|---------|---------|
| Originalindikasjon | Ikke spesifisert i evidenspakken (`original_indications` er tomt); litteraturkontekst indikerer bred PD-1-checkpoint-inhibitorbruk innen onkologi |
| Forutsagt ny indikasjon | Fibromatose, gingivalt |
| TxGNN-prediksjonspoengsum | 99.40% (rangering 6326 blant alle prediksjoner) |
| Bevisnivå | L5 |
| Norges markedsstatus | ✗ Ikke markedsført |
| Antall godkjennelser | 0 |
| Anbefalt beslutning | Avvent |

## Hvorfor er denne prediksjonen rimelig?

Detaljerte data om virkningsmekanisme er for tiden ikke tilgjengelige for dette legemidlet i evidenspakken (Datakløft DG002, høy alvorlighetsgrad). Basert på kjent farmakologi blokkerer pembrolizumab PD-1-reseptoren på T-celler, og desinhiberer således anti-tumorimmunsvar i immunogene, immunevasive maligniteter.

Gingivalt fibromatose er imidlertid en benign fibrøs vevsvekst – typisk arvelig eller legemiddelindusert (f.eks. av phenytoin, ciclosporin, kalciumkanalblokkere) – og er ikke en malignitet med immunevajons-fenotypt. Omforbrukingsgrunnlaget som leveres med denne prediksjonen angir eksplisitt at det er **ingen mekanistisk sammenheng** mellom PD-1-blokkade og gingivalt fibromatose, og ingen klinisk eller litteraturbevis støtter assosiasjonen.

Denne prediksjonen synes å være en nettverksbasert artefakt av TxGNN-modellen (en høy likhetsscore uten plausibelt biologisk grunnlag), snarere enn et ekte omforbrukingssignal. Derimot er andre lavere rangerte kandidater i denne samme serien – *lungerot-karsinom*, *lungekimcelletumor* og *lungetoppsneoplasme* – anatomiske/posisjonsbaserte undertyper av lungmalignitet der pembrolizumabs klassenivå-NSCLC-mekanisme i det minste teoretisk kan utvides, og disse ble scoret på beslutningsstadium S1 («Forskningsspørsmål») snarere enn S0 («Avvent»). Disse kan berettige separat evaluering foran den høyest rangerte kandidaten diskutert her.

## Bevis fra kliniske forsøk

Ingen relaterte kliniske forsøk er for tiden registrert

## Litteraturbevis

Ingen relatert litteratur er for tiden tilgjengelig

## Markedsinformasjon for Norge

Pembrolizumab er for tiden **ikke markedsført** i Norge ifølge denne evidenspakken (0 godkjennelser på registreringen; `market_status` = Ikke markedsført). Ingen produktlisenser er tilgjengelige å oppføre.

## Cytotoksisitet

*(Avsnitt inkludert: selv om det strukturerte `original_indications`-feltet er tomt, identifiserer den siterte litteraturen gjennom hele denne evidenspakken konsekvent pembrolizumab som et antineoplasmisk PD-1-immunolog checkpoint-inhibitor som brukes på tvers av flere krefttyper.)*

| Element | Innhold |
|---------|---------|
| Cytotoksisitetsklassifisering | Immunterapi (anti-PD-1-immunolog checkpoint-inhibitor) – ikke et konvensjonelt cytotoksisk middel |
| Risiko for myelosuppresjon | Lav – pembrolizumab virker ikke via direkte cytotoksisitet på benmargsprogenitorer; det dominerende toksisitetsmønsteret er immunrelaterte bivirkninger (irAEs) snarere enn klassisk myelosuppresjon |
| Emetogenisitetsklassifisering | Lav |
| Overvåkingselementer | Baseline og periodiske skjoldbruskkirtelsfunksjonstester (TSH/fritt T4), leverfunksjon, nyrefunksjon, kortisol/ACTH (for hypofysitt), hjertekrumpmuskelverdier hvis miokarditt mistenkes, og klinisk overvåking for irAEs (kolitt, pneumonitt, dermatologiske reaksjoner, myositt/myastenia gravis) |
| Håndteringsbeskyttelse | Som et monoklonalt antistoff biologisk middel krever pembrolizumab ikke sikkerhetsforsiktigheter for lukket-system-håndtering av farlige cytotoksiske legemidler som brukes for konvensjonell kjemoterapi; administrer ifølge institusjonell onkologi-infusjonsprotokoll og pakningsvedlegget |

## Sikkerhetshensyn

Se pakningsvedlegget for sikkerhetsinformasjon. (Viktige advarsler, kontraindikasjoner og DDI-data er alle registrert som datakløfter i denne evidenspakken – DG001 er flagget som **Blokkering**, noe som betyr at TFDA/etikett-nivå-advarsler og kontraindikasjoner må oppnås før denne kandidaten engang kan gå inn i S1-sikkerhetsevalueringsstadiet.)

## Konklusjon og neste trinn

**Beslutning: Avvent**

**Grunngivelse:**
Den høyest rangerte forutsa indikasjon (gingivalt fibromatose) har null klinisk forsøk eller litteraturstøtte, og det leverte mekanistiske grunnlag motsier direkte biologisk plausibilitet – en benign fibrøs vevsvekst har ingen etablert sammenheng til PD-1-mediert tumorimmunevasjon. Separat hindrer en datakløft med blokkerings-alvorlighet (manglende TFDA-etikett advarsler/kontraindikasjoner) denne kandidaten fra formelt å gå inn i S1-sikkerhetsevalueringsstadiet uavhengig av indikasjonsnivå-bevis.

**For å fortsette kreves følgende:**
- Løs DG001 (Blokkering): oppnå og analyser den offisielle TFDA/norske etiketten for advarsler og kontraindikasjoner
- Løs DG002: oppnå bekreftet virkningsmekanisme-data fra DrugBank
- Gjenveie prioritering av kandidatene med høyere plausibilitet i denne samme prediksjonsserien (lungerot-karsinom, lungekimcelletumor, lungetoppsneoplasme – for tiden på beslutningsstadium S1) snarere enn den høyeste TxGNN-score-kandidaten, som mangler biologisk plausibilitet
- Hvis gingivalt fibromatose skal forfølges videre til tross for det ovennevnte, ville dedikert preklinisk/mekanistisk forskning være nødvendig, da ingen klinisk eller litteraturbevis for tiden eksisterer

## Ansvarsfraskrivelse

Dette innholdet er kun til forskningsformål og utgjør ikke medisinsk rådgivning.
Klinisk validering kreves før enhver klinisk anvendelse.

---

