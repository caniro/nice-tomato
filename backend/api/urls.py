from django.urls import path, include
from rest_framework import routers
from api.views import *

router = routers.DefaultRouter()

router.register('sensor', SensorViewSet) # api/sensor
router.register('last', SensorLastViewSet) # api/sensor

urlpatterns = [
    path('', include(router.urls)),
]
