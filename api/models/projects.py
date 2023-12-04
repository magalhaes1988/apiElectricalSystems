from django.db import models
from uuid import uuid4
from datetime import datetime
from . import Client


class ProjectManager(models.Manager):

    def not_deleted(self):
        return self.filter(deleted=False).select_related()

    def deleted(self):
        return self.filter(deleted=True).select_related()


class Project(models.Model):

    objects = ProjectManager()
    uuid = models.UUIDField(primary_key=True, null=False, blank=False, default=uuid4, editable=False, unique=True)
    project_id = models.BigIntegerField(primary_key=False, editable=False, auto_created=True)
    project_description = models.TextField(null=True, blank=True)
    client = models.ForeignKey(Client, on_delete=models.PROTECT)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    delete_at = models.DateTimeField(blank=True, null=True)
    deleted = models.BooleanField(default=False)

    def __str__(self):
        return str(self.project_description)

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

        if self.project_id == None:
            self.project_id = Project.objects.count() + 1
        #self.project_id = Project.objects.count()+1
        super(Project, self).save(*args, **kwargs)
