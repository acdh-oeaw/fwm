from django.views.generic import TemplateView

from webpage.utils import PROJECT_METADATA as PM
from . models import AboutTheProject, TeamMember


class TeamView(TemplateView):
    template_name = "infos/team.html"

    def get_context_data(self, **kwargs):
        objects = TeamMember.objects.all()
        project = AboutTheProject.objects.all()[0]
        context = super().get_context_data(**kwargs)
        context['objects'] = objects
        context['project'] = project
        return context


class SpecialAboutView(TemplateView):
    template_name = 'infos/about.html'

    def get_context_data(self, **kwargs):
        try:
            object = AboutTheProject.objects.all()[0]
        except IndexError:
            object = PM
        context = super().get_context_data(**kwargs)
        context['object'] = object
        return context
