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

## Den registrertes rettigheter

Dette nettstedet har ingen kontoer og lagrer ingen personopplysninger på egne servere (det har ingen).
Bruksstatistikken samles inn av Google Analytics 4; du kan blokkere eller slette informasjonskapslene i
nettleserinnstillingene.
Har du spørsmål om denne erklæringen, kontakt service@yao.care.

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
