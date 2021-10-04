/********************
* this program allow to send a get request on a specified url from ESP01
* it is usefull as a remote controler for the raspberry-pi in InstagramAutoPoster project
* using a push button, this program connect to specified wifi, send a get request to the server and get back to (deep)sleep
* olivain.art
**************/
#include <ESP8266WiFi.h>
#include <ESP8266HTTPClient.h>
#define _RPI_URL_ "http://192.168.0.1/takeapicandpost"

void setup() {
  Serial.begin(115200);
  Serial.println();

  WiFi.begin("WiFiSSID", "WiFiPassword");
  Serial.print("Connecting");
  while (WiFi.status() != WL_CONNECTED)
  {
    delay(10);
  }
  HTTPClient http;  //Declare an object of class HTTPClient
  http.begin(_RPI_URL_);
  http.GET();                                  //Send the request
  http.end();   //Close connection
  ESP.deepSleep(0);
}

void loop(){}
