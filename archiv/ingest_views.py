from django import forms
from django.views.generic.edit import FormView
import glob
import os
from archiv.models import OUT_DIR


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
    success_url = '/'

    # def form_valid(self, form):
    #     # This method is called when valid form data has been POSTed.
    #     # It should return an HttpResponse.
    #     return super().form_valid(form)