import pytest

from airtable_client import AirtableClient

airtable_dictionary = {
    "title": "PlayStation 5 (CFI-1000A01)",
    "asin": "B08GGGBKRQ",
    "url": "https://www.amazon.co.jp/ソニー・インタラクティブエンタテインメント-PlayStation-5-CFI-1000A01/dp/B08GGGBKRQ/",
    "images":
        [
            {
                "url": "https://images-na.ssl-images-amazon.com/images/I/61YYOeZy9aL._AC_SL1500_.jpg"
            }
        ],
    "manufacture": "ソニー・インタラクティブエンタテインメント",
    "contributor": "None",
    "product_group": "Video game",
    "publication_date": "2020-11-18T23:00+09:00",
    "features": "圧巻のスピード:統合I/O(Integrated I/O)により、カスタムされたCPU・GPU・SSDがその力を発揮。",
    "default_position": "渡邉宅",
    "current_position": "渡邉宅",
    "note": "リモートゲーム大会用に購入。",
    "registrant_name": "yusuke-sforzando",
    "registered_at": "2020-11-20 02:01:01.847113+09:00"
}


@ pytest.fixture
def airtable_client():
    airtable_client = AirtableClient()
    return airtable_client


def test_register_illegal_dict(airtable_client):
    """Testing when a non-existent field name is registered."""

    assert not airtable_client.validate_input_dict({"test": "test"})


def test_register(airtable_client):
    """Testing whether a dictionary with the proper field names can be registered correctly."""

    assert airtable_client.register_assets(airtable_dictionary)
