from django.test import TestCase, Client, override_settings

from zotero_ac.utils import search_zotero, get_zotero_item
from zotero_ac.models import ZoteroReference, ZoteroItem

ZOTERO_URL = "https://api.zotero.org/groups/440857/items"
ZOTERO_ITEM = "ADY7BMGA"
a = f"Andorfer et al., DHd 2019 Book of AbstractsHackathon, 2019 || {ZOTERO_ITEM}"
client = Client()


@override_settings(ZOTERO_URL="https://api.zotero.org/groups/440857/items")
class ZoteroAcTest(TestCase):
    fixtures = ['dump.json']

    def test_001_no_schema_zotero_url(self):
        wrong_url = "aslödfkj"
        result = search_zotero('asdf', url=wrong_url)
        self.assertEqual(result, [])

    def test_002_wrong_zotero_url(self):
        wrong_url = "http://slödfkj"
        result = search_zotero('asdf', url=wrong_url)
        self.assertEqual(result, [])

    def test_003_good_url(self):
        result = search_zotero('Histogis', url=ZOTERO_URL)
        self.assertTrue('zotero_key' in result[0].keys())

    def test_004_get_zotero_item(self):
        result = get_zotero_item(
            ZOTERO_ITEM, base_url=ZOTERO_URL
        )
        self.assertTrue(result['zotero_key'], ZOTERO_ITEM)
    
    def test_005_save_object(self):
        item = ZoteroReference.objects.create(
            zotero_key=ZOTERO_ITEM,
            location="p. 10-12"
        )
        self.assertEqual(item.zotero_key, ZOTERO_ITEM)
        self.assertTrue(item.location in item.__str__())
    

    def test_006_ac_endpoint(self):
        item = ZoteroItem.objects.first()
        url = item.get_ac_url()
        response = client.get(url)
        self.assertEqual(response.status_code, 200)
        item = ZoteroReference.objects.first()
        url = item.get_ac_url()
        response = client.get(url)
        self.assertEqual(response.status_code, 200)

