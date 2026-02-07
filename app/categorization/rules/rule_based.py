from typing import Dict


class RuleBasedCategorizer:
    def __init__(self, keyword_map: Dict[str, str]) -> None:
        self._keyword_map = keyword_map

    def classify(self, product_name: str) -> str:
        name = product_name.lower()
        for keyword, category in self._keyword_map.items():
            if keyword in name:
                return category
        return "uncategorized"
