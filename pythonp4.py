import threading
import time 


def koko():
    for x in range(0,150):
            time.sleep(0.1)
            print(x)
            if x == 50:
                break
        
def space():
    for x in range(0,150):
            time.sleep(0.1)
            print(x)
            if x == 100:
                break
        
def pro():
    for x in range(0,150):
            time.sleep(0.1)
            print(x)
            if x == 150:
                break
            
            
            
t1 = threading.Thread(target=koko)
t2 = threading.Thread(target=space)
t3 = threading.Thread(target=pro)

t1.start()
t2.start()
t3.start()

            