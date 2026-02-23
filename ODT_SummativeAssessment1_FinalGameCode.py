from machine import Pin, TouchPad, PWM
import time
import neopixel
import random

led1 = Pin(12,Pin.OUT)
led2 = Pin(14,Pin.OUT)
led3 = Pin(27,Pin.OUT)
leds = [led1, led2, led3]

pb = Pin(25, Pin.IN, Pin.PULL_UP)
np = neopixel.NeoPixel(Pin(21),16)

buzzer = PWM(Pin(18))
buzzer.duty(0)
def play_tone(freq, duration):
    buzzer.freq(freq)
    buzzer.duty(512)  # 50% volume
    time.sleep(duration)
    buzzer.duty(0)
    time.sleep(0.05)

def play_tune(tune):
    for freq, dur in tune:
        play_tone(freq, dur)

# Winning melody (rising happy sound)
WIN_TUNE = [
    (784, 0.12),   # G5
    (988, 0.12),   # B5
    (1175, 0.15),  # D6
    (1568, 0.2),   # G6
    (1318, 0.15),  # E6
    (1568, 0.4),   # G6 hold
    (2093, 0.6)    # C7 BIG finish
]
# Losing melody (dramatic falling sound)
LOSE_TUNE = [
    (1046, 0.25),  # C6
    (880, 0.25),   # A5
    (784, 0.3),    # G5
    (698, 0.3),    # F5
    (659, 0.35),   # E5
    (587, 0.4),    # D5
    (523, 0.5),    # C5
    (415, 0.7),    # G#4 (darker tone)
    (392, 1.2)     # G4 long dramatic fall
]

wire = TouchPad(Pin(4))
IRsensor = Pin(32, Pin.IN, Pin.PULL_UP)

while True:
    lives = 3
    win = 0 #dont question it, it makes sense later on in the code :D
    pb_value = pb.value()
    time.sleep(0.1)
    led1.off()
    led2.off()
    led3.off()
    for a in range (0,16,1):
        np[a] = (0,0,0)
        np.write()
    while pb.value() == 1: #ur skipping the naming ceremony and seeing value (skip the shenanigans)
        print("Ready Steady Po!")
        while lives > 0 and win == 0: #this is where it makes sense, to prevent this loop from running unnecesarily, youve added a win condition also
            pb_value = pb.value()
            wire_value = wire.read()
            print(wire_value)
            IRsensor_value = IRsensor.value()
            time.sleep(0.1)
            if wire.read() < 400: #losing code cuz capacitance dipped
                time.sleep(0.1)
                lives = lives-1
                leds[lives].on() #3-1 = 2 so led[2] will switch off which on the list is the 3rd led
                play_tune([(400,0.15),(250,0.2)])  # quick hurt sound
                print("Oops! You lost a life!")
                time.sleep(1)
                if lives == 0: #all lives damar
                    play_tune(LOSE_TUNE)
                    print("HA LOSER, KILL YOURSELF!")
                    time.sleep(1)
            if IRsensor_value == 0: #omg they came to the end
                for a in range (0,16,1): #it goes one circle and stops
                    r = random.randint(0,255)
                    g = random.randint(0,255)
                    b = random.randint(0,255)
                    np[a] = (r,g,b) #can we add a random here hmmmm
                    time.sleep(0.1)
                    np.write()                        
                play_tune(WIN_TUNE)
                print("Yay! You Won!")
                time.sleep(1)
                win = 1 #see now the condition on top where "win == 0" wont be true anymore and the loop wont run infinitely like one gandu
            #interrupts the game nvm the no. of lives left
            if pb_value == 0:
                print("Lets Start Again!")
                time.sleep(1)
                break #leaves while lives > 0
            #resets the game after win/lose
            #yay code finish
