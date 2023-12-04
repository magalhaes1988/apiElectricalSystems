from django.db import models
from uuid import uuid4
from math import sqrt,pow
from datetime import datetime
from .projects import Project
from .electricalCharges import ElectricalCharges
#from .loadProjectByCircuit import LoadDescriptionByCircuit

# class LoadDescriptionManager(models.Manager):
#     def all(self):
#         return self

class LoadDescription(models.Model):
    #objects = LoadDescriptionManager()
    uuid = models.UUIDField(primary_key=True, editable=False, unique=True, null=False, default=uuid4, blank=False)
    project = models.ForeignKey(Project, on_delete=models.PROTECT)
    circuit_number = models.PositiveBigIntegerField(null=False, blank=False, unique=False)
    circuit_description = models.CharField(max_length=255, null=True, blank=True)
    electrical_charges = models.ManyToManyField(ElectricalCharges, related_name="electrical",
                                              through="LoadDescriptionByCircuit", symmetrical=False)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    delete_at = models.DateTimeField(blank=True, null=True, default=None)
    deleted = models.BooleanField(default=False)

    def __str__(self):
        return f'Circuit Number: {self.circuit_number} - Description: {self.circuit_description}'

    @property
    def total_power_circuit(self):
        total = 0
        objs = self.electrical.filter(load_description=self.uuid)
        for obj in objs:
            total += obj.quantity*obj.electrical_charge.total_power

        return total

    @property
    def total_reactive_power_circuit(self):
        total = 0
        objs = self.electrical.filter(load_description=self.uuid)
        for obj in objs:
            total += obj.quantity*obj.electrical_charge.total_reactive_power

        return total

    @property
    def total_apparent_power_circuit(self):
        return sqrt(pow(self.total_power_circuit, 2)+pow(self.total_reactive_power_circuit, 2))


# class LoadDescriptionByCircuit(models.Model):
#     load_description = models.ForeignKey(LoadDescription, on_delete=models.CASCADE, related_name="load_description")
#     electrical_charge = models.ForeignKey(ElectricalCharges, on_delete=models.PROTECT, related_name="load_description")
#     quantity = models.PositiveBigIntegerField(null=False, blank=False)

