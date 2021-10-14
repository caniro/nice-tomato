from rest_framework import serializers
from mqtt.models import Sensor

# Django의 모델 -> json 형식으로 직렬화
class SensorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sensor
        exclude = []
