from rest_framework import serializers

from ..models.loadDescription import LoadDescription
from ..models.electricalCharges import ElectricalCharges
from ..models.loadProjectByCircuit import LoadDescriptionByCircuit
from .electricalCharges import ElectricalChargesSerializer


class LoadDescriptionByCircuitSerializer(serializers.ModelSerializer):
    class Meta:
        model = LoadDescriptionByCircuit
        fields = ['quantity', 'load_description', 'electrical_charge']
        depth = 0





class LoadDescriptionSerializer(serializers.ModelSerializer):

    electrical = serializers.SerializerMethodField()
    total_power_circuit = serializers.Field
    total_reactive_power_circuit = serializers.Field
    total_apparent_power_circuit = serializers.Field
    class Meta:
        model = LoadDescription
        fields = [
            'uuid',
            'project',
            'circuit_number',
            'circuit_description',
            'create_at',
            'update_at',
            'delete_at',
            'deleted',
            'electrical',
            'total_power_circuit',
            'total_reactive_power_circuit',
            'total_apparent_power_circuit'

        ]
        extra_fields = ['teste']
        read_only_fields = ['uuid', 'create_at', 'update_at', 'delete_at']
        depth = 0


    def get_electrical(self, obj):

        instance = obj.electrical.all()
        serializer = LoadDescriptionByCircuitSerializer(instance, many=True, read_only=True)
        return serializer.data

    def create(self, validated_data):

        rs = self.context.pop('electrical')
        instance = LoadDescription.objects.create(**validated_data)

        for electrical_charge in rs:
            print(electrical_charge.keys)
            instance.electrical_charges.add(
                list(electrical_charge.keys())[0],
                through_defaults={'quantity': list(electrical_charge.values())[0]}
            )

        return instance



