from dataclasses import dataclass, field
from datetime import datetime, timedelta, timezone


@dataclass
class Asset:

    title: str
    asset_id: str = field(init=False)
    asin: str
    url: str
    images: list
    manufacture: str
    contributor: str
    product_group: str
    publication_date: str
    features: str
    default_position: str
    current_position: str
    note: str
    registrant_name: str
    registered_at: str = field(init=False)

    def __post_init__(self):
        self.asset_id = "0"
        self.registered_at = datetime.now(timezone.utc).astimezone(timezone(timedelta(hours=+9))).isoformat()
