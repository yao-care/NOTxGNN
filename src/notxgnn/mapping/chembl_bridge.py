#!/usr/bin/env python3
"""ChEMBL 橋接模組

使用 ChEMBL API 或本地 SQLite 資料庫補充藥物映射。
ChEMBL 包含核准藥物的生物活性資料。

API 文件：https://www.ebi.ac.uk/chembl/api/data/docs
"""

import json
import logging
import sqlite3
import time
from pathlib import Path
from typing import Dict, List, Optional, Set

import requests

logger = logging.getLogger(__name__)

# ChEMBL API 基礎 URL
CHEMBL_API_URL = "https://www.ebi.ac.uk/chembl/api/data"

# 快取檔案路徑
CACHE_FILE = Path(__file__).parent.parent.parent.parent / "data" / "external" / "chembl_cache.json"

# 本地 SQLite 資料庫路徑（選用）
SQLITE_DB_PATH = Path(__file__).parent.parent.parent.parent / "data" / "external" / "chembl_35.db"


class ChEMBLBridge:
    """ChEMBL 橋接器

    支援 API 查詢和本地 SQLite 資料庫兩種模式。
    """

    def __init__(
        self,
        cache_file: Optional[Path] = None,
        sqlite_db: Optional[Path] = None,
        use_sqlite: bool = False
    ):
        """初始化橋接器

        Args:
            cache_file: API 快取檔案路徑
            sqlite_db: SQLite 資料庫路徑
            use_sqlite: 是否使用本地 SQLite 資料庫
        """
        self.cache_file = cache_file or CACHE_FILE
        self.sqlite_db = sqlite_db or SQLITE_DB_PATH
        self.use_sqlite = use_sqlite and self.sqlite_db.exists()
        self.cache: Dict[str, dict] = {}
        self.conn: Optional[sqlite3.Connection] = None
        self.request_count = 0
        self.last_request_time = 0.0

        self._load_cache()

        if self.use_sqlite:
            self._connect_db()
            logger.info(f"Using local ChEMBL SQLite database: {self.sqlite_db}")
        else:
            logger.info("Using ChEMBL API")

    def _load_cache(self):
        """載入 API 快取"""
        if self.cache_file.exists():
            try:
                with open(self.cache_file, "r", encoding="utf-8") as f:
                    self.cache = json.load(f)
                logger.info(f"Loaded {len(self.cache)} cached ChEMBL entries")
            except (json.JSONDecodeError, IOError) as e:
                logger.warning(f"Failed to load cache: {e}")
                self.cache = {}

    def _save_cache(self):
        """儲存 API 快取"""
        self.cache_file.parent.mkdir(parents=True, exist_ok=True)
        with open(self.cache_file, "w", encoding="utf-8") as f:
            json.dump(self.cache, f, ensure_ascii=False, indent=2)

    def _connect_db(self):
        """連接 SQLite 資料庫"""
        if self.sqlite_db.exists():
            self.conn = sqlite3.connect(str(self.sqlite_db))
            self.conn.row_factory = sqlite3.Row

    def _rate_limit(self):
        """API 速率限制"""
        current_time = time.time()
        elapsed = current_time - self.last_request_time
        if elapsed < 0.1:  # 100ms 間隔
            time.sleep(0.1 - elapsed)
        self.last_request_time = time.time()

    def _api_request(self, endpoint: str, params: Optional[dict] = None) -> Optional[dict]:
        """發送 API 請求

        Args:
            endpoint: API 端點
            params: 查詢參數

        Returns:
            JSON 回應
        """
        self._rate_limit()
        url = f"{CHEMBL_API_URL}/{endpoint}"

        if params is None:
            params = {}
        params["format"] = "json"

        try:
            response = requests.get(url, params=params, timeout=10)
            self.request_count += 1

            if response.status_code == 200:
                return response.json()
            else:
                logger.debug(f"API request failed: {response.status_code}")
                return None
        except requests.RequestException as e:
            logger.warning(f"API request error: {e}")
            return None

    def search_molecule(self, name: str) -> Optional[dict]:
        """搜尋分子

        Args:
            name: 藥物名稱

        Returns:
            分子資訊字典
        """
        name_upper = name.upper().strip()
        cache_key = f"molecule:{name_upper}"

        # 檢查快取
        if cache_key in self.cache:
            return self.cache[cache_key]

        result = None

        if self.use_sqlite and self.conn:
            # 使用 SQLite 查詢
            cursor = self.conn.execute("""
                SELECT chembl_id, pref_name, max_phase
                FROM molecule_dictionary
                WHERE UPPER(pref_name) = ?
                LIMIT 1
            """, (name_upper,))
            row = cursor.fetchone()
            if row:
                result = {
                    "chembl_id": row["chembl_id"],
                    "pref_name": row["pref_name"],
                    "max_phase": row["max_phase"],
                }
        else:
            # 使用 API 查詢
            data = self._api_request("molecule/search", {"q": name})
            if data and data.get("molecules"):
                mol = data["molecules"][0]
                result = {
                    "chembl_id": mol.get("molecule_chembl_id"),
                    "pref_name": mol.get("pref_name"),
                    "max_phase": mol.get("max_phase"),
                }

        # 儲存到快取
        self.cache[cache_key] = result
        return result

    def get_synonyms(self, chembl_id: str) -> List[str]:
        """取得分子的同義詞

        Args:
            chembl_id: ChEMBL ID

        Returns:
            同義詞列表
        """
        cache_key = f"synonyms:{chembl_id}"

        # 檢查快取
        if cache_key in self.cache:
            return self.cache[cache_key].get("synonyms", [])

        synonyms = []

        if self.use_sqlite and self.conn:
            # 使用 SQLite 查詢
            cursor = self.conn.execute("""
                SELECT DISTINCT ms.synonyms
                FROM molecule_dictionary md
                JOIN molecule_synonyms ms ON md.molregno = ms.molregno
                WHERE md.chembl_id = ?
            """, (chembl_id,))
            for row in cursor:
                if row["synonyms"]:
                    synonyms.append(row["synonyms"].upper())
        else:
            # 使用 API 查詢
            data = self._api_request(f"molecule/{chembl_id}")
            if data and data.get("molecule_synonyms"):
                for syn in data["molecule_synonyms"]:
                    if syn.get("molecule_synonym"):
                        synonyms.append(syn["molecule_synonym"].upper())

        # 儲存到快取
        self.cache[cache_key] = {"synonyms": synonyms}
        return synonyms

    def find_drugbank_candidates(
        self,
        name: str,
        drugbank_names: Set[str]
    ) -> Optional[str]:
        """透過 ChEMBL 尋找可能的 DrugBank 映射

        Args:
            name: 原始成分名稱
            drugbank_names: DrugBank 中所有藥物名稱（大寫）

        Returns:
            匹配的 DrugBank 名稱，若無則回傳 None
        """
        # 先搜尋分子
        mol = self.search_molecule(name)
        if not mol or not mol.get("chembl_id"):
            return None

        # 取得同義詞
        synonyms = self.get_synonyms(mol["chembl_id"])

        # 加入 pref_name
        if mol.get("pref_name"):
            synonyms.append(mol["pref_name"].upper())

        # 找匹配
        for synonym in synonyms:
            if synonym in drugbank_names:
                return synonym

        return None

    def save(self):
        """儲存快取"""
        self._save_cache()
        logger.info(f"Saved {len(self.cache)} ChEMBL cache entries")

    def close(self):
        """關閉資料庫連線"""
        if self.conn:
            self.conn.close()


def download_chembl_sqlite():
    """下載 ChEMBL SQLite 資料庫

    注意：檔案約 5 GB，需要足夠的磁碟空間和下載時間。
    """
    try:
        from chembl_downloader import download_extract_sqlite
        print("開始下載 ChEMBL SQLite 資料庫...")
        print("注意：檔案約 5 GB，請耐心等待")
        path = download_extract_sqlite()
        print(f"下載完成：{path}")
        return path
    except ImportError:
        print("請先安裝 chembl-downloader：uv add chembl-downloader")
        return None


if __name__ == "__main__":
    # 測試範例
    logging.basicConfig(level=logging.INFO)

    bridge = ChEMBLBridge()

    # 測試幾個藥物
    test_names = [
        "ISOCONAZOLE",
        "METAPROTERENOL",
        "SILYMARIN",
        "BERBERINE",
    ]

    for name in test_names:
        print(f"\n=== {name} ===")
        mol = bridge.search_molecule(name)
        if mol:
            print(f"ChEMBL ID: {mol.get('chembl_id')}")
            print(f"Pref Name: {mol.get('pref_name')}")
            print(f"Max Phase: {mol.get('max_phase')}")
            if mol.get("chembl_id"):
                synonyms = bridge.get_synonyms(mol["chembl_id"])
                print(f"Synonyms (top 5): {synonyms[:5]}")
        else:
            print("Not found")

    bridge.save()
    bridge.close()
