from typing import Iterable, Dict

from app.core.models import Product
from app.scraper.base.scraper import Scraper


class EbayScraper(Scraper):
    def fetch(self) -> Iterable[Dict]:
        return []

    def parse(self, raw: Dict) -> Dict:
        return raw

    def normalize(self, parsed: Dict) -> Product:
        return Product(
            id=parsed.get("id", ""),
            name=parsed.get("name", ""),
            description=parsed.get("description", ""),
            price=float(parsed.get("price", 0)),
            category_id=None,
            attributes=parsed.get("attributes", {}),
            source="ebay",
        )
