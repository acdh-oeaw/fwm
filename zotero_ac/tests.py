from django.test import TestCase

from zotero_ac.utils import search_zotero, get_zotero_item

ZOTERO_URL = "https://api.zotero.org/groups/2770745/items"
ZOTERO_ITEM = "SM5N3AF2"
a = f"Schütz, Die geographische Terminologie des Serbokroatischen, 1957 || {ZOTERO_ITEM}"


class ZoteroAcTest(TestCase):

    def test_001_no_schema_zotero_url(self):
        wrong_url = "aslödfkj"
        result = search_zotero('asdf', url=wrong_url)
        self.assertEqual(result, [])

    def test_002_wrong_zotero_url(self):
        wrong_url = "http://slödfkj"
        result = search_zotero('asdf', url=wrong_url)
        self.assertEqual(result, [])

    def test_003_good_url(self):
        result = search_zotero('Sprache', url=ZOTERO_URL)
        self.assertTrue('zotero_key' in result[0].keys())

    def test_004_get_zotero_item(self):
        result = get_zotero_item(
            ZOTERO_ITEM, base_url=ZOTERO_URL
        )
        self.assertTrue(result['zotero_key'], ZOTERO_ITEM)
