1.
from machine import Pin
import bluetooth
import time
led = Pin(2,Pin.OUT)
value = 0
name = "ESP32-JaskiratS  inghRangi" #Name of Your ESP32 (Change it to avoid Confusion)

ble = bluetooth.BLE()
ble.active(False)
time.sleep(0.5)
ble.active(True)
ble.config(gap_name=name)

SERVICE_UUID = bluetooth.UUID("6e400001-b5a3-f393-e0a9-e50e24dcca9e")
CHAR_UUID = bluetooth.UUID("6e400002-b5a3-f393-e0a9-e50e24dcca9e")

CHAR = (CHAR_UUID, bluetooth.FLAG_WRITE)
SERVICE = (SERVICE_UUID, (CHAR,),)
((char_handle,),) = ble.gatts_register_services((SERVICE,))

connections = set()

def irq(event, data):
    global connections
    if event == 1:
        conn_handle, addr_type, addr = data
        connections.add(conn_handle)
        print("Connected")
        
    elif event == 2:
        conn_handle, addr_type, addr = data
        connections.discard(conn_handle)
        print("Disconnected")
        advertise(name)
        
    elif event == 3:
        conn_handle, value_handle = data
        if value_handle == char_handle:
            msg = ble.gatts_read(char_handle).decode().strip() #reading the Value written on characteristics by Phone/client
            print("Received:", msg)
                
            global value
            value = msg[0]
     

            
ble.irq(irq)

def advertise(l_name):
    
    name_bytes = l_name.encode()

    flags = bytearray([0x02, 0x01, 0x06])
    short_name = bytearray([len(name_bytes) + 1, 0x08]) + name_bytes
    full_name = bytearray([len(name_bytes) + 1, 0x09]) + name_bytes
    adv_data = flags + short_name + full_name

    ble.gap_advertise(50, adv_data=adv_data)
    print("Advertising as:", l_name)

advertise(name)
print("Waiting for connection...")

while True:
    if value == '1':
        led.on()
        print("ON")
        value = 0
    elif value == '2':
        led.off()
        print("OFF")
        value = 0
    time.sleep(1)

2.
from machine import Pin
import bluetooth
import time
import random

name = "ESP32-Jassi" #Name of Your ESP32

ble = bluetooth.BLE()
ble.active(False)
time.sleep(0.5)
ble.active(True)
ble.config(gap_name=name)


SERVICE_UUID = bluetooth.UUID("6e400001-b5a3-f393-e0a9-e50e24dcca9e")
CHAR_UUID = bluetooth.UUID("6e400002-b5a3-f393-e0a9-e50e24dcca9e")

CHAR = (CHAR_UUID, bluetooth.FLAG_READ | bluetooth.FLAG_NOTIFY)

SERVICE = (SERVICE_UUID, (CHAR,),)

((char_handle,),) = ble.gatts_register_services((SERVICE,))

connections = set()

def irq(event, data):

    global connections

    if event == 1:  # Connected
        conn_handle, addr_type, addr = data
        connections.add(conn_handle)
        print("Connected")

    elif event == 2: # Disconnected
        conn_handle, addr_type, addr = data
        connections.remove(conn_handle)
        advertise(name)
        print("Disconnected")
                

ble.irq(irq)

def advertise(l_name):
        
    name_bytes = l_name.encode()

    flags = bytearray([0x02, 0x01, 0x06])
    short_name  = bytearray([len(name_bytes) + 1, 0x08]) + name_bytes
    full_name   = bytearray([len(name_bytes) + 1, 0x09]) + name_bytes
    adv_data = flags + short_name + full_name

    ble.gap_advertise(50, adv_data=adv_data)
    print("Advertising as:", l_name)


advertise(name)
print("Waiting for connection...")

while True:
    
    if connections:
        sensor_value = random.randint(0, 100) #Mimic Sensor Data
        print("Sending:", sensor_value)

        # Convert to bytes
        data = str(sensor_value)

        # Update characteristic value
        ble.gatts_write(char_handle, data)

        # Notify connected phone
        for conn_handle in connections:
            ble.gatts_notify(conn_handle, char_handle)
    time.sleep(1)

3.
from machine import Pin
import time

sensor = Pin(4, Pin.IN)

print("sensor initialization")
time.sleep(60)

while True:
    sensor_val= sensor.value()
    print(sensor_val)
    time.sleep(2)
    
    if sensor_val==1:
        print("motion detected")
    else:
        print("nothing moving")

4.
from machine import Pin,ADC
import time

sensor= ADC(4)
sensor.ATTN_11DB

led1 = Pin(12,Pin.OUT)
led2= Pin(14,Pin.OUT)

while True:
    sensor_val = sensor.read()
    print(sensor_val)
    time.sleep(0.5)
    
    if sensor_val > 4000:
        led1.on()
        led2.off()
    if sensor_val <= 4000:
        led2.on()
        led1.off()
    
    
        
