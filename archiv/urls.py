# generated by appcreator
from django.conf.urls import url
from . import views
from . import ingest_views

app_name = "archiv"
urlpatterns = [
    url(r"^test/$", views.count_geo, name="test"),
    url(r"^ingest/$", ingest_views.ContactFormView.as_view(), name="ingest"),
    url(r"^task-overview/$", views.TaskOveriewView.as_view(), name="task_overview"),
    url(r"^analyse/$", views.AnalyseListView.as_view(), name="analyse_browse"),
    url(
        r"^analyse/detail/(?P<pk>[0-9]+)$",
        views.AnalyseDetailView.as_view(),
        name="analyse_detail",
    ),
    url(r"^analyse/create/$", views.AnalyseCreate.as_view(), name="analyse_create"),
    url(
        r"^analyse/edit/(?P<pk>[0-9]+)$",
        views.AnalyseUpdate.as_view(),
        name="analyse_edit",
    ),
    url(
        r"^analyse/delete/(?P<pk>[0-9]+)$",
        views.AnalyseDelete.as_view(),
        name="analyse_delete",
    ),
    url(r"^artifact/$", views.ArtifactListView.as_view(), name="artifact_browse"),
    url(
        r"^artifact/detail/(?P<pk>[0-9]+)$",
        views.ArtifactDetailView.as_view(),
        name="artifact_detail",
    ),
    url(r"^artifact/create/$", views.ArtifactCreate.as_view(), name="artifact_create"),
    url(
        r"^artifact/edit/(?P<pk>[0-9]+)$",
        views.ArtifactUpdate.as_view(),
        name="artifact_edit",
    ),
    url(
        r"^artifact/delete/(?P<pk>[0-9]+)$",
        views.ArtifactDelete.as_view(),
        name="artifact_delete",
    ),
    url(r"^geography/$", views.GeographyListView.as_view(), name="geography_browse"),
    url(
        r"^geography/detail/(?P<pk>[0-9]+)$",
        views.GeographyDetailView.as_view(),
        name="geography_detail",
    ),
    url(
        r"^geography/create/$", views.GeographyCreate.as_view(), name="geography_create"
    ),
    url(
        r"^geography/edit/(?P<pk>[0-9]+)$",
        views.GeographyUpdate.as_view(),
        name="geography_edit",
    ),
    url(
        r"^geography/delete/(?P<pk>[0-9]+)$",
        views.GeographyDelete.as_view(),
        name="geography_delete",
    ),
    url(
        r"^institution/$",
        views.InstitutionListView.as_view(),
        name="institution_browse",
    ),
    url(
        r"^institution/detail/(?P<pk>[0-9]+)$",
        views.InstitutionDetailView.as_view(),
        name="institution_detail",
    ),
    url(
        r"^institution/create/$",
        views.InstitutionCreate.as_view(),
        name="institution_create",
    ),
    url(
        r"^institution/edit/(?P<pk>[0-9]+)$",
        views.InstitutionUpdate.as_view(),
        name="institution_edit",
    ),
    url(
        r"^institution/delete/(?P<pk>[0-9]+)$",
        views.InstitutionDelete.as_view(),
        name="institution_delete",
    ),
    url(r"^number/$", views.NumberListView.as_view(), name="number_browse"),
    url(
        r"^number/detail/(?P<pk>[0-9]+)$",
        views.NumberDetailView.as_view(),
        name="number_detail",
    ),
    url(r"^number/create/$", views.NumberCreate.as_view(), name="number_create"),
    url(
        r"^number/edit/(?P<pk>[0-9]+)$",
        views.NumberUpdate.as_view(),
        name="number_edit",
    ),
    url(
        r"^number/delete/(?P<pk>[0-9]+)$",
        views.NumberDelete.as_view(),
        name="number_delete",
    ),
    url(r"^quarry/$", views.QuarryListView.as_view(), name="quarry_browse"),
    url(
        r"^quarry/detail/(?P<pk>[0-9]+)$",
        views.QuarryDetailView.as_view(),
        name="quarry_detail",
    ),
    url(r"^quarry/create/$", views.QuarryCreate.as_view(), name="quarry_create"),
    url(
        r"^quarry/edit/(?P<pk>[0-9]+)$",
        views.QuarryUpdate.as_view(),
        name="quarry_edit",
    ),
    url(
        r"^quarry/delete/(?P<pk>[0-9]+)$",
        views.QuarryDelete.as_view(),
        name="quarry_delete",
    ),
    url(
        r"^quarrygroup/$",
        views.QuarryGroupListView.as_view(),
        name="quarrygroup_browse",
    ),
    url(
        r"^quarrygroup/detail/(?P<pk>[0-9]+)$",
        views.QuarryGroupDetailView.as_view(),
        name="quarrygroup_detail",
    ),
    url(
        r"^quarrygroup/create/$",
        views.QuarryGroupCreate.as_view(),
        name="quarrygroup_create",
    ),
    url(
        r"^quarrygroup/edit/(?P<pk>[0-9]+)$",
        views.QuarryGroupUpdate.as_view(),
        name="quarrygroup_edit",
    ),
    url(
        r"^quarrygroup/delete/(?P<pk>[0-9]+)$",
        views.QuarryGroupDelete.as_view(),
        name="quarrygroup_delete",
    ),
    url(r"^sample/$", views.SampleListView.as_view(), name="sample_browse"),
    url(
        r"^sample/detail/(?P<pk>[0-9]+)$",
        views.SampleDetailView.as_view(),
        name="sample_detail",
    ),
    url(r"^sample/create/$", views.SampleCreate.as_view(), name="sample_create"),
    url(
        r"^sample/edit/(?P<pk>[0-9]+)$",
        views.SampleUpdate.as_view(),
        name="sample_edit",
    ),
    url(
        r"^sample/delete/(?P<pk>[0-9]+)$",
        views.SampleDelete.as_view(),
        name="sample_delete",
    ),
]
