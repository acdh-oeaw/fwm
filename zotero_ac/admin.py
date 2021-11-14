from django.contrib import admin

from zotero_ac.models import ZoteroItem, ZoteroReference
from zotero_ac.forms import ZoteroItemForm, ZoteroReferenceForm


class ZoteroItemAdmin(admin.ModelAdmin):
    form = ZoteroItemForm


class ZoteroReferenceAdmin(admin.ModelAdmin):
    form = ZoteroReferenceForm


admin.site.register(ZoteroItem, ZoteroItemAdmin)
admin.site.register(ZoteroReference, ZoteroReferenceAdmin)
