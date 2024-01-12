from django.urls import path, include
from rest_framework import routers
from . import views


router = routers.DefaultRouter()
router.register('list', views.PatientViewset)
urlpatterns = [
    path('', include(router.urls)),
    path('register/', views.UserRegistrationAPIView.as_view(), name='register'),
    path('login/', views.UserLoginAPIView.as_view(), name='login'),
    path('logout/', views.UserLogoutView.as_view(), name='logout'),
    path('active/<uid64>/<token>/', views.activate, name='activate')
]
