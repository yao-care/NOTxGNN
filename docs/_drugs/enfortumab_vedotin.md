---
layout: default
title: Enfortumab Vedotin
parent: Kun modellprediksjon (L5)
nav_order: 131
evidence_level: L5
indication_count: 9
---

# Enfortumab Vedotin
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

# Enfortumab vedotin: Fra uspesifisert originalindikasjon til lepra (signal med lav sikkerhet)

## Oppsummering i én setning

Enfortumab vedotin er et antistoff-medikament-konjugat (ADC) som retter seg mot Nectin-4; denne bevis-pakken inneholder ikke dets oprindelige regulatoriske indikasjon eller mekanisme-for-virkning-data. TxGNNs høyeste rangerte prediksjon er **lepra** (score 99.53%), men det finnes **null kliniske forsøk og null publikasjoner** som støtter dette signalet, og modellens eget mekanistiske begrunnelse markerer det som sannsynlig grafstøy snarere enn en genuin biologisk sammenheng. Alle 9 predikerte indikasjoner i denne pakken har en **Avvent**-anbefaling.

---

## Rask oversikt

| Element | Innhold |
|---------|---------|
| Originalindikasjon | Ikke oppgitt (ingen lisens-/regulatoriske data; medikament ikke markedsført) |
| Predikert ny indikasjon | Lepra |
| TxGNN prediksjons score | 99.53% |
| Bevis nivå | L5 |
| Status på norsk marked | Ikke markedsført |
| Antall godkjenninger | 0 |
| Anbefalt beslutning | Avvent |

---

## Hvorfor er denne prediksjonen rimelig?

For tiden er det ikke tilgjengelig detaljert mekanisme-for-virkning-data for enfortumab vedotin i denne bevis-pakken. Basert på litteraturbeviset som er tilstede (en 2025 FAERS farmakovigilans-studie om ADC-er i blærekreft), synes medikamentets virkelige brukskontekst å være et anti-Nectin-4-antistoff-medikament-konjugat som leverer den cytotoksiske lasten MMAE (monomethyl auristatin E) i avansert blærekreft — men dette er utledet fra en sikkerhetssignal-artikkel, ikke bekreftet regulatorisk eller indikasjondata.

For topprangerte prediksjon, **lepra**, eksisterer det ingen mekanistisk sammenheng mellom Nectin-4-targeting eller en mikrotubuli-forstyrrende cytotoksin og *Mycobacterium leprae*-infeksjon. Begrunnelsen som følger med denne prediksjonen uttaler eksplisitt: *"Enfortumab vedotin er en anti-Nectin-4 ADC (MMAE last); det er ingen kjent mekanisme som forklarer effektivitet mot lepra-infeksjon. Den høye TxGNN-scoren gjenspeiler sannsynligvis mangel på biologisk grunnlag og kan representere kunnskapsgraff-støy."*

Dette samme mønsteret gjentar seg på tvers av alle 9 prediksjoner i denne pakken: multipel endokrin neoplasi, hjerneinfarkt, HIV, homozygøs familær hyperkolesterolemi, og to veterinær-/ikke-menneske-sykdommer (infeksiøs bovint rhinotracheitis, ondartete katarrh) mangler alle enhver plausibel mekanistisk sammenheng med en ADC cytotoksisk last. Den ene indikasjonen med litteraturstøtte, candidose, motsies av bevisenes retning — den siterte artikkelen beskriver ADC-assosiert immunsuppresjon som et **risikosignal for uønskede hendelser**, ikke en terapeutisk begrunnelse. Samlet sett støtter denne klyngen av prediksjoner ikke for tiden noen omdirigerings-hypotese.

---

## Bevis fra kliniske forsøk

For tiden er det ingen relaterte kliniske forsøk registrert.

---

## Litteraturbevis

For tiden er det ingen relatert litteratur tilgjengelig for topprangerte indikasjon (lepra).

---

## Alle predikerte indikasjoner (rangert oppsummering)

Fordi denne bevis-pakken evaluerer flere signaler med lav sikkerhet for samme medikament, oppsummeres det fullstendige rangerte settet nedenfor snarere enn en enkelt indikasjon isolert.

| Rangering | Predikert indikasjon | TxGNN score | Bevis nivå | Merknad |
|-----------|----------------------|-------------|-----------|--------|
| 1 | Lepra | 99.53% | L5 | Ingen mekanistisk grunnlag; sannsynligvis grafstøy |
| 2 | Multipel endokrin neoplasi | 99.43% | L5 | Ingen mekanistisk grunnlag |
| 3 | Cytomegalovirus-infeksjon | 99.36% | L5 | Enhver ADC-relatert sammenheng ville være immunsuppresjon-risiko, ikke terapeutisk fordel |
| 4 | Candidose | 99.30% | L4 | Eneste litteratur (FAERS-studie) beskriver ADC-assosiert infeksjonsrisiko, ikke behandlingseffektivitet — bevisenes retning motsier prediksjonen |
| 5 | Hjerneinfarkt | 99.23% | L5 | Ingen mekanistisk grunnlag |
| 6 | HIV infeksjonssykdom | 99.19% | L5 | Ingen mekanistisk grunnlag |
| 7 | Homozygøs familær hyperkolesterolemi | 99.18% | L5 | Ingen mekanistisk grunnlag |
| 8 | Infeksiøs bovint rhinotracheitis | 99.13% | L5 | Ikke-menneske (veterinær) sykdom |
| 9 | Ondartete katarrh | 99.13% | L5 | Ikke-menneske (veterinær) sykdom |

---

## Norsk markedsinformasjon

Medikamentet er ikke markedsført og har ingen registrerte godkjenninger i dette datasettet (0 lisenser).

---

## Cytotoksisitet

Basert på klassifisering av medikamentgruppen fra den tilgjengelige litteraturen (ADC-kontekst i blærekreft), behandles enfortumab vedotin som et antineoplastisk stoff for denne delen.

| Element | Innhold |
|---------|---------|
| Cytotoksisitets klassifisering | Målrettet terapi (antistoff-medikament-konjugat som leverer en MMAE cytotoksisk last) |
| Myelosuppresjon risiko | Se pakningsvedlegg for advarsler og forholdsregler |
| Emetogenisitets klassifisering | Se pakningsvedlegg for advarsler og forholdsregler |
| Overvåkings elementer | Se pakningsvedlegg for advarsler og forholdsregler |
| Håndterings beskyttelse | Se pakningsvedlegg for advarsler og forholdsregler |

---

## Sikkerhetshensyn

Se pakningsvedlegg for sikkerhetsinformasjon.

---

## Konklusjon og neste trinn

**Beslutning: Avvent**

**Begrunnelse:**
Ingen klinisk forsøk eller litteraturbevis støtter noen av de 9 predikerte indikasjonene over L4, og den høyeste scorede prediksjonen (lepra) har en eksplisitt angitt mangel på biologisk plausibilitet. Den ene kandidaten med støttende litteratur (candidose) motsies i retning — beviset beskriver en sikkerheitsrisiko, ikke en terapeutisk begrunnelse. Kombinert med manglende originalindikasjon og MOA-data, oppfyller denne kandidaten ikke terskelen for å gå videre forbi S0.

**For å gå videre er følgende nødvendig:**
- TFDA/regulatorisk etikett (advarsler, kontraindikasjoner) — for tiden en **Blokkerende** datakløft (DG001); påkrevd før noen S1 sikkerhetskontroll
- Bekreftet mekanisme-for-virkning-data fra DrugBank — for tiden en **Høy** alvorlighetsgrad kløft (DG002)
- Originalindikasjon og regulatorisk historie for medikamentet
- Hvis noen av disse 9 signalene skal forfølges videre, dedikerte litteratur-/kliniske-forsøks-søk spesifikk for det sykdom-medikament-par, siden ingen for tiden eksisterer utover den enkle (motstridende) candidose-referansen

## Ansvarsfraskrivelse

Dette innholdet er kun til forskningsformål og utgjør ikke medisinsk rådgivning.
Klinisk validering kreves før enhver klinisk anvendelse.

---

