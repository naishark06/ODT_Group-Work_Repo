1. 
from machine import Pin
import bluetooth
import time
import random

conn_handle = None
value = ""
name = "ESP32-Jassi" #Name of Your ESP32 (Change it to avoid Confusion)
ble = bluetooth.BLE()

ble.active(False)
time.sleep(0.5)
ble.active(True)
ble.config(gap_name=name)

service_UUID = bluetooth.UUID("6e400001-b5a3-f393-e0a9-e50e24dcca9e")
char_UUID = bluetooth.UUID("6e400002-b5a3-f393-e0a9-e50e24dcca9e")

char = (char_UUID, bluetooth.FLAG_READ | bluetooth.FLAG_NOTIFY)
service = (service_UUID, (char,),)
((char_handle,),) = ble.gatts_register_services((service,))

def event_occured(event, data):
    
    global conn_handle 

    if event == 1:
        conn_handle = data[0]
        print("Connected")
        
    elif event == 2:
        conn_handle = None
        print("Disconnected")
        advertise(name)
                  

def advertise(device_name):
    
    name_bytes = device_name.encode()

    flags = bytearray([0x02, 0x01, 0x06])
    short_name = bytearray([len(name_bytes) + 1, 0x08]) + name_bytes
    full_name = bytearray([len(name_bytes) + 1, 0x09]) + name_bytes
    adv_data = flags + short_name + full_name

    ble.gap_advertise(50, adv_data=adv_data)
    print("Awating Connection...Advertising as:", device_name)

advertise(name)

ble.irq(event_occured)

while True:
    #Generating Sensor values(just as an example) using Random
    sensor_value = random.randint(0, 100)
    print("Generated :", sensor_value)
    
    # Update characteristic value
    ble.gatts_write(char_handle, str(sensor_value))
    
    if conn_handle is not None:
        ble.gatts_notify(conn_handle, char_handle)

2.
import network
import socket

# ---------- ACCESS POINT SETUP ----------
ap = network.WLAN(network.AP_IF)
ap.active(True)
ap.config(essid='Jameel Jamali', password='08112401')  # min 8 chars

print("Access Point Active")
print("Connect to WiFi: ESP32-WiFi")
print("IP Address:", ap.ifconfig()[0])

# ---------- SOCKET SERVER ----------
addr = socket.getaddrinfo('0.0.0.0', 80)[0][-1]
server = socket.socket()
server.bind(addr)
server.listen(1)

print("Web server running...")

# ---------- HTML PAGE ----------
html = """<!DOCTYPE html>
<html>
<head>
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Chicken Biryani</title>
<style>
body {
  margin: 0;
  font-family: Arial, sans-serif;
  background: #f4f4f4;
  color: #333;
}
.container {
  max-width: 600px;
  margin: 20px auto;
  padding: 15px;
  background: #fff;
  border-radius: 8px;
}
h1 {
  font-size: 22px;
  margin-bottom: 10px;
}
p {
  font-size: 14px;
  line-height: 1.6;
}
</style>
</head>
<body>
<div class="container">
  <h1>Chicken Biryani</h1>
  <p>
    Chicken biryani is one of the most loved dishes in many parts of the world,
    especially in South Asia. It is a flavorful rice dish made by combining
    fragrant basmati rice with marinated chicken, spices, and herbs. The rich
    aroma comes from ingredients like saffron, cardamom, cloves, and fried onions,
    which give the dish its unique taste and character.
  </p>
  <p>
    What makes chicken biryani special is the layering and slow cooking process.
    The chicken is cooked with spices, and then partially cooked rice is layered
    over it. This mixture is then sealed and cooked on low heat, allowing the
    flavors to blend perfectly. Each grain of rice absorbs the essence of the
    spices and the chicken, creating a balanced and delicious meal.
  </p>
  <p>
    Chicken biryani is not just food; it is an experience. It is often served
    during celebrations, family gatherings, and special occasions. Its rich taste,
    comforting warmth, and cultural significance make it a timeless dish enjoyed
    by people of all ages.
  </p>
</div>
</body>
</html>
"""

while True:
    conn, addr = server.accept()
    print("Client connected from", addr)

    request = conn.recv(1024)  # receive request (not used here)

    conn.send("HTTP/1.1 200 OK\r\n")
    conn.send("Content-Type: text/html\r\n")
    conn.send("Connection: close\r\n\r\n")
    conn.sendall(html)

    conn.close()

3.
import network
import socket
from machine import Pin

# ---------- LED SETUP ----------
led = Pin(2, Pin.OUT)

# ---------- ACCESS POINT ----------
ap = network.WLAN(network.AP_IF)
ap.active(True)
ap.config(essid='ESP32 Jameel Jamali', password='12345678')

print("Connect to WiFi: ESP32 Jameel Jamali")
print("IP Address:", ap.ifconfig()[0])


# ---------- HTML PAGE ----------
def webpage():
    html = """<!DOCTYPE html>
<html>
<head>
    <title>ESP32 LED Control</title>
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <style>
        body {
            font-family: Arial;
            text-align: center;
            background: #0f2027;
            color: white;
            padding: 40px;
        }
        button {
            padding: 15px 30px;
            font-size: 18px;
            margin: 10px;
            border: none;
            border-radius: 10px;
        }
        .on { background: #00c853; color: white; }
        .off { background: #d50000; color: white; }
    </style>
</head>
<body>
    <h1> ESP32 LED Control</h1>
    <p>Control the LED using WiFi</p>
    <a href="/on"><button class="on">ON</button></a>
    <a href="/off"><button class="off">OFF</button></a>
</body>
</html>
"""
    return html


# ---------- SOCKET SERVER ----------
addr = socket.getaddrinfo('0.0.0.0', 80)[0][-1]

server = socket.socket()
server.bind(addr)
server.listen(1)

print("Server running...")

while True:
    conn, addr = server.accept()
    print("Client connected:", addr)

    request = conn.recv(1024)
    request = str(request)

    # ---------- HANDLE REQUEST ----------
    if '/on' in request:
        print("LED ON")
        led.value(1)

    if '/off' in request:
        print("LED OFF")
        led.value(0)

    # ---------- SEND RESPONSE ----------
    response = webpage()

    conn.send("HTTP/1.1 200 OK\r\n")
    conn.send("Content-Type: text/html\r\n")
    conn.send("Connection: close\r\n\r\n")
    conn.sendall(response)

    conn.close()


    time.sleep(1)
