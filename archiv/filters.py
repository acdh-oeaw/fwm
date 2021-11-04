# generated by appcreator
import django_filters

from dal import autocomplete
from django import forms
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

NUMBER_LOOKUP_CHOICES = [
    ('exact', 'Equals'),
    ('gt', 'Greater than'),
    ('lt', 'Less than')
]

CHAR_LOOKUP_CHOICES = [
    ('icontains', 'Contains'),
    ('iexact', 'Equals'),
    ('istartswith', 'Starts with'),
    ('iendswith', 'Ends with')
]


class AnalyseListFilter(django_filters.FilterSet):
    legacy_id = django_filters.LookupChoiceFilter(
        lookup_choices=CHAR_LOOKUP_CHOICES,
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
            tech_collection__pref_label="analyse__analyse_type"
        ),
        help_text=Analyse._meta.get_field('analyse_type').help_text,
        label=Analyse._meta.get_field('analyse_type').verbose_name,
        widget=autocomplete.Select2Multiple(
            url="/vocabs-ac/concept/analyse__analyse_type",
            attrs={
                'data-placeholder': 'Autocomplete ...',
                'data-minimum-input-length': 2,
            },
        )
    )
    notes_thinsection = django_filters.LookupChoiceFilter(
        lookup_choices=CHAR_LOOKUP_CHOICES,
        help_text=Analyse._meta.get_field('notes_thinsection').help_text,
        label=Analyse._meta.get_field('notes_thinsection').verbose_name
    )
    mgco3 = django_filters.LookupChoiceFilter(
        field_class=forms.DecimalField,
        lookup_choices=NUMBER_LOOKUP_CHOICES,
        help_text=Analyse._meta.get_field('mgco3').help_text,
        label=Analyse._meta.get_field('mgco3').verbose_name
    )
    fe = django_filters.LookupChoiceFilter(
        field_class=forms.DecimalField,
        lookup_choices=NUMBER_LOOKUP_CHOICES,
        help_text=Analyse._meta.get_field('fe').help_text,
        label=Analyse._meta.get_field('fe').verbose_name
    )
    mn = django_filters.LookupChoiceFilter(
        field_class=forms.DecimalField,
        lookup_choices=NUMBER_LOOKUP_CHOICES,
        help_text=Analyse._meta.get_field('mn').help_text,
        label=Analyse._meta.get_field('mn').verbose_name
    )
    sr = django_filters.LookupChoiceFilter(
        field_class=forms.DecimalField,
        lookup_choices=NUMBER_LOOKUP_CHOICES,
        help_text=Analyse._meta.get_field('sr').help_text,
        label=Analyse._meta.get_field('sr').verbose_name
    )
    ion_li = django_filters.LookupChoiceFilter(
        field_class=forms.DecimalField,
        lookup_choices=NUMBER_LOOKUP_CHOICES,
        help_text=Analyse._meta.get_field('ion_li').help_text,
        label=Analyse._meta.get_field('ion_li').verbose_name
    )
    ion_na = django_filters.LookupChoiceFilter(
        field_class=forms.DecimalField,
        lookup_choices=NUMBER_LOOKUP_CHOICES,
        help_text=Analyse._meta.get_field('ion_na').help_text,
        label=Analyse._meta.get_field('ion_na').verbose_name
    )
    ion_k = django_filters.LookupChoiceFilter(
        field_class=forms.DecimalField,
        lookup_choices=NUMBER_LOOKUP_CHOICES,
        help_text=Analyse._meta.get_field('ion_k').help_text,
        label=Analyse._meta.get_field('ion_k').verbose_name
    )
    ion_mg = django_filters.LookupChoiceFilter(
        field_class=forms.DecimalField,
        lookup_choices=NUMBER_LOOKUP_CHOICES,
        help_text=Analyse._meta.get_field('ion_mg').help_text,
        label=Analyse._meta.get_field('ion_mg').verbose_name
    )
    ion_ca = django_filters.LookupChoiceFilter(
        field_class=forms.DecimalField,
        lookup_choices=NUMBER_LOOKUP_CHOICES,
        help_text=Analyse._meta.get_field('ion_ca').help_text,
        label=Analyse._meta.get_field('ion_ca').verbose_name
    )
    ion_f = django_filters.LookupChoiceFilter(
        field_class=forms.DecimalField,
        lookup_choices=NUMBER_LOOKUP_CHOICES,
        help_text=Analyse._meta.get_field('ion_f').help_text,
        label=Analyse._meta.get_field('ion_f').verbose_name
    )
    ion_cl = django_filters.LookupChoiceFilter(
        field_class=forms.DecimalField,
        lookup_choices=NUMBER_LOOKUP_CHOICES,
        help_text=Analyse._meta.get_field('ion_cl').help_text,
        label=Analyse._meta.get_field('ion_cl').verbose_name
    )
    ion_br = django_filters.LookupChoiceFilter(
        field_class=forms.DecimalField,
        lookup_choices=NUMBER_LOOKUP_CHOICES,
        help_text=Analyse._meta.get_field('ion_br').help_text,
        label=Analyse._meta.get_field('ion_br').verbose_name
    )
    ion_j = django_filters.LookupChoiceFilter(
        field_class=forms.DecimalField,
        lookup_choices=NUMBER_LOOKUP_CHOICES,
        help_text=Analyse._meta.get_field('ion_j').help_text,
        label=Analyse._meta.get_field('ion_j').verbose_name
    )
    ion_no3 = django_filters.LookupChoiceFilter(
        field_class=forms.DecimalField,
        lookup_choices=NUMBER_LOOKUP_CHOICES,
        help_text=Analyse._meta.get_field('ion_no3').help_text,
        label=Analyse._meta.get_field('ion_no3').verbose_name
    )
    ion_so4 = django_filters.LookupChoiceFilter(
        field_class=forms.DecimalField,
        lookup_choices=NUMBER_LOOKUP_CHOICES,
        help_text=Analyse._meta.get_field('ion_so4').help_text,
        label=Analyse._meta.get_field('ion_so4').verbose_name
    )
    ion_li_na = django_filters.LookupChoiceFilter(
        field_class=forms.DecimalField,
        lookup_choices=NUMBER_LOOKUP_CHOICES,
        help_text=Analyse._meta.get_field('ion_li_na').help_text,
        label=Analyse._meta.get_field('ion_li_na').verbose_name
    )
    ion_k_na = django_filters.LookupChoiceFilter(
        field_class=forms.DecimalField,
        lookup_choices=NUMBER_LOOKUP_CHOICES,
        help_text=Analyse._meta.get_field('ion_k_na').help_text,
        label=Analyse._meta.get_field('ion_k_na').verbose_name
    )
    ion_cl_na = django_filters.LookupChoiceFilter(
        field_class=forms.DecimalField,
        lookup_choices=NUMBER_LOOKUP_CHOICES,
        help_text=Analyse._meta.get_field('ion_cl_na').help_text,
        label=Analyse._meta.get_field('ion_cl_na').verbose_name
    )
    ion_br_na = django_filters.LookupChoiceFilter(
        field_class=forms.DecimalField,
        lookup_choices=NUMBER_LOOKUP_CHOICES,
        help_text=Analyse._meta.get_field('ion_br_na').help_text,
        label=Analyse._meta.get_field('ion_br_na').verbose_name
    )
    ion_i_na = django_filters.LookupChoiceFilter(
        field_class=forms.DecimalField,
        lookup_choices=NUMBER_LOOKUP_CHOICES,
        help_text=Analyse._meta.get_field('ion_i_na').help_text,
        label=Analyse._meta.get_field('ion_i_na').verbose_name
    )
    ion_so4_na = django_filters.LookupChoiceFilter(
        field_class=forms.DecimalField,
        lookup_choices=NUMBER_LOOKUP_CHOICES,
        help_text=Analyse._meta.get_field('ion_so4_na').help_text,
        label=Analyse._meta.get_field('ion_so4_na').verbose_name
    )
    ion_f_na = django_filters.LookupChoiceFilter(
        field_class=forms.DecimalField,
        lookup_choices=NUMBER_LOOKUP_CHOICES,
        help_text=Analyse._meta.get_field('ion_f_na').help_text,
        label=Analyse._meta.get_field('ion_f_na').verbose_name
    )
    ion_no3_na = django_filters.LookupChoiceFilter(
        field_class=forms.DecimalField,
        lookup_choices=NUMBER_LOOKUP_CHOICES,
        help_text=Analyse._meta.get_field('ion_no3_na').help_text,
        label=Analyse._meta.get_field('ion_no3_na').verbose_name
    )
    iso_d18o = django_filters.LookupChoiceFilter(
        field_class=forms.DecimalField,
        lookup_choices=NUMBER_LOOKUP_CHOICES,
        help_text=Analyse._meta.get_field('iso_d18o').help_text,
        label=Analyse._meta.get_field('iso_d18o').verbose_name
    )
    iso_d13c = django_filters.LookupChoiceFilter(
        field_class=forms.DecimalField,
        lookup_choices=NUMBER_LOOKUP_CHOICES,
        help_text=Analyse._meta.get_field('iso_d13c').help_text,
        label=Analyse._meta.get_field('iso_d13c').verbose_name
    )
    icp_mg = django_filters.LookupChoiceFilter(
        field_class=forms.DecimalField,
        lookup_choices=NUMBER_LOOKUP_CHOICES,
        help_text=Analyse._meta.get_field('icp_mg').help_text,
        label=Analyse._meta.get_field('icp_mg').verbose_name
    )
    icp_mn = django_filters.LookupChoiceFilter(
        field_class=forms.DecimalField,
        lookup_choices=NUMBER_LOOKUP_CHOICES,
        help_text=Analyse._meta.get_field('icp_mn').help_text,
        label=Analyse._meta.get_field('icp_mn').verbose_name
    )
    icp_fe = django_filters.LookupChoiceFilter(
        field_class=forms.DecimalField,
        lookup_choices=NUMBER_LOOKUP_CHOICES,
        help_text=Analyse._meta.get_field('icp_fe').help_text,
        label=Analyse._meta.get_field('icp_fe').verbose_name
    )
    icp_sr = django_filters.LookupChoiceFilter(
        field_class=forms.DecimalField,
        lookup_choices=NUMBER_LOOKUP_CHOICES,
        help_text=Analyse._meta.get_field('icp_sr').help_text,
        label=Analyse._meta.get_field('icp_sr').verbose_name
    )
    icp_cr = django_filters.LookupChoiceFilter(
        field_class=forms.DecimalField,
        lookup_choices=NUMBER_LOOKUP_CHOICES,
        help_text=Analyse._meta.get_field('icp_cr').help_text,
        label=Analyse._meta.get_field('icp_cr').verbose_name
    )
    icp_cr_n2o = django_filters.LookupChoiceFilter(
        field_class=forms.DecimalField,
        lookup_choices=NUMBER_LOOKUP_CHOICES,
        help_text=Analyse._meta.get_field('icp_cr_n2o').help_text,
        label=Analyse._meta.get_field('icp_cr_n2o').verbose_name
    )
    icp_v = django_filters.LookupChoiceFilter(
        field_class=forms.DecimalField,
        lookup_choices=NUMBER_LOOKUP_CHOICES,
        help_text=Analyse._meta.get_field('icp_v').help_text,
        label=Analyse._meta.get_field('icp_v').verbose_name
    )
    icp_y = django_filters.LookupChoiceFilter(
        field_class=forms.DecimalField,
        lookup_choices=NUMBER_LOOKUP_CHOICES,
        help_text=Analyse._meta.get_field('icp_y').help_text,
        label=Analyse._meta.get_field('icp_y').verbose_name
    )
    icp_cd = django_filters.LookupChoiceFilter(
        field_class=forms.DecimalField,
        lookup_choices=NUMBER_LOOKUP_CHOICES,
        help_text=Analyse._meta.get_field('icp_cd').help_text,
        label=Analyse._meta.get_field('icp_cd').verbose_name
    )
    icp_ba = django_filters.LookupChoiceFilter(
        field_class=forms.DecimalField,
        lookup_choices=NUMBER_LOOKUP_CHOICES,
        help_text=Analyse._meta.get_field('icp_ba').help_text,
        label=Analyse._meta.get_field('icp_ba').verbose_name
    )
    icp_la = django_filters.LookupChoiceFilter(
        field_class=forms.DecimalField,
        lookup_choices=NUMBER_LOOKUP_CHOICES,
        help_text=Analyse._meta.get_field('icp_la').help_text,
        label=Analyse._meta.get_field('icp_la').verbose_name
    )
    icp_ce = django_filters.LookupChoiceFilter(
        field_class=forms.DecimalField,
        lookup_choices=NUMBER_LOOKUP_CHOICES,
        help_text=Analyse._meta.get_field('icp_ce').help_text,
        label=Analyse._meta.get_field('icp_ce').verbose_name
    )
    icp_pr = django_filters.LookupChoiceFilter(
        field_class=forms.DecimalField,
        lookup_choices=NUMBER_LOOKUP_CHOICES,
        help_text=Analyse._meta.get_field('icp_pr').help_text,
        label=Analyse._meta.get_field('icp_pr').verbose_name
    )
    icp_dy = django_filters.LookupChoiceFilter(
        field_class=forms.DecimalField,
        lookup_choices=NUMBER_LOOKUP_CHOICES,
        help_text=Analyse._meta.get_field('icp_dy').help_text,
        label=Analyse._meta.get_field('icp_dy').verbose_name
    )
    icp_ho = django_filters.LookupChoiceFilter(
        field_class=forms.DecimalField,
        lookup_choices=NUMBER_LOOKUP_CHOICES,
        help_text=Analyse._meta.get_field('icp_ho').help_text,
        label=Analyse._meta.get_field('icp_ho').verbose_name
    )
    icp_yb = django_filters.LookupChoiceFilter(
        field_class=forms.DecimalField,
        lookup_choices=NUMBER_LOOKUP_CHOICES,
        help_text=Analyse._meta.get_field('icp_yb').help_text,
        label=Analyse._meta.get_field('icp_yb').verbose_name
    )
    icp_pb = django_filters.LookupChoiceFilter(
        field_class=forms.DecimalField,
        lookup_choices=NUMBER_LOOKUP_CHOICES,
        help_text=Analyse._meta.get_field('icp_pb').help_text,
        label=Analyse._meta.get_field('icp_pb').verbose_name
    )
    icp_u = django_filters.LookupChoiceFilter(
        field_class=forms.DecimalField,
        lookup_choices=NUMBER_LOOKUP_CHOICES,
        help_text=Analyse._meta.get_field('icp_u').help_text,
        label=Analyse._meta.get_field('icp_u').verbose_name
    )

    class Meta:
        model = Analyse
        fields = [
            'id',
            'legacy_id',
            'legacy_pk',
            'oeai_inventory_number',
            'institute',
            'analyse_type',
            'date',
            'notes_thinsection',
            'mgco3',
            'fe',
            'mn',
            'sr',
            'ion_li',
            'ion_na',
            'ion_k',
            'ion_mg',
            'ion_ca',
            'ion_f',
            'ion_cl',
            'ion_br',
            'ion_j',
            'ion_no3',
            'ion_so4',
            'ion_li_na',
            'ion_k_na',
            'ion_cl_na',
            'ion_br_na',
            'ion_i_na',
            'ion_so4_na',
            'ion_f_na',
            'ion_no3_na',
            'iso_d18o',
            'iso_d13c',
            'icp_mg',
            'icp_mn',
            'icp_fe',
            'icp_sr',
            'icp_cr',
            'icp_cr_n2o',
            'icp_v',
            'icp_y',
            'icp_cd',
            'icp_ba',
            'icp_la',
            'icp_ce',
            'icp_pr',
            'icp_dy',
            'icp_ho',
            'icp_yb',
            'icp_pb',
            'icp_u',
            
        ]


class ArtifactListFilter(django_filters.FilterSet):
    legacy_id = django_filters.LookupChoiceFilter(
        lookup_choices=CHAR_LOOKUP_CHOICES,
        help_text=Artifact._meta.get_field('legacy_id').help_text,
        label=Artifact._meta.get_field('legacy_id').verbose_name
    )
    artefact_type = django_filters.ModelMultipleChoiceFilter(
        queryset=SkosConcept.objects.filter(
            tech_collection__pref_label="artifact__artefact_type"
        ),
        help_text=Artifact._meta.get_field('artefact_type').help_text,
        label=Artifact._meta.get_field('artefact_type').verbose_name,
        widget=autocomplete.Select2Multiple(
            url="/vocabs-ac/concept/artifact__artefact_type",
            attrs={
                'data-placeholder': 'Autocomplete ...',
                'data-minimum-input-length': 2,
            },
        )
    )
    description = django_filters.LookupChoiceFilter(
        lookup_choices=CHAR_LOOKUP_CHOICES,
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
    find_spot_extra = django_filters.LookupChoiceFilter(
        lookup_choices=CHAR_LOOKUP_CHOICES,
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
            tech_collection__pref_label="artifact__material"
        ),
        help_text=Artifact._meta.get_field('material').help_text,
        label=Artifact._meta.get_field('material').verbose_name,
        widget=autocomplete.Select2Multiple(
            url="/vocabs-ac/concept/artifact__material",
            attrs={
                'data-placeholder': 'Autocomplete ...',
                'data-minimum-input-length': 2,
            },
        )
    )
    measurement = django_filters.LookupChoiceFilter(
        lookup_choices=CHAR_LOOKUP_CHOICES,
        help_text=Artifact._meta.get_field('measurement').help_text,
        label=Artifact._meta.get_field('measurement').verbose_name
    )
    preservation = django_filters.LookupChoiceFilter(
        lookup_choices=CHAR_LOOKUP_CHOICES,
        help_text=Artifact._meta.get_field('preservation').help_text,
        label=Artifact._meta.get_field('preservation').verbose_name
    )
    dating = django_filters.ModelMultipleChoiceFilter(
        queryset=SkosConcept.objects.filter(
            tech_collection__pref_label="artifact__dating"
        ),
        help_text=Artifact._meta.get_field('dating').help_text,
        label=Artifact._meta.get_field('dating').verbose_name,
        widget=autocomplete.Select2Multiple(
            url="/vocabs-ac/concept/artifact__dating",
            attrs={
                'data-placeholder': 'Autocomplete ...',
                'data-minimum-input-length': 2,
            },
        )
    )
    images = django_filters.LookupChoiceFilter(
        lookup_choices=CHAR_LOOKUP_CHOICES,
        help_text=Artifact._meta.get_field('images').help_text,
        label=Artifact._meta.get_field('images').verbose_name
    )
    literature = django_filters.LookupChoiceFilter(
        lookup_choices=CHAR_LOOKUP_CHOICES,
        help_text=Artifact._meta.get_field('literature').help_text,
        label=Artifact._meta.get_field('literature').verbose_name
    )

    class Meta:
        model = Artifact
        fields = [
            'id',
            'legacy_id',
            'legacy_pk',
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
    legacy_id = django_filters.LookupChoiceFilter(
        lookup_choices=CHAR_LOOKUP_CHOICES,
        help_text=Geography._meta.get_field('legacy_id').help_text,
        label=Geography._meta.get_field('legacy_id').verbose_name
    )
    name = django_filters.LookupChoiceFilter(
        lookup_choices=CHAR_LOOKUP_CHOICES,
        help_text=Geography._meta.get_field('name').help_text,
        label=Geography._meta.get_field('name').verbose_name
    )
    identifier = django_filters.LookupChoiceFilter(
        lookup_choices=CHAR_LOOKUP_CHOICES,
        help_text=Geography._meta.get_field('identifier').help_text,
        label=Geography._meta.get_field('identifier').verbose_name
    )
    notes = django_filters.LookupChoiceFilter(
        lookup_choices=CHAR_LOOKUP_CHOICES,
        help_text=Geography._meta.get_field('notes').help_text,
        label=Geography._meta.get_field('notes').verbose_name
    )

    class Meta:
        model = Geography
        fields = [
            'id',
            'legacy_id',
            'name',
            'identifier',
            
            
            
            'notes',
            
        ]


class InstitutionListFilter(django_filters.FilterSet):
    legacy_id = django_filters.LookupChoiceFilter(
        lookup_choices=CHAR_LOOKUP_CHOICES,
        help_text=Institution._meta.get_field('legacy_id').help_text,
        label=Institution._meta.get_field('legacy_id').verbose_name
    )
    name = django_filters.LookupChoiceFilter(
        lookup_choices=CHAR_LOOKUP_CHOICES,
        help_text=Institution._meta.get_field('name').help_text,
        label=Institution._meta.get_field('name').verbose_name
    )
    identifier = django_filters.LookupChoiceFilter(
        lookup_choices=CHAR_LOOKUP_CHOICES,
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
    legacy_id = django_filters.LookupChoiceFilter(
        lookup_choices=CHAR_LOOKUP_CHOICES,
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
    number = django_filters.LookupChoiceFilter(
        lookup_choices=CHAR_LOOKUP_CHOICES,
        help_text=Number._meta.get_field('number').help_text,
        label=Number._meta.get_field('number').verbose_name
    )
    number_type = django_filters.ModelMultipleChoiceFilter(
        queryset=SkosConcept.objects.filter(
            tech_collection__pref_label="number__number_type"
        ),
        help_text=Number._meta.get_field('number_type').help_text,
        label=Number._meta.get_field('number_type').verbose_name,
        widget=autocomplete.Select2Multiple(
            url="/vocabs-ac/concept/number__number_type",
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
    notes = django_filters.LookupChoiceFilter(
        lookup_choices=CHAR_LOOKUP_CHOICES,
        help_text=Number._meta.get_field('notes').help_text,
        label=Number._meta.get_field('notes').verbose_name
    )

    class Meta:
        model = Number
        fields = [
            'id',
            'legacy_id',
            'legacy_pk',
            'oeai_inventory_number',
            'number',
            'number_type',
            'institute',
            'notes',
            
        ]


class QuarryListFilter(django_filters.FilterSet):
    legacy_id = django_filters.LookupChoiceFilter(
        lookup_choices=CHAR_LOOKUP_CHOICES,
        help_text=Quarry._meta.get_field('legacy_id').help_text,
        label=Quarry._meta.get_field('legacy_id').verbose_name
    )
    name = django_filters.LookupChoiceFilter(
        lookup_choices=CHAR_LOOKUP_CHOICES,
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
    images = django_filters.LookupChoiceFilter(
        lookup_choices=CHAR_LOOKUP_CHOICES,
        help_text=Quarry._meta.get_field('images').help_text,
        label=Quarry._meta.get_field('images').verbose_name
    )
    description = django_filters.LookupChoiceFilter(
        lookup_choices=CHAR_LOOKUP_CHOICES,
        help_text=Quarry._meta.get_field('description').help_text,
        label=Quarry._meta.get_field('description').verbose_name
    )
    literature = django_filters.LookupChoiceFilter(
        lookup_choices=CHAR_LOOKUP_CHOICES,
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
            'open_access',
            
        ]


class QuarryGroupListFilter(django_filters.FilterSet):
    legacy_id = django_filters.LookupChoiceFilter(
        lookup_choices=CHAR_LOOKUP_CHOICES,
        help_text=QuarryGroup._meta.get_field('legacy_id').help_text,
        label=QuarryGroup._meta.get_field('legacy_id').verbose_name
    )
    name = django_filters.LookupChoiceFilter(
        lookup_choices=CHAR_LOOKUP_CHOICES,
        help_text=QuarryGroup._meta.get_field('name').help_text,
        label=QuarryGroup._meta.get_field('name').verbose_name
    )
    description = django_filters.LookupChoiceFilter(
        lookup_choices=CHAR_LOOKUP_CHOICES,
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
    legacy_id = django_filters.LookupChoiceFilter(
        lookup_choices=CHAR_LOOKUP_CHOICES,
        help_text=Sample._meta.get_field('legacy_id').help_text,
        label=Sample._meta.get_field('legacy_id').verbose_name
    )
    oeai_inventory_number = django_filters.LookupChoiceFilter(
        lookup_choices=CHAR_LOOKUP_CHOICES,
        help_text=Sample._meta.get_field('oeai_inventory_number').help_text,
        label=Sample._meta.get_field('oeai_inventory_number').verbose_name
    )
    smell = django_filters.ModelMultipleChoiceFilter(
        queryset=SkosConcept.objects.filter(
            tech_collection__pref_label="sample__smell"
        ),
        help_text=Sample._meta.get_field('smell').help_text,
        label=Sample._meta.get_field('smell').verbose_name,
        widget=autocomplete.Select2Multiple(
            url="/vocabs-ac/concept/sample__smell",
            attrs={
                'data-placeholder': 'Autocomplete ...',
                'data-minimum-input-length': 2,
            },
        )
    )
    grain_size_min = django_filters.ModelMultipleChoiceFilter(
        queryset=SkosConcept.objects.filter(
            tech_collection__pref_label="sample__grain_size_min"
        ),
        help_text=Sample._meta.get_field('grain_size_min').help_text,
        label=Sample._meta.get_field('grain_size_min').verbose_name,
        widget=autocomplete.Select2Multiple(
            url="/vocabs-ac/concept/sample__grain_size_min",
            attrs={
                'data-placeholder': 'Autocomplete ...',
                'data-minimum-input-length': 2,
            },
        )
    )
    grain_size_max = django_filters.ModelMultipleChoiceFilter(
        queryset=SkosConcept.objects.filter(
            tech_collection__pref_label="sample__grain_size_max"
        ),
        help_text=Sample._meta.get_field('grain_size_max').help_text,
        label=Sample._meta.get_field('grain_size_max').verbose_name,
        widget=autocomplete.Select2Multiple(
            url="/vocabs-ac/concept/sample__grain_size_max",
            attrs={
                'data-placeholder': 'Autocomplete ...',
                'data-minimum-input-length': 2,
            },
        )
    )
    material = django_filters.ModelMultipleChoiceFilter(
        queryset=SkosConcept.objects.filter(
            tech_collection__pref_label="sample__material"
        ),
        help_text=Sample._meta.get_field('material').help_text,
        label=Sample._meta.get_field('material').verbose_name,
        widget=autocomplete.Select2Multiple(
            url="/vocabs-ac/concept/sample__material",
            attrs={
                'data-placeholder': 'Autocomplete ...',
                'data-minimum-input-length': 2,
            },
        )
    )
    color = django_filters.ModelMultipleChoiceFilter(
        queryset=SkosConcept.objects.filter(
            tech_collection__pref_label="sample__color"
        ),
        help_text=Sample._meta.get_field('color').help_text,
        label=Sample._meta.get_field('color').verbose_name,
        widget=autocomplete.Select2Multiple(
            url="/vocabs-ac/concept/sample__color",
            attrs={
                'data-placeholder': 'Autocomplete ...',
                'data-minimum-input-length': 2,
            },
        )
    )
    color_description = django_filters.LookupChoiceFilter(
        lookup_choices=CHAR_LOOKUP_CHOICES,
        help_text=Sample._meta.get_field('color_description').help_text,
        label=Sample._meta.get_field('color_description').verbose_name
    )
    color_kodak = django_filters.LookupChoiceFilter(
        lookup_choices=CHAR_LOOKUP_CHOICES,
        help_text=Sample._meta.get_field('color_kodak').help_text,
        label=Sample._meta.get_field('color_kodak').verbose_name
    )
    stdcolor = django_filters.LookupChoiceFilter(
        lookup_choices=CHAR_LOOKUP_CHOICES,
        help_text=Sample._meta.get_field('stdcolor').help_text,
        label=Sample._meta.get_field('stdcolor').verbose_name
    )
    weight = django_filters.LookupChoiceFilter(
        field_class=forms.DecimalField,
        lookup_choices=NUMBER_LOOKUP_CHOICES,
        help_text=Sample._meta.get_field('weight').help_text,
        label=Sample._meta.get_field('weight').verbose_name
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
    notes = django_filters.LookupChoiceFilter(
        lookup_choices=CHAR_LOOKUP_CHOICES,
        help_text=Sample._meta.get_field('notes').help_text,
        label=Sample._meta.get_field('notes').verbose_name
    )
    sampling = django_filters.LookupChoiceFilter(
        lookup_choices=CHAR_LOOKUP_CHOICES,
        help_text=Sample._meta.get_field('sampling').help_text,
        label=Sample._meta.get_field('sampling').verbose_name
    )
    literature = django_filters.LookupChoiceFilter(
        lookup_choices=CHAR_LOOKUP_CHOICES,
        help_text=Sample._meta.get_field('literature').help_text,
        label=Sample._meta.get_field('literature').verbose_name
    )
    image = django_filters.LookupChoiceFilter(
        lookup_choices=CHAR_LOOKUP_CHOICES,
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
            'weight',
            'artefakt_id',
            'quarry',
            'quarry_group',
            'notes',
            'sampling',
            'literature',
            'image',
            'open_access',
            
        ]


