---
layout: default
title: Remdesivir
parent: Kun modellprediksjon (L5)
nav_order: 301
evidence_level: L5
indication_count: 6
---

# Remdesivir
{: .fs-9 }

Evidensnivå: **L5** | Predikerte indikasjoner: **6** stk.
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

# Remdesivir: fra COVID-19 (SARS-CoV-2-infeksjon) til multipel endokrin neoplasi

## Sammenfatting på én setning

Remdesivir er et nukleotid-analogt antiviralt middel som opprinnelig ble utviklet og klinisk brukt mot RNA-virus, mest omfattende dokumentert i denne evidenspakken gjennom store COVID-19 (SARS-CoV-2) forsøk. TxGNN-modellens høyest rangerte prediksjon er **multipel endokrin neoplasi**, men denne kandidaten støttes av **null kliniske forsøk** og **null publikasjoner**, og modellens nest høyest rangerte kandidat (HIV-infeksjon) viser seg – ved gjennomgang av bevis – å være bygget helt på feilmerkede COVID-19-forsøksdata i stedet for genuint HIV-bevis. Samlet sett støtter ikke dette kandidatsettet en gjenbruksavgjørelse på dette tidspunktet.

---

## Rask oversikt

| Punkt | Innhold |
|-------|---------|
| Original indikasjon | Ikke dokumentert i Taiwan-regulatoriske registreringer (legemiddel ikke markedsført); bevis fra kliniske forsøk i denne pakken identifiserer konsekvent remdesivirs etablerte bruk som behandling av COVID-19 (SARS-CoV-2-infeksjon) |
| Forutsagt ny indikasjon | Multipel endokrin neoplasi |
| TxGNN-prediksjonspoeng | 99.50% |
| Bevisnivå | L5 |
| Status på Taiwan-marked | ✗ Ikke markedsført |
| Antall godkjenninger | 0 |
| Anbefalt beslutning | Innestill |

---

## Hvorfor er denne prediksjonen rimelig?

Detaljerte, verifiserte data om virkningsmekanisme for remdesivir er ikke tilgjengelig fra DrugBank i denne evidenspakken (flagget som en datakløft med høy alvorlighetsgrad). Basert på gjenbruksrasjonalet som følger med prediksjoner, er remdesivir et nukleotid-analogt middel som hemmer den virale RNA-avhengig RNA-polymerase (RdRp), replikasjonsenzymet som brukes av RNA-virus som SARS-CoV-2 og Ebola-virus.

Multipel endokrin neoplasi (MEN) er et arvelig tumordsyndrom drevet av germlinale mutasjoner i gener som *RET* og *MEN1*, med en patofysiologi sentrert rundt endokrin cellproliferasjon snarere enn viral replikasjon. Det er ingen kjent mekanistisk vei som forbinder RdRp-hemming til MEN-patogenese, og ingen kliniske forsøk eller litteratur ble hentet for å støtte denne koblingen. Evidenspakkens eget rasjonale karakteriserer eksplisitt denne prediksjonen som sannsynlig **graph-embedding-støy** i TxGNN-kunnskapsgrafen snarere enn et biologisk fundert signal.

Et relatert mønster vises i modellens nest høyest rangerte prediksjon, HIV-infeksjon: selv om 23 kliniske forsøk og 20 publikasjoner ble hentet, viser manuell gjennomgang at nesten alle av dem er COVID-19/SARS-CoV-2-studier som ble feilmatches til etiketten "HIV-infeksjonssykdom" i kildedatabasen, ikke genuine remdesivir-for-HIV-bevis. Dette forsterker at dette kandidatsettet, som det for øyeblikket er avledet, ikke representerer et validert gjenbrukssignal.

---

## Bevis fra kliniske forsøk

Det er for øyeblikket ingen relaterte kliniske forsøk registrert for den høyest rangerte forutsagte indikasjonen (multipel endokrin neoplasi).

---

## Litteraturbevis

Det er for øyeblikket ingen relatert litteratur tilgjengelig for den høyest rangerte forutsagte indikasjonen (multipel endokrin neoplasi).

---

## Andre forutsagte indikasjoner som er utelukket (kontekst)

Evidenspakken inkluderte fem ytterligere kandidater utover topprankingen. Alle ble gjennomgått og avvist av de samme årsakene — mekanistisk implausibilitet, fraværende bevis, eller feilmerking av database:

| Rangering | Sykdom | Poeng | Bevis | Nøkkelproblematikk |
|----------|---------|-------|----------|-------------|
| 2 | HIV-infeksjonssykdom | 99.32% | 23 forsøk / 20 artikler (alle COVID-19-relaterte) | Feilmerking av database — ingen genuint HIV-bevis; RdRp-hemmer retter seg ikke mot revers transkriptase |
| 3 | Felint immundefisienssyndrom | 99.07% | Ingen | Sannsynlig forvirring med felint coronavirus (FIP) grafnaboskaper; FIV er et retrovirus, mekanismemismatch |
| 4 | Simian immunodeficiency virus-infeksjon | 99.07% | Ingen | Retrovirus, samme mekanismemismatch som HIV/FIV |
| 5 | Nevrutviklingsforstyrrelse (ataktisk gang, fraværende tale, nedsatt hvit substans) | 99.03% | Ingen | Sjelden genetisk forstyrrelse, ingen plausibel biologisk kobling til antiviralt RdRp-hemming |
| 6 | Homozygot familiær hyperkolesterolemi | 99.03% | Ingen | Lipidmetabolisme-forstyrrelser (LDLR/APOB/PCSK9), ingen plausibel kobling til antiviralt mekanisme |

Alle seks kandidater ble tildelt en **innestillingsanbefaling** av scoringssystemet.

---

## Informasjon om Taiwan-marked

Remdesivir er for øyeblikket **ikke markedsført** på Taiwan – ingen legemiddellisenser finnes i registre, så ingen godkjent indikasjonstekst, doseringsform eller godkjenningsnummer er tilgjengelig som referanse.

---

## Sikkerhetshensyn

Se pakningsvedlegget for sikkerhetsinformasjon. TFDA-spesifikke advarsler og kontraindikasjoner for remdesivir kunne ikke hentes i denne evidenspakken (flagget som en datakløft med blokkerings-alvorlighetsgrad), og ingen registre over legemiddel-legemiddel-interaksjoner ble funnet.

---

## Konklusjon og neste trinn

**Beslutning: Innestill**

**Begrunnelse:**
Den høyest rangerte forutsagte indikasjonen (multipel endokrin neoplasi) har ingen støtte fra kliniske forsøk, litteratur, eller plausibel mekanistisk rasjonale (Bevisnivå L5). Den neste mest «bevisede» kandidaten (HIV) er en artefakt av databasefeilmerking – de underliggende forsøkene og publikasjonene er nesten helt COVID-19-studier, ikke genuint HIV-bevis. Ingen av de seks kandidatene i denne evidenspakken oppfyller en terskel som er tilstrekkelig for videre klinisk evaluering.

**For å gå videre er følgende nødvendig:**
- TFDA-pakningsvedleggsdata (advarsler, kontraindikasjoner) – for øyeblikket en datakløft med blokkerings-alvorlighetsgrad
- Verifisert data om virkningsmekanisme fra DrugBank – for øyeblikket en datakløft med høy alvorlighetsgrad
- Korrigering av feil i kartlegging av sykdomsetiketter i den underliggende forsøks-/litteraturdatabasen (HIV-feilmerkingen bør flagges oppstrøms slik at den ikke gjentas i fremtidig kandidatgenerering)
- Hvis noen fremtidig TxGNN-kjøring produserer en mekanistisk plausibel RNA-virus-relatert indikasjon for remdesivir, bør den kandidaten re-evalueres på egne vilkår

## Ansvarsfraskrivelse

Dette innholdet er kun til forskningsformål og utgjør ikke medisinsk rådgivning.
Klinisk validering kreves før enhver klinisk anvendelse.

---

