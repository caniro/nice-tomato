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
// Analog cds(A0, 0, 100);
// temperature led pin = D7, D5, D3
Led led(D8);
Led led1(D7);
Led led2(D5);
Led led3(D3);

int target_illu = 20;
int target_temp = 20;

const int doc_size = 512;
String g_place("farm2");
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

void TempControlled(const int value) 
{
    // 목표 값과 측정 값의 차이가 15도 이하
    if (target_temp - value < 15)
        led1.off();
    else if (target_temp - value >= 15)
        led1.on();
        
    // 10도 이하
    if (target_temp - value < 10)
        led2.off();
    else if (target_temp - value >= 10)
        led2.on();
        
    // 5도 이하
    if (target_temp - value < 5)
        led3.off();
    else if (target_temp - value >= 5)
        led3.on();

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

    if (illu.toInt() >= 1)
    {
        target_illu = illu.toInt();
        Serial.print("target illu : ");
        Serial.println(target_illu);
    }
    if (temp.toInt() >= 1)
    {
        target_temp = temp.toInt();
        Serial.print("target temp : ");
        Serial.println(target_temp);
    }
}

void Publish()
{
    char msg[50];
    float fc = dht11.readTemperature();
    float fh = dht11.readHumidity();
    int illu = analogRead(A0);
    illu = map(illu, 0, 1023, 100, 0);
    Serial.println(illu);
    // int illu = cds.read();
    if (isnan(fh) || isnan(fc))
    {
        Serial.println("DHT11 read failed");
        return ;
    }

    com.publish((sensor_topic + "temp").c_str(), fc);
    com.publish((sensor_topic + "humi").c_str(), fh);
    com.publish((sensor_topic + "illu").c_str(), illu);

    ControlLed(illu);
    TempControlled(fc);
}

void setup()
{
    com.init(ssid, password);
    com.setServer(mqtt_server, "iot/control", Callback);
    com.setInterval(2000, Publish);
    dht11.begin();
}

void loop()
{
    com.run();
}
