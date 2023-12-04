from rest_framework import serializers

from api.models.projects import Project
from api.models.clients import Client

from api.serializers.clients import ClientSerializer


class ProjectSerializer(serializers.ModelSerializer):

    class Meta:
        model = Project
        fields = ['uuid', 'project_id', 'project_description', 'client', 'client_link',
                  'create_at', 'update_at', 'delete_at', 'deleted'
                  ]
        read_only_fields = ['client_link']

    client = serializers.StringRelatedField(
        many=False,
        read_only=False
    )

    client_link = serializers.HyperlinkedRelatedField(
        many=False,
        source='client',
        lookup_field='uuid',
        read_only=True,
        view_name='api:client-detail'
    )




