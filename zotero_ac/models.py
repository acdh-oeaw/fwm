from django.db import models


class ZoteroItemBase(models.Model):
    zotero_key = models.CharField(max_length=20)
    zotero_title = models.TextField(blank=True, null=True)
    zotero_data = models.JSONField(blank=True, null=True)

    def __str__(self):
        if self.zotero_title:
            return f"{self.zotero_title} || {self.zotero_key}"
        else:
            f"{self.zotero_key}"
    
    class Meta:
        abstract = True


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
