---
layout: default
title: Aztreonam
parent: Kun modellprediksjon (L5)
nav_order: 51
evidence_level: L5
indication_count: 10
monitor_inn: "AZTREONAM"
predicted_indications: ["hyperamylasemia", "polyclonal hyperviscosity syndrome", "congenital analbuminemia", "gonococcal urethritis", "Ureaplasma urethritis", "blood group incompatibility", "premalignant hematological system disease", "epiglottitis", "monoclonal gammopathy", "xanthogranulomatous pyelonephritis"]
last_modified_at: 2026-11-24
description: "Aztreonam: predikert ny indikasjon Hyperamylasemi (hyperamylasemia) (evidensnivå L5). Opprinnelig indikasjon: Gram-Negative Bacterial Infections"
---

# Aztreonam
{: .fs-9 }

Evidensnivå: **L5** | Predikerte indikasjoner: **10** stk.
{: .fs-6 .fw-300 }

---

## Innholdsfortegnelse
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist" markdown="1">

## Farmasøytens vurderingsrapport

</div>

## Aztreonam: monobaktam-antibiotikum → hyperamylasemi (hyperamylasemia)
{: .text-alpha }

## Oppsummering i én setning

Aztreonam er et monobaktam-antibiotikum som hemmer bakteriell celleveggsyntese hos gramnegative bakterier. TxGNN-modellen predikerer at legemidlet kan være aktuelt ved **hyperamylasemi (hyperamylasemia)**, men dette er en laboratoriefunn-diagnose uten støtte i de innsamlede dataene: det finnes **ingen kliniske studier** og **ingen publikasjoner** som omhandler denne tilstanden direkte.

## Hurtigoversikt

| Punkt | Innhold |
|------|------|
| Opprinnelig indikasjon | Gram-Negative Bacterial Infections;Urinary Tract Infections;Healthcare-Associated Pneumonia;Soft Tissue Infections |
| Predikert ny indikasjon | Hyperamylasemi (hyperamylasemia) |
| TxGNN-skåre | 0,9973 |
| Evidensnivå | L5 |
| Markedsstatus i Norge | Markedsført (gyldige tillatelser: 1 av 1) |
| Antall godkjenninger | 1 (gyldige: 1) |
| Anbefalt beslutning | Hold |

## Hvorfor er denne prediksjonen (ikke) rimelig?

Ifølge avsnittet «Mechanism of Action» i preparatomtalen som er godkjent av amerikanske FDA (Prescribing Information), for Aztreonam (uoffisiell oversettelse): «Aztreonam er et baktericid middel som virker ved å hemme syntesen av bakteriecelleveggen. Aztreonam har aktivitet i nærvær av enkelte betalaktamaser, både penicillinaser og cefalosporinaser, hos gramnegative og grampositive bakterier.» Engelsk originaltekst: "Aztreonam is a bactericidal agent that acts by inhibition of bacterial cell wall synthesis. Aztreonam has activity in the presence of some beta-lactamases, both penicillinases and cephalosporinases, of Gram-negative and Gram-positive bacteria." ([DailyMed: aztreonam prescribing information, Hospira, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=d4500795-3b07-4a7d-b432-73cafbb3dbc6), versjon av 2024-06-03; hentet 2026-11-19). Aztreonam er likevel kjent som et monobaktam som hemmer penicillinbindende protein 3 (PBP3) hos gramnegative aerobe bakterier.

Hyperamylasemi er et laboratoriefunn (forhøyet amylase i blod), ikke en infeksjonssykdom. Det finnes ingen plausibel mekanistisk kobling mellom en antibakteriell virkning og senking av serumamylase. Den høye skåren (0,9973) ser ut til å være et artefakt fra modellens grafbaserte læring og bør ikke tolkes som klinisk støtte. Det finnes heller ingen forskjell i skåre som skiller denne prediksjonen fra den neste på listen (polyklonalt hyperviskositetssyndrom, samme skåre), noe som styrker inntrykket av at skåren i seg selv er lite informativ her.

## Evidens fra kliniske studier

Foreløpig er ingen relaterte kliniske studier registrert.

## Litteraturevidens

Foreløpig er ingen relatert litteratur tilgjengelig.

## Informasjon om det norske markedet

<!-- licenses:begin -->

| Godkjenningsnummer | Preparatnavn (EMA) | Virkestoff(er) (EMA, engelsk) | Terapeutisk område (EMA, engelsk) | Status |
|------|------|------|------|------|
| EMEA/H/C/006113 | Emblaveo | avibactam; aztreonam | Gram-Negative Bacterial Infections; Urinary Tract Infections; Healthcare-Associated Pneumonia; Soft Tissue In… | Gyldig |

Kilde: EMA – Medicines output (sentralt godkjente legemidler til mennesker); preparatnavn, virkestoffer og terapeutisk område er gjengitt i engelsk original. Nasjonale markedsføringstillatelser (DMP) og veterinærpreparater er ikke med i disse dataene.

<!-- licenses:end -->

<!-- review:begin no-lic-20261124b-aztreonam-1 -->

> **Kontrollrettelse (2026-11-24)**: Opprinnelig sto det: «Merk: Denne godkjenningen gjelder et produkt som oppføres som enkeltstoff i de lokale dataene, og lisensposten er markert som kansellert, mens samlet markedsstatus i dataene er «Markedsført». Statusen bør verifiseres mot oppdatert kilde før en eventuell beslutning.» Fjernet: merknaden om at lisensposten er kansellert og gjelder et enkeltstoffprodukt, stemte ikke med EMAs data om sentrale EU-godkjenninger (2026-11-12): godkjenningen står som gyldig (Authorised), og Emblaveo er et kombinasjonspreparat (avibactam og aztreonam). Oppdaterte antall og statuser for godkjenningene står i hurtigoversikten og i lisenstabellen under markedsinformasjonen. Kilde: [EMA – Medicines output: medicines report](https://www.ema.europa.eu/en/documents/report/medicines-output-medicines-report_en.xlsx); [European Medicines Agency](https://www.ema.europa.eu/).

<!-- review:end no-lic-20261124b-aztreonam-1 -->

## Sikkerhetsvurderinger

**Legemiddelinteraksjoner:** Det er registrert 27 mulige interaksjoner. Av de som er klassifisert med alvorlighetsgrad, er følgende **moderate**:
- Pikosulfat (picosulfuric acid)
- Dikumarol
- Warfarin

Øvrige registrerte interaksjoner har ukjent alvorlighetsgrad, blant annet vankomycin, amikacin, amfotericin B, takrolimus, heparin, acetylsalisylsyre, metronidazol og flukonazol. Kombinasjon med antikoagulantia (warfarin, dikumarol, heparin) krever særlig oppmerksomhet.

**Sykdomstilstander registrert som kontraindikasjoner i datagrunnlaget:** nyresykdom, leversykdom, galleblæresykdom, Clostridium difficile-kolitt, perinatal nekrotiserende enterokolitt, bronkial sykdom og pyoureter. Dette er ikke hentet fra preparatomtale og må bekreftes mot denne.

For øvrig sikkerhetsinformasjon, se preparatomtalen.

## Konklusjon og neste steg

**Beslutning: Hold**

**Begrunnelse:**
Hyperamylasemi er et laboratoriefunn uten plausibel mekanistisk kobling til et antibakterielt middel, og det finnes verken kliniske studier eller publikasjoner som støtter prediksjonen. Evidensnivået er L5 (kun modellprediksjon).

**For å gå videre kreves følgende:**
- Direkte kliniske eller prekliniske data som kobler aztreonam til hyperamylasemi (ingen finnes i dag)
- En klar klinisk hypotese som skiller en eventuell effekt fra et rent artefakt i modellen
- Preparatomtale med advarsler og kontraindikasjoner for en fullstendig sikkerhetsvurdering
- Verifisering av gjeldende markedsstatus og lisensstatus i Norge

<!-- review:begin log -->

## Kontrollogg

Nedenfor er kontrolloggen for denne siden: opplysninger kontrollert mot EMAs data om sentrale EU-godkjenninger. Rettelser gjelder bare grunnleggende faktaopplysninger; modellens prediksjoner, evidensnivåer og konklusjoner er ikke skrevet om. Setningen om at data om virkningsmekanismen ikke var tilgjengelige, er erstattet med et utdrag fra den oppgitte offisielle preparatomtalen (med uoffisiell oversettelse).

| Kontrolldato | Punkt | Tiltak | Kilde |
|------|------|------|------|
| 2026-11-19 | Setningen «data om virkningsmekanismen er ikke tilgjengelige» erstattet med utdrag fra amerikansk preparatomtale | Setning om manglende data om virkningsmekanismen erstattet med et utdrag med kilde | [DailyMed: aztreonam prescribing information, Hospira, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=d4500795-3b07-4a7d-b432-73cafbb3dbc6) |
| 2026-11-24 | Fjernet: «Merk: Denne godkjenningen gjelder et produkt som oppføres som enkeltstoff i de lokale dataene, og lisensposten er markert som kansellert, mens samlet markedsstatus i dataene er «Markedsført». Statusen bør verifiseres mot oppdatert kilde før en eventuell beslutning.» | Rettet | [EMA – Medicines output: medicines report](https://www.ema.europa.eu/en/documents/report/medicines-output-medicines-report_en.xlsx); [European Medicines Agency](https://www.ema.europa.eu/) |

<!-- review:end log -->

## Ansvarsfraskrivelse

Dette innholdet er kun til forskningsformål og utgjør ikke medisinsk rådgivning.
Klinisk validering kreves før enhver klinisk anvendelse.

---

