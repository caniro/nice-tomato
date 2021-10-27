import paho.mqtt.client as mqtt
from . import topicHandler, add_topic_handler
from .sensors import save_sensor

def on_connect(client, userdata, flags, rc):
    print("Connected with result code " + str(rc))
    if rc == 0:
        client.subscribe('iot/sensor/#')
    else:
        print('connection failed:', rc)

def on_message(client, userdata, msg):
    topic = msg.topic.split('/')[1] # sensor
    handler = topicHandler.get(topic)
    if handler:
        value = msg.payload.decode()
        handler(msg.topic, value)
    else:
        print('unknown topic:', msg.topic)

mqttClient = mqtt.Client()
mqttClient.on_connect = on_connect
mqttClient.on_message = on_message

try:
    mqttClient.connect('localhost')
    mqttClient.loop_start() # 웹서버와는 별도의 스레드로 구동
    add_topic_handler('sensor', save_sensor)

except Exception as e:
    print('error: ', e)
