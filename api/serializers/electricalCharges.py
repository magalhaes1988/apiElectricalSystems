from rest_framework import serializers
from rest_framework.relations import StringRelatedField

from api.models.electricalCharges import ElectricalCharges


class ElectricalChargesSerializer(serializers.ModelSerializer):

    class Meta:
        model = ElectricalCharges
        fields = '__all__'
        extra_fields = ['quantity']


    group = serializers.StringRelatedField(
        many=False,
        read_only=False,
    )

    group_link = serializers.HyperlinkedRelatedField(
        many=False,
        source='group',
        lookup_field='uuid',
        read_only=True,
        view_name='api:loadgroup-detail'
    )
