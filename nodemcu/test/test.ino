#include <MqttCom.h>
#include <DHT.h>
#include <Analog.h>
#include <Led.h>
#include <ArduinoJson.h>

const char *ssid = "HanGuest1";
const char *password = "00001234";
const char *mqtt_server = "192.168.117.22";

MqttCom com;
DHT dht11(D6, DHT11);
Analog cds(A0, 100, 0);
// D1, D2는 MiniCom의 I2C 통신때문에 사용 못하는 듯
Led led(D8);
int target_illu = 0;

const int doc_size = 512;
String g_place("barn");
String g_section("section1");
String sensor_topic = "iot/sensor/" + g_place + "/" + g_section + "/";

StaticJsonDocument<doc_size> Deserialize(const String& str)
{
    StaticJsonDocument<doc_size> doc;

    auto error = deserializeJson(doc, String(str));
    if (error)
    {
        Serial.print("deserializeJson() failed with code");
        Serial.println(error.c_str());
    }
    return doc;
}

void ControlLed(const int value)
{
    Serial.println(value);
    Serial.println(target_illu);
    if (target_illu < value)
        led.off();
    else
        led.on();
}

void Callback(char *topic, byte *payload, unsigned int length)
{
    char buf[doc_size];
    memcpy(buf, payload, length);
    buf[length] = '\0';

    auto doc = Deserialize(buf);
    String place = doc["place"];
    String section = doc["section"];
    String temp = doc["temp"];
    String humi = doc["humi"];
    String illu = doc["illu"];

    if (place != g_place || section != g_section)
        return ;

    target_illu = illu.toInt();
    Serial.print("target illu : ");
    Serial.println(target_illu);
}

void Publish()
{
    char msg[50];
    float fc = dht11.readTemperature();
    float fh = dht11.readHumidity();
    int illu = cds.read();

    if (isnan(fh) || isnan(fc))
    {
        Serial.println("DHT11 read failed");
        return ;
    }

    com.publish((sensor_topic + "temp").c_str(), fc);
    com.publish((sensor_topic + "humi").c_str(), fh);
    com.publish((sensor_topic + "illu").c_str(), illu);

    ControlLed(illu);
}

void setup()
{
    com.init(ssid, password);
    com.setServer(mqtt_server, "iot/control", Callback);
    com.setInterval(10000, Publish);
    dht11.begin();
}

void loop()
{
    com.run();
}
