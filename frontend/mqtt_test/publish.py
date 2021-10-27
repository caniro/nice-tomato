import paho.mqtt.client as mqtt
from time import sleep
from random import uniform

client = mqtt.Client()

try:
    client.connect("localhost")
    while True:
        client.publish("iot/sensor/farm/section1/temp", f'{uniform(0, 100):.2f}')
        client.publish("iot/sensor/farm/section1/humi", f'{uniform(0, 100):.2f}')
        client.publish("iot/sensor/farm/section1/illu", f'{uniform(0, 100):.2f}')
        client.publish("iot/sensor/farm/section2/temp", f'{uniform(0, 100):.2f}')
        client.publish("iot/sensor/farm/section2/humi", f'{uniform(0, 100):.2f}')
        client.publish("iot/sensor/farm/section2/illu", f'{uniform(0, 100):.2f}')
        client.publish("iot/sensor/farm/section3/temp", f'{uniform(0, 100):.2f}')
        client.publish("iot/sensor/farm/section3/humi", f'{uniform(0, 100):.2f}')
        client.publish("iot/sensor/farm/section3/illu", f'{uniform(0, 100):.2f}')

        client.publish("iot/sensor/barn/section1/temp", f'{uniform(0, 100):.2f}')
        client.publish("iot/sensor/barn/section1/humi", f'{uniform(0, 100):.2f}')
        client.publish("iot/sensor/barn/section1/illu", f'{uniform(0, 100):.2f}')
        client.publish("iot/sensor/barn/section2/temp", f'{uniform(0, 100):.2f}')
        client.publish("iot/sensor/barn/section2/humi", f'{uniform(0, 100):.2f}')
        client.publish("iot/sensor/barn/section2/illu", f'{uniform(0, 100):.2f}')

        client.publish("iot/sensor/outdoor/section1/temp", f'{uniform(0, 100):.2f}')
        client.publish("iot/sensor/outdoor/section1/humi", f'{uniform(0, 100):.2f}')
        client.publish("iot/sensor/outdoor/section1/illu", f'{uniform(0, 100):.2f}')
        client.publish("iot/sensor/outdoor/section2/temp", f'{uniform(0, 100):.2f}')
        client.publish("iot/sensor/outdoor/section2/humi", f'{uniform(0, 100):.2f}')
        client.publish("iot/sensor/outdoor/section2/illu", f'{uniform(0, 100):.2f}')
        client.loop(2)
        sleep(5)
except Exception as err:
    print(f"에러: {err}")
