1. 
import time
while True:
    t1= time.time()
    print(t1)
    time.sleep(4)
    t2= time.time()
    print(t2)
    T=t2-t1
    print(T)
    time.sleep(1)
  
2. 
import time
t1= time.ticks_ms()
print(t1)
time.sleep(2)
t2= time.ticks_ms()
print(t2)
T=t2-t1
print(T)

3.
import time
from machine import Pin
import random

led = Pin(4, Pin.OUT)
pb = Pin(32, Pin.IN, Pin.PULL_UP)

while True:
    t = random.randint(0,5)
    print(t)
    led.value(0)
    time.sleep(t)
    led.value(1)
    t1= time.ticks_ms()
    print("Start time:", t1)

    while pb.value()==1:
        t2 = time.ticks_ms()
    print("End time:",  t2)
    led.value(0)

    T= time.ticks_diff(t2,t1)
    print("Reaction Time:", T)
    time.sleep(1)

4.
import time
import random

t1= time.ticks_ms()
print("Yazhini", "Yazhini","Yazhini","Yazhini","Yazhini","Yazhini","Yazhini","Yazhini","Yazhini","Yazhini")
print("Time taken without for loop:", t1)
time.sleep(1)

print("Yazhini")
for a in range (0,10,1):
    t2= time.ticks_ms()
    print ("Time taken with for loop:", t2)
    time.sleep(1)
    
T = time.ticks_diff(t2,t1)
print("Time difference:", T)
time.sleep(1)

5.
#ultrasound sensor code

import time
from machine import Pin, time_pulse_us

trig = Pin(32, Pin.OUT)
echo = Pin(14, Pin.IN)

while True:
    trig.off()
    time.sleep_us(2)
    trig.on()
    time.sleep_us(10)
    trig.off()
    
    duration = time_pulse_us(echo,1,30000)
    
    if duration < 0:
        print("No object ditected")
        
    else:
        distance = duration / 58
        print("Distance", distance, "cm")
        
    time.sleep(1)

6.
#DC motor code

from machine import Pin, PWM
import time

IN1 = Pin(13, Pin.OUT)
IN2 = Pin(12, Pin.OUT)
ENA = PWM(Pin(15))
ENA.freq(1000)

 while True:
    ENA.duty(1000)
    IN1.value(1)
    IN2.value(0)
    time.sleep(3)
    ENA.duty(1000)
    IN1.value(0)
    IN2.value(1)
    time.sleep(3)
  
7.


