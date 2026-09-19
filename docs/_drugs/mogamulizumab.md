---
layout: default
title: Mogamulizumab
parent: Kun modellprediksjon (L5)
nav_order: 233
evidence_level: L5
indication_count: 7
---

# Mogamulizumab
{: .fs-9 }

Evidensnivå: **L5** | Predikerte indikasjoner: **7** stk.
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

# Mogamulizumab: Fra kutane T-celleslymfomer til urotelialt karsinom i prostata-urinrør

## Sammendrag i én setning

> Mogamulizumab er et humanisert anti-CCR4-monoklonalt antistoff historisk knyttet til kutane T-celleslymfomer (CTCL)/Sézarys syndrom (ifølge bevispakets mekanistiske notater; ikke til stede i det strukturerte `original_indications`-feltet).
> TxGNN-modellen predikerer at det kan være effektivt for **urotelialt karsinom i prostata-urinrør**,
> men **0 kliniske studier** og **0 publikasjoner** støtter for tiden denne retningen — dette er en ren beregningsbasert prediksjon.

## Kort oversikt

| Element | Innhold |
|---------|---------|
| Original indikasjon | Kutane T-celleslymfomer (CTCL) / Sézarys syndrom — referert kun i bevispakets rasjonale-tekst; ikke fanget i det strukturerte `original_indications`-feltet |
| Forutsagt ny indikasjon | Urotelialt karsinom i prostata-urinrør |
| TxGNN prediksjonspoengsum | 99.44% (rang 5955) |
| Bevisnivå | L5 |
| Status på norsk marked | Ikke markedsført |
| Antall autorisasjoner | 0 |
| Anbefalt avgjørelse | Utsett |

## Hvorfor er denne prediksjonen rimelig?

Strukturerte virkemåte-data er ikke tilgjengelig for dette legemidlet (`original_moa: [Data Gap]`). Imidlertid beskriver rasjonale-teksten knyttet til hver kandidat konsekvent mogamulizumab som et humanisert anti-CCR4-monoklonalt antistoff som depletterer CCR4-positive tumor-infiltrerende regulatoriske T-celler (Tregs) via antisstoff-avhengig cellulær cytotoksisitet (ADCC), og derved lindrer tumor-formidlet immunsuppresjon.

De forutsatte nye indikasjonene — urotelialt karsinom i prostata-urinrør, nyrebækken og blæren, pluss flere sjeldne tumorer (HHV8-relaterte tumorer, ektomesenkymom, ondartad granulær celletumor i huden) — er knyttet til den opprinnelige mekanismen bare gjennom en generell biologisk hypotese: mange solide tumorer viser CCR4+ Treg-infiltrasjon, og depletering av disse cellene kunne teoretisk gjenopprette anti-tumor-immunitet. Ingen av de sju kandidatene har spesifikke biomarkør-data, prekliniske modeller eller klinisk erfaring sitert i denne bevispakningen for å bekrefte CCR4/Treg-involvering i disse spesifikke tumortyper.

Kort sagt, dette er en mekanistisk plausibel men helt uvalidert ekstrapolasjon. TxGNN-poengsumet reflekterer nettverksbasert likhet i kunnskapsgrafen, ikke eksperimentell eller klinisk evidens.

## Evidens fra kliniske studier

Ingen relaterte kliniske studier er for tiden registrert

## Litteratureviden

Ingen relatert litteratur er for tiden tilgjengelig

## Norsk markedsinformasjon

Mogamulizumab har for tiden **ingen markedsautorisasjoner i Norge** (`total_licenses: 0`, `market_status: Not marketed`). Ingen produktoppføringer, doseringsformer eller godkjent indikasjonsstekst er tilgjengelig i bevispakningen.

## Cytotoksisitet

Mogamulizumab er et antineoplastisk biologikum (anti-CCR4-monoklonalt antistoff, immunterapiklasse); seksjonen nedenfor er inkludert tilsvarende.

| Element | Innhold |
|---------|---------|
| Klassifikasjon av cytotoksisitet | Immunterapi (anti-CCR4-monoklonalt antistoff; Treg-depleterende mekanisme, ikke et konvensjonelt cytotoksisk middel) |
| Risiko for myelosuppresjon | Ikke karakterisert i denne bevispakningen. Vennligst se pakningsvedleggets advarsler og forholdsregler |
| Klassifikasjon av emetogenitet | Lav (typisk for antisstoff-basert immunterapi, som generelt har minimal direkte emetogen potensial) |
| Overvåkingspunkter | CBC, hud-/mukokutan undersøkelse, infusjonsreaksjonsovervåking og overvåking for immunrelaterte bivirkninger (leverfunksjon, skjoldbruskkirtel-funksjon, GI-symptomer) — i samsvar med monoklonalt antistoff-immunterapiklasse |
| Håndteringsbeskyttelse | Ingen cytotoksisk farliglegemidler-data gitt; bekreft håndteringskrav mot institusjonelle biologikum/monoklonalt antistoff-infusjonsprotokoll |

## Sikkerhetshensyn

Vennligst se pakningsvedlegget for sikkerhetsinformasjon.

> Merk: Dette er en **blokkering** datakløft (DG001 — TFDA/etikett-advarsler og motindikasjoner utilgjengelig), som i seg selv er tilstrekkelig til å forhindre progresjon forbi initiell sikkerhetspreskåning (S1).

## Konklusjon og neste trinn

**Avgjørelse: Utsett**

**Begrunnelse:**
Alle sju forutsagte indikasjonene ligger på bevisnivå L5 (modellprediksjon kun, ingen studier eller litteratur), legemidlet er ikke markedsført i Norge, og en blokkering datakløft (TFDA/regulatorisk etikett-data: advarsler, motindikasjoner) forhindrer enhver sikkerhetspreskåning. Det er for tiden ingen grunnlag for å avansere forbi hypotesestadiet.

**For å fortsette, er følgende nødvendig:**
- Løs DG001: innhent TFDA/regulatorisk etikett-data (advarsler, motindikasjoner, DDI)
- Løs DG002: bekreft virkemåte via DrugBank API (utover rasjonale-tekst-beskrivelsen)
- Bekreft legemidlets faktiske opprinnelig godkjente indikasjon(er) i strukturert form
- Målrettet litteratur-/forsøkssøk for CCR4-ekspresjon eller Treg-infiltrasjon i urotelialt karsinom og de andre kandidattumortypene
- Hvis noe signal dukker opp, prioriter preklinisk/biomarkør-studier før du vurderer klinisk evaluering

## Ansvarsfraskrivelse

Dette innholdet er kun til forskningsformål og utgjør ikke medisinsk rådgivning.
Klinisk validering kreves før enhver klinisk anvendelse.

---

