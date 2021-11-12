# generated by appcreator
from django.db.models import Q
from dal import autocomplete
from . models import (
    Analyse,
    Artifact,
    Geography,
    Institution,
    Number,
    Quarry,
    QuarryGroup,
    Sample
)


class AnalyseAC(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        qs = Analyse.objects.all()

        if self.q:
            qs = qs.filter(
                Q(legacy_id__icontains=self.q) |
                Q(id__icontains=self.q)
            )
        return qs


class ArtifactAC(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        qs = Artifact.objects.all()

        if self.q:
            qs = qs.filter(
                Q(legacy_id__icontains=self.q) |
                Q(id__icontains=self.q)
            )
        return qs


class GeographyAC(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        qs = Geography.objects.all()

        if self.q:
            qs = qs.filter(
                Q(legacy_id__icontains=self.q) |
                Q(name__icontains=self.q)
            )
        return qs


class InstitutionAC(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        qs = Institution.objects.all()

        if self.q:
            qs = qs.filter(
                Q(legacy_id__icontains=self.q) |
                Q(name__icontains=self.q)
            )
        return qs


class NumberAC(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        qs = Number.objects.all()

        if self.q:
            qs = qs.filter(
                Q(legacy_id__icontains=self.q) |
                Q(id__icontains=self.q)
            )
        return qs


class QuarryAC(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        qs = Quarry.objects.all()

        if self.q:
            qs = qs.filter(
                Q(legacy_id__icontains=self.q) |
                Q(name__icontains=self.q)
            )
        return qs


class QuarryGroupAC(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        qs = QuarryGroup.objects.all()

        if self.q:
            qs = qs.filter(
                Q(legacy_id__icontains=self.q) |
                Q(name__icontains=self.q)
            )
        return qs


class SampleAC(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        qs = Sample.objects.all()

        if self.q:
            qs = qs.filter(
                Q(legacy_id__icontains=self.q) |
                Q(oeai_inventory_number__icontains=self.q)
            )
        return qs


