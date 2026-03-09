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

