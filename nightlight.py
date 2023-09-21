#!/usr/bin/python
import RPi.GPIO as GPIO
import time
from rpi_ws281x import PixelStrip, Color, Adafruit_NeoPixel

SENSOR_PIN = 23
LIGHT_SENSOR_PIN = 21

GPIO.setmode(GPIO.BCM)
GPIO.setup(SENSOR_PIN, GPIO.IN)
GPIO.setup(LIGHT_SENSOR_PIN, GPIO.IN)

LED_COUNT = 15

led_duration = 0

strip = Adafruit_NeoPixel(LED_COUNT, 18, 800000, 5, False, 255)
strip.begin()


def turn_on_light(channel):
    if GPIO.input(LIGHT_SENSOR_PIN):
        # motion detected
        # reset LED duration
        global led_duration
        led_duration = 0
        colorWipe(strip, Color(255, 0, 32))
    else:
        # there was motion but it is not dark yet
        colorWipe(strip, Color(0, 0, 0))


def turn_off_light(channel):
    # turn off light
    colorWipe(strip, Color(0, 0, 0))


def colorWipe(strip, color, wait_ms=100):
    for i in range(strip.numPixels()):
        strip.setPixelColor(i, color)
        strip.show()
        time.sleep(wait_ms / 1000.0)


try:
    GPIO.add_event_detect(
        SENSOR_PIN, GPIO.RISING, callback=turn_on_light
    )
    GPIO.add_event_detect(
        LIGHT_SENSOR_PIN, GPIO.RISING, callback=turn_off_light, bouncetime=500
    )
    while True:
        if strip.getPixelColor(0) > 0:
            # check if LED is on for more than X seconds
            if led_duration > 180:
                # turn off LED
                colorWipe(strip, Color(0, 0, 0))
                led_duration = 0
            else:
                led_duration += 1
        else:
            led_duration = 0
        time.sleep(1)
except KeyboardInterrupt:
    colorWipe(strip, Color(0, 0, 0))
    print("Exiting...")
GPIO.cleanup()
