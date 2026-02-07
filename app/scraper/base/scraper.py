from abc import ABC, abstractmethod
from typing import Iterable, Dict

from app.core.models import Product


class Scraper(ABC):
    @abstractmethod
    def fetch(self) -> Iterable[Dict]:
        raise NotImplementedError

    @abstractmethod
    def parse(self, raw: Dict) -> Dict:
        raise NotImplementedError

    @abstractmethod
    def normalize(self, parsed: Dict) -> Product:
        raise NotImplementedError
