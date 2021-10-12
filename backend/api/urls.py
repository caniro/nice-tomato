from django.urls import path, include
from rest_framework import routers
from api.views import *

router = routers.DefaultRouter()

# router.register('video', VideoViewSet)          # api/video

urlpatterns = [
    path('', include(router.urls)),
]
