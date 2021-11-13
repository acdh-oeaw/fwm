from django.contrib import admin

from zotero_ac.models import ZoteroItem, ZoteroReference

admin.site.register(ZoteroItem)
admin.site.register(ZoteroReference)
