17. Lists and Appends
  lists = ['a','b','c','d','e','f']
  print(lists)
  LISTS = lists.append('g ')
  print(lists)

18. Using Lists and random in neopixel
  from machine import Pin
  import time
  import neopixel
  import random
  
  np = neopixel.NeoPixel(Pin(18),16) 
  
  color = [(255,0,0),(0,255,0),(0,0,255),(255,255,0),(0,255,255),(255,0,255),(255,255,255)]
  
  while True:
      a = random.randint(0,6)
      for z in range(0,16,2):
          np[z] = color[a]
          np.write()
          time.sleep(0.1)
      b = random.randint(0,6)
      for y in range(1,16,2):
          np[y] = color[b]
          np.write()
          time.sleep(0.1)

19. Randomising RGB values using lists also
  from machine import Pin
  import time
  import neopixel
  import random
  
  np = neopixel.NeoPixel(Pin(18),16)
  
  while True:
      r = random.randint(0,255)
      g = random.randint(0,255)
      b = random.randint(0,255)
      for i in range(0,16,2):
          np[i] = (r,g,b)
          np.write()
          time.sleep(0.1)
      R = random.randint(0,255)
      G = random.randint(0,255)
      B = random.randint(0,255)
      for e in range(1,16,2):
          np[e] = (R,G,B)
          np.write()
          time.sleep(0.1)

20. elif function
  x = 25
  if x>0 and x<2:
      print("Yo")
  elif x>4 and x<6:
      print("Hello!")
  elif x>6 and x<8:
      print("Namaste!")
  else:
      print("Bye!")

21. Using PushButtons to add increments to numbers
  from machine import Pin
  import time
  
  pb = Pin(12, Pin.IN, Pin.PULL_UP)
  x = 0
  while x<5:
      pb_value = pb.value()
      if pb_value == 0:
          x = (x+1)
          print(x)
          time.sleep(0.5)
      if x>=5:
          x = 0

22. Lighting up the neopixel according to the above code
  from machine import Pin
  import time
  import neopixel
  
  np = neopixel.NeoPixel(Pin(18),16)
  pb = Pin(12, Pin.IN, Pin.PULL_UP)
  PB = Pin(14,Pin.IN,Pin.PULL_UP)
  x = 0
  
  while x<16:
      np[x] = (0,0,0)
      np.write()
      pb_value = pb.value()
      PB_value = PB.value()
      print(PB_value)
      time.sleep(0.2)
      if pb_value == 0:
          np[x] = (255,255,255)
          np.write()
          x = (x+1)
          print(x)
          time.sleep(0.1)
      if PB_value == 0:
          for a in range (0,16,1):
              np[a] = (0,0,0)
              np.write()
          x = 0

23. Lighting up neopixel using above code and also switching it off in reverse
  from machine import Pin
  import time
  import neopixel
  
  np = neopixel.NeoPixel(Pin(18),16)
  pb = Pin(12, Pin.IN, Pin.PULL_UP)
  PB = Pin(14,Pin.IN,Pin.PULL_UP)
  x = 0
  
  while x<16:
      np[x] = (0,0,0)
      np.write()
      pb_value = pb.value()
      PB_value = PB.value()
      time.sleep(0.2)
      if pb_value == 0:
          np[x] = (255,255,255)
          np.write()
          x = (x+1)
          print(x)
          time.sleep(0.1)
      if PB_value == 0:
          np[x] = (0,0,0)
          np.write()
          x = (x-1)
          print(x)
          time.sleep(0.1)

24. Servo Motor (start at duty35 and go to duty77)
  from machine import Pin, PWM
  import time
  
  servo = PWM(Pin(18))
  while True:
      servo.freq(50)
      servo.duty(35)
      time.sleep(0.5)
      servo.duty(77)
      time.sleep(0.5)

25. Make the servo motor oscillate
  from machine import Pin, PWM
  import time
  
  servo = PWM(Pin(18))
  servo.freq(50)
  while True:
      for k in range (35,110,5):
          servo.duty(k)
          time.sleep(0.2)
      for m in range (110,35,-5):
          servo.duty(m)
          time.sleep(0.2)

26. PWM in buzzers
  from machine import Pin,PWM
  import time
  
  buzzer = PWM(Pin(18))
  buzzer.duty(100)
  x = 1
  
  while True:
      buzzer.freq(x)
      time.sleep(1)
      x = x+1

ACTIVITY: Using PWM make a tune on your buzzer (can use AI)
~MARIO THEME~
  from machine import Pin, PWM
  import time
  buzzer = PWM(Pin(18))
  buzzer.duty(400)
  
  TEMPO = 0.95 
  E7 = 2637
  C7 = 2093
  G7 = 3136
  G6 = 1568
  E6 = 1319
  A6 = 1760
  B6 = 1976
  AS6 = 1865
  F7 = 2794
  D7 = 2349
  A7 = 3520
  
  mario = [
      (E7, 0.15), (E7, 0.15), (0, 0.10),
      (E7, 0.15), (0, 0.10),
      (C7, 0.15), (E7, 0.15), (0, 0.10),
      (G7, 0.30), (0, 0.20),
      (G6, 0.30), (0, 0.20),
  
      (C7, 0.25), (0, 0.10),
      (G6, 0.25), (0, 0.10),
      (E6, 0.25), (0, 0.10),
      (A6, 0.15), (0, 0.05),
      (B6, 0.15), (0, 0.05),
      (AS6, 0.15),
      (A6, 0.25),
  
      (G6, 0.20),
      (E7, 0.20),
      (G7, 0.20),
      (A7, 0.25),
      (F7, 0.15), (G7, 0.15),
      (0, 0.10),
      (E7, 0.15),
      (C7, 0.15),
      (D7, 0.15),
      (B6, 0.30),
  ]
  def play(note, duration):
      if note == 0:
          buzzer.duty(0)
      else:
          buzzer.freq(note)
          buzzer.duty(512)
      time.sleep(duration * TEMPO)
      buzzer.duty(0)
      time.sleep(0.01 * TEMPO)  # tight gap = authentic feel
  
  for note, length in mario:
      play(note, length)

buzzer.deinit()
