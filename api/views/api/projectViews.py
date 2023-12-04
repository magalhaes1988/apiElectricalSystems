
from rest_framework.decorators import action
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import ListCreateAPIView, ListAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.pagination import PageNumberPagination
from django.shortcuts import get_object_or_404


from ...models.clients import Client
from ...models.projects import Project
from ...serializers.projects import ProjectSerializer
import uuid


def is_valid_uuid(value):
    try:
        uuid.UUID(str(value))
        return True

    except:
        return False


class ProjectApiV1Pagination(PageNumberPagination):
    page_size = 5


class ProjectApiV1ViewSet(ModelViewSet):
    queryset = Project.objects.all().order_by('project_id')
    serializer_class = ProjectSerializer
    pagination_class = ProjectApiV1Pagination
    lookup_field = 'uuid'
    permission_classes = []

    def get_queryset(self):
        qs = super().get_queryset()

        if self.request.resolver_match.view_name != 'api:projects-deleted':
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

    def partial_update(self, request, *args, **kwargs):
        kwargs['partial'] = True
        return self.update(request, *args, **kwargs)

    def perform_create(self, serializer):
        serializer.save(Client.objects.get(uuid=self.request.data['client']))

#
# class ProjectsApiV1List(ListCreateAPIView):
#     queryset = Project.objects.not_deleted()
#     serializer_class = ProjectSerializer
#     pagination_class = ProjectApiV1Pagination
#     lookup_field = 'uuid'
#
#     def perform_create(self, serializer):
#         serializer.save(client=Client.objects.get(uuid=self.request.data['client']))
#
#
# class ProjectApiV1Detail(RetrieveUpdateDestroyAPIView):
#     queryset = Project.objects.all()
#     serializer_class = ProjectSerializer
#     pagination_class = ProjectApiV1Pagination
#     lookup_field = 'uuid'
#
#
# class ProjectsDeletedApiV1List(ListAPIView):
#     queryset = Project.objects.deleted()
#     serializer_class = ProjectSerializer
#     pagination_class = ProjectApiV1Pagination
#     lookup_field = 'uuid'

