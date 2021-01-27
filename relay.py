import time
import digitalio
import board
from Adafruit_IO import Client, Feed, RequestError
ADAFRUIT_IO_KEY = 'your AIO KEY' # Set your APIO Key
 # Set to your Adafruit IO username.
ADAFRUIT_IO_USERNAME = 'YOUR AIO User'
aio = Client(ADAFRUIT_IO_USERNAME, ADAFRUIT_IO_KEY)
try:
    digital = aio.feeds('your AIO feed')
except RequestError:
    feed = Feed(name="your AIO feed")
    LED = aio.create_feed(feed)
# led set up and button
led = digitalio.DigitalInOut(board.D6)
led.direction = digitalio.Direction.OUTPUT
taster = digitalio.DigitalInOut(board.D5)
taster.direction = digitalio.Direction.INPUT
while True:
    data = aio.receive(digital.key)
    if int(data.value) == 1:
        print('received <- ON\n')
        led.value = 0
        time.sleep(1)
        led.value = 1
        aio.send('your AIO feed',0)
        print('trigger reset\n')
    elif int(data.value) == 0:
        print('received <- OFF\n')

    led.value = 1
# button read
    if int(taster.value) == 1:
        print('taster on\n')
        led.value = 0
        time.sleep(10)
    else:
        print('teaster off\n')
        led.value = 1
