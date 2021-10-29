from django.apps import apps
from django.contrib.auth.models import User
from django.test import Client, TestCase


MODELS = list(apps.all_models['archiv'].values())

client = Client()
USER = {
    "username": "temporary1",
    "password": "temporary1"
}


class InfosTest(TestCase):
    fixtures = ['dump.json']

    def setUp(self):
        self.client = Client()
        User.objects.create_user(**USER)

    def test_002_listviews(self):
        for x in MODELS:
            try:
                url = x.get_listview_url()
            except AttributeError:
                url = False
            if url:
                response = client.get(url)
                self.assertEqual(response.status_code, 200)

    def test_003_detailviews(self):
        for x in MODELS:
            item = x.objects.first()
            try:
                url = item.get_absolute_url()
            except AttributeError:
                url = False
            if url:
                response = client.get(url, {'pk': item.id})
                self.assertEqual(response.status_code, 200)
