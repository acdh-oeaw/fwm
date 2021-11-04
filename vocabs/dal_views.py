from django.db.models import Q
from dal import autocomplete
from django.core.exceptions import ObjectDoesNotExist
from vocabs.models import SkosConcept, SkosTechnicalCollection


class SkosConceptAC(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        qs = SkosConcept.objects.all()
        if self.q:
            qs = qs.filter(
                Q(pref_label__icontains=self.q) |
                Q(source_uri__icontains=self.q)
            )
        return qs


class SpecificConcepts(autocomplete.Select2QuerySetView):

    def get_queryset(self):
        tech_collection = self.kwargs['tech_col']
        try:
            selected_collection = SkosTechnicalCollection.objects.get(pref_label=tech_collection)
            qs = SkosConcept.objects.filter(tech_collection=selected_collection)
        except ObjectDoesNotExist:
            qs = SkosConcept.objects.all()

        if self.q:
            direct_match = qs.filter(pref_label__icontains=self.q)
            return direct_match
        else:
            return qs
