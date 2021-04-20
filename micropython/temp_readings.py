# micropython script that outputs the temperature from a 1-wire sensor to the REPL
import time
from ds18x20_thermometer import TemperatureSensor

# define onewire bus pin
ONEWIRE_PIN = 0

sensor = TemperatureSensor(ONEWIRE_PIN)

try:
    while True:
        # get sensor temperature and store value in variable 'temperature'
        temperature = sensor.read_temp()

        # print value to console.
        # {} is used in conjunction with format() for substitution.
        # .2f       - format to 2 decimal places.
        # end='\r'  - curser will go to the start of the current line instead of making a new line.
        print("Temperature is {:.2f} celsius".format(temperature), end='\r')
        time.sleep(1)

except KeyboardInterrupt:
    print('script stopped by user')
finally:
    print('Goodbye!')
