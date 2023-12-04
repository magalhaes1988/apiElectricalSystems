from rest_framework.generics import ListCreateAPIView, ListAPIView, RetrieveUpdateDestroyAPIView
from rest_framework_extensions.mixins import NestedViewSetMixin
from rest_framework.pagination import PageNumberPagination
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.decorators import action

from api.models.loadGroup import LoadGroup
from api.serializers.loadGroup import LoadGroupSerializer


import uuid


def is_valid_uuid(value):
    try:
        uuid.UUID(str(value))
        return True

    except:
        return False



class LoadGroupApiV1Pagination(PageNumberPagination):
    page_size = 5


class LoadGroupApiV1ViewSet(NestedViewSetMixin, ModelViewSet):
    queryset = LoadGroup.objects.all().order_by('description')
    serializer_class = LoadGroupSerializer
    pagination_class = LoadGroupApiV1Pagination

    page_size = 2
    lookup_field = 'uuid'

    def get_queryset(self):
        qs = super().get_queryset()

        if self.request.resolver_match.view_name != 'api:loadGroup-deleted':
            match self.action:
                case 'list':
                    return qs.filter(deleted=False)
                case 'retrieve':
                    if self.kwargs[self.lookup_field] != '' and is_valid_uuid(self.kwargs[self.lookup_field]):
                        return qs.filter(uuid=self.kwargs[self.lookup_field])
                case _:
                    return qs
        else:
            return qs.filter(deleted=True)

    @action(methods=['get'], detail=False)
    def deleted(self, request):
        return Response(self.get_serializer(self.get_queryset(), many=True).data)

