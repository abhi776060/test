#Write a Python program to unpack a tuple in several variables
'''
input:
( 1 2 3 4,,,,,,,)
output :
 a=1 b= 2 c=3 d=4,,,,,,,,,,,,
'''
class Tup:
    def __init__(self):
        pass

    def unpack(self,tup1):
        dict1={}
        for x in range(len(tup1)):
            dict1[f'a{x+1}']=tup1[x]
        for x,y in dict1.items():
            print(f'{x}={y}')


tuple1=Tup()
tuple1.unpack((1,2,3,4))