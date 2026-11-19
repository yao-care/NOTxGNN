---
layout: default
title: Personvernerklæring
nav_order: 95
permalink: /privacy-policy/
description: "Personvernerklæring for NOTxGNN: et statisk nettsted uten kontoer og skjemaer; det bruker analyseinformasjonskapsler fra Google Analytics 4 til bruksstatistikk."
---

# Personvernerklæring

<div class="key-takeaway">
Dette er et statisk nettsted — ingen registrering og ingen skjemaer. Det bruker analyseinformasjonskapsler fra Google Analytics 4 til å lage bruksstatistikk.
</div>

---

## Hva vi samler inn

<p class="key-answer" data-question="Samler NOTxGNN inn personopplysninger?">
<strong>Bare bruksstatistikk, via Google Analytics 4.</strong> Dette nettstedet driftes på GitHub Pages som et rent statisk
nettsted. Det finnes ikke noe kontosystem og ingen skjemaer, og vi samler ikke inn navn, e-postadresser eller
pasientjournaler. Nettstedet bruker analyseinformasjonskapsler fra Google Analytics 4 til å lage bruksstatistikk (viste
sider, henvisende nettsted, rulledybde og tid på siden). Informasjonskapslene settes når en side lastes inn; søkeord,
skjemainnhold og URL-spørreparametere sendes ikke.
</p>

---

## Tredjepartstjenester

Nettstedet bruker følgende tredjepartsressurser, som kan logge tilgang i henhold til sine egne
retningslinjer:

| Tjeneste | Formål | Personvernerklæring |
|---------|---------|----------------|
| GitHub Pages | Drift av nettstedet | [GitHub Privacy Statement](https://docs.github.com/site-policy/privacy-policies/github-privacy-statement) |
| Google Analytics 4 (www.googletagmanager.com, google-analytics.com) | Besøksstatistikk (viste sider, henvisende side); bruker analyseinformasjonskapsler. Søkeord, skjemainnhold og URL-parametere sendes ikke. | [Googles personvernregler](https://policies.google.com/privacy) |
| cdn.jsdelivr.net | Skriptbiblioteker: d3-diagrammer på alle sider; Fuse.js for navnesammenligning og SMART on FHIR-klienten på SMART-sidene | [jsDelivrs personvernerklæring](https://www.jsdelivr.com/terms/privacy-policy-jsdelivr-net) |
| clinicaltrials.gov | Søk etter kliniske studier på SMART-sidene: bare når du ber om det, sendes navnet på legemiddelet og indikasjonen til ClinicalTrials.gov-API-et | [NLMs nettretningslinjer](https://www.nlm.nih.gov/web_policies.html) |
| rxnav.nlm.nih.gov | SMART-appen: RxNorm-kodene for legemidlene som leses fra din elektroniske pasientjournal, sendes til NLMs RxNav-API for å slå opp virkestoffnavnet (ingen pasientidentifikatorer) | [NLMs nettretningslinjer](https://www.nlm.nih.gov/web_policies.html) |

Når du selv starter SMART on FHIR-appen, henter den legemiddeldata fra journalsystemet ditt.
Pasientens identitet og journaldata <strong>sendes ikke til serverne til dette nettstedet</strong> (det er et statisk
nettsted uten backend) og lagres ikke av nettstedet. For å matche legemiddelnavn sender appen legemidlenes
RxNorm-koder til RxNav-tjenesten hos det amerikanske National Library of Medicine; kodene inneholder ingen
opplysninger som identifiserer pasienten. Når du ber om kliniske studier, sendes legemiddelnavnet og indikasjonen
til ClinicalTrials.gov.

---

<!-- privacy-law:start（母目錄 .claude/gen_local_pages_20261119.py 產生，勿手改；法規與連結見 .claude/privacy_text_20261119.py）-->
## Gjeldende lovgivning

For besøkende i Norge gjelder [personopplysningsloven](https://lovdata.no/dokument/NL/lov/2018-06-15-38), som gjør personvernforordningen (GDPR) til norsk lov gjennom EØS-avtalen; for informasjonskapsler gjelder i tillegg ekomloven. Tilsynsmyndighet er [Datatilsynet](https://www.datatilsynet.no/). Den behandlingsansvarlige holder til i Taiwan; behandlingen gjelder bruksdataene Google Analytics 4 samler inn via informasjonskapsler.

## Dine rettigheter og hvordan du bruker dem

- Rett til innsyn (artikkel 15) og retting (artikkel 16).
- Rett til sletting (artikkel 17) og begrensning (artikkel 18).
- Rett til å protestere (artikkel 21), også mot webanalyse.
- Rett til å klage til Datatilsynet (artikkel 77).

Henvendelser: service@yao.care. Siden nettstedet ikke har kontoer, kan vi bare håndtere data hos Google Analytics hvis du gir oss nok opplysninger (f.eks. dato og sider for besøket); du kan også blokkere eller slette analysecookies i nettleseren.

## Opphavsrett og datakilder

Nettstedets tekster er vernet etter [åndsverkloven](https://lovdata.no/dokument/NL/lov/2018-06-15-40). Nettstedets kode er publisert under MIT-lisensen i [GitHub-repositoriet](https://github.com/yao-care/NOTxGNN); rapporttekstene er © 藥提醒科技有限公司 (yao.care).

Datakilder på dette nettstedet og vilkårene deres:

- **TxGNN**-prediksjonsdata (Harvard Dataverse): CC0 1.0 (frigitt til allmennheten); siter Huang et al., *Nature Medicine* 2024.
- **ClinicalTrials.gov** og **PubMed**: US National Library of Medicine; se [vilkårene for ClinicalTrials.gov](https://clinicaltrials.gov/about-site/terms-conditions) og [NCBIs retningslinjer](https://www.ncbi.nlm.nih.gov/home/about/policies/) (noen PubMed-sammendrag er fortsatt vernet av forlagets opphavsrett).
- **DrugBank**-ID-er og -data: etter [DrugBank](https://go.drugbank.com/)s lisensvilkår (ikke-kommersiell bruk).
- **Lokalt datasett**: [EMA Medicines report](https://www.ema.europa.eu/en/documents/report/medicines-output-medicines-report_en.xlsx), publisert av Det europeiske legemiddelkontoret (EMA); gjenbruk følger utgiverens vilkår, og dette nettstedet gir ingen ytterligere rettigheter.

<!-- privacy-law:end -->

---

## Endringer i denne erklæringen

Eventuelle endringer publiseres direkte på denne siden.

---

## Om utvikleren

Denne plattformen er utviklet og drives av **藥提醒科技有限公司** (yao.care). Opplysninger om selskapet,
bakgrunnen for TxGNN-modellen og alle nettstedene i produktlinjen finner du på siden <a href="{{ '/about/' | relative_url }}">Om</a>.

---

<div class="disclaimer">
<strong>Ansvarsfraskrivelse</strong><br>
Denne rapporten er kun ment som referanse for akademisk forskning og <strong>utgjør ikke medisinske råd</strong>. Følg alltid legens anvisninger; juster aldri medisineringen på egen hånd. Enhver beslutning om legemiddelreposisjonering krever fullstendig klinisk validering og regulatorisk gjennomgang.
<br><br>
<small>Gjennomgått av: 藥提醒科技有限公司 (yao.care)</small>
</div>
