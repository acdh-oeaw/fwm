from django.apps import apps
from django import forms


def get_choices():
    MODELS = list(apps.all_models['archiv'].values())
    choices = [
        (x._meta.model_name, x.__name__) for x in MODELS if getattr(x, 'get_source_table', None)
    ]
    return list(choices)


class SelectSheeForm(forms.Form):
    sheet = forms.ChoiceField(choices=get_choices())