# generated by appcreator
from django.conf.urls import url
from . import dal_views

app_name = 'archiv'
urlpatterns = [
    url(
        r'^analyse-autocomplete/$',
        dal_views.AnalyseAC.as_view(),
        name='analyse-autocomplete'
    ),
    url(
        r'^artifact-autocomplete/$',
        dal_views.ArtifactAC.as_view(),
        name='artifact-autocomplete'
    ),
    url(
        r'^geography-autocomplete/$',
        dal_views.GeographyAC.as_view(),
        name='geography-autocomplete'
    ),
    url(
        r'^institution-autocomplete/$',
        dal_views.InstitutionAC.as_view(),
        name='institution-autocomplete'
    ),
    url(
        r'^number-autocomplete/$',
        dal_views.NumberAC.as_view(),
        name='number-autocomplete'
    ),
    url(
        r'^quarry-autocomplete/$',
        dal_views.QuarryAC.as_view(),
        name='quarry-autocomplete'
    ),
    url(
        r'^quarrygroup-autocomplete/$',
        dal_views.QuarryGroupAC.as_view(),
        name='quarrygroup-autocomplete'
    ),
    url(
        r'^sample-autocomplete/$',
        dal_views.SampleAC.as_view(),
        name='sample-autocomplete'
    ),
]
