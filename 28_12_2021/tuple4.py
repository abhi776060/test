# Write a Python program to convert a tuple to a string
'''
input:                            input:
( 1 2 3 4 5 6)                    ('a','b','h','i')
output:                            output:
'123456'                            'abhi'


( 1 2 3 4 5 6)
output:
'123456'
'''
class Tup:
    def __init__(self):
        pass


    def convert(self,tup):
        str1=''
        for x in tup:
            str1+=str(x)
        print(str1)

tuple1=Tup()
tuple1.convert( ('a','b','h','i'))