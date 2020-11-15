import api_keys


def test_api_keys():
    assert api_keys.airtable_base_id
    assert api_keys.airtable_api_key
    assert api_keys.amazon_partner_tag
    assert api_keys.amazon_access_key
    assert api_keys.amazon_secret_key
