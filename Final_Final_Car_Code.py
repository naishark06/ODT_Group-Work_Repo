from machine import Pin, PWM, time_pulse_us
import network
import socket
import time
import select

# ---------------- MOTOR PINS ----------------
LF_fwd = Pin(32, Pin.OUT)
LF_back = Pin(33, Pin.OUT)

LB_fwd = Pin(25, Pin.OUT)
LB_back = Pin(26, Pin.OUT)

RF_fwd = Pin(18, Pin.OUT)
RF_back = Pin(19, Pin.OUT)

RB_fwd = Pin(21, Pin.OUT)
RB_back = Pin(22, Pin.OUT)

# ---------------- PWM ----------------
ena_left = PWM(Pin(23), freq=1000)
enb_left = PWM(Pin(5), freq=1000)

ena_right = PWM(Pin(15), freq=1000)
enb_right = PWM(Pin(2), freq=1000)

SPEED = 1000

# ---------------- LEDS ----------------
led1 = Pin(13, Pin.OUT)
led2 = Pin(12, Pin.OUT)
led3 = Pin(14, Pin.OUT)
led4 = Pin(27, Pin.OUT)

leds = [led1, led2, led3, led4]

# ---------------- BUZZER ----------------
buzzer = Pin(4, Pin.OUT)

# ---------------- ULTRASONIC ----------------
trig = Pin(17, Pin.OUT)
echo = Pin(34, Pin.IN)

# ---------------- HELPERS ----------------
def all_leds_off():
    for led in leds:
        led.off()

def all_leds_on():
    for led in leds:
        led.on()

def stop():
    ena_left.duty(0)
    enb_left.duty(0)
    ena_right.duty(0)
    enb_right.duty(0)

    for p in [LF_fwd, LF_back, LB_fwd, LB_back,
              RF_fwd, RF_back, RB_fwd, RB_back]:
        p.value(0)

    all_leds_on()
    time.sleep(0.2)
    all_leds_off()
    buzzer.off()

# ---------------- SMOOTH START ----------------
def ramp_up():
    enb_left.duty(700)
    enb_right.duty(700)
    time.sleep(0.08)

    ena_left.duty(700)
    ena_right.duty(700)
    time.sleep(0.08)

    for sp in range(700, SPEED, 60):
        ena_left.duty(sp)
        enb_left.duty(sp)
        ena_right.duty(sp)
        enb_right.duty(sp)
        time.sleep(0.015)

# ---------------- INDICATORS ----------------
def left_indicator():
    for led in reversed(leds):
        all_leds_off()
        led.on()
        time.sleep(0.05)

def right_indicator():
    for led in leds:
        all_leds_off()
        led.on()
        time.sleep(0.05)

# ---------------- DISTANCE ----------------
def get_distance():
    trig.off()
    time.sleep_us(2)
    trig.on()
    time.sleep_us(10)
    trig.off()

    duration = time_pulse_us(echo, 1, 30000)

    if duration <= 0:
        return 100

    distance = (duration / 2) / 29.1

    if distance < 2 or distance > 400:
        return 100

    return distance

# ---------------- BUZZER ----------------
last_beep = 0

def parking_buzzer(distance):
    global last_beep

    now = time.ticks_ms()

    if distance > 15:
        interval = 800
    elif distance > 10:
        interval = 400
    elif distance > 5:
        interval = 200
    else:
        buzzer.on()
        return

    if time.ticks_diff(now, last_beep) > interval:
        buzzer.on()
        time.sleep(0.03)
        buzzer.off()
        last_beep = now

# ---------------- REVERSE LED BLINK ----------------
last_led_toggle = 0
led_state = False

def reverse_led_blink():
    global last_led_toggle, led_state

    now = time.ticks_ms()

    if time.ticks_diff(now, last_led_toggle) > 300:
        led_state = not led_state

        for led in leds:
            led.value(led_state)

        last_led_toggle = now

# ---------------- MOVEMENT ----------------
def forward():
    buzzer.off()
    all_leds_off()

    LF_fwd.value(1); LF_back.value(0)
    LB_fwd.value(1); LB_back.value(0)
    RF_fwd.value(1); RF_back.value(0)
    RB_fwd.value(1); RB_back.value(0)

    ramp_up()

def backward():
    LF_fwd.value(0); LF_back.value(1)
    LB_fwd.value(0); LB_back.value(1)
    RF_fwd.value(0); RF_back.value(1)
    RB_fwd.value(0); RB_back.value(1)

    ena_left.duty(SPEED)
    enb_left.duty(SPEED)
    ena_right.duty(SPEED)
    enb_right.duty(SPEED)

def left():
    left_indicator()
    LF_fwd.value(0); LF_back.value(1)
    LB_fwd.value(0); LB_back.value(1)
    RF_fwd.value(1); RF_back.value(0)
    RB_fwd.value(1); RB_back.value(0)
    ramp_up()

def right():
    right_indicator()
    LF_fwd.value(1); LF_back.value(0)
    LB_fwd.value(1); LB_back.value(0)
    RF_fwd.value(0); RF_back.value(1)
    RB_fwd.value(0); RB_back.value(1)
    ramp_up()

# ---------------- WIFI ----------------
ap = network.WLAN(network.AP_IF)
ap.active(True)
ap.config(essid='CarESP32', password='12345678')

s = socket.socket()
s.bind(('', 80))
s.listen(5)

print("WiFi: CarESP32")
print("IP: 192.168.4.1")

mode = "STOP"

# ---------------- MAIN LOOP ----------------
while True:
    r, _, _ = select.select([s], [], [], 0.01)

    if r:
        conn, addr = s.accept()
        request = conn.recv(1024).decode()

        if "GET /F" in request:
            mode = "FORWARD"
        elif "GET /B" in request:
            mode = "BACKWARD"
        elif "GET /L" in request:
            mode = "LEFT"
        elif "GET /R" in request:
            mode = "RIGHT"
        elif "GET /S" in request:
            mode = "STOP"

        conn.send("HTTP/1.1 200 OK\r\n\r\nOK")
        conn.close()

    # ---------------- CONTROL ----------------
    if mode == "FORWARD":
        forward()

    elif mode == "BACKWARD":
        backward()
        dist = get_distance()
        print(dist)
        parking_buzzer(dist)
        reverse_led_blink()

    elif mode == "LEFT":
        left()
        buzzer.off()

    elif mode == "RIGHT":
        right()
        buzzer.off()

    elif mode == "STOP":
        stop()
