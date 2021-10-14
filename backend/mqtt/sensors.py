from . import add_topic_handler
from .models import Sensor

def save_sensor(topic, value):
    value = float(value)
    # 토픽 형식 : iot/sensor/place/section/type
    _, _, place, section, sensor = topic.split('/')
    s = Sensor(place=place, section=section,
            sensor=sensor, value=value)
    s.save()

# add_topic_handler('iot/sensor/#', save_sensor) # 와일드카드 적용 안됨(사전의 키니까)
if __name__=='__main__':
    add_topic_handler('sensor', save_sensor)
