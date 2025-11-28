from django.db import models
from django.conf import settings
from django.urls import reverse


from zotero_ac.utils import get_zotero_item


class ZoteroItemBase(models.Model):
    zotero_key = models.CharField(max_length=20)
    zotero_title = models.TextField(blank=True, null=True)
    zotero_creator = models.CharField(blank=True, null=True, max_length=250)
    zotero_date = models.DateField(blank=True, null=True)
    zotero_data = models.JSONField(blank=True, null=True)

    class Meta:
        abstract = True
        ordering = ["zotero_creator", "id"]

    @classmethod
    def cur_zotero_url(cls):
        zotero = getattr(settings, "ZOTERO_URL")
        return zotero

    def save(self, *args, **kwargs):
        if self.zotero_key and not self.zotero_data:
            zotero_object = get_zotero_item(
                self.zotero_key, base_url=self.cur_zotero_url()
            )
            for key, value in zotero_object.items():
                setattr(self, key, value)
        super().save(*args, **kwargs)

    def __str__(self):
        if self.zotero_title:
            if self.zotero_date:
                my_str = f"{self.zotero_creator}, {self.zotero_title}, {self.zotero_date.year} || {self.zotero_key}"
            else:
                my_str = (
                    f"{self.zotero_creator}, {self.zotero_title} || {self.zotero_key}"
                )
            return my_str
        else:
            return f"{self.zotero_key}"


class ZoteroItem(ZoteroItemBase):
    @classmethod
    def get_ac_url(self):
        return reverse("zotero-ac:zotero-item")


class ZoteroReference(ZoteroItemBase):
    location = models.CharField(max_length=20, null=True, blank=True)

    def __str__(self):
        if self.zotero_title:
            if self.zotero_date:
                my_str = f"{self.zotero_creator}, {self.zotero_title}, {self.zotero_date.year}, {self.location} || {self.zotero_key}"  # noqa: E501
            else:
                my_str = f"{self.zotero_creator}, {self.zotero_title}, {self.location} || {self.zotero_key}"
            return my_str
        else:
            return f"{self.zotero_key}"

    @classmethod
    def get_ac_url(self):
        return reverse("zotero-ac:zotero-reference")
