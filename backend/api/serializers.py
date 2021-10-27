from rest_framework import serializers
from mqtt.models import Sensor

# Django의 모델 -> json 형식으로 직렬화
class SensorSerializer(serializers.ModelSerializer):
    count = serializers.IntegerField()
    avg = serializers.FloatField()
    regdate_h = serializers.DateTimeField()

    class Meta:
        model = Sensor
        fields = ('place', 'section', 'sensor', 'regdate_h', 'count', 'avg')

class SensorLastSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sensor
        exclude = []
