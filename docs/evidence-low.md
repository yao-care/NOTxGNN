---
layout: default
title: Kun modellprediksjon (L5)
nav_order: 23
permalink: /evidence-low/
description: "368 legemidler på evidensnivå L5 på dette nettstedet (Norge), f.eks. Denosumab, Metformin, Emtricitabine, med viktigste predikerte indikasjon, sentrale EU-godkjenninger (EMA) og kontrollogg for hvert."
---

# Kun modellprediksjon (L5)

<!-- tier-facts:start（母目錄 .claude/gen_local_pages_20261119.py 產生，勿手改）-->
{% assign ev_share = site.data.evidence_tier_facts.low.count | times: 100.0 | divided_by: site.data.drug_stats.total_drugs %}
Siden viser **{{ site.data.evidence_tier_facts.low.count }}** av de **{{ site.data.drug_stats.total_drugs }}** legemidlene med publisert rapport på dette nettstedet ({{ site.data.evidence_tier_facts.low.count | times: 100.0 | divided_by: site.data.drug_stats.total_drugs | round: 1 }} %): L5 **{{ site.data.evidence_tier_facts.low.by_level.L5 }}**.
Medianandel på L5 på tvers av de 30 TxGNN-nettstedene: {{ site.data.evidence_tier_facts.low.cross.median_share }} %. {% if ev_share > site.data.evidence_tier_facts.low.cross.median_share %}Dette nettstedet ligger over medianen.{% elsif ev_share < site.data.evidence_tier_facts.low.cross.median_share %}Dette nettstedet ligger under medianen.{% else %}Dette nettstedet ligger på medianen.{% endif %}

{% if site.data.evidence_tier_facts.low.count > 0 %}
I de lokale dataene (sentrale EU-godkjenninger (EMA)) har **{{ site.data.evidence_tier_facts.low.with_current }}** av disse legemidlene minst én gyldige oppføring, **{{ site.data.evidence_tier_facts.low.none_current }}** har oppføringer, men ingen gyldige, og **{{ site.data.evidence_tier_facts.low.without_data }}** finnes ikke i de lokale dataene. **{{ site.data.evidence_tier_facts.low.with_reviews }}** har oppføringer i kontrolloggen (rettelser av godkjenningsopplysninger på legemiddelsiden). **{{ site.data.evidence_tier_facts.low.cross.unique_drugs }}** har en predikert indikasjon som ingen andre TxGNN-nettsteder oppgir for samme legemiddel.
{% if site.data.evidence_tier_facts.low.none_current_list.size > 0 %}

Med oppføringer, men ingen gyldige: {% for r in site.data.evidence_tier_facts.low.none_current_list %}[{{ r.t }}]({{ r.u | relative_url }}){% unless forloop.last %}, {% endunless %}{% endfor %}.{% endif %}

Legemidler med en gyldige lokal oppføring vises først.
{% endif %}

Definisjon av alle nivåene: [Metodikk]({{ '/methodology/' | relative_url }}).
<!-- tier-facts:end -->

<p style="font-size: 1.25rem; color: #666; margin-bottom: 1.5rem;">
Kandidater med kun modellprediksjon og uten evidens fra mennesker så langt
</p>

---

## Kriterier

| Nivå | Definisjon | Klinisk betydning |
|-------|------------|------------------|
| **L5** | Kun modellprediksjon | Hypotesestadiet; ingen human evidens ennå |

---

{% assign l5_drugs = site.drugs | where: "evidence_level", "L5" | where_exp: "d", "d.noindex != true" | sort: "title" %}

### L5 ({{ site.data.evidence_tier_facts.low.by_level.L5 }} legemidler)

<!-- tier-table:start L5（母目錄 .claude/gen_local_pages_20261119.py 產生，勿手改）-->

| Legemiddel | Nivå | Viktigste predikerte nye indikasjon | sentrale EU-godkjenninger (EMA): gyldige / totalt | Kontrollogg | Bare på dette nettstedet |
|---|---|---|---|---|---|
{% for r in site.data.evidence_tier_facts.low.rows %}{% if r.l == "L5" %}| [{{ r.t | replace: '|', '/' }}]({{ r.u | relative_url }}) | {{ r.l }} | {{ r.i | replace: '|', '/' }} | {% if r.lt %}{{ r.lv }} / {{ r.lt }}{% else %}—{% endif %} | {{ r.r }}{% if r.rs and r.rs != '' %}: {{ r.rs | replace: '|', '/' }}{% endif %} | {% if r.x and r.x > 0 %}ja ({{ r.x }}){% else %}—{% endif %} |
{% endif %}{% endfor %}

<!-- tier-table:end -->

---

<div class="disclaimer">
<strong>Ansvarsfraskrivelse</strong><br>
Denne rapporten er kun ment som referanse for akademisk forskning og <strong>utgjør ikke medisinske råd</strong>. Følg alltid legens anvisninger; juster aldri medisineringen på egen hånd. Enhver beslutning om legemiddelreposisjonering krever fullstendig klinisk validering og regulatorisk gjennomgang.
<br><br>
<small>Gjennomgått av: 藥提醒科技有限公司 (yao.care)</small>
</div>
