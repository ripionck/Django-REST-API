from django.urls import path, include
from rest_framework import routers
from . import views


router = routers.DefaultRouter()
router.register('list', views.PatientViewset)
urlpatterns = [
    path('', include(router.urls))
]
