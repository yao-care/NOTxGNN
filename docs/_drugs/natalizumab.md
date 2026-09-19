---
layout: default
title: Natalizumab
parent: Kun modellprediksjon (L5)
nav_order: 237
evidence_level: L5
indication_count: 5
---

# Natalizumab
{: .fs-9 }

Evidensnivå: **L5** | Predikerte indikasjoner: **5** stk.
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

# Natalizumab: Fra udokumentert opprinnelig indikasjon til bronkitt

## Oppsummering i en setning

Natalizumab (DrugBank ID DB00108) beskrives i den underliggende gjenbruksrasjonalen som et anti-α4-integrin (VLA-4) monoklonalt antistoff, men dets opprinnelig godkjente indikasjon og formelle virkningsmekanisme-register er ikke dokumentert i det gjeldende bevismateriell. TxGNN-modellens høyest rangerte prediksjon er **Bronkitt**, men denne prediksjonen støttes for tiden av **0 kliniske forsøk** og **0 publikasjoner** — det gjenspeiler bare topologisk lignhet i kunnskapsgrafen, uten mekanistisk eller klinisk støtte.

---

## Rask oversikt

| Punkt | Innhold |
|------|---------|
| Opprinnelig indikasjon | Ikke dokumentert i bevismateriell (se Datamangler) |
| Prediktert ny indikasjon | Bronkitt |
| TxGNN-prediksjonsscore | 99.46% |
| Bevisnivå | L5 |
| Norges markedsstatus | Ikke markedsført |
| Antall autorisasjoner | 0 |
| Anbefalt beslutning | Avvent |

---

## Hvorfor er denne prediksjonen rimelig?

For tiden er detaljerte virkningsmekanisme-data for natalizumab ikke tilgjengelige som et strukturert felt i dette bevismateriell. Modellens egen rasjonale karakteriserer imidlertid natalizumab som et anti-α4-integrin (VLA-4) monoklonalt antistoff som blokkerer leukosyttmigrering over VCAM-1-eksprimerende endotel inn i betent vev. Dette er en mekanisme forbundet med autoimmune/nevroinflamatoriske tilstander, ikke med akutt eller kronisk luftveisinfeksjon/betennelse (bronkitt).

Bevismateriell angir eksplisitt at det er **ingen direkte mekanistisk argument** som forbinder VLA-4/VCAM-1-blokering med bronkitt-patofysiologi. Den høye TxGNN-scoren (99.46%) ser ut til å være drevet helt av graf-embedding-nærhet i kunnskapsgrafen, ikke av noen hentet klinisk forsøk eller litteratursignal — det er null støttende oppføringer av noen som helst type for denne indikasjonsparet.

Gitt den fullstendige mangelen på støttende bevis og mangelen på en sammenhengende mekanistisk hypotese, bør denne prediksjonen behandles som kun utforskende, ikke som grunnlag for videre klinisk utvikling på dette stadiet.

---

## Bevis fra kliniske forsøk

For tiden er det ingen relaterte kliniske forsøk registrert.

---

## Litteraturbevis

For tiden er det ingen relatert litteratur tilgjengelig.

---

## Norges markedsinformasjon

Natalizumab har **0 autorisasjoner** i oversikten og en markedsstatus på "Ikke markedsført" i dette bevismateriell — ingen lisensposter er tilgjengelige for tabellering.

---

## Sikkerhetshensyn

Vennligst se pakningsvedlegget for sikkerhetsinformasjon. (Viktige advarsler, kontraindikasjoner og data om legemiddelinteraksjon er for tiden ikke tilgjengelige i dette bevismateriell; TFDA/produktetikett-oppslaget er flagget som et **Blokkering**-alvorlighetsgrad-datahull — se Konklusjon.)

---

## Konklusjon og neste steg

**Beslutning: Avvent**

**Rasjonale:**
Den høyest rangerte prediksjonen (Bronkitt) har bevisnivå L5 — en modellscore med null kliniske forsøk og null litteratursupport, og pakkens egen mekanistiske analyse finner ingen direkte rasjonale som forbinder legemidlets foreslåtte mekanisme til denne sykdommen. Separat er det et **Blokkering**-alvorlighetsgrad-datahull (manglende TFDA-etikett/advarsler) som betyr at kandidaten ikke engang kan passere en innledende sikkerhetskontroll (S1), uavhengig av effektivitetsbevis.

**For å fortsette, er følgende nødvendig:**
- TFDA/regulatorisk etikett (advarsler, kontraindikasjoner) — påkrevd for å rydde S1-sikkerhetsporten (for tiden blokkert datahull, DG001)
- Verifisert virkningsmekanisme-register fra DrugBank eller primærlitteratur (for tiden høy-alvorlighetsgrad datahull, DG002)
- Bekreftet opprinnelig godkjent indikasjon(er) for legemidlet, for å etablere en basislinje for mekanistisk sammenligning
- Minst preklinisk eller observasjonsbevis som direkte forbinder α4-integrin/VLA-4-blokering til bronkitt-patofysiologi før avansering utover modell-prediksjonsstadium

*Merknad: innenfor denne samme prediksjonsgruppen, er flere andre kandidatindikasjoner for natalizumab (psoriasis, parapsoriasis, acute lichenoid pityriasis) bare støttet av kasusrapporter som beskriver disse tilstandene som **bivirkninger indusert eller forverret av natalizumab-behandling**, ikke som terapeutiske fordeler. Disse bør ikke misforstås som effektivitetssignaler under triering.*

## Ansvarsfraskrivelse

Dette innholdet er kun til forskningsformål og utgjør ikke medisinsk rådgivning.
Klinisk validering kreves før enhver klinisk anvendelse.

---

