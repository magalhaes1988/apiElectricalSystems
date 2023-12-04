from django.urls import path

from api.views.api.projectViews import *

urlpatterns = [
    path('', ProjectsApiV1List.as_view(), name='activeProjects'),
    path('<uuid:uuid>/', ProjectApiV1Detail.as_view(), name='detailProject'),
    path('deleted/', ProjectsDeletedApiV1List.as_view(), name='deletedProjects'),
]
