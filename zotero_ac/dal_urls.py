from django.urls import path

from zotero_ac import dal_views

app_name = 'zotero_ac'

urlpatterns = [
    path(
        '',
        dal_views.ZoteroAc.as_view(),
        name='zotero-ac'
    ),
]
