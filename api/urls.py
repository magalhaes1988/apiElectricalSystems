"""
URL configuration for apiElectricalSystems project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework_extensions.routers import DefaultRouter
from .views.api.clientViews import ClientApiV1ViewSet
from .views.api.loadGroupViews import LoadGroupApiV1ViewSet
from .views.api.projectViews import ProjectApiV1ViewSet
from .views.api.electricalChargesViews import ElectricalChargesApiV1ViewSet
from .views.api.loadDescriptionView import LoadDescriptionApiV1View,Test


app_name = 'api'

router = DefaultRouter(
    trailing_slash=True
)
router.register(r'clients', ClientApiV1ViewSet)
router.register(r'loadgroup', LoadGroupApiV1ViewSet)
router.register(r'projects', ProjectApiV1ViewSet)
router.register(r'electricalcharges', ElectricalChargesApiV1ViewSet)
router.register(r'loaddescription', LoadDescriptionApiV1View)
router.register(r'teste', Test)

#electrical_route = router.register(r'electricalcharges', ElectricalChargesApiV1ViewSet)
#electrical_route.register(r'group_by', LoadGroupApiV1ViewSet, basename='group_by', parents_query_lookups=['description'])



urlpatterns = [


    path('', include(router.urls)),
]
