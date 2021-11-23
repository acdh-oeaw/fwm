from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic.edit import FormView

from archiv.ingest_forms import SelectSheeForm
from archiv.tasks import ingest_data


class ContactFormView(FormView):
    template_name = 'archiv/ingest.html'
    form_class = SelectSheeForm
    success_url = reverse_lazy('archiv:task_overview')

    def form_valid(self, form):
        model_name = form.cleaned_data['sheet']
        ingest_data.delay(model_name)
        return super().form_valid(form)

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(ContactFormView, self).dispatch(*args, **kwargs)
