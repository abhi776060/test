#Write a Python program to add an item in a tuple
'''
input:
  (1 2 3 4 5)    add 6
  output:
  (1 2 3 4 5 6)
'''


class Tup:
    def __init__(self,tup):
        self.tup=tup
    def add(self,num):
            tup1 = list(self.tup)
            tup1.append(num)
            print(tup1)

tuple1=Tup((1,2,3,5))
x=input(" enter adding elements ;")
try:
    tuple1.add(int(x))
except Exception as e:

    tuple1.add(x)
except :
    print("you can add one elements at a time")