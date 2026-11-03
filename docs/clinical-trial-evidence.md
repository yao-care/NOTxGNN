---
layout: default
title: "Legemidler med studieevidens for en ny indikasjon"
nav_order: 25
permalink: /clinical-trial-evidence/
description: "Sentralt godkjente EU-legemidler (EMA) der den nye indikasjonen TxGNN har predikert, har evidens fra kliniske studier (L1-L2): indikasjon, nivå, studier."
last_modified_at: 2026-11-03
---
{%- comment -%}
2026-11-03：回答 AI 搜尋常問的「本國藥物中，哪些新適應症有臨床試驗證據」。全表由 Liquid 從藥物頁產生，不寫死藥名或數字。
收錄＝公開藥物頁（排除 id_redirect 與 noindex）中 evidence_level 為 L1 或 L2（本站 evidence-high 標準：L1 多個 Phase 3 RCT／系統性回顧，
L2 單一 RCT 或多個 Phase 2 試驗）。預測新適應症與等級註記取自各藥物頁快速總覽表；下列欄名是本站藥物頁實際用到的寫法（建頁時逐頁核對），
新寫法抓不到時顯示「se rapporten」、等級仍取 front matter。試驗數＝該藥物頁引用的不重複 NCT 編號數。
{%- endcomment -%}
{%- assign ind_labels = "Predikert ny indikasjon|Foreslått ny indikasjon|Forutsagt ny indikasjon" | split: "|" -%}
{%- assign lev_labels = "Evidensnivå" | split: "|" -%}
{%- assign listed = site.drugs | where_exp: "d", "d.layout != 'id_redirect'" | where_exp: "d", "d.noindex != true" -%}
{%- assign l1 = listed | where: "evidence_level", "L1" | sort: "title" -%}
{%- assign l2 = listed | where: "evidence_level", "L2" | sort: "title" -%}
{%- assign trial_drugs = l1 | concat: l2 -%}
{%- assign latest = trial_drugs | sort: "last_modified_at" | last -%}
{%- assign latest_date = latest.last_modified_at | date: "%Y-%m-%d" -%}

# Legemidler i Norge med evidens fra kliniske studier for en ny indikasjon

<p class="key-answer" data-question="Hvilke legemidler i Norge har evidens fra kliniske studier for en ny indikasjon?">
<strong>{{ trial_drugs.size }}</strong> av de {{ listed.size }} legemidlene med en NOTxGNN-rapport har en ny indikasjon predikert av TxGNN med evidensnivå <strong>L1 eller L2</strong> ({{ l1.size }} på L1, {{ l2.size }} på L2), altså er det funnet evidens fra kliniske studier (randomiserte studier, fase 2–3-studier eller systematiske oversikter).
</p>

Legemidlene kommer fra sentrale markedsføringstillatelser i EU i [EMA Medicines report](https://www.ema.europa.eu/en/documents/report/medicines-output-medicines-report_en.xlsx) (gjelder også i Norge; status vises i hver rapport); listen gjenspeiler legemiddelrapportene sist oppdatert {{ latest_date }}.

<div class="key-takeaway">
Studieevidens for en predikert indikasjon er ikke bevis for effekt. Alle kandidatene nedenfor <strong>krever fortsatt klinisk validering</strong> og myndighetsvurdering før klinisk bruk.
</div>

---

## Legemidler med studieevidens (L1–L2)

<div class="table-wrapper"><table>
<thead>
<tr><th>Legemiddel</th><th>Predikert ny indikasjon</th><th>Evidensnivå</th><th>Siterte registrerte studier (NCT)</th></tr>
</thead>
<tbody>
{%- for drug in trial_drugs -%}
{%- assign indication = "" -%}
{%- for lab in ind_labels -%}{%- if indication == "" -%}{%- assign needle = "<td>" | append: lab | append: "</td>" -%}{%- assign qo = drug.content | split: needle -%}{%- if qo.size > 1 -%}{%- assign indication = qo[1] | split: "</td>" | first | split: "<td>" | last | strip -%}{%- endif -%}{%- endif -%}{%- endfor -%}
{%- assign level_cell = "" -%}
{%- for lab in lev_labels -%}{%- if level_cell == "" -%}{%- assign needle = "<td>" | append: lab | append: "</td>" -%}{%- assign lv = drug.content | split: needle -%}{%- if lv.size > 1 -%}{%- assign level_cell = lv[1] | split: "</td>" | first | split: "<td>" | last | strip -%}{%- endif -%}{%- endif -%}{%- endfor -%}
{%- assign parts = drug.content | split: "NCT" -%}
{%- capture nct_ids -%}{%- for p in parts offset: 1 -%}{%- assign id = p | slice: 0, 8 -%}{%- assign rest = id | remove: "0" | remove: "1" | remove: "2" | remove: "3" | remove: "4" | remove: "5" | remove: "6" | remove: "7" | remove: "8" | remove: "9" -%}{%- if id.size == 8 and rest == "" -%}{{ id }},{%- endif -%}{%- endfor -%}{%- endcapture -%}
{%- assign nct_count = nct_ids | split: "," | uniq | size %}
<tr><td><a href="{{ drug.url | relative_url }}">{{ drug.title }}</a></td><td>{% if indication != "" %}{{ indication }}{% else %}se rapporten{% endif %}</td><td>{{ drug.evidence_level }}{% if level_cell != "" and level_cell != drug.evidence_level %} <a href="{{ drug.url | relative_url }}" title="{{ level_cell | strip_html | escape }}">(med forbehold)</a>{% endif %}</td><td>{{ nct_count }}</td></tr>
{%- endfor %}
</tbody>
</table></div>

## Slik leser du listen

- **Evidensnivå** følger nettstedets [kriterier]({{ '/evidence-high/' | relative_url }}): L1 = Flere fase 3-RCT-er / systematiske oversikter; L2 = Én enkelt RCT eller flere fase 2-studier. «(med forbehold)» betyr at rapporten tar forbehold om nivået; les merknaden i rapporten før du legger vekt på det.
- **Predikert ny indikasjon** er hovedprediksjonen i hver rapport. Indikasjoner og kontraindikasjoner som allerede er registrert i TxGNN-kunnskapsgrafen, er utelatt, men enkelte prediksjoner kan likevel overlappe en etablert bruk; rapporten forklarer dette der det er aktuelt.
- **Siterte registrerte studier** teller ClinicalTrials.gov-numrene (NCT) som siteres i rapporten. Rapportene siterer et utvalg av studiene som ble funnet; 0 betyr at rapporten ikke siterer noen registrert studie, og avsnittet om litteraturevidens viser grunnlaget for nivået.
- Se alle nivåer og hele metoden under [Høy evidens (L1-L2)]({{ '/evidence-high/' | relative_url }}), [Alle legemidler]({{ '/drugs/' | relative_url }}) og [metode]({{ '/methodology/' | relative_url }}).

---

<div class="disclaimer">
<strong>Ansvarsfraskrivelse</strong><br>
Denne rapporten er kun ment som referanse for akademisk forskning og <strong>utgjør ikke medisinske råd</strong>. Følg alltid legens anvisninger; juster aldri medisineringen på egen hånd. Enhver beslutning om legemiddelreposisjonering krever fullstendig klinisk validering og regulatorisk gjennomgang.
<br><br>
<small>Gjennomgått av: 藥提醒科技有限公司 (yao.care)</small>
</div>
