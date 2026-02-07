from typing import Dict, List

from app.core.models import Product


class FilterEngine:
    def apply_filters(self, products: List[Product], criteria: Dict) -> List[Product]:
        filtered = products

        category = criteria.get("category")
        if category:
            filtered = [p for p in filtered if p.category_id == category]

        price_min = criteria.get("price_min")
        if price_min is not None:
            filtered = [p for p in filtered if p.price >= price_min]

        price_max = criteria.get("price_max")
        if price_max is not None:
            filtered = [p for p in filtered if p.price <= price_max]

        brand = criteria.get("brand")
        if brand:
            filtered = [p for p in filtered if p.attributes.get("brand") == brand]

        return filtered
