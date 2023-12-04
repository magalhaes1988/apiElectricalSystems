from django.db import models
from uuid import uuid4
from datetime import datetime


class LoadGroupManager(models.Manager):

    def not_deleted(self):
        return self.filter(deleted=False)

    def deleted(self):
        return self.filter(deleted=True)


class LoadGroup(models.Model):
    objects = LoadGroupManager()
    uuid = models.UUIDField(primary_key=True, null=False, blank=False, default=uuid4, editable=False, unique=True)
    description = models.CharField(max_length=255, null=False)
    is_discharge_group = models.BooleanField(default=False, null=False)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    delete_at = models.DateTimeField(blank=True, null=True, default=None)
    deleted = models.BooleanField(default=False)

    def __str__(self):
        return self.description

    def delete(self):
        if self.deleted:
            models.Model.delete(self)
        else:
            self.deleted = True
            self.delete_at = datetime.now()
            self.save()



    def save(self, *args, **kwargs):
        if self.deleted:
            self.deleted = True
            self.delete_at = datetime.now()
        else:
            self.deleted = False
            self.delete_at = None
        super(LoadGroup, self).save(*args, **kwargs)

