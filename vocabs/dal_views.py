from django.db.models import Q
from dal import autocomplete
from vocabs.models import SkosTechnicalCollection, SkosConcept


class SkosConceptAC(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        qs = SkosConcept.objects.all()
        if self.q:
            qs = qs.filter(
                Q(pref_label__icontains=self.q) |
                Q(source_uri__icontains=self.q)
            )
        return qs