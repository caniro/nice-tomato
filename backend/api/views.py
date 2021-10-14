from rest_framework import viewsets
from mqtt.models import Sensor
from .serializers import SensorSerializer
from .paginations import SensorPageNumberPagination
from rest_framework.permissions import AllowAny
from datetime import datetime

class SensorViewSet(viewsets.ModelViewSet):
    now = datetime.today()
    start_time = "2021-10-14T03:00:00"
    queryset = Sensor.objects.filter(regdate__range=[start_time, now]).order_by('-regdate')
    serializer_class = SensorSerializer
    pagination_class = SensorPageNumberPagination
    permission_classes = (AllowAny, ) # jwt 인증 제외
