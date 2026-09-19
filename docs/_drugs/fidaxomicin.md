---
layout: default
title: Fidaxomicin
parent: Kun modellprediksjon (L5)
nav_order: 151
evidence_level: L5
indication_count: 9
---

# Fidaxomicin
{: .fs-9 }

Evidensnivå: **L5** | Predikerte indikasjoner: **9** stk.
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

# Fidaxomicin: Fra uspesifisert opprinnelig indikasjon til Staphylococcal Scalded Skin Syndrome

## Sammendrag i én setning

> Evidenspakken for Fidaxomicin (DrugBank ID: DB08874) inneholder ikke data om dets opprinnelige godkjente indikasjon eller virkemåte, og legemidlet har for tiden ingen markedsgodkjenning i Norge.
> TxGNN-modellens topprediksjon er **Staphylococcal Scalded Skin Syndrome (SSSS)**, men dette støttes av **0 kliniske forsøk** og **0 publikasjoner**,
> og begrunnelsen som følger med prediksjonen selv markerer den mekanistiske sammenhengen som svak, mest sannsynlig en modellartefakt i stedet for et genuint repurposerings-signal.

## Hurtigoversikt

| Punkt | Innhold |
|-------|---------|
| Opprinnelig indikasjon | Ikke tilgjengelig — ingen lisens-/indikasjondata i evidenspakken |
| Forutsagt ny indikasjon | Staphylococcal Scalded Skin Syndrome |
| TxGNN-prediksjonsscore | 99.71% |
| Bevisnivå | L5 |
| Norsk markedsstatus | ✗ Ikke markedsført |
| Antall godkjennelser | 0 |
| Anbefalt beslutning | Vent |

## Hvorfor er denne prediksjonen rimelig?

For øyeblikket er det ikke tilgjengelig detaljerte data om virkemåte for Fidaxomicin i denne evidenspakken, og ingen opprinnelig indikasjon er registrert heller. Det som kan rekonstrueres fra generell farmakologi (som nevnt i modellens egen begrunnelse) er at fidaxomicin er et snevertsektrum-makrolid med in vitro-aktivitet mot noen gram-positive organismer, inkludert *S. aureus*. Den administreres imidlertid oralt og har ubetydelig systemisk biotilgjengelighet (<0,5%), og virker nesten utelukkende innenfor tarmlumen.

Staphylococcal Scalded Skin Syndrome er en toksittformidlet, systemisk hudsykdom som krever et antibiotikum som er i stand til å nå terapeutiske konsentrasjoner systemisk for å fjerne toksinproduserende staphylococcus-fokus. Gitt fidaxomicinets farmakokinetiske profil, kan det ikke oppnå meningsfull systemisk eksponering, så det mekanistiske grunnlaget for denne prediksjonen er svakt.

Modellens egen repurposerings-begrunnelse karakteriserer eksplisitt dette som et sannsynlig tilfelle av TxGNN-embedding-overgeneralisering — modellen ser ut til å plukke opp «anti-staphylococcus-aktivitet» som en delt egenskap uten å ta hensyn til administrasjonsmåte og farmakokinetisk uoverensstemmelse. Samme forbehold (ingen systemisk eksponering, ingen topisk/parenteral formulering) gjentar seg på tvers av nesten alle de ni beste forutsagte indikasjonene for dette legemidlet (bullös impetig, impetig, hordeolum, *S. aureus*-pneumoni), og to prediksjoner (inhalativ og toksittformidlet botulisme) er mekanistisk usammenhengende i det hele tatt (nevrotoksin-formidlet sykdom vs. et antibakterielt middel), og en (vulvovaginal kandidose) involverer en sopppatogen som fidaxomicin, et antibakteriell RNA-polymerase-hemmer, ikke har kjent aktivitet mot.

## Bevis fra kliniske forsøk

Foreløpig ingen relaterte kliniske forsøk registrert

## Litteraturbevis

Foreløpig ingen relatert litteratur tilgjengelig

## Norsk markedsinformasjon

Fidaxomicin har for øyeblikket **ingen markedsgodkjenning i Norge** (markedsstatus: Ikke markedsført, 0 lisenser registrert). Ingen produkt-, doseringsform- eller godkjent-indikasjondata er tilgjengelig.

## Sikkerhetshensyn

Vennligst se pakningsvedlegget for sikkerhetsinformasjon.

*(Merk: viktige advarsler, kontraindikasjoner og legemiddelinteraksjonsdata er merket som en blokkerende datakløft (DG001) i denne evidenspakken — TFDA/regulatoriske etiketterdata har ikke blitt hentet og analysert ennå.)*

## Konklusjon og neste skritt

**Beslutning: Vent**

**Begrunnelse:**
Topprediksjonen (SSSS) har høy TxGNN-likhetsscore, men er helt uten støtte fra kliniske forsøk eller litteratur (Bevisnivå L5), og modellens egen mekanistiske begrunnelse identifiserer fidaxomicinets ubetydelige systemisk absorpsjon som en grunnleggende barriere for effektivitet i en systemisk, toksittformidlet hudsykdom. Dette mønsteret gjentar seg på tvers av i hovedsak alle topprangerte prediksjoner for dette legemidlet — flere er mekanistisk usannsynlige (soppformidlet eller nevrotoksin-formidlet sykdommer mot et snevertsektrum-antibakteriell middel), og ingen har tilgjengelig administrasjonsmåte (topisk/oftalmisk/parenteral) som samsvarer med den foreslåtte indikasjonen. Kombinert med en blokkerende sikkerhetsdatakløft (DG001), er det ingen grunnlag for å avansere noen av disse kandidatene forbi innledende screening.

**For å fortsette er følgende nødvendig:**
- Løs DG001: hent og analyser TFDA (eller tilsvarende) etikett-advarsler/kontraindikasjoner før noen S1-sikkerhetssscreening kan forekomme
- Få bekreftet virkemåte (DG002) og opprinnelig godkjent indikasjon for fidaxomicin for å riktig forankre likhets-til-original-analyse
- Hvis SSSS- eller impetig-type-indikasjoner skal forfølges videre, etabler først om en topisk/dermatologisk formulering av fidaxomicin er teknisk gjennomførbar, siden den orale formuleringens PK-profil ikke støtter disse brukssakene
- Uavhengig litteratur-/mekanisme-gjennomgang for å skille genuint repurposerings-signal fra TxGNN-embedding-overgeneralisering før du forplikter videre evalueringsressurser

## Ansvarsfraskrivelse

Dette innholdet er kun til forskningsformål og utgjør ikke medisinsk rådgivning.
Klinisk validering kreves før enhver klinisk anvendelse.

---

