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

    def test_001_str(self):
        for x in MODELS:
            item = x.objects.first()
            self.assertTru('<' in f"{item}")
