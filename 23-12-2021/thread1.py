from threading import Thread
from time import sleep

class hi(Thread):
	def run(self):
		for i in range(20):
			print("hi")
			sleep(1)


class hello(Thread):
	def run(self):
		for i in range(20):
			print("hello")
			sleep(1)
t1=hi()
t2=hello()

t1.start()
sleep(0.2)
t2.start()

t1.join()
t2.join()

print('bye')
