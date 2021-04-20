# script that reads temperature data from a DS18B20 temperature sensor, and
# sends that data to a mqtt server. if the sensor is the hottest, a return message
# will be sent triggering an LED to light.

from umqtt.simple import MQTTClient
from ds18x20_thermometer import TemperatureSensor
import machine
import utime
import uos
import ubinascii
import json

import config

# define pins
ONEWIRE_PIN = const(0)

# MQTT settings
SERVER = config.MQTT_ADDRESS
PORT = config.MQTT_PORT
CLIENT_ID = uos.uname()[0].upper().encode('utf-8') + b"-" + ubinascii.hexlify(machine.unique_id())
BASE_TOPIC = config.BASE_TOPIC

connect_msg = {
    'Connected Client ID': CLIENT_ID,
    'message type': 'on-connect'
}

# main loop
def run():
    print("** Temperature to MQTT lab **")
    try:
        sensor = TemperatureSensor(ONEWIRE_PIN)

        # connect to MQTT server
        c = MQTTClient(CLIENT_ID, SERVER, PORT)
        c.connect()
        print("connected to server {0}:{1}".format(SERVER, PORT))
        c.publish(BASE_TOPIC+b'/messages', json.dumps(connect_msg))

        while True:
            temperature = sensor.read_temp()
            print("Temperature: {}C".format(temperature))

            c.publish(BASE_TOPIC+b'/'+CLIENT_ID+b'/temperature', str(temperature))
            print("published message")

            utime.sleep(5)

    except KeyboardInterrupt:
        print("user terminated")
        print("goodbye")
    except:
        print("something went wrong")
    finally:
        c.disconnect()
