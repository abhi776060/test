#Find the size of a Tuple in Python
'''
Tuple1 = ("A", 1, "B", 2, "C", 3)
Size of Tuple1: 72bytes
'''
class String:
    def __init__(self):
        pass

    def size(self,tup):
        print(f"size of tuple is  {tup.__sizeof__()}bytes")


string=String()
string.size( ("A", 1, "B", 2, "C", 3))