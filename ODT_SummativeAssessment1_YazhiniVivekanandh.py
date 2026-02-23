from machine import Pin, TouchPad, PWM
import time
import random
import neopixel

led1= Pin(12,Pin.OUT)
led2= Pin(14,Pin.OUT)
led3= Pin(27,Pin.OUT)
pb = Pin(25,Pin.IN, Pin.PULL_UP)
TP= TouchPad(Pin(4))
IRsensor = Pin(32, Pin.IN, Pin.PULL_UP)
leds = [led1,led2,led3]
buzzer = PWM(Pin(18))
buzzer.duty(0)
np = neopixel.NeoPixel(Pin(21),16)

while True:
    lives = 3
    win = 0
    TP_val = TP.read()
    pb_value = pb.value()
    time.sleep(0.1)
    led1.off()
    led2.off()
    led3.off()
    r = random.randint (0,255)
    g = random.randint (0,255)
    b = random.randint(0,255)
    for a in range (0,16,1):
        np[a] = (0,0,0)
        np.write()
    print(TP_val)
    time.sleep(0.1)
    while pb_value == 1:
        print("Ready Set Po!")
        while lives>0 and win == 0:
            IRsensor_val = IRsensor.value()
            time.sleep(0.1)
            pb_value = pb.value()
            TP_val = TP.read()
            print(TP_val)
            time.sleep(0.01)
            if TP_val < 400:
                lives = lives-1
                leds[lives].on()
                buzzer.duty(100)
                buzzer.freq(2)
                time.sleep(1)
                buzzer.duty(0)
                print("You Lost A Life!") 
                if lives == 0:
                    buzzer.duty(400)
                    buzzer.freq(100)
                    time.sleep(3)
                    buzzer.duty(0)
                    print("HA LOSER, KILL YOURSELF!")
            if IRsensor_val == 0:
                z= random.randint (0,6)
                for a in range (0,16,1):
                    np[a] = (r,g,b)
                    np.write()
                    time.sleep(0.1)
                buzzer.freq(5)
                buzzer.duty(100)
                time.sleep(2)
                print("YOU WON!!!")
                for a in range (0,16,1):
                    np[a] = (0,0,0)
                    np.write()
                    time.sleep(0.1)
                buzzer.duty(0)
                win = 1
            if pb_value == 0:
                break
