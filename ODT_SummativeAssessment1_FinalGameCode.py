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

wire = TouchPad(Pin(4))
IRsensor = Pin(32, Pin.IN, Pin.PULL_UP)

while True:
    lives = 3
    win = 0 #dont question it, it makes sense later on in the code :D
    pb_value = pb.value()
    time.sleep(0.1)
    led1.on()
    led2.on()
    led3.on()
    for a in range (0,16,1):
        np[a] = (0,0,0)
        np.write()
    while pb.value() == 1: #ur skipping the naming ceremony and seeing value (skip the shenanigans)
        print("Let's Begin!")
        while lives > 0 and win == 0: #this is where it makes sense, to prevent this loop from running unnecesarily, youve added a win condition also
            pb_value = pb.value()
            wire_value = wire.read()
            print(wire_value)
            IRsensor_value = IRsensor.value()
            time.sleep(0.1)
            if wire.read() < 400: #losing code cuz capacitance dipped
                time.sleep(0.1)
                lives = lives-1
                leds[lives].off() #3-1 = 2 so led[2] will switch off which on the list is the 3rd led
                buzzer.duty(100)
                buzzer.freq(2)
                time.sleep(1)
                buzzer.duty(0)
                print("Oops! You lost a life!")
                if lives == 0: #all lives damar
                    buzzer.duty(100)
                    buzzer.freq(50) #tune for losing
                    time.sleep(1)
                    buzzer.duty(0)
                    print("Oh No! You Lost! Better Luck Next Time!")
            if IRsensor_value == 0: #omg they came to the end
                for a in range (0,16,1): #it goes one circle and stops
                    r = random.randint(0,255)
                    g = random.randint(0,255)
                    b = random.randint(0,255)
                    np[a] = (r,g,b) #can we add a random here hmmmm
                    time.sleep(0.1)
                    np.write()                        
                buzzer.duty(100)
                buzzer.freq(10) #tune for winning yay
                time.sleep(2)
                for a in range (0,16,1):#after they won little bit shut up and switch off
                    np[a] = (0,0,0)
                    np.write()
                print("Yay! You Won!")
                buzzer.duty(0)
                win = 1 #see now the condition on top where "win == 0" wont be true anymore and the loop wont run infinitely like one gandu
            #interrupts the game nvm the no. of lives left
            if pb_value == 0:
                print("Lets Start Again!")
                break #leaves while lives > 0
            #resets the game after win/lose
            #yay code finish
