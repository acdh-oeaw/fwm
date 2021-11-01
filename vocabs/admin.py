from django.contrib import admin
from mptt.admin import DraggableMPTTAdmin, TreeRelatedFieldListFilter
from vocabs.models import SkosCollection, SkosConcept


@admin.register(SkosConcept)
class SkosConceptAdmin(DraggableMPTTAdmin):
    model = SkosConcept

    list_filter = (
        ('collection'),
        ('broader_concept', TreeRelatedFieldListFilter),
    )
    list_per_page = 50
    search_fields = ['pref_label']


admin.site.register(SkosCollection)
