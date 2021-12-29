#How to Print Multiple Arguments in Python
'''
inputs:'abhishek',26
output:Abhishek is 26 years old boy
'''
import logging
logging.basicConfig(filename="test1.txt",filemode="a",level=logging.INFO)
class Function:
    def __init__(self):
        pass

    def display(self,name,age):
        logging.info(f'{name} is {age} years old boy')

my_function=Function()
my_function.display("abhishek",26)
my_function.display("vishnu",25)
