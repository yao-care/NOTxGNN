---
layout: default
title: Andexanet Alfa
parent: Kun modellprediksjon (L5)
nav_order: 31
evidence_level: L5
indication_count: 4
---

# Andexanet Alfa
{: .fs-9 }

Evidensnivå: **L5** | Predikerte indikasjoner: **4** stk.
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

# Andexanet Alfa: Fra Factor Xa-hemmer-reversering til Glanzmanns trombasteni

## Oppsummering på én setning

> Andexanet alfa er et modifisert rekombinant factor Xa-lokkprotein som brukes til å reversere antikoagulasjon forårsaket av factor Xa-hemmere (apixaban/rivaroxaban) ved livsfarlig blødning.
> TxGNN-modellen predikerer at det kan være effektivt for **Glanzmanns trombasteni**,
> men **ingen kliniske studier og ingen støttende litteratur** støtter denne retningen for tiden — skåren ser ut til å være drevet av grafinnebygningsnærhet ("blødningssykdom" semantisk gruppering) snarere enn biologisk plausibilitet.

## Hurtig oversikt

| Element | Innhold |
|---------|---------|
| Originalindikasjon | Reversering av antikoagulanteffekt av factor Xa-hemmere (apixaban/rivaroxaban) hos pasienter med livsfarlig eller ukontrollert blødning *(utledet fra mekanistisk beskrivelse; ikke ennå lokalt autorisert)* |
| Predikert ny indikasjon | Glanzmanns trombasteni |
| TxGNN-prediksjonspoeng | 99.77% |
| Bevisnivå | L5 |
| Markedsstatus (Taiwan) | ✗ Ikke markedsført (Ikke markedsført) |
| Antall autorisasjoner | 0 |
| Anbefalt beslutning | **Avvent** |

## Hvorfor er denne prediksjonen rimelig?

For tiden er en strukturert virkningsmekanisme (MOA) -post ikke tilgjengelig (flagget som et høyt alvorlighetsgrad datakløft, DG002). Gjenbruksrasjonalet knyttet til hver prediksjon beskriver imidlertid konsekvent andexanet alfa som et **modifisert rekombinant factor Xa-lokkprotein**: det bindes til og nøytraliserer direkte factor Xa-hemmere (apixaban, rivaroxaban) og hemmer også vevfaktorbane-inhibitor (TFPI), og gjenoppretter trombin-generering for å fremme hemostase.

Glanzmanns trombasteni derimot er forårsaket av en defekt i **GPIIb/IIIa-reseptoren**, som hemmer plateletaggregasjon på reseptornivået — en mekanisme helt ovenfor og urelatert til factor Xa/TFPI-banen som andexanet alfa virker på. Bevispaketets egen mekanistiske vurdering angir eksplisitt at det er **ingen biologisk bane** ved hvilken gjenopprettelse av trombin-generering ville korrigere en defekt i plateletaggregasjonsreseptor, og konkluderer at den høye TxGNN-skåren mest sannsynlig gjenspeiler grafinnebygningsnærhet mellom "blødningssykdommer" som en semantisk klasse, snarere enn et genuint farmakologisk forhold.

Dette mønsteret gjentar seg på tvers av de andre topprangerte kandidatene i denne bevispacken (primær plateletutsendelsesforstyrrelse, pseudo-von Willebrands sykdom og hemofili) — hver innebærer platelet-nivå- eller koagulasjonsfaktormangel-mekanismer som er adskilte fra factor Xa/TFPI-aksen som andexanet alfa målretter mot, og ingen har støttende mekanistisk begrunnelse for en terapeutisk (snarere enn tilfeldig/interfererende) rolle.

## Bevis fra kliniske studier

For tiden er det ingen registrerte relaterte kliniske studier.

## Litteraturbevis

For tiden er det ingen tilgjengelig relatert litteratur.

*(Merk: for den fjerde rangerte kandidaten, hemofili, eksisterer 11 publikasjoner — men ved gjennomgang handlet disse hovedsakelig om (a) andexanets kjente interferens med factor VIII/IX laboratorieanlyser, og (b) generelle gjennomganger av DOAC-reversalstrategier. Ingen beskriver andexanet alfa som en terapeutisk agent for hemofili selv, så denne litteraturen utgjør ikke støttende bevis for gjenbruk.)*

## Taiwans markedsinformasjon

Ingen markedsføringsautorisasjonsposter eksisterer for tiden for andexanet alfa i Taiwan (Ikke markedsført, 0 lisenser).

## Sikkerhetsaspekter

Vennligst se pakningsvedlegget for sikkerhetsinformasjon.

> ⚠️ Merk: TFDA-merking / advarsler og kontraindikasjonerdata er merket som en **blokkering** datakløft (DG001) — dette må løses før noen fase 1 (S1) sikkerhetsforhåndsvurdering kan gjennomføres for noen indikasjon som involverer dette legemidlet.

## Konklusjon og neste skritt

**Beslutning: Avvent**

**Begrunnelse:**
Den forutsagte indikasjonen (Glanzmanns trombasteni) har ingen kliniske studier, ingen litteraturstøtte, og ingen plausibel mekanistisk bane — bevispaketets egen begrunnelse konkluderer at skåren reflekterer innebygningsartefakt snarere enn farmakologisk relevans. Kombinert med fraværet av TFDA-sikkerhetsmerkingsdata (blokkering datakløft), oppfyller denne kandidaten ikke terskelen for å avansere forbi S0.

**For å fortsette, er følgende nødvendig:**
- Løs DG001: skaff TFDA-ekvivalente merkingsadvarsler og kontraindikasjoner før fase 1 (S1) sikkerhetsforhåndsvurdering kan gjennomføres
- Løs DG002: skaff en strukturert MOA-post fra DrugBank for å formelt dokumentere factor Xa/TFPI-mekanismen
- Søk preklinisk eller case-nivå bevis som spesifikt tester andexanet alfa (eller factor Xa/TFPI-rettede agenser) i platelet-reseptordefekt-blødningssykdommer, hvis denne indikasjonen skal forfølges videre
- Hvis ingen slik mekanistisk eller empirisk bevis kommer fram, bør denne kandidaten nedprioriteres til fordel for høyere-skårende, evidensbaserte prediksjoner fra denne legemiddelens komplette prediksjonslist

## Ansvarsfraskrivelse

Dette innholdet er kun til forskningsformål og utgjør ikke medisinsk rådgivning.
Klinisk validering kreves før enhver klinisk anvendelse.

---

