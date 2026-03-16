1.
from machine import Pin
import time

red = Pin(15, Pin.OUT)
yellow = Pin(4, Pin.OUT)
green = Pin(5,Pin.OUT)

while True:
    #blink 3 times @interval of 0.5 seconds
    red.on()
    yellow.on()
    green.on()
    time.sleep(0.5)
    red.off()
    yellow.off()
    green.off()
    time.sleep(0.5)
    red.on()
    yellow.on()
    green.on()
    time.sleep(0.5)
    red.off()
    yellow.off()
    green.off()
    time.sleep(0.5)
    red.on()
    yellow.on()
    green.on()
    time.sleep(0.5)
    red.off()
    yellow.off()
    green.off()
    time.sleep(0.5)
    
    #constantly on for 2 seconds
    red.on()
    yellow.on()
    green.on()
    time.sleep(2)
    red.off()
    yellow.off()
    green.off()
    time.sleep(1)
    
    #right moving pattern with speed of 0.3 seconds in between each LED-once
    red.on()
    time.sleep(0.3)
    red.off()
    yellow.on()
    time.sleep(0.3)
    yellow.off()
    green.on()
    time.sleep(0.3)
    green.off()
    
    #Blink 3 times @ blink interval of 1 seconds
    red.on()
    yellow.on()
    green.on()
    time.sleep(1)
    red.off()
    yellow.off()
    green.off()
    time.sleep(1)
    red.on()
    yellow.on()
    green.on()
    time.sleep(1)
    red.off()
    yellow.off()
    green.off()
    time.sleep(1)
    red.on()
    yellow.on()
    green.on()
    time.sleep(1)
    red.off()
    yellow.off()
    green.off()
    time.sleep(1)

2.
from machine import Pin
import time

red = Pin(15, Pin.OUT)
yellow = Pin(4, Pin.OUT)
green = Pin(5,Pin.OUT)

def pattern_1(s):
    for i in range(2):
        red.on()
        yellow.on()
        green.on()
        time.sleep(s)
        red.off()
        yellow.off()
        green.off()
        
def pattern_2():
    red.on()
    yellow.on()
    green.on()
    time.sleep(2)
    red.off()
    yellow.off()
    green.off()
    time.sleep(2)
    
def pattern_3():
    red.on()
    time.sleep(0.3)
    red.off()
    yellow.on()
    time.sleep(0.3)
    yellow.off()
    green.on()
    time.sleep(0.3)
    green.off()

def pattern_4():
    for a in range(2):
        red.on()
        yellow.on()
        green.on()
        time.sleep(1)
        red.off()
        yellow.off()
        green.off()
        time.sleep(1)
    

while True:
    pattern_1(2)
    pattern_2()
    pattern_3()
    pattern_4()
    pattern_4()
    pattern_4()
    print("done")

3.
from machine import Pin
import bluetooth
import time

ble = bluetooth.BLE()
ble.active(True)

# UUIDs
SERVICE_UUID = bluetooth.UUID("6e400001-b5a3-f393-e0a9-e50e24dcca9e")
CHAR_UUID = bluetooth.UUID("6e400002-b5a3-f393-e0a9-e50e24dcca9e")

# Characteristic only needs WRITE
CHAR = (CHAR_UUID, bluetooth.FLAG_WRITE)

SERVICE = (SERVICE_UUID, (CHAR,),)

((char_handle,),) = ble.gatts_register_services((SERVICE,))

connections = set()

def irq(event, data):
    
    global connections
    # Event 1 → Phone Connected
    if event == 1:
        conn_handle, addr_type, addr = data
        connections.add(conn_handle)
        print("Phone connected")
    
    # Event 2 → Phone Disconnected
    elif event == 2:
        conn_handle, addr_type, addr = data
        connections.remove(conn_handle)
        print("Phone disconnected")
        advertise()
        
    # Event 3 → phone wrote data
    elif event == 3:
        conn_handle, value_handle = data

        if value_handle == char_handle:

            msg = ble.gatts_read(char_handle).decode().strip()

            print("Received from phone:", msg)
            

ble.irq(irq)


def advertise():
    name = "ESP32-GOOBE"

    adv_data = bytearray()
    adv_data += bytearray((len(name) + 1, 0x09)) + name.encode()

    ble.gap_advertise(100, adv_data)

    print("Advertising as:", name)


advertise()

print("Waiting for phone connection...")

while True:
    time.sleep(1)

4.
from machine import Pin
import bluetooth
import time

led1= Pin(4,Pin.OUT)
led2= Pin(5, Pin.OUT)
led3= Pin(19,Pin.OUT)
    
led1.off()
led2.off()
led3.off()

ble = bluetooth.BLE()
ble.active(True)

# UUIDs
SERVICE_UUID = bluetooth.UUID("6e400001-b5a3-f393-e0a9-e50e24dcca9e")
CHAR_UUID = bluetooth.UUID("6e400002-b5a3-f393-e0a9-e50e24dcca9e")

# Characteristic only needs WRITE
CHAR = (CHAR_UUID, bluetooth.FLAG_WRITE)

SERVICE = (SERVICE_UUID, (CHAR,),)

((char_handle,),) = ble.gatts_register_services((SERVICE,))

connections = set()

def irq(event, data):
    
    global connections
    # Event 1 → Phone Connected
    if event == 1:
        conn_handle, addr_type, addr = data
        connections.add(conn_handle)
        print("Phone connected")
    
    # Event 2 → Phone Disconnected
    elif event == 2:
        conn_handle, addr_type, addr = data
        connections.remove(conn_handle)
        print("Phone disconnected")
        advertise()
        
    # Event 3 → phone wrote data
    elif event == 3:
        conn_handle, value_handle = data

        if value_handle == char_handle:

            msg = ble.gatts_read(char_handle).decode().strip()

            print("Received from phone:", msg)
            

            if msg== '1':
                led1.on()
            elif msg== '2':
                led2.on()
            elif msg == '3':
                led3.on()
            elif msg == '4':
                led1.off()
                led2.off()
                led3.off()
            

ble.irq(irq)


def advertise():
    name = "ESP32-GOOBE"

    adv_data = bytearray()
    adv_data += bytearray((len(name) + 1, 0x09)) + name.encode()

    ble.gap_advertise(100, adv_data)

    print("Advertising as:", name)


advertise()

print("Waiting for phone connection...")

while True:
    time.sleep(1)

5.
from machine import Pin
import bluetooth
import time

red= Pin(4,Pin.OUT)
yellow= Pin(5, Pin.OUT)
green= Pin(19,Pin.OUT)

def pattern_1():
    for i in range(2):
        red.on()
        yellow.on()
        green.on()
        time.sleep(0.5)
        red.off()
        yellow.off()
        green.off()
        
def pattern_2():
    red.on()
    yellow.on()
    green.on()
    time.sleep(2)
    red.off()
    yellow.off()
    green.off()
    time.sleep(2)
    
def pattern_3():
    red.on()
    time.sleep(0.3)
    red.off()
    yellow.on()
    time.sleep(0.3)
    yellow.off()
    green.on()
    time.sleep(0.3)
    green.off()

def pattern_4():
    for a in range(2):
        red.on()
        yellow.on()
        green.on()
        time.sleep(1)
        red.off()
        yellow.off()
        green.off()
        time.sleep(1)
    
    
red.off()
yellow.off()
green.off()

ble = bluetooth.BLE()
ble.active(True)

# UUIDs
SERVICE_UUID = bluetooth.UUID("6e400001-b5a3-f393-e0a9-e50e24dcca9e")
CHAR_UUID = bluetooth.UUID("6e400002-b5a3-f393-e0a9-e50e24dcca9e")

# Characteristic only needs WRITE
CHAR = (CHAR_UUID, bluetooth.FLAG_WRITE)

SERVICE = (SERVICE_UUID, (CHAR,),)

((char_handle,),) = ble.gatts_register_services((SERVICE,))

connections = set()

def irq(event, data):
    
    global connections
    # Event 1 → Phone Connected
    if event == 1:
        conn_handle, addr_type, addr = data
        connections.add(conn_handle)
        print("Phone connected")
    
    # Event 2 → Phone Disconnected
    elif event == 2:
        conn_handle, addr_type, addr = data
        connections.remove(conn_handle)
        print("Phone disconnected")
        advertise()
        
    # Event 3 → phone wrote data
    elif event == 3:
        conn_handle, value_handle = data

        if value_handle == char_handle:

            msg = ble.gatts_read(char_handle).decode().strip()

            print("Received from phone:", msg)
            

            if msg== '1':
                pattern_1()
            elif msg== '2':
                pattern_2()
            elif msg == '3':
                pattern_3()
            elif msg == '4':
                pattern_4()
            elif msg == '5':
                red.off()
                yellow.off()
                green.off()
            

ble.irq(irq)


def advertise():
    name = "ESP32-GOOBE"

    adv_data = bytearray()
    adv_data += bytearray((len(name) + 1, 0x09)) + name.encode()

    ble.gap_advertise(100, adv_data)

    print("Advertising as:", name)


advertise()

print("Waiting for phone connection...")

while True:
    time.sleep(1)
6.
import bluetooth
import random
import time
from micropython import const

# BLE event constants
_IRQ_CENTRAL_CONNECT = const(1)
_IRQ_CENTRAL_DISCONNECT = const(2)

# Create BLE object
ble = bluetooth.BLE()
ble.active(True)

# UUIDs for the service and characteristic
SERVICE_UUID = bluetooth.UUID("12345678-1234-5678-1234-56789abcdef0")
CHAR_UUID = bluetooth.UUID("12345678-1234-5678-1234-56789abcdef1")

# Characteristic properties: Notify + Read
CHARACTERISTIC = (
    CHAR_UUID,
    bluetooth.FLAG_NOTIFY | bluetooth.FLAG_READ,
)

# Create service
SERVICE = (
    SERVICE_UUID,
    (CHARACTERISTIC,),
)

# Register service
((char_handle,),) = ble.gatts_register_services((SERVICE,))

connections = set()

# BLE interrupt handler
def ble_irq(event, data):
    global connections
    
    if event == _IRQ_CENTRAL_CONNECT:
        conn_handle, addr_type, addr = data
        print("Phone connected")
        connections.add(conn_handle)

    elif event == _IRQ_CENTRAL_DISCONNECT:
        conn_handle, addr_type, addr = data
        print("Phone disconnected")
        connections.remove(conn_handle)
        advertise()  # restart advertising

ble.irq(ble_irq)

# Advertising function
def advertise():
    name = "ESP32-Kothi"

    adv_data = bytearray()
    adv_data += bytearray((len(name) + 1, 0x09)) + name.encode()

    ble.gap_advertise(100, adv_data)

    print("Advertising as:", name)


advertise()

# Main loop
while True:

    if connections:
        sensor_value = random.randint(0, 100)
        print("Sending:", sensor_value)

        # Convert to bytes
        data = str(sensor_value)

        # Update characteristic value
        ble.gatts_write(char_handle, data)

        # Notify connected phone
        for conn_handle in connections:
            ble.gatts_notify(conn_handle, char_handle)

    time.sleep(2)
