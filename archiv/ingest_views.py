from django.urls import reverse_lazy
from django.views.generic.edit import FormView

from archiv.ingest_forms import SelectSheetForm
import csv
from io import TextIOWrapper
from .models import Sample
from vocabs.models import SkosConcept


class ContactFormView(FormView):
    template_name = "archiv/ingest.html"
    form_class = SelectSheetForm
    success_url = reverse_lazy("archiv:task_overview")

    def form_valid(self, form):
        csv_file = form.cleaned_data["csv_file"]
        sheet = form.cleaned_data["sheet"]
        decoded_file = TextIOWrapper(csv_file.file, encoding="utf-8")
        reader = csv.DictReader(decoded_file, delimiter=",")
        if sheet == "sample":
            for row in reader:
                vocab_material, _ = SkosConcept.objects.get_or_create(
                    pref_label=row["material_id"].strip()
                )
                vocab_color, _ = SkosConcept.objects.get_or_create(
                    pref_label=row["color"].strip()
                )
                vocab_smell, _ = SkosConcept.objects.get_or_create(
                    pref_label=row["smell"].strip()
                )
                vocab_grain_max, _ = SkosConcept.objects.get_or_create(
                    pref_label=row["grain_max"].strip()
                )
                vocab_grain_min, _ = SkosConcept.objects.get_or_create(
                    pref_label=row["grain_min"].strip()
                )
                vocab_license, _ = SkosConcept.objects.get_or_create(
                    pref_label=row["license"].strip()
                )

                Sample.objects.update_or_create(
                    oeai_inventory_number=row["oeai_inventory_number"],
                    defaults={
                        "oeai_inventory_number": row["oeai_inventory_number"],
                        "color_description": row["color_description"],
                        "weight": row["weight"],
                        "notes": row["notes"],
                        "sampling": row["sampling"],
                        "literature": row["literature"],
                        "open_access": row["open_access"],
                        "color_id": vocab_color.id,
                        "grain_size_max_id": vocab_grain_max.id,
                        "grain_size_min_id": vocab_grain_min.id,
                        "material_id": vocab_material.id,
                        "license": vocab_license,
                    },
                )
        return super().form_valid(form)
