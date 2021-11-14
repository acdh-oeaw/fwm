from django.contrib import admin

from zotero_ac.models import ZoteroItem, ZoteroReference
from zotero_ac.forms import ZoteroItemForm


class ZoteroItemAdmin(admin.ModelAdmin):
    form = ZoteroItemForm


admin.site.register(ZoteroItem, ZoteroItemAdmin)
admin.site.register(ZoteroReference)
