from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework_extensions.mixins import NestedViewSetMixin
from rest_framework.pagination import PageNumberPagination
from rest_framework.decorators import action
from api.models.electricalCharges import ElectricalCharges
from api.serializers.electricalCharges import ElectricalChargesSerializer
import uuid


def is_valid_uuid(value):
    try:
        uuid.UUID(str(value))
        return True

    except:
        return False

class ElectricalChargerApiV1Pagination(PageNumberPagination):
    page_size = 5


class ElectricalChargesApiV1ViewSet(NestedViewSetMixin, ModelViewSet):
    queryset = ElectricalCharges.objects.order_by('group').all()
    serializer_class = ElectricalChargesSerializer
    pagination_class = ElectricalChargerApiV1Pagination
    lookup_field = 'uuid'


    def get_queryset(self):

        qs = super().get_queryset()

        if self.request.resolver_match.view_name != 'api:electricalcharges-deleted':
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
        return Response(
            self.get_serializer(self.get_queryset().delete(), many=True).data
        )
    #
    # @action(methods=['get'], detail=False)
    # def bygroup(self, request, group=None):
    #     print(request)
    #     return Response(
    #         self.get_serializer(self.get_queryset(), many=True).data
    #     )
