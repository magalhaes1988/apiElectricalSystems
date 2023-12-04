
from rest_framework.generics import ListAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.pagination import PageNumberPagination
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action, permission_classes
from rest_framework.permissions import IsAuthenticated
import uuid as uid

from ...models.clients import Client
from ...serializers.clients import ClientSerializer


def is_valid_uuid(value):
    try:
        uid.UUID(str(value))
        return True

    except:
        return False

class ClientApiV1Pagination(PageNumberPagination):

    page_size = 5


#@permission_classes([IsAuthenticated,])
class ClientApiV1ViewSet(viewsets.ModelViewSet):
    serializer_class = ClientSerializer
    pagination_class = ClientApiV1Pagination
    lookup_field = 'uuid'
    queryset = Client.objects.all().order_by('name')
    #permission_classes = [IsAuthenticated, ]


    def get_queryset(self):

        qs = super().get_queryset()

        if self.request.resolver_match.view_name != 'api:client-deleted':

            match self.action:
                case 'list':
                    return qs.filter(deleted=False)
                case 'retrieve':
                    if self.kwargs[self.lookup_field] != '' and is_valid_uuid(self.kwargs[self.lookup_field]):
                        return qs.filter(uuid=self.kwargs[self.lookup_field])
                case _:
                    return qs
        else:
            return qs.filter(deleted=True).order_by('name')

    @action(methods=['get'], detail=False)
    def deleted(self, request):
        serializer = self.get_serializer(self.get_queryset(), many=True)
        return Response(serializer.data)



