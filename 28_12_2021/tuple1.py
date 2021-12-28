#Write a Python program to create a tuple with numbers and print one item

'''
user=1,2,3,5---(1,2,3,5)
if user=1 ---(1,) tuple typle

'''
class Tup:
    def __init__(self):
        pass
    def tup(self,tup1):
        tup2=[]
        for x in tup1.split(","):
            if x =='':
                pass
            else:
                try:
                    tup2.append(int(x))
                except:
                    tup2.append(x)
        print(tuple(tup2))



list1=Tup()
user=input("enter cama-seperated tuple elements  :")
list1.tup(user)