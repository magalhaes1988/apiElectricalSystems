from django.contrib import admin
from computedfields import admin as cadmin
from .models.clients import Client
from .models.projects import Project
from .models.loadGroup import LoadGroup
from .models.electricalCharges import ElectricalCharges
from .models.loadDescription import LoadDescription
from .models.loadProjectByCircuit import LoadDescriptionByCircuit

# Register your models here.

class ClientAdmin(admin.ModelAdmin):

    readonly_fields = ('uuid',)
    list_display = [field.name for field in Client._meta.fields]


class ProjectAdmin(admin.ModelAdmin):
    readonly_fields = ('uuid',)
    list_display = [field.name for field in Project._meta.fields]

class LoadGroupAdmin(admin.ModelAdmin):
    readonly_fields = ('uuid',)
    list_display = [field.name for field in LoadGroup._meta.fields if field.name != "id"]

class ElectricalChargesAdmin(admin.ModelAdmin):

   # print(field.name for field in ElectricalCharges._meta.fields)
    readonly_fields = ('uuid',)
    list_display = [field.name for field in ElectricalCharges._meta.fields if field.name != "id"]
   # fields = [field.name for field in ElectricalCharges._meta.fields if field.name != "id"]

class ElectricalInLine(admin.TabularInline):
    model = LoadDescription.electrical_charges.through

class LoadDescriptionAdmin(admin.ModelAdmin):
    readonly_fields = ('uuid', )
    list_display = [field.name for field in LoadDescription._meta.fields]
    inlines = [ElectricalInLine]


class LoadDescriptionByCircuitAdmin(admin.ModelAdmin):
    #readonly_fields = ('uuid',)
    list_display = [field.name for field in LoadDescriptionByCircuit._meta.fields]

admin.site.register(Client, ClientAdmin)
admin.site.register(Project, ProjectAdmin)
admin.site.register(LoadGroup, LoadGroupAdmin)
admin.site.register(ElectricalCharges, ElectricalChargesAdmin)
admin.site.register(LoadDescription, LoadDescriptionAdmin)
admin.site.register(LoadDescriptionByCircuit, LoadDescriptionByCircuitAdmin)