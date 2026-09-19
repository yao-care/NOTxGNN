---
layout: default
title: Dupilumab
parent: Kun modellprediksjon (L5)
nav_order: 116
evidence_level: L5
indication_count: 10
---

# Dupilumab
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

# Dupilumab: Fra atopisk dermatitt / astma til bronkitt

## Sammenfattelse i én setning

Dupilumab er et monoklonalt antistoff med etablert rolle i moderat til alvorlig atopisk dermatitt og astma, begge drevet av Type 2 (Th2) inflammasjon. TxGNN-modellen forutsier at det også kan være effektivt for **bronkitt**, men denne retningen støttes foreløpig av kun **1 klinisk studie** (på en relatert tilstand) og **6 publikasjoner**, hvorav de fleste tar for seg astma/KOLS i stedet for bronkitt direkte.

---

## Hurtigoversikt

| Punkt | Innhold |
|-------|---------|
| Original indikasjon | Moderat til alvorlig atopisk dermatitt / astma *(antatt fra klinisk studie- og litteraturbeskrivelser i denne bevispacken — ingen formell TFDA/DrugBank-indikasjon tekst ble hentet; se Datakløfter)* |
| Forutsagt ny indikasjon | Bronkitt |
| TxGNN-prediksjonscore | 99.92% |
| Bevisnivå | L2 *(indirekte — se forbeholdene i begrunnelsen nedenfor)* |
| Markedsstatus Norge | ✗ Ikke markedsført (Ikke markedsført) |
| Antall godkjenninger | 0 |
| Anbefalt beslutning | **Vent** |

---

## Hvorfor er denne prognosen rimelig?

Detaljerte data om virkningsmekanisme fra DrugBank er foreløpig en datakløft (DG002, høy alvorlighetsgrad). Litteraturbevisene samlet i denne pakken beskriver imidlertid dupilumabs virkningsmekanisme uavhengig og konsistent: det er et fullt humant monoklonalt antistoff (IgG4-isotype) som binder den delte interleukin-4-reseptoralfa (IL-4Rα)-underenheten, og blokkerer signalering fra både IL-4 og IL-13 — de to nøkkelcytokiner som driver Type 2/Th2-mediert inflammasjon (PMID 25006719, PMID 30194992, PMID 29557246).

Dupilumabs etablerte bruksområder (atopisk dermatitt, astma, og relaterte tilstander som kronisk rhinosinusitt) deler denne samme Type 2/eosinofil inflammasjonsbanen. Bronkitt — særlig dens eosinofil og røykingassosiierte (astma-KOLS overlap) undertyper — har blitt forbundet i litteraturen med samme Th2/IL-4/IL-13-akse (PMID 30196731 diskuterer kronisk bronkitt innen astma-KOLS overlap; PMID 38488768 diskuterer «nye terapi for eosinofil pediatrisk plastisk bronkitt»; PMID 39904363 gjennomgår farmakologiske tilnærminger, inkludert biologikker, for å forhindre KOLS/bronkitt-forverringer).

Dette gir en plausibel mekanistisk begrunnelse for reposisjonering: hvis bronkitt hos en gitt pasient er drevet av eosinofil/Type 2 luftveisinflammasjon, kunne IL-4/IL-13-blokkering plausibelt redusere inflammasjon og forverringer, på samme måte som dens etablerte virkning i astma. Når det er sagt, bygger bevisene som er tilgjengelig for tiden i stor grad på ekstrapolering fra tilgrensende luftveistilstander (astma, KOLS, CRS) i stedet for fra studier gjennomført spesifikt i en bronkittpopulasjon — denne kløften bør veies nøye i enhver beslutning.

---

## Klinisk forsøksbevis

| Studienummer | Fase | Status | Deltakerantall | Viktige funn |
|---------|------|------|------|---------|
| [NCT04362501](https://clinicaltrials.gov/study/NCT04362501) | Fase 2 | Avsluttet | 33 | Randomisert, dobbeltblindet, placebokontrollert studie av dupilumab i kronisk rhinosinusitt uten nesepolypper (CRSsNP) — en relatert øvre luftvei Type 2-inflammatorisk tilstand, ikke bronkitt i seg selv. Hadde som mål å bestemme klinisk effektivitet på tvers av flere sykdomsendotyper og informere retningslinjer for pasientvalg i fremtidig anvendt forskning. |

*Merk: Ingen studie registrert til nå har rekruttert en bronkitt-spesifikk populasjon; den eneste hentede studien retter seg mot en mekanistisk relatert men distinkt diagnose (CRSsNP).*

---

## Litteraturbevis

| PMID | År | Type | Tidsskrift | Viktige funn |
|------|-----|------|------|---------|
| [30273510](https://pubmed.ncbi.nlm.nih.gov/30273510/) | 2019 | Systematisk oversikt / Meta-analyse | Journal of Asthma | Meta-analyse av RCT-er som sammenligner dupilumab vs. placebo i ukontrollert astma; etablert effektivitets-/sikkerhetsprofil i Type 2 luftveisykdom. |
| [34597534](https://pubmed.ncbi.nlm.nih.gov/34597534/) | 2022 | Åpen-etikett forlengelsesstudie | Lancet Respiratory Medicine | TRAVERSE-studie: langtidsikkerhet og effektivitet (>1 år) av dupilumab i moderat til alvorlig astma. |
| [39904363](https://pubmed.ncbi.nlm.nih.gov/39904363/) | 2025 | Oversikt | Tuberculosis and Respiratory Diseases | Omfattende oversikt over farmakologiske terapi, inkludert biologikker, for å forhindre KOLS-forverringer. |
| [30196731](https://pubmed.ncbi.nlm.nih.gov/30196731/) | 2018 | Oversikt / Ekspertuttalelse | Expert Opinion on Pharmacotherapy | Diskuterer behandlingsutfordringer i røykinginduserte luftveisykdommer, inkludert kronisk bronkitt og astma-KOLS overlap. |
| [38488768](https://pubmed.ncbi.nlm.nih.gov/38488768/) | 2024 | Oversikt | Pediatric Pulmonology | Gjennomgår nye terapi, inkludert biologikker, for eosinofil pediatrisk plastisk bronkitt. |
| [32428511](https://pubmed.ncbi.nlm.nih.gov/32428511/) | 2020 | Observasjonell studie | Chest | MR-basert evaluering av anti-T2 biologisk behandlingseffekter på lungventilasjon i prednisonavhengig astma. |

---

## Markedsinformasjon Norge

Dupilumab har foreløpig **ingen markedsføringsgodkjenning** i Norge i henhold til denne bevispacken (markedsstatus: Ikke markedsført / Ikke markedsført; 0 totale godkjenninger; ingen lisensregistreringer tilgjengelig).

---

## Sikkerhetshensyn

Vennligst se pakningsvedlegget for sikkerhetsinformasjon. *(Viktige advarsler, kontraindikasjoner og legemiddel-legemiddel-interaksjonsdata kunne ikke hentes på dette tidspunktet — TFDA-pakningsvedlegg-utdrag er flagget som en blokkerende datakløft, DG001, som forhindrer en fullstendig S1-sikkerhetsvurdering for denne kandidaten.)*

---

## Konklusjon og neste steg

**Beslutning: Vent**

**Begrunnelse:**
- TFDA-pakningsvedlegget (advarsler/kontraindikasjoner) er en **blokkerende** datakløft (DG001), som i seg selv forhindrer en foreløpig sikkerhetsvurdering (S1) for denne kandidaten.
- Effektivitetsbevis som er spesifikt for bronkitt er indirekte: den eneste registrerte studien retter seg mot en relatert men distinkt tilstand (CRSsNP), og den støttende litteraturen er hentet hovedsakelig fra astma/KOLS-populasjoner i stedet for bronkitt selv.
- Dupilumab er ikke markedsført i Norge, så det eksisterer ingen lokal sikkerhet-/brukserfaring å basere seg på.

**For å fortsette, er følgende nødvendig:**
- TFDA-pakningsvedlegg (advarsler, kontraindikasjoner, forsiktighetsregler) — DG001
- Bekreftet DrugBank virkningsmekanisme-post — DG002
- Bekrefting av legemidlets formelt godkjente opprinnelige indikasjon(er) (regulatorisk lisenstekst)
- Ideelt sett, en studie eller observasjonell studie gjennomført spesifikt i en bronkitt (særlig eosinofil/Type 2) populasjon, i stedet for ekstrapolering fra astma/KOLS/CRS-data
- Bekreftelse av markedsregistreringsstatus i Norge, dersom kommersialisering skal vurderes

## Ansvarsfraskrivelse

Dette innholdet er kun til forskningsformål og utgjør ikke medisinsk rådgivning.
Klinisk validering kreves før enhver klinisk anvendelse.

---

