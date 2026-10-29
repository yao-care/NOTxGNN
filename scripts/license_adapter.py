"""EMA 集中許可（DE、FI、NO、EU 四站共用；2026-10-30）。各站 license_adapters/<站>.py 是本檔的複本，推廣時一起複製。

來源：EMA medicines report（https://www.ema.europa.eu/en/documents/report/medicines-output-medicines-report_en.xlsx，免金鑰）。
表頭列含「EMA product number」「Medicine status」（前面有說明列，自動找表頭）。人用與獸用都取：
DE 的證據包混有獸用集中許可（EMEA/V/C，原本的資料問題，另案處理），狀態一樣要追。
證據包紀錄 license_id＝EMA product number（EMEA/H/C/xxxxxx）、status＝Medicine status 原文
（Authorised／Withdrawn／Lapsed／Expired／Revoked／Suspended／Refused…）；reviewer 依文字判定。新檔沒有的編號保留原狀態。
"""
import io
import time

import openpyxl
import requests

RAW_FILE = "raw/ema_medicine_status.json"
URL = "https://www.ema.europa.eu/en/documents/report/medicines-output-medicines-report_en.xlsx"


def fetch():
    for attempt in range(4):
        try:
            r = requests.get(URL, timeout=180, headers={"User-Agent": "Mozilla/5.0 (compatible; TxGNN/1.0; research)"})
            r.raise_for_status()
            break
        except Exception:
            if attempt == 3:
                raise
            time.sleep(15 * (attempt + 1))
    ws = openpyxl.load_workbook(io.BytesIO(r.content), read_only=True).active
    head, out = None, []
    for row in ws.iter_rows(values_only=True):
        if head is None:
            if row and "EMA product number" in row and "Medicine status" in row:
                head = list(row)
            continue
        rec = dict(zip(head, row))
        k = str(rec.get("EMA product number") or "").strip()
        if k:
            out.append({"ema": k, "status": str(rec.get("Medicine status") or "").strip()})
    if head is None:
        raise RuntimeError("找不到表頭（EMA product number／Medicine status）")
    return out


def validate(new, old):
    p = []
    if len(new) < 1500:
        p.append(f"只解析出 {len(new)} 筆，疑似格式改變")
    if sum(1 for r in new if not r["status"]) > 0.01 * max(1, len(new)):
        p.append("超過 1% 缺 Medicine status")
    if old and len(new) < 0.9 * len(old):
        p.append(f"筆數 {len(new)} 比上次 {len(old)} 少超過 10%")
    return p


def status_index(new):
    return {r["ema"]: r["status"] for r in new if r["status"]}


def record_id(rec):
    return str(rec.get("license_id") or "").strip()


def update(rec, new):
    if rec.get("status") == new:
        return False
    rec["status"] = new
    return True
