from threading import Thread
from time import sleep

def fun1():
    for x in range(10):
        print("hai")
        sleep(1)

def fun2():
    for x in range(10):
        print("abhi")
        sleep(1)

t1=Thread(target=fun1)
t2=Thread(target=fun2)

t1.start()
sleep(.2)
t2.start()

t1.join()
t2.join()
