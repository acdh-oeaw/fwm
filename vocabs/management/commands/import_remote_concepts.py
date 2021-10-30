from rdflib import Graph

from django.core.management.base import BaseCommand

from vocabs.import_utils import concept_sparql_to_df, import_concept_from_df

V_BASE = "https://vocabs.acdh.oeaw.ac.at"

DEFAULT_IMPORT_URL = f"{V_BASE}/rest/v1/arche_category/data?format=text/turtle"


class Command(BaseCommand):
    help = "Create app files"

    def add_arguments(self, parser):
        parser.add_argument(
            "-u",
            "--url",
            type=str,
            help=f"The URL of the Concepts to import, defaults to {DEFAULT_IMPORT_URL}")

    def handle(self, *args, **kwargs):

        if kwargs['url']:
            url = kwargs['url']
        else:
            url = DEFAULT_IMPORT_URL
        g = Graph()
        g.parse(url)
        imported = import_concept_from_df(concept_sparql_to_df(g))
        print(f"imported {len(imported)} SkosConcepts")
