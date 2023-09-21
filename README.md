# Raspberry Pi nightlight

A simple Python script which turns your Raspberry Pi into a motion activated nightlight.

## Installation

You will need the following dependencies:

```
pip3 install RPi.GPIO rpi-ws281x
```

Clone this repo or just download the python script and put it into `/usr/local/bin` for example and make it executeable.

```
chmod +x /usr/local/bin/nightlight.py
```


Probably you want to start this script at boot, put this in `/etc/cron.d/nightlight`
```
@reboot root /usr/local/bin/nightlight.py > /dev/null 2>&1
```

## GPIO PINs

Connect the PIR sensor as following (I have used a HC-SR501):

```
VCC: 5V
DATA: GPIO 23
GND: GND
```

Connect the Neopixel strip (some ws281x will do) as following:

```
VCC: 5V
DATA: GPIO 18
GND: GND
```
