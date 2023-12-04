from django.db import models
from uuid import uuid4
from datetime import datetime
from .loadGroup import LoadGroup
from math import acos, tan, sqrt, pow
from computedfields.models import ComputedFieldsModel, ComputedField, computed


class ElectricalChargesManager(models.Manager):

    def not_deleted(self):
        return self.filter(deleted=False)

    def deleted(self):
        return self.filter(deleted=True)


class ElectricalCharges(ComputedFieldsModel):




    objects = ElectricalChargesManager()
    uuid = models.UUIDField(primary_key=True, null=False, blank=False, default=uuid4, editable=False, unique=True)
    tag = models.CharField(max_length=255, blank=True, default=None, null=True)
    power = models.FloatField(null=False, blank=False)
    power_factor = models.FloatField(null=False, blank=False)
    group = models.ForeignKey(LoadGroup, on_delete=models.PROTECT)
    active_power = models.FloatField(null=True, blank=True)

    @computed(
        models.FloatField(null=True, blank=False),
        depends = [('self',['active_power','power_factor'])],
    )
    def reactive_power(self):
        return self.active_power*tan(acos(self.power_factor))

    @computed(
        models.FloatField(null=True, blank=False),
        depends=[('self', ['active_power', 'reactive_power'])],
    )
    def apparent_power(self):
        return sqrt(pow(self.active_power, 2) + pow(self.reactive_power, 2))

    @computed(
        models.FloatField(null=True, blank=False),
        depends = [('self', ('power', 'active_power'))],
    )
    def total_power(self):
        if self.group.is_discharge_group:
            return self.power + self.active_power
        else:
            return self.active_power

    @computed(
        models.FloatField(null=True, blank=False),
        depends=[('self', ('reactive_power', ))],
    )
    def total_reactive_power(self):
        return self.reactive_power

    @computed(
        models.FloatField(null=True, blank=False),
        depends=[('self', ('total_power', 'total_reactive_power'))]
    )
    def total_apparent_power(self):
        return sqrt(pow(self.total_power, 2)+pow(self.total_reactive_power, 2))

    @computed(
        models.FloatField(null=True, blank=False),
        depends=[('self', ('total_power', 'total_apparent_power'))]
    )
    def final_factor_power(self):
        return self.total_power/self.total_apparent_power

    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    delete_at = models.DateTimeField(blank=True, null=True)
    deleted = models.BooleanField(default=False)

    def _active_power(self):
        if LoadGroup.objects.get(uuid=self.group.uuid).is_discharge_group:
            self.active_power = self.active_power
        else:
            self.active_power = self.power

    def __str__(self):
        return self.tag

    def delete(self, using=None, keep_parents=False):
        if self.deleted:
            super().delete()
        else:
            self.deleted = True
            self.deleted = datetime.now()
            self.save()

    def save(
        self, force_insert=False, force_update=False, using=None, update_fields=None, *args, **kwargs
    ):
        if self.deleted:
            self.deleted = True
            self.delete_at = datetime.now()
        else:
            self.deleted = False
            self.delete_at = None
        self._active_power()
        super(ElectricalCharges, self).save(*args, **kwargs)