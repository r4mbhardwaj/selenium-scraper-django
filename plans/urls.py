from django.urls import path, include
from .views import *

# django rest framework
from rest_framework import routers
from rest_framework.routers import DefaultRouter

router = routers.DefaultRouter()
router.register(r'plans', PlanViewSet)

urlpatterns = [
    path('', PlanList.as_view()),
    # rest framework
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]