from django.db import models
from .electricalCharges import ElectricalCharges
from .loadDescription import LoadDescription


class LoadDescriptionByCircuit(models.Model):

    load_description = models.ForeignKey(LoadDescription, on_delete=models.CASCADE, related_name="electrical")
    electrical_charge = models.ForeignKey(ElectricalCharges, on_delete=models.PROTECT, related_name="teste2")
    quantity = models.PositiveBigIntegerField(null=False, blank=False)





