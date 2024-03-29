from django.urls import path
from . import views
from . import special_views

app_name = "infos"
urlpatterns = [
    path("project-team/", special_views.TeamView.as_view(), name="project-team"),
    path(
        "about-the-project/",
        special_views.SpecialAboutView.as_view(),
        name="about-the-project",
    ),
    path("about/", views.AboutTheProjectListView.as_view(), name="about_browse"),
    path(
        "about/detail/<int:pk>",
        views.AboutTheProjectDetailView.as_view(),
        name="about_detail",
    ),
    path("about/create/", views.AboutTheProjectCreate.as_view(), name="about_create"),
    path(
        "about/edit/<int:pk>",
        views.AboutTheProjectUpdate.as_view(),
        name="about_edit",
    ),
    path(
        "about/delete/<int:pk>",
        views.AboutTheProjectDelete.as_view(),
        name="about_delete",
    ),
    path("teammember/", views.TeamMemberListView.as_view(), name="teammember_browse"),
    path(
        "teammember/detail/<int:pk>",
        views.TeamMemberDetailView.as_view(),
        name="teammember_detail",
    ),
    path(
        "teammember/create/",
        views.TeamMemberCreate.as_view(),
        name="teammember_create",
    ),
    path(
        "teammember/edit/<int:pk>",
        views.TeamMemberUpdate.as_view(),
        name="teammember_edit",
    ),
    path(
        "teammember/delete/<int:pk>",
        views.TeamMemberDelete.as_view(),
        name="teammember_delete",
    ),
    path(
        "projectinst/",
        views.ProjectInstListView.as_view(),
        name="projectinst_browse",
    ),
    path(
        "projectinst/detail/<int:pk>",
        views.ProjectInstDetailView.as_view(),
        name="projectinst_detail",
    ),
    path(
        "projectinst/create/",
        views.ProjectInstCreate.as_view(),
        name="projectinst_create",
    ),
    path(
        "projectinst/edit/<int:pk>",
        views.ProjectInstUpdate.as_view(),
        name="projectinst_edit",
    ),
    path(
        "projectinst/delete/<int:pk>",
        views.ProjectInstDelete.as_view(),
        name="projectinst_delete",
    ),
]
