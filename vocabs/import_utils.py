import pandas as pd
from django.conf import settings
from tqdm import tqdm

from vocabs.models import SkosConcept, SkosCollection


DEFAULT_LANG = getattr(settings, 'VOCABS_DEFAULT_LANG', 'eng')


get_concepts_query = f"""
PREFIX skos: <http://www.w3.org/2004/02/skos/core#>
SELECT ?concept ?label ?definition ?broader WHERE
{{
  ?concept a skos:Concept ;
  skos:prefLabel ?label .
  OPTIONAL {{ ?concept skos:definition ?definition }} .
  OPTIONAL {{ ?concept skos:broader ?broader }} .
  FILTER (LANG(?label)="{DEFAULT_LANG}")
  FILTER (LANG(?definition)="{DEFAULT_LANG}")
}}
"""

colums = [
    "concept", "label", "definition", "broader"
]


def concept_sparql_to_df(graph):
    qres = graph.query(get_concepts_query)
    df = pd.DataFrame(
        [x for x in qres], columns=colums
    )
    return df


def import_concept_from_df(
    df,
    collection_uri="https://some-default-collection",
    collection_pref_label="default-collection"
):
    collection, _ = SkosCollection.objects.get_or_create(
        source_uri=collection_uri
    )
    collection.pref_label = collection_pref_label
    collection.save()
    concepts = []
    for i, row in tqdm(df.iterrows(), total=(len(df))):
        concept, _ = SkosConcept.objects.get_or_create(
            source_uri=row['concept']
        )
        concept.pref_label = row['label']
        concept.definition = row['definition']
        if row['broader']:
            broader, _ = SkosConcept.objects.get_or_create(
                source_uri=row['broader']
            )
            concept.broader_concept = broader
        concept.collection = collection
        concept.save()
        concepts.append(concept)
    return concepts
