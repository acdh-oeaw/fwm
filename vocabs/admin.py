from django.conf import settings
from django.contrib import admin
from mptt.admin import DraggableMPTTAdmin
from vocabs.models import SkosCollection, SkosConcept, SkosTechnicalCollection


VOCABS_LISTVIEW_PAGESIZE = getattr(settings, "VOCABS_LISTVIEW_PAGESIZE", 50)


@admin.register(SkosConcept)
class SkosConceptAdmin(DraggableMPTTAdmin):
    model = SkosConcept

    list_filter = (
        ("tech_collection", admin.RelatedOnlyFieldListFilter),
        ("collection"),
        ("broader_concept", admin.RelatedOnlyFieldListFilter),
    )
    list_per_page = VOCABS_LISTVIEW_PAGESIZE
    search_fields = ["pref_label"]
    autocomplete_fields = ["broader_concept"]


@admin.register(SkosCollection)
class SkosCollectionAdmin(admin.ModelAdmin):
    model = SkosCollection
    list_display = ("pref_label", "source_uri")
    list_filter = ("pref_label",)


@admin.register(SkosTechnicalCollection)
class SkosTechnicalCollectionAdmin(admin.ModelAdmin):
    pass
