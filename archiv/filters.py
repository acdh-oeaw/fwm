# generated by appcreator
import django_filters

from dal import autocomplete
from vocabs.models import SkosConcept

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


class AnalyseListFilter(django_filters.FilterSet):
    legacy_id = django_filters.CharFilter(
        lookup_expr='icontains',
        help_text=Analyse._meta.get_field('legacy_id').help_text,
        label=Analyse._meta.get_field('legacy_id').verbose_name
    )
    oeai_inventory_number = django_filters.ModelMultipleChoiceFilter(
        queryset=Sample.objects.all(),
        help_text=Analyse._meta.get_field('oeai_inventory_number').help_text,
        label=Analyse._meta.get_field('oeai_inventory_number').verbose_name,
        widget=autocomplete.Select2Multiple(
            url="archiv-ac:sample-autocomplete",
        )
    )
    institute = django_filters.ModelMultipleChoiceFilter(
        queryset=Institution.objects.all(),
        help_text=Analyse._meta.get_field('institute').help_text,
        label=Analyse._meta.get_field('institute').verbose_name,
        widget=autocomplete.Select2Multiple(
            url="archiv-ac:institution-autocomplete",
        )
    )
    analyse_type = django_filters.ModelMultipleChoiceFilter(
        queryset=SkosConcept.objects.filter(
            collection__pref_label="analyse_type"
        ),
        help_text=Analyse._meta.get_field('analyse_type').help_text,
        label=Analyse._meta.get_field('analyse_type').verbose_name,
        widget=autocomplete.Select2Multiple(
            url="/vocabs-ac/specific-concept-ac/analyse_type",
            attrs={
                'data-placeholder': 'Autocomplete ...',
                'data-minimum-input-length': 2,
            },
        )
    )
    notes_thinsection = django_filters.CharFilter(
        lookup_expr='icontains',
        help_text=Analyse._meta.get_field('notes_thinsection').help_text,
        label=Analyse._meta.get_field('notes_thinsection').verbose_name
    )

    class Meta:
        model = Analyse
        fields = [
            'id',
            'legacy_id',
            'oeai_inventory_number',
            'institute',
            'analyse_type',
            'date',
            'notes_thinsection',
        ]


class ArtifactListFilter(django_filters.FilterSet):
    legacy_id = django_filters.CharFilter(
        lookup_expr='icontains',
        help_text=Artifact._meta.get_field('legacy_id').help_text,
        label=Artifact._meta.get_field('legacy_id').verbose_name
    )
    artefact_type = django_filters.ModelMultipleChoiceFilter(
        queryset=SkosConcept.objects.filter(
            collection__pref_label="artefact_type"
        ),
        help_text=Artifact._meta.get_field('artefact_type').help_text,
        label=Artifact._meta.get_field('artefact_type').verbose_name,
        widget=autocomplete.Select2Multiple(
            url="/vocabs-ac/specific-concept-ac/artefact_type",
            attrs={
                'data-placeholder': 'Autocomplete ...',
                'data-minimum-input-length': 2,
            },
        )
    )
    description = django_filters.CharFilter(
        lookup_expr='icontains',
        help_text=Artifact._meta.get_field('description').help_text,
        label=Artifact._meta.get_field('description').verbose_name
    )
    find_spot = django_filters.ModelMultipleChoiceFilter(
        queryset=Geography.objects.all(),
        help_text=Artifact._meta.get_field('find_spot').help_text,
        label=Artifact._meta.get_field('find_spot').verbose_name,
        widget=autocomplete.Select2Multiple(
            url="archiv-ac:geography-autocomplete",
        )
    )
    find_spot_extra = django_filters.CharFilter(
        lookup_expr='icontains',
        help_text=Artifact._meta.get_field('find_spot_extra').help_text,
        label=Artifact._meta.get_field('find_spot_extra').verbose_name
    )
    storage_place = django_filters.ModelMultipleChoiceFilter(
        queryset=Institution.objects.all(),
        help_text=Artifact._meta.get_field('storage_place').help_text,
        label=Artifact._meta.get_field('storage_place').verbose_name,
        widget=autocomplete.Select2Multiple(
            url="archiv-ac:institution-autocomplete",
        )
    )
    material = django_filters.ModelMultipleChoiceFilter(
        queryset=SkosConcept.objects.filter(
            collection__pref_label="material"
        ),
        help_text=Artifact._meta.get_field('material').help_text,
        label=Artifact._meta.get_field('material').verbose_name,
        widget=autocomplete.Select2Multiple(
            url="/vocabs-ac/specific-concept-ac/material",
            attrs={
                'data-placeholder': 'Autocomplete ...',
                'data-minimum-input-length': 2,
            },
        )
    )
    measurement = django_filters.CharFilter(
        lookup_expr='icontains',
        help_text=Artifact._meta.get_field('measurement').help_text,
        label=Artifact._meta.get_field('measurement').verbose_name
    )
    preservation = django_filters.CharFilter(
        lookup_expr='icontains',
        help_text=Artifact._meta.get_field('preservation').help_text,
        label=Artifact._meta.get_field('preservation').verbose_name
    )
    dating = django_filters.ModelMultipleChoiceFilter(
        queryset=SkosConcept.objects.filter(
            collection__pref_label="dating"
        ),
        help_text=Artifact._meta.get_field('dating').help_text,
        label=Artifact._meta.get_field('dating').verbose_name,
        widget=autocomplete.Select2Multiple(
            url="/vocabs-ac/specific-concept-ac/dating",
            attrs={
                'data-placeholder': 'Autocomplete ...',
                'data-minimum-input-length': 2,
            },
        )
    )
    images = django_filters.CharFilter(
        lookup_expr='icontains',
        help_text=Artifact._meta.get_field('images').help_text,
        label=Artifact._meta.get_field('images').verbose_name
    )
    literature = django_filters.CharFilter(
        lookup_expr='icontains',
        help_text=Artifact._meta.get_field('literature').help_text,
        label=Artifact._meta.get_field('literature').verbose_name
    )

    class Meta:
        model = Artifact
        fields = [
            'id',
            'legacy_id',
            'artefact_type',
            'description',
            'find_spot',
            'find_spot_extra',
            'storage_place',
            'material',
            'measurement',
            'preservation',
            'dating',
            'images',
            'literature',
        ]


class GeographyListFilter(django_filters.FilterSet):
    legacy_id = django_filters.CharFilter(
        lookup_expr='icontains',
        help_text=Geography._meta.get_field('legacy_id').help_text,
        label=Geography._meta.get_field('legacy_id').verbose_name
    )
    contintent = django_filters.ModelMultipleChoiceFilter(
        queryset=SkosConcept.objects.filter(
            collection__pref_label="contintent"
        ),
        help_text=Geography._meta.get_field('contintent').help_text,
        label=Geography._meta.get_field('contintent').verbose_name,
        widget=autocomplete.Select2Multiple(
            url="/vocabs-ac/specific-concept-ac/contintent",
            attrs={
                'data-placeholder': 'Autocomplete ...',
                'data-minimum-input-length': 2,
            },
        )
    )
    land = django_filters.ModelMultipleChoiceFilter(
        queryset=SkosConcept.objects.filter(
            collection__pref_label="land"
        ),
        help_text=Geography._meta.get_field('land').help_text,
        label=Geography._meta.get_field('land').verbose_name,
        widget=autocomplete.Select2Multiple(
            url="/vocabs-ac/specific-concept-ac/land",
            attrs={
                'data-placeholder': 'Autocomplete ...',
                'data-minimum-input-length': 2,
            },
        )
    )
    province = django_filters.ModelMultipleChoiceFilter(
        queryset=SkosConcept.objects.filter(
            collection__pref_label="province"
        ),
        help_text=Geography._meta.get_field('province').help_text,
        label=Geography._meta.get_field('province').verbose_name,
        widget=autocomplete.Select2Multiple(
            url="/vocabs-ac/specific-concept-ac/province",
            attrs={
                'data-placeholder': 'Autocomplete ...',
                'data-minimum-input-length': 2,
            },
        )
    )
    location = django_filters.ModelMultipleChoiceFilter(
        queryset=SkosConcept.objects.filter(
            collection__pref_label="location"
        ),
        help_text=Geography._meta.get_field('location').help_text,
        label=Geography._meta.get_field('location').verbose_name,
        widget=autocomplete.Select2Multiple(
            url="/vocabs-ac/specific-concept-ac/location",
            attrs={
                'data-placeholder': 'Autocomplete ...',
                'data-minimum-input-length': 2,
            },
        )
    )
    name = django_filters.ModelMultipleChoiceFilter(
        queryset=SkosConcept.objects.filter(
            collection__pref_label="name"
        ),
        help_text=Geography._meta.get_field('name').help_text,
        label=Geography._meta.get_field('name').verbose_name,
        widget=autocomplete.Select2Multiple(
            url="/vocabs-ac/specific-concept-ac/name",
            attrs={
                'data-placeholder': 'Autocomplete ...',
                'data-minimum-input-length': 2,
            },
        )
    )
    identifier = django_filters.CharFilter(
        lookup_expr='icontains',
        help_text=Geography._meta.get_field('identifier').help_text,
        label=Geography._meta.get_field('identifier').verbose_name
    )
    coordinates = django_filters.CharFilter(
        lookup_expr='icontains',
        help_text=Geography._meta.get_field('coordinates').help_text,
        label=Geography._meta.get_field('coordinates').verbose_name
    )
    coordinates = django_filters.CharFilter(
        lookup_expr='icontains',
        help_text=Geography._meta.get_field('coordinates').help_text,
        label=Geography._meta.get_field('coordinates').verbose_name
    )
    notes = django_filters.CharFilter(
        lookup_expr='icontains',
        help_text=Geography._meta.get_field('notes').help_text,
        label=Geography._meta.get_field('notes').verbose_name
    )

    class Meta:
        model = Geography
        fields = [
            'id',
            'legacy_id',
            'contintent',
            'land',
            'province',
            'location',
            'name',
            'identifier',
            'coordinates',
            'coordinates',
            'notes',
        ]


class InstitutionListFilter(django_filters.FilterSet):
    legacy_id = django_filters.CharFilter(
        lookup_expr='icontains',
        help_text=Institution._meta.get_field('legacy_id').help_text,
        label=Institution._meta.get_field('legacy_id').verbose_name
    )
    name = django_filters.CharFilter(
        lookup_expr='icontains',
        help_text=Institution._meta.get_field('name').help_text,
        label=Institution._meta.get_field('name').verbose_name
    )
    identifier = django_filters.CharFilter(
        lookup_expr='icontains',
        help_text=Institution._meta.get_field('identifier').help_text,
        label=Institution._meta.get_field('identifier').verbose_name
    )

    class Meta:
        model = Institution
        fields = [
            'id',
            'legacy_id',
            'name',
            'identifier',
        ]


class NumberListFilter(django_filters.FilterSet):
    legacy_id = django_filters.CharFilter(
        lookup_expr='icontains',
        help_text=Number._meta.get_field('legacy_id').help_text,
        label=Number._meta.get_field('legacy_id').verbose_name
    )
    oeai_inventory_number = django_filters.ModelMultipleChoiceFilter(
        queryset=Sample.objects.all(),
        help_text=Number._meta.get_field('oeai_inventory_number').help_text,
        label=Number._meta.get_field('oeai_inventory_number').verbose_name,
        widget=autocomplete.Select2Multiple(
            url="archiv-ac:sample-autocomplete",
        )
    )
    number = django_filters.CharFilter(
        lookup_expr='icontains',
        help_text=Number._meta.get_field('number').help_text,
        label=Number._meta.get_field('number').verbose_name
    )
    number_type = django_filters.ModelMultipleChoiceFilter(
        queryset=SkosConcept.objects.filter(
            collection__pref_label="number_type"
        ),
        help_text=Number._meta.get_field('number_type').help_text,
        label=Number._meta.get_field('number_type').verbose_name,
        widget=autocomplete.Select2Multiple(
            url="/vocabs-ac/specific-concept-ac/number_type",
            attrs={
                'data-placeholder': 'Autocomplete ...',
                'data-minimum-input-length': 2,
            },
        )
    )
    institute = django_filters.ModelMultipleChoiceFilter(
        queryset=Institution.objects.all(),
        help_text=Number._meta.get_field('institute').help_text,
        label=Number._meta.get_field('institute').verbose_name,
        widget=autocomplete.Select2Multiple(
            url="archiv-ac:institution-autocomplete",
        )
    )
    notes = django_filters.CharFilter(
        lookup_expr='icontains',
        help_text=Number._meta.get_field('notes').help_text,
        label=Number._meta.get_field('notes').verbose_name
    )

    class Meta:
        model = Number
        fields = [
            'id',
            'legacy_id',
            'oeai_inventory_number',
            'number',
            'number_type',
            'institute',
            'notes',
        ]


class QuarryListFilter(django_filters.FilterSet):
    legacy_id = django_filters.CharFilter(
        lookup_expr='icontains',
        help_text=Quarry._meta.get_field('legacy_id').help_text,
        label=Quarry._meta.get_field('legacy_id').verbose_name
    )
    name = django_filters.CharFilter(
        lookup_expr='icontains',
        help_text=Quarry._meta.get_field('name').help_text,
        label=Quarry._meta.get_field('name').verbose_name
    )
    geography = django_filters.ModelMultipleChoiceFilter(
        queryset=Geography.objects.all(),
        help_text=Quarry._meta.get_field('geography').help_text,
        label=Quarry._meta.get_field('geography').verbose_name,
        widget=autocomplete.Select2Multiple(
            url="archiv-ac:geography-autocomplete",
        )
    )
    images = django_filters.CharFilter(
        lookup_expr='icontains',
        help_text=Quarry._meta.get_field('images').help_text,
        label=Quarry._meta.get_field('images').verbose_name
    )
    description = django_filters.CharFilter(
        lookup_expr='icontains',
        help_text=Quarry._meta.get_field('description').help_text,
        label=Quarry._meta.get_field('description').verbose_name
    )
    literature = django_filters.CharFilter(
        lookup_expr='icontains',
        help_text=Quarry._meta.get_field('literature').help_text,
        label=Quarry._meta.get_field('literature').verbose_name
    )

    class Meta:
        model = Quarry
        fields = [
            'id',
            'legacy_id',
            'name',
            'geography',
            'images',
            'description',
            'literature',
        ]


class QuarryGroupListFilter(django_filters.FilterSet):
    legacy_id = django_filters.CharFilter(
        lookup_expr='icontains',
        help_text=QuarryGroup._meta.get_field('legacy_id').help_text,
        label=QuarryGroup._meta.get_field('legacy_id').verbose_name
    )
    name = django_filters.CharFilter(
        lookup_expr='icontains',
        help_text=QuarryGroup._meta.get_field('name').help_text,
        label=QuarryGroup._meta.get_field('name').verbose_name
    )
    description = django_filters.CharFilter(
        lookup_expr='icontains',
        help_text=QuarryGroup._meta.get_field('description').help_text,
        label=QuarryGroup._meta.get_field('description').verbose_name
    )

    class Meta:
        model = QuarryGroup
        fields = [
            'id',
            'legacy_id',
            'name',
            'description',
        ]


class SampleListFilter(django_filters.FilterSet):
    legacy_id = django_filters.CharFilter(
        lookup_expr='icontains',
        help_text=Sample._meta.get_field('legacy_id').help_text,
        label=Sample._meta.get_field('legacy_id').verbose_name
    )
    oeai_inventory_number = django_filters.CharFilter(
        lookup_expr='icontains',
        help_text=Sample._meta.get_field('oeai_inventory_number').help_text,
        label=Sample._meta.get_field('oeai_inventory_number').verbose_name
    )
    smell = django_filters.ModelMultipleChoiceFilter(
        queryset=SkosConcept.objects.filter(
            collection__pref_label="smell"
        ),
        help_text=Sample._meta.get_field('smell').help_text,
        label=Sample._meta.get_field('smell').verbose_name,
        widget=autocomplete.Select2Multiple(
            url="/vocabs-ac/specific-concept-ac/smell",
            attrs={
                'data-placeholder': 'Autocomplete ...',
                'data-minimum-input-length': 2,
            },
        )
    )
    grain_size_min = django_filters.ModelMultipleChoiceFilter(
        queryset=SkosConcept.objects.filter(
            collection__pref_label="grain_size_min"
        ),
        help_text=Sample._meta.get_field('grain_size_min').help_text,
        label=Sample._meta.get_field('grain_size_min').verbose_name,
        widget=autocomplete.Select2Multiple(
            url="/vocabs-ac/specific-concept-ac/grain_size_min",
            attrs={
                'data-placeholder': 'Autocomplete ...',
                'data-minimum-input-length': 2,
            },
        )
    )
    grain_size_max = django_filters.ModelMultipleChoiceFilter(
        queryset=SkosConcept.objects.filter(
            collection__pref_label="grain_size_max"
        ),
        help_text=Sample._meta.get_field('grain_size_max').help_text,
        label=Sample._meta.get_field('grain_size_max').verbose_name,
        widget=autocomplete.Select2Multiple(
            url="/vocabs-ac/specific-concept-ac/grain_size_max",
            attrs={
                'data-placeholder': 'Autocomplete ...',
                'data-minimum-input-length': 2,
            },
        )
    )
    material = django_filters.ModelMultipleChoiceFilter(
        queryset=SkosConcept.objects.filter(
            collection__pref_label="material"
        ),
        help_text=Sample._meta.get_field('material').help_text,
        label=Sample._meta.get_field('material').verbose_name,
        widget=autocomplete.Select2Multiple(
            url="/vocabs-ac/specific-concept-ac/material",
            attrs={
                'data-placeholder': 'Autocomplete ...',
                'data-minimum-input-length': 2,
            },
        )
    )
    color = django_filters.ModelMultipleChoiceFilter(
        queryset=SkosConcept.objects.filter(
            collection__pref_label="color"
        ),
        help_text=Sample._meta.get_field('color').help_text,
        label=Sample._meta.get_field('color').verbose_name,
        widget=autocomplete.Select2Multiple(
            url="/vocabs-ac/specific-concept-ac/color",
            attrs={
                'data-placeholder': 'Autocomplete ...',
                'data-minimum-input-length': 2,
            },
        )
    )
    color_description = django_filters.CharFilter(
        lookup_expr='icontains',
        help_text=Sample._meta.get_field('color_description').help_text,
        label=Sample._meta.get_field('color_description').verbose_name
    )
    color_kodak = django_filters.CharFilter(
        lookup_expr='icontains',
        help_text=Sample._meta.get_field('color_kodak').help_text,
        label=Sample._meta.get_field('color_kodak').verbose_name
    )
    stdcolor = django_filters.CharFilter(
        lookup_expr='icontains',
        help_text=Sample._meta.get_field('stdcolor').help_text,
        label=Sample._meta.get_field('stdcolor').verbose_name
    )
    artefakt_id = django_filters.ModelMultipleChoiceFilter(
        queryset=Artifact.objects.all(),
        help_text=Sample._meta.get_field('artefakt_id').help_text,
        label=Sample._meta.get_field('artefakt_id').verbose_name,
        widget=autocomplete.Select2Multiple(
            url="archiv-ac:artifact-autocomplete",
        )
    )
    quarry = django_filters.ModelMultipleChoiceFilter(
        queryset=Quarry.objects.all(),
        help_text=Sample._meta.get_field('quarry').help_text,
        label=Sample._meta.get_field('quarry').verbose_name,
        widget=autocomplete.Select2Multiple(
            url="archiv-ac:quarry-autocomplete",
        )
    )
    quarry_group = django_filters.ModelMultipleChoiceFilter(
        queryset=QuarryGroup.objects.all(),
        help_text=Sample._meta.get_field('quarry_group').help_text,
        label=Sample._meta.get_field('quarry_group').verbose_name,
        widget=autocomplete.Select2Multiple(
            url="archiv-ac:quarrygroup-autocomplete",
        )
    )
    notes = django_filters.CharFilter(
        lookup_expr='icontains',
        help_text=Sample._meta.get_field('notes').help_text,
        label=Sample._meta.get_field('notes').verbose_name
    )
    sampling = django_filters.CharFilter(
        lookup_expr='icontains',
        help_text=Sample._meta.get_field('sampling').help_text,
        label=Sample._meta.get_field('sampling').verbose_name
    )
    literature = django_filters.CharFilter(
        lookup_expr='icontains',
        help_text=Sample._meta.get_field('literature').help_text,
        label=Sample._meta.get_field('literature').verbose_name
    )
    image = django_filters.CharFilter(
        lookup_expr='icontains',
        help_text=Sample._meta.get_field('image').help_text,
        label=Sample._meta.get_field('image').verbose_name
    )

    class Meta:
        model = Sample
        fields = [
            'id',
            'legacy_id',
            'oeai_inventory_number',
            'smell',
            'grain_size_min',
            'grain_size_max',
            'material',
            'color',
            'color_description',
            'color_kodak',
            'stdcolor',
            'artefakt_id',
            'quarry',
            'quarry_group',
            'notes',
            'sampling',
            'literature',
            'image',
        ]

