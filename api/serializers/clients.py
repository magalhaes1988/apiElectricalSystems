from rest_framework import serializers
from api.models.clients import Client


class ClientSerializer(serializers.ModelSerializer):

    class Meta:
        model = Client
        fields = ['uuid', 'name', 'cpf_cnpj', 'cep', 'public_place', 'neighborhood',
                  'city', 'state', 'create_at', 'update_at', 'delete_at', 'deleted']

        read_only_fields = ['uuid', 'create_at', 'update_at', 'delete_at']


    
    def validate(self, attrs):
        return super().validate(attrs)
