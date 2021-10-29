from django.contrib import admin
from mptt.admin import DraggableMPTTAdmin
from vocabs.models import SkosCollection, SkosConcept

admin.site.register(SkosConcept, DraggableMPTTAdmin)
admin.site.register(SkosCollection)
