from rest_framework import serializers
from api.models.loadGroup import LoadGroup


class LoadGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = LoadGroup
        fields = ['uuid', 'description','create_at', 'update_at', 'delete_at', 'deleted']

        read_only_fields = ['uuid', 'create_at', 'update_at', 'delete_at']

