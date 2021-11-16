from django.urls import path

from zotero_ac import dal_views

app_name = 'zotero_ac'

urlpatterns = [
    path(
        '',
        dal_views.ZoteroAc.as_view(),
        name='zotero-ac'
    ),
    path(
        'zotero-item',
        dal_views.ZoteroItemAC.as_view(create_field='zotero_key'),
        name='zotero-item'
    ),
    path(
        'zotero-reference',
        dal_views.ZoteroReferenceAC.as_view(create_field='zotero_key'),
        name='zotero-reference'
    ),
]
