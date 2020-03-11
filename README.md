# Lab Exercise - ESP8266 and MQTT

This lab will introduce students to using MQTT with an ESP8266. A DS18B20 temperature sensor is also used in the lab.

### MQTT

MQTT (MQ Telemetry Transport) is a lightweight publish/subscribe messaging protocol.


### DS18B20 Temperature Sensor

![sensor](assets/ds18b20_1.jpg)

The DS18B20 digital thermometer provides 9-bit to 12-bit Celsius temperature measurements in the range -55°C to +125°C. The DS18B20 uses a 1-wire serial protocol. Multiple devices can share the same 1-wire bus as each device has a unique 64-bit serial code. The DS18B20 can be powered by a supply between 3.0V and 5.5V.



## Exercise 1

First, we will build and test a circuit using the temperature sensor.

#### Components Needed
* DS18B20 temperature sensor
* 4k7 resistor
* connecting wires
* esp8266 development board (e.g. Wemos D1 mini)

### Instructions

1. Wire up the components as shown in the diagrams. The data line (DQ) needs to be pulled high using a 4k7 ohm resistor.
   
   ![circuit diagram](assets/esp8266-ds18b20-temp-sensor-circuit-diagram_schem.png)
   <br />
   ![breadboard diagram](assets/esp8266-ds18b20-temp-sensor-circuit-diagram_bb.png)

   ### Default Pin Wiring

    | Pin No | Function | Device Connection |
    | --- | --- | --- |
    | 3V3 | +3.3V | Vdd |
    | G | GND | GND |
    | D3 | GPIO 0 | DQ |

2. Make sure the temperature sensor is wired the correct way round!

3. Open the [ds18b20-simple](arduino/ds18b20-simple/ds18b20-simple.ino) sketch and run it.

4. Open the serial monitor and check that the sensor is working correctly. ![serial monitor button](assets/serial-monitor-button.png)

Q1. What cable carries the data?

Q2. What libraries are needed to run this sketch?

Q3. What are libraries (in this context)? How are they helpful?

## Exercise 2

## Exercise 3

