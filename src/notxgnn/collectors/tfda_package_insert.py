"""Enhanced TFDA collector with package insert parsing."""

import json
import re
import time
from pathlib import Path
from typing import Any
from urllib.parse import quote

import httpx

from .base import BaseCollector, CollectorResult
from .tfda import TFDACollector


class TFDAPackageInsertCollector(BaseCollector):
    """Enhanced TFDA collector that fetches package insert details.

    Provides:
    - Basic TFDA license information (from TFDACollector)
    - Package insert details:
      - Warnings (警語)
      - Contraindications (禁忌)
      - Dosage and administration (用法用量)
      - Pregnancy/lactation (孕婦及哺乳)
      - Hepatic impairment (肝功能不全)
      - Renal impairment (腎功能不全)
      - Adverse reactions (不良反應)
      - Drug interactions (藥物交互作用)
    """

    source_name = "tfda_package_insert"

    def __init__(
        self,
        data_path: str | Path | None = None,
        cache_dir: str | Path | None = None,
        use_web: bool = True,
    ):
        """Initialize the collector.

        Args:
            data_path: Path to tw_fda_drugs.json
            cache_dir: Directory for caching package insert data
            use_web: Whether to fetch from web if not in cache
        """
        base_dir = Path(__file__).parent.parent.parent.parent / "data"

        # Initialize base TFDA collector
        self.tfda_collector = TFDACollector(data_path)

        if cache_dir is None:
            self.cache_dir = base_dir / "external" / "tfda_package_inserts"
        else:
            self.cache_dir = Path(cache_dir)

        self.use_web = use_web

    def _get_cache_path(self, license_id: str) -> Path:
        """Get cache file path for a license ID."""
        # Sanitize license ID for filename
        safe_id = re.sub(r'[^\w\-]', '_', license_id)
        return self.cache_dir / f"{safe_id}.json"

    def _load_from_cache(self, license_id: str) -> dict | None:
        """Load package insert data from cache."""
        cache_path = self._get_cache_path(license_id)
        if cache_path.exists():
            with open(cache_path, "r", encoding="utf-8") as f:
                return json.load(f)
        return None

    def _save_to_cache(self, license_id: str, data: dict) -> None:
        """Save package insert data to cache."""
        self.cache_dir.mkdir(parents=True, exist_ok=True)
        cache_path = self._get_cache_path(license_id)
        with open(cache_path, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2, ensure_ascii=False)

    def _fetch_package_insert(self, license_id: str) -> dict | None:
        """Fetch package insert from TFDA website.

        Args:
            license_id: Taiwan FDA license ID

        Returns:
            Dictionary with package insert information or None
        """
        # TFDA drug detail page
        # Example URL pattern - this may need adjustment based on actual TFDA website
        encoded_id = quote(license_id)

        # Try different TFDA URL patterns
        urls_to_try = [
            f"https://info.fda.gov.tw/MLMS/H0001D.aspx?LicId={encoded_id}",
            f"https://www.fda.gov.tw/MLMS/H0001D.aspx?LicId={encoded_id}",
        ]

        for url in urls_to_try:
            try:
                with httpx.Client(timeout=30.0, follow_redirects=True) as client:
                    response = client.get(url)
                    if response.status_code == 200:
                        html = response.text
                        data = self._parse_package_insert_html(html, license_id)
                        if data:
                            return data
            except Exception as e:
                continue

        return None

    def _parse_package_insert_html(self, html: str, license_id: str) -> dict | None:
        """Parse package insert information from HTML.

        Args:
            html: HTML content from TFDA page
            license_id: License ID for reference

        Returns:
            Dictionary with parsed information
        """
        data = {
            "license_id": license_id,
            "fetched_from_web": True,
        }

        # Parse sections - these patterns may need adjustment
        sections = {
            "warnings": [r"警語[：:]?\s*(.*?)(?=\n\n|禁忌|$)", r"注意事項[：:]?\s*(.*?)(?=\n\n|$)"],
            "contraindications": [r"禁忌[：:]?\s*(.*?)(?=\n\n|警語|$)"],
            "dosage": [r"用法用量[：:]?\s*(.*?)(?=\n\n|$)", r"劑量[：:]?\s*(.*?)(?=\n\n|$)"],
            "pregnancy": [r"孕婦[及與和]?哺乳[婦期]?[：:]?\s*(.*?)(?=\n\n|$)", r"懷孕[：:]?\s*(.*?)(?=\n\n|$)"],
            "hepatic_impairment": [r"肝功能[不全障礙]?[：:]?\s*(.*?)(?=\n\n|$)", r"肝臟[：:]?\s*(.*?)(?=\n\n|$)"],
            "renal_impairment": [r"腎功能[不全障礙]?[：:]?\s*(.*?)(?=\n\n|$)", r"腎臟[：:]?\s*(.*?)(?=\n\n|$)"],
            "adverse_reactions": [r"不良反應[：:]?\s*(.*?)(?=\n\n|$)", r"副作用[：:]?\s*(.*?)(?=\n\n|$)"],
            "drug_interactions": [r"藥物交互作用[：:]?\s*(.*?)(?=\n\n|$)", r"交互作用[：:]?\s*(.*?)(?=\n\n|$)"],
        }

        # Clean HTML and extract text
        text = self._clean_html(html)

        for section_name, patterns in sections.items():
            for pattern in patterns:
                match = re.search(pattern, text, re.IGNORECASE | re.DOTALL)
                if match:
                    content = match.group(1).strip()
                    if len(content) > 10:  # Minimum content length
                        data[section_name] = content
                        break

        # Check if we got any useful data
        useful_sections = [k for k in sections.keys() if k in data and data[k]]
        if not useful_sections:
            return None

        return data

    def _clean_html(self, html: str) -> str:
        """Clean HTML and extract text."""
        # Remove script and style
        text = re.sub(r'<script[^>]*>.*?</script>', '', html, flags=re.DOTALL | re.IGNORECASE)
        text = re.sub(r'<style[^>]*>.*?</style>', '', text, flags=re.DOTALL | re.IGNORECASE)
        # Remove HTML tags
        text = re.sub(r'<[^>]+>', '\n', text)
        # Decode HTML entities
        text = text.replace('&nbsp;', ' ')
        text = text.replace('&lt;', '<')
        text = text.replace('&gt;', '>')
        text = text.replace('&amp;', '&')
        # Normalize whitespace
        text = re.sub(r'\n\s*\n', '\n\n', text)
        text = re.sub(r' +', ' ', text)
        return text.strip()

    def search(self, drug: str, disease: str | None = None) -> CollectorResult:
        """Search for package insert data.

        Args:
            drug: Drug name
            disease: Optional disease filter

        Returns:
            CollectorResult with package insert data
        """
        query = {"drug": drug, "disease": disease}

        # First get basic TFDA info
        tfda_result = self.tfda_collector.search(drug, disease)

        if not tfda_result.success or not tfda_result.data.get("found"):
            return self._make_result(
                query=query,
                data={
                    "found": False,
                    "basic_info": tfda_result.data,
                    "package_insert": None,
                },
                success=True,
            )

        # Get license IDs from results
        records = tfda_result.data.get("records", [])
        if not records:
            return self._make_result(
                query=query,
                data={
                    "found": True,
                    "basic_info": tfda_result.data,
                    "package_insert": None,
                    "message": "No license records found",
                },
                success=True,
            )

        # Try to get package insert for the first active license
        package_insert = None
        license_id = None

        for record in records:
            license_id = record.get("license_id", "")
            status = record.get("status", "")

            # Skip cancelled licenses
            if "註銷" in status:
                continue

            # Try cache first
            package_insert = self._load_from_cache(license_id)

            if package_insert is None and self.use_web:
                # Fetch from web
                package_insert = self._fetch_package_insert(license_id)
                if package_insert:
                    self._save_to_cache(license_id, package_insert)
                    time.sleep(1)  # Rate limiting

            if package_insert:
                break

        # Create structured package insert data
        if package_insert:
            structured = {
                "license_id": license_id,
                "warnings": package_insert.get("warnings", "[未找到]"),
                "contraindications": package_insert.get("contraindications", "[未找到]"),
                "dosage": package_insert.get("dosage", "[未找到]"),
                "pregnancy_lactation": package_insert.get("pregnancy", "[未找到]"),
                "hepatic_impairment": package_insert.get("hepatic_impairment", "[未找到]"),
                "renal_impairment": package_insert.get("renal_impairment", "[未找到]"),
                "adverse_reactions": package_insert.get("adverse_reactions", "[未找到]"),
                "drug_interactions": package_insert.get("drug_interactions", "[未找到]"),
                "source": "tfda_package_insert",
            }
        else:
            structured = {
                "license_id": license_id,
                "warnings": "[未檢索]",
                "contraindications": "[未檢索]",
                "dosage": records[0].get("dosage", "[未檢索]") if records else "[未檢索]",
                "pregnancy_lactation": "[未檢索]",
                "hepatic_impairment": "[未檢索]",
                "renal_impairment": "[未檢索]",
                "adverse_reactions": "[未檢索]",
                "drug_interactions": "[未檢索]",
                "source": "tfda_basic_only",
                "message": "Package insert details not available",
            }

        return self._make_result(
            query=query,
            data={
                "found": True,
                "basic_info": tfda_result.data,
                "package_insert": structured,
            },
            success=True,
        )

    def get_package_insert(self, license_id: str) -> dict | None:
        """Get package insert for a specific license ID.

        Args:
            license_id: Taiwan FDA license ID

        Returns:
            Package insert data or None
        """
        # Try cache first
        data = self._load_from_cache(license_id)

        if data is None and self.use_web:
            data = self._fetch_package_insert(license_id)
            if data:
                self._save_to_cache(license_id, data)

        return data
