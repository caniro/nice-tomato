#include <MCP3008.h> // https://github.com/nodesign/MCP3008
#include <MqttCom.h>

MCP3008 adc(D5, D7, D6, D8);
const int x_joystick = 0;
const int y_joystick = 1;
const int z_sw = D4;

const char *ssid = "HanGuest1";
const char *password = "00001234";
const char *mqtt_server = "192.168.117.22";
MqttCom com;

String SetDirection(const int& dx, const int& dy)
{
    const int one_third = 200;
    const int two_third = 1023 - one_third;

    if (dy < one_third)
    {
        if (dx < one_third)
            return String("tl");
        else if (dx < two_third)
            return String("u");
        else
            return String("tr");
    }
    else if (dy < two_third)
    {
        if (dx < one_third)
            return String("l");
        else if (dx < two_third)
            return String("s");
        else
            return String("r");
    }
    else
    {
        if (dx < one_third)
            return String("bl");
        else if (dx < two_third)
            return String("d");
        else
            return String("br");
    }
}

void ReadJoy()
{
    int dx = adc.readADC(x_joystick);
    int dy = adc.readADC(y_joystick);
    boolean sw = digitalRead(z_sw);
    Serial.println("----------------------");
    Serial.println("x_joystick: " + String(dx));
    Serial.println("y_joystick: " + String(dy));
    Serial.println("z_sw: " + String(sw));

    String direction = SetDirection(dx, dy);

    com.publish("iot/control/car", direction.c_str());
}

void setup()
{
    com.init(ssid, password);
    com.setServer(mqtt_server);
    com.setInterval(500, ReadJoy);
}

void loop()
{
    com.run();
}
