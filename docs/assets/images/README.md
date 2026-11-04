---
sitemap: false
nav_exclude: true
---

# OG Image 說明

## 需要準備的檔案

### og-default.png

- **尺寸**: 1200 x 630 px
- **格式**: PNG 或 JPG
- **檔案大小**: < 1 MB

### 設計要求

1. 包含網站名稱「NOTxGNN」與網域
2. 包含該站語言的一行副標（取自 _config.yml 的 title）
3. 不放藥物數、候選數等數字（會過期）
4. 簡潔、專業風格
5. 適合在社群媒體預覽顯示

### 產生方式

由 TxGNN 母 repo 的 `.claude/gen_og_image.py` 產生（同時輸出 og-default.svg）。

### 使用位置

此圖片會作為網站在社群媒體分享時的預設預覽圖。
