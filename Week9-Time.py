35. Print the absolute time
  import time
  while True:
      absolute = time.time()
      print (absolute)
      time.sleep(1)
36. Print 2 values of absolute time and the difference between each
  import time
  from machine import Pin
  led = Pin(4, Pin.OUT)
  t1 = time.time()
  print(t1)
  time.sleep(3)
  print ("This statement is used as a filler")
  led.on()
  time.sleep(3)
  led.off()
  t2 = time.time()
  print(t2)
  time.sleep(0.1)
  T = t2-t1
  print(T,"seconds")
37. Using time.ticks_ms() (relative time) repeat the above codes
  import time
  t1 = time.ticks_ms()
  print (t1)
38. Print difference using time.ticks_ms()
  import time
  t1 = time.ticks_ms()
  print (t1)
  time.sleep(3)
  t2 = time.ticks_ms()
  print (t2)
  T = t2-t1
  print(T)
39. Calculate time difference between a for loop and without a for loop
  import time
  print("This is the time using a for loop")
  t1 = time.ticks_ms()
  print(t1)
  for a in range (0,10,1):
      print("Naisha")
  t2 = time.ticks_ms()
  print(t2)
  T1 = time.ticks_diff(t2,t1)
  print(T1, "miliseconds. With a for loop")
  
  print("This is the time without for loop")
  t3 = time.ticks_ms()
  print(t3)
  
  print("Naisha")
  print("Naisha")
  print("Naisha")
  print("Naisha")
  print("Naisha")
  print("Naisha")
  print("Naisha")
  print("Naisha")
  print("Naisha")
  print("Naisha")
  
  t4 = time.ticks_ms()
  print(t4)
  T2 = time.ticks_diff(t4, t3)
  print (T2, "miliseconds. Without a for loop")
  Difference = time.ticks_diff(T2, T1)
  print (Difference, "miliseconds. The total difference with a for loop and without a for loop")
40. Reaction Time Test
  import time
  from machine import Pin
  import random
  pb = Pin(32, Pin.IN, Pin.PULL_UP)
  led = Pin(4, Pin.OUT)
  
  while True:
      R = random.randint(0,5)
      print(R)
      led.value(0)
      time.sleep(R)
      led.value(1)
      start = time.ticks_ms()
      print(start)
      while pb.value() == 1:
          stop = time.ticks_ms()
      led.value(0)
      Time = time.ticks_diff(stop,start)
      print(Time, "miliseconds. This is your reaction time")
      time.sleep(1)
41. Ultrasound Sensor Code (Object distance measurement)
  from machine import Pin, time_pulse_us
  import time
  trig = Pin(32, Pin.OUT)
  echo = Pin(14, Pin.IN)
  
  while True:
      trig.off()
      time.sleep_us(2)
      trig.on()
      time.sleep(10)
      trig.off
      duration = time_pulse_us(echo 1, 30000)
      if duration<0:
          print("No object detected (Timeout)")
      else:
          distance = duration / 58
          print("Distance:", distance, "cm")
      time.sleep(1)
42. DC Motor
  from machine import Pin, PWM
  import time
  
  IN1 = Pin(13, Pin.OUT)
  IN2 = Pin(12, Pin.OUT)
  ENA = PWM(Pin(15))
  ENA.freq(1000)
  pb1 = Pin(4, Pin.IN, Pin.PULL_UP)
  pb2 = Pin(5, Pin.IN, Pin.PULL_UP)
  
  if pb1.value() == 0:
    ENA.duty(1000)
    IN1.value(1)
    IN2.value(0)
    time.sleep(3)
  if pb2.value() == 0:
    ENA.duty(1000)
    IN1.value(0)
    IN2.value(1)
    time.sleep(3)
