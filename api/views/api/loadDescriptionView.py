from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework_extensions.mixins import NestedViewSetMixin
from rest_framework.pagination import PageNumberPagination
from rest_framework.decorators import action
from api.models.loadDescription import LoadDescription
from api.models.loadProjectByCircuit import LoadDescriptionByCircuit
from api.serializers.loadDescription import LoadDescriptionSerializer, LoadDescriptionByCircuitSerializer
from api.models.electricalCharges import ElectricalCharges
from rest_framework.status import HTTP_201_CREATED
import uuid


def is_valid_uuid(value):
    try:
        uuid.UUID(str(value))
        return True

    except:
        return False


class LoadDescriptionApiV1Pagination(PageNumberPagination):
    page_size = 5

class Test(ModelViewSet):
    queryset = LoadDescriptionByCircuit.objects.all()
    serializer_class = LoadDescriptionByCircuitSerializer
class LoadDescriptionApiV1View(ModelViewSet):
    #queryset = LoadDescription.objects.all().prefetch_related('electrical_charges')
    queryset = LoadDescription.objects.all()
    serializer_class = LoadDescriptionSerializer
    pagination_class = LoadDescriptionApiV1Pagination
    lookup_field = 'uuid'

    def get_queryset(self):

        qs = super().get_queryset()

        if self.request.resolver_match.view_name != 'api:loaddescription-deleted':
            match self.action:
                case 'list':
                    return qs
                case 'retrieve':
                    if self.kwargs[self.lookup_field] != '' and is_valid_uuid(self.kwargs[self.lookup_field]):
                        return qs.filter(uuid=self.kwargs[self.lookup_field])
                case _:
                    return qs

        else:
            return qs


    def create(self, request, *args, **kwargs):
        electrical = request.data.pop('electrical')

        serializer = self.serializer_class(data=request.data, context={'electrical': electrical})
        serializer.is_valid(raise_exception=False)
        serializer.save()
    #
    #     serializer = self.get_serializer()
    #     print(**kwargs)
    #
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=HTTP_201_CREATED,headers=headers)

    #def perform_create(self, serializer):
        #electrical_charges =
        #print(f'Na View Request: {self.request.data}')
        #serializer.save(data=self.request.data)

