from django.db import models
from uuid import uuid4
from datetime import datetime


class ClientManager(models.Manager):

    def not_deleted(self):
        return self.filter(deleted=False)

    def deleted(self):
        return self.filter(deleted=True)


class Client(models.Model):
    objects = ClientManager()
    uuid = models.UUIDField(primary_key=True, null=False, blank=False, default=uuid4, editable=False, unique=True)
    name = models.CharField(max_length=255, null=False)
    cpf_cnpj = models.BigIntegerField(unique=True, blank=False, db_index=True)
    cep = models.BigIntegerField(unique=False)
    public_place = models.CharField(max_length=255)
    neighborhood = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=2)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    delete_at = models.DateTimeField(blank=True, null=True, default=None)
    deleted = models.BooleanField(default=False)

    def __str__(self):
        return str(self.name)

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
        super(Client, self).save(*args, **kwargs)
