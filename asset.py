from dataclasses import dataclass, field
from __init__ import time_now


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
        self.registered_at = time_now
