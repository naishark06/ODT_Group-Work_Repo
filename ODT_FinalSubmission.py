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

4. Making eyes move
from machine import Pin, PWM
import time

# Setup servos
servo_left = PWM(Pin(13), freq=50)
servo_right = PWM(Pin(12), freq=50)

# Convert angle (0–180) to duty
def set_angle(servo, angle):
    duty = int(40 + (angle / 180) * 75)
    servo.duty(duty)

# Smooth movement function
def move_eyes_smooth(target_left, target_right):
    for i in range(10):  # smaller steps = smoother motion
        current_left = 70 + (target_left - 70) * i / 10
        current_right = 110 + (target_right - 110) * i / 10
        
        set_angle(servo_left, current_left)
        set_angle(servo_right, current_right)
        
        time.sleep(0.05)  # controls speed (increase = slower)

# Eye positions
def eyes_forward():
    move_eyes_smooth(70, 110)

def eyes_left():
    move_eyes_smooth(40, 80)

def eyes_right():
    move_eyes_smooth(100, 140)

def eyes_stop():
    set_angle(servo_left, 70)
    set_angle(servo_right, 110)
  
def forward():
    motor1_fwd.on()
    motor2_fwd.on()
    eyes_forward()

def backward():
    motor1_back.on()
    motor2_back.on()
    eyes_forward()

def left():
    motor1_back.on()
    motor2_fwd.on()
    eyes_left()
    time.sleep(0.3)
    stop()

def right():
    motor1_fwd.on()
    motor2_back.on()
    eyes_right()
    time.sleep(0.3)
    stop()

def stop():
    motor1_fwd.off()
    motor1_back.off()
    motor2_fwd.off()
    motor2_back.off()
    eyes_stop()
  
time.sleep(0.05)




5. Overall Code:

from machine import Pin, PWM, time_pulse_us
import network
import socket
import time

# ---------------- LED INDICATORS ----------------
light1 = Pin(2, Pin.OUT)
light2 = Pin(4, Pin.OUT)
light3 = Pin(16, Pin.OUT)   
light4 = Pin(19, Pin.OUT)

# ---------------- MOTORS ----------------
motor1_fwd = Pin(22, Pin.OUT)
motor1_back = Pin(23, Pin.OUT)
motor2_fwd = Pin(18, Pin.OUT)
motor2_back = Pin(21, Pin.OUT)

# ---------------- ULTRASONIC ----------------
trig = Pin(5, Pin.OUT)
echo = Pin(17, Pin.IN)

# ---------------- BUZZER ----------------
buzzer = Pin(15, Pin.OUT)

# ---------------- SERVOS ----------------
servo_left = PWM(Pin(13), freq=50)
servo_right = PWM(Pin(12), freq=50)

# ---------------- WIFI ----------------
ap = network.WLAN(network.AP_IF)
ap.active(True)
ap.config(essid='CarESP32', password='12345678')

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('', 80))
s.listen(5)

# ---------------- ULTRASONIC ----------------
def get_distance():
    trig.off()
    time.sleep_us(2)
    trig.on()
    time.sleep_us(10)
    trig.off()
    duration = time_pulse_us(echo, 1)
    return (duration / 2) / 29.1

# ---------------- BUZZER ----------------
def alert():
    buzzer.on()
    time.sleep(3)
    buzzer.off()

# ---------------- LED PATTERNS ----------------
def indicator_left():
    light1.on(); time.sleep(0.1); light1.off()
    light2.on(); time.sleep(0.1); light2.off()
    light3.on(); time.sleep(0.1); light3.off()
    light4.on(); time.sleep(0.1); light4.off()

def indicator_right():
    light4.on(); time.sleep(0.1); light4.off()
    light3.on(); time.sleep(0.1); light3.off()
    light2.on(); time.sleep(0.1); light2.off()
    light1.on(); time.sleep(0.1); light1.off()

# ---------------- SERVO ----------------
def set_angle(servo, angle):
    duty = int(40 + (angle / 180) * 75)
    servo.duty(duty)

def move_eyes_smooth(target_l, target_r):
    for i in range(10):
        l = 70 + (target_l - 70) * i / 10
        r = 110 + (target_r - 110) * i / 10
        set_angle(servo_left, l)
        set_angle(servo_right, r)
        time.sleep(0.05)

def eyes_forward():
    move_eyes_smooth(70, 110)

def eyes_left():
    move_eyes_smooth(40, 80)

def eyes_right():
    move_eyes_smooth(100, 140)

def eyes_stop():
    set_angle(servo_left, 70)
    set_angle(servo_right, 110)

# ---------------- MOVEMENT ----------------
def stop():
    motor1_fwd.off(); motor1_back.off()
    motor2_fwd.off(); motor2_back.off()
    eyes_stop()

def forward():
    if get_distance() <= 5:
        stop()
        alert()
        return
    motor1_fwd.on(); motor1_back.off()
    motor2_fwd.on(); motor2_back.off()
    eyes_forward()

def backward():
    motor1_fwd.off(); motor1_back.on()
    motor2_fwd.off(); motor2_back.on()
    eyes_forward()

def left():
    indicator_left()
    motor1_back.on(); motor2_fwd.on()
    eyes_left()
    time.sleep(0.3)
    stop()

def right():
    indicator_right()
    motor1_fwd.on(); motor2_back.on()
    eyes_right()
    time.sleep(0.3)
    stop()

# ---------------- MAIN LOOP ----------------
print("Connect to WiFi: CarESP32")

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
    elif '/IL' in request:
        indicator_left()
    elif '/IR' in request:
        indicator_right()

    conn.send('OK')
    conn.close()
