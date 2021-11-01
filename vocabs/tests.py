from django.apps import apps
from django.core.management import call_command
from django.contrib.auth.models import User
from django.test import Client, TestCase

from vocabs.models import SkosCollection

IMPORT_URL = "https://vocabs.dariah.eu/rest/v1/arche_access_restrictions/data?format=application/rdf%2Bxml"
MODELS = list(apps.all_models['vocabs'].values())

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

    def test_import_cmd(self):

        call_command('import_remote_concepts', import_url=IMPORT_URL)
        new_collection = SkosCollection.objects.get(
            source_uri=IMPORT_URL
        )
        self.assertEqual(
            IMPORT_URL,
            new_collection.source_uri
        )
