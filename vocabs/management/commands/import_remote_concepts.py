from rdflib import Graph

from django.core.management.base import BaseCommand

from vocabs.import_utils import concept_sparql_to_df, import_concept_from_df

V_BASE = "https://vocabs.acdh.oeaw.ac.at"

DEFAULT_IMPORT_URL = f"{V_BASE}/rest/v1/arche_category/data?format=text/turtle"


class Command(BaseCommand):
    help = "Create app files"

    def add_arguments(self, parser):
        parser.add_argument(
            "-i",
            "--import-url",
            type=str,
            help=f"The URL of the Concepts to import, defaults to {DEFAULT_IMPORT_URL}"
        )
        parser.add_argument(
            "-u",
            "--collection-uri",
            type=str,
            help=f"An URI for a SkosCollection to group the imported SkosConcetps\
                defaults to {DEFAULT_IMPORT_URL}"
        )
        parser.add_argument(
            "-l",
            "--label",
            type=str,
            help=f"A label for a SkosCollection to group the imported SkosConcetps\
                defaults to {DEFAULT_IMPORT_URL}"
        )

    def handle(self, *args, **kwargs):

        if kwargs['import_url']:
            import_url = kwargs['import_url']
        else:
            import_url = DEFAULT_IMPORT_URL
        if kwargs['collection_uri']:
            collection_uri = import_url
        else:
            collection_uri = import_url
        if kwargs['label']:
            label = kwargs['label']
        else:
            label = import_url
        g = Graph()
        g.parse(import_url)
        imported = import_concept_from_df(
            concept_sparql_to_df(g),
            collection_uri=collection_uri,
            collection_pref_label=label
        )
        print(f"imported {len(imported)} SkosConcepts")
