from django.db import models
from django.conf import settings

from mptt.models import MPTTModel, TreeForeignKey


DEFAULT_LANG = getattr(settings, 'VOCABS_DEFAULT_LANG', 'eng')


LABEL_TYPES = (
    ('prefLabel', 'prefLabel'),
    ('altLabel', 'altLabel'),
    ('hiddenLabel', 'hiddenLabel'),
)

NOTE_TYPES = (
    ('note', 'note'),
    ('scopeNote', 'scopeNote'),
    ('changeNote', 'changeNote'),
    ('editorialNote', 'editorialNote'),
    ('historyNote', 'historyNote'),
    ('definition', 'definition'),
    ('example', 'example'),
)


class SkosCollection(models.Model):
    """
    SKOS collections are labeled and/or ordered groups of SKOS concepts.
    Collections are useful where a group of concepts shares something in common,
    and it is convenient to group them under a common label, or
    where some concepts can be placed in a meaningful order.
    Miles, Alistair, and Sean Bechhofer. "SKOS simple knowledge
    organization system reference. W3C recommendation (2009)."
    """

    pref_label = models.CharField(
        blank=True,
        null=True,
        max_length=300,
        verbose_name="skos:prefLabel",
        help_text="Collection label or name",
    )
    label_lang = models.CharField(
        max_length=3, blank=True,
        default=DEFAULT_LANG,
        verbose_name="skos:prefLabel language",
        help_text="Language of preferred label given above"
    )
    description = models.TextField(
        blank=True,
        null=True,
        verbose_name="elaborate description of the collection",
        help_text="Description"
    )

    def __str__(self):
        return f"{self.pref_label}"


class SkosConcept(MPTTModel):
    """
    A SKOS concept can be viewed as an idea or notion; a unit of thought.
    However, what constitutes a unit of thought is subjective,
    and this definition is meant to be suggestive, rather than restrictive.
    Miles, Alistair, and Sean Bechhofer. "SKOS simple knowledge
    organization system reference. W3C recommendation (2009)."
    """
    pref_label = models.CharField(
        max_length=300,
        verbose_name="skos:prefLabel",
        help_text="Preferred label for concept"
    )
    pref_label_lang = models.CharField(
        max_length=3, blank=True,
        verbose_name="skos:prefLabel language",
        help_text="Language of preferred label given above",
        default=DEFAULT_LANG
    )
    # relation to SkosConceptScheme to inherit all objects permissions
    collection = models.ForeignKey(
        'SkosCollection',
        null=True,
        blank=True,
        verbose_name="member of skos:Collection",
        help_text="Collection that this concept is a member of",
        related_name="has_members",
        on_delete=models.SET_NULL,
    )
    top_concept = models.BooleanField(
        null=True,
        help_text="Is this concept a top concept of concept scheme?"
    )
    broader_concept = TreeForeignKey(
        'self',
        verbose_name="skos:broader",
        blank=True, null=True, on_delete=models.SET_NULL,
        related_name="narrower_concepts",
        help_text="Concept with a broader meaning that this concept inherits from"
    )

    class MPTTMeta:
        parent_attr = 'broader_concept'

    def __str__(self):
        return f"{self.pref_label}"
