---
layout: default
title: Moderat evidens (L3-L4)
nav_order: 22
permalink: /evidence-medium/
description: "38 legemidler på evidensnivå L3–L4 på dette nettstedet (Norge), f.eks. Abatacept, Brentuximab Vedotin, Cilastatin, med viktigste predikerte indikasjon, sentrale EU-godkjenninger (EMA) og kontrollogg for hvert."
---

# Moderat evidens (L3-L4)

<!-- tier-facts:start（母目錄 .claude/gen_local_pages_20261119.py 產生，勿手改）-->
{% assign ev_share = site.data.evidence_tier_facts.medium.count | times: 100.0 | divided_by: site.data.drug_stats.total_drugs %}
Siden viser **{{ site.data.evidence_tier_facts.medium.count }}** av de **{{ site.data.drug_stats.total_drugs }}** legemidlene med publisert rapport på dette nettstedet ({{ site.data.evidence_tier_facts.medium.count | times: 100.0 | divided_by: site.data.drug_stats.total_drugs | round: 1 }} %): L3 **{{ site.data.evidence_tier_facts.medium.by_level.L3 }}**, L4 **{{ site.data.evidence_tier_facts.medium.by_level.L4 }}**.
Medianandel på L3–L4 på tvers av de 30 TxGNN-nettstedene: {{ site.data.evidence_tier_facts.medium.cross.median_share }} %. {% if ev_share > site.data.evidence_tier_facts.medium.cross.median_share %}Dette nettstedet ligger over medianen.{% elsif ev_share < site.data.evidence_tier_facts.medium.cross.median_share %}Dette nettstedet ligger under medianen.{% else %}Dette nettstedet ligger på medianen.{% endif %}

{% if site.data.evidence_tier_facts.medium.count > 0 %}
I de lokale dataene (sentrale EU-godkjenninger (EMA)) har **{{ site.data.evidence_tier_facts.medium.with_current }}** av disse legemidlene minst én gyldige oppføring, **{{ site.data.evidence_tier_facts.medium.none_current }}** har oppføringer, men ingen gyldige, og **{{ site.data.evidence_tier_facts.medium.without_data }}** finnes ikke i de lokale dataene. **{{ site.data.evidence_tier_facts.medium.with_reviews }}** har oppføringer i kontrolloggen (rettelser av godkjenningsopplysninger på legemiddelsiden). **{{ site.data.evidence_tier_facts.medium.cross.unique_drugs }}** har en predikert indikasjon som ingen andre TxGNN-nettsteder oppgir for samme legemiddel.
{% if site.data.evidence_tier_facts.medium.none_current_list.size > 0 %}

Med oppføringer, men ingen gyldige: {% for r in site.data.evidence_tier_facts.medium.none_current_list %}[{{ r.t }}]({{ r.u | relative_url }}){% unless forloop.last %}, {% endunless %}{% endfor %}.{% endif %}
{% endif %}

Definisjon av alle nivåene: [Metodikk]({{ '/methodology/' | relative_url }}).
<!-- tier-facts:end -->

<p style="font-size: 1.25rem; color: #666; margin-bottom: 1.5rem;">
Kandidater med foreløpig evidens som krever ytterligere validering
</p>

---

## Kriterier

| Nivå | Definisjon | Klinisk betydning |
|-------|------------|------------------|
| **L3** | Observasjonsstudier / store kasusserier | Foreløpig støtte; krever ytterligere validering |
| **L4** | Prekliniske / mekanistiske studier | Teoretisk støtte; langt fra klinisk bruk |

---

{% assign l3_drugs = site.drugs | where: "evidence_level", "L3" | where_exp: "d", "d.noindex != true" | sort: "title" %}
{% assign l4_drugs = site.drugs | where: "evidence_level", "L4" | where_exp: "d", "d.noindex != true" | sort: "title" %}

### L3 ({{ site.data.evidence_tier_facts.medium.by_level.L3 }} legemidler)

<!-- tier-table:start L3（母目錄 .claude/gen_local_pages_20261119.py 產生，勿手改）-->

| Legemiddel | Nivå | Viktigste predikerte nye indikasjon | sentrale EU-godkjenninger (EMA): gyldige / totalt | Kontrollogg | Bare på dette nettstedet |
|---|---|---|---|---|---|
{% for r in site.data.evidence_tier_facts.medium.rows %}{% if r.l == "L3" %}| [{{ r.t | replace: '|', '/' }}]({{ r.u | relative_url }}) | {{ r.l }} | {{ r.i | replace: '|', '/' }} | {% if r.lt %}{{ r.lv }} / {{ r.lt }}{% else %}—{% endif %} | {{ r.r }}{% if r.rs and r.rs != '' %}: {{ r.rs | replace: '|', '/' }}{% endif %} | {% if r.x and r.x > 0 %}ja ({{ r.x }}){% else %}—{% endif %} |
{% endif %}{% endfor %}

<!-- tier-table:end -->

### L4 ({{ site.data.evidence_tier_facts.medium.by_level.L4 }} legemidler)

<!-- tier-table:start L4（母目錄 .claude/gen_local_pages_20261119.py 產生，勿手改）-->

| Legemiddel | Nivå | Viktigste predikerte nye indikasjon | sentrale EU-godkjenninger (EMA): gyldige / totalt | Kontrollogg | Bare på dette nettstedet |
|---|---|---|---|---|---|
{% for r in site.data.evidence_tier_facts.medium.rows %}{% if r.l == "L4" %}| [{{ r.t | replace: '|', '/' }}]({{ r.u | relative_url }}) | {{ r.l }} | {{ r.i | replace: '|', '/' }} | {% if r.lt %}{{ r.lv }} / {{ r.lt }}{% else %}—{% endif %} | {{ r.r }}{% if r.rs and r.rs != '' %}: {{ r.rs | replace: '|', '/' }}{% endif %} | {% if r.x and r.x > 0 %}ja ({{ r.x }}){% else %}—{% endif %} |
{% endif %}{% endfor %}

<!-- tier-table:end -->

---

<div class="disclaimer">
<strong>Ansvarsfraskrivelse</strong><br>
Denne rapporten er kun ment som referanse for akademisk forskning og <strong>utgjør ikke medisinske råd</strong>. Følg alltid legens anvisninger; juster aldri medisineringen på egen hånd. Enhver beslutning om legemiddelreposisjonering krever fullstendig klinisk validering og regulatorisk gjennomgang.
<br><br>
<small>Gjennomgått av: 藥提醒科技有限公司 (yao.care)</small>
</div>
