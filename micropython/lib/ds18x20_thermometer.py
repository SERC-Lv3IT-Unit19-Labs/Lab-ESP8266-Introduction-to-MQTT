import time

from ds18x20 import DS18X20
from machine import Pin
from onewire import OneWire


class TemperatureSensor:
    """
    Represents a Temperature sensor
    """

    def __init__(self, pin):
        """
        Finds addresses of DS18B20 on bus specified by `pin`
        :param pin: 1-Wire bus pin
        :type pin: int
        """
        self.ds = DS18X20(OneWire(Pin(pin)))
        self.addrs = self.ds.scan()
        if not self.addrs:
            raise Exception('no DS18B20 found at bus on pin %d' % pin)
        # save what should be the only address found
        # self.addr = addrs.pop()

    def read_temp(self, fahrenheit=False, multiple=False):
        """
        Reads temperature from one or many DS18X20
        :param fahrenheit: Whether or not to return value in Fahrenheit
        :type fahrenheit: bool
        :param multiple: Whether to return readings from multiple sensors, or just the first
        :type multiple: bool
        :return: Temperature
        :rtype: float/list
        """

        self.ds.convert_temp()
        time.sleep_ms(750)

        # if multiple:
        #     temps = []
        #     for addr in self.addrs:
        #         temp = self.ds.read_temp(addr)
        #         if fahrenheit:
        #             temp = self.c_to_f(temp)
        #         temps.append(temp)
        #     return temps
        # else:
        #     temp = self.ds.read_temp(self.addrs[0])
        #     if fahrenheit:
        #         temp = self.c_to_f(temp)
        #     return temp
        
        temps = []
        for addr in self.addrs:
            temp = self.ds.read_temp(addr)
            if fahrenheit:
                temp = self.c_to_f(temp)
            temps.append(temp)
        
        if multiple:
            return temps
        else:
            return temps[0]
        
    @staticmethod
    def c_to_f(c):
        """
        Converts Celsius to Fahrenheit
        :param c: Temperature in Celsius
        :type c: float
        :return: Temperature in Fahrenheit
        :rtype: float
        """
        return (c * 1.8) + 32
