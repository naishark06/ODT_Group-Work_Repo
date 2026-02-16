27. PWM in Servo Motors using lists
  from machine import Pin, PWM
  import time
  
  Duty_Value = [35, 55, 85, 110]
  servo = PWM(Pin(18))
  servo.freq(50)
  while True:
      for a in Duty_Value:
          servo.duty(a)
          time.sleep(0.5)

28. List in a List
  my_list = [[12,56,34,54],[13,65,34,67],[56,45,23,76]]
  for i in my_list:
      print(i)
      for k in i:
          print(k)

29. "break" to stop a loop from running
  from machine import Pin
  import time
  import neopixel
  
  np = neopixel.NeoPixel(Pin(4),16)
  pb = Pin(14, Pin.IN, Pin.PULL_UP)
  
  while True:
      pb_val = pb.value()
      if pb_val == 0:
          for i in range(0,16,1):
              pb_val = pb.value()
              if pb_val == 0:
                  break (this will break the "for" loop since "if" is not a "loop" but it is a "conditional statement")
              np[i]=(255,0,0)
              np.write()
              time.sleep(0.1)
      time.sleep(0.2)

30. Light up LED sequentially using lists
  from machine import Pin
  import time
  
  t = 0.2
  led1 = Pin(12, Pin.OUT)
  led2 = Pin(14, Pin.OUT)
  led3 = Pin(27, Pin.OUT)
  led4 = Pin(26, Pin.OUT)
  
  my_list = [[1,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,1]]
  
  while True:
      for i in my_list:
          led1.value(i[0])
          led2.value(i[1])
          led3.value(i[2])
          led4.value(i[3])
          time.sleep(t)    

31. Step-Up Motor (Wave Drive)
  from machine import Pin
  import time
  
  in1 = Pin(5, Pin.OUT)
  in2 = Pin(18, Pin.OUT)
  in3 = Pin(19, Pin.OUT)
  in4 = Pin(21, Pin.OUT)
  t = 2
  
  while True:
      in1.value(1)
      in2.value(0)
      in3.value(0)
      in4.value(0)
      time.sleep_ms(t)
      
      in1.value(0)
      in2.value(1)
      in3.value(0)
      in4.value(0)
      time.sleep_ms(t)
      
      in1.value(0)
      in2.value(0)
      in3.value(1)
      in4.value(0)
      time.sleep_ms(t)
      
      in1.value(0)
      in2.value(0)
      in3.value(0)
      in4.value(1)
      time.sleep_ms(t)

32. Step-Up Motor (Full Step)
  from machine import Pin
  import time
    
  in1 = Pin(5, Pin.OUT)
  in2 = Pin(18, Pin.OUT)
  in3 = Pin(19, Pin.OUT)
  in4 = Pin(21, Pin.OUT)
  t = 2
    
  while True:
      in1.value(1)
      in2.value(1)
      in3.value(0)
      in4.value(0)
      time.sleep_ms(t)
        
      in1.value(0)
      in2.value(1)
      in3.value(1)
      in4.value(0)
      time.sleep_ms(t)
        
      in1.value(0)
      in2.value(0)
      in3.value(1)
      in4.value(1)
      time.sleep_ms(t)
        
      in1.value(1)
      in2.value(0)
      in3.value(0)
      in4.value(1)
      time.sleep_ms(t)

33. Step-Up Motor (Half Step)
  from machine import Pin
  import time
    
  in1 = Pin(5, Pin.OUT)
  in2 = Pin(18, Pin.OUT)
  in3 = Pin(19, Pin.OUT)
  in4 = Pin(21, Pin.OUT)
  t = 2
    
  while True:
      #Step1
      in1.value(1)
      in2.value(1)
      in3.value(0)
      in4.value(0)
      time.sleep_ms(t)
      #Step2 
      in1.value(0)
      in2.value(1)
      in3.value(0)
      in4.value(0)
      time.sleep_ms(t)
      #Step3
      in1.value(0)
      in2.value(1)
      in3.value(1)
      in4.value(0)
      time.sleep_ms(t)
      #Step4
      in1.value(0)
      in2.value(0)
      in3.value(1)
      in4.value(0)
      time.sleep_ms(t)
      #Step5
      in1.value(0)
      in2.value(0)
      in3.value(1)
      in4.value(1)
      time.sleep_ms(t)
      #Step6
      in1.value(0)
      in2.value(0)
      in3.value(0)
      in4.value(1)
      time.sleep_ms(t)
      #Step7
      in1.value(1)
      in2.value(0)
      in3.value(0)
      in4.value(1)
      time.sleep_ms(t)
      #Step8
      in1.value(1)
      in2.value(0)
      in3.value(0)
      in4.value(0)
      time.sleep_ms(t)

34. Step-Up Motor (Full Step with Lists)
