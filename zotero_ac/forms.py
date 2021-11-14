from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from dal import autocomplete
from django import forms


from zotero_ac.models import ZoteroItem

class ZoteroItemForm(forms.ModelForm):
    zotero_key = forms.CharField(
        widget=autocomplete.ListSelect2(url='zotero-ac:zotero-ac')
    )

    class Meta:
        model = ZoteroItem
        fields = ('__all__')
    
    def __init__(self, *args, **kwargs):
        super(ZoteroItemForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = True
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-md-3'
        self.helper.field_class = 'col-md-9'
        self.helper.add_input(Submit('submit', 'save'),)