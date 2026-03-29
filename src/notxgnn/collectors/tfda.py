"""TFDA collector - fetches Taiwan FDA drug data."""

import json
from pathlib import Path
from typing import Any

from .base import BaseCollector, CollectorResult


class TFDACollector(BaseCollector):
    """Collector for Taiwan FDA (TFDA) drug data.

    Reads from local tw_fda_drugs.json file that was processed
    from the FDA open data.
    """

    source_name = "tfda"

    def __init__(self, data_path: str | Path | None = None):
        """Initialize the collector.

        Args:
            data_path: Path to tw_fda_drugs.json file.
                      Defaults to data/raw/tw_fda_drugs.json
        """
        if data_path is None:
            self.data_path = (
                Path(__file__).parent.parent.parent.parent
                / "data"
                / "raw"
                / "tw_fda_drugs.json"
            )
        else:
            self.data_path = Path(data_path)

        self._data: list[dict] | None = None

    def _load_data(self) -> list[dict]:
        """Load FDA data from JSON file."""
        if self._data is not None:
            return self._data

        if not self.data_path.exists():
            self._data = []
            return self._data

        with open(self.data_path, "r", encoding="utf-8") as f:
            self._data = json.load(f)

        return self._data

    def search(self, drug: str, disease: str | None = None) -> CollectorResult:
        """Search for TFDA records matching a drug name.

        Args:
            drug: Drug name (INN or brand name, Chinese or English)
            disease: Disease/indication name (used for filtering if provided)

        Returns:
            CollectorResult with TFDA data
        """
        query = {"drug": drug, "disease": disease}

        try:
            data = self._load_data()

            # Search for matching records
            matches = self._find_matches(drug, data)

            # If disease is provided, further filter by indication
            if disease and matches:
                matches = self._filter_by_indication(matches, disease)

            # Format the result
            result = self._format_result(matches)

            return self._make_result(
                query=query,
                data=result,
                success=True,
            )

        except Exception as e:
            return self._make_result(
                query=query,
                data={"found": False, "records": []},
                success=False,
                error_message=str(e),
            )

    def _find_matches(self, drug: str, data: list[dict]) -> list[dict]:
        """Find records matching the drug name.

        Args:
            drug: Drug name to search for
            data: List of FDA records

        Returns:
            List of matching records
        """
        drug_lower = drug.lower()
        matches = []

        for record in data:
            # Check various name fields
            fields_to_check = [
                record.get("中文品名", ""),
                record.get("英文品名", ""),
                record.get("主成分略述", ""),
                record.get("適應症", ""),
            ]

            for field in fields_to_check:
                if field and drug_lower in field.lower():
                    matches.append(record)
                    break

        return matches

    def _filter_by_indication(
        self, records: list[dict], disease: str
    ) -> list[dict]:
        """Filter records by indication/disease.

        Args:
            records: List of FDA records
            disease: Disease/indication to filter by

        Returns:
            Filtered list of records
        """
        disease_lower = disease.lower()
        filtered = []

        for record in records:
            indication = record.get("適應症", "").lower()
            if disease_lower in indication:
                filtered.append(record)

        # If no matches with indication filter, return original
        return filtered if filtered else records

    def _format_result(self, records: list[dict]) -> dict:
        """Format the result for the bundle.

        Args:
            records: List of matching FDA records

        Returns:
            Formatted result dictionary
        """
        if not records:
            return {"found": False, "records": []}

        formatted_records = []
        for record in records[:20]:  # Limit to 20 records
            formatted = {
                "license_id": record.get("許可證字號", ""),
                "brand_name_zh": record.get("中文品名", ""),
                "brand_name_en": record.get("英文品名", ""),
                "ingredients": record.get("主成分略述", ""),
                "indication": record.get("適應症", ""),
                "dosage_form": record.get("劑型", ""),
                "manufacturer": record.get("製造廠名稱", ""),
                "license_holder": record.get("申請商名稱", ""),
                "approval_date": record.get("發證日期", ""),
                "expiry_date": record.get("有效日期", ""),
                "status": record.get("註銷狀態", ""),
            }
            formatted_records.append(formatted)

        # Create package insert summary from first record
        first_record = records[0]
        package_insert = {
            "warnings": [],  # Would need additional data source
            "contraindications": [],
            "dosage": first_record.get("用法用量", ""),
            "special_populations": [],
        }

        return {
            "found": True,
            "records": formatted_records,
            "total_matches": len(records),
            "package_insert": package_insert,
        }

    def get_by_license_id(self, license_id: str) -> dict | None:
        """Get a specific record by license ID.

        Args:
            license_id: Taiwan FDA license ID (e.g., "衛部藥製字第000001號")

        Returns:
            Record dictionary or None if not found
        """
        data = self._load_data()

        for record in data:
            if record.get("許可證字號") == license_id:
                return record

        return None
