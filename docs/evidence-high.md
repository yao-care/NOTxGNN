---
layout: default
title: Høy evidens (L1-L2)
nav_order: 21
permalink: /evidence-high/
description: "26 legemidler på evidensnivå L1–L2 på dette nettstedet (Norge), f.eks. Bupropion, Clofarabine, Doxorubicin, med viktigste predikerte indikasjon, sentrale EU-godkjenninger (EMA) og kontrollogg for hvert."
---

# Høy evidens (L1-L2)

<!-- tier-facts:start（母目錄 .claude/gen_local_pages_20261119.py 產生，勿手改）-->
{% assign ev_share = site.data.evidence_tier_facts.high.count | times: 100.0 | divided_by: site.data.drug_stats.total_drugs %}
Siden viser **{{ site.data.evidence_tier_facts.high.count }}** av de **{{ site.data.drug_stats.total_drugs }}** legemidlene med publisert rapport på dette nettstedet ({{ site.data.evidence_tier_facts.high.count | times: 100.0 | divided_by: site.data.drug_stats.total_drugs | round: 1 }} %): L1 **{{ site.data.evidence_tier_facts.high.by_level.L1 }}**, L2 **{{ site.data.evidence_tier_facts.high.by_level.L2 }}**.
Medianandel på L1–L2 på tvers av de 30 TxGNN-nettstedene: {{ site.data.evidence_tier_facts.high.cross.median_share }} %. {% if ev_share > site.data.evidence_tier_facts.high.cross.median_share %}Dette nettstedet ligger over medianen.{% elsif ev_share < site.data.evidence_tier_facts.high.cross.median_share %}Dette nettstedet ligger under medianen.{% else %}Dette nettstedet ligger på medianen.{% endif %}

{% if site.data.evidence_tier_facts.high.count > 0 %}
I de lokale dataene (sentrale EU-godkjenninger (EMA)) har **{{ site.data.evidence_tier_facts.high.with_current }}** av disse legemidlene minst én gyldige oppføring, **{{ site.data.evidence_tier_facts.high.none_current }}** har oppføringer, men ingen gyldige, og **{{ site.data.evidence_tier_facts.high.without_data }}** finnes ikke i de lokale dataene. **{{ site.data.evidence_tier_facts.high.with_reviews }}** har oppføringer i kontrolloggen (rettelser av godkjenningsopplysninger på legemiddelsiden). **{{ site.data.evidence_tier_facts.high.cross.unique_drugs }}** har en predikert indikasjon som ingen andre TxGNN-nettsteder oppgir for samme legemiddel.
{% if site.data.evidence_tier_facts.high.none_current_list.size > 0 %}

Med oppføringer, men ingen gyldige: {% for r in site.data.evidence_tier_facts.high.none_current_list %}[{{ r.t }}]({{ r.u | relative_url }}){% unless forloop.last %}, {% endunless %}{% endfor %}.{% endif %}
{% endif %}

Definisjon av alle nivåene: [Metodikk]({{ '/methodology/' | relative_url }}).
<!-- tier-facts:end -->

<p style="font-size: 1.25rem; color: #666; margin-bottom: 1.5rem;">
Kandidater som kan prioriteres for klinisk evaluering
</p>

Hvilke av disse legemidlene har studieevidens for den predikerte nye indikasjonen, og hvor mange registrerte studier siteres? Se [Legemidler i Norge med evidens fra kliniske studier for en ny indikasjon]({{ '/clinical-trial-evidence/' | relative_url }}).

---

## Kriterier

| Nivå | Definisjon | Klinisk betydning |
|-------|------------|------------------|
| **L1** | Flere fase 3-RCT-er / systematiske oversikter | Sterk støtte; klinisk bruk kan vurderes |
| **L2** | Én enkelt RCT eller flere fase 2-studier | Moderat støtte; valideringsstudier kan utformes |

---

{% assign l1_drugs = site.drugs | where: "evidence_level", "L1" | where_exp: "d", "d.noindex != true" | sort: "title" %}
{% assign l2_drugs = site.drugs | where: "evidence_level", "L2" | where_exp: "d", "d.noindex != true" | sort: "title" %}

### L1 ({{ site.data.evidence_tier_facts.high.by_level.L1 }} legemidler)

<!-- tier-table:start L1（母目錄 .claude/gen_local_pages_20261119.py 產生，勿手改）-->

| Legemiddel | Nivå | Viktigste predikerte nye indikasjon | sentrale EU-godkjenninger (EMA): gyldige / totalt | Kontrollogg | Bare på dette nettstedet |
|---|---|---|---|---|---|
{% for r in site.data.evidence_tier_facts.high.rows %}{% if r.l == "L1" %}| [{{ r.t | replace: '|', '/' }}]({{ r.u | relative_url }}) | {{ r.l }} | {{ r.i | replace: '|', '/' }} | {% if r.lt %}{{ r.lv }} / {{ r.lt }}{% else %}—{% endif %} | {{ r.r }}{% if r.rs and r.rs != '' %}: {{ r.rs | replace: '|', '/' }}{% endif %} | {% if r.x and r.x > 0 %}ja ({{ r.x }}){% else %}—{% endif %} |
{% endif %}{% endfor %}

<!-- tier-table:end -->

### L2 ({{ site.data.evidence_tier_facts.high.by_level.L2 }} legemidler)

<!-- tier-table:start L2（母目錄 .claude/gen_local_pages_20261119.py 產生，勿手改）-->

| Legemiddel | Nivå | Viktigste predikerte nye indikasjon | sentrale EU-godkjenninger (EMA): gyldige / totalt | Kontrollogg | Bare på dette nettstedet |
|---|---|---|---|---|---|
{% for r in site.data.evidence_tier_facts.high.rows %}{% if r.l == "L2" %}| [{{ r.t | replace: '|', '/' }}]({{ r.u | relative_url }}) | {{ r.l }} | {{ r.i | replace: '|', '/' }} | {% if r.lt %}{{ r.lv }} / {{ r.lt }}{% else %}—{% endif %} | {{ r.r }}{% if r.rs and r.rs != '' %}: {{ r.rs | replace: '|', '/' }}{% endif %} | {% if r.x and r.x > 0 %}ja ({{ r.x }}){% else %}—{% endif %} |
{% endif %}{% endfor %}

<!-- tier-table:end -->

---

<div class="disclaimer">
<strong>Ansvarsfraskrivelse</strong><br>
Denne rapporten er kun ment som referanse for akademisk forskning og <strong>utgjør ikke medisinske råd</strong>. Følg alltid legens anvisninger; juster aldri medisineringen på egen hånd. Enhver beslutning om legemiddelreposisjonering krever fullstendig klinisk validering og regulatorisk gjennomgang.
<br><br>
<small>Gjennomgått av: 藥提醒科技有限公司 (yao.care)</small>
</div>
