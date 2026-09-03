---
layout: default
title: Lumacaftor
parent: 僅模型預測 (L5)
nav_order: 218
evidence_level: L5
indication_count: 1
---

# Lumacaftor
{: .fs-9 }

證據等級: **L5** | 預測適應症: **1** 個
{: .fs-6 .fw-300 }

---

## 目錄
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## 藥師評估報告

</div>

# Lumacaftor：從囊狀纖維化到痲瘋病

## 一句話摘要

Lumacaftor 是一種 CFTR 蛋白質摺疊校正劑，原用於治療囊狀纖維化（與 ivacaftor 併用，如 Orkambi，適用於 F508del-CFTR 突變患者）。
TxGNN 模型預測其可能對**痲瘋病（Leprosy）**有效，但目前**沒有臨床試驗、也沒有文獻**支持此方向，證據等級為最低的 L5。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原始適應症 | 囊狀纖維化（合併 ivacaftor 使用，如 Orkambi） |
| 預測新適應症 | 痲瘋病（Leprosy） |
| TxGNN 預測分數 | 99.44% |
| 證據等級 | L5（僅模型預測，無實際研究支持） |
| 台灣市場狀態 | 未上市 |
| 許可證數量 | 0 |
| 建議決策 | Hold（暫緩） |

---

## 為什麼這個預測合理性存疑？

Lumacaftor 官方 MOA 欄位標記為資料缺口（[Data Gap]），但根據已知藥理學資訊，Lumacaftor 是一種 CFTR 蛋白質摺疊校正劑（CFTR corrector），透過分子伴侶樣作用改善 F508del-CFTR 突變蛋白的細胞內運輸與功能，臨床上僅核准與 ivacaftor 併用（如 Orkambi）治療囊狀纖維化。

痲瘋病的病理機轉為 *Mycobacterium leprae* 感染引發之慢性肉芽腫性發炎與周邊神經損傷，目前並無已知證據顯示 CFTR 蛋白摺疊或氯離子通道功能與此病理過程存在生物學關聯。

TxGNN 給出的高分（0.994）較可能反映知識圖譜中的間接連結（例如藥物—基因—疾病共現路徑），而非具生物合理性的機轉假說。在缺乏任何支持性文獻或試驗的情況下，此預測的機轉合理性應被視為**存疑**，需要人工複核後才能決定是否進一步投入資源。

---

## 臨床試驗證據

目前無相關臨床試驗登記

---

## 文獻證據

目前無相關文獻資料

---

## 台灣市場資訊

該藥品目前**未於台灣上市**，無許可證記錄可供列出。

---

## 安全性考量

請參考仿單以獲取安全性資訊。

（註：仿單警語與禁忌事項目前為 Blocking 等級資料缺口，須先取得 TFDA 官方仿單內容，才能進行 S1 安全性初評。）

---

## 結論與下一步

**決策：Hold（暫緩）**

**理由：**
TxGNN 預測分數雖高，但完全缺乏臨床試驗與文獻支持（L5），且機轉層面（CFTR 蛋白摺疊校正 vs. 分枝桿菌感染性肉芽腫疾病）無已知生物學關聯，機轉合理性存疑。此外，仿單警語與禁忌事項仍為 Blocking 等級資料缺口，尚無法進行安全性初評。

**若要繼續推進，需要補齊：**
- TFDA 官方仿單警語／禁忌（DG001，Blocking，須下載並解析）
- DrugBank 完整 MOA 資料以確認機轉關聯性（DG002，High）
- 針對 CFTR 調節劑是否具抗分枝桿菌或免疫調節作用的臨床前機轉研究
- 機轉合理性人工複核結果，作為是否進入下一階段（S1）的判斷依據
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

