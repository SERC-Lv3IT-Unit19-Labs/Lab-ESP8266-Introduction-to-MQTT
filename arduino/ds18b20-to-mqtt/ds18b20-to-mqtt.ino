// Include the libraries we need
#include <OneWire.h>
#include <DallasTemperature.h>
#include <ESP8266WiFi.h>    // Include the Wi-Fi library
#include <PubSubClient.h>   // PubSubClient is a library that impliments the MQTT protocol
#include "config.h"

// Data wire is plugged into port 0 on the Wemos D1 mini
#define ONE_WIRE_BUS 0

// Setup a oneWire instance to communicate with any OneWire devices (not just Maxim/Dallas temperature ICs)
OneWire oneWire(ONE_WIRE_BUS);

// Pass our oneWire reference to Dallas Temperature. 
DallasTemperature sensors(&oneWire);

float celcius=0;

// Create MQTT client object
WiFiClient espClient;
PubSubClient client(espClient);

// topic to publish temperature values to
char* topic = baseTopic;
const char* msg;

/*
 * The setup function.
 *   - connect to WiFi
 *   - connect to MQTT broker
 *   - initialise sensors
 */
void setup(void)
{
  // start serial port
  Serial.begin(115200);
  Serial.println("DS18B20 Temperature Sensor to MQTT Lab");

  // Create and assign a hostname to the device
  // Hostname is generated as a prefix combined with the chid id code as a hexidecimal string
  WiFi.hostname("ESP8266-" + String(ESP.getChipId(), HEX));

  // Connect to the WiFi network
  WiFi.begin(ssid, password);
  Serial.print("Connecting to ");
  Serial.print(ssid); Serial.println(" ...");

  while (WiFi.status() != WL_CONNECTED) { // Wait for the Wi-Fi to connect
      delay(1000);
      Serial.print('.');
  }

  Serial.println("");
  Serial.println("Connection established!");
  Serial.print("IP address: ");
  Serial.println(WiFi.localIP());         // Send the IP address of the ESP8266 to the computer

  // Connect to MQTT broker
  client.setServer(mqttServer, 1883);
  Serial.println("");
  Serial.print("Connecting to MQTT broker at ");
  Serial.println(mqttServer);
  Serial.print("Attempting MQTT connection...");
  // Create a random client ID
  String clientId = "ESP8266Client-";
  clientId += String(random(0xffff), HEX);
  // Attempt to connect
  if (client.connect(clientId.c_str())) {
    Serial.println("connected");
    // Once connected, publish an announcement...
    client.publish("device-connected", "hello world");
  }
  
  // Start up the temperature sensor library
  sensors.begin();
}

/*
 * Main function, get and show the temperature
 */
void loop(void)
{ 
  // call sensors.requestTemperatures() to issue a global temperature 
  // request to all devices on the bus
  Serial.print("Requesting temperatures...");
  sensors.requestTemperatures(); // Send the command to get temperatures
  
  // After we got the temperatures, we can print them here.
  // We use the function ByIndex, and as an example get the temperature from the first sensor only.
  celcius=sensors.getTempCByIndex(0);
  Serial.print("Temperature: ");
  Serial.print(celcius);
  Serial.println(" C");

  // publish temperature reading to MQTT topic
  // publish() takes 2 arguments.
  //   topic - topic to publish payload to
  //   payload - data to be sent. needs to be of type char or int.
  client.publish(topic, String(celcius).c_str());
  Serial.print("Published temperature to ");
  Serial.println(topic);
  delay(2000);
}
