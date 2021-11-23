import glob
import os
from django import forms
from django.urls import reverse_lazy
from django.views.generic.edit import FormView

from archiv.models import OUT_DIR
from archiv.tasks import ingest_data


def get_sheet_list():
    glob_pattern = f"{OUT_DIR}/*.csv"
    files = glob.glob(glob_pattern)
    choices = list(((x, os.path.split(x)[1]) for x in files))
    return choices


class SelectSheeForm(forms.Form):
    sheet = forms.ChoiceField(choices=get_sheet_list())


class ContactFormView(FormView):
    template_name = 'archiv/ingest.html'
    form_class = SelectSheeForm
    success_url = reverse_lazy('archiv:task_overview')

    def form_valid(self, form):
        ingest_data.delay()
        return super().form_valid(form)
