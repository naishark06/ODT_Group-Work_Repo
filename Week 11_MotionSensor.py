1. Motion Sensor
from machine import Pin
import time
sensor = Pin(4, Pin.IN)
print("Sensor Initialisation")
time.sleep(60)
while True:
    sensor_value = sensor.value()
    print(sensor_value)
    time.sleep(2)
    if sensor_value == 1:
        print("Motion Detected")

  2. Resistor 
from machine import Pin, ADC
import time
led1 = Pin(12, Pin.OUT)
led2 = Pin(14, Pin.OUT)
sensor = ADC(4)
sensor.ATTN_11DB
while True:
    sensor_val = sensor.read()
    print(sensor_val)
    time.sleep(0.5)
    if sensor_val < 4000:
        led1.on()
        led2.off()
    if sensor_cal >= 4000:
        led2.on()
        led1.off()
