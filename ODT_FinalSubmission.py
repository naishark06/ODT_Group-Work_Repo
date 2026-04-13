1. Car Indicator Lights:

  from machine import Pin
  import time
  light1 = Pin(2, Pin.OUT)
  light2 = Pin(4, Pin.OUT)
  light3 = Pin(5, Pin.OUT)
  light4 = Pin(19, Pin.OUT)
  PB1 = Pin(12, Pin.IN, Pin.PULL_UP)
  PB2 = Pin(14, Pin.IN, Pin.PULL_UP)
  while True:
      PB1_value = PB1.value()
      print(PB1_value)
      PB2_value = PB2.value()
      print(PB2_value)
      time.sleep(0.1)
      light1.on()
      light2.on()
      light3.on()
      light4.on()
      time.sleep(0.1)
      if PB1_value == 0 :
          light1.on()
          time.sleep(0.1)
          light1.off()
          light2.on()
          time.sleep(0.1)
          light2.off()
          light3.on()
          time.sleep(0.1)
          light3.off()
          light4.on()
          time.sleep(0.1)
          light4.off()
      if PB2_value == 0 :
          light4.on()
          time.sleep(0.1)
          light4.off()
          light3.on()
          time.sleep(0.1)
          light3.off()
          light2.on()
          time.sleep(0.1)
          light2.off()
          light1.on()
          time.sleep(0.1)
          light1.off()
          time.sleep(0.1)

2. Car Crash Detection:
from machine import Pin, time_pulse_us
import time

# Ultrasonic sensor pins
trig = Pin(5, Pin.OUT)
echo = Pin(18, Pin.IN)

# Motor control pins 
motor1 = Pin(22, Pin.OUT)
motor2 = Pin(23, Pin.OUT)

# Buzzer
buzzer = Pin(15, Pin.OUT)

def get_distance():
    # Send trigger pulse
    trig.off()
    time.sleep_us(2)
    trig.on()
    time.sleep_us(10)
    trig.off()

    # Measure echo time
    duration = time_pulse_us(echo, 1)

    # Convert to distance (cm)
    distance = (duration / 2) / 29.1
    return distance

def move_forward():
    motor1.on()
    motor2.on()

def stop():
    motor1.off()
    motor2.off()

while True:
    dist = get_distance()
    print("Distance:", dist)

    if dist <= 5:
        stop()
        buzzer.on()
        time.sleep(3)
        buzzer.off()
    else:
        move_forward()

    time.sleep(0.1)

3. Making car move:

from machine import Pin
import network
import socket
import time

# Motor pins (change if needed)
motor1_fwd = Pin(22, Pin.OUT)
motor1_back = Pin(23, Pin.OUT)
motor2_fwd = Pin(19, Pin.OUT)
motor2_back = Pin(21, Pin.OUT)

# WiFi setup (ESP32 as hotspot)
ssid = 'CarESP32'
password = '12345678'

ap = network.WLAN(network.AP_IF)
ap.active(True)
ap.config(essid=ssid, password=password)

# Create socket server
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('', 80))
s.listen(5)

def stop():
    motor1_fwd.off()
    motor1_back.off()
    motor2_fwd.off()
    motor2_back.off()

def forward():
    motor1_fwd.on()
    motor1_back.off()
    motor2_fwd.on()
    motor2_back.off()

def backward():
    motor1_fwd.off()
    motor1_back.on()
    motor2_fwd.off()
    motor2_back.on()

def left():
    # turn left (approx 45°)
    motor1_back.on()
    motor2_fwd.on()
    time.sleep(0.3)
    stop()

def right():
    # turn right (approx 45°)
    motor1_fwd.on()
    motor2_back.on()
    time.sleep(0.3)
    stop()

while True:
    conn, addr = s.accept()
    request = conn.recv(1024).decode()

    if '/F' in request:
        forward()
    elif '/B' in request:
        backward()
    elif '/L' in request:
        left()
    elif '/R' in request:
        right()
    elif '/S' in request:
        stop()

    conn.send('OK')
    conn.close()
