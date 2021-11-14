from django.db import models

from zotero_ac.utils import get_zotero_item


class ZoteroItemBase(models.Model):
    zotero_key = models.CharField(max_length=20)
    zotero_title = models.TextField(blank=True, null=True)
    zotero_creator = models.CharField(blank=True, null=True, max_length=250)
    zotero_date = models.DateField(blank=True, null=True)
    zotero_data = models.JSONField(blank=True, null=True)

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        if self.zotero_key and not self.zotero_data:
            zotero_object = get_zotero_item(self.zotero_key)
            for key, value in zotero_object.items():
                setattr(self, key, value)
        super().save(*args, **kwargs)

    def __str__(self):
        if self.zotero_title:
            return f"{self.zotero_title} || {self.zotero_key}"
        return f"{self.zotero_key}"


class ZoteroItem(ZoteroItemBase):
    pass


class ZoteroReference(ZoteroItemBase):
    location = models.CharField(
        max_length=20
    )

    def __str__(self):
        if self.zotero_title:
            return f"{self.zotero_title}, {self.location}"
        else:
            f"{self.zotero_key}"
