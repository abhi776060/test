'''
storing funcion reference to object
then calling a function
'''
import logging
logging.basicConfig(filename='test1.txt',filemode='a',level=logging.INFO)
def function():
    logging.info('function calling by its refernece :abhishek')
greeting=function
print(greeting())