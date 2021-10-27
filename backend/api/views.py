from django.db.models import Avg, Sum, Count, query, Max, F
from django.db.models.functions import Trunc
from rest_framework import viewsets
from mqtt.models import Sensor
from .serializers import SensorSerializer, SensorLastSerializer
from .paginations import SensorPageNumberPagination
from datetime import datetime, timedelta

class SensorViewSet(viewsets.ModelViewSet):
    queryset = Sensor.objects.all() # 성능 이슈 있는지?
    serializer_class = SensorSerializer

    def get_queryset(self):
        now = datetime.today()
        start_time = now - timedelta(hours=12)
        place = self.request.query_params.get('place', '')
        section = self.request.query_params.get('section', '')
        queryset = Sensor.objects\
            .filter(regdate__gte=start_time, place=place, section=section)\
            .annotate(regdate_h=Trunc('regdate', 'hour'))\
            .values('place', 'section', 'sensor', 'regdate_h')\
            .annotate(count=Count('id'), avg=Avg('value'))

        return queryset

class SensorLastViewSet(viewsets.ModelViewSet):
    queryset = Sensor.objects.order_by('-regdate')[:100]

    serializer_class = SensorLastSerializer
    pagination_class = SensorPageNumberPagination
