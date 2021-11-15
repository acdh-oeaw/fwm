from django.db.models import Q
from django.http import JsonResponse

from dal import autocomplete
from zotero_ac.utils import search_zotero
from . models import (
    ZoteroItem, ZoteroReference
)


class ZoteroAc(autocomplete.Select2ListView):

    def get(self, request, *args, **kwargs):
        choices = []
        q = self.request.GET.get('q')

        if len(self.q) < 4:
            choices = []
            return JsonResponse({"results": choices})
        else:
            choices = [
                {
                    "id": x['zotero_key'],
                    "text": x['zotero_title'],
                    "data": x['zotero_data']['data']
                } for x in search_zotero(q)
            ]
            return JsonResponse({"results": choices})


class ZoteroReferenceAC(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        qs = ZoteroReference.objects.all()

        if self.q:
            qs = qs.filter(
                Q(zotero_key__icontains=self.q) |
                Q(zotero_title__icontains=self.q) |
                Q(zotero_creator__icontains=self.q) |
                Q(location__icontains=self.q)
            )
        return qs


class ZoteroItemAC(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        qs = ZoteroItem.objects.all()

        if self.q:
            qs = qs.filter(
                Q(zotero_key__icontains=self.q) |
                Q(zotero_title__icontains=self.q) |
                Q(zotero_creator__icontains=self.q)
            )
        return qs
