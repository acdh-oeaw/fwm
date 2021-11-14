from django.http import JsonResponse

from dal import autocomplete
from zotero_ac.utils import search_zotero


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
