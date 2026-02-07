from dataclasses import dataclass
from datetime import datetime
from typing import Optional


@dataclass
class ScrapeJob:
    source: str
    status: str
    last_run: Optional[datetime] = None
